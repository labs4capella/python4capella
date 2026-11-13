/*******************************************************************************
 * Copyright (c) 2015 Jonah Graham and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Jonah Graham - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.modules.platform.debug;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.debug.core.DebugPlugin;
import org.eclipse.debug.core.ILaunch;
import org.eclipse.debug.core.ILaunchConfiguration;
import org.eclipse.debug.core.ILaunchManager;
import org.eclipse.debug.ui.DebugUITools;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.swt.widgets.Display;

/**
 * Methods in the launch module ease writing scripts to perform complicated launch set-up and control. The key method is {@link #launch(String, String)}.
 * <p>
 * A simple example of its use is:
 *
 * <pre>
 * loadModule("/System/Launch")
 * launch("Client", "debug")
 * </pre>
 *
 * where "Client" is the name of a launch configuration in the workbench and "debug" is the launch mode to use.
 * </p>
 * <p>
 * More examples of using the launch method are available in JavaScript Snippets.
 * </p>
 */
public class LaunchModule extends AbstractScriptModule {

	public static final String MODULE_ID = "/System/Launch";

	/**
	 * Obtain the platform launch manager. This allows access to the Eclipse debug core launch manager, allowing control over all non-UI aspects of launches.
	 * The most valuable of these should be wrapped for ideal script usage and made available in the module itself.
	 *
	 * @return the launch manager
	 */
	@WrapToScript
	public static ILaunchManager getLaunchManager() {
		return DebugPlugin.getDefault().getLaunchManager();
	}

	/**
	 * Returns an array of all the Launch Configuration Names known to the Launch Manager. These names can be used as the argument to the
	 * {@module #getLaunchConfiguration(String)}, {@module #launch(String, String)} and {@module #launchUI(String, String)} methods.
	 *
	 * @return array of launch configuration names.
	 * @throws CoreException
	 *             if an exception occurs retrieving configurations
	 */
	@WrapToScript
	public static String[] getLaunchConfigurationNames() throws CoreException {
		final ILaunchConfiguration[] configurations = getLaunchConfigurations();
		final String[] names = new String[configurations.length];
		for (int i = 0; i < names.length; i++) {
			names[i] = configurations[i].getName();
		}
		return names;
	}

	/**
	 * Returns an array of all the Launch Configurations known to the Launch Manager. These can be used as the argument to
	 * {@module #launch(ILaunchConfiguration, String)} and {@module #launchUI(ILaunchConfiguration, String)} methods.
	 *
	 * @return array of launch configurations
	 * @throws CoreException
	 *             if an exception occurs retrieving configurations
	 */
	@WrapToScript
	public static ILaunchConfiguration[] getLaunchConfigurations() throws CoreException {
		return DebugPlugin.getDefault().getLaunchManager().getLaunchConfigurations();
	}

	/**
	 * Return the launch configuration given by name parameter. The launch configuration can be edited or otherwise operated on.
	 *
	 * @param name
	 *            the launch configuration name
	 * @return the named launch configuration
	 * @throws IllegalArgumentException
	 *             if the name is not known to the launch manager
	 * @throws CoreException
	 *             if an exception occurs retrieving configurations
	 * @see ILaunchConfiguration#getWorkingCopy()
	 */
	@WrapToScript
	public static ILaunchConfiguration getLaunchConfiguration(String name) throws CoreException, IllegalArgumentException {
		final ILaunchConfiguration[] configurations = getLaunchConfigurations();
		for (final ILaunchConfiguration configuration : configurations) {
			if (configuration.getName().equals(name)) {
				return configuration;
			}
		}

		throw new IllegalArgumentException("Unknown launch configuration name, use getLaunchConfigurationNames() to obtain all names");
	}

	/**
	 * Launch the configuration given by name, or an {@link ILaunchConfiguration}, and return the ILaunch for further processing.
	 * <p>
	 * This is the way to launch a configuration within a script which is itself launched. Consider using {@module #launchUI(String, String)} if a full UI style
	 * launch is required, for example when invoked from the interactive console.
	 * </p>
	 *
	 * @param launchConfiguration
	 *            the {@link ILaunchConfiguration}, or the name of the launch configuration to be resolved with {@module #getLaunchConfiguration(String)}
	 * @param mode
	 *            the launch mode, normally "debug" or "run" but can be any of the launch modes available on the platform. The default value is "run".
	 * @return the resulting launch
	 * @throws IllegalArgumentException
	 *             if the name is not known to the launch manager
	 * @throws CoreException
	 *             if an exception occurs retrieving configurations
	 */
	@WrapToScript
	public static ILaunch launch(Object launchConfiguration, @ScriptParameter(defaultValue = "run") String mode) throws CoreException {
		ILaunchConfiguration config;
		if (launchConfiguration instanceof ILaunchConfiguration) {
			config = (ILaunchConfiguration) launchConfiguration;
		} else {
			config = getLaunchConfiguration(launchConfiguration.toString());
		}
		return config.launch(mode, new NullProgressMonitor());
	}

	/**
	 * Launch the configuration given by name, or an {@link ILaunchConfiguration}, in the UI thread. This method respects the workspace settings for things like
	 * building before launching.
	 * <p>
	 * This method, unlike {@module #launch(String, String)}, does not return the ILaunch because it is delegated to run via the UI thread and perform UI tasks
	 * before the launch (such as prompting the user).
	 * </p>
	 *
	 * @param launchConfiguration
	 *            the {@link ILaunchConfiguration}, or the name of the launch configuration to be resolved with {@module #getLaunchConfiguration(String)}
	 * @param mode
	 *            the launch mode, normally "debug" or "run" but can be any of the launch modes available on the platform. The default value is "run".
	 * @throws CoreException
	 *             if an exception occurs retrieving configurations
	 */
	@WrapToScript
	public static void launchUI(Object launchConfiguration, @ScriptParameter(defaultValue = "run") final String mode) throws CoreException {
		final ILaunchConfiguration config;
		if (launchConfiguration instanceof ILaunchConfiguration) {
			config = (ILaunchConfiguration) launchConfiguration;
		} else {
			config = getLaunchConfiguration(launchConfiguration.toString());
		}
		Display.getDefault().syncExec(() -> DebugUITools.launch(config, mode));
	}
}
