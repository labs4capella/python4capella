/**
 *   Copyright (c) 2021, 2024 THALES GLOBAL SERVICES
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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.NullProgressMonitor;
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
import org.polarsys.capella.core.commandline.core.ui.AbstractWorkbenchCommandLine;

/**
 * Command line to launch Python4Capella.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class Python4CapellaCommandLine extends AbstractWorkbenchCommandLine {

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
			final int scriptPathIndex = getScriptPathIndex((String[]) argObject);
			if (scriptPathIndex >= 0) {
				final String scriptPath = ((String[]) argObject)[scriptPathIndex];
				final List<String> argv = new ArrayList<>();
				for (int i = scriptPathIndex + 1; i < ((String[]) argObject).length; i++) {
					final String arg = ((String[]) argObject)[i];
					if (arg != null) {
						argv.add(arg);
					}
				}
				return runScript(scriptPath, argv.toArray(new String[argv.size()]));
			} else {
				System.err.println("<script name.py> <script parameters>");
			}
		} else {
			System.err.println("<script name.py> <script parameters>");
		}

		return false;
	}

	/**
	 * Gets the script path index from the given arguments.
	 * 
	 * @param args the arguments array
	 * @return the script path index from the given arguments
	 */
	private int getScriptPathIndex(String[] args) {
		int res = -1;

		for (int i = 0; i < args.length; i++) {
			if (args[i] != null && args[i].endsWith(".py")) {
				res = i;
				break;
			}
		}

		return res;
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

		try {
			ResourcesPlugin.getWorkspace().save(true, new NullProgressMonitor());
		} catch (CoreException e) {
			System.err.println("Can't save workspace: " + e.getMessage());
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

	@Override
	protected IStatus executeWithinWorkbench() {
		return Status.OK_STATUS;
	}
}
