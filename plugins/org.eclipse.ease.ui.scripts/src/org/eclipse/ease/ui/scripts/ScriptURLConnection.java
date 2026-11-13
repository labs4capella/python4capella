/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;

import org.eclipse.ease.ui.scripts.repository.IScript;

public class ScriptURLConnection extends URLConnection {

	private final IScript fScript;

	public ScriptURLConnection(final URL url, final IScript script) {
		super(url);

		fScript = script;
	}

	@Override
	public void connect() throws IOException {
	}

	@Override
	public InputStream getInputStream() throws IOException {
		return fScript.getInputStream();
	}
}
