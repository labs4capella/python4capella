/*******************************************************************************
 * Copyright (c) 2017 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.expressions.ui;

import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.jface.dialogs.Dialog;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;

public class ExpressionDialog extends Dialog {

	private final String fDescription;
	private ExpressionComposite fExpressionComposite;
	private final String fRootExpressionName;
	private IExpressionDefinition fExpression;

	/**
	 * Create the dialog.
	 *
	 * @param parentShell
	 */
	public ExpressionDialog(Shell parentShell, String description, String rootExpressionName) {
		super(parentShell);
		fDescription = description;
		fRootExpressionName = rootExpressionName;
	}

	/**
	 * Create contents of the dialog.
	 *
	 * @param parent
	 */
	@Override
	protected Control createDialogArea(Composite parent) {
		final Composite container = (Composite) super.createDialogArea(parent);
		container.setLayout(new GridLayout(1, false));

		if (fDescription != null) {
			final Label lblDescription = new Label(container, SWT.WRAP);
			lblDescription.setLayoutData(new GridData(SWT.LEFT, SWT.TOP, true, false, 1, 1));
			lblDescription.setText(fDescription);
		}

		fExpressionComposite = new ExpressionComposite(null, container, SWT.NONE);
		fExpressionComposite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true, 1, 1));

		fExpressionComposite.setExpression(null, fRootExpressionName);

		return container;
	}

	@Override
	protected void okPressed() {
		// save expression
		fExpression = fExpressionComposite.getExpression();

		super.okPressed();
	}

	@Override
	protected void createButtonsForButtonBar(Composite parent) {
		createButton(parent, IDialogConstants.OK_ID, IDialogConstants.OK_LABEL, true);
		createButton(parent, IDialogConstants.CANCEL_ID, IDialogConstants.CANCEL_LABEL, false);
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.jface.dialogs.Dialog#getInitialSize()
	 */
	@Override
	protected Point getInitialSize() {
		return new Point(400, 250);
	}

	@Override
	protected boolean isResizable() {
		return true;
	}

	public IExpressionDefinition getExpression() {
		return fExpression;
	}
}
