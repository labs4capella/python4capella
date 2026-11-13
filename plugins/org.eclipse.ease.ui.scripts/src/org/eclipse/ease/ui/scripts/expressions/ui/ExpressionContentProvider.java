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
package org.eclipse.ease.ui.scripts.expressions.ui;

import java.util.ArrayList;

import org.eclipse.ease.ui.scripts.expressions.ICompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.definitions.AbstractExpressionDefinition;
import org.eclipse.jface.viewers.ITreeContentProvider;

public class ExpressionContentProvider implements ITreeContentProvider {

	@Override
	public Object[] getElements(Object inputElement) {
		if (inputElement instanceof Object[]) {
			final Object[] rawInput = (Object[]) inputElement;
			if ((rawInput.length == 1) && (rawInput[0] instanceof IExpressionDefinition))
				return new Object[] { rawInput[0] };
		}

		return new Object[0];
	}

	@Override
	public Object[] getChildren(Object parentElement) {
		final ArrayList<Object> children = new ArrayList<>();

		if (parentElement instanceof AbstractExpressionDefinition)
			children.addAll(((AbstractExpressionDefinition) parentElement).getParameters());

		if (parentElement instanceof ICompositeExpressionDefinition)
			children.addAll(((ICompositeExpressionDefinition) parentElement).getChildren());

		return children.toArray();
	}

	@Override
	public Object getParent(Object element) {
		if (element instanceof IExpressionDefinition)
			return ((IExpressionDefinition) element).getParent();

		return null;
	}

	@Override
	public boolean hasChildren(Object element) {
		if ((element instanceof AbstractExpressionDefinition) && (!((AbstractExpressionDefinition) element).getParameters().isEmpty()))
			return true;

		return ((element instanceof ICompositeExpressionDefinition) && (!((ICompositeExpressionDefinition) element).getChildren().isEmpty()));
	}
}
