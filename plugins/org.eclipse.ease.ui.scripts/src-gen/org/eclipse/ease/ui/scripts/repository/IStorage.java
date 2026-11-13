/**
 * Copyright (c) 2013 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 */
package org.eclipse.ease.ui.scripts.repository;

import java.util.Collection;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> A representation of the model object ' <em><b>Storage</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IStorage#getEntries <em>Entries</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getStorage()
 * @model
 * @generated
 */
public interface IStorage extends EObject {
	/**
	 * Returns the value of the '<em><b>Entries</b></em>' containment reference list. The list contents are of type
	 * {@link org.eclipse.ease.ui.scripts.repository.IScriptLocation}. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Entries</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>Entries</em>' containment reference list.
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getStorage_Entries()
	 * @model containment="true"
	 * @generated
	 */
	EList<IScriptLocation> getEntries();

	Collection<IScript> getScripts();
} // IStorage
