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
package org.eclipse.ease.lang.unittest;

/**
 * Return value type that can be checked for validity.
 */
public interface IAssertion {
	/**
	 * Valid assertion.
	 */
	IAssertion VALID = new IAssertion() {

		@Override
		public boolean isValid() {
			return true;
		}

		@Override
		public String toString() {
			return "OK";
		}

		@Override
		public void throwOnError() throws AssertionException {
			// do nothing
		}
	};

	/**
	 * Invalid assertion.
	 */
	IAssertion INVALID = new IAssertion() {

		@Override
		public boolean isValid() {
			return false;
		}

		@Override
		public String toString() {
			return "Assertion failed";
		}

		@Override
		public void throwOnError() throws AssertionException {
			throw new AssertionException(toString());
		}
	};

	/**
	 * Return <code>true</code> when assertion is valid.
	 *
	 * @return <code>true</code> on valid assertion
	 */
	boolean isValid();

	/**
	 * Throw exception in case {@link #isValid()} is <code>false</code>.
	 *
	 * @throws AssertionException
	 *             when {@link #isValid()} is <code>false</code>
	 */
	void throwOnError() throws AssertionException;
}
