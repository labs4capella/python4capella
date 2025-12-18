###############################################################################
# Copyright (c) 2016 Kichwa Coders and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# Contributors:
#     Jonah Graham (Kichwa Coders) - initial API and implementation
###############################################################################
import sys as _pyease_sys
if __name__ == '__main__':
    # To be able to import all the py4j and related items, we need to add to the PYTHONPATH
    # all the correct paths. Because we may be launched with -E, the command line provides
    # all the paths to what we need.
    # sys.argv[1] - required - the port to conenct o
    # sys.argv[2:] - optional - paths to prepend on sys.path
    _pyease_sys.path[0:0] = _pyease_sys.argv[2:]

import code as _pyease_code
import os as _pyease_os
import py4j
from py4j.clientserver import ClientServer as _pyease_ClientServer
from py4j.clientserver import JavaParameters as _pyease_JavaParameters
from py4j.clientserver import PythonParameters as _pyease_PythonParameters
from py4j.java_collections import MapConverter as _pyease_MapConverter
from py4j.java_collections import ListConverter as _pyease_ListConverter
from py4j.java_collections import SetConverter as _pyease_SetConverter
from py4j.java_gateway import JavaObject as _pyease_JavaObject
from py4j.java_gateway import JavaClass as _pyease_JavaClass
from py4j.protocol import Py4JJavaError as _pyease_Py4JJavaError
import threading as _pyease_threading
import __main__
import ast as _pyease_ast
try:
    from six import integer_types as _pyease_integer_types
    from six import string_types as _pyease_string_types
except ImportError:
    if _pyease_sys.version_info.major == 2:
        _pyease_integer_types = (int, long)
        _pyease_string_types = (basestring,)
    else:
        _pyease_integer_types = (int,)
        _pyease_string_types = (str,)

# builtins used to set global variables
try:
    # Python 3.*
    import builtins as _pyease_builtins
except ImportError:
    # Python 2.*
    _pyease_builtins = __builtins__


def _pyease_patch_builtins(name, value):
    '''
    Patches Python builtins to make given value available as a builtin
    Python object in all modules.

    :param name:    Name of the builtin
    :type name:     str
    :param value:   Value for the builtin
    :type value:    object
    '''
    _pyease_builtins.__dict__.update({name: value})


# To ease some debugging of the py4j engine itself it is useful to turn logging on,
# uncomment the following lines for one way to do that
# import logging
# logger = logging.getLogger("py4j")
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())
def convert_value(
        value,
        gw=None,
        integer_types=_pyease_integer_types,
        string_types=_pyease_string_types,
        dict_types=dict,
        list_types=list,
        set_types=set):
    '''
    Tries to convert the given value using different strategies.

    Used because default py4j converters have some issues with e.g.
    nested collections.

    :param value:    Value to be converted.
    :param gw:       py4j gateway necessary for converters.
    '''
    if not gw:
        gw = gateway._gateway_client

    # None will be mapped to Java null
    if value is None:
        return value

    # Integers can be send directly
    if isinstance(value, integer_types):
        if (value > java.lang.Long.MAX_VALUE) or (value < java.lang.Long.MIN_VALUE):
            return java.math.BigInteger(str(value))

        return value

    # Floats can be send directly
    if isinstance(value, float):
        return value

    # Strings can be send directly
    if isinstance(value, string_types):
        return value

    # Recursively check collections
    if isinstance(value, dict_types):
        return _pyease_MapConverter().convert({
            convert_value(k, gw): convert_value(v, gw)
            for k, v in value.items()
        }, gw)
    if isinstance(value, list_types):
        return _pyease_ListConverter().convert([
            convert_value(v, gw) for v in value
        ], gw)
    if isinstance(value, set_types):
        return _pyease_SetConverter().convert({
            convert_value(v, gw) for v in value
        }, gw)

    # Try registered converters
    for converter in gw.converters:
        if converter.can_convert(value):
            try:
                return converter.convert(value, gw)
            except Exception:
                # TODO: Actually find out what this might throw
                pass

    # Issues with marshalling Java class objects
    if isinstance(value, _pyease_JavaClass):
        return repr(value)

    # Check if we have a Java object
    if isinstance(value, _pyease_JavaObject):
        return value

    # Check if we implement a Java interface
    if hasattr(value, 'Java') and hasattr(getattr(value, 'Java'), 'implements'):
        if hasattr(value, '_get_obj_id'):
            if callable(value._get_obj_id):
                return value
        else:
            # Issue with invalid implementations
            if hasattr(value, 'toString'):
                return value

    # Last resort use string representation
    return repr(value)

