/*******************************************************************************
 * Copyright (c) 2015 Christian Pontesegger and others.
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

package org.eclipse.ease.ui.scripts.view;

import org.eclipse.ease.IReplEngine;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.ui.ScriptComposite;
import org.eclipse.ease.ui.views.shell.dropins.AbstractDropin;
import org.eclipse.jface.viewers.ISelectionProvider;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.IWorkbenchPartSite;

public class ScriptDropin extends AbstractDropin {

	private ScriptComposite fComposite;

	@Override
	public void setScriptEngine(IReplEngine engine) {
		super.setScriptEngine(engine);

		if (fComposite != null)
			fComposite.setEngine(engine.getDescription().getID());
	}

	@Override
	public String getTitle() {
		return Messages.ScriptDropin_scripts;
	}

	@Override
	protected void updateUI() {
		// TODO Auto-generated method stub
	}

	@Override
	protected Composite createComposite(IWorkbenchPartSite site, Composite parent) {
		fComposite = new ScriptComposite(this, site, parent, SWT.NONE);

		if (getScriptEngine() != null)
			fComposite.setEngine(getScriptEngine().getDescription().getID());

		return fComposite;
	}

	@Override
	public ISelectionProvider getSelectionProvider() {
		return fComposite.getSelectionProvider();
	}
}
