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
package org.eclipse.ease.ui.scripts.repository.impl;

import org.eclipse.ui.IStartup;

public class Startup implements IStartup {

	@Override
	public void earlyStartup() {
		// make sure the service gets started automatically
		// TODO this might be achieved by auto starting the bundle and activating the service from the bundle activator
		try {
			RepositoryService.getInstance();
		} catch (final IllegalStateException e) {
			// workbench not started, possibly we are running in headless mode?
		}
	}
}
