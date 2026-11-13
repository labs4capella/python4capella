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
import org.eclipse.core.internal.expressions.IterateExpression;
import org.eclipse.core.runtime.CoreException;

@SuppressWarnings("restriction")
public class IterateExpressionDefinition extends AbstractCompositeExpressionDefinition {

	private static final String OPERATOR = "operator";
	private static final String IF_EMPTY = "ifEmpty";

	@Override
	public Expression toCoreExpression() {
		try {
			return new IterateExpression(getParameter(OPERATOR), getParameter(IF_EMPTY));
		} catch (final CoreException e) {
			// when invalid OPERATOR is entered
			return Expression.FALSE;
		}
	}
}
