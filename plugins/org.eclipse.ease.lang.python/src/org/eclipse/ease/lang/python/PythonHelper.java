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

package org.eclipse.ease.lang.python;

import java.util.Random;
import java.util.regex.Pattern;

import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptService;
import org.eclipse.ease.service.ScriptType;

public final class PythonHelper {

	/** Script type identifier for Python. Must match with the script type 'name' from plugin.xml. */
	public static final String SCRIPT_TYPE_PYTHON = "Python";

	@Deprecated
	private PythonHelper() {
		throw new UnsupportedOperationException("Utility class shall not be instantiated");
	}

	public static String getSaveName(final String identifier) {
		// check if name is already valid
		if (isSaveName(identifier))
			return identifier;

		// not valid, convert string to valid format
		final StringBuilder buffer = new StringBuilder(identifier.replaceAll("[^a-zA-Z0-9]", "_"));

		// check for valid first character
		if (buffer.length() > 0) {
			final char start = buffer.charAt(0);
			if (((start < 65) || ((start > 90) && (start < 97)) || (start > 122)) && (start != '_'))
				buffer.insert(0, '_');
		} else {
			// buffer is empty, create a random string of lowercase letters
			final Random random = new Random();
			buffer.append('_');
			for (int index = 0; index < random.nextInt(20); index++)
				buffer.append('a' + random.nextInt(26));
		}

		return buffer.toString();
	}

	public static boolean isSaveName(final String identifier) {
		return Pattern.matches("[a-zA-Z_$][a-zA-Z0-9_$]*", identifier);
	}

	/**
	 * Get the {@link ScriptType} for python.
	 *
	 * @return script type definition
	 */
	public static ScriptType getScriptType() {
		final IScriptService scriptService = ScriptService.getInstance();
		return scriptService.getAvailableScriptTypes().get(SCRIPT_TYPE_PYTHON);
	}
}
