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

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.IScriptEngineLaunchExtension;
import org.eclipse.ease.Script;
import org.eclipse.ease.modules.EnvironmentModule;

/**
 * Loads basic module support for script Py4J based engines.
 */
public class Py4JBootstrap implements IScriptEngineLaunchExtension {

	private static final String BOOTSTRAP_CODE = EnvironmentModule.class.getName() + "().bootstrap()";

	@Override
	public void createEngine(final IScriptEngine engine) {
		engine.execute(new Script(Py4JBootstrap.class.getSimpleName(), BOOTSTRAP_CODE));
	}
}
