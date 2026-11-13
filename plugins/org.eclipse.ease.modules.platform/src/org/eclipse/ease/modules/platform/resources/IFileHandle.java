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

import java.io.Closeable;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;

import org.eclipse.core.resources.IFile;

/**
 * Generic handle to an {@link IFile} or {@link File} instance.
 */
public interface IFileHandle extends Closeable {

	/** Open file in read mode. */
	int READ = 1;

	/** Open file in write mode. */
	int WRITE = 2;

	/** Open file in append mode. */
	int APPEND = 4;

	/**
	 * Read characters from a file.
	 *
	 * @param characters
	 *            amount of characters to read
	 * @return data read from file
	 * @throws IOException
	 *             on access errors
	 */
	String read(int characters) throws IOException;

	/**
	 * Read a line of data from a file. Reads until a line feed is detected.
	 *
	 * @return single line of text
	 * @throws IOException
	 *             on access errors
	 */
	String readLine() throws IOException;

	/**
	 * Returns the java.io.File Path to the underlying file.
	 *
	 * @return Path of the file
	 * @throws IOException
	 *             on access errors
	 */
	Path getPath() throws IOException;

	/**
	 * Write data to a file. Uses platform default encoding to write strings to the file.
	 *
	 * @param data
	 *            data to write
	 * @throws IOException
	 *             on write errors
	 */
	void write(String data) throws IOException;

	/**
	 * Write data to a file.
	 *
	 * @param data
	 *            data to write
	 * @throws IOException
	 *             on write errors
	 */
	void write(byte[] data) throws IOException;

	/**
	 * Check if a physical file exists.
	 *
	 * @return <code>true</code> when file exists
	 */

	boolean exists();

	/**
	 * Create a file.
	 *
	 * @param createHierarchy
	 *            create parent folders if they do not exist
	 * @return <code>true</code> on success
	 * @throws Exception
	 *             on creation errors
	 */
	boolean createFile(boolean createHierarchy) throws IOException;

	/**
	 * Close a file instance.
	 */
	@Override
	void close();

	/**
	 * Get the base file object. Returns an {@link IFile} or a {@link File} instance.
	 *
	 * @return base file object
	 */
	Object getFile();

	/**
	 * Get the mode (READ/WRITE/APPEND) this handle is operating for.
	 *
	 * @return file mode
	 */
	int getMode();
}
