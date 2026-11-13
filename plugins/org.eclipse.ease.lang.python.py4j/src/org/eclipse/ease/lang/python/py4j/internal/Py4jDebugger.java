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
import java.util.Collections;
import java.util.List;

import org.eclipse.core.resources.IMarker;
import org.eclipse.debug.core.DebugEvent;
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
	 * Returns list of all breakpoints in given file.
	 *
	 * @param filename
	 *            Filename to get all breakpoints for.
	 * @return List of breakpoints in given file.
	 */
	public List<PythonBreakpoint> getBreakpoints(String filename) {
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

					return pythonBreakpoints;
				}
			}
		}

		return Collections.emptyList();
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
	public Object execute(Script script) {
		try {
			String reference = script.getTitle();
			final IPythonScriptRegistry registry = getScriptRegistry();
			if (registry != null) {
				registry.put(script);
				reference = registry.getReference(script);
			}

			return fPythonDebuggerStub.run(script, reference);

		} catch (final Exception e) {
			/*
			 * When terminating, #handleEvent sets resume type to STEP_END, which causes #traceDispatch to raise an ExitException. The ExitException is
			 * propagated back to python, and eventually ends up back here at Exit method. However Py4J does not support propogating the same type of exception
			 * across the Python/Java barrier, so what ends up being thrown is a Py4JException instead.
			 *
			 * Therefore we catch that case and re-raise the expected ExitException()
			 */
			if (getThreadState(getThread()).fResumeType == DebugEvent.STEP_END) {
				throw new ScriptEngineCancellationException();
			}

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
		return toStackTrace(fPythonDebuggerStub.getCurrentFrame());
	}

	@Override
	public ScriptStackTrace getExceptionStacktrace() {
		return toStackTrace(fPythonDebuggerStub.getExceptionFrame());
	}

	private ScriptStackTrace toStackTrace(IPyFrame frame) {
		final ScriptStackTrace trace = new ScriptStackTrace();

		while (frame != null) {
			trace.add(new PythonDebugFrame(frame));

			frame = frame.getParent();
		}

		return trace;
	}
}