convert_value.__ease__ = True

class _pyease_EaseInteractiveConsole(_pyease_code.InteractiveConsole):
    '''
    Extension to standard InteractiveConsole so we can handle and capture
    error output better
    '''

    def __init__(self, engine, *args, **kwargs):
        _pyease_code.InteractiveConsole.__init__(self, *args, **kwargs)
        self.engine = engine

    def write(self, data):
        # Python 3 write the whole error in one write, Python 2 does multiple writes
        if self.engine.except_data is None:
            self.engine.except_data = [data]
        else:
            self.engine.except_data.append(data)

    def runcode(self, code, filename=None):
        filename = filename or '<...>'
        try:
            # If we have compiled code we cannot use AST
            if isinstance(code, _pyease_string_types):
                # Parse code input
                tree = _pyease_ast.parse(code)

                # Check if we have multiline statement
                if len(tree.body) > 1:
                    module = _pyease_ast.Module(tree.body[:-1], type_ignores=[])
                    compiled = compile(module, filename, 'exec')
                    exec(compiled, self.locals)

                # Check if at least one line given
                if len(tree.body):
                    if isinstance(tree.body[-1], _pyease_ast.Expr):
                        # Only expressions can be evaluated
                        expression = _pyease_ast.Expression(tree.body[-1].value)
                        compiled = compile(expression, filename, 'eval')
                        result = eval(compiled, self.locals)
                        return result, False
                    else:
                        module = _pyease_ast.Module([tree.body[-1]], type_ignores=[])
                        compiled = compile(module, filename, 'exec')
                        exec(compiled, self.locals)
            else:
                exec(code, self.locals)

        except SystemExit:
            raise
        except _pyease_Py4JJavaError as e:
            if isinstance(e.java_exception, _pyease_JavaObject):
                # Skip self.showtraceback/self.write as we can get
                # a Java exception instance already
                self.engine.except_data = e.java_exception
            else:
                # No java exception here, fallback to normal case
                self.showtraceback()
        except Exception:
            # create information that will end up in a
            # ScriptExecutionException
            self.showtraceback()

    def push(self, cmd, filename=None):
        return _pyease_code.InteractiveConsole.push(self, cmd)


# Sentinel object for no result (different than None)
_pyease_NO_RESULT = object()


class _pyease_InteractiveReturn(object):
    '''
    Instance of Java's IInteractiveReturn.
    This class encapsulates the return state from the
    ScriptEngineExecute.executeInteractive() method
    '''

    def __init__(self, gateway_client, display_data=None, except_data=None, result=_pyease_NO_RESULT):
        self.gateway_client = gateway_client
        self.display_data = display_data
        self.except_data = except_data
        self.result = result

    def getException(self):
        data = self.except_data
        if data is None:
            return None
        if isinstance(data, _pyease_JavaObject):
            return data
        return "".join(data)

    def getResult(self):
        # Check if we did not receive result
        if self.result is _pyease_NO_RESULT:
            data = self.display_data
        else:
            data = self.result

        # Use conversion just to be sure
        return convert_value(data, self.gateway_client)

    class Java:
        implements = ['org.eclipse.ease.lang.python.py4j.internal.IInteractiveReturn']


