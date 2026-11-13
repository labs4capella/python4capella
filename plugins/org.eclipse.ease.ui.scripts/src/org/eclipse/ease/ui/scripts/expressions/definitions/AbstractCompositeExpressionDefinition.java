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

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import org.eclipse.core.expressions.Expression;
import org.eclipse.ease.ui.scripts.expressions.ICompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;

public abstract class AbstractCompositeExpressionDefinition extends AbstractExpressionDefinition implements ICompositeExpressionDefinition {

	private List<IExpressionDefinition> fChildren = null;

	protected int getChildLimit() {
		try {
			return Integer.parseInt(getConfigurationElement().getAttribute("childElements"));
		} catch (final NumberFormatException e) {
			return 0;
		}
	}

	@Override
	public boolean acceptsChild() {
		return (getChildLimit() < 0) || ((getChildLimit() > 0) && ((fChildren == null) || (getChildLimit() > fChildren.size())));
	}

	@Override
	public boolean addChild(IExpressionDefinition expression) {
		if (acceptsChild()) {
			if (fChildren == null)
				fChildren = new ArrayList<>(2);

			fChildren.add(expression);
			expression.setParent(this);
			return true;
		}

		return false;
	}

	@Override
	public List<IExpressionDefinition> getChildren() {
		return (fChildren != null) ? fChildren : Collections.emptyList();
	}

	protected List<Expression> getChildrenAsExpressions() {
		return getChildren().stream().map(e -> e.toCoreExpression()).collect(Collectors.toList());
	}

	@Override
	public void removeChild(IExpressionDefinition element) {
		getChildren().remove(element);
	}

	@Override
	public String serialize() {
		final StringBuilder builder = new StringBuilder();
		builder.append(toString());
		builder.append('(');

		final String serializedParameters = serializeParameters();
		final String serializedChildren = serializeChildren();
		builder.append(serializedParameters);
		if (!serializedParameters.isEmpty() && !serializedChildren.isEmpty())
			builder.append(", ");

		builder.append(serializedChildren);

		builder.append(')');
		return builder.toString();
	}

	private String serializeChildren() {
		final StringBuilder builder = new StringBuilder();
		for (final IExpressionDefinition child : getChildren()) {
			builder.append(child.serialize());
			builder.append(", ");
		}
		if (!getChildren().isEmpty())
			builder.delete(builder.length() - 2, builder.length());

		return builder.toString();
	}
}
