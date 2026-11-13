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

import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.jface.viewers.ViewerFilter;

public class ScriptEngineFilter extends ViewerFilter {

	private final String fEngineID;

	public ScriptEngineFilter(final String engineID) {
		// TODO filter on script type
		fEngineID = engineID;
	}

	@Override
	public boolean select(final Viewer viewer, final Object parentElement, final Object element) {
		if (element instanceof IScript) {
			// TODO retrieve content type from script and filter
		}

		return true;
	}
}
