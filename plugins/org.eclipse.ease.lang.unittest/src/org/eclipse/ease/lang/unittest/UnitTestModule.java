/*******************************************************************************
 * Copyright (c) 2017 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.unittest;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.lang.reflect.Method;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.ease.IDebugEngine;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Script;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ICode;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.reporters.IReportGenerator;
import org.eclipse.ease.lang.unittest.reporters.ReportTools;
import org.eclipse.ease.lang.unittest.runtime.IMetadata;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestClass;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestFile;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.IEnvironment;
import org.eclipse.ease.modules.IModuleCallbackProvider;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.ease.tools.ResourceTools;

/**
 * Support methods for scripted unit tests. Provides several assertion methods and utility functions to manipulate the current test instances and states.
 */
public class UnitTestModule extends AbstractScriptModule {

	private ITestClass fCurrentTestClass = null;
	private ITest fCurrentTest = null;
	private boolean fThrowOnFailure = false;

	@Override
	public void initialize(IScriptEngine engine, IEnvironment environment) {
		super.initialize(engine, environment);

		environment.addModuleCallback(new IModuleCallbackProvider() {

			@Override
			public void preExecutionCallback(Method method, Object[] parameters) {
			}

			@Override
			public void postExecutionCallback(Method method, Object result) {
				if (result instanceof IAssertion)
					assertion((IAssertion) result);
			}

			@Override
			public boolean hasPreExecutionCallback(Method method) {
				return false;
			}

			@Override
			public boolean hasPostExecutionCallback(Method method) {
				return IAssertion.class.isAssignableFrom(method.getReturnType());
			}
		});
	}

	/**
	 * Start a specific unit test. Started tests should be terminated by an {module #endTest()}.
	 *
	 * @param title
	 *            name of test
	 * @param description
	 *            short test description
	 */
	@WrapToScript
	public final void startTest(final String title, @ScriptParameter(defaultValue = "") final String description) {
		ITestContainer container = fCurrentTestClass;

		if (container == null) {
			final ITestFile testFile = getTestFile();
			if (testFile != null)
				container = testFile;
			else
				// temporary container to allow to run tests as normal scripts
				container = IRuntimeFactory.eINSTANCE.createTestFile();
		}

		fCurrentTest = IRuntimeFactory.eINSTANCE.createTest();
		fCurrentTest.setName(title);
		fCurrentTest.setDescription(description);
		fCurrentTest.setEntityStatus(TestStatus.RUNNING);

		if (getScriptEngine() instanceof IDebugEngine)
			fCurrentTest.setStackTrace(((IDebugEngine) getScriptEngine()).getStackTrace());

		container.getChildren().add(fCurrentTest);
	}

	/**
	 * End the current test. Does nothing if no test was started.
	 */
	@WrapToScript
	public final void endTest() {
		if (fCurrentTest != null) {
			fCurrentTest.setEntityStatus(TestStatus.PASS);
			fCurrentTest = null;
		}
	}

	/**
	 * Get the current test suite.
	 *
	 * @return test suite instance
	 */
	@WrapToScript
	public ITestSuite getTestSuite() {
		if (getTestFile() != null)
			return getTestFile().getTestSuite();

		final Object testSuite = getScriptEngine().getVariable(TestSuiteScriptEngine.TEST_SUITE_VARIABLE);
		return (testSuite instanceof ITestSuite) ? (ITestSuite) testSuite : null;
	}

	/**
	 * Get the currently executed test file instance. The test file is not a file instance but the runtime representation of a testsuite test file.
	 *
	 * @return test file instance
	 */
	@WrapToScript
	public ITestFile getTestFile() {
		final Object testFile = getScriptEngine().getVariable(TestSuiteScriptEngine.TEST_FILE_VARIABLE);
		return (testFile instanceof ITestFile) ? (ITestFile) testFile : null;
	}

	/**
	 * Append generic data to the current test, testfile or test suite.
	 *
	 * @param name
	 *            key to use. Has to be unique for this test object
	 * @param value
	 *            data to be stored
	 */
	@WrapToScript
	public void addMetaData(String name, Object value) {
		final IMetadata metadata = IRuntimeFactory.eINSTANCE.createMetadata();
		metadata.setKey(name);
		metadata.setValue(value);

		if (getScriptEngine() instanceof IDebugEngine)
			metadata.setStackTrace(((IDebugEngine) getScriptEngine()).getStackTrace());

		if (fCurrentTest != null)
			fCurrentTest.getMetadata().add(metadata);

		else if (getTestFile() != null)
			getTestFile().getMetadata().add(metadata);

		else if (getTestSuite() != null)
			getTestSuite().getMetadata().add(metadata);

		else
			throw new RuntimeException("No test entity availabe. Nowhere to store metadata to");
	}

