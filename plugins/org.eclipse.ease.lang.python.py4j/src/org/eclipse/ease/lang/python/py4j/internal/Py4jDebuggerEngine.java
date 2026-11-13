/*******************************************************************************
 * Copyright (c) 2014 Martin Kloesch and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Martin Kloesch - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.py4j.internal;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;
import java.util.Map.Entry;

import org.eclipse.debug.core.ILaunch;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptEngineException;
import org.eclipse.ease.debugging.EaseDebugFrame;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.debugging.model.EaseDebugVariable;
import org.eclipse.ease.lang.python.debugger.IPythonDebugEngine;
import org.eclipse.ease.lang.python.debugger.PythonDebugger;
import org.eclipse.ease.lang.python.debugger.PythonEventDispatchJob;
import org.eclipse.ease.lang.python.debugger.PythonScriptRegistry;
import org.eclipse.ease.lang.python.debugger.ResourceHelper;
import org.eclipse.ease.lang.python.debugger.model.PythonDebugTarget;

/***
 * A script engine to debug Python code on a PY4J engine.
 *
 * Uses most of {@link Py4jDebuggerEngine}'s functionality and only extends it when file is to be debugged.
 */

public class Py4jDebuggerEngine extends Py4jScriptEngine implements IPythonDebugEngine {

	public static final String ENGINE_ID = "org.eclipse.ease.lang.python.py4j.debugger.engine";

	private Py4jDebugger fDebugger = null;

	@Override
	public void setDebugger(final PythonDebugger debugger) {
		setDebugger((Py4jDebugger) debugger);
	}

	private void setDebugger(final Py4jDebugger debugger) {
		fDebugger = debugger;
	}

	@Override
	protected void setupEngine() throws ScriptEngineException {
		super.setupEngine();

		if (fDebugger == null) {
			final Py4jDebugger debugger = new Py4jDebugger(this, false);
			debugger.setScriptRegistry(new PythonScriptRegistry());
			setDebugger(debugger);
		}

		// in case we were called using "Run as"
		if (fDebugger != null) {
			try {
				// load python part of debugger
				final InputStream stream = ResourceHelper.getResourceStream("org.eclipse.ease.lang.python.py4j", "pysrc/py4jdb.py");
				final ICodeTraceFilter pythonDebugger = (ICodeTraceFilter) super.internalExecute(new Script("Load Python debugger", stream), null);

				// Connect both sides
				pythonDebugger.setDebugger(fDebugger);
				fDebugger.setPythonDebuggerStub(pythonDebugger);

			} catch (final Throwable e) {
				throw new ScriptEngineException("Failed to load Python Debugger", e);
			}
		}
	}

	@Override
	protected void teardownEngine() {
		super.teardownEngine();

		fDebugger = null;
	}

	@Override
	protected Object internalExecute(final Script script, final String fileName) throws Throwable {
		return fDebugger.execute(script);
	}

	@Override
	public ScriptStackTrace getStackTrace() {
		return fDebugger.getStacktrace();
	}

	@Override
	public void setupDebugger(final ILaunch launch, final boolean suspendOnStartup, final boolean suspendOnScriptLoad, final boolean showDynamicCode) {
		final PythonDebugTarget target = new PythonDebugTarget(launch, suspendOnStartup, suspendOnScriptLoad, showDynamicCode);
		launch.addDebugTarget(target);

		final Py4jDebugger debugger = new Py4jDebugger(this, showDynamicCode);

		setDebugger(debugger);

		new PythonEventDispatchJob(target, debugger);
	}

	@Override
	public Object removeVariable(final String name) {
		throw new UnsupportedOperationException();
	}

	@Override
	public Collection<EaseDebugVariable> getVariables(Object scope) {
		final Map<String, Object> variablesMap;
		if (scope instanceof EaseDebugFrame) {
			final EaseDebugFrame frame = (EaseDebugFrame) scope;
			variablesMap = frame.getVariables();
		} else {
			variablesMap = getVariables();
		}

		final Collection<EaseDebugVariable> variables = new ArrayList<>();

		for (final Entry<String, Object> entry : variablesMap.entrySet())
			variables.add(createVariable(entry.getKey(), entry.getValue()));

		return variables;
	}
}
