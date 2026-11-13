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

public class RootExpressionDefinition extends AbstractCompositeExpressionDefinition {

	private final String fName;

	public RootExpressionDefinition(String name) {
		super();
		fName = name;
	}

	@Override
	protected int getChildLimit() {
		return 1;
	}

	@Override
	public Expression toCoreExpression() {
		if (getChildren().size() == 1)
			return getChildren().get(0).toCoreExpression();

		return Expression.TRUE;
	}

	@Override
	public String serialize() {
		if (getChildren().size() == 1)
			return getChildren().get(0).serialize();

		return "";
	}

	@Override
	public String toString() {
		return fName;
	}
}
