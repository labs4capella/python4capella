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
package org.eclipse.ease.ui.scripts.repository;

import java.util.Collection;

import org.eclipse.core.runtime.Platform;
import org.eclipse.ease.ui.scripts.Activator;

/**
 * Global service to register user scripts and to query for registered scripts. To get the service instance use
 *
 * <pre>
 * final IRepositoryService repositoryService = (IRepositoryService) PlatformUI.getWorkbench().getService(IRepositoryService.class);
 * </pre>
 */
public interface IRepositoryService {

	/** Base channel for all script events. */
	String BROKER_CHANNEL_SCRIPTS_BASE = "org/eclipse/ease/scripts/";

	/** Channel to promote new detected user scripts. */
	String BROKER_CHANNEL_SCRIPTS_NEW = BROKER_CHANNEL_SCRIPTS_BASE + "new";

	/** Channel to promote script executions on. */
	String BROKER_CHANNEL_SCRIPTS_RUN = BROKER_CHANNEL_SCRIPTS_BASE + "run";

	/** Channel to promote when user scripts are removed. */
	String BROKER_CHANNEL_SCRIPTS_REMOVED = BROKER_CHANNEL_SCRIPTS_BASE + "removed";

	/** Channel to promote all keyword changes from user scripts. */
	String BROKER_CHANNEL_SCRIPT_KEYWORDS = BROKER_CHANNEL_SCRIPTS_BASE + "keyword/";

	/** Trace enablement for the repository service. */
	boolean TRACE_REPOSITORY_SERVICE = Activator.getDefault().isDebugging()
			&& "true".equalsIgnoreCase(Platform.getDebugOption(Activator.PLUGIN_ID + "/debug/repositoryService"));

	/**
	 * Trigger an immediate refresh of all script sources and contained scripts.
	 *
	 * @param force
	 *            force the update when set to <code>true</code>
	 */
	void update(boolean force);

	void updateLocation(IScriptLocation location, String scriptURI, long lastChanged);

	/**
	 * Get all scripts registered with this service.
	 *
	 * @return collection of scripts
	 */
	Collection<IScript> getScripts();

	/**
	 * Get a script by providing its full name.
	 *
	 * @param name
	 *            full name of script (including path)
	 * @return script instance
	 */
	IScript getScript(String name);

	/**
	 * Get all script locations currently registered.
	 *
	 * @return registered script locations
	 */
	Collection<IScriptLocation> getLocations();

	/**
	 * Add a new script location to the repository. Takes care that the same location is not registered yet. If a location with the same URI is already
	 * registered, we update its flags (defaultLocation, recursive).
	 *
	 * @param locationURI
	 *            location URI to register
	 * @param defaultLocation
	 *            set to true to be the default location for scripts
	 * @param recursive
	 *            <code>true</code> to parse subfolders of location
	 */
	void addLocation(String locationURI, boolean defaultLocation, boolean recursive);

	/**
	 * Remove a give location from the repository. Removes the location and all scripts registered under that location.
	 *
	 * @param locationURI
	 *            location URI to unregister
	 */
	void removeLocation(String locationURI);
}
