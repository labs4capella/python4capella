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
package org.eclipse.ease.modules.platform.resources;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.Collection;
import java.util.HashSet;
import java.util.Objects;
import java.util.regex.Pattern;

import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IMarker;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IResourceChangeEvent;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.ease.IExecutionListener;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Script;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.swt.SWT;

/**
 * Provides file access for workspace and file system resources. Methods accepting location objects can deal with {@link String}, {@link URI}, {@link IFile} and
 * {@link File} instances.
 */
public class ResourcesModule extends AbstractScriptModule implements IExecutionListener {

	/** Module identifier. */
	public static final String MODULE_ID = "/System/Resources";

	/** Access modifier for read mode (1). */
	@WrapToScript
	public static final int READ = IFileHandle.READ;

	/** Access modifier for write mode (2). */
	@WrapToScript
	public static final int WRITE = IFileHandle.WRITE;

	/** Access modifier for append mode (4). */
	@WrapToScript
	public static final int APPEND = IFileHandle.APPEND;

	/** Open file handles managed by this module. */
	private final Collection<IFileHandle> fOpenHandles = new HashSet<>();

	/**
	 * Get the workspace root.
	 *
	 * @return workspace root
	 */
	@WrapToScript
	public static IWorkspaceRoot getWorkspace() {
		return WorkspaceTools.getWorkspace();
	}

	/**
	 * Get a project instance.
	 *
	 * @param name
	 *            project name
	 * @return project or <code>null</code>
	 */
	@WrapToScript
	public static IProject getProject(final String name) {
		return getWorkspace().getProject(name);
	}

	/**
	 * Get a workspace or file system file. Resolves relative and absolute file locations. Relative files are resolved against the current script file. If
	 * <i>exists</i> is <code>false</code> this method also returns files that do not exist yet. If <code>true</code> only existing instances are returned.
	 *
	 * @scriptExample getFile("workspace://my project/some folder/file.txt") to get the file.txt resource from the workspace
	 * @scriptExample getFile("project://some folder/file.txt") to get the file.txt resource as a project relative path
	 *
	 * @param location
	 *            file location/path to resolve
	 * @param exists
	 *            whether the resolved file needs to exist
	 * @return resolved {@link IFile} or {@link File} instance
	 * @throws FileNotFoundException
	 *             when file does not exist and <i>exists</i> is <code>true</code>
	 */
	@WrapToScript
	public Object getFile(final String location, @ScriptParameter(defaultValue = ScriptParameter.TRUE) final boolean exists) throws FileNotFoundException {
		final Object resource = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());
		if ((exists) && (!fileExists(resource)))
			throw new FileNotFoundException(String.format("File '%s' does not exist", location));

