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

package org.eclipse.ease.lang.unittest.execution;

import java.util.Collection;

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.lang.unittest.TestSuiteScriptEngine;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;

public interface ITestExecutionStrategy {
	/**
	 * Prepare test execution for a given test root element.
	 *
	 * @param engine
	 *            executing root engine
	 * @param root
	 *            test root element
	 */
	void prepareExecution(TestSuiteScriptEngine engine, ITestEntity root);

	/**
	 * Prepare test execution for a given test root element given a dedicated filter on child elements.
	 *
	 * @param engine
	 *            executing root engine
	 * @param root
	 *            test root element
	 * @param activeEntities
	 *            active elements within root
	 */
	void prepareExecution(TestSuiteScriptEngine engine, ITestEntity root, Collection<ITestEntity> activeEntities);

	/**
	 * Execute a test entity. Executed the element and all its child elements, if any.
	 *
	 * @param testEntity
	 *            entity to execute
	 */
	void execute(ITestEntity testEntity);

	/**
	 * Create a script engine for a given testsuite and resource. The testsuite might provide information on the default engine to use. The resource might need
	 * a different engine to execute.
	 *
	 * @param testSuite
	 *            testsuite to be executed from or <code>null</code>
	 * @param resource
	 *            resource to execute or <code>null</code>
	 * @return script engine or <code>null</code>
	 */
	IScriptEngine createScriptEngine(ITestSuite testSuite, Object resource);
}
