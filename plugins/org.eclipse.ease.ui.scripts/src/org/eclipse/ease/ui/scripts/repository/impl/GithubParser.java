/*******************************************************************************
 * Copyright (c) 2017 Utsav Oza and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Utsav Oza - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

import org.eclipse.core.runtime.Platform;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ui.PlatformUI;
import org.osgi.framework.Bundle;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class GithubParser {

	private static final String BASE_URL = "https://api.github.com/repos";
	private static final String RAW_CONTENT_BASE_URL = "https://raw.githubusercontent.com";
	private static final String CONTENT = "contents";
	private static final String GIT = "git";
	private static final String GIT_EXTENSION = ".git";
	private static final String TREE = "trees";
	private static final String RECURSIVE = "?recursive=1";
	private static final String BRANCH = "master";
	private static final String BLOB = "blob";
	private static final String SEPARATOR = "/";
	private static final String JSON_TREE_LABEL = "tree";
	private static final String JSON_PATH_LABEL = "path";
	private static final String JSON_SHA_LABEL = "sha";
	private static final String JSON_TYPE_LABEL = "type";
	private static final String JSON_BLOB_LABEL = "blob";

	public static boolean checkBundle() {
		final Bundle gsonBundle = Platform.getBundle("com.google.gson");
		if (gsonBundle == null) {
			Logger.info(Activator.PLUGIN_ID, "Bundle: com.google.gson is not loaded");
			return false;
		} else {
			Logger.info(Activator.PLUGIN_ID, "Bundle: com.google.gson is loaded");
			return true;
		}
	}

	/* This regex strictly validates the Github clone url, visualize it here: https://www.debuggex.com/r/4up7OqFnL7OvfReR */
	public static boolean isLocationValid(String location) {
		if (location == null)
			return false;

		final String regex = "(http(s)?)(://)((www.)?github.com)(/)([\\w]+(-+(\\w)+)*)(/)(\\w|_|-|.)+(.git)$";
		return Pattern.matches(regex, location);
	}

	public void parse(String location, IScriptLocation entry) {
		final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
		final Map<String, String> scripts = fetchRemoteScripts(location, entry.isRecursive());
		for (final Map.Entry<String, String> script : scripts.entrySet()) {
			final String scriptUrl = getRawContentUrl(location, script.getValue()).replaceAll(" ", "%20");
			repositoryService.updateLocation(entry, scriptUrl, new Date().getTime()); // Timestamp needs to be String yet.
		}
	}

	/**
	 * Fetches script locations relative to the project and their latest commit hashes.
	 *
	 * @param location
	 *            repository url
	 * @param isRecursive
	 *            set <code>true</code> to obtain scripts from repository recursively
	 * @return a map that maps script's latest commit hash(SHA) to their relative location
	 */
	private Map<String, String> fetchRemoteScripts(String location, boolean isRecursive) {
		final Map<String, String> scripts = new HashMap<>();
		final String contentTreeUrl = getContentTreeUrl(location);
		final JsonParser jsonParser = new JsonParser();
		try (Reader reader = new InputStreamReader(new URL(contentTreeUrl).openStream(), StandardCharsets.UTF_8)) {
			final JsonObject rootObject = jsonParser.parse(reader).getAsJsonObject();
			if (rootObject == null)
				return scripts; // return empty map
			final JsonArray projectTree = rootObject.getAsJsonArray(JSON_TREE_LABEL);
			if (projectTree == null)
				return scripts; // return empty map
			for (final JsonElement element : projectTree) {
				final JsonObject object = element.getAsJsonObject();
				if (object == null)
					continue; // continue with the next json entry in the response
				final String scriptPath = object.get(JSON_PATH_LABEL).getAsString();
				final String scriptName = (scriptPath.contains(SEPARATOR)) ? getScriptName(scriptPath) : scriptPath;
				final String scriptSHA = object.get(JSON_SHA_LABEL).getAsString();
				final String scriptType = object.get(JSON_TYPE_LABEL).getAsString();

				if ((scriptType == null) && (scriptName == null) && (scriptSHA == null) && (scriptType == null))
					continue; // if either value is missing then ignore the script

				if (JSON_BLOB_LABEL.equals(scriptType)) {
					final String repositoryName = getRepositoryName(location);
					final String relativeScriptPath = getRelativeScriptPath(location);
					if (repositoryName != null) {
						if (isRecursive) {
							if ((((repositoryName.equals(relativeScriptPath))) || scriptPath.startsWith(relativeScriptPath))) {
								scripts.put(scriptSHA, scriptPath);
							}
						} else if ((repositoryName.equals(relativeScriptPath) && !scriptPath.contains(SEPARATOR))
								|| (scriptPath.endsWith(relativeScriptPath + SEPARATOR + scriptName))) {
							scripts.put(scriptSHA, scriptPath);
						}
					}
				}

			}
		} catch (final IOException e) {
			Logger.error(Activator.PLUGIN_ID, "Unable to fetch content: " + e.getMessage());
		}
		return scripts;
	}

	/**
	 * Extracts the repository name from the validated location.
	 *
	 * @param location
	 *            repository url
	 * @return repository name, or null if location is not a valid Github repository url
	 */
	private String getRepositoryName(String location) {
		final String[] tokens = location.split(SEPARATOR);
		if (tokens.length >= 5)
			return (location.endsWith(GIT_EXTENSION)) ? tokens[4].substring(0, tokens[4].length() - 4) : tokens[4].substring(0);
		return null;
	}

	private String getRelativeScriptPath(String location) {
		final String[] tokens = location.split(SEPARATOR);
		String relativeScriptPath = tokens[tokens.length - 1].replaceAll("%20", " ");
		if (relativeScriptPath.endsWith(GIT_EXTENSION))
			relativeScriptPath = relativeScriptPath.substring(0, relativeScriptPath.length() - GIT_EXTENSION.length());
		return relativeScriptPath;
	}

	private String getScriptName(String path) {
		if (path != null)
			return path.substring(path.lastIndexOf(SEPARATOR) + 1, path.length());
		return null;
	}

	/**
	 * Constructs the raw content url for a given script.
	 *
	 * @param location
	 *            repository url
	 * @param scriptRelativePath
	 *            relative path of the script
	 * @return raw content url of the script
	 */
	private String getRawContentUrl(String location, String scriptRelativePath) {
		final StringBuilder rawContentUrl = new StringBuilder(RAW_CONTENT_BASE_URL);
		final String[] tokens = location.split(SEPARATOR);
		final String userName = tokens[3];
		final String repositoryName = getRepositoryName(location);

		rawContentUrl.append(SEPARATOR + userName);
		rawContentUrl.append(SEPARATOR + repositoryName);
		rawContentUrl.append(SEPARATOR + BRANCH);
		rawContentUrl.append(SEPARATOR + scriptRelativePath);

		return rawContentUrl.toString();
	}

	/**
	 * Constructs the content tree url that is used to obtain the complete project tree as a json response.
	 *
	 * @param location
	 *            repository url
	 * @return content tree url
	 */
	private String getContentTreeUrl(String location) {
		final StringBuilder contentTreeUrl = new StringBuilder(BASE_URL);
		final String[] tokens = location.split(SEPARATOR);
		final String userName = tokens[3];
		final String repositoryName = tokens[4].endsWith(GIT_EXTENSION) ? tokens[4].substring(0, tokens[4].length() - 4) : tokens[4];

		contentTreeUrl.append(SEPARATOR + userName);
		contentTreeUrl.append(SEPARATOR + repositoryName);
		contentTreeUrl.append(SEPARATOR + GIT);
		contentTreeUrl.append(SEPARATOR + TREE);
		contentTreeUrl.append(SEPARATOR + BRANCH + RECURSIVE);

		return contentTreeUrl.toString();
	}
}