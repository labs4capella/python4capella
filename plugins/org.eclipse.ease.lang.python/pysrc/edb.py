'''
Copyright (c) 2014 Martin Kloesch
All rights reserved. This program and the accompanying materials
are made available under the terms of the Eclipse Public License v2.0
which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-2.0/

Contributors:
 * Martin Kloesch - initial API and implementation
 * Christian Pontesegger - stripped most parts to simply trace and relay to java
'''

# Python std library imports
import sys as _pyease_sys
import re as _pyease_re
import ast as _pyease_ast

# : Regular expression if we are dealing with internal module.
_pyease_INTERNAL_CHECKER = _pyease_re.compile(r"^<.+>$")


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
        
    def getFilename(self):
        '''
        Returns the filename of the frame.
        
        If no frame was set, a dummy value will be returned.
        
        :returns:    Filename of frame or dummy value.
        '''
        if self._frame:
            return self._frame.f_code.co_filename
        else:
            return "__no_frame__"
        
    def getLineNumber(self):
        '''
        Returns the linenumber of the frame.
        
        If no frame was set, -1 is returned.
        
        :returns:    Line number of frame or -1.
        '''
        if self._frame:
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
        if self._frame:
            return _pyease_PyFrame(self._frame.f_back)
        else:
            return None
    
    def getVariable(self, name):
        '''
        Get a variable from the current frame.
         
        :param: name:   variable name to look up
        :return:        variable or <code>null</code>
        '''
        if (self._frame):
            if name in self._frame.f_locals:
                return self._frame.f_locals[name]
            
            if name in self._frame.f_globals:
                return self._frame.f_globals[name]
            
        return None
    
    def getVariables(self):
        '''
        Get variables visible from current frame.
         
        :return:        variableName -> variableContent
        '''
        variables = {}
        if (self._frame):
            variables.update(self._frame.f_globals)
            variables.update(self._frame.f_locals)
            
        return variables
    
    def setVariable(self, name, value):
        if (self._frame):
            if name in self._frame.f_locals:
                self._frame.f_locals[name] = value
            
            elif name in self._frame.f_globals:
                self._frame.f_locals[name] = value
        
    def toString(self):
        return str(self.getFilename()) + ": #" + str(self.getLineNumber())
        
    class Java:
        implements = ['org.eclipse.ease.lang.python.debugger.IPyFrame']


class _pyease_CodeTracer:
    '''
    Eclipse Debugger class.
    '''
    _debugger = None
    _framework_variables = {}

    def __init__(self):
        _pyease_sys.settrace(self.trace_dispatch)         

    def set_debugger(self, debugger):
        '''
        Setter method for self._debugger.
        
        :param org.eclipse.ease.lang.python.debugger.PythonDebugger debugger:
            PythonDebugger object to handling communication with Eclipse.
        '''
        self._debugger = debugger
    
    def trace_dispatch(self, frame, event, arg):
        '''
        Method called each time a new frame is reached in execution.
        <p>
        Performs prefiltering and dispatches the data to Eclipse.
        
        :param frame:    New execution frame.
        :param event:    ignored.
        :param arg:      ignored.
        :see:            sys.settrace
        '''
        
        if not self.ignore_frame(frame):
            if self._debugger:
                if event == "return":
                    self._debugger.traceDispatch(_pyease_PyFrame(frame.f_back), event)
                else:
                    self._debugger.traceDispatch(_pyease_PyFrame(frame), event)
                
        return self.trace_dispatch
                
    def run(self, script, filename):
        '''
        Executes the file given using the bdb.Bdb.run method.
        '''
        code = "{}\n".format(script.getCode())

        ast_ = _pyease_ast.parse(code, filename, 'exec')
        final_expr = None
        for field_ in _pyease_ast.iter_fields(ast_):
            if 'body' != field_[0]:
                continue
            
            if len(field_[1]) > 0:
                if isinstance(field_[1][-1], _pyease_ast.Expr):
                    final_expr = _pyease_ast.Expression()
                    popped = field_[1].pop(len(field_[1]) - 1);  # Jython pop() will not accept -1 as parameter
                    final_expr.body = popped.value
        
        return_value = None
        exec(compile(ast_, filename, 'exec'), globals())
        if final_expr:
            return_value = eval(compile(final_expr, filename, 'eval'), None)
            
        return return_value
       
#        exec(compiledCode, g)

    def ignore_frame(self, frame, first=True):
        '''
        Utility method to check if a frame should be ignored.
    
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
            if frame.f_code.co_filename == "(none)":
                return True

        # Check if we are in the standard modules
        if _pyease_INTERNAL_CHECKER.match(frame.f_code.co_filename):
            # Only ignore standard module if its the top of the stack
            return first
        
        # TODO: Think of better way to identify py4j library
        if 'py4j' in frame.f_code.co_filename.lower():
            return True
    
        # Check parent in stack
        return self.ignore_frame(frame.f_back, False)
        
    class Java:
        implements = ['org.eclipse.ease.lang.python.debugger.ICodeTracer']


# Set up connection between eclipse and python
_pyease_eclipse_python_debugger = _pyease_CodeTracer()
_pyease_eclipse_python_debugger.set_debugger(_pyease_debugger)
_pyease_debugger.setCodeTracer(_pyease_eclipse_python_debugger)
