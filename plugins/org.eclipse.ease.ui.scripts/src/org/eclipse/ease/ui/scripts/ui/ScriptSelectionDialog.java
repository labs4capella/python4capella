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

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.IScriptEngineProvider;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.dialogs.Dialog;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.IWorkbenchPartSite;

public class ScriptSelectionDialog extends Dialog {

	private final IWorkbenchPartSite dialogSite;
	private IScript fSelectedScript = null;

	/**
	 * Construct Macro dialog that shows all Macros in Environment and then you can choose Macro to run
	 * 
	 * @param parentShell
	 *            Shell from Parent
	 * 
	 * @param iWorkbenchPartSite
	 *            Workbench Site
	 */
	public ScriptSelectionDialog(final Shell parentShell, final IWorkbenchPartSite iWorkbenchPartSite) {
		super(parentShell);
		dialogSite = iWorkbenchPartSite;
		setShellStyle(parentShell.getStyle() | SWT.CLOSE | SWT.TITLE | SWT.BORDER | SWT.APPLICATION_MODAL);
		setBlockOnOpen(true);
	}

	@Override
	protected Control createDialogArea(final Composite parent) {
		Composite composite = (Composite) super.createDialogArea(parent);

		composite.setLayout(new GridLayout(1, false));

		Composite mComposite = new ScriptComposite(new IScriptEngineProvider() {

			@Override
			public IScriptEngine getScriptEngine() {
				return null;
			}
		}, dialogSite, composite, SWT.NONE);
		mComposite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true));

		return composite;
	}

	@Override
	protected void configureShell(final Shell newShell) {
		super.configureShell(newShell);
		newShell.setText(Messages.ScriptSelectionDialog_scriptBrowser);
	}

	@Override
	protected void createButtonsForButtonBar(final Composite parent) {
		super.createButtonsForButtonBar(parent);

		final Button ok = getButton(IDialogConstants.OK_ID);
		ok.setText(Messages.ScriptSelectionDialog_open);
		setButtonLayoutData(ok);

		final Button cancel = getButton(IDialogConstants.CANCEL_ID);
		cancel.setText(Messages.ScriptSelectionDialog_cancel);
		setButtonLayoutData(cancel);
	}

	@Override
	public void okPressed() {
		final IStructuredSelection selection = (IStructuredSelection) dialogSite.getSelectionProvider().getSelection();
		if (selection.getFirstElement() instanceof IScript)
			fSelectedScript = (IScript) selection.getFirstElement();

		super.okPressed();
	}

	/**
	 * @return the selected Macro
	 */
	public IScript getMacro() {
		return fSelectedScript;
	}
}
