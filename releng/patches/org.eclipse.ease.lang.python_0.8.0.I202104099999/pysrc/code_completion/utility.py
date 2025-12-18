#################################################################################
# Copyright (c) 2017 Martin Kloesch and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# Contributors:
#     Martin Kloesch - initial API and implementation
#################################################################################
'''
Utility functions for code completion library.

:author: Martin Kloesch <martin.kloesch@gmail.com>
'''
import inspect
import keyword
import os
import re
import sys
import threading
from zipimport import zipimporter
import __main__
try:
    # Python 3.3+
    from importlib.machinery import all_suffixes
    _suffixes = all_suffixes()
except ImportError:
    # Fallback to Python < 3.3
    from imp import get_suffixes
    _suffixes = [s[0] for s in get_suffixes()]
try:
    # Python 3
    import builtins
    _builtins = vars(builtins)
except ImportError:
    # Python 2
    _builtins = __builtins__


#: Regular expression for package names.
#: Used to filter files that and folders that contain python modules.
_modulename_re = re.compile(r'(?P<name>[a-zA-Z_][a-zA-Z0-9_]*?)'
                            r'(?P<package>[/\\]__init__)?'
                            r'(?P<suffix>%s)$' %
                            r'|'.join(re.escape(s) for s in _suffixes))


#: Additional globals for test purposes.
#: Do not use in production.
_additional_globals = {}
def full_globals():
    '''
    Returns dictionary of all globally available variables.

    Fetches globals from:
        * keywords
        * :data:`__builtins__<_builtins>`
        * :mod:`__main__`

    Internally also uses :data:`_additional_globals` for test purposes.
    Do NOT! update this dictionary in production.

    :returns:   Dictionary with all global variables.
    :rtype:     dict<str, obj>
    '''
    g = {kw: None for kw in keyword.kwlist}
    g.update(_builtins)
    g.update(__main__.__dict__)
    g.update(_additional_globals)
    return g


def _find_modules(path):
    '''
    Lists all modules found at the given path.

    Checks (sub-)directories as well as zip files.

    :param path:    Path to search modules in.
    :type path:     str
    :returns:       set of modules found at given path.
    :rtype:         set<string>
    '''
    # If no path given use current working directory
    if not path:
        path = '.'

    # Try to search folder
    if os.path.isdir(path):
        files = []
        for root,  _,  nondirs in os.walk(path, followlinks=True):
            # Remove parent path to only get module name
            subdir = root[len(path) + 1:]

            # Check if subdirectories used -> submodules
            if subdir:
                files.extend(os.path.join(subdir, f) for f in nondirs)
            else:
                files.extend(nondirs)

    # Otherwise try if import from zip file (e.g. python egg)
    else:
        try:
            files = list(zipimporter(path)._files.keys())
        except:
            files = []

    # Actually match files to module names
    modules = []
    for f in files:
        m = _modulename_re.match(f)
        if m:
            modules.append(m.group('name'))

    return set(modules)


def modules(pattern=''):
    '''
    Lists all modules on Python path that start with given pattern.

    This only checks the cache so results might not match everything.
    Cache is filled asynchronously using :func:`_update_modules_cache`.

    :param pattern: Pattern for module name.
    :type pattern:  str
    :returns:       set of modules found.
    :rtype:         set<str>
    '''
    # Use all builtin modules
    modules = list(sys.builtin_module_names)

    # Use current working directory
    modules.extend(_find_modules('.'))

    # Trigger update of modules cache, might not be complete though
    _update_modules_cache()

    with _modules_lock:
        modules.extend(i for l in _modules_cache.values() for i in l)

    return set([module for module in modules if module.startswith(pattern)])


#: Simple cache for modules (takes long to parse)
_modules_cache = {}
_checked_paths = []
_modules_lock = threading.RLock()
def _update_modules_cache():
    '''
    Searches python search path for all modules and caches result.

    This function is called by :data:`_module_fetcher_thread` to
    increase performance.
    '''
    for path in sys.path:
        # Ignore current working directory (not cached)
        if path in ['', '.']:
            continue

        # Ignore already cached paths
        with _modules_lock:
            if path in _modules_cache:
                continue
            elif path in _checked_paths:
                continue
            else:
                _checked_paths.append(path)

        # Actually search path
        modules = _find_modules(path)
        try:
            modules.remove('__init__')
        except KeyError:
            pass

        with _modules_lock:
            _modules_cache[path] = modules


#: Thread for asynchronously searching all available modules.
#: Fetching modules takes a lot of time but can easily be cached.
_module_fetcher_thread = threading.Thread(target=_update_modules_cache)
_module_fetcher_thread.daemon = True


def is_importable(module, attr, only_modules):
    '''
    Checks if the given attribute is importable.

    :param module:  Module to import attribute from.
    :type module:   module
    :param attr:    Attribute to be imported.
    :type attr:     str
    :param only_modules:
        Flag to signalize if only submodules should be importable.
    :type only_modules: bool
    :returns:   ``True`` if importable.
    :rtype:     bool
    '''
    if only_modules:
        return inspect.ismodule(getattr(module, attr))
    else:
        return not (attr[:2] == '__' and attr[-2:] == '__')


def inspect_import(modulename, pattern='', only_modules=False):
    '''
    Searches submodules and objects in given module.

    Note that module will actually be imported so this
    has all the implications of importing a module.

    :param modulename:  Name of module to be imported.
    :type modulename:   str
    :param pattern:     Pattern to match submodules and objects against.
    :type pattern:      str
    :param only_modules:
        Flag to signalize if only submodules should be importable.
    :type only_modules: bool
    :returnsields:      Matching submodules or objects.
    :rtpye:             set<string>
    '''
    # Actually import the module
    try:
        m = __import__(modulename)
    except ImportError:
        return []

    # Get last submodule in module tree
    submodules = modulename.split('.')
    for module in submodules[1:]:
        m = getattr(m, module)

    completions = []

    # Check if file or module imported (__init__ means module)
    _is_module = hasattr(m, '__file__') and '__init__' in m.__file__

    # Import all attributes from module
    if not hasattr(m, '__file__') or not only_modules or _is_module:
        completions.extend(
            attr for attr in dir(m)
            if is_importable(m, attr, only_modules)
        )

    # Get submodules from file system
    if _is_module:
        completions.extend(_find_modules(os.path.dirname(m.__file__)))

    # Use __all__ attribute
    completions.extend(getattr(m, '__all__', []))

    # Remove duplicates
    completions = set(completions)
    completions.discard('__init__')
    completions = {
        completion for completion in completions
        if completion.startswith(pattern)
    }

    return completions


__all__ = ['full_globals', 'modules', 'is_importable', 'inspect_import']
