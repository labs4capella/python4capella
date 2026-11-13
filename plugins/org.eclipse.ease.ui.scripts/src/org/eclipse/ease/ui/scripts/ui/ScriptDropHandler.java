/*******************************************************************************
 * Copyright (c) 2015 Christian Pontesegger and others.
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
import org.eclipse.ease.ui.dnd.IShellDropHandler;
import org.eclipse.ease.ui.scripts.repository.IScript;

public class ScriptDropHandler implements IShellDropHandler {

	@Override
	public boolean accepts(IScriptEngine scriptEngine, Object element) {
		return element instanceof IScript;
	}

	@Override
	public void performDrop(final IScriptEngine scriptEngine, final Object element) {
		if (element instanceof IScript)
			scriptEngine.execute("include('script:/" + ((IScript) element).getPath() + "');");
	}
}
