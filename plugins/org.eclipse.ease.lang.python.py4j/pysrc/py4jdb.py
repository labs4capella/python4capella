'''
Copyright (c) 2018 Martin Kloesch
All rights reserved. This program and the accompanying materials
are made available under the terms of the Eclipse Public License v2.0
which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-2.0/

Contributors:
 * Martin Kloesch - initial API and implementation
'''

# Python std library imports
import ast as _pyease_ast
import bdb as _pyease_bdb
import functools as _pyease_functools
import re as _pyease_re
import sys as _pyease_sys
import threading as _pyease_threading

# : Regular expression if we are dealing with internal module.
_pyease_INTERNAL_CHECKER = _pyease_re.compile(r'^<.+>$')


class _pyease_PyFrame:
    '''
    Python implementation of IPyFrame used for exchanging frame data
    with eclipse.

    Simply wraps standard python frame to more easily usable format.

    Python frame documentation is available here:
    https://docs.python.org/3/reference/datamodel.html#types
    '''

    def __init__(self, frame):
        '''
        Constructor only stores frame to member.

        :param frame:    Python frame to be converted.
        '''
        self._frame = frame

    def _valid_frame(self):
        '''
        Utility method checking if the current frame is valid

        A frame is valid if all information is present and
        it's file is not ignored.

        :returns:    ``True`` if frame is valid.
        '''
        return self._frame and not _pyease_ignore_frame(self._frame)

    def getFilename(self):
        '''
        Returns the filename of the frame.

        If no frame was set, a dummy value will be returned.

        :returns:    Filename of frame or dummy value.
        '''
        if self._valid_frame():
            return self._frame.f_code.co_filename
        else:
            return '__no_frame__'

    def getLineNumber(self):
        '''
        Returns the linenumber of the frame.

        If no frame was set, -1 is returned.

        :returns:    Line number of frame or -1.
        '''
        if self._valid_frame():
            return self._frame.f_lineno
        else:
            return -1

    def getParent(self):
        '''
        Returns the parent of the frame.

        If no frame was set or the frame does not have a parent
        `None` is returned.

        :returns:    Parent frame in stack or `None`
        '''
        if self._valid_frame():
            return _pyease_PyFrame(self._frame.f_back)
        else:
            return None

    def getVariable(self, name):
        '''
        Get a variable from the current frame.

        :param: name:   variable name to look up
        :return:        variable or <code>null</code>
        '''
        if self._valid_frame():
            if name in self._frame.f_locals:
                return convert_value(self._frame.f_locals[name])

            if name in self._frame.f_globals:
                return convert_value(self._frame.f_globals[name])

        return None

    def getVariables(self):
        '''
        Get variables visible from current frame.

        :return:        variableName -> variableContent
        '''
        variables = {}
        if self._valid_frame():
            # TODO: Differentiate between global and local variables
            variables.update(self._frame.f_globals)
            variables.update(self._frame.f_locals)

        return convert_value(variables)

    def setVariable(self, name, value):
        '''
        Sets new value for a variable only if it exists.

        :param name:    Name of variable to be updated.
        :param value:   New value for variable.
        '''
        if self._valid_frame():
            if name in self._frame.f_locals:
                self._frame.f_locals[name] = value

            elif name in self._frame.f_globals:
                self._frame.f_globals[name] = value

    def toString(self):
        '''
        Required override to avoid problems in py4j bridge.
        '''
        return '{}: #{:d}'.format(self.getFilename(), self.getLineNumber())

    class Java:
        implements = ['org.eclipse.ease.lang.python.debugger.IPyFrame']


def _pyease_ignore_frame(frame, first=True):
    '''
    Utility to check if a frame should be ignored.

    Current reasons to ignore a frame:
        * It is the top entry of the stack and it is a standard module.
          e.g. <string>
        * It is part of the py4j library or has py4j in its call chain.

    Recursively checks trace until at bottom of stack.

    :param frame:    Frame to check if it should be ignored.
    :param first:    Flag to signalize if it is the first call.
    :returns:        `True` if the frame should be ignored.
    '''
    # End of frame
    if not frame:
        return False

    # ignore frames that originate from the self.run() method
    if first:
        if frame.f_code.co_filename == '(none)':
            return True

    # Check if we are in the standard modules
    if _pyease_INTERNAL_CHECKER.match(frame.f_code.co_filename):
        # Only ignore standard module if its the top of the stack
        return first

    # TODO: Think of better way to identify py4j library
    if 'py4j' in frame.f_code.co_filename.lower():
        return True

    return _pyease_ignore_frame(frame.f_back, False)


