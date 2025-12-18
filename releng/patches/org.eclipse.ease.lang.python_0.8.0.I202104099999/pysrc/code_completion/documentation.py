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
Documentation providers for code completion library

:author: Martin Kloesch <martin.kloesch@gmail.com>
'''
import pydoc
try:
    # Python >= 3.3
    from inspect import signature as _signature
except ImportError:
    # Python < 3.3
    import inspect

    def _signature(func):
        '''
        Backwards compatible implementation of :func:`inspect.signature`
        as this function is only available in Python >= 3.3.

        Uses :mod:`inspect` module to get arguments and formats this
        information in a way similar to the 3.3+ implementation.

        :param func:    Function to get signature for.
        :type func:     callable
        :returns:       Function signature (with brackets, without name)
        :rtype:         str
        '''
        argspec = inspect.getargspec(func)

        # Add all normal arguments
        argslist = argspec.args[:len(argspec.defaults or [])]

        # Add arguments with default values
        if argspec.defaults:
            argslist.extend(
                '{}={}'.format(k, v) for k, v in zip(
                    argspec.args[len(argspec.defaults):],
                    argspec.defaults
                )
            )

        # Add varargs
        if argspec.varargs:
            argslist.append('*{}'.format(argspec.varargs))

        # Add keywords
        if argspec.keywords:
            argslist.append('**{}'.format(argspec.keywords))

        return '({})'.format(', '.join(argslist))


class Documentation:
    '''
    Data-storage class for object documentation.

    Stores docstrings in different formats to be used in multiple
    applications.

    Current formats:
        * Plain text
        * HTML
    '''
    def __init__(self, plain, html=None):
        '''
        Constructor only stores parameters to members.

        :param plain:   Documentation as plaintext.
        :type plain:    str
        :param html:    Documentation in HTML format.
        :type html:     str
        '''
        self.plain = plain
        self.html = html or plain

    @classmethod
    def from_object(cls, object):
        '''
        Creates :class:`Documentation` object by inspecting
        a given object.

        :param object:  Object to get documentation for.
        '''
        plain = pydoc.getdoc(object)

        # try to add function signature
        if hasattr(object, '__name__'):
            try:
                plain = '{}{}\n{}'.format(
                    object.__name__,
                    _signature(object),
                    plain
                )
            except (ValueError, TypeError):
                # Ignore if no signature found
                pass

        # Create HTML documentation
        html = pydoc.HTMLDoc()
        try:
            object, name = pydoc.resolve(object)
        except ImportError:
            # Special case for string objects
            name = str(object)
        page = html.page(pydoc.describe(object), html.document(object, name))

        # Actually instantiate object
        return cls(plain, page)


__all__ = ['Documentation']
