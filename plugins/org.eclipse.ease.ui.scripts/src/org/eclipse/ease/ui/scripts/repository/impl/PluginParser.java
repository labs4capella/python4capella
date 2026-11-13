/*******************************************************************************
 * Copyright (c) 2016 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Platform;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ui.PlatformUI;
import org.osgi.framework.Bundle;

public class PluginParser extends InputStreamParser {

	public void parse(final Object content, final IScriptLocation location) {
		if (content instanceof URI) {
			Path path = new Path(((URI) content).getPath());

			if (path.segmentCount() >= 2) {
				if ("plugin".equals(path.segment(0))) {
					File root = getBundleLocation(path.segment(1));
					if (root != null) {

						IPath rootPath = new Path(root.getAbsolutePath());
						IPath subFolder = path.removeFirstSegments(2);
						rootPath = rootPath.append(subFolder);

						if ((root != null) && (root.exists())) {
							if (root.isDirectory()) {
								// found a bundle directory to host script files
								parseFolder(rootPath.toFile(), path, location);

							} else {
								try {
									parseJar(new ZipFile(root), path, location, root.lastModified());
								} catch (Exception e) {
									Logger.error(Activator.PLUGIN_ID, "Cannot parse plugin jar: " + root.getName());
								}
							}
						}
					}
				}
			}
		}
	}

	private void parseJar(final ZipFile file, final Path path, final IScriptLocation location, final long lastModified) {
		final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);

		IPath pluginFolder = path.removeFirstSegments(2);
		Enumeration<? extends ZipEntry> elements = file.entries();
		while (elements.hasMoreElements()) {
			ZipEntry entry = elements.nextElement();

			if (!entry.isDirectory()) {
				if (!pluginFolder.isEmpty()) {
					if (pluginFolder.isPrefixOf(new Path(entry.getName())))
						repositoryService.updateLocation(location, "platform:" + path.removeLastSegments(path.segmentCount() - 2).append(entry.getName()),
								lastModified);

				} else
					repositoryService.updateLocation(location, "platform:" + path.append(entry.getName()), lastModified);
			}
		}
	}

	private void parseFolder(final File entry, final IPath path, final IScriptLocation location) {
		if (entry.isDirectory()) {
			// containment, parse children
			for (File child : entry.listFiles()) {
				if ((child.isFile()) || (location.isRecursive()))
					parseFolder(child, path.append(child.getName()), location);
			}

		} else {
			final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
			repositoryService.updateLocation(location, "platform:" + path.toString(), entry.lastModified());
		}
	}

	private File getBundleLocation(final String pluginName) {
		Bundle bundle = Platform.getBundle(pluginName);
		try {
			if (bundle != null)
				return FileLocator.getBundleFile(bundle);
		} catch (IOException e) {
		}

		return null;
	}
}