class _pyease_CodeTracer(_pyease_bdb.Bdb):
    '''
    Eclipse Debugger class.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor initializes instance variables.
        '''
        _pyease_bdb.Bdb.__init__(self, *args, **kwargs)

        # Debugger for communication with Java world
        self._debugger = None

        # Caches for currently executed code parts
        self._current_frame = None
        self._last_exception_frame = None
        self._current_file = None

        # Async continuation handling
        self._continue_event = _pyease_threading.Event()
        self._continue_func = lambda: None

        # TODO: Think about a better way to handle step return
        self._return_hack = False

    def getCurrentFrame(self):
        if self._current_frame is not None:
        	  return _pyease_PyFrame(self._current_frame)
        	  
        return None
    
    def getExceptionFrame(self):
        if self._last_exception_frame is not None:
        	  return _pyease_PyFrame(self._last_exception_frame)

        return None

    def setDebugger(self, debugger):
        '''
        Setter method for self._debugger.

        :param org.eclipse.ease.lang.python.debugger.PythonDebugger debugger:
            PythonDebugger object to handling communication with Eclipse.
        '''
        self._debugger = debugger

    def trace_dispatch(self, frame, event, arg):
        '''
        Called for every executed line of source code.

        Checks if line is of interest and dispatches the call for
        further investigation.

        :param frame:    Current stack frame.
        :param event:    Type of dispatch event that occurred.
        :param arg:      Optional argument for dispatching.
        '''
        # Pre-filter to avoid issues with library internals
        if not _pyease_ignore_frame(frame):
            self._current_frame = frame
            _pyease_bdb.Bdb.trace_dispatch(self, frame, event, arg)
        
        return self.trace_dispatch

    def user_line(self, frame):
        '''
        Called when debugger thinks line is of interest.

        :param frame:    Current stack frame with line.
        '''
        self._continue_func = self.set_continue
        self.dispatch(frame, 'line')

    def user_call(self, frame, argument_list):
        '''
        Called when debugger thinks call is of interest.

        :param frame:    Current stack frame with call information.
        :param argument_list:    ignored
        '''
        self.dispatch(frame, 'call')

    def user_return(self, frame, return_value):
        '''
        Called when debugger thinks returning from function is of interest.

        :param frame:    Current stack frame with return information.
        :param return_value:    ignored
        '''
        self._continue_func = self.set_step
        self.dispatch(frame, 'return')

    def dispatch_exception(self, frame, arg):
        if not frame.f_code.co_filename.endswith("bdb.py"):
            self._last_exception_frame = frame
        
        _pyease_bdb.Bdb.dispatch_exception(self, frame, arg)
        
    def user_exception(self, frame, exc_info):
        '''
        Called when debugger thinks thrown exception is of interest.

        :param frame:    Current stack frame with exception information.
        :param exc_info:    ignored
        '''

        self._continue_func = self.set_continue
        self.dispatch(frame, 'exception')

    def dispatch(self, frame, dispatch_type):
        '''
        Dispatches the given frame to the interested debugger.

        :param frame:    Current stack frame to be dispatched.
        :param dispatch_type:    Type of dispatch event (call, line, ...)
        '''
        if not self._debugger:
            return

        # Set up caches for asynchronous continuation
        self._current_frame = frame
        self._continue_event.set()

        # Check if we need to fake the current frame for Eclipse
        if self._return_hack:
            frame = frame.f_back
            self._return_hack = False

        # Dispatch call to Java
        self._debugger.traceDispatch(_pyease_PyFrame(frame), dispatch_type)

        # Make asynchronous call synchronous again
        self._continue_event.wait()
        self._continue_func()

    def suspend(self):
        '''
        Suspend the execution to wait for asynchronous callbacks
        from Java.
        '''
        self._continue_event.clear()

    def resume(self, resume_type):
        '''
        Resume execution by calling the given resume function.

        :param resume_type:    Desired resume function identifier.
        '''
        frame = self._current_frame

        # Step into
        if resume_type == 1:
            self._continue_func = self.set_step

        # Step over
        elif resume_type == 2:
            self._continue_func = _pyease_functools.partial(self.set_next, frame)

        # Step return
        elif resume_type == 4:
            self._return_hack = True
            self._continue_func = _pyease_functools.partial(self.set_return, frame)

        # Continue
        else:
            self._continue_func = self.set_continue

        self._continue_event.set()

    def set_continue(self):
        '''
        FIXME:  Override of bdb.Bdb.set_continue
                Original stops debugging when no more breakpoints in file.
                This means we cannot add breakpoints later on.
        '''
        self._set_stopinfo(self.botframe, None, -1)

    def setBreakpoint(self, breakpoint):
        '''
        Interface method for Java to have simpler method of setting
        a breakpoint.

        FIXME:  This is a copy of bdb.Bdb.set_break
                set_break performs OS level checks to see if file exists.

        :param breakpoint:    Breakpoint to be set.
        '''
        filename = self.canonic(breakpoint.getFilename())
        lineno = breakpoint.getLineno()

        if filename not in self.breaks:
            self.breaks[filename] = []
        linenos = self.breaks[filename]
        if lineno not in linenos:
            linenos .append(lineno)
        _pyease_bdb.Breakpoint(filename, lineno, 0, None, None)

    def removeBreakpoint(self, breakpoint):
        '''
        Interface method for Java to have simpler method of removing
        a breakpoint.

        :param breakpoint:    Breakpoint to be removed.
        '''
        filename = self.canonic(breakpoint.getFilename())
        lineno = breakpoint.getLineno()
        self.clear_break(filename, lineno)

    def stop_here(self, frame):
        '''
        Hijacks frame check to see if currently executed file has changed.

        If file changed new breakpoints will be loaded.

        :param frame:    Current stack frame to check for file change.
        '''
        if self._debugger:
            file = frame.f_code.co_filename
            if file != self._current_file:
                self._current_file = file
                self.clear_all_file_breaks(file)

                breakpoints = self._debugger.getBreakpoints(file)
                for breakpoint in breakpoints:
                    self.setBreakpoint(breakpoint)

                # If we have breakpoints we want to let the debugger know
                if breakpoints:
                    return True

        return _pyease_bdb.Bdb.stop_here(self, frame)

    def run(self, script, filename):
        '''
        Executes the script given using the bdb.Bdb.run method.

        :param script:    Script to be executed.
        :param filename:  Filename for easier identification of dynamic code.
        '''
        # Compile code for better inspection
        code = '{}\n'.format(script.getCode())
        ast_ = _pyease_ast.parse(code, filename, 'exec')
        final_expr = None
        for field_ in _pyease_ast.iter_fields(ast_):
            if 'body' != field_[0]:
                continue

            # Check if last item is an expression
            if len(field_[1]) > 0:
                if isinstance(field_[1][-1], _pyease_ast.Expr):
                    final_expr = _pyease_ast.Expression()
                    popped = field_[1].pop(-1)
                    final_expr.body = popped.value

        # Run code up to last expression
        return_value = None
        compiled = compile(ast_, filename, 'exec')
        _pyease_bdb.Bdb.run(self, compiled)
        self._keep_debugging()

        # Check if last expression still needs to be run
        if final_expr:
            compiled = compile(final_expr, filename, 'eval')
            return_value = self.runeval(compiled)
            self._keep_debugging()

        return return_value

    def _keep_debugging(self):
        '''
        Resets debugger state to be able to continue debugging after
        script injection.
        '''
        _pyease_sys.settrace(self.trace_dispatch)
        self.quitting = False

    def toString(self):
        '''
        Required override to avoid problems in py4j bridge.
        '''
        return str(self)

    def equals(self, other):
        '''
        Required override to avoid problems in py4j bridge.
        '''
        return self is other

    class Java:
        implements = ['org.eclipse.ease.lang.python.py4j.internal.ICodeTraceFilter']


# Set up connection between eclipse and python
_pyease_CodeTracer()