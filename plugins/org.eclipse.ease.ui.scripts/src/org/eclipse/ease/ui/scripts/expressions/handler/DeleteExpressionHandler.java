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
package org.eclipse.ease.ui.scripts.expressions.handler;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.commands.IHandler;
import org.eclipse.ease.ui.scripts.expressions.ICompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.ui.handlers.HandlerUtil;

public class DeleteExpressionHandler extends AbstractHandler implements IHandler {

	public static final String COMMAND_ID = "org.eclipse.ease.commands.expressions.deleteExpression";

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		final ISelection selection = HandlerUtil.getActiveMenuSelection(event);
		if (selection instanceof IStructuredSelection) {
			final Object element = ((IStructuredSelection) selection).getFirstElement();
			if (element instanceof IExpressionDefinition) {
				final ICompositeExpressionDefinition parent = ((IExpressionDefinition) element).getParent();
				if (parent != null)
					parent.removeChild((IExpressionDefinition) element);

			}
		}

		return null;
	}
}
