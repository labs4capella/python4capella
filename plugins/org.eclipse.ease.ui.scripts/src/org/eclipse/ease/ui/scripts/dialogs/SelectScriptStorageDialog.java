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
package org.eclipse.ease.ui.scripts.dialogs;

import java.io.File;

import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.preferences.PreferencesHelper;
import org.eclipse.jface.dialogs.Dialog;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.jface.window.Window;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.dialogs.ContainerSelectionDialog;

public class SelectScriptStorageDialog extends Dialog {
	private Text fTxtWorkspace;
	private Text fTxtFileSystem;
	private Button fBtnStoreInSettings;
	private Button fBtnStoreInWorkspace;
	private Button fBtnStoreOnFileSystem;
	private String fLocation = null;

	/**
	 * Create the dialog.
	 *
	 * @param parentShell
	 */
	public SelectScriptStorageDialog(final Shell parentShell) {
		super(parentShell);
	}

	@Override
	protected void configureShell(Shell newShell) {
		super.configureShell(newShell);

		newShell.setText(Messages.SelectScriptStorageDialog_storageLocation);
	}

	/**
	 * Create contents of the dialog.
	 *
	 * @param parent
	 */
	@Override
	protected Control createDialogArea(final Composite parent) {
		final Composite container = (Composite) super.createDialogArea(parent);
		container.setLayout(new GridLayout(2, false));

		final Label lblWhereDoYou = new Label(container, SWT.NONE);
		lblWhereDoYou.setLayoutData(new GridData(SWT.LEFT, SWT.CENTER, false, false, 2, 1));
		lblWhereDoYou.setText(Messages.SelectScriptStorageDialog_storageDescription);

		fBtnStoreInSettings = new Button(container, SWT.RADIO);
		fBtnStoreInSettings.setSelection(true);
		fBtnStoreInSettings.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(final SelectionEvent e) {
			}
		});
		final GridData gd_btnStoreInSettings = new GridData(SWT.LEFT, SWT.CENTER, false, false, 1, 1);
		gd_btnStoreInSettings.verticalIndent = 20;
		fBtnStoreInSettings.setLayoutData(gd_btnStoreInSettings);
		fBtnStoreInSettings.setText(Messages.SelectScriptStorageDialog_storeInSettings);
		new Label(container, SWT.NONE);

		fBtnStoreInWorkspace = new Button(container, SWT.RADIO);
		fBtnStoreInWorkspace.setText(Messages.SelectScriptStorageDialog_storeInWorkspace);
		new Label(container, SWT.NONE);

		fTxtWorkspace = new Text(container, SWT.BORDER);
		final GridData gd_txtWorkspace = new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1);
		gd_txtWorkspace.horizontalIndent = 17;
		fTxtWorkspace.setLayoutData(gd_txtWorkspace);

		final Button btnNewButton = new Button(container, SWT.NONE);
		btnNewButton.setText(Messages.SelectScriptStorageDialog_browse);
		btnNewButton.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(final SelectionEvent e) {
				final ContainerSelectionDialog dialog = new ContainerSelectionDialog(getShell(), ResourcesPlugin.getWorkspace().getRoot(), true,
						Messages.SelectScriptStorageDialog_selectFolder);
				if (dialog.open() == Window.OK) {
					final Object[] result = dialog.getResult();
					if ((result.length > 0) && (result[0] instanceof IPath))
						fTxtWorkspace.setText(result[0].toString());
				}
			}
		});

		fBtnStoreOnFileSystem = new Button(container, SWT.RADIO);
		fBtnStoreOnFileSystem.setText(Messages.SelectScriptStorageDialog_fileSystem);
		new Label(container, SWT.NONE);

		fTxtFileSystem = new Text(container, SWT.BORDER);
		final GridData gd_txtFileSystem = new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1);
		gd_txtFileSystem.horizontalIndent = 17;
		fTxtFileSystem.setLayoutData(gd_txtFileSystem);

		final Button btnNewButton_1 = new Button(container, SWT.NONE);
		btnNewButton_1.setText(Messages.SelectScriptStorageDialog_browse);
		btnNewButton_1.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(final SelectionEvent e) {
				final DirectoryDialog dialog = new DirectoryDialog(getShell());
				final String path = dialog.open();
				if (path != null)
					fTxtFileSystem.setText(new File(path).toURI().toString());
			}
		});
		return container;
	}

	/**
	 * Create contents of the button bar.
	 *
	 * @param parent
	 */
	@Override
	protected void createButtonsForButtonBar(final Composite parent) {
		createButton(parent, IDialogConstants.OK_ID, IDialogConstants.OK_LABEL, true);
		createButton(parent, IDialogConstants.CANCEL_ID, IDialogConstants.CANCEL_LABEL, false);
	}

	/**
	 * Return the initial size of the dialog.
	 */
	@Override
	protected Point getInitialSize() {
		return new Point(450, 300);
	}

	@Override
	protected void okPressed() {
		if (fBtnStoreInSettings.getSelection())
			fLocation = PreferencesHelper.getDefaultScriptStorageLocation();

		else if (fBtnStoreInWorkspace.getSelection()) {
			if (fTxtWorkspace.getText().startsWith("/"))
				fLocation = "workspace:/" + fTxtWorkspace.getText();
			else
				fLocation = "workspace://" + fTxtWorkspace.getText();
		}

		else if (fBtnStoreOnFileSystem.getSelection())
			// FIXME change user input to URI syntax
			fLocation = fTxtFileSystem.getText();

		super.okPressed();
	}

	public String getLocation() {
		return fLocation;
	}
}
