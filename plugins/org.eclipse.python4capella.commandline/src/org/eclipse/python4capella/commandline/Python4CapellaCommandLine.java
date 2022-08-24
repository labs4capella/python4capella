/**
 *   Copyright (c) 2021, 2022 THALES GLOBAL SERVICES
 *  This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License 2.0
 *  which accompanies this distribution, and is available at
 *  https://www.eclipse.org/legal/epl-2.0/
 *
 *  SPDX-License-Identifier: EPL-2.0
 *
 *  Contributors:
 *       Obeo - Initial API and implementation
 */
package org.eclipse.python4capella.commandline;

import java.util.Arrays;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.ScriptResult;
import org.eclipse.ease.service.EngineDescription;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptService;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.equinox.app.IApplicationContext;
import org.polarsys.capella.core.commandline.core.CommandLineException;
import org.polarsys.capella.core.commandline.core.DefaultCommandLine;

/**
 * Command line to launch Python4Capella.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class Python4CapellaCommandLine extends DefaultCommandLine {

	// @formatter:off
// ./eclipse -nosplash -consolelog -application org.polarsys.capella.core.commandline.core -appid org.eclipse.python4capella.commandline -data workspace workspace://Python4Capella/sample_scripts/list_logical_components.py "In-Flight Entertainment System/In-Flight Entertainment System.aird"	
	// @formatter:on

	/**
	 * {@inheritDoc}
	 */
	@Override
	public boolean execute(IApplicationContext context) {
		final Object argObject = context.getArguments().get(IApplicationContext.APPLICATION_ARGS);
		if (argObject instanceof String[]) {
			final String scriptPath = ((String[]) argObject)[2];
			final String[] argv = new String[((String[]) argObject).length - 3];
			for (int i = 3; i < ((String[]) argObject).length; i++) {
				argv[i - 3] = ((String[]) argObject)[i];
			}
			return runScript(scriptPath, argv);
		} else {
			System.err.println("<script name> <script parameters>");
		}

		return false;
	}

	private boolean runScript(final String scriptPath, final String[] argv) {
		final IScriptService scriptService = ScriptService.getInstance();
		final ScriptType scriptType = scriptService.getScriptType(scriptPath);
		if (scriptType != null) {
			final EngineDescription engineDescription = scriptService.getEngine(scriptType.getName());
			if (engineDescription != null) {
				final IScriptEngine engine = engineDescription.createEngine();
				engine.setVariable("argv", argv);
				final Object script;
				final Object scriptObject = ResourceTools.resolve(scriptPath);
				if (scriptObject != null) {
					script = scriptObject;
				} else {
					script = "include(\"" + scriptPath + "\")";
				}

				try {
					System.out.println("Executing " + scriptPath + " with arguments: " + Arrays.deepToString(argv));
					final ScriptResult scriptResult = engine.execute(script);
					engine.schedule();

					final Object result = scriptResult.get();
					if (result != null) {
						if (ScriptResult.VOID.equals(result)) {
							return true;
						}

						try {
							return Integer.parseInt(result.toString()) == 0;
						} catch (final Exception e) {
							// no integer
						}

						try {
							return Double.valueOf(result.toString()).intValue() == 0;
						} catch (final Exception e) {
							// no double
						}

						try {
							return Boolean.parseBoolean(result.toString());
						} catch (final Exception e) {
							// no boolean
						}
					} else {
						return true;
					}
				} catch (Exception e) {
					Python4CapellaCommandLinePlugin.getPlugin().log(new Status(IStatus.ERROR,
							Python4CapellaCommandLinePlugin.PLUGIN_ID, "Error executing script: " + scriptPath, e));
				}
			} else {
				System.err.println("Can't find script engine for: " + scriptPath);
			}
		} else {
			System.err.println("Can't find script engine for: " + scriptPath);
		}
		return false;
	}

	@Override
	public void checkArgs(IApplicationContext context) throws CommandLineException {
		// nothing to do here
	}

	@Override
	public void printHelp() {
		System.out.println("Python4Capella Command Line"); //$NON-NLS-1$
		super.printHelp();
	}

}
