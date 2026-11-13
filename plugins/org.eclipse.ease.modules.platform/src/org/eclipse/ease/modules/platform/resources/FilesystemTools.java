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

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.StandardCopyOption;
import java.nio.file.attribute.BasicFileAttributes;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

import org.eclipse.core.runtime.URIUtil;
import org.eclipse.ease.tools.RunnableWithResult;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.FileDialog;

public final class FilesystemTools {

	@Deprecated
	private FilesystemTools() {
		throw new IllegalArgumentException("Not intended to be instantiated");
	}

	public static File createFolder(File folder) throws IOException {
		if (!folder.exists()) {

			if (folder.mkdirs())
				return folder;
			else
				throw new IOException(String.format("Could not create folder '%s' on file system", folder.toString()));

		}

		if (folder.isFile())
			throw new IOException(String.format("A file with the name '%s' already exists", folder.toString()));

		return folder;
	}

	public static File createFile(File file) throws IOException {
		if (file.exists())
			throw new IOException(String.format("A file with the name '%s' already exists", file.toString()));

		createFolder(file.getParentFile());

		if (file.createNewFile())
			return file;

		throw new IOException(String.format("Could not create file '%s'", file.toString()));
	}

	public static void deleteFile(File file) throws IOException {
		if (file.exists()) {
			if (file.isFile()) {
				try {
					Files.delete(file.toPath());
				} catch (final NoSuchFileException e) {
					// ignore when file does not exist
				}

			} else
				throw new IOException(String.format("Cannot delete file '%s' as it is a folder", file));
		}
	}

	public static void deleteFolder(File folder) throws IOException {
		if (folder.exists()) {
			if (folder.isDirectory()) {
				for (final File file : folder.listFiles()) {
					if (file.isFile())
						deleteFile(file);
					else
						deleteFolder(file);
				}

				Files.delete(folder.toPath());

			} else
				throw new IOException(String.format("Cannot delete folder '%s' as it is a file", folder));
		}
	}

	public static String openFileSelectionDialog(File dialogRoot, int mode, String title) {
		final RunnableWithResult<String> runnable = new RunnableWithResult<String>() {

			@Override
			public String runWithTry() throws Throwable {
				final FileDialog dialog = new FileDialog(Display.getDefault().getActiveShell(), mode);

				if (title != null)
					dialog.setText(title);

				dialog.setFilterPath(dialogRoot.getAbsolutePath());
				return dialog.open();
			}
		};

		Display.getDefault().syncExec(runnable);
		return runnable.getResult();
	}

	public static String openFolderSelectionDialog(File dialogRoot, String title, String message) {
		final RunnableWithResult<String> runnable = new RunnableWithResult<String>() {

			@Override
			public String runWithTry() throws Throwable {
				final DirectoryDialog dialog = new DirectoryDialog(Display.getCurrent().getActiveShell());

				if (title != null)
					dialog.setText(title);

				if (message != null)
					dialog.setMessage(message);

				dialog.setFilterPath(dialogRoot.getAbsolutePath());
				return dialog.open();
			}
		};

		Display.getDefault().syncExec(runnable);
		return runnable.getResult();
	}

	public static String[] findFiles(Pattern regExp, File root, boolean recursive) throws IOException {
		if (!root.isDirectory())
			throw new IOException(String.format("'%s' is a file, not a folder", root));

		final List<String> result = new ArrayList<>();

		final Collection<File> toVisit = new HashSet<>();
		toVisit.add(root);

		do {
			final File container = toVisit.iterator().next();
			toVisit.remove(container);

			final File[] files = container.listFiles();
			if (files != null) {
				for (final File child : files) {
					if (child.isFile()) {
						if (regExp.matcher(child.getName()).matches())
							result.add(child.getAbsolutePath());

					} else if ((recursive) && (child.isDirectory()))
						toVisit.add(child);
				}
			}

		} while (!toVisit.isEmpty());

		return result.toArray(new String[0]);
	}

	public static void zip(Path sourceFilePath, Path zipFilePath) throws IOException {
		try {
			final URI uri = URIUtil.fromString("jar:file:" + zipFilePath.toUri().getPath());
			final Map<String, String> env = new HashMap<>();
			env.put("create", zipFilePath.toFile().exists() ? Boolean.FALSE.toString() : Boolean.TRUE.toString());

			try (FileSystem fileSystem = FileSystems.newFileSystem(uri, env)) {

				final Path root = fileSystem.getPath("/");

				if (Files.isDirectory(sourceFilePath)) {
					// source is a directory
					Files.walkFileTree(sourceFilePath, new SimpleFileVisitor<Path>() {
						@Override
						public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
							final Path relativePath = sourceFilePath.relativize(file);
							final Path zipEntry = fileSystem.getPath(root.toString(), relativePath.toString());
							Files.copy(file, zipEntry, StandardCopyOption.REPLACE_EXISTING);
							return FileVisitResult.CONTINUE;
						}

						@Override
						public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
							final Path relativePath = sourceFilePath.relativize(dir);
							final Path zipDirectory = fileSystem.getPath(root.toString(), relativePath.toString());

							if (Files.notExists(zipDirectory))
								Files.createDirectories(zipDirectory);

							return FileVisitResult.CONTINUE;
						}
					});

				} else {
					// source is a simple file
					if (Files.notExists(root))
						Files.createDirectories(root);

					final Path destinationPath = fileSystem.getPath(root.toString(), sourceFilePath.getFileName().toString());
					Files.copy(sourceFilePath, destinationPath, StandardCopyOption.REPLACE_EXISTING);
				}
			}
		} catch (final URISyntaxException e) {
			throw new IOException(e);
		}
	}

	public static void unzip(Path zipFilePath, Path targetDirectoryPath) throws IOException {
		final URI uri = URI.create("jar:file:" + zipFilePath.toUri().getPath());
		final Map<String, String> env = new HashMap<>();
		env.put("create", Boolean.FALSE.toString());

		try (FileSystem fileSystem = FileSystems.newFileSystem(uri, env)) {

			final java.nio.file.Path root = fileSystem.getPath("/");

			// walk the zip file tree and copy files to the destination
			Files.walkFileTree(root, new SimpleFileVisitor<java.nio.file.Path>() {
				@Override
				public FileVisitResult visitFile(java.nio.file.Path file, BasicFileAttributes attrs) throws IOException {
					final java.nio.file.Path targetFile = java.nio.file.Paths.get(targetDirectoryPath.toString(), file.toString());
					Files.copy(file, targetFile, StandardCopyOption.REPLACE_EXISTING);
					return FileVisitResult.CONTINUE;
				}

				@Override
				public FileVisitResult preVisitDirectory(java.nio.file.Path dir, BasicFileAttributes attrs) throws IOException {
					final java.nio.file.Path targetDirectory = java.nio.file.Paths.get(targetDirectoryPath.toString(), dir.toString());
					if (Files.notExists(targetDirectory))
						Files.createDirectory(targetDirectory);

					return FileVisitResult.CONTINUE;
				}
			});
		}
	}

	public static byte[] getChecksum(InputStream input) throws IOException {
		try {
			final MessageDigest digest = MessageDigest.getInstance("MD5");
			final DigestInputStream digestInputStream = new DigestInputStream(input, digest);

			final byte[] buffer = new byte[8 * 1024];
			int readBytes;
			do {
				readBytes = digestInputStream.read(buffer);
			} while (readBytes > 0);

			return digest.digest();

		} catch (final NoSuchAlgorithmException e) {
			throw new IOException("MD5 digest not found", e);
		}
	}
}
