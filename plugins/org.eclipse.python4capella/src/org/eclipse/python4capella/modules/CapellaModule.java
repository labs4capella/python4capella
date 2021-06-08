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

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;

import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.ui.massactions.core.shared.helper.SemanticBrowserHelper;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;
import org.polarsys.kitalpha.emde.model.ElementExtension;
import org.polarsys.kitalpha.emde.model.ExtensibleElement;

/**
 * EASE module for Capella.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class CapellaModule {

	/**
	 * Gets the {@link List} of {@link ElementExtension} with the given
	 * {@link EPackage#getNsURI() nsURI} and {@link EClass#getName() eclass name}
	 * type for the given {@link ExtensibleElement}.
	 * 
	 * @param element    the {@link ExtensibleElement}
	 * @param nsURI      the {@link EPackage#getNsURI() nsURI}
	 * @param eClassName the {@link EClass#getName() eclass name}
	 * @return the {@link List} of {@link ElementExtension} with the given
	 *         {@link EPackage#getNsURI() nsURI} and {@link EClass#getName() eclass
	 *         name} type for the given {@link ExtensibleElement}
	 */
	@WrapToScript
	public List<ElementExtension> getExtensions(ExtensibleElement element, String nsURI, String eClassName) {
		final List<ElementExtension> res = new ArrayList<>();

		final EClassifier eClassifier = EPackage.Registry.INSTANCE.getEPackage(nsURI).getEClassifier(eClassName);

		for (ElementExtension extension : element.getOwnedExtensions()) {
			if (eClassifier.isInstance(extension)) {
				res.add(extension);
			}
		}

		return res;
	}

	/**
	 * Calls the {@link IQuery} by its {@link Class#getCanonicalName() class
	 * canonical name} on the given {@link Object}.
	 * 
	 * @param queryClass the {@link Class#getCanonicalName() class canonical name}
	 * @param object     the {@link Object}
	 * @return result of the call
	 */
	@WrapToScript
	public List<Object> callQuery(String queryClass, Object object) {
		try {
			IQuery query = (IQuery) getClass().getClassLoader().loadClass(queryClass).getConstructor().newInstance();
			return query.compute(object);
		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException
				| NoSuchMethodException | SecurityException | ClassNotFoundException e) {
			throw new IllegalStateException(queryClass + " query can't be loaded.", e);
		}
	}

	/**
	 * Gets the list of available semantic browser queries for the given
	 * {@link EObject}.
	 * 
	 * @param obj the {@link EObject}
	 * @return the list of available semantic browser queries for the given
	 *         {@link EObject}
	 */
	@WrapToScript
	public List<String> getAvailableSBQueries(EObject obj) {
		List<String> result = new ArrayList<String>();
		Collection<EObject> col = new ArrayList<EObject>();
		col.add(obj);
		Set<ICategory> SBQueries = SemanticBrowserHelper.getCommonObjectCategories(col);
		for (ICategory cat : SBQueries) {
			result.add(cat.getName());
		}
		return result;
	}

	/**
	 * Gets the result of the given semantic browser query for the given
	 * {@link EObject}.
	 * 
	 * @param obj   the {@link EObject}
	 * @param query the semantic browser query
	 * @return the list of available semantic browser queries for the given
	 *         {@link EObject}
	 */
	@WrapToScript
	public List<EObject> getSBQuery(EObject obj, String query) {
		List<EObject> queryResult = new ArrayList<EObject>();
		Collection<EObject> col = new ArrayList<EObject>();
		col.add(obj);
		Set<ICategory> SBQueries = SemanticBrowserHelper.getCommonObjectCategories(col);
		ICategory category = null;
		for (ICategory cat : SBQueries) {
			if (cat.getName().equals(query)) {
				category = cat;
				break;
			}
		}
		if (category != null) {
			for (Object object : category.compute(obj)) {
				if (object instanceof EObject) {
					queryResult.add((EObject) object);
				}
			}
		}
		return queryResult;
	}

}
