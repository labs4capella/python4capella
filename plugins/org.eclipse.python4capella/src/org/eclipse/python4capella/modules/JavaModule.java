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
import java.util.List;

import org.eclipse.ease.modules.WrapToScript;

/**
 * EASE module for Java.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class JavaModule {

	/**
	 * Removes an element by index without ambiguity with {@link List#remove(Object)}.
	 *
	 * @param list the backing list
	 * @param index the index to remove
	 * @return the removed element
	 */
	@WrapToScript
	public Object listRemoveAt(List<?> list, int index) {
		return list.remove(index);
	}

	/**
	 * Removes a value while preserving the Java boolean result across script bridges.
	 *
	 * @param list the backing list
	 * @param value the value to remove
	 * @return whether the list changed
	 */
	@WrapToScript
	public boolean listRemove(List<?> list, Object value) {
		return list.remove(value);
	}

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