class _pyease_ScriptEngineExecute(object):
    '''
    Instance of Java's IPythonSideEngine.
    This class is the main class of the Python side.
    '''

    def __init__(self):
        self.shutdown_event = _pyease_threading.Event()

    def set_gateway(self, gateway):
        self.gateway = gateway
        self.locals = __main__.__dict__
        self.interp = _pyease_EaseInteractiveConsole(self, self.locals)
        # Provide most common top level pacakage names in the namespace
        # so that code like "java.lang.String()" can work.
        # for other names, jvm.<package name> should be used
        self.locals['java'] = gateway.jvm.java
        _pyease_patch_builtins('java', gateway.jvm.java)

        self.locals['javax'] = gateway.jvm.javax
        _pyease_patch_builtins('javax', gateway.jvm.javax)

        self.locals['org'] = gateway.jvm.org
        _pyease_patch_builtins('org', gateway.jvm.org)

        self.locals['com'] = gateway.jvm.com
        _pyease_patch_builtins('com', gateway.jvm.com)

        self.locals['net'] = gateway.jvm.net
        _pyease_patch_builtins('net', gateway.jvm.net)

        self.locals['jvm'] = gateway.jvm
        _pyease_patch_builtins('jvm', gateway.jvm.jvm)

        self.locals['gateway'] = gateway
        _pyease_patch_builtins('gateway', gateway)

        self.locals['py4j'] = py4j
        _pyease_patch_builtins('py4j', py4j)

        _pyease_sys.displayhook = self.displayhook
        self.display_data = None
        self.except_data = None

    def displayhook(self, data):
        self.display_data = data
        if data is not None:
            self.locals['_'] = data

    def executeCommon(self, code_text, code_exec, filename=None):
        self.display_data = None
        self.except_data = None
        execution_result = code_exec(code_text, filename)

        # Check if we received a tuple, meaning that we are in script mode 
        if isinstance(execution_result, tuple) and len(execution_result) == 2:
            result, needMore = execution_result
        else:
            # Set result to NO_RESULT to distinguish from None result
            result = _pyease_NO_RESULT
            needMore = execution_result

        if needMore:
            # TODO, need to handle this with prompts, this message
            # is a workaround
            return _pyease_InteractiveReturn(self.gateway._gateway_client, display_data="... - more input required to complete statement")
        else:
            display_data = self.display_data
            except_data = self.except_data
            self.display_data = None
            self.except_data = None
            return _pyease_InteractiveReturn(self.gateway._gateway_client, display_data=display_data, except_data=except_data, result=result)

    def executeScript(self, code_text, filename=None):
        return self.executeCommon(code_text, self.interp.runcode, filename)

    def executeInteractive(self, code_text):
        return self.executeCommon(code_text, self.interp.push)

    def internalGetVariable(self, name):
        return convert_value(self.locals.get(name), self.gateway._gateway_client)

    def internalGetVariables(self):
        # Filter out data we do not want
        filtered = {
            k: convert_value(v, self.gateway._gateway_client)
            for k, v in self.locals.items()
            if k.startswith('__EASE') or ((not k.startswith('__')) and (not k.startswith('_pyease_')) and (not v.__class__.__module__.startswith('py4j.')) and (not hasattr(v, '__ease__')) and (not v.__class__.__name__ == 'module'))
        }

        return _pyease_MapConverter().convert(filtered, self.gateway._gateway_client)

    def internalHasVariable(self, name):
        return name in self.locals

    def internalSetVariable(self, name, content):
        self.locals[name] = content
        _pyease_builtins.__dict__.update({name: content}) 

    def teardownEngine(self):
        self.shutdown_event.set()

    def wait_on_shutdown(self):
        self.shutdown_event.wait()

    def addSearchPath(self, path):
        _pyease_sys.path.append(path)

    class Java:
        implements = ['org.eclipse.ease.lang.python.py4j.internal.IPythonSideEngine']


def _pyease_watchdog(engine):
    # Read from the parent process until EOF, EOF indicates the
    # parent process has terminated
    try:
        _pyease_sys.stdin.read()
    except:
        pass

    # shutdown the engine
    engine.teardownEngine()

    # Allow some time for the shutdown to be clean, but
    # fallback to a hard exit if that fails
    timer = _pyease_threading.Timer(10.0, _pyease_os._exit, (1,))
    timer.daemon = True
    timer.start()


def _pyease_main(argv):
    port = int(argv[1])
    engine = _pyease_ScriptEngineExecute()
    # Bug 517528: Disable memory management until Py4J #275 is resolved
    enable_memory_management = True
    java_params = _pyease_JavaParameters(auto_convert=True, port=port,
                                 enable_memory_management=enable_memory_management)
    gateway = _pyease_ClientServer(java_parameters=java_params,
                          python_parameters=_pyease_PythonParameters(port=0),
                          python_server_entry_point=engine)
    # retrieve the port on which the python callback server was bound to.
    python_port = gateway.get_callback_server().get_listening_port()
    engine.set_gateway(gateway)

    # tell Java that we are up and running and where to direct
    # calls to python to.
    gateway.entry_point.pythonStartupComplete(python_port, engine)

    # start a watchdog on stdin to make sure we terminate
    thread = _pyease_threading.Thread(target=_pyease_watchdog, args=(engine,))
    thread.daemon = True
    thread.start()

    # now wait until we have a request for shutdown
    engine.wait_on_shutdown()

    gateway.shutdown_callback_server()
    gateway.shutdown()


if __name__ == '__main__':
    # Will be patched via builtins
    gateway = None
    _pyease_main(_pyease_sys.argv)
