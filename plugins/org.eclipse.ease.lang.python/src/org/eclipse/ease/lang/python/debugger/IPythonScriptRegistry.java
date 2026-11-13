/*******************************************************************************
 * Copyright (c) 2018 Martin Kloesch and others.
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

package org.eclipse.ease.lang.python.debugger;

import org.eclipse.ease.Script;
import org.eclipse.ease.debugging.IScriptRegistry;

/**
 * Extension of {@link IScriptRegistry} to also add mapping from {@link Script} used in EASE world to {@link String} used in Python world.
 */
public interface IPythonScriptRegistry extends IScriptRegistry {

	/**
	 * Return the {@link Script} identified by this reference {@link String}.
	 *
	 * @param reference
	 *            Reference {@link String} to get {@link Script} for.
	 * @return {@link Script} identified by reference {@link String} or {@code null} if no mapping found.
	 */
	Script getScript(String reference);

	/**
	 * Return the reference {@link String} for this {@link Script}.
	 *
	 * @param script
	 *            {@link Script} to get reference {@link String} for.
	 * @return Reference {@link String} for {@link Script} or {@code null} if no mapping found.
	 */
	String getReference(Script script);
}
