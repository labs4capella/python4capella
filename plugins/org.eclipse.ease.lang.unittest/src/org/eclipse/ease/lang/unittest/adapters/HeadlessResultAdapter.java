/*******************************************************************************
 * Copyright (c) 2021 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.unittest.adapters;

import org.eclipse.core.runtime.IAdapterFactory;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;

public class HeadlessResultAdapter implements IAdapterFactory {

	@Override
	public <T> T getAdapter(Object adaptableObject, Class<T> adapterType) {
		if ((adaptableObject instanceof ITestSuite) && (Integer.class.equals(adapterType))) {

			switch (((ITestSuite) adaptableObject).getStatus()) {
			case ERROR:
				return (T) Integer.valueOf(200);
			case FAILURE:
				return (T) Integer.valueOf(100);
			default:
				return (T) Integer.valueOf(0);
			}
		}

		return null;
	}

	@Override
	public Class<?>[] getAdapterList() {
		return new Class<?>[] { ITestSuite.class };
	}
}
