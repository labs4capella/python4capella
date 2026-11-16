/*******************************************************************************
 * Copyright (c) 2017 Christian Pontesegger and others.
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

import java.util.Collection;

import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;

public class FilteredTestCommand {

	private final ITestContainer fRoot;
	private final Collection<ITestEntity> fActiveTests;

	public FilteredTestCommand(ITestContainer root, Collection<ITestEntity> activeTests) {
		fRoot = root;
		fActiveTests = activeTests;
	}

	public ITestContainer getTestRoot() {
		return fRoot;
	}

	public Collection<ITestEntity> getActiveTests() {
		return fActiveTests;
	}
}
