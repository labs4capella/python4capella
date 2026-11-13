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
package org.eclipse.ease.ui.scripts.expressions.definitions;

import org.eclipse.core.expressions.Expression;
import org.eclipse.core.internal.expressions.SystemTestExpression;

@SuppressWarnings("restriction")
public class SystemTestExpressionDefinition extends AbstractExpressionDefinition {

	protected static final String PROPERTY = "property";
	protected static final String VALUE = "value";

	@Override
	public Expression toCoreExpression() {
		return new SystemTestExpression(getParameter(PROPERTY), getParameter(VALUE));
	}
}
