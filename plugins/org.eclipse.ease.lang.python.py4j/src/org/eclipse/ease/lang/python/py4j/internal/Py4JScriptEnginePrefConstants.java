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

package org.eclipse.ease.lang.python.py4j.internal;

public interface Py4JScriptEnginePrefConstants {
	String PREFIX = Activator.PLUGIN_ID + "."; //$NON-NLS-1$

	String INTERPRETER = PREFIX + "INTERPRETER";
	String DEFAULT_INTERPRETER = "python"; //$NON-NLS-1$

	String IGNORE_PYTHON_ENV_VARIABLES = PREFIX + "IGNORE_PYTHON_ENV_VARIABLES";
	boolean DEFAULT_IGNORE_PYTHON_ENV_VARIABLES = false;
}
