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

import org.eclipse.ease.ui.scripts.repository.IScript;

public class PopupHandler extends ToolbarHandler {

	public static final String POPUP_LOCATION = "popup:org.eclipse.ui.popup.any?after=additions";

	public PopupHandler() {
		getContributionFactory(POPUP_LOCATION);
	}

	/**
	 * Add a popup menu script contribution.
	 *
	 * @param script
	 *            script to add
	 * @param value
	 *            menu keyword value
	 */
	@Override
	protected void addContribution(final IScript script, final String value) {
		getContributionFactory(POPUP_LOCATION).addScript(script);
	}

	/**
	 * Remove a popup menu script contribution.
	 *
	 * @param script
	 *            script to remove
	 * @param value
	 *            menu keyword value
	 */
	@Override
	protected void removeContribution(final IScript script, final String value) {
		getContributionFactory(POPUP_LOCATION).removeScript(script);
	}

	@Override
	protected String getHandlerType() {
		return "popup";
	}
}
