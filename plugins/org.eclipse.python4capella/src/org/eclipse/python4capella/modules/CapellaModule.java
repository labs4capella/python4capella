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
import org.eclipse.emf.ecore.EObject;
import org.polarsys.capella.common.helpers.EObjectExt;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.ui.massactions.core.shared.helper.SemanticBrowserHelper;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;
import org.polarsys.capella.core.data.capellacommon.CapellacommonPackage;
import org.polarsys.capella.core.data.cs.Component;
import org.polarsys.capella.core.data.cs.ComponentPkg;

/**
 * EASE module for Capella.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class CapellaModule {

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

	/**
	 * Gets the version of Capella.
	 * 
	 * @return the version of Capella
	 */
	@WrapToScript
	public String getCapellaVersion() {
		final String ensUri = CapellacommonPackage.eNS_URI;

		return ensUri.substring(ensUri.lastIndexOf('/') + 1);
	}

	/**
	 * Gets the label of the given {@link EObject}.
	 * 
	 * @param eObject the {@link EObject}
	 */
	@WrapToScript
	public String getLabel(EObject eObject) {
		return EObjectExt.getText(eObject);
	}

	/**
	 * Tells if the given {@link Object} is a system.
	 * 
	 * @param component the {@link Object}
	 * @return <code>true</code> if the given {@link Object} is a system,
	 *         <code>false</code> otherwise
	 */
	@WrapToScript
	public boolean isSystem(Object object) {
		boolean res = false;

		if (object instanceof Component) {
			final Component component = (Component) object;
			if (!component.isActor()) {
				if (component.eContainer() instanceof ComponentPkg) {
					final Object eGetValue = component.eContainer().eGet(component.eContainingFeature());
					if (eGetValue instanceof List) {
						@SuppressWarnings("unchecked")
						final List<Component> components = (List<Component>) eGetValue;
						for (Component comp : components) {
							if (!comp.isActor()) {
								res = comp == component;
								break;
							}
						}
					}
				}
			}
		}

		return res;
	}

}
