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

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class StartupHandler implements EventHandler {

	@Override
	public void handleEvent(final Event event) {
		final IScript script = (IScript) event.getProperty("script");
		String value = (String) event.getProperty("value");
		String oldValue = (String) event.getProperty("oldValue");

		// check oldValue to not execute on keyword changes
		if ((!value.isEmpty()) && (oldValue == null)) {
			int delay = 0;
			try {
				delay = Integer.parseInt(value);
			} catch (NumberFormatException e) {
				Logger.error(Activator.PLUGIN_ID, "Invalid onStartup delay for script: " + script.getLocation());
			}

			if (delay > 0) {
				new Job("Startup script execution") {

					@Override
					protected IStatus run(final IProgressMonitor monitor) {
						script.run();
						return Status.OK_STATUS;
					}
				}.schedule(delay * 1000);

			} else
				// scripts spawn their own thread so we may run them directly
				script.run();
		}
	}
}
