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

import java.net.URL;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.eclipse.debug.core.ILaunch;
import org.eclipse.ease.AbstractScriptEngine;
import org.eclipse.ease.IDebugEngine;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptEngineException;
import org.eclipse.ease.debugging.model.EaseDebugVariable;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.definition.IVariable;
import org.eclipse.ease.lang.unittest.execution.DefaultTestExecutionStrategy;
import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.service.EngineDescription;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptService;
import org.eclipse.ease.service.ScriptType;

/**
 * Script engine executing *.suite files and {@link ITestEntity} elements.
 */
public class TestSuiteScriptEngine extends AbstractScriptEngine implements IDebugEngine {

	public static final String ENGINE_ID = "org.eclipse.ease.lang.unittest.engine";

	/** Name of variable to be injected into executing test engines. */
	public static final String TEST_FILE_VARIABLE = "__EASE_UnitTest_File";

	public static final String TEST_SUITE_VARIABLE = "__EASE_UnitTest_Suite";

	/**
	 * Debug method to print test execution results. This method is not needed for runtime functionality.
	 *
	 * @param entity
	 *            test element to print status from (recursive)
	 * @param string
	 *            indentation (typically use an empty string)
	 */
	private static void printStatus(ITestEntity entity, String indent) {
		System.out.println(
				indent + entity.getClass().getSimpleName() + " <" + entity.getName() + "> : " + entity.getStatus() + (" (" + entity.getDuration() + " ms)"));

		if (entity instanceof ITestContainer) {
			for (final ITestEntity child : ((ITestContainer) entity).getChildren())
				printStatus(child, indent + "\t");
		}
	}

	private final Map<String, Object> fVariables = new HashMap<>();
	private final List<URL> fRegisteredJars = new ArrayList<>();

	private final ITestContainer fTestRoot;

	/** Debug variables. */
	private ILaunch fLaunch = null;
	private boolean fSuspendOnStartup;
	private boolean fSuspendOnScriptLoad;
	private boolean fShowDynamicCode;

	/** Marker to indicate that this engine has received a termination request. */
	private boolean fTerminated = false;

	public TestSuiteScriptEngine() {
		super("Script Testsuite");

		fTestRoot = IRuntimeFactory.eINSTANCE.createTestFolder();
		fTestRoot.setName("Root");
	}

	@Override
	public void terminateCurrent() {
		terminate();
	}

	@Override
	public void registerJar(URL url) {
		fRegisteredJars.add(url);
	}

	@Override
	protected Object internalGetVariable(String name) {
		return fVariables.get(name);
	}

	@Override
	protected Map<String, Object> internalGetVariables() {
		return fVariables;
	}

	@Override
	protected boolean internalHasVariable(String name) {
		return internalGetVariables().containsKey(name);
	}

	@Override
	protected void internalSetVariable(String name, Object content) {
		fVariables.put(name, content);
	}

	@Override
	public Object removeVariable(String name) {
		return fVariables.remove(name);
	}

	@Override
	protected void setupEngine() throws ScriptEngineException {
		fTerminated = false;
	}

	@Override
	protected void teardownEngine() throws ScriptEngineException {
		// nothing to do
	}

	private ITestSuite loadTestSuiteDefinition(Script script) throws Exception {
		// load definition
		final ITestSuiteDefinition definition = UnitTestHelper.loadTestSuite(script.getCodeStream());

		if (definition != null) {

			definition.setResource(script.getFile());

			final ITestSuite runtimeSuite = UnitTestHelper.createRuntimeSuite(definition);
			runtimeSuite.setResource(definition.getResource());

			fTestRoot.getChildren().clear();
			fTestRoot.getChildren().add(runtimeSuite);

			// load variables
			for (final IVariable variable : definition.getVariables())
				setVariable(variable.getName(), variable.getContent());

			return runtimeSuite;
		}

		return null;
	}

	@Override
	protected Object execute(Script script, String fileName, boolean uiThread) throws Throwable {

		Object command = script.getCommand();

		if ((!(command instanceof ITestEntity)) && (!(command instanceof FilteredTestCommand))) {
			// not a testsuite. Probably a *.suite file or a stream providing suite data
			try {
				final ITestSuite runtimeSuite = loadTestSuiteDefinition(script);
				if (runtimeSuite != null)
					command = runtimeSuite;
				else
					throw new Exception("Could not load suite from resource: " + script.getFile());
			} catch (final Exception e) {
				throw new Exception("Invalid testsuite content detected in: " + script.getFile(), e);
			}
		}

		if (command instanceof ITestEntity) {
			final ITestExecutionStrategy strategy = new DefaultTestExecutionStrategy();
			strategy.prepareExecution(this, (ITestEntity) command);
			strategy.execute((ITestEntity) command);

			// not needed for productive environment, can be enabled for debugging purposes
			// printStatus(((ITestEntity) command), "");

			return command;

		} else if (command instanceof FilteredTestCommand) {
			// called when a test entity is re-executed with an applied filter
			final ITestExecutionStrategy strategy = new DefaultTestExecutionStrategy();
			strategy.prepareExecution(this, ((FilteredTestCommand) command).getTestRoot(), ((FilteredTestCommand) command).getActiveTests());
			strategy.execute(((FilteredTestCommand) command).getTestRoot());

			// not needed for productive environment, can be enabled for debugging purposes
			// printStatus(((ITestEntity) command), "");

			return command;
		} else
			throw new Exception("Cannot execute object \"" + command + "\"");
	}

