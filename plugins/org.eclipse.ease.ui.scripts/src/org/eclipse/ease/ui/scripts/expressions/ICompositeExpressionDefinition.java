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

import java.util.List;

public interface ICompositeExpressionDefinition extends IExpressionDefinition {

	boolean addChild(IExpressionDefinition expression);

	void removeChild(IExpressionDefinition element);

	List<IExpressionDefinition> getChildren();

	boolean acceptsChild();
}
