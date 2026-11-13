/*******************************************************************************
 * Copyright (c) 2013 Christian Pontesegger and others.
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
package org.eclipse.ease.lang.python.debugger.model;

import org.eclipse.core.resources.IFile;
import org.eclipse.debug.core.model.IValue;
import org.eclipse.debug.ui.IDebugModelPresentation;
import org.eclipse.debug.ui.IValueDetailListener;
import org.eclipse.ease.Script;
import org.eclipse.ease.ui.debugging.model.AbstractEaseDebugModelPresentation;
import org.eclipse.ui.IEditorDescriptor;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IEditorRegistry;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.editors.text.EditorsUI;

public class PythonDebugModelPresentation extends AbstractEaseDebugModelPresentation implements IDebugModelPresentation {

	@Override
	public String getEditorId(final IEditorInput input, final Object element) {
		if (element instanceof Script) {
			final Object file = ((Script) element).getFile();
			IEditorDescriptor editor;

			if (file instanceof IFile)
				// try to find native editor
				editor = PlatformUI.getWorkbench().getEditorRegistry().getDefaultEditor(((IFile) file).getName());
			else
				// use PY default editor
				editor = PlatformUI.getWorkbench().getEditorRegistry().getDefaultEditor("foo.py");

			if (editor != null)
				return editor.getId();

			// use default text editor
			editor = PlatformUI.getWorkbench().getEditorRegistry().findEditor(EditorsUI.DEFAULT_TEXT_EDITOR_ID);
			if (editor != null)
				return editor.getId();

			// use system default editor
			return IEditorRegistry.SYSTEM_EXTERNAL_EDITOR_ID;
		}

		return null;
	}

	@Override
	public void computeDetail(final IValue value, final IValueDetailListener listener) {
		final Object adapter = value.getAdapter(String.class);
		if (adapter instanceof String)
			listener.detailComputed(value, (String) adapter);
	}
}
