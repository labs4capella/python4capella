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
package org.eclipse.ease.ui.scripts.handler;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.commands.IHandler;
import org.eclipse.core.resources.IFile;
import org.eclipse.ease.Logger;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.ScriptEditorInput;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ui.IEditorDescriptor;
import org.eclipse.ui.IEditorPart;
import org.eclipse.ui.IWorkbenchPage;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.ide.IDE;
import org.eclipse.ui.texteditor.AbstractDecoratedTextEditor;
import org.eclipse.ui.texteditor.AbstractTextEditor;
import org.eclipse.ui.texteditor.IDocumentProvider;

public class EditScript extends AbstractHandler implements IHandler {

	public static final String COMMAND_ID = "org.eclipse.ease.commands.script.edit";
	public static final String PARAMETER_NAME = COMMAND_ID + ".name";

	@Override
	public Object execute(final ExecutionEvent event) throws ExecutionException {
		final IScript script = RunScript.getScript(event, PARAMETER_NAME);

		if (script != null) {
			final Object content = script.getResource();
			if ((content instanceof IFile) && (((IFile) content).exists())) {
				// open editor
				final IWorkbenchPage page = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage();
				try {
					IDE.openEditor(page, (IFile) content);
				} catch (final PartInitException e) {
					Logger.error(Activator.PLUGIN_ID, "Could not open editor for file " + content, e);
				}

			} else if ((content instanceof File) && (((File) content).exists())) {
				final ScriptType type = script.getType();
				final IEditorDescriptor descriptor;
				if (type == null) {
					descriptor = null;
				} else {
					descriptor = PlatformUI.getWorkbench().getEditorRegistry().getDefaultEditor("foo." + type.getDefaultExtension());
				}
				if (descriptor != null) {
					final IWorkbenchPage page = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage();
					try {
						final ScriptEditorInput editorInput = new ScriptEditorInput(script);
						final IEditorPart editor = page.openEditor(editorInput, descriptor.getId());

						// editor will not save external script files,
						// we need to do this on our own
						editor.addPropertyListener((source, propId) -> {

							// check for changes of PROP_DIRTY from
							// true to false,
							// meaning the editor tried to save data
							if (IEditorPart.PROP_DIRTY == propId) {
								if ((editor instanceof AbstractDecoratedTextEditor) && (!editor.isDirty())) {
									final IDocumentProvider documentProvider = ((AbstractTextEditor) editor).getDocumentProvider();
									final String newSource = documentProvider.getDocument(editorInput).get();

									FileOutputStream outputStream = null;
									try {
										outputStream = new FileOutputStream((File) content);
										outputStream.write(newSource.getBytes());

									} catch (final Exception e1) {
										Logger.error(Activator.PLUGIN_ID, "Could not store recorded script.", e1);
									} finally {
										if (outputStream != null) {
											try {
												outputStream.close();
											} catch (final IOException e2) {
												// giving up
											}
										}
									}

									// refresh script in repository
									final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
									// FIXME we should only update
									// this one resource instead of
									// all scripts
									repositoryService.update(false);
								}
							}
						});

					} catch (final PartInitException e) {
						Logger.error(Activator.PLUGIN_ID, "Could not open editor for file " + content, e);
					}
				}

			} else {
				final ScriptType type = script.getType();
				final IEditorDescriptor descriptor = PlatformUI.getWorkbench().getEditorRegistry().getDefaultEditor("foo." + type.getDefaultExtension());
				if (descriptor != null) {
					final IWorkbenchPage page = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage();
					try {
						final ScriptEditorInput editorInput = new ScriptEditorInput(script);
						page.openEditor(editorInput, descriptor.getId());

					} catch (final PartInitException e) {
						Logger.error(Activator.PLUGIN_ID, "Could not open editor for file " + content, e);
					}
				}
			}
		}

		return null;
	}
}
