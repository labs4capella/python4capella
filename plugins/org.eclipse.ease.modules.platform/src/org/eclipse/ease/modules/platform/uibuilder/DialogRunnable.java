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

import org.eclipse.swt.widgets.Composite;

public abstract class DialogRunnable implements Runnable {

	private Composite fComposite;

	private ScriptableDialog fDialog;

	public void setDialog(ScriptableDialog dialog) {
		fDialog = dialog;
	}

	public ScriptableDialog getDialog() {
		return fDialog;
	}

	public void setComposite(Composite composite) {
		fComposite = composite;
	}

	public Composite getComposite() {
		return fComposite;
	}
}