	/**
	 * Expect two objects to be equal.
	 *
	 * @param expected
	 *            expected result
	 * @param actual
	 *            actual result
	 * @param errorDescription
	 *            optional error text to be displayed when not equal
	 * @return assertion containing comparison result
	 */
	@WrapToScript
	public static IAssertion assertEquals(final Object expected, final Object actual,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		if (expected != null)
			return new DefaultAssertion(expected.equals(actual),
					(errorDescription == null) ? "Objects do not match: expected <" + expected + ">, actual <" + actual + ">" : errorDescription.toString());

		return assertNull(actual, errorDescription);
	}

	/**
	 * Asserts when provided value does not match to a given regular expression pattern.
	 *
	 * @param pattern
	 *            pattern to match
	 * @param candidate
	 *            text to be matched
	 * @param errorMessage
	 *            error message in case of a mismatch
	 * @return assertion depending on <code>actual</code> value
	 */
	@WrapToScript
	public static IAssertion assertMatch(String pattern, String candidate, @ScriptParameter(defaultValue = ScriptParameter.NULL) String errorMessage) {
		if (Pattern.matches(pattern, candidate))
			return IAssertion.VALID;

		return new DefaultAssertion((errorMessage != null) ? errorMessage : "\"" + candidate + "\" does not match pattern \"" + pattern + "\"");
	}

	/**
	 * Expect two objects not to be equal.
	 *
	 * @param expected
	 *            unexpected result
	 * @param actual
	 *            actual result
	 * @param errorDescription
	 *            optional error text to be displayed when equal
	 * @return assertion containing comparison result
	 */
	@WrapToScript
	public static IAssertion assertNotEquals(final Object expected, final Object actual,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		if (expected != null)
			return new DefaultAssertion(!expected.equals(actual), (errorDescription == null) ? "Objects match" : errorDescription.toString());

		return assertNotNull(actual, errorDescription);
	}

	/**
	 * Asserts when provided value is not <code>null</code>.
	 *
	 * @param actual
	 *            value to verify
	 * @param errorDescription
	 *            optional error description
	 * @return assertion depending on <code>actual</code> value
	 */
	@WrapToScript
	public static IAssertion assertNull(final Object actual, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		return new DefaultAssertion(actual == null, (errorDescription == null) ? "Object is not null, actual <" + actual + ">" : errorDescription.toString());
	}

	/**
	 * Asserts when provided value is <code>null</code>.
	 *
	 * @param actual
	 *            value to verify
	 * @param errorDescription
	 *            optional error description
	 * @return assertion depending on <code>actual</code> value
	 */
	@WrapToScript
	public static IAssertion assertNotNull(final Object actual, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		return new DefaultAssertion(actual != null, (errorDescription == null) ? "Object is null" : errorDescription.toString());
	}

	/**
	 * Asserts when provided value is <code>false</code>.
	 *
	 * @param actual
	 *            value to verify
	 * @param errorDescription
	 *            optional error description
	 * @return assertion depending on <code>actual</code> value
	 */
	@WrapToScript
	public static IAssertion assertTrue(final Boolean actual, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		return new DefaultAssertion(actual, (errorDescription == null) ? "Value is false" : errorDescription.toString());
	}

	/**
	 * Asserts when provided value is <code>true</code>.
	 *
	 * @param actual
	 *            value to verify
	 * @param errorDescription
	 *            optional error description
	 * @return assertion depending on <code>actual</code> value
	 */
	@WrapToScript
	public static IAssertion assertFalse(final Boolean actual, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Object errorDescription) {
		return new DefaultAssertion(!actual, (errorDescription == null) ? "Value is true" : errorDescription.toString());
	}

	/**
	 * Changes behavior for assertion handling. By default assertions do not cause an exception to be thrown, which supports classic (functional) test mode.
	 * Object oriented test mode enhances exceptions to be thrown on assertions.
	 *
	 * @param throwOnFailure
	 *            <code>true</code> to thow exceptions on assertions
	 */
	public void setThrowOnFailure(boolean throwOnFailure) {
		fThrowOnFailure = throwOnFailure;
	}

	/**
	 * Create a new assertion for the current test. According to the assertion status an error might be added to the current testcase.
	 *
	 * @param reason
	 *            assertion to be checked
	 * @throws AssertionException
	 *             in case {@module #setThrowOnFailure(boolean)} is enabled
	 */
	@WrapToScript
	public final void assertion(final IAssertion reason) throws AssertionException {
		if (!reason.isValid()) {
			if (fThrowOnFailure)
				throw new AssertionException(reason.toString());
			else
				failure(reason.toString());
		}
	}

	/**
	 * Adds a new Testclass to the list of {@link ITestFile} in the Test. If testClass already exists, then it returns the first testNode with given className.
	 *
	 * @param className
	 *            Name of testClass
	 * @return {@link ITestContainer}
	 */
	public ITestContainer addTestClass(String className) {
		if (fCurrentTestClass != null) {
			fCurrentTestClass.setEntityStatus(TestStatus.FINISHED);
			fCurrentTestClass = null;
		}

		if (className != null) {
			final ITestFile testFile = getTestFile();
			final List<ITestEntity> duplicateClasses = testFile.getChildren().stream()
					.filter(p -> ITestClass.class.isAssignableFrom(p.getClass()) && p.getName().equals(className)).collect(Collectors.toList());

			if (duplicateClasses.isEmpty()) {
				fCurrentTestClass = IRuntimeFactory.eINSTANCE.createTestClass();
				fCurrentTestClass.setName(className);
			} else {
				fCurrentTestClass = (ITestClass) duplicateClasses.get(0);
			}

			fCurrentTestClass.setEntityStatus(TestStatus.RUNNING);

			if (getScriptEngine() instanceof IDebugEngine)
				fCurrentTestClass.setStackTrace(((IDebugEngine) getScriptEngine()).getStackTrace());

			testFile.getChildren().add(fCurrentTestClass);
		}

		return fCurrentTestClass;
	}

	/**
	 * Ignore the current test, the current testfile or test suite. What is ignored depends on the scope this command is executed in.
	 *
	 * @param reason
	 *            message why the test got ignored.
	 */
	@WrapToScript(alias = "ignoreTest")
	public void ignore(@ScriptParameter(defaultValue = "") String reason) {
		if (fCurrentTest != null)
			addResult(getTest(), TestStatus.DISABLED, reason, null);
		else if (getTestFile() != null)
			addResult(getTestFile(), TestStatus.DISABLED, reason, null);
		else if (getTestSuite() != null)
			addResult(getTestSuite(), TestStatus.DISABLED, reason, null);
	}

	/**
	 * Force a failure (=assertion) for the current test entity (test/testclass/testfile/testsuite).
	 *
	 * @param message
	 *            failure message
	 */
	@WrapToScript
	public void failure(String message) {
		failure(message, null);
	}

	/**
	 * Called from the javascript runner.
	 *
	 * @param message
	 *            failure message
	 * @param stackTrace
	 *            stacktrace of failure event
	 */
	public void failure(String message, ScriptStackTrace stackTrace) {
		final ITestSuiteDefinition definition = (getTestSuite() != null) ? getTestSuite().getDefinition() : null;
		if ((definition != null) && (definition.getFlag(Flag.PROMOTE_FAILURE_TO_ERROR, false)))
			error(message, stackTrace);
		else
			addResult(getTest(), TestStatus.FAILURE, message, stackTrace);
	}

	private void addResult(ITestEntity owner, TestStatus status, String message, ScriptStackTrace stackTrace) {
		final ITestResult result = IRuntimeFactory.eINSTANCE.createTestResult();
		result.setStatus(status);
		result.setMessage(message);

		if (stackTrace != null)
			result.setStackTrace(stackTrace);

		else if (getScriptEngine() instanceof IDebugEngine)
			result.setStackTrace(((IDebugEngine) getScriptEngine()).getStackTrace());

		owner.getResults().add(result);
	}

	/**
	 * Get the current unit test.
	 *
	 * @return the current test or a generic global test scope if called outside of a valid testcase
	 */
	@WrapToScript
	public ITest getTest() {
		if (fCurrentTest == null) {
			if (getTestFile() != null)
				return getTestFile().getTest(ITestEntity.GLOBAL_SCOPE_TEST);

			if (getTestSuite() != null)
				return getTestSuite().getTest(ITestEntity.GLOBAL_SCOPE_TEST);

			// executed outside of unit test framework, return dummy test instance
			return IRuntimeFactory.eINSTANCE.createTest();
		}

		return fCurrentTest;
	}

	/**
	 * Force an error for the current test entity (test/testclass/testfile/testsuite).
	 *
	 * @param message
	 *            error message
	 * @throws AssertionException
	 *             containing the provided message
	 */
	@WrapToScript
	public void error(String message) throws AssertionException {
		throw new AssertionException(message);
	}

