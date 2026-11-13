/*******************************************************************************
 * Copyright (c) 2017 Martin Kloesch and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Martin Kloesch - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.debugger.actions;

import java.util.regex.Pattern;

import org.eclipse.ease.debugging.model.EaseDebugVariable;
import org.eclipse.jface.viewers.Viewer;

/**
 * {@link ViewFilterAction} for hiding Python magic variables.
 */
public class MagicFilterAction extends ViewFilterAction {

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.wst.jsdt.debug.internal.ui.actions.ViewFilterAction#getPreferenceKey()
	 */
	@Override
	protected String getPreferenceKey() {
		return "org.eclipse.ease.ui.show_magicvariables";
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.jface.viewers.ViewerFilter#select(org.eclipse.jface.viewers.Viewer, java.lang.Object, java.lang.Object)
	 */
	@Override
	public boolean select(final Viewer viewer, final Object parentElement, final Object element) {
		if (element instanceof EaseDebugVariable) {
			final EaseDebugVariable variable = (EaseDebugVariable) element;
			return !Pattern.matches("^__.+__$", variable.getName());
		}

		return true;
	}

}
