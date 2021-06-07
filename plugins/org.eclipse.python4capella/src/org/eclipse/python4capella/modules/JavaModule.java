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

	/**
	 * Calls {@link List#iterator()}.
	 * 
	 * @param list the {@link List}
	 * @return {@link List#iterator()}
	 */
	@WrapToScript
	public Iterator<?> listIterator(List<?> list) {
		return list.iterator();
	}

	/**
	 * Calls {@link List#clear()}.
	 * 
	 * @param list the {@link List}
	 * @return {@link List#clear()}
	 */
	@WrapToScript
	public void listClear(List<?> list) {
		list.clear();
	}

	/**
	 * Calls {@link List#size()}.
	 * 
	 * @param list the {@link List}
	 * @return {@link List#size()}
	 */
	@WrapToScript
	public void listSize(List<?> list) {
		list.size();
	}

	/**
	 * Calls {@link List#get(int)}.
	 * 
	 * @param list the {@link List}
	 * @return {@link List#get(int)}
	 */
	@WrapToScript
	public void listGet(List<?> list, int index) {
		list.get(index);
	}

	/**
	 * Calls {@link List#indexOf(Object)}.
	 * 
	 * @param it the {@link List}
	 * @return {@link List#indexOf(Object)}
	 */
	@WrapToScript
	public int listIndexOf(List<Object> list, Object object) {
		return list.indexOf(object);
	}

	/**
	 * Calls {@link List#lastIndexOf(Object)}.
	 * 
	 * @param it the {@link List}
	 * @return {@link List#lastIndexOf(Object)}
	 */
	@WrapToScript
	public int listLastIndexOf(List<Object> list, Object object) {
		return list.lastIndexOf(object);
	}

	/**
	 * Calls {@link List#add(Object)}.
	 * 
	 * @param it the {@link List}
	 * @return {@link List#add(Object)}
	 */
	@WrapToScript
	public boolean listAdd(List<Object> list, Object object) {
		return list.add(object);
	}

	/**
	 * Calls {@link List#remove(Object)}.
	 * 
	 * @param it the {@link List}
	 * @return {@link List#remove(Object)}
	 */
	@WrapToScript
	public boolean listRemove(List<Object> list, Object object) {
		return list.remove(object);
	}

	/**
	 * Calls {@link List#contains(Object)}.
	 * 
	 * @param it the {@link List}
	 * @return {@link List#contains(Object)}
	 */
	@WrapToScript
	public boolean listContains(List<Object> list, Object object) {
		return list.contains(object);
	}

}
