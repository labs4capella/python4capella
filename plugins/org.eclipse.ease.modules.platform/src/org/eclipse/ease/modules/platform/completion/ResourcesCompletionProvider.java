/*******************************************************************************
 * Copyright (c) 2015 Christian Pontesegger and others.
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
package org.eclipse.ease.modules.platform.completion;

import org.eclipse.ease.ICompletionContext;
import org.eclipse.ease.modules.platform.ScriptingModule;
import org.eclipse.ease.modules.platform.UIModule;
import org.eclipse.ease.modules.platform.resources.ResourcesModule;
import org.eclipse.ease.ui.completion.provider.AbstractFileLocationCompletionProvider;

public class ResourcesCompletionProvider extends AbstractFileLocationCompletionProvider {

	@Override
	public boolean isActive(final ICompletionContext context) {
		if (super.isActive(context))
			return isMethodFromResources(context) || isMethodFromScripting(context) || isMethodFromUi(context);

		return false;
	}

	private boolean isMethodFromUi(final ICompletionContext context) {
		if (context.getLoadedModules().contains(getModuleDefinition(UIModule.MODULE_ID)))
			return isMethodParameter(context, "showEditor", 0) || isMethodParameter(context, "openEditor", 0);

		return false;
	}

	private boolean isMethodFromScripting(final ICompletionContext context) {
		if (context.getLoadedModules().contains(getModuleDefinition(ScriptingModule.MODULE_ID)))
			return isMethodParameter(context, "fork", 0);

		return false;
	}

	private boolean isMethodFromResources(final ICompletionContext context) {
		if (context.getLoadedModules().contains(getModuleDefinition(ResourcesModule.MODULE_ID))) {
			return isMethodParameter(context, "copyFile", 0) || isMethodParameter(context, "copyFile", 1) || isMethodParameter(context, "createFile", 0)
					|| isMethodParameter(context, "createFolder", 0) || isMethodParameter(context, "deleteFile", 0)
					|| isMethodParameter(context, "deleteFolder", 0) || isMethodParameter(context, "fileExists", 0)
					|| isMethodParameter(context, "findFiles", 1) || isMethodParameter(context, "getFile", 0) || isMethodParameter(context, "openFile", 0)
					|| isMethodParameter(context, "readFile", 0) || isMethodParameter(context, "writeFile", 0)
					|| isMethodParameter(context, "createProblemMarker", 1);
		}

		return false;
	}

	@Override
	protected boolean showCandidate(final Object candidate) {
		if (isMethodFromUi(getContext()))
			return !isFileSystemResource(candidate);

		if (isMethodParameter(getContext(), "createFile", 0) || isMethodParameter(getContext(), "createFolder", 0)
				|| isMethodParameter(getContext(), "deleteFolder", 0) || isMethodParameter(getContext(), "findFiles", 1))
			return !isFile(candidate);

		return super.showCandidate(candidate);
	}
}