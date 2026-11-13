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

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.ExecutionException;
import java.util.stream.Collectors;

import org.eclipse.core.resources.IProject;
import org.eclipse.ease.IScriptEngine;
import org.python.pydev.core.IPythonPathNature;
import org.python.pydev.plugin.nature.PythonNature;

public class PyDevPathImporter extends ResourceProjectPathImporter {

	@Override
	protected void doRegisterProject(IProject project, IScriptEngine engine) {
		try {
			final PythonNature pythonNature = PythonNature.getPythonNature(project);
			if (Objects.nonNull(pythonNature)) {
				final String[] paths = getProjectPaths(pythonNature.getPythonPathNature());

				final String importCode = Arrays.asList(paths).stream().filter(p -> Objects.nonNull(p) && !p.isEmpty())
						.map(p -> String.format("sys.path.append('%s')%n", p)).collect(Collectors.joining());
				final String code = String.format("import sys%n%s", importCode).replace("\\", "\\\\");

				engine.inject(code, false);
			}
		} catch (ExecutionException | ReflectiveOperationException | NoClassDefFoundError e) {
			// loading project paths failed, try to continue without
		}
	}

	private static String[] getProjectPaths(IPythonPathNature pathNature) throws ReflectiveOperationException {
		try {
			// Older PyDev versions return a pipe-separated string.
			final String paths = (String) IPythonPathNature.class.getMethod("getOnlyProjectPythonPathStr", boolean.class).invoke(pathNature, true);
			return paths.split("\\|");
		} catch (NoSuchMethodException e) {
			// Newer PyDev versions accept a substitution flag and return a list.
			final List<?> paths = (List<?>) IPythonPathNature.class.getMethod("getOnlyProjectPythonPathStr", boolean.class, boolean.class)
					.invoke(pathNature, true, false);
			return paths.toArray(new String[0]);
		}
	}
}
