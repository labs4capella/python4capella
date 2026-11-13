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
package org.eclipse.ease.ui.scripts.expressions;

import org.eclipse.core.expressions.Expression;

public interface IExpressionDefinition {

	void setParent(ICompositeExpressionDefinition parent);

	String serialize();

	Expression toCoreExpression();

	ICompositeExpressionDefinition getParent();

	void setParameter(String key, String value);

	void setParameterValues(String key, String[] allowedValues);

	boolean hasParameter(String key);

	String getDescription();
}
