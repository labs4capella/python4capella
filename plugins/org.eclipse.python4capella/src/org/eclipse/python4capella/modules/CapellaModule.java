/**
 *   Copyright (c) 2021, 2024 THALES GLOBAL SERVICES
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
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sirius.business.api.query.EObjectQuery;
import org.polarsys.capella.common.helpers.EObjectExt;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.libraries.ILibraryManager;
import org.polarsys.capella.common.libraries.IModel;
import org.polarsys.capella.common.libraries.manager.LibraryManagerExt;
import org.polarsys.capella.common.ui.massactions.core.shared.helper.SemanticBrowserHelper;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;
import org.polarsys.capella.core.data.capellacommon.CapellacommonPackage;
import org.polarsys.capella.core.data.capellamodeller.Project;
import org.polarsys.capella.core.data.capellamodeller.SystemEngineering;
import org.polarsys.capella.core.libraries.model.CapellaModel;
import org.polarsys.capella.core.libraries.queries.QueryExt;
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
	 * Gets the array of available semantic browser queries for the given
	 * {@link EObject}.
	 * 
	 * @param obj the {@link EObject}
	 * @return the array of available semantic browser queries for the given
	 *         {@link EObject}
	 */
	@WrapToScript
	public String[] getAvailableSBQueries(EObject obj) {
		List<String> result = new ArrayList<String>();
		Collection<EObject> col = new ArrayList<EObject>();
		col.add(obj);
		Set<ICategory> SBQueries = SemanticBrowserHelper.getCommonObjectCategories(col);
		for (ICategory cat : SBQueries) {
			result.add(cat.getName());
		}
		return result.toArray(new String[result.size()]);
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
		// this need to be accessed via the instance to be independent from the build
		// target platform
		final String ensUri = CapellacommonPackage.eINSTANCE.getNsURI();

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
	 * Gets the array of {@link SystemEngineering} used as libraries of the given
	 * {@link SystemEngineering}.
	 * 
	 * @param system {@link SystemEngineering}
	 * @return the array of {@link SystemEngineering} used as libraries of the given
	 *         {@link SystemEngineering}
	 */
	@WrapToScript
	public SystemEngineering[] getLibraries(SystemEngineering system) {
		final List<SystemEngineering> res = new ArrayList<>();

		if (system != null) {
			final IModel currentProject = ILibraryManager.INSTANCE.getModel(system);
			final TransactionalEditingDomain domain = new EObjectQuery(system).getSession()
					.getTransactionalEditingDomain();
			final Collection<IModel> libraries = LibraryManagerExt.getActivesReferences(currentProject);
			for (IModel library : libraries) {
				if (library instanceof CapellaModel) {
					final Project libraryProject = ((CapellaModel) library).getProject(domain);
					final SystemEngineering systemEngineering = QueryExt.getSystemEngineeringFrom(libraryProject);
					if (systemEngineering != null) {
						res.add(systemEngineering);
					}
				}
			}
		}

		return res.toArray(new SystemEngineering[res.size()]);
	}

	/**
	 * Gets the {@link List} of {@link ElementExtension} of the given {@link EClass
	 * type} for the given {@link ExtensibleElement}.
	 * 
	 * @param element the {@link ExtensibleElement}
	 * @param eCls    the {@link EClass} used to filter
	 * @return the {@link List} of {@link ElementExtension} of the given
	 *         {@link EClass type} for the given {@link ExtensibleElement}
	 */
	@WrapToScript
	public List<ElementExtension> getExtensions(ExtensibleElement element, EClass eCls) {
		final List<ElementExtension> res = new ArrayList<>();

		for (ElementExtension extension : element.getOwnedExtensions()) {
			if (eCls.isInstance(extension)) {
				res.add(extension);
			}
		}

		return res;
	}

}
