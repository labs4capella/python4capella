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

import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;

public class LabelPlaceHolder extends Label implements IPlaceHolder {

	public LabelPlaceHolder(Composite composite, int row, int column) {
		super(composite, SWT.NONE);
		setText(column + "/" + row);
		setLayoutData(new GridData(SWT.CENTER, SWT.CENTER, false, false));

		setForeground(Display.getCurrent().getSystemColor(SWT.COLOR_DARK_GRAY));
	}

	@Override
	protected void checkSubclass() {
	}
}