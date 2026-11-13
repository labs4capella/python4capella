/*******************************************************************************
 * Copyright (c) 2021 Christian Pontesegger and others.
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

package org.eclipse.ease.lang.python;

import java.util.Collection;
import java.util.HashSet;
import java.util.concurrent.ExecutionException;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.ease.IExecutionListener;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.IScriptEngineLaunchExtension;
import org.eclipse.ease.Script;

public class ResourceProjectPathImporter implements IScriptEngineLaunchExtension, IExecutionListener {

	private final Collection<IProject> fRegisteredProjects = new HashSet<>();

	@Override
	public void createEngine(IScriptEngine engine) {
		engine.addExecutionListener(this);
	}

	@Override
	public void notify(IScriptEngine engine, Script script, int status) {
		if (status == SCRIPT_START) {
			Object file = script.getFile();
			if (file instanceof IResource)
				registerProject(((IResource) file).getProject(), engine);

			else {
				file = engine.getExecutedFile();
				if (file instanceof IResource)
					registerProject(((IResource) file).getProject(), engine);
			}
		}
	}

	private void registerProject(IProject project, IScriptEngine engine) {
		if (!fRegisteredProjects.contains(project)) {
			fRegisteredProjects.add(project);

			doRegisterProject(project, engine);
		}
	}

	protected void doRegisterProject(IProject project, IScriptEngine engine) {
		try {
			final String path = project.getLocation().toOSString();
			final String code = String.format("import sys%nsys.path.append('%s')%n", path).replace("\\", "\\\\");

			engine.inject(code, false);

		} catch (ExecutionException | NoClassDefFoundError e) {
			// loading project paths failed, try to continue without
		}
	}
}
