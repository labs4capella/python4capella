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
package org.eclipse.ease.ui.scripts.dialogs;

import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.impl.RepositoryService;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.jface.dialogs.IMessageProvider;
import org.eclipse.jface.dialogs.TitleAreaDialog;
import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.ComboViewer;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.ViewerComparator;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.ModifyEvent;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;

public class AddKeywordDialog extends TitleAreaDialog {

	private class Validator implements ModifyListener {

		@Override
		public void modifyText(ModifyEvent e) {

			getButton(IDialogConstants.OK_ID).setEnabled(false);

			// check that keyword is not empty
			if (fComboViewer.getCombo().getText().trim().isEmpty())
				setMessage(Messages.AddKeywordDialog_emptyKey, IMessageProvider.ERROR);

			else if (fTxtValue.getText().trim().isEmpty())
				setMessage(Messages.AddKeywordDialog_emptyValue, IMessageProvider.ERROR);

			else if ((fScript != null) && (fScript.getKeywords().containsKey(fComboViewer.getCombo().getText().trim()))) {
				getButton(IDialogConstants.OK_ID).setEnabled(true);
				setMessage(Messages.AddKeywordDialog_keyAlreadyExists, IMessageProvider.WARNING);

			} else {
				getButton(IDialogConstants.OK_ID).setEnabled(true);
				setMessage(Messages.AddKeywordDialog_text, IMessageProvider.INFORMATION);
			}
		}
	}

	private Text fTxtValue;
	private ComboViewer fComboViewer;
	private final IScript fScript;
	private String fSelectedKeyword;
	private String fSelectedValue;

	/**
	 * Create the dialog.
	 *
	 * @param parentShell
	 * @param script
	 */
	public AddKeywordDialog(Shell parentShell, IScript script) {
		super(parentShell);
		fScript = script;
	}

	@Override
	public void create() {
		super.create();
		setTitle(Messages.AddKeywordDialog_createNew);
		setMessage(Messages.AddKeywordDialog_text, IMessageProvider.INFORMATION);
	}

	@Override
	protected Control createDialogArea(Composite parent) {
		final Composite area = (Composite) super.createDialogArea(parent);
		final Composite composite = new Composite(area, SWT.NONE);
		composite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true));
		final GridLayout layout = new GridLayout(2, false);
		composite.setLayout(layout);

		final Label lblKeyword = new Label(composite, SWT.NONE);
		lblKeyword.setSize(47, 13);
		lblKeyword.setText(Messages.AddKeywordDialog_keyword);

		final Validator validator = new Validator();

		fComboViewer = new ComboViewer(composite, SWT.NONE);
		final Combo combo = fComboViewer.getCombo();
		combo.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		combo.setSize(380, 20);
		fComboViewer.setLabelProvider(new LabelProvider());
		fComboViewer.setContentProvider(ArrayContentProvider.getInstance());
		fComboViewer.setInput(RepositoryService.getSupportedKeywords());
		fComboViewer.setComparator(new ViewerComparator());
		combo.addModifyListener(validator);

		final Label lblValue = new Label(composite, SWT.NONE);
		lblValue.setSize(30, 13);
		lblValue.setText(Messages.AddKeywordDialog_value);

		fTxtValue = new Text(composite, SWT.BORDER);
		fTxtValue.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		fTxtValue.setSize(380, 19);
		fTxtValue.addModifyListener(validator);

		return area;
	}

	@Override
	protected Control createButtonBar(Composite parent) {
		final Control control = super.createButtonBar(parent);
		getButton(IDialogConstants.OK_ID).setEnabled(false);
		return control;
	}

	@Override
	protected boolean isResizable() {
		return true;
	}

	@Override
	protected void okPressed() {
		// store variables
		fSelectedKeyword = fComboViewer.getCombo().getText();
		fSelectedValue = fTxtValue.getText();

		super.okPressed();
	}

	public String getKeyword() {
		return fSelectedKeyword;
	}

	public String getValue() {
		return fSelectedValue;
	}
}
