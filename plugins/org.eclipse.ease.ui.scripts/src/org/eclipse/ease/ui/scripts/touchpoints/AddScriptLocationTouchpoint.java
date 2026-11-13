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
package org.eclipse.ease.ui.scripts.touchpoints;

import java.util.Map;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.equinox.p2.engine.spi.ProvisioningAction;
import org.eclipse.ui.PlatformUI;

/**
 * Touchpoint to register a new script location. Requires parameter <i>location</i> which contains the absolute location to be registered.
 * <p>
 * <b>How to use this touchpoint:</b><br />
 * Add a file p2.inf to the root folder of a feature project. Set the content to:<br />
 * instructions.configure = org.eclipse.ease.ui.scripts.addScriptLocation(location:platform:/plugin/your.plugin/subfolder,recursive:true);
 * </p>
 */
public class AddScriptLocationTouchpoint extends ProvisioningAction {

	@Override
	public IStatus execute(final Map<String, Object> parameters) {

		Object location = parameters.get("location");
		if (location != null) {
			boolean recursive = parameters.containsKey("recursive") ? Boolean.parseBoolean(parameters.get("recursive").toString()) : true;

			IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
			repositoryService.addLocation(location.toString(), false, recursive);
		}

		return Status.OK_STATUS;
	}

	@Override
	public IStatus undo(final Map<String, Object> parameters) {
		Object location = parameters.get("location");
		if (location != null) {
			IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
			repositoryService.removeLocation(location.toString());
		}

		return Status.OK_STATUS;
	}
}
