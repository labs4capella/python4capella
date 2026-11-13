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

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Pattern;

import org.eclipse.core.resources.IFile;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.tools.AbstractWorkbenchRunnable;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IEditorPart;
import org.eclipse.ui.IPartListener;
import org.eclipse.ui.IPartService;
import org.eclipse.ui.IPropertyListener;
import org.eclipse.ui.IWorkbenchPart;
import org.eclipse.ui.IWorkbenchPartConstants;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.FileEditorInput;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class SaveEditorHandler implements EventHandler, IPartListener, IPropertyListener {

	private static List<String> createPattern(final String fileMask) {
		final List<String> result = new ArrayList<>();

		for (final String token : fileMask.split(","))
			result.add(token.startsWith("^") ? token : token.replaceAll("\\*", ".*"));

		return result;
	}

	private final Map<String, Collection<IScript>> fRegisteredScripts = new HashMap<>();

	public SaveEditorHandler() {
		new AbstractWorkbenchRunnable() {
			@Override
			public void run() {
				initialize();
			}
		}.launch();
	}

	private void initialize() {
		final IPartService service = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getService(IPartService.class);
		service.addPartListener(this);

		if (PlatformUI.getWorkbench().getActiveWorkbenchWindow() != null) {
			final IEditorPart editor = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().getActiveEditor();
			if (editor != null)
				editor.addPropertyListener(this);
		}
	}

	@Override
	public void handleEvent(final Event event) {

		final IScript script = (IScript) event.getProperty("script");
		final String value = (String) event.getProperty("value");
		final String oldValue = (String) event.getProperty("oldValue");

		if (oldValue != null) {
			for (final String pattern : createPattern(oldValue)) {
				if (fRegisteredScripts.containsKey(pattern))
					fRegisteredScripts.get(pattern).remove(script);
			}
		}

		if (value != null) {
			for (final String pattern : createPattern(value)) {
				if (!fRegisteredScripts.containsKey(pattern))
					fRegisteredScripts.put(pattern, new HashSet<IScript>());

				fRegisteredScripts.get(pattern).add(script);
			}
		}
	}

	@Override
	public void partActivated(final IWorkbenchPart part) {
		if (part instanceof IEditorPart)
			part.addPropertyListener(this);
	}

	@Override
	public void partBroughtToTop(final IWorkbenchPart part) {
	}

	@Override
	public void partClosed(final IWorkbenchPart part) {
	}

	@Override
	public void partDeactivated(final IWorkbenchPart part) {
	}

	@Override
	public void partOpened(final IWorkbenchPart part) {
		if (part instanceof IEditorPart)
			part.addPropertyListener(this);
	}

	@Override
	public void propertyChanged(final Object source, final int propId) {
		if (propId == IWorkbenchPartConstants.PROP_DIRTY) {
			if (source instanceof IEditorPart) {
				if (!((IEditorPart) source).isDirty()) {
					final IEditorInput input = ((IEditorPart) source).getEditorInput();
					if (input instanceof FileEditorInput) {
						final IFile file = ((FileEditorInput) input).getFile();
						final String location = ResourceTools.toAbsoluteLocation(file, null);

						if (location != null) {
							for (final Entry<String, Collection<IScript>> entry : fRegisteredScripts.entrySet()) {
								if (Pattern.matches(entry.getKey(), location)) {
									// execute registered scripts
									for (final IScript script : entry.getValue())
										script.run(location);
								}
							}
						}
					}
				}
			}
		}
	}
}
