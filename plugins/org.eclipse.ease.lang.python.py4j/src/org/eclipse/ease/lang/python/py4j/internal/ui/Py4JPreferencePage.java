/*******************************************************************************
 * Copyright (c) 2016 Kichwa Coders and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Jonah Graham (Kichwa Coders) - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.python.py4j.internal.ui;

import java.io.File;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.variables.IStringVariableManager;
import org.eclipse.core.variables.VariablesPlugin;
import org.eclipse.debug.ui.StringVariableSelectionDialog;
import org.eclipse.ease.lang.python.py4j.internal.Activator;
import org.eclipse.ease.lang.python.py4j.internal.Py4JScriptEnginePrefConstants;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.jface.dialogs.IMessageProvider;
import org.eclipse.jface.preference.BooleanFieldEditor;
import org.eclipse.jface.preference.FieldEditorPreferencePage;
import org.eclipse.jface.preference.FileFieldEditor;
import org.eclipse.jface.preference.StringFieldEditor;
import org.eclipse.jface.window.Window;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.IWorkbenchPreferencePage;

public class Py4JPreferencePage extends FieldEditorPreferencePage implements IWorkbenchPreferencePage {

	public Py4JPreferencePage() {
	}

	@Override
	public void init(final IWorkbench workbench) {
		setPreferenceStore(Activator.getDefault().getPreferenceStore());
	}

	@Override
	protected void createFieldEditors() {
		addField(new FileFieldEditor(Py4JScriptEnginePrefConstants.INTERPRETER, "Python location:", false, StringFieldEditor.VALIDATE_ON_KEY_STROKE,
				getFieldEditorParent()) {
			private Button variablesButton;

			{
				setErrorMessage("Python location must be absolute path to python, or name of executable to launch from System PATH");
			}

			@Override
			public int getNumberOfControls() {
				return 4;
			}

			protected void variablesPressed() {
				final StringVariableSelectionDialog dialog = new StringVariableSelectionDialog(getTextControl().getShell());
				if (dialog.open() == Window.OK) {
					getTextControl().insert(dialog.getVariableExpression());
					valueChanged();
				}
			}

			/**
			 * Get the change control. Create it in parent if required.
			 *
			 * @param parent
			 * @return Button
			 */
			protected Button getVariablesControl(final Composite parent) {
				if (variablesButton == null) {
					variablesButton = new Button(parent, SWT.PUSH);
					variablesButton.setText("Variables...");
					variablesButton.setFont(parent.getFont());
					variablesButton.addSelectionListener(new SelectionAdapter() {
						@Override
						public void widgetSelected(final SelectionEvent evt) {
							variablesPressed();
						}
					});
					variablesButton.addDisposeListener(event -> variablesButton = null);
				} else {
					checkParent(variablesButton, parent);
				}
				return variablesButton;
			}

			@Override
			protected void doFillIntoGrid(final Composite parent, final int numColumns) {
				super.doFillIntoGrid(parent, numColumns - 1);
				variablesButton = getVariablesControl(parent);
				final GridData gd = new GridData();
				gd.horizontalAlignment = GridData.FILL;
				final int widthHint = convertHorizontalDLUsToPixels(variablesButton, IDialogConstants.BUTTON_WIDTH);
				gd.widthHint = Math.max(widthHint, variablesButton.computeSize(SWT.DEFAULT, SWT.DEFAULT, true).x);
				variablesButton.setLayoutData(gd);
			}

			@Override
			protected boolean checkState() {

				String msg = null;
				String info = null;

				String rawPath = getTextControl().getText();
				if (rawPath != null) {
					rawPath = rawPath.trim();
				} else {
					rawPath = "";//$NON-NLS-1$
				}

				final IStringVariableManager variableManager = VariablesPlugin.getDefault().getStringVariableManager();
				String resolvedPath;
				try {
					resolvedPath = variableManager.performStringSubstitution(rawPath);
				} catch (final CoreException e) {
					msg = e.getLocalizedMessage();
					resolvedPath = "";
				}

				if (msg == null) {
					if (resolvedPath.isEmpty()) {
						if (rawPath.isEmpty()) {
							msg = getErrorMessage();
						} else {
							msg = "Variable used in Python location has not resolved to anything";
						}
					} else {
						final File file = new File(resolvedPath);
						if (file.isFile() && file.isAbsolute()) {
							if (resolvedPath.equals(rawPath)) {
								// all good and the user can see what is going to be used
							} else {
								// show the user how the path has been resolved
								info = "'" + resolvedPath + "' will be used as the Python location.";
							}
						} else if (file.isDirectory() || resolvedPath.contains("/") || resolvedPath.contains("\\")) {
							msg = getErrorMessage() + ". The current setting is resolving to '" + resolvedPath + "'.";
						} else {
							info = "'" + resolvedPath + "' will be launched from PATH unless an absolute location is provided.";
						}
					}
				}

				if (msg != null) { // error
					showErrorMessage(msg);
					return false;
				}

				if (doCheckState()) { // OK!
					clearErrorMessage();
					getPage().setMessage(null);
					if (info != null) {
						getPage().setMessage(info, IMessageProvider.INFORMATION);
					}
					return true;
				}
				msg = getErrorMessage(); // subclass might have changed it in the #doCheckState()
				if (msg != null) {
					showErrorMessage(msg);
				}
				return false;
			}
		});

		final Composite fieldEditorParent = getFieldEditorParent();
		final BooleanFieldEditor booleanFieldEditor = new BooleanFieldEditor(Py4JScriptEnginePrefConstants.IGNORE_PYTHON_ENV_VARIABLES,
				"Ignore all PYTHON* environment variables when launching Python", fieldEditorParent);
		booleanFieldEditor.getDescriptionControl(fieldEditorParent).setToolTipText(
				"Ignore all PYTHON* environment variables, e.g. PYTHONPATH and PYTHONHOME, that might be set. (-E command line option to Python)");
		addField(booleanFieldEditor);
	}

}
