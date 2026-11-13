/*******************************************************************************
 * Copyright (c) 2016 Christian Pontesegger and others.
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

package org.eclipse.ease.ui.scripts.keywordhandler;

import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ui.IViewPart;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.ViewPart;

public class MenuHandler extends ToolbarHandler {

	/**
	 * Add a menu script contribution.
	 *
	 * @param script
	 *            script to add
	 * @param value
	 *            menu keyword value
	 */
	@Override
	protected void addContribution(final IScript script, final String value) {

		// process each location
		for (Location location : toLocations(value)) {
			Logger.trace(Activator.PLUGIN_ID, TRACE_UI_INTEGRATION, Activator.PLUGIN_ID,
					"Adding script \"" + script.getName() + "\" to " + location.fScheme + ":" + location.fTargetID);

			if (location.fTargetID != null) {
				IViewPart view = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().findView(location.fTargetID);

				// update contribution factory
				getContributionFactory(location.getID()).addScript(script);

				if ((view instanceof ViewPart) && (view.getViewSite() != null)) {
					// the view is already rendered, contributions will not be
					// considered anymore so add item directly
					// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=452203 for
					// details

					getContributionFactory(location.getID()).setAffectedContribution(view.getViewSite().getActionBars().getMenuManager());
					view.getViewSite().getActionBars().getMenuManager().add(new ScriptContributionItem(script));
					view.getViewSite().getActionBars().updateActionBars();
				}
			}
		}
	}

	/**
	 * Remove a menu script contribution.
	 *
	 * @param script
	 *            script to remove
	 * @param value
	 *            menu keyword value
	 */
	@Override
	protected void removeContribution(final IScript script, final String value) {
		// process each location
		for (Location location : toLocations(value)) {
			Logger.trace(Activator.PLUGIN_ID, TRACE_UI_INTEGRATION, Activator.PLUGIN_ID,
					"Removing script \"" + script.getName() + "\" from " + location.fScheme + ":" + location.fTargetID);

			// update contribution
			getContributionFactory(location.getID()).removeScript(script);

			if (location.fTargetID != null) {
				IViewPart view = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().findView(location.fTargetID);
				if ((view instanceof ViewPart) && (view.getViewSite() != null)) {
					// the view is already rendered, contributions will not be
					// considered anymore so remove item directly
					// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=452203 for
					// details
					view.getViewSite().getActionBars().getMenuManager().remove(script.getLocation());
					view.getViewSite().getActionBars().updateActionBars();
				}
			}
		}
	}

	@Override
	protected String getHandlerType() {
		return "menu";
	}
}
