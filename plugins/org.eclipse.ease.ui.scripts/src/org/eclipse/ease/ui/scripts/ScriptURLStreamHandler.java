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
import java.net.URL;
import java.net.URLConnection;

import org.eclipse.core.runtime.Path;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ui.PlatformUI;
import org.osgi.service.url.AbstractURLStreamHandlerService;

public class ScriptURLStreamHandler extends AbstractURLStreamHandlerService {

	@Override
	public URLConnection openConnection(URL url) throws IOException {
		final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
		if (repositoryService != null) {
			final IScript script = repositoryService.getScript(new Path(url.getHost() + url.getFile()).makeAbsolute().toString());

			if (script != null)
				return new ScriptURLConnection(url, script);

			throw new IOException("\"" + url + "\" not found");
		}

		return null;
	}
}