	@Override
	public void setupDebugger(ILaunch launch, boolean suspendOnStartup, boolean suspendOnScriptLoad, boolean showDynamicCode) {
		fLaunch = launch;
		fSuspendOnStartup = suspendOnStartup;
		fSuspendOnScriptLoad = suspendOnScriptLoad;
		fShowDynamicCode = showDynamicCode;
	}

	/**
	 * Get the root container for all executed test entities. This container gets created once and remains constant for the whole lifecycle of this engine. Its
	 * child elements may change however depending on what entities get executed.
	 *
	 * @return root container
	 */
	public ITestContainer getTestRoot() {
		return fTestRoot;
	}

	@Override
	public void terminate() {
		if (!fTerminated) {
			fTerminated = true;

			// propagate termination event to all engines
			if (getTestRoot() != null)
				getTestRoot().setTerminated(true);

			super.terminate();
		}
	}

	/**
	 * Create a script engine for a given testsuite and resource. The testsuite might provide information on the default engine to use. The resource might need
	 * a different engine to execute.
	 *
	 * @param testSuite
	 *            testsuite to be executed from or <code>null</code>
	 * @param resource
	 *            resource to execute or <code>null</code>
	 * @return script engine or <code>null</code>
	 */
	public IScriptEngine createScriptEngine(ITestSuite testSuite, Object resource) {
		// load service directly to allow to work in headless mode
		final IScriptService scriptService = ScriptService.getInstance();

		EngineDescription candidate = null;
		if ((testSuite != null) && (testSuite.getDefinition() != null)) {
			if (testSuite.getDefinition().getFlag(Flag.PREFERRED_ENGINE_ID, "") != null)
				candidate = scriptService.getEngineByID(testSuite.getDefinition().getFlag(Flag.PREFERRED_ENGINE_ID, ""));
		}

		// now lets see if candidate supports our script resource
		if (resource != null) {
			final String location = resource.toString();
			if ((location != null) && (!location.isEmpty())) {
				final ScriptType requiredScriptType = scriptService.getScriptType(location);

				final List<EngineDescription> engines = requiredScriptType.getEngines();

				// first pass: see if one of these engine matches with our preferred one
				if (candidate != null) {
					for (final EngineDescription description : engines) {
						if (candidate.equals(description))
							return prepareEngine(description.createEngine());
					}
				}

				// we need to use a backup engine
				// 2nd pass: look for a debug engine
				for (final EngineDescription description : engines) {
					if (description.supportsDebugging())
						return prepareEngine(description.createEngine());
				}

				// final shot: take any engine available
				if (!engines.isEmpty())
					return prepareEngine(engines.get(0).createEngine());
			}
		}

		if (candidate != null)
			return prepareEngine(candidate.createEngine());

		return null;
	}

	/**
	 * Prepare any engine created during test execution to use the same settings as this engine.
	 *
	 * @param engine
	 *            engine to be prepared
	 * @return prepared engine instance
	 */
	private IScriptEngine prepareEngine(IScriptEngine engine) {

		// link I/O streams
		engine.setOutputStream(getOutputStream());
		engine.setInputStream(getInputStream());
		engine.setErrorStream(getErrorStream());

		// enable debug support
		if ((fLaunch != null) && (engine instanceof IDebugEngine)) {
			// debug setup preferred
			((IDebugEngine) engine).setupDebugger(fLaunch, fSuspendOnStartup, fSuspendOnScriptLoad, fShowDynamicCode);
		}

		// pass variables from suite
		for (final Entry<String, Object> variable : getVariables().entrySet()) {
			if (TEST_FILE_VARIABLE.equals(variable.getKey()))
				continue;

			if (TEST_SUITE_VARIABLE.equals(variable.getKey()))
				continue;

			engine.setVariable(variable.getKey(), variable.getValue());
		}

		// add registered jars rom suite
		for (final URL jarLocation : fRegisteredJars)
			engine.registerJar(jarLocation);

		return engine;
	}

	@Override
	public Collection<EaseDebugVariable> getVariables(Object scope) {
		throw new UnsupportedOperationException();
	}

	public void reset() {
		getScheduler().init();
	}
}
