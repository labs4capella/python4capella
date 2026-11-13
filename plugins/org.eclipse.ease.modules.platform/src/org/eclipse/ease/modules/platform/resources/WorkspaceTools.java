/*******************************************************************************
 * Copyright (c) 2021 Christian Pontesegger and others.
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

package org.eclipse.ease.modules.platform.resources;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Pattern;

import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IMarker;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IProjectDescription;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IResourceVisitor;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.tools.RunnableWithResult;
import org.eclipse.jface.window.Window;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.dialogs.ContainerSelectionDialog;
import org.eclipse.ui.dialogs.ElementTreeSelectionDialog;
import org.eclipse.ui.dialogs.IOverwriteQuery;
import org.eclipse.ui.dialogs.SaveAsDialog;
import org.eclipse.ui.model.WorkbenchContentProvider;
import org.eclipse.ui.model.WorkbenchLabelProvider;
import org.eclipse.ui.texteditor.MarkerUtilities;
import org.eclipse.ui.views.navigator.ResourceComparator;
import org.eclipse.ui.wizards.datatransfer.FileSystemStructureProvider;
import org.eclipse.ui.wizards.datatransfer.ImportOperation;

public final class WorkspaceTools {

	@Deprecated
	private WorkspaceTools() {
		throw new IllegalArgumentException("Not intended to be instantiated");
	}

	public static IContainer createFolder(IResource resource) throws IOException {
		IFolder folder = null;

		// resolve returns IFile instances if a container does not exist, so we need to convert it to a folder
		if (resource instanceof IFile) {
			if (resource.exists())
				throw new IOException(String.format("A file with the name '%s' already exists", resource.toString()));

			folder = resource.getProject().getFolder(resource.getProjectRelativePath());

		} else if (resource instanceof IFolder)
			folder = (IFolder) resource;

		if (folder != null) {
			if (!folder.exists()) {
				if (!folder.getParent().exists())
					createFolder(folder.getParent());

				try {
					folder.create(true, true, new NullProgressMonitor());
				} catch (final CoreException e) {
					throw new IOException(e);
				}
			}

			return folder;
		}

		throw new IOException(String.format("Location '%s' cannot be cast to a folder", folder.toString()));
	}

	public static IFile createFile(IFile file) throws IOException {
		if (file.getParent() instanceof IFolder)
			createFolder(file.getParent());

		try {
			file.create(new ByteArrayInputStream(new byte[0]), false, null);
			return file;
		} catch (final CoreException e) {
			throw new IOException(e);
		}
	}

	public static void deleteFile(IResource file) throws IOException {
		if (file instanceof IFile) {
			try {
				file.delete(true, new NullProgressMonitor());
			} catch (final CoreException e) {
				throw new IOException(String.format("Cannot delete file '%s'", file), e);
			}

		} else
			throw new IOException(String.format("Cannot delete file '%s' as it is not a file", file));
	}

	public static void deleteFolder(IResource folder) throws IOException {
		if (folder.exists()) {
			if (folder instanceof IFolder) {
				try {
					((IFolder) folder).delete(true, new NullProgressMonitor());
				} catch (final CoreException e) {
					throw new IOException(e);
				}

			} else
				throw new IOException(String.format("Cannot delete folder '%s' as it is not a folder", folder));
		}
	}

	public static IWorkspaceRoot getWorkspace() {
		return ResourcesPlugin.getWorkspace().getRoot();
	}

	public static String openFileSelectionDialog(IContainer dialogRoot, int mode, String title, String message) {

		final RunnableWithResult<String> runnable = new RunnableWithResult<String>() {

			@Override
			public String runWithTry() throws Throwable {
				if (mode == SWT.SAVE) {
					// open a save as dialog
					final SaveAsDialog dialog = new SaveAsDialog(Display.getDefault().getActiveShell());
					// set default filename if a subfolder is selected
					if (!dialogRoot.equals(getWorkspace()))
						dialog.setOriginalFile(dialogRoot.getFile(new Path("newFile")));

					dialog.setTitle(title);
					dialog.setMessage(message);

					if (dialog.open() == Window.OK)
						return "workspace:/" + dialog.getResult().toPortableString();

				} else {
					// open a select file dialog

					final ElementTreeSelectionDialog dialog = new ElementTreeSelectionDialog(Display.getDefault().getActiveShell(),
							new WorkbenchLabelProvider(), new WorkbenchContentProvider());
					dialog.setTitle(title);
					dialog.setMessage(message);
					dialog.setInput(dialogRoot);
					dialog.setComparator(new ResourceComparator(ResourceComparator.NAME));

					if (dialog.open() == Window.OK)
						return "workspace:/" + ((IResource) dialog.getFirstResult()).getFullPath().toPortableString();
				}

				return null;
			}
		};

		Display.getDefault().syncExec(runnable);
		return runnable.getResult();
	}

	public static String openFolderSelectionDialog(IContainer dialogRoot, String title, String message) {
		final RunnableWithResult<String> runnable = new RunnableWithResult<String>() {

			@Override
			public String runWithTry() throws Throwable {
				final ContainerSelectionDialog dialog = new ContainerSelectionDialog(Display.getDefault().getActiveShell(), dialogRoot, true, message);
				dialog.setTitle(title);

				if (dialog.open() == Window.OK)
					return "workspace:/" + ((IPath) dialog.getResult()[0]).toPortableString();

				return null;
			}

		};

		Display.getDefault().syncExec(runnable);
		return runnable.getResult();
	}

	public static String[] findFiles(Pattern regExp, IContainer root, boolean recursive) throws IOException {
		try {
			final List<String> result = new ArrayList<>();

			root.accept((IResourceVisitor) resource -> {
				if ((resource instanceof IFile) && (regExp.matcher(resource.getName()).matches()))
					result.add("workspace:/" + resource.getFullPath());

				return true;
			}, recursive ? IResource.DEPTH_INFINITE : IResource.DEPTH_ONE, IContainer.INCLUDE_HIDDEN);

			return result.toArray(new String[0]);

		} catch (final CoreException e) {
			throw new IOException(e);
		}
	}

	public static IProject linkProject(File folder) throws IOException {
		if (folder.isDirectory()) {

			try {
				final IProjectDescription description = getProjectDescription(folder);
				final IProject project = getProject(description.getName());
				project.create(description, null);
				project.open(null);
				return project;

			} catch (final CoreException e) {
				throw new IOException("Cannot read project description", e);
			}
		} else
			throw new IOException(String.format("'%s' is not a directory", folder));
	}

	public static IProject importProject(File resolvedFile) throws IOException {
		if (resolvedFile.isDirectory()) {
			try {
				final IProjectDescription projectDescription = getProjectDescription(resolvedFile);
				final IProject project = createProject(projectDescription.getName());

				final ImportOperation importOperation = new ImportOperation(project.getFullPath(), resolvedFile, FileSystemStructureProvider.INSTANCE,
						file -> IOverwriteQuery.ALL);
				importOperation.setCreateContainerStructure(false);
				importOperation.run(new NullProgressMonitor());
				return project;

			} catch (final InvocationTargetException e) {
				throw new IOException("Import failed", e);

			} catch (final CoreException e) {
				throw new IOException("Cannot read project description", e);

			} catch (final InterruptedException e) {
				throw new IOException("Import got interrupted", e);
			}

		} else
			throw new IOException("location is not a directory");
	}

	public static IProject createProject(final String name) throws IOException {
		final IProject project = getProject(name);
		if (!project.exists()) {
			try {
				project.create(new NullProgressMonitor());
				project.open(new NullProgressMonitor());

			} catch (final CoreException e) {
				throw new IOException(e);
			}
		}

		return project;
	}

	private static IProjectDescription getProjectDescription(File folder) throws CoreException {
		final Path projectPath = new Path(folder.getAbsoluteFile() + File.separator + ".project");
		return ResourcesPlugin.getWorkspace().loadProjectDescription(projectPath);
	}

	private static IProject getProject(final String name) {
		return getWorkspace().getProject(name);
	}

	public static void createProblemMarker(IFile file, String type, int lineNumber, int intSeverity, String message, boolean permanent) throws IOException {
		final HashMap<String, Object> attributes = new HashMap<>();
		attributes.put(IMarker.LINE_NUMBER, lineNumber);
		attributes.put(IMarker.SEVERITY, intSeverity);
		attributes.put(IMarker.MESSAGE, message);
		attributes.put(IMarker.TRANSIENT, !permanent);

		try {
			MarkerUtilities.createMarker(file, attributes, type);
		} catch (final CoreException e) {
			throw new IOException(e);
		}
	}
}