		return resource;
	}

	/**
	 * Create a new workspace project. Will create a new project if it not already exists. In case the project already exists, the existing instance will be
	 * returned.
	 *
	 * @param name
	 *            name of project to create
	 * @return project instance
	 * @throws IOException
	 *             when project creation fails
	 */
	@WrapToScript
	public static IProject createProject(final String name) throws IOException {
		return WorkspaceTools.createProject(name);
	}

	/**
	 * Create a new folder in the workspace or the file system.
	 *
	 * @param location
	 *            folder location
	 * @return {@link IFolder} or {@link File} instance
	 * @throws IOException
	 *             if this method fails. Reasons include:
	 *             <ul>
	 *             <li>This resource already exists in the workspace.</li>
	 *             <li>The workspace contains a resource of a different type at the same path as this resource.</li>
	 *             <li>The parent of this resource does not exist.</li>
	 *             <li>The parent of this resource is a project that is not open.</li>
	 *             <li>The parent contains a resource of a different type at the same path as this resource.</li>
	 *             <li>The parent of this resource is virtual, but this resource is not.</li>
	 *             <li>The name of this resource is not valid (according to <code>IWorkspace.validateName</code>).</li>
	 *             <li>The corresponding location in the local file system is occupied by a file (as opposed to a directory).</li>
	 *             <li>The corresponding location in the local file system is occupied by a folder and <code>force </code> is <code>false</code>.</li>
	 *             <li>Resource changes are disallowed during certain types of resource change event notification. See <code>IResourceChangeEvent</code> for
	 *             more details.</li>
	 *             </ul>
	 */
	@WrapToScript
	public Object createFolder(final Object location) throws IOException {
		final Object folder = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (folder instanceof File)
			return FilesystemTools.createFolder((File) folder);

		else if (folder instanceof IResource)
			return WorkspaceTools.createFolder((IResource) folder);

		throw new IOException(String.format("Invalid location '%s'", folder));
	}

	/**
	 * Create a new file in the workspace or the file system.
	 *
	 * @param location
	 *            file location
	 * @return {@link IFile}, {@link File} or <code>null</code> in case of error
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public Object createFile(final Object location) throws IOException {
		final Object file = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (file instanceof File)
			return FilesystemTools.createFile((File) file);

		else if (file instanceof IFile)
			return WorkspaceTools.createFile((IFile) file);

		throw new IOException(String.format("Invalid location '%s'", file));
	}

	/**
	 * Opens a file from the workspace or the file system. If the file does not exist and we open it for writing, the file is created automatically.
	 *
	 * @param location
	 *            file location
	 * @param mode
	 *            one of {@module #READ}, {@module #WRITE}, {@module #APPEND}
	 * @param autoClose
	 *            automatically close resource when script engine is terminated
	 *
	 * @return file handle instance to be used for file modification commands
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public IFileHandle openFile(final Object location, @ScriptParameter(defaultValue = "1") final int mode,
			@ScriptParameter(defaultValue = ScriptParameter.TRUE) boolean autoClose) throws IOException {
		return getFileHandle(location, mode, autoClose);
	}

	/**
	 * Verifies that a specific file exists.
	 *
	 * @param location
	 *            file location to verify
	 * @return <code>true</code> if file exists
	 */
	@WrapToScript
	public boolean fileExists(final Object location) {
		final Object resource = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());
		return (resource != null) && (ResourceTools.exists(resource)) && (ResourceTools.isFile(resource));
	}

	/**
	 * Close a file. Releases system resources bound by an open file.
	 *
	 * @param handle
	 *            handle to be closed
	 */
	@WrapToScript
	public void closeFile(final IFileHandle handle) {
		fOpenHandles.remove(handle);

		handle.close();
	}

	/**
	 * Read data from a file. To repeatedly read from a file retrieve a {@link IFileHandle} first using {@module #openFile(String, int)} and use the handle for
	 * <i>location</i>.
	 *
	 * @param location
	 *            file location, file handle or file instance
	 * @param bytes
	 *            amount of bytes to read (-1 for whole file)
	 * @return file data or <code>null</code> if EOF is reached
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public String readFile(final Object location, @ScriptParameter(defaultValue = "-1") final int bytes) throws IOException {
		final IFileHandle handle = getFileHandle(location, IFileHandle.READ, false);
		final String result = handle.read(bytes);

		if (!(location instanceof IFileHandle))
			handle.close();

		return result;
	}

	/**
	 * Copies a file from location to targetLocation.
	 *
	 * @param sourceLocation
	 *            file location, file handle or file instance for the source object
	 * @param targetLocation
	 *            file location, file handle or file instance for the target object
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public void copyFile(final Object sourceLocation, final Object targetLocation) throws IOException {
		final IFileHandle inputFile = getFileHandle(sourceLocation, READ, false);
		final IFileHandle targetFile = getFileHandle(targetLocation, -1, false);

		Files.copy(inputFile.getPath(), targetFile.getPath(), StandardCopyOption.REPLACE_EXISTING);

		if (targetFile.getFile() instanceof IResource) {
			try {
				((IResource) targetFile.getFile()).getParent().refreshLocal(1, null);
			} catch (final CoreException e) {
				throw new IOException("Cannot refresh workspace, ", e);
			}
		}
	}

	/**
	 * Delete a file. Does nothing if <i>location</i> cannot be resolved to an existing file.
	 *
	 * @param location
	 *            file to be deleted
	 * @throws IOException
	 *             on deletion errors
	 */
	@WrapToScript
	public void deleteFile(final Object location) throws IOException {
		final Object file = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (file instanceof IResource)
			WorkspaceTools.deleteFile((IResource) file);

		else if (file instanceof File)
			FilesystemTools.deleteFile((File) file);
	}

	/**
	 * Delete a folder recursively.
	 *
	 * @param location
	 *            folder to be deleted
	 * @throws IOException
	 *             on deletion errors
	 */
	@WrapToScript
	public void deleteFolder(final Object location) throws IOException {
		final Object folder = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (folder instanceof IResource)
			WorkspaceTools.deleteFolder((IResource) folder);

		else if (folder instanceof File)
			FilesystemTools.deleteFolder((File) folder);
	}

	/**
	 * Delete a project from the workspace.
	 *
	 * @param source
	 *            location or name of project to be deleted
	 * @throws IOException
	 *             on deletion errors
	 */
	@WrapToScript
	public void deleteProject(final Object source) throws IOException {
		try {
			final Object project = ResourceTools.resolve(source, getScriptEngine().getExecutedFile());
			if (project instanceof IProject)
				((IProject) project).delete(true, new NullProgressMonitor());

			else if (source != null) {
				final IProject localProject = getProject(source.toString());
				if (localProject.exists())
					localProject.delete(true, new NullProgressMonitor());
				else
					throw new FileNotFoundException(String.format("Project '%s' cannot be found", source));

			} else
				throw new IllegalArgumentException("cannot delete project <null>");

		} catch (final CoreException e) {
			throw new IOException(String.format("Project '%s' cannot be deleted", source), e);
		}
	}

	/**
	 * Read a single line from a file. To repeatedly read from a file retrieve a {@link IFileHandle} first using {@module #openFile(String, int)} and use the
	 * handle for <i>location</i>.
	 *
	 * @param location
	 *            file location, file handle or file instance
	 * @return line of text or <code>null</code> if EOF is reached
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public String readLine(final Object location) throws IOException {
		final IFileHandle handle = getFileHandle(location, IFileHandle.READ, false);

		final String result = handle.readLine();
		if (!(location instanceof IFileHandle))
			handle.close();

		return result;
	}

	/**
	 * Write data to a file. Files that do not exist yet will be created automatically. After the write operation the file remains open. It needs to be closed
	 * explicitly using the {@module #closeFile(IFileHandle)} command.
	 *
	 * @param location
	 *            file location
	 * @param data
	 *            data to be written
	 * @param mode
	 *            write mode ({@module #WRITE}/{@module #APPEND})
	 * @param autoClose
	 *            automatically close resource when script engine is terminated
	 * @return file handle to continue write operations
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public IFileHandle writeFile(final Object location, final Object data, @ScriptParameter(defaultValue = "2") final int mode,
			@ScriptParameter(defaultValue = ScriptParameter.TRUE) boolean autoClose) throws IOException {
		final IFileHandle handle = getFileHandle(location, mode, autoClose);

		if (data instanceof byte[])
			handle.write((byte[]) data);

		else if (data != null)
			handle.write(data.toString());

		return handle;
	}

	/**
	 * Write a line of data to a file. Files that do not exist yet will be created automatically. After the write operation the file remains open. It needs to
	 * be closed explicitly using the {@module #closeFile(IFileHandle)} command.
	 *
	 * @param location
	 *            file location
	 * @param data
	 *            data to be written
	 * @param mode
	 *            write mode ({@module #WRITE}/{@module #APPEND})
	 * @param autoClose
	 *            automatically close resource when script engine is terminated
	 * @return file handle to continue write operations
	 * @throws IOException
	 *             problems on file access
	 */
	@WrapToScript
	public IFileHandle writeLine(final Object location, final String data, @ScriptParameter(defaultValue = "2") final int mode,
			@ScriptParameter(defaultValue = ScriptParameter.TRUE) boolean autoClose) throws IOException {

		return writeFile(location, String.format("%s%n", data), mode, autoClose);
	}

	private IFileHandle getFileHandle(final Object location, final int mode, boolean autoClose) throws IOException {
		IFileHandle handle = null;

		if ((location instanceof String) && (((String) location).isEmpty()))
			handle = null;

		else if (location instanceof IFileHandle)
			handle = (IFileHandle) location;

		else if (location instanceof File) {
			handle = findHandle(location, mode);
			if (handle == null)
				handle = new FilesystemHandle((File) location, mode);

		} else if (location instanceof IFile) {
			handle = findHandle(location, mode);
			if (handle == null)
				handle = new ResourceHandle((IFile) location, mode);

		} else if (location instanceof IProject) {
			throw new IllegalArgumentException("Location points to a workspace project, not to a file");

		} else if (location instanceof IWorkspaceRoot) {
			throw new IllegalArgumentException("Location points to the workspace root, not to a file");

		} else if (location != null)
			handle = getFileHandle(ResourceTools.resolve(location, getScriptEngine().getExecutedFile()), mode, autoClose);

		if ((handle != null) && (!handle.exists())) {
			if (mode == READ)
				throw new FileNotFoundException(String.format("File '%s' does not exist", location));

			// create file if it does not exist yet for write/append mode
			handle.createFile(true);
		}

		if ((handle != null) && (autoClose)) {
			fOpenHandles.add(handle);
			// we need to manage a handle, register script engine listener
			getScriptEngine().addExecutionListener(this);
		}

		if (handle != null)
			return handle;

		throw new FileNotFoundException("Could not locate file \"" + location + "\"");
	}

	private IFileHandle findHandle(Object location, int mode) {
		for (final IFileHandle handle : fOpenHandles) {
			if ((Objects.equals(handle.getFile(), location)) && (Objects.equals(handle.getMode(), mode)))
				return handle;
		}

		return null;
	}

	/**
	 * Opens a file dialog. Depending on the <i>rootFolder</i> a workspace dialog or a file system dialog will be used. If the folder cannot be located, the
	 * workspace root folder is used by default. When type is set to {@module #WRITE} or {@module #APPEND} a save dialog will be shown instead of the default
	 * open dialog.
	 *
	 * @param rootFolder
	 *            root folder path to use
	 * @param type
	 *            dialog type to use ({@module #WRITE}/ {@module #APPEND} for save dialog, {@module #READ} for open dialog)
	 * @param title
	 *            dialog title
	 * @param message
	 *            dialog message
	 * @return full path to selected file either as absolute file system path or as absolute workspace URI. Returns <code>null</code> when the dialog is
	 *         cancelled by the user.
	 * @throws IOException
	 *             when root folder cannot be found
	 */
	@WrapToScript
	public String showFileSelectionDialog(@ScriptParameter(defaultValue = ScriptParameter.NULL) final Object rootFolder,
			@ScriptParameter(defaultValue = "0") final int type, @ScriptParameter(defaultValue = ScriptParameter.NULL) final String title,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) final String message) throws IOException {

		Object root = ResourceTools.resolve(rootFolder, getScriptEngine().getExecutedFile());
		if (rootFolder == null)
			root = getWorkspace();

		final int mode = ((type == WRITE) || (type == APPEND)) ? SWT.SAVE : SWT.OPEN;

		if (root instanceof File) {
			// file system
			return FilesystemTools.openFileSelectionDialog((File) root, mode, title);

		} else if (root instanceof IContainer) {
			// workspace
			return WorkspaceTools.openFileSelectionDialog((IContainer) root, mode, title, message);
		}

		throw new IOException(String.format("Cannot resolve root folder: '%s'", rootFolder));
	}

	/**
	 * Opens a dialog box which allows the user to select a container (project or folder). Workspace paths will always display the workspace as root object.
	 *
	 * @param rootFolder
	 *            root folder to display: for workspace paths this will set the default selection
	 * @param title
	 *            dialog title
	 * @param message
	 *            dialog message
	 *
	 * @return full path to selected folder either as absolute file system path or as absolute workspace URI. Returns <code>null</code> when the dialog is
	 *         cancelled by the user.
	 * @throws IOException
	 *             when root folder cannot be found
	 */
	@WrapToScript
	public String showFolderSelectionDialog(@ScriptParameter(defaultValue = ScriptParameter.NULL) final Object rootFolder,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) final String title,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) final String message) throws IOException {

		Object root = ResourceTools.resolve(rootFolder, getScriptEngine().getExecutedFile());
		if (rootFolder == null)
			root = getWorkspace();

		if (root instanceof File) {
			// file system
			return FilesystemTools.openFolderSelectionDialog((File) root, title, message);

		} else if (root instanceof IContainer) {
			// workspace
			return WorkspaceTools.openFolderSelectionDialog((IContainer) root, title, message);
		}

		throw new IOException(String.format("Cannot resolve root folder: '%s'", rootFolder));
	}

	/**
	 * Return files matching a certain pattern.
	 *
	 * @param pattern
	 *            search pattern: use * and ? as wildcards. If the pattern starts with '^' then a regular expression can be used.
	 * @param rootFolder
	 *            root folder to start your search from. <code>null</code> for workspace root
	 * @param recursive
	 *            searches subfolders when set to <code>true</code>
	 * @return An array of all matching file locations
	 * @throws IOException
	 *             when search fails
	 */
	@WrapToScript
	public String[] findFiles(final String pattern, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Object rootFolder,
			@ScriptParameter(defaultValue = ScriptParameter.TRUE) final boolean recursive) throws IOException {

		// evaluate expression to look for
		final Pattern regExp = (pattern.startsWith("^")) ? Pattern.compile(pattern) : Pattern.compile(pattern.replaceAll("\\*", ".*").replaceAll("\\?", "."));

		// locate root folder to start with
		Object root = ResourceTools.resolve(rootFolder, getScriptEngine().getExecutedFile());
		if ((root == null) || (rootFolder == null))
			root = getWorkspace();

		if (root instanceof IContainer) {
			// search in workspace
			return WorkspaceTools.findFiles(regExp, (IContainer) root, recursive);

		} else if (root instanceof File) {
			// search in file system
			return FilesystemTools.findFiles(regExp, (File) root, recursive);
		}

		throw new IOException(String.format("Cannot resolve root folder: '%s'", rootFolder));
	}

	/**
	 * Links a project into the current workspace. Does not copy resources to the workspace.
	 *
	 * @param location
	 *            location of project folder (needs to contain <i>.project</i> file)
	 * @return linked project, throws otherwise
	 * @throws IOException
	 *             when project location cannot be read/linked
	 */
	@WrapToScript
	public IProject linkProject(final Object location) throws IOException {
		final Object resolvedLocation = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (resolvedLocation instanceof File)
			return WorkspaceTools.linkProject((File) resolvedLocation);

		else if (resolvedLocation instanceof IResource)
			throw new IOException(String.format("'%s' is already part of the workspace", location));

		else
			throw new IOException(String.format("Could not resolve location '%s'", location));
	}

	/**
	 * Imports a project into the current workspace. The project needs to be available on the file system and needs to be unpacked. Zipped projects cannot be
	 * imported.
	 *
	 * @param location
	 *            location of project folder (needs to contain <i>.project</i> file)
	 * @return project instance, throws otherwise
	 * @throws IOException
	 *             on any import errors
	 */
	@WrapToScript
	public IProject importProject(final Object location) throws IOException {
		final Object resolvedLocation = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (resolvedLocation instanceof File)
			return WorkspaceTools.importProject((File) resolvedLocation);

		else if (resolvedLocation instanceof IResource)
			throw new IOException(String.format("'%s' is already part of the workspace", location));

		else
			throw new IOException("Could not resolve file location \"" + location + "\"");
	}

	/**
	 * Refresh a given resource and all its child elements.
	 *
	 * @param resource
	 *            {@link IFile}, {@link IFolder}, {@link IProject} or workspace root to update
	 * @throws IOException
	 *             if this method fails. Reasons include:
	 *             <ul>
	 *             <li>Resource changes are disallowed during certain types of resource change event notification. See {@link IResourceChangeEvent} for more
	 *             details.</li>
	 *             </ul>
	 * @scriptExample refreshResource(getProject("my project")) to update the project and all its subfolders
	 */
	@WrapToScript
	public void refreshResource(final Object resource) throws IOException {
		final Object resolvedResource = ResourceTools.resolve(resource);
		if (resolvedResource instanceof IResource) {
			try {
				((IResource) resolvedResource).refreshLocal(IResource.DEPTH_INFINITE, null);
			} catch (final CoreException e) {
				throw new IOException(e);
			}
		}
	}

	/**
	 * Read from an InputStream into a string. Consumes an {@link InputStream} and stores all available data in a string. Usually a stream is only readable
	 * once.
	 *
	 * @param input
	 *            input stream to read from
	 * @return string content of stream.
	 * @throws IOException
	 *             on read error on the stream
	 */
	@WrapToScript
	public String readStream(final InputStream input) throws IOException {
		return ResourceTools.toString(input);
	}

	/**
	 * Read full content from a given URL.
	 *
	 * @param address
	 *            address to read from
	 * @return read data
	 * @throws IOException
	 *             on read error on the stream
	 */
	@WrapToScript
	public String readUrl(String address) throws IOException {
		try (InputStream stream = new URL(address).openStream()) {
			return readStream(stream);
		}
	}

	/**
	 * Create a problem marker on a file resource.
	 *
	 * @param severity
	 *            one of <i>error</i>/<i>warning</i>/<i>info</i>
	 * @param location
	 *            file resource to create marker for
	 * @param lineNumber
	 *            line number to set marker on
	 * @param message
	 *            message to be added to the marker
	 * @param type
	 *            marker type to create, needs to match an existing type
	 * @param permanent
	 *            <code>true</code> for permanent markers, <code>false</code> for temporary markers
	 * @throws IOException
	 *             when marker cannot be created
	 */
	@WrapToScript
	public void createProblemMarker(final String severity, final Object location, final int lineNumber, final String message,
			@ScriptParameter(defaultValue = "org.eclipse.core.resources.problemmarker") final String type,
			@ScriptParameter(defaultValue = ScriptParameter.TRUE) final boolean permanent) throws IOException {
		final Object file = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());

		if (file instanceof IFile)
			WorkspaceTools.createProblemMarker((IFile) file, type, lineNumber, convertMarkerSeverity(severity), message, permanent);

		else
			throw new IOException(String.format("'%s' is not a workspace file", location));
	}

	private int convertMarkerSeverity(String severity) {
		switch (severity) {
		case "error":
			return IMarker.SEVERITY_ERROR;
		case "warning":
			return IMarker.SEVERITY_WARNING;
		default:
			return IMarker.SEVERITY_INFO;
		}
	}

	@Override
	public void notify(IScriptEngine engine, Script script, int status) {
		if (status == IExecutionListener.ENGINE_END) {
			// close all managed file handles
			for (final IFileHandle handle : fOpenHandles)
				handle.close();

			fOpenHandles.clear();
		}
	}

	/**
	 * Create or update a zip file with given resources.
	 *
	 * @param sourceLocation
	 *            source folder/file to zip
	 * @param zipLocation
	 *            zip file to use
	 * @return zip file reference
	 * @throws IOException
	 *             when zip file cannot be created/appended
	 */
	@WrapToScript
	public Object zip(Object sourceLocation, Object zipLocation) throws IOException {

		final java.nio.file.Path sourceFilePath = resolveFilePath(sourceLocation);
		final java.nio.file.Path zipFilePath = resolveFilePath(zipLocation);

		FilesystemTools.zip(sourceFilePath, zipFilePath);

		// refresh workspace
		final Object zipFile = ResourceTools.resolve(zipLocation, getScriptEngine().getExecutedFile());
		if (zipFile instanceof IFile)
			refreshResource(((IFile) zipFile).getParent());

		return zipFile;
	}

	private java.nio.file.Path resolveFilePath(Object location) throws IOException {
		Object file = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());
		if (file instanceof IResource)
			file = ((IResource) file).getLocation().toFile();

		if (!(file instanceof File))
			throw new IOException(String.format("Cannot resolve location: %s", location));

		return ((File) file).toPath();
	}

	/**
	 * Unzip a zip file to the provided target location.
	 *
	 * @param zipLocation
	 *            zip file to unzip
	 * @param targetLocation
	 *            folder to unzip to
	 * @return target location reference
	 * @throws IOException
	 *             when zip file cannot be unzipped
	 */
	@WrapToScript
	public Object unzip(Object zipLocation, Object targetLocation) throws IOException {
		final java.nio.file.Path zipFilePath = resolveFilePath(zipLocation);
		final java.nio.file.Path targetDirectoryPath = resolveFilePath(targetLocation);

		if (!targetDirectoryPath.toFile().exists())
			createFolder(targetDirectoryPath.toFile());

		FilesystemTools.unzip(zipFilePath, targetDirectoryPath);

		final Object targetDirectory = ResourceTools.resolve(targetLocation, getScriptEngine().getExecutedFile());
		if (targetDirectory instanceof IContainer)
			refreshResource(((IContainer) targetDirectory).getParent());

		return targetDirectory;
	}

	/**
	 * Get an MD5 checksum over a readable resource.
	 *
	 * @param location
	 *            location of resource to create checksum for
	 * @return file hash as hex encoded string
	 * @throws IOException
	 *             when resource cannot be read
	 */
	@WrapToScript
	public String getChecksum(Object location) throws IOException {
		final Object resolvedLocation = ResourceTools.resolve(location, getScriptEngine().getExecutedFile());
		try (InputStream input = ResourceTools.getInputStream(resolvedLocation)) {
			if (input != null)
				return byteArrayToHexString(FilesystemTools.getChecksum(input));

			else
				throw new IOException("Location \"" + location + "\" cannot be accessed.");
		}
	}

	private String byteArrayToHexString(byte[] bytes) {
		final StringBuilder builder = new StringBuilder();

		for (final byte b : bytes) {
			final String token = Integer.toHexString(b);
			if (token.length() == 1)
				builder.append('0');

			builder.append(token.substring(Math.max(token.length() - 2, 0)));
		}

		return builder.toString();
	}
}