	/**
	 * Called from the javascript runner.
	 *
	 * @param message
	 *            error message
	 * @param stackTrace
	 *            stacktrace of error event
	 */
	public void error(String message, ScriptStackTrace stackTrace) {
		addResult(getTest(), TestStatus.ERROR, message, stackTrace);
	}

	/**
	 * Set the timeout for the current test. If test execution takes longer than the timeout, the test is marked as failed.
	 *
	 * @param timeout
	 *            timeout in [ms]
	 */
	@WrapToScript
	public void setTestTimeout(long timeout) {
		if (fCurrentTest != null)
			getTest().setDurationLimit(timeout);
	}

	/**
	 * Execute code registered in the testsuite.
	 *
	 * @param location
	 *            name of the code fragment to execute.
	 * @return execution result
	 * @throws Exception
	 *             when no user specific code can be found or the injected code throws
	 */
	@WrapToScript
	public Object executeUserCode(String location) throws Exception {
		final ITestSuiteDefinition definition = (getTestSuite() != null) ? getTestSuite().getDefinition() : null;
		if (definition != null) {
			final ICode customCode = definition.getCustomCode(location);
			if (customCode != null)
				return getScriptEngine().inject(new Script(customCode.getLocation(), customCode.getContent()), false);
			else
				throw new Exception("No user specific code for \"" + location + "\" found.");

		} else
			throw new Exception("No user specific code for \"" + location + "\" found.");
	}

	/**
	 * Get a list of available test report types.
	 *
	 * @return String array containing available report types
	 */
	@WrapToScript
	public static String[] getReportTypes() {
		return ReportTools.getReportTemplates().toArray(new String[0]);
	}

	/**
	 * Create a test report file.
	 *
	 * @param reportType
	 *            type of report; see getReportTypes() for values
	 * @param suite
	 *            {@link ITestEntity} to be reported
	 * @param fileLocation
	 *            location where report should be stored
	 * @param title
	 *            report title
	 * @param description
	 *            report description (ignored by some reports)
	 * @param reportData
	 *            additional report data. Specific to report type
	 * @throws CoreException
	 *             when we could not write to a workspace file
	 * @throws IOException
	 *             when we could not write to the file system
	 */
	@WrapToScript
	public void createReport(final String reportType, final ITestEntity suite, final Object fileLocation,
			@ScriptParameter(defaultValue = "Test Report") final String title, @ScriptParameter(defaultValue = "") final String description,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object reportData) throws IOException, CoreException {

		if (suite == null)
			throw new IllegalArgumentException("Provided suite is null.");

		final IReportGenerator report = ReportTools.getReport(reportType);
		if (report != null) {
			final String reportOutput = report.createReport(title, description, suite, reportData);

			saveDataToFile(reportOutput.getBytes(), fileLocation);

		} else
			throw new IllegalArgumentException("Report type \"" + reportType + "\" is unknown");
	}

	/**
	 * Load a test suite definition from a given resource.
	 *
	 * @param location
	 *            location to load from
	 * @return test suite definition
	 * @throws IOException
	 *             when reading of definition fails
	 */
	@WrapToScript
	public ITestSuiteDefinition loadTestSuiteDefinition(Object location) throws IOException {
		final Object resolvedLocation = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());
		return UnitTestHelper.loadTestSuite(ResourceTools.getInputStream(resolvedLocation));
	}

	/**
	 * Save a test suite definition to a file.
	 *
	 * @param testsuite
	 *            definition to save
	 * @param fileLocation
	 *            location to save file to (file system or workspace)
	 * @throws CoreException
	 *             when we could not write to a workspace file
	 * @throws IOException
	 *             when we could not write to the file system
	 */
	@WrapToScript
	public void saveTestSuiteDefinition(ITestSuiteDefinition testsuite, Object fileLocation) throws IOException, CoreException {
		final byte[] testSuiteData = UnitTestHelper.serializeTestSuite(testsuite);
		saveDataToFile(testSuiteData, fileLocation);
	}

	private void saveDataToFile(byte[] data, Object fileLocation) throws IOException, CoreException {
		final Object file = ResourceTools.resolve(fileLocation, getScriptEngine().getExecutedFile());
		if (file instanceof IFile) {
			if (((IFile) file).exists())
				((IFile) file).setContents(new ByteArrayInputStream(data), IResource.FORCE | IResource.KEEP_HISTORY, null);
			else {
				ResourceTools.createFolder(((IFile) file).getParent());
				((IFile) file).create(new ByteArrayInputStream(data), true, null);
			}

		} else if (file instanceof File) {
			final FileOutputStream outputStream = new FileOutputStream((File) file);
			outputStream.write(data);
			outputStream.close();

		} else
			throw new IOException("Could not find file: " + fileLocation);
	}
}
