/*******************************************************************************
 * Copyright (c) 2013 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.ui;

import java.util.HashMap;

import org.eclipse.ease.ui.scripts.handler.RunScript;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.tools.AbstractPopupItem;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.ui.menus.CommandContributionItem;
import org.eclipse.ui.menus.CommandContributionItemParameter;
import org.eclipse.ui.plugin.AbstractUIPlugin;

public class ScriptPopup extends AbstractPopupItem {

	private final IScript fScript;

	public ScriptPopup(final IScript script) {
		fScript = script;
	}

	@Override
	public CommandContributionItemParameter getContributionParameter() {
		final CommandContributionItemParameter contributionParameter = new CommandContributionItemParameter(null, null, RunScript.COMMAND_ID,
				CommandContributionItem.STYLE_PUSH);

		final HashMap<String, String> parameters = new HashMap<String, String>();
		parameters.put(RunScript.PARAMETER_NAME, fScript.getPath().toString());

		contributionParameter.parameters = parameters;

		return contributionParameter;
	}

	@Override
	public String getDisplayName() {
		return fScript.getName();
	}

	@Override
	protected ImageDescriptor getImageDescriptor() {
		return AbstractUIPlugin.imageDescriptorFromPlugin(org.eclipse.ease.ui.Activator.PLUGIN_ID, "/images/eobj16/script.gif");
	}
}
