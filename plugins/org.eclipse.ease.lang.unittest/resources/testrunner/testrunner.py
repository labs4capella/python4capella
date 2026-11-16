import unittest
import warnings
import sys
import os
import re
from unittest.signals import registerResult

import eclipse.unittest as easeunit

class EASETestResult(unittest.result.TestResult):
    def __init__(self, stream, descriptions, verbosity):
        super(EASETestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions
              
    def startTest(self, test):
        super(EASETestResult, self).startTest(test)
        easeunit.startTest(test._testMethodName, test.shortDescription())
       
    def stopTest(self, test):
        easeunit.endTest()
 
    def addError(self, test, err):
        try:
            if (hasattr(err[1], 'java_exception')):
                if ("org.eclipse.ease.lang.unittest.AssertionException" == err[1].java_exception.getClass().getName()):
                    self.addFailure(test, (AssertionError, AssertionError(err[1].java_exception.getMessage()), err[2]))
                    return
        except:
            pass

        super(EASETestResult, self).addError(test, err)
        self.addTestResult(org.eclipse.ease.lang.unittest.runtime.TestStatus.ERROR, str(err[0].__name__) + ": " + str(err[1]), self._convert_stacktrace(err[2]))
 
    def addFailure(self, test, err):
        super(EASETestResult, self).addFailure(test, err)
        self.addTestResult(org.eclipse.ease.lang.unittest.runtime.TestStatus.FAILURE, str(err[1]), self._convert_stacktrace(err[2]))
   
    def addTestResult(self, type, message, stacktrace=None):
        result = org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory.eINSTANCE.createTestResult()
        result.setStatus(type);
        result.setMessage(message);
       
        try:
            if stacktrace:
                result.setStackTrace(stacktrace)
            else:
                result.setStackTrace(getScriptEngine().getStackTrace())
        except Exception:
            print("could not set stacktrace")
            pass
       
        easeunit.getTest().getResults().add(result);       
    
    def addSkip(self, test, reason):
        super(EASETestResult, self).addSkip(test, reason)
        self.addTestResult(org.eclipse.ease.lang.unittest.runtime.TestStatus.DISABLED, reason)
 
    def addUnexpectedSuccess(self, test):
        super(EASETestResult, self).addUnexpectedSuccess(test)
        self.addTestResult(org.eclipse.ease.lang.unittest.runtime.TestStatus.FAILURE, "We expected an error")

    def _convert_stacktrace(self, traceback):
        while traceback and self._is_relevant_tb_level(traceback):
            traceback = traceback.tb_next

        if not traceback:
            return None

        frame = traceback.tb_frame
        stacktrace = org.eclipse.ease.debugging.ScriptStackTrace()
        while frame:
            filename = frame.f_code.co_filename
            
            # Name mangled workspace file
            if re.match("^__ref_L/(.+)_[a-z]{10}$", filename):
                filename = filename[8:-11]
            
            # Simple workspace file
            elif filename.startswith("L/") and not os.path.exists(filename):
                filename = filename[2:]
            
            # Not a workspace file (so ignore)
            else:
                break
    
            # Convert to debug frame            
            path = org.eclipse.core.runtime.Path(filename)
            workspace = org.eclipse.core.resources.ResourcesPlugin.getWorkspace()
            file = workspace.getRoot().getFile(path)
            script = org.eclipse.ease.Script(filename, file, False)
            ease_frame = org.eclipse.ease.debugging.EaseDebugFrame(script, frame.f_lineno, 1, filename)
            stacktrace.add(ease_frame)
            
            # Check next entry in stacktrace
            frame = frame.f_back

        return stacktrace


class EASETestRunner(object):
    """A test runner class that cooperates with the Eclipse EASE framework.
    """
    resultclass = EASETestResult

    def __init__(self, stream=None, descriptions=True, verbosity=1,
                 failfast=False, buffer=False, resultclass=None, warnings=None):
        if stream is None:
            stream = sys.stderr
        
        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer
        self.warnings = warnings
        if resultclass is not None:
            self.resultclass = resultclass

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        with warnings.catch_warnings():
            if self.warnings:
                # if self.warnings is set, use it to filter all the warnings
                warnings.simplefilter(self.warnings)
                # if the filter is 'default' or 'always', special-case the
                # warnings from the deprecated unittest methods to show them
                # no more than once per module, because they can be fairly
                # noisy.  The -Wd and -Wa flags can be used to bypass this
                # only when self.warnings is None.
                if self.warnings in ['default', 'always']:
                    warnings.filterwarnings('module',
                            category=DeprecationWarning,
                            message='Please use assert\w+ instead.')
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
            try:
                test(result)
            finally:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
        result.printErrors()
        run = result.testsRun

        expectedFails = unexpectedSuccesses = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses,
                                result.skipped))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped = results

        infos = []
        return result

if __name__ == "__ease_unittest__":
    # Dynamically create test suite to combine test cases
    tests = unittest.TestLoader().loadTestsFromModule(sys.modules["__main__"])
    testSuite = unittest.TestSuite(tests)
    
    runner = EASETestRunner()
    runner.run(testSuite)
