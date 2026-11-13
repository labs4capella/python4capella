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
package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.Collection;
import java.util.HashSet;

import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.tools.StringTools;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.emf.common.util.URI;
import org.eclipse.ui.PlatformUI;

public class HttpParser extends InputStreamParser {

	public void parse(final String location, final IScriptLocation entry) {
		final IScriptService scriptService = (IScriptService) PlatformUI.getWorkbench().getService(IScriptService.class);
		ScriptType scriptType = scriptService.getScriptType(location);
		if (scriptType != null) {
			// register script
			final IRepositoryService repositoryService = (IRepositoryService) PlatformUI.getWorkbench().getService(IRepositoryService.class);
			repositoryService.updateLocation(entry, location, System.currentTimeMillis());

		} else {
			try {
				InputStream stream = new URL(location).openStream();
				if (stream != null) {
					String content = StringTools.toString(stream);

					try {
						stream.close();
					} catch (IOException e) {
					}

					Collection<String> anchors = extractAnchors(location, content);

					for (String subLocation : anchors)
						parse(subLocation, entry);
				}
			} catch (IOException e) {
				// cannot read content, ignore location
				// Includes MalformedURLException, so ignore invalid URLs

			}
		}
	}

	private Collection<String> extractAnchors(final String base, final String content) {
		Collection<String> anchorNodes = new HashSet<String>();

		URI baseURI = URI.createURI(base);
		if (baseURI.fileExtension() != null) {
			// base refers to a file, not a folder
			baseURI = baseURI.trimSegments(1);
		}

		if (baseURI.hasTrailingPathSeparator())
			baseURI = baseURI.trimSegments(1);

		int pos = content.indexOf(" href=");
		do {
			if (pos != -1) {
				int endpos = content.indexOf(content.charAt(pos + 6), pos + 7);
				if (content.charAt(pos + 7) != '#') {
					URI candidate = URI.createURI(content.substring(pos + 7, endpos));
					if (candidate.isRelative())
						candidate = candidate.resolve(baseURI);

					if (candidate.hasTrailingPathSeparator())
						candidate = candidate.trimSegments(1);

					if (candidate.toString().startsWith(baseURI.toString())) {
						// candidate is stored below the base

						if (candidate.segmentCount() > baseURI.segmentCount())
							anchorNodes.add(candidate.toString());
					}
				}
			}

			pos = content.indexOf(" href=", pos + 1);

		} while (pos != -1);

		// make sure we do not recursive load the same page over and over
		anchorNodes.remove(base);

		return anchorNodes;
	}
}
