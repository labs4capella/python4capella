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
package org.eclipse.ease.ui.scripts;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.InputStream;

import org.eclipse.core.resources.IStorage;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.ui.IPersistableElement;
import org.eclipse.ui.IStorageEditorInput;
import org.eclipse.ui.plugin.AbstractUIPlugin;

public class ScriptEditorInput implements IStorageEditorInput {

	private final String fName;
	private final InputStream fContent;
	private final IScript fScript;

	public ScriptEditorInput(final IScript script) {
		fScript = script;
		fName = script.getName();
		fContent = null;
	}

	public ScriptEditorInput(final String name, final String content) {
		fName = name;
		fContent = new ByteArrayInputStream(content.getBytes());
		fScript = null;
	}

	@Override
	public final boolean equals(final Object other) {
		return (other instanceof ScriptEditorInput) && fName.equals(((ScriptEditorInput) other).fName);
	}

	@Override
	public final Object getAdapter(final Class adapter) {
		return null;
	}

	@Override
	public final IPersistableElement getPersistable() {
		return null;
	}

	@Override
	public final boolean exists() {
		return true;
	}

	@Override
	public final IStorage getStorage() {
		return new IStorage() {
			@Override
			public Object getAdapter(final Class adapter) {
				return null;
			}

			@Override
			public boolean isReadOnly() {
				return (fScript != null) ? fScript.isRemote() : false;
			}

			@Override
			public String getName() {
				return fName;
			}

			@Override
			public IPath getFullPath() {
				if (fScript != null) {
					final Object content = fScript.getResource();
					if (content instanceof File)
						return new Path(((File) content).getPath());
				}

				return null;
			}

			@Override
			public InputStream getContents() throws CoreException {
				if (fScript != null)
					return fScript.getInputStream();

				return fContent;
			}
		};
	}

	@Override
	public final ImageDescriptor getImageDescriptor() {
		return AbstractUIPlugin.imageDescriptorFromPlugin(org.eclipse.ease.ui.Activator.PLUGIN_ID, "/images/eobj16/script.gif");
	}

	@Override
	public final String getName() {
		return "Script: " + fName;
	}

	@Override
	public final String getToolTipText() {
		return "Script editor";
	}
}
