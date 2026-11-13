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
package org.eclipse.ease.ui.scripts.preferences;

import java.util.Collection;
import java.util.HashSet;

import org.eclipse.core.filesystem.URIUtil;
import org.eclipse.core.runtime.preferences.IEclipsePreferences;
import org.eclipse.core.runtime.preferences.InstanceScope;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IRepositoryFactory;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.osgi.service.prefs.BackingStoreException;
import org.osgi.service.prefs.Preferences;

/**
 * Helper methods to access script storage preferences.
 */
public final class PreferencesHelper {

	/**
	 * Only static methods available, do not create instance.
	 */
	@Deprecated
	private PreferencesHelper() {
	}

	/**
	 * Get the default location to store recorded/imported scripts to. If no path was defined by the user, a default path within the .metadata workspace folder
	 * is returned. As the user might change the default path also invalid entries might be returned.
	 *
	 * @return path to default script storage location
	 */
	public static String getScriptStorageLocation() {
		final String location = getUserScriptStorageLocation();
		if (location != null)
			return location;

		return getDefaultScriptStorageLocation();
	}

	/**
	 * Get the storage location for recorded/imported scripts as set by the user. If the user did not explicitly set a location, <code>null</code> is returned.
	 *
	 * @return user provided storage location or <code>null</code>
	 */
	public static String getUserScriptStorageLocation() {
		for (final IScriptLocation location : getLocations()) {
			if (location.isDefault())
				return location.getLocation();
		}

		return null;
	}

	/**
	 * Get the default location to store recorded/imported scripts to. Returns the hard-coded default location within the workspace/.metadata folder.
	 *
	 * @return path to default script storage location
	 */
	public static String getDefaultScriptStorageLocation() {
		return URIUtil.toURI(Activator.getDefault().getStateLocation().append("recordedScripts")).toASCIIString();
	}

	/**
	 * Returns a collection of script locations as stored in the preferences. Converts preference data to {@link IScriptLocation} elements.
	 *
	 * @return all configured script locations
	 */
	public static Collection<IScriptLocation> getLocations() {
		final Collection<IScriptLocation> locations = new HashSet<>();

		final IEclipsePreferences rootNode = InstanceScope.INSTANCE.getNode(Activator.PLUGIN_ID);

		try {
			rootNode.accept(node -> {
				if (rootNode.equals(node))
					return true;

				else {
					final String location = node.get(IPreferenceConstants.SCRIPT_STORAGE_LOCATION, "");
					if (!location.isEmpty())
						locations.add(getLocationForNode(node));

					return false;
				}
			});
		} catch (final BackingStoreException e) {
			// we were not able to load any locations, display empty view
		}

		return locations;
	}

	/**
	 * Create a location for a given preferences node. Reads preferences data to recreate the node.
	 *
	 * @param node
	 *            preferences node to read
	 * @return script location
	 */
	public static IScriptLocation getLocationForNode(final Preferences node) {
		final IScriptLocation entry = IRepositoryFactory.eINSTANCE.createScriptLocation();
		try {
			entry.setLocation(node.get(IPreferenceConstants.SCRIPT_STORAGE_LOCATION, ""));
			entry.setRecursive(node.getBoolean(IPreferenceConstants.SCRIPT_STORAGE_RECURSIVE, true));
			entry.setDefault(node.getBoolean(IPreferenceConstants.SCRIPT_STORAGE_DEFAULT, false));
		} catch (final IllegalStateException e) {
			// preferences node is deleted, we cannot recreate all its content
			entry.setLocation(node.name().replace('|', '/'));
		}

		return entry;
	}

	/**
	 * Add a script storage location to the preferences.
	 *
	 * @param entry
	 *            location to add
	 */
	public static void addLocation(final IScriptLocation entry) {
		final String path = entry.getLocation().replace('/', '|');
		final IEclipsePreferences node = InstanceScope.INSTANCE.getNode(Activator.PLUGIN_ID + "/" + path);
		node.put(IPreferenceConstants.SCRIPT_STORAGE_LOCATION, entry.getLocation());
		node.putBoolean(IPreferenceConstants.SCRIPT_STORAGE_DEFAULT, entry.isDefault());
		node.putBoolean(IPreferenceConstants.SCRIPT_STORAGE_RECURSIVE, entry.isRecursive());
	}

	/**
	 * Remove a script storage location from preferences.
	 *
	 * @param locationURI
	 *            location of storage
	 */
	public static void removeLocation(final String locationURI) {
		final String path = locationURI.replace('/', '|');
		final IEclipsePreferences node = InstanceScope.INSTANCE.getNode(Activator.PLUGIN_ID + "/" + path);
		if (node != null) {
			try {
				node.removeNode();
			} catch (final BackingStoreException e) {
				Logger.error(Activator.PLUGIN_ID, "Could not remove storage location for \"" + locationURI + "\"", e);
			}
		}
	}
}
