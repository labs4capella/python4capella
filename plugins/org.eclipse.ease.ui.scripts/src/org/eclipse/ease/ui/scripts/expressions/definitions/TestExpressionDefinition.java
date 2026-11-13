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
import org.eclipse.core.expressions.TestExpression;
import org.eclipse.core.internal.expressions.Expressions;
import org.eclipse.core.runtime.CoreException;

@SuppressWarnings("restriction")
public class TestExpressionDefinition extends SystemTestExpressionDefinition {

	private static final String ARGUMENTS = "arguments";
	private static final String FORCE_PLUGIN_ACTIVATION = "force plugin activation";

	/** Copied from {@link TestExpression}. */
	private static final char PROP_SEP = '.';

	@Override
	public Expression toCoreExpression() {
		String property = getParameter(PROPERTY);
		final int pos = property.lastIndexOf(PROP_SEP);
		if (pos == -1)
			return Expression.FALSE;

		final String namespace = property.substring(0, pos);
		property = property.substring(pos + 1);

		Object[] arguments;
		try {
			arguments = Expressions.parseArguments(getParameter(ARGUMENTS));
		} catch (final CoreException e) {
			return Expression.FALSE;
		}

		return ExpressionFactory.getInstance().createTestExpression(namespace, property, arguments, getParameter(VALUE),
				Boolean.parseBoolean(getParameter(FORCE_PLUGIN_ACTIVATION)));
	}
}
