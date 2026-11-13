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

import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IResourceVisitor;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ui.PlatformUI;

public class WorkspaceParser extends InputStreamParser {

	public void parse(final IResource resource, final IScriptLocation entry) {
		if (resource instanceof IContainer) {
			// containment, parse children
			try {
				resource.accept(new IResourceVisitor() {

					@Override
					public boolean visit(final IResource resource) throws CoreException {

						if (resource instanceof IFile)
							parse(resource, entry);

						return entry.isRecursive();
					}

				}, entry.isRecursive() ? IResource.DEPTH_INFINITE : IResource.DEPTH_ONE, 0);
			} catch (CoreException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		} else if (resource instanceof IFile) {
			// try to locate registered script
			String location = "workspace:/" + resource.getFullPath();

			final IRepositoryService repositoryService = (IRepositoryService) PlatformUI.getWorkbench().getService(IRepositoryService.class);
			repositoryService.updateLocation(entry, location, resource.getModificationStamp());
		}
	}
}
