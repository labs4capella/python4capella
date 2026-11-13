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

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;

import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.Logger;

public class FileScriptStorage extends ScriptStorage {

	public FileScriptStorage(final String location) {
		super(location);
	}

	@Override
	protected boolean createFile(final Path path, final String content) {
		URI uri = URI.create(new Path(getLocation()).append(path).toString().replace(" ", "%20"));
		File file = new File(uri);

		try {
			if (!file.exists()) {
				if (file.createNewFile()) {

					FileOutputStream outputStream = null;
					try {
						outputStream = new FileOutputStream(file);
						outputStream.write(content.getBytes());
						return true;

					} catch (Exception e) {
						Logger.error(Activator.PLUGIN_ID, "Could not store recorded script.", e);
					} finally {
						if (outputStream != null) {
							try {
								outputStream.close();
							} catch (IOException e) {
								// giving up
							}
						}
					}
				}
			}
		} catch (IOException e) {
			Logger.error(Activator.PLUGIN_ID, "Could not create file", e);
		}

		return false;
	}

	@Override
	protected boolean createPath(final IPath path) {
		// TODO find a better way to encode URIs correctly
		File file = new File(URI.create((getLocation() + "/" + path).replace(" ", "%20")));
		if (!file.exists())
			return file.mkdirs();

		return true;
	}
}
