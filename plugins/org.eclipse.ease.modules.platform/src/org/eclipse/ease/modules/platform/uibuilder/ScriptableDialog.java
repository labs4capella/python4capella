/*******************************************************************************
 * Copyright (c) 2019 Christian Pontesegger and others.
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
package org.eclipse.ease.modules.platform.uibuilder;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.jface.dialogs.TitleAreaDialog;
import org.eclipse.jface.viewers.StructuredViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.List;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;

public class ScriptableDialog extends TitleAreaDialog {

	private Composite fContainer;
	private final DialogRunnable fRunnableOnCreation;

	private final Map<Object, Object> fData = new HashMap<>();
	private final Map<Control, StructuredViewer> fViewers = new HashMap<>();

	private String fMessageText = null;
	private String fTitleText = null;
	private Point fInitialSize = new Point(450, 450);

	/**
	 * Create the dialog.
	 *
	 * @param parentShell
	 */
	public ScriptableDialog(Shell parentShell, DialogRunnable runnableOnCreation) {
		super(parentShell);
		fRunnableOnCreation = runnableOnCreation;
	}

	/**
	 * Create contents of the dialog.
	 *
	 * @param parent
	 */
	@Override
	protected Control createDialogArea(Composite parent) {
		final Composite area = (Composite) super.createDialogArea(parent);
		fContainer = new Composite(area, SWT.NONE);
		fContainer.setLayoutData(new GridData(GridData.FILL_BOTH));

		if (fTitleText != null)
			setTitle(fTitleText);

		if (fMessageText != null)
			setMessage(fMessageText);

		fRunnableOnCreation.setComposite(fContainer);
		fRunnableOnCreation.setDialog(this);
		fRunnableOnCreation.run();

		return area;
	}

	public Composite getContainer() {
		return fContainer;
	}

	/**
	 * Create contents of the button bar.
	 *
	 * @param parent
	 */
	@Override
	protected void createButtonsForButtonBar(Composite parent) {
		createButton(parent, IDialogConstants.OK_ID, IDialogConstants.OK_LABEL, true);
		createButton(parent, IDialogConstants.CANCEL_ID, IDialogConstants.CANCEL_LABEL, false);
	}

	/**
	 * Return the initial size of the dialog.
	 */
	@Override
	protected Point getInitialSize() {
		return fInitialSize;
	}

	public void setInitialSize(int x, int y) {
		fInitialSize = new Point(x, y);
	}

	@Override
	protected void okPressed() {
		storeChildren(fContainer);

		super.okPressed();
	}

	private void storeChildren(Composite container) {
		for (final Control child : container.getChildren()) {

			if (child instanceof Text)
				fData.put(child, ((Text) child).getText());

			else if (child instanceof Button)
				fData.put(child, ((Button) child).getSelection());

			else if (child instanceof Combo) {

				final StructuredViewer viewer = fViewers.get(child);
				if (viewer != null)
					fData.put(viewer, viewer.getStructuredSelection().getFirstElement());

			} else if (child instanceof List) {

				final StructuredViewer viewer = fViewers.get(child);
				if (viewer != null)
					fData.put(viewer, viewer.getStructuredSelection().toArray());

			} else if (child instanceof Composite)
				// do this after all others as eg combo is a composite
				storeChildren((Composite) child);
		}
	}

	public Object getData(Object control) {
		return fData.get(control);
	}

	public void setMessageText(String messageText) {
		fMessageText = messageText;
	}

	public void setTitleText(String titleText) {
		fTitleText = titleText;
	}

	public void registerViewer(Control control, StructuredViewer viewer) {
		fViewers.put(control, viewer);
	}
}
