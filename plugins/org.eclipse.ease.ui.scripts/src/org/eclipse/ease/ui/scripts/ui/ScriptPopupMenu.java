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

import java.util.ArrayList;
import java.util.List;

import org.eclipse.ease.ui.tools.AbstractPopupItem;
import org.eclipse.ease.ui.tools.AbstractPopupMenu;

public class ScriptPopupMenu extends AbstractPopupMenu {

	private final List<AbstractPopupItem> mItems = new ArrayList<>();

	public ScriptPopupMenu(final String name) {
		super(name);
	}

	public void addItem(final AbstractPopupItem item) {
		mItems.add(item);
	}

	@Override
	protected void populate() {
		for (final AbstractPopupItem item : mItems)
			addPopup(item);
	}

	public boolean hasSubMenu(final String name) {
		for (final AbstractPopupItem item : mItems) {
			if (item.getDisplayName().equals(name))
				return true;
		}

		return false;
	}

	public ScriptPopupMenu getSubMenu(final String name) {
		for (final AbstractPopupItem item : mItems) {
			if ((item.getDisplayName().equals(name)) && (item instanceof ScriptPopupMenu))
				return (ScriptPopupMenu) item;
		}

		return null;
	}
}
