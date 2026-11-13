/*******************************************************************************
 * Copyright (c) 2016 Kichwa Coders and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Jonah Graham (Kichwa Coders) - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.py4j.internal;

/**
 * Type encapsulating return from the Python side.
 */
public interface IInteractiveReturn {
	/**
	 * Return the exception details, or <code>null</code> if there was no exception.
	 *
	 * This method may return a fully constructed Java exception is possible, if not possible, this method returns the message for an exception.
	 *
	 * @return the exception details.
	 */
	Object getException();

	/**
	 * Get the result of running the code, or <code>null</code> if there is no return value.
	 *
	 * @return the Java instance of the type, or if Python returned something that cannot be represented as a Java type, return a repr() of the value.
	 */
	Object getResult();
}
