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

import java.util.Collection;
import java.util.HashSet;

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.IWorkbenchListener;
import org.eclipse.ui.PlatformUI;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class ShutdownHandler implements EventHandler, IWorkbenchListener {

	private class ShutdownJob extends Job {

		public ShutdownJob() {
			super("Wait for shutdown scripts");
		}

		@Override
		protected IStatus run(final IProgressMonitor monitor) {
			// wait for engines to be completed
			for (final IScriptEngine engine : fEngines) {
				final long timeout = (fStartTime + fShutdownTimeout) - System.currentTimeMillis();
				if (timeout > 0) {
					try {
						engine.joinEngine(timeout);
					} catch (final InterruptedException e) {
					}
				} else
					break;
			}

			// terminate engines that are not completed
			for (final IScriptEngine engine : fEngines) {
				if (!engine.isFinished())
					engine.terminate();
			}

			// call final shutdown
			Display.getDefault().asyncExec(() -> {
				fShutdownScripts.clear();
				PlatformUI.getWorkbench().close();
			});

			return Status.OK_STATUS;
		}
	}

	/** Registered shutdown scripts. */
	Collection<IScript> fShutdownScripts = new HashSet<>();

	/** Default script timeout: 10s. */
	private long fShutdownTimeout = 10 * 1000;

	/** Running engines for shutdown scripts. */
	Collection<IScriptEngine> fEngines = null;

	/** Start timestamp for shutdown script execution. */
	private long fStartTime;

	@Override
	public void handleEvent(final Event event) {
		final IScript script = (IScript) event.getProperty("script");
		final String value = (String) event.getProperty("value");

		if (value == null)
			fShutdownScripts.remove(script);
		else {
			fShutdownScripts.add(script);

			if (!value.isEmpty()) {
				try {
					fShutdownTimeout = Math.max(fShutdownTimeout, Integer.parseInt(value) * 1000);
				} catch (final NumberFormatException e) {
					Logger.error(Activator.PLUGIN_ID, "Invalid onShutdown timeout for script: " + script.getLocation());
				}
			}
		}

		if (fShutdownScripts.isEmpty())
			PlatformUI.getWorkbench().removeWorkbenchListener(this);
		else
			PlatformUI.getWorkbench().addWorkbenchListener(this);
	}

	@Override
	public boolean preShutdown(final IWorkbench workbench, final boolean forced) {
		if ((!forced) && (!fShutdownScripts.isEmpty())) {
			fStartTime = System.currentTimeMillis();
			fEngines = new HashSet<>();
			for (final IScript script : fShutdownScripts)
				fEngines.add(script.run());

			new ShutdownJob().schedule();

			return false;
		}

		return true;
	}

	@Override
	public void postShutdown(final IWorkbench workbench) {
	}
}
