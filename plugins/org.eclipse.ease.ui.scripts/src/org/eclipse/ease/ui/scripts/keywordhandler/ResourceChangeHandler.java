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

package org.eclipse.ease.ui.scripts.keywordhandler;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Pattern;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResourceChangeEvent;
import org.eclipse.core.resources.IResourceChangeListener;
import org.eclipse.core.resources.IResourceDelta;
import org.eclipse.core.resources.IResourceDeltaVisitor;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.urlhandler.WorkspaceURLConnection;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class ResourceChangeHandler implements EventHandler, IResourceChangeListener {

	private static List<String> createPattern(final String fileMask) {
		List<String> result = new ArrayList<String>();

		for (String token : fileMask.split(","))
			result.add(token.startsWith("^") ? token : token.replaceAll("\\*", ".*"));

		return result;
	}

	private final Map<String, Collection<IScript>> fRegisteredScripts = new HashMap<String, Collection<IScript>>();

	public ResourceChangeHandler() {
	}

	@Override
	public void handleEvent(final Event event) {

		final IScript script = (IScript) event.getProperty("script");
		String value = (String) event.getProperty("value");
		String oldValue = (String) event.getProperty("oldValue");

		if (oldValue != null) {
			for (String pattern : createPattern(oldValue)) {
				if (fRegisteredScripts.containsKey(pattern)) {
					Collection<IScript> scripts = fRegisteredScripts.get(pattern);
					scripts.remove(script);
					if (scripts.isEmpty())
						fRegisteredScripts.remove(pattern);
				}
			}
		}

		if (value != null) {
			for (String pattern : createPattern(value)) {
				if (!fRegisteredScripts.containsKey(pattern))
					fRegisteredScripts.put(pattern, new HashSet<IScript>());

				fRegisteredScripts.get(pattern).add(script);
			}
		}

		if (fRegisteredScripts.isEmpty())
			ResourcesPlugin.getWorkspace().removeResourceChangeListener(this);
		else
			ResourcesPlugin.getWorkspace().addResourceChangeListener(this);
	}

	@Override
	public void resourceChanged(final IResourceChangeEvent event) {
		try {
			event.getDelta().accept(new IResourceDeltaVisitor() {

				@Override
				public boolean visit(final IResourceDelta delta) throws CoreException {
					if ((delta.getResource() instanceof IFile) && (getKind(delta.getKind()) != null)) {
						// directly create the location as we know it is an IFile and we cannot be sure that the resource is still available
						String location = WorkspaceURLConnection.SCHEME + ":/" + delta.getResource().getFullPath().toPortableString();

						for (Entry<String, Collection<IScript>> entry : fRegisteredScripts.entrySet()) {
							if (Pattern.matches(entry.getKey(), location)) {
								// execute registered scripts
								for (IScript script : entry.getValue())
									script.run(location, getKind(delta.getKind()));
							}
						}
					}

					return true;
				}

				private String getKind(final int kind) {
					switch (kind) {
					case IResourceDelta.ADDED:
						return "added";
					case IResourceDelta.CHANGED:
						return "changed";
					case IResourceDelta.REMOVED:
						return "removed";
					default:
						return null;
					}
				}
			});
		} catch (CoreException e) {
			// TODO handle this exception (but for now, at least know it happened)
			throw new RuntimeException(e);
		}
	}
}
