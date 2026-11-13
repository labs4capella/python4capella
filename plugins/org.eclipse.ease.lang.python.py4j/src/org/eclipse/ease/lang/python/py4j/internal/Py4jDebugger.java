/*******************************************************************************
 * Copyright (c) 2018 Martin Kloesch and others.
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

import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.resources.IMarker;
import org.eclipse.debug.core.model.IBreakpoint;
import org.eclipse.ease.IDebugEngine;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptEngineCancellationException;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.debugging.events.debugger.IDebuggerEvent;
import org.eclipse.ease.lang.python.debugger.IPyFrame;
import org.eclipse.ease.lang.python.debugger.IPythonScriptRegistry;
import org.eclipse.ease.lang.python.debugger.PythonBreakpoint;
import org.eclipse.ease.lang.python.debugger.PythonDebugger;

import py4j.Py4JException;

/**
 * Extension of {@link PythonDebugger} with additional {@link ICodeTraceFilter} to lower amount of trace dispatches.
 */
public class Py4jDebugger extends PythonDebugger {
	/**
	 * Extended code tracer doing pre-filtering.
	 */
	private ICodeTraceFilter fPythonDebuggerStub;

	// Trace callbacks and script execution may run on different Py4J threads.
	private volatile ScriptEngineCancellationException fCancellation;

	public Py4jDebugger(IDebugEngine engine, boolean showDynamicCode) {
		super(engine, showDynamicCode);
	}

	/**
	 * Sets extended code tracer doing pre-filtering of dispatch calls..
	 *
	 * @param traceFilter
	 *            Extended code tracer.
	 */
	public void setPythonDebuggerStub(ICodeTraceFilter traceFilter) {
		fPythonDebuggerStub = traceFilter;
	}

	/**
	 * Returns an array of all breakpoints in the given file.
	 * Arrays avoid exposing JDK collection iterators through Py4J on Java 17 and later.
	 *
	 * @param filename
	 *            Filename to get all breakpoints for.
	 * @return Array of breakpoints in the given file.
	 */
	public PythonBreakpoint[] getBreakpoints(String filename) {
		final IPythonScriptRegistry registry = getScriptRegistry();
		if (registry != null) {

			final Script script = registry.getScript(filename);
			if (script != null) {
				final List<IBreakpoint> breakpoints = fBreakpoints.get(script);
				if (breakpoints != null) {
					final List<PythonBreakpoint> pythonBreakpoints = new ArrayList<>();

					for (final IBreakpoint breakpoint : breakpoints) {
						final int lineNumber = breakpoint.getMarker().getAttribute(IMarker.LINE_NUMBER, -1);
						pythonBreakpoints.add(new PythonBreakpoint(filename, lineNumber));
					}

					return pythonBreakpoints.toArray(new PythonBreakpoint[0]);
				}
			}
		}

		return new PythonBreakpoint[0];
	}

	@Override
	protected void suspend(IDebuggerEvent event) {
		fPythonDebuggerStub.suspend();

		super.suspend(event);
	}

	@Override
	protected void resume(int resumeType, Object thread) {
		super.resume(resumeType, thread);

		fPythonDebuggerStub.resume(resumeType);
	}

	@Override
	public void traceDispatch(IPyFrame frame, String type) {
		try {
			super.traceDispatch(frame, type);
		} catch (ScriptEngineCancellationException e) {
			fCancellation = e;
			throw e;
		}
	}

	@Override
	public Object execute(Script script) {
		fCancellation = null;
		try {
			String reference = script.getTitle();
			final IPythonScriptRegistry registry = getScriptRegistry();
			if (registry != null) {
				registry.put(script);
				reference = registry.getReference(script);
			}

			return fPythonDebuggerStub.run(script, reference);

		} catch (final Exception e) {
			// Py4J wraps cancellation from traceDispatch on its round trip through Python.
			final ScriptEngineCancellationException cancellation = fCancellation;
			if ((e instanceof Py4JException) && (cancellation != null))
				throw cancellation;

			if (e instanceof Py4JException)
				throw new Py4JException(beautifyExceptionMessage(e.getMessage()));

			throw e;
		}
	}

	private String beautifyExceptionMessage(String message) {
		return message;
	}

	@Override
	protected void breakpointAdded(final Script script, final IBreakpoint breakpoint) {
		final IPythonScriptRegistry registry = getScriptRegistry();
		if (registry == null) {
			return;
		}

		final String reference = registry.getReference(script);
		if (reference != null) {
			final int lineNumber = breakpoint.getMarker().getAttribute(IMarker.LINE_NUMBER, -1);

			if (lineNumber != -1)
				fPythonDebuggerStub.setBreakpoint(new PythonBreakpoint(reference, lineNumber));
		}
	}

	@Override
	protected void breakpointRemoved(final Script script, final IBreakpoint breakpoint) {
		final IPythonScriptRegistry registry = getScriptRegistry();
		if (registry == null) {
			return;
		}

		final String reference = registry.getReference(script);
		if (reference != null) {
			final int lineNumber = breakpoint.getMarker().getAttribute(IMarker.LINE_NUMBER, -1);

			if (lineNumber != -1)
				fPythonDebuggerStub.removeBreakpoint(new PythonBreakpoint(reference, lineNumber));
		}
	}

	@Override
	public ScriptStackTrace getStacktrace() {
		// Match the tracked frames saved by traceDispatch when comparing stepping depths.
		return getStacktrace(fPythonDebuggerStub.getCurrentFrame());
	}

	@Override
	public ScriptStackTrace getExceptionStacktrace() {
		return getStacktrace(fPythonDebuggerStub.getExceptionFrame());
	}
}
