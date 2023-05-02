/**
 *   Copyright (c) 2022 THALES GLOBAL SERVICES
 *  This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License 2.0
 *  which accompanies this distribution, and is available at
 *  https://www.eclipse.org/legal/epl-2.0/
 *
 *  SPDX-License-Identifier: EPL-2.0
 *
 *  Contributors:
 *       Obeo - Initial API and implementation
 */
package org.eclipse.python4capella.pydev;

import java.io.IOException;
import java.util.Set;
import java.util.StringJoiner;

import org.eclipse.core.runtime.preferences.InstanceScope;
import org.eclipse.ui.IStartup;
import org.eclipse.ui.preferences.ScopedPreferenceStore;

import com.python.pydev.analysis.AnalysisPreferenceInitializer;
import com.python.pydev.analysis.AnalysisPreferences;

/**
 * Checks Pydev analysis preferences for EASE keywords.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class Startup implements IStartup {

	public static final String INCLUDE = "include";

	public static final String LOAD_MODULE = "loadModule";

	public static final String ARGV = "argv";

	public static final String ALREADY_VERIFIED = "ALREADY_VERIFIED";

	private final ScopedPreferenceStore preferenceStore = new ScopedPreferenceStore(InstanceScope.INSTANCE,
			Activator.PLUGIN_ID);

	/**
	 * Tells if the verification has already be done.
	 * 
	 * @return <code>true</code> if the verification has already be done,
	 *         <code>false</code> otherwise
	 */
	public boolean isAlreadyVerified() {
		return preferenceStore.getBoolean(ALREADY_VERIFIED);
	}

	/**
	 * Sets the verification already done.
	 * 
	 * @param alreadyVerified <code>true</code> if the verification has already be
	 *                        done, <code>false</code> otherwise
	 */
	public void setAlreadyVerified(boolean alreadyVerified) {
		preferenceStore.setValue(ALREADY_VERIFIED, alreadyVerified);
		try {
			preferenceStore.save();
		} catch (IOException e) {
			Activator.log(e, false);
		}
	}

	@Override
	public void earlyStartup() {

		if (!isAlreadyVerified()) {
			final AnalysisPreferences preferences = new AnalysisPreferences(null);
			final ScopedPreferenceStore analysisPreferenceStore = new ScopedPreferenceStore(InstanceScope.INSTANCE,
					AnalysisPreferenceInitializer.DEFAULT_SCOPE);
			final Set<String> keywords = preferences.getTokensAlwaysInGlobals();

			if (keywords != null) {
				final StringJoiner joiner = new StringJoiner(",");
				for (String keyword : keywords) {
					joiner.add(keyword);
				}

				if (!keywords.contains(INCLUDE)) {
					joiner.add(INCLUDE);
				}
				if (!keywords.contains(LOAD_MODULE)) {
					joiner.add(LOAD_MODULE);
				}
				if (!keywords.contains(ARGV)) {
					joiner.add(ARGV);
				}

				analysisPreferenceStore.setValue(AnalysisPreferenceInitializer.NAMES_TO_CONSIDER_GLOBALS,
						joiner.toString());
				setAlreadyVerified(true);
			}
		}

	}

}
