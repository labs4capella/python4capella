/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
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

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.action.IContributionItem;
import org.eclipse.jface.action.IContributionManager;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.action.ToolBarManager;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.menus.AbstractContributionFactory;
import org.eclipse.ui.menus.IContributionRoot;
import org.eclipse.ui.menus.IMenuService;
import org.eclipse.ui.services.IServiceLocator;

public class ScriptContributionFactory extends AbstractContributionFactory {

	/** List of scripts to be registered. */
	protected final List<IScript> fScripts = new ArrayList<IScript>();

	/** ContributionManager scripts should be added to. */
	protected IContributionManager fContributionManager = null;

	public ScriptContributionFactory(final String location) {
		super(location, null);

		// register factory
		final IMenuService menuService = PlatformUI.getWorkbench().getService(IMenuService.class);
		menuService.addContributionFactory(this);
	}

	@Override
	public void createContributionItems(final IServiceLocator serviceLocator, final IContributionRoot additions) {

		// if we added contributions manually before, do not add them a 2nd time
		// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=452203 for details
		boolean rendered = (fContributionManager instanceof MenuManager) && (((MenuManager) fContributionManager).getMenu() != null);
		rendered |= (fContributionManager instanceof ToolBarManager) && (((ToolBarManager) fContributionManager).getControl() != null);

		if (rendered) {
			for (IContributionItem item : fContributionManager.getItems()) {
				if (item instanceof ScriptContributionItem) {
					// contributions already added to toolbar, do not add again
					return;
				}
			}
		}

		if (getLocation().endsWith(PopupHandler.POPUP_LOCATION)) {
			for (IScript script : sortScripts(fScripts))
				additions.addContributionItem(new ScriptContributionItem(script, script.getKeywords().get("popup")), null);

		} else {
			for (IScript script : fScripts)
				additions.addContributionItem(new ScriptContributionItem(script), null);
		}
	}

	public void addScript(final IScript script) {
		if (!fScripts.contains(script))
			fScripts.add(script);
	}

	public void removeScript(final IScript script) {
		fScripts.remove(script);
	}

	public void setAffectedContribution(final IContributionManager manager) {
		fContributionManager = manager;
	}

	protected static List<IScript> sortScripts(final List<IScript> scripts) {
		Collections.sort(scripts, new Comparator<IScript>() {

			@Override
			public int compare(final IScript s1, final IScript s2) {
				return s1.getName().compareToIgnoreCase(s2.getName());
			}
		});

		return scripts;
	}
}
