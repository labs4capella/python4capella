/*******************************************************************************
 * Copyright (c) 2018 Christian Pontesegger and others.
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

import java.io.IOException;
import java.io.InputStream;

import org.eclipse.ease.ICodeFactory;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.IScriptEngineLaunchExtension;
import org.eclipse.ease.lang.python.debugger.ResourceHelper;
import org.eclipse.ease.modules.EnvironmentModule;
import org.eclipse.ease.modules.ModuleCategoryDefinition;
import org.eclipse.ease.modules.ModuleDefinition;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptService;
import org.eclipse.ease.tools.StringTools;

public class Pep302ModuleImporter implements IScriptEngineLaunchExtension {

	/**
	 * Verify if a given path is a subpath of an EASE module.
	 *
	 * @param candidate
	 *            module path name candidate
	 * @return <code>true</code> when candidate is a path to an EASE module
	 */
	public static boolean isModulePath(String candidate) {
		// do not alter signature as this is called from python code directly.
		candidate = candidate.toLowerCase();

		if ("eclipse".equals(candidate))
			return true;

		if (candidate.startsWith("eclipse.")) {
			// remove eclipse prefix
			candidate = candidate.substring("eclipse".length());
			candidate = candidate.replace('.', '/').replaceAll("[^A-Za-z0-9/]", "_");

			final IScriptService scriptService = ScriptService.getService();
			for (final ModuleCategoryDefinition category : scriptService.getAvailableModuleCategories().values()) {
				if (category.getFullName().toLowerCase().replaceAll("[^A-Za-z0-9/]", "_").equals(candidate))
					return true;
			}
		}

		return false;
	}

	public static boolean isModule(String candidate) {
		// do not alter signature as this is called from python code directly.
		return getModuleDefinition(candidate) != null;
	}

	private static ModuleDefinition getModuleDefinition(String candidate) {
		candidate = candidate.toLowerCase();

		if (candidate.startsWith("eclipse"))
			candidate = candidate.substring("eclipse".length());

		candidate = candidate.replace('.', '/').replaceAll("[^A-Za-z0-9/]", "_");

		final IScriptService scriptService = ScriptService.getService();
		for (final ModuleDefinition definition : scriptService.getAvailableModules()) {
			if (definition.getPath().toString().toLowerCase().replaceAll("[^A-Za-z0-9/]", "_").equals(candidate))
				return definition;
		}

		return null;
	}

	public static String getCode(String moduleName, EnvironmentModule enviromentModule) {
		// do not alter signature as this is called from python code directly.
		final ModuleDefinition definition = getModuleDefinition(moduleName);
		if (definition != null) {
			final Object instance = enviromentModule.getModuleInstance(definition);

			final ICodeFactory factory = ScriptService.getCodeFactory(enviromentModule.getScriptEngine());
			if (factory instanceof PythonCodeFactory) {

				final String identifier = factory.getSaveVariableName(EnvironmentModule.getWrappedVariableName(instance));
				enviromentModule.getScriptEngine().setVariable(identifier, instance);

				return ((PythonCodeFactory) factory).createPep302WrapperCode(enviromentModule, instance, identifier);
			}

			// not expected to be reached
			throw new RuntimeException("No code factory found supporting Pep302 imports");

		} else
			throw new RuntimeException("Module <" + moduleName + "> could not be found");
	}

	@Override
	public void createEngine(IScriptEngine engine) {
		try {
			final InputStream resourceStream = ResourceHelper.getResourceStream(Activator.PLUGIN_ID, "/pysrc/pep302.py");
			final String code = StringTools.toString(resourceStream);
			resourceStream.close();

			engine.execute(code);
		} catch (final IOException e) {
			throw new RuntimeException(e);
		}
	}
}
