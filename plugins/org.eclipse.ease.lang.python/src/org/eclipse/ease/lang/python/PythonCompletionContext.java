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

package org.eclipse.ease.lang.python;

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.ui.completion.BasicContext;

public class PythonCompletionContext extends BasicContext {

	public PythonCompletionContext(IScriptEngine scriptEngine, String contents, int position) {
		super(scriptEngine, contents, position);
	}

	public PythonCompletionContext(Object resource, String contents, int position) {
		super(PythonHelper.getScriptType(), resource, contents, position);
	}
}
