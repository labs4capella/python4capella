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
package org.eclipse.ease.modules.platform;

import org.eclipse.ease.modules.WrapToScript;
import org.osgi.framework.Bundle;
import org.osgi.framework.BundleContext;
import org.osgi.framework.BundleException;

/**
 * Provides access to the OSGI runtime.
 */
public class OsgiModule {

	private static BundleContext getContext() {
		return org.eclipse.ease.Activator.getDefault().getContext();
	}

	/**
	 * Install a bundle from a given location.
	 *
	 * @param url
	 *            install location URI
	 * @return bundle instance or null
	 * @throws BundleException
	 *             if the installation failed. BundleException types thrown by this method include: BundleException.READ_ERROR ,
	 *             BundleException.DUPLICATE_BUNDLE_ERROR, BundleException.MANIFEST_ERROR, and BundleException.REJECTED_BY_HOOK. SecurityException - If the
	 *             caller does not have the appropriate AdminPermission[installed bundle,LIFECYCLE], and the Java Runtime Environment supports permissions.
	 *             IllegalStateException - If this BundleContext is no longer valid.
	 */
	@WrapToScript
	public Bundle installBundle(String url) throws BundleException {
		return getContext().installBundle(url);
	}

	/**
	 * Get a bundle instance. If the bundle is registered in the OSGI runtime, the bundle instance is returned
	 *
	 * @param name
	 *            bundle symbolic name to look for
	 * @return bundle instance or <code>null</code>
	 */
	@WrapToScript
	public Bundle getBundle(String name) {
		for (final Bundle bundle : getContext().getBundles()) {
			if (bundle.getSymbolicName().equals(name))
				return bundle;
		}

		return null;
	}
}
