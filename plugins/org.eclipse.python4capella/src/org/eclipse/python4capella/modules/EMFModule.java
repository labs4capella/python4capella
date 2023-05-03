/**
 *   Copyright (c) 2021, 2023 THALES GLOBAL SERVICES
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

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.emf.common.util.Enumerator;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.EEnumLiteral;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.emf.ecore.EStructuralFeature.Setting;
import org.eclipse.emf.ecore.util.ECrossReferenceAdapter;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.sirius.business.api.query.EObjectQuery;
import org.eclipse.sirius.business.api.session.Session;

/**
 * EASE module for EMF.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class EMFModule {

	/**
	 * Deletes the given {@link EObject}.
	 * 
	 * @param eObj the {@link EObject} to delete
	 */
	@WrapToScript
	public void delete(EObject eObj) {
		EcoreUtil.delete(eObj);
	}

	/**
	 * Creates an instance of the {@link EClass} in the {@link EPackage} with the
	 * given {@link EPackage#getNsURI() nsURI} and the given {@link EClass#getName()
	 * eclass name}.
	 * 
	 * @param nsURI      the {@link EPackage#getNsURI() nsURI}
	 * @param eClassName the {@link EClass#getName() eclass name}
	 * @return the created instance of the {@link EClass} in the {@link EPackage}
	 *         with the given {@link EPackage#getNsURI() nsURI} and the given
	 *         {@link EClass#getName() name}
	 */
	@WrapToScript
	public EObject create(String nsURI, String eClassName) {
		final EClassifier eClassifier = EPackage.Registry.INSTANCE.getEPackage(nsURI).getEClassifier(eClassName);

		return createFromEClassifier(eClassifier);
	}

	/**
	 * Creates an instance of the given {@link EClassifier}.
	 * 
	 * @param eClassifier
	 * @return the created instance of the given {@link EClassifier}
	 */
	@WrapToScript
	public EObject createFromEClassifier(EClassifier eClassifier) {
		if (eClassifier instanceof EClass) {
			return EcoreUtil.create((EClass) eClassifier);
		} else {
			throw new IllegalStateException("only instance of EClasses can be created.");
		}
	}

	/**
	 * Get the {@link EClassifier} in the {@link EPackage} with the given
	 * {@link EPackage#getNsURI() nsURI} and the given {@link EClass#getName()
	 * eclass name}.
	 * 
	 * @param nsURI      the {@link EPackage#getNsURI() nsURI}
	 * @param eClassName the {@link EClass#getName() eclass name}
	 * @return the {@link EClassifier} in the {@link EPackage} with the given
	 *         {@link EPackage#getNsURI() nsURI} and the given
	 *         {@link EClass#getName() eclass name}
	 */
	@WrapToScript
	public EClassifier getEClassifier(String nsURI, String eClassName) {
		return EPackage.Registry.INSTANCE.getEPackage(nsURI).getEClassifier(eClassName);
	}

	/**
	 * Gets the {@link List} all {@link EObject} contained directly or indirectly in
	 * the given {@link EObject}.
	 * 
	 * @param eObj the {@link EObject}
	 * @return the {@link List} all {@link EObject} contained directly or indirectly
	 *         in the given {@link EObject}
	 */
	@WrapToScript
	public List<EObject> eAllContents(EObject eObj) {
		final List<EObject> res = new ArrayList<EObject>();

		final Iterator<EObject> it = eObj.eAllContents();
		while (it.hasNext()) {
			final EObject child = it.next();
			res.add(child);
		}

		return res;
	}

	/**
	 * Gets the {@link List} all {@link EObject} contained directly or indirectly in
	 * the given {@link EObject} that are instances of the given
	 * {@link EClassifier}.
	 * 
	 * @param eObj        the {@link EObject}
	 * @param eClassifier the {@link EClassifier} to use as filter
	 * @return the {@link List} all {@link EObject} contained directly or indirectly
	 *         in the given {@link EObject} that are instances of the given
	 *         {@link EClassifier}
	 */
	@WrapToScript
	public List<EObject> eAllContentsByType(EObject eObj, EClassifier eClassifier) {
		final List<EObject> res = new ArrayList<EObject>();

		final Iterator<EObject> it = eObj.eAllContents();
		while (it.hasNext()) {
			final EObject child = it.next();
			if (eClassifier.isInstance(child)) {
				res.add(child);
			}
		}

		return res;
	}

	/**
	 * Gets the {@link Enumerator} for the given {@link EPackage#getNsURI() nsURI},
	 * {@link EEnum#getName() eenum name} and {@link EEnumLiteral#getName() eenume
	 * literal name}.
	 * 
	 * @param nsURI       the {@link EPackage#getNsURI() nsURI}
	 * @param enumName    the {@link EEnum#getName() eenum name}
	 * @param literalName the {@link EEnumLiteral#getName() eenume literal name}
	 * @return the {@link Enumerator} for the given {@link EPackage#getNsURI()
	 *         nsURI}, {@link EEnum#getName() eenum name} and
	 *         {@link EEnumLiteral#getName() eenume literal name}
	 */
	@WrapToScript
	public Enumerator getEnumLiteral(String nsURI, String enumName, String literalName) {
		return ((EEnum) EPackage.Registry.INSTANCE.getEPackage(nsURI).getEClassifier(enumName))
				.getEEnumLiteral(literalName).getInstance();
	}

	/**
	 * Gets the {@link List} of object referencing the given {@link EObject}.
	 * 
	 * @param eObj the {@link EObject}
	 * @return the {@link List} of object referencing the given {@link EObject}
	 * 
	 */
	@WrapToScript
	public List<EObject> eInverse(EObject eObj) {
		return new ArrayList<EObject>(getInverseReferences(eObj, s -> true));
	}

	/**
	 * Gets the {@link List} of object referencing the given {@link EObject}
	 * instances of the given {@link EClassifier}.
	 * 
	 * @param eObj        the {@link EObject}
	 * @param eClassifier the {@link EClassifier}
	 * @return the {@link List} of object referencing the given {@link EObject}
	 *         instances of the given {@link EClassifier}
	 */
	@WrapToScript
	public List<EObject> eInverseByType(EObject eObj, EClassifier eClassifier) {
		return new ArrayList<EObject>(getInverseReferences(eObj, s -> eClassifier.isInstance(s.getEObject())));
	}

	/**
	 * Gets the {@link List} of object referencing the given {@link EObject} via an
	 * {@link EReference} with the given name.
	 * 
	 * @param eObj          the {@link EObject}
	 * @param referenceName the {@link EReference} name
	 * @return the {@link List} of object referencing the given {@link EObject} via
	 *         an {@link EReference} with the given name
	 */
	@WrapToScript
	public List<EObject> eInverseByName(EObject eObj, String referenceName) {
		return new ArrayList<EObject>(getInverseReferences(eObj,
				s -> s.getEStructuralFeature() != null && s.getEStructuralFeature().getName().equals(referenceName)));
	}

	/**
	 * Finds all the objects in the session which reference the given EObject
	 * through a setting matching the specified predicate. The queried EObject must
	 * be part of an opened Sirius session.
	 * 
	 * @param eObj      the {@link EObject}
	 * @param predicate the predicate to use to match incoming references to this
	 *                  object.
	 * @return all the EObjects in the same session as this EObject which point to
	 *         it through a matching setting.
	 */
	private Collection<EObject> getInverseReferences(EObject eObj, Predicate<Setting> predicate) {
		final Collection<EObject> res;
		Objects.requireNonNull(predicate);
		final ECrossReferenceAdapter xref;
		final Session session = new EObjectQuery(eObj).getSession();
		if (session != null) {
			xref = session.getSemanticCrossReferencer();
			if (xref == null) {
				res = Collections.emptySet();
			} else {
				res = xref.getInverseReferences(eObj).stream().filter(predicate).map(s -> s.getEObject())
						.collect(Collectors.toCollection(LinkedHashSet::new));
			}
		} else {
			res = Collections.emptySet();
		}

		return res;
	}

	@WrapToScript
	public EObject copy(EObject eObj) {
		return EcoreUtil.copy(eObj);
	}

	@WrapToScript
	public List<EObject> copyAll(List<EObject> eObjects) {
		return new ArrayList<>(EcoreUtil.copyAll(eObjects));
	}

}
