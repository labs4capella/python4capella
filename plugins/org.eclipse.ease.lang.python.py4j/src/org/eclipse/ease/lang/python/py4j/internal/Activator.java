/*******************************************************************************
 * Copyright (c) 2016 Kichwa Coders and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Jonah Graham (Kichwa Coders) - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.py4j.internal;

import org.eclipse.ui.plugin.AbstractUIPlugin;
import org.osgi.framework.BundleContext;

public class Activator extends AbstractUIPlugin {

	public static final String PLUGIN_ID = "org.eclipse.ease.lang.python.py4j";

	// The shared instance
	private static Activator fPlugin;

	@Override
	public void start(final BundleContext context) throws Exception {
		super.start(context);
		fPlugin = this;
	}

	@Override
	public void stop(final BundleContext context) throws Exception {
		fPlugin = null;
		super.stop(context);
	}

	public static Activator getDefault() {
		return fPlugin;
	}

}
