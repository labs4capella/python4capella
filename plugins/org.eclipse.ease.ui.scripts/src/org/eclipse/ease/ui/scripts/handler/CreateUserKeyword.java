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
package org.eclipse.ease.ui.scripts.handler;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.commands.IHandler;
import org.eclipse.ease.ui.scripts.dialogs.AddKeywordDialog;
import org.eclipse.ease.ui.scripts.properties.AllKeywordsSection;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.window.Window;
import org.eclipse.ui.IWorkbenchPart;
import org.eclipse.ui.handlers.HandlerUtil;
import org.eclipse.ui.part.IPage;
import org.eclipse.ui.views.properties.PropertySheet;
import org.eclipse.ui.views.properties.tabbed.ISection;
import org.eclipse.ui.views.properties.tabbed.TabContents;
import org.eclipse.ui.views.properties.tabbed.TabbedPropertySheetPage;

public class CreateUserKeyword extends AbstractHandler implements IHandler {

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {

		// try to get selected script
		final IWorkbenchPart part = HandlerUtil.getActivePart(event);
		if (part instanceof PropertySheet) {
			final IPage currentPage = ((PropertySheet) part).getCurrentPage();
			if (currentPage instanceof TabbedPropertySheetPage) {
				final TabContents currentTab = ((TabbedPropertySheetPage) currentPage).getCurrentTab();

				for (final ISection section : currentTab.getSections()) {
					if (section instanceof AllKeywordsSection) {
						final IScript script = ((AllKeywordsSection) section).getScript();

						final AddKeywordDialog dialog = new AddKeywordDialog(HandlerUtil.getActiveShell(event), script);
						if (dialog.open() == Window.OK) {
							script.setUserKeyword(dialog.getKeyword(), dialog.getValue());
							section.refresh();
						}
					}
				}
			}
		}

		return null;
	}
}
