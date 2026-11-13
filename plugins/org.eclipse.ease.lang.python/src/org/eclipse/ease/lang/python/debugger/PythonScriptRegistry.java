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

import java.io.File;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;

import org.eclipse.ease.Script;
import org.eclipse.ease.debugging.ScriptRegistry;

/**
 * Default implementation of {@link IPythonScriptRegistry} simply using maps to perform 1:1 mapping.
 */
public class PythonScriptRegistry extends ScriptRegistry implements IPythonScriptRegistry {

	/** List of framework files that should be ignored by script registry. */
	private static final List<String> IGNORED_FILES = Arrays.asList(new String[] { "cp1252.py", "bdb.py", "ast.py", "threading.py" });

	/** Lookup from {@link Script} in EASE world to {@link String} in Python world */
	private final Map<Script, String> fScriptMap = new HashMap<>();

	/** Reverse lookup from {@link String} in Python world to {@link Script} in EASE world */
	private final Map<String, Script> fStringMap = new HashMap<>();

	@Override
	public void put(Script script) {
		// IResource <-> Script mapping
		super.put(script);

		// Script <-> String mapping
		final String reference = uid(script);
		fStringMap.put(reference, script);
		fScriptMap.put(script, reference);

	}

	@Override
	public Script getScript(String reference) {
		Script script = fStringMap.get(reference);
		if (script == null) {
			final File file = new File(reference);
			if (file.exists()) {
				if (!IGNORED_FILES.contains(file.getName())) {
					script = new Script(file);
					put(script);
				}
			}
		}

		return script;
	}

	@Override
	public String getReference(Script script) {
		return fScriptMap.get(script);
	}

	/**
	 * Creates a unique reference identifier for the given script.
	 *
	 * @param script
	 *            Script to get unique identifier for.
	 * @return Unique identifer for script.
	 */
	private String uid(final Script script) {
		final Set<String> existingKeys = fStringMap.keySet();
		final StringBuilder buffer = new StringBuilder("__ref_");
		buffer.append(script.isDynamic() ? "dyn" : script.getCommand().toString());
		buffer.append("_");

		for (int index = 0; index < 10; index++)
			buffer.append((char) ('a' + new Random().nextInt(26)));

		if (existingKeys.contains(buffer.toString()))
			return uid(script);

		return buffer.toString();
	}

}
