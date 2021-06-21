/**
 *   Copyright (c) 2021 THALES GLOBAL SERVICES
 *  This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License 2.0
 *  which accompanies this distribution, and is available at
 *  https://www.eclipse.org/legal/epl-2.0/
 *
 *  SPDX-License-Identifier: EPL-2.0
 *
 *  Contributors:
 *       Obeo - Initial API and implementation
 */
package org.eclipse.python4capella.modules;

import java.util.Iterator;

import org.eclipse.ease.modules.WrapToScript;

/**
 * EASE module for Java.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class JavaModule {

	/**
	 * Calls {@link Iterator#hasNext()}.
	 * 
	 * @param it the {@link Iterator}
	 * @return {@link Iterator#hasNext()}
	 */
	@WrapToScript
	public boolean iteratorHasNext(Iterator<?> it) {
		return it.hasNext();
	}

	/**
	 * Calls {@link Iterator#next()}.
	 * 
	 * @param it the {@link Iterator}
	 * @return {@link Iterator#next()}
	 */
	@WrapToScript
	public Object iteratorNext(Iterator<?> it) {
		return it.next();
	}

}
