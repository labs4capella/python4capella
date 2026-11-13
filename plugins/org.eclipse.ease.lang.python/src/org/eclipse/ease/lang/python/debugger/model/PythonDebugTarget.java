/*******************************************************************************
 * Copyright (c) 2013 Martin Kloesch and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API
 *     Martin Kloesch - implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.debugger.model;

import java.util.Arrays;
import java.util.Collection;

import org.eclipse.debug.core.DebugPlugin;
import org.eclipse.debug.core.ILaunch;
import org.eclipse.debug.core.model.IBreakpoint;
import org.eclipse.ease.Script;
import org.eclipse.ease.debugging.model.EaseDebugTarget;

/**
 * ScriptDebugTarget for communication between Eclipse framework and Python debugger.
 */
public class PythonDebugTarget extends EaseDebugTarget {
	private static final String BREAKPOINT_TYPE = "org.python.pydev.debug";

	public PythonDebugTarget(final ILaunch launch, final boolean suspendOnStartup, final boolean suspendOnScriptLoad, boolean showDynamicCode) {
		super(launch, suspendOnStartup, suspendOnScriptLoad, showDynamicCode);
	}

	@Override
	public String getName() {
		return "EASE Python Debugger";
	}

	/**
	 * Getter methods for all matching breakpoints in given script.
	 *
	 * Currently EASE Python Debugger uses PyDev breakpoints, this could change though.
	 */
	@Override
	protected Collection<IBreakpoint> getBreakpoints(final Script script) {
		return Arrays.asList(DebugPlugin.getDefault().getBreakpointManager().getBreakpoints(BREAKPOINT_TYPE));
	}

	@Override
	public boolean supportsBreakpoint(final IBreakpoint breakpoint) {
		return true;
	}

	@Override
	public boolean canSuspend() {
		return false;
	}

	@Override
	public String getModelIdentifier() {
		return "org.eclipse.ease.debugModelPresentation.python";
	}
}
