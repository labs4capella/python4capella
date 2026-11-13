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
package org.eclipse.ease.lang.python.debugger;

import java.io.BufferedInputStream;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.jar.JarFile;

import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.Platform;

public class ResourceHelper {

	/**
	 * Returns an {@link InputStream} for a given resource within a bundle.
	 *
	 * @param bundle
	 *            qualified name of the bundle to resolve
	 * @param path
	 *            full path of the file to load
	 * @return input stream to resource
	 * @throws IOException
	 *             on access errors on the resource
	 */
	public static InputStream getResourceStream(final String bundle, final String path) throws IOException {
		// FIXME see if we can reuse methods from ResourceTools and get rid of this helper class
		String location = Platform.getBundle(bundle).getLocation();

		if (location.toLowerCase().endsWith(".jar")) {
			// we need to open a jar file
			final int pos = location.indexOf("file:");
			if (pos != -1) {
				location = location.substring(pos + 5);
				if (!location.startsWith("/")) {
					// relative location, add full path to executable
					location = (Platform.getInstallLocation().getURL().toString() + location).substring(6);
				}
				JarFile file = null;
				try {
					file = new JarFile(location);
					if (path.startsWith("/"))
						return wrapStream(file.getInputStream(file.getEntry(path.substring(1))));
					else
						return wrapStream(file.getInputStream(file.getEntry(path)));
				} finally {
					if (file != null) {
						file.close();
					}
				}
			}

			return null;

		} else {
			final URL url = Platform.getBundle(bundle).getResource(path);
			return FileLocator.resolve(url).openStream();
		}
	}

	/**
	 * Consumes a given {@link InputStream} and returns a buffered version of the stream content. This allows to close any external resource providing the
	 * stream data.
	 *
	 * @param inputStream
	 *            original input stream
	 * @return wrapped input stream
	 * @throws IOException
	 *             on read error on the given input
	 */
	private static InputStream wrapStream(InputStream inputStream) throws IOException {
		final byte[] buffer = new byte[8192];
		final InputStream bufferedInput = new BufferedInputStream(inputStream);
		final ByteArrayOutputStream data = new ByteArrayOutputStream();

		try {
			int length = bufferedInput.read(buffer);
			while (length > 0) {
				data.write(buffer, 0, length);
				length = bufferedInput.read(buffer);
			}
		} finally {
			try {
				inputStream.close();
			} catch (final IOException e) {
				// ignore
			}
		}

		return new ByteArrayInputStream(data.toByteArray());
	}
}
