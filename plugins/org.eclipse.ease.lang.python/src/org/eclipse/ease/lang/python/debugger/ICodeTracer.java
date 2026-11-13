/*******************************************************************************
 * Copyright (c) 2017 Kloesch and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Kloesch - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.python.debugger;

import org.eclipse.ease.Script;

/**
 * Interface for execution tracing in Python.
 *
 * This object is the link between Eclipse and the Python implementation.
 *
 */
public interface ICodeTracer {
	/**
	 * Runs the given script via the code tracer in Python.
	 *
	 * @param script
	 *            Script to be run via code tracer.
	 * @param filename
	 *            Filename for script.
	 */
	Object run(Script script, String filename);
}
