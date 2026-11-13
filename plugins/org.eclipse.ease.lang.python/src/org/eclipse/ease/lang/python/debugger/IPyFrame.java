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

import java.util.Map;

/**
 * Abstraction interface for frame information in Python.
 */
public interface IPyFrame {
	/**
	 * Returns the filename of the current frame.
	 * <p>
	 * Must <b>NOT</b> return <code>null</code>.
	 *
	 * @return filename for the current frame.
	 */
	String getFilename();

	/**
	 * Returns the linenumber of the current frame.
	 *
	 * @return line number of the current frame.
	 */
	int getLineNumber();

	/**
	 * Returns the parent frame in the call stack.
	 * <p>
	 * If the current frame is the root, <code>null</code> should be returned.
	 *
	 * @return Parent in the call stack or <code>null</code>
	 */
	IPyFrame getParent();

	/**
	 * Get a variable from the current frame.
	 *
	 * @param name
	 *            variable name to look up
	 * @return variable or <code>null</code>
	 */
	Object getVariable(String name);

	/**
	 * Get variables visible from current frame.
	 *
	 * @return variableName -&gt; variableContent
	 */
	Map<String, Object> getVariables();

	/**
	 * Set the content of a variable to a given value.
	 *
	 * @param name
	 *            name of variable to set
	 * @param value
	 *            value to set to
	 */
	void setVariable(String name, Object value);
}
