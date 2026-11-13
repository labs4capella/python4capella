/*******************************************************************************
 * Copyright (c) 2015 Christian Pontesegger and others.
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
package org.eclipse.ease.modules.platform.dnd;

import java.io.File;
import java.net.URI;
import java.util.concurrent.ExecutionException;

import org.eclipse.core.resources.IFile;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.modules.IEnvironment;
import org.eclipse.ease.modules.platform.ScriptingModule;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ease.ui.dnd.IShellDropHandler;
import org.eclipse.ui.PlatformUI;

public class ForkDropHandler implements IShellDropHandler {

	@Override
	public boolean accepts(IScriptEngine scriptEngine, Object element) {
		if ((element instanceof IFile) || (element instanceof File) || (element instanceof URI))
			return getScriptType(element) != null;

		return false;
	}

	@Override
	public void performDrop(IScriptEngine scriptEngine, Object element) {
		final ScriptType scriptType = getScriptType(element);

		if (scriptType != null) {
			// resource not supported by current engine, spawn new one
			final IEnvironment environment = IEnvironment.getEnvironment(scriptEngine);
			if (environment != null) {
				if (environment.getModule(ScriptingModule.class) == null) {
					try {
						if (environment.loadModule(ScriptingModule.MODULE_ID, false) == null)
							throw new RuntimeException("Cannot load module '" + ScriptingModule.MODULE_ID + "'");

					} catch (final ExecutionException e) {
						throw new RuntimeException(e);
					}
				}

				scriptEngine.execute("fork(\"" + ResourceTools.toAbsoluteLocation(element, null) + "\")");

			} else
				throw new RuntimeException("No environment loaded, cannot execute dropped file");

		} else {
			// should not happen as accepts guarantees that a scripttype exists for the given resource
			throw new RuntimeException("Could not detect script type of dropped resource");
		}
	}

	private static ScriptType getScriptType(Object element) {
		final IScriptService scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);
		return scriptService.getScriptType(ResourceTools.toAbsoluteLocation(element, null));
	}

}
