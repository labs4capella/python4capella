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
package org.eclipse.ease.modules.platform.completion;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.debug.core.DebugPlugin;
import org.eclipse.debug.core.ILaunchConfiguration;
import org.eclipse.debug.core.ILaunchConfigurationType;
import org.eclipse.debug.ui.DebugUITools;
import org.eclipse.debug.ui.ILaunchGroup;
import org.eclipse.ease.ICompletionContext;
import org.eclipse.ease.Logger;
import org.eclipse.ease.modules.platform.PluginConstants;
import org.eclipse.ease.modules.platform.debug.LaunchModule;
import org.eclipse.ease.ui.completion.ScriptCompletionProposal;
import org.eclipse.ease.ui.completion.provider.AbstractCompletionProvider;

public class LaunchModuleCompletionProvider extends AbstractCompletionProvider {

	@Override
	public boolean isActive(final ICompletionContext context) {
		if ((isStringParameter(context)) && (context.getLoadedModules().contains(getModuleDefinition(LaunchModule.MODULE_ID))))
			return isLaunchConfigurationParameter(context) || isLaunchTypeParameter(context);

		return false;
	}

	private boolean isLaunchConfigurationParameter(ICompletionContext context) {
		return isMethodParameter(context, "launch", 0) || isMethodParameter(context, "launchUI", 0) || isMethodParameter(context, "getLaunchConfiguration", 0);
	}

	private boolean isLaunchTypeParameter(ICompletionContext context) {
		return isMethodParameter(context, "launch", 1) || isMethodParameter(context, "launchUI", 1);
	}

	@Override
	protected void prepareProposals(ICompletionContext context) {
		if (isLaunchConfigurationParameter(getContext())) {

			try {
				final ILaunchConfiguration[] configurations = DebugPlugin.getDefault().getLaunchManager().getLaunchConfigurations();
				for (final ILaunchConfiguration configuration : configurations) {
					final String name = configuration.getName();
					final ILaunchConfigurationType type = configuration.getType();
					final String typeName = type.getName();
					final String display = name + " - " + typeName;
					addProposal(display, name, new DescriptorImageResolver(DebugUITools.getDefaultImageDescriptor(configuration)), 0, null);
				}
			} catch (final CoreException e) {
				Logger.warning(PluginConstants.PLUGIN_ID, "Code Completion: could not read launch configurations", e);
			}

		} else if (isLaunchTypeParameter(getContext())) {
			// TODO: Make this parameter dependent on the selected launch config
			// to only populate the relevant modes
			final Collection<ScriptCompletionProposal> proposals = new ArrayList<>();
			final ILaunchGroup[] launchGroups = DebugUITools.getLaunchGroups();
			final Map<String, ILaunchGroup> modes = new HashMap<>();
			for (final ILaunchGroup launchGroup : launchGroups) {
				modes.put(launchGroup.getMode(), launchGroup);
			}
			for (final ILaunchGroup launchGroup : modes.values()) {
				final String display = launchGroup.getLabel().replace("&", "");
				final String name = launchGroup.getMode();
				addProposal(display, name, new DescriptorImageResolver(launchGroup.getImageDescriptor()), 0, null);
			}
		}
	}
}