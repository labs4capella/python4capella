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

import org.eclipse.ease.IExecutionListener;
import org.eclipse.ease.debugging.dispatcher.IEventProcessor;
import org.eclipse.ease.lang.python.debugger.ICodeTracer;
import org.eclipse.ease.lang.python.debugger.IPyFrame;
import org.eclipse.ease.lang.python.debugger.PythonBreakpoint;
import org.eclipse.ease.lang.python.debugger.PythonDebugger;

/**
 * Extension of {@link ICodeTracer} performing pre-filtering before code gets to actual tracer.
 */
public interface ICodeTraceFilter extends ICodeTracer, IEventProcessor, IExecutionListener {
	/**
	 * Sets the {@link PythonDebugger} to be used by the code trace filter to perform callbacks.
	 *
	 * @param debugger
	 *            {@link PythonDebugger} for callbacks.
	 */
	void setDebugger(PythonDebugger debugger);

	/**
	 * Sets a breakpoint in the trace filter.
	 *
	 * @param breakpoint
	 *            Breakpoint to be set.
	 */
	void setBreakpoint(PythonBreakpoint breakpoint);

	/**
	 * Removes a breakpoint from the trace filter.
	 *
	 * @param breakpoint
	 *            Breakpoint to be removed.
	 */
	void removeBreakpoint(PythonBreakpoint breakpoint);

	/**
	 * Resume execution after filter has notified us that execution might need to be stopped.
	 *
	 * @param resumeType
	 *            Resume type for execution continuation.
	 */
	void resume(int resumeType);

	/**
	 * Suspend execution after filter has notified us that execution might need to be stopped.
	 */
	void suspend();

	/**
	 * Get the current python frame.
	 *
	 * @return current python frame
	 */
	IPyFrame getCurrentFrame();

	/**
	 * Get the python frame of the last thrown exception.
	 *
	 * @return last exception python frame
	 */
	IPyFrame getExceptionFrame();
}
