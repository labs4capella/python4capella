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

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc --> A representation of the model object ' <em><b>Script Location</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isRecursive <em>Recursive</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isDefault <em>Default</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#getScripts <em>Scripts</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScriptLocation()
 * @model
 * @generated
 */
public interface IScriptLocation extends IRawLocation {
	/**
	 * Returns the value of the '<em><b>Recursive</b></em>' attribute. The default value is <code>"false"</code>. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Recursive</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * 
	 * @return the value of the '<em>Recursive</em>' attribute.
	 * @see #setRecursive(boolean)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScriptLocation_Recursive()
	 * @model default="false" required="true"
	 * @generated
	 */
	boolean isRecursive();

	/**
	 * Sets the value of the ' {@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isRecursive <em>Recursive</em>}' attribute. <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * 
	 * @param value
	 *            the new value of the '<em>Recursive</em>' attribute.
	 * @see #isRecursive()
	 * @generated
	 */
	void setRecursive(boolean value);

	/**
	 * Returns the value of the '<em><b>Default</b></em>' attribute. The default value is <code>"false"</code>. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Default</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * 
	 * @return the value of the '<em>Default</em>' attribute.
	 * @see #setDefault(boolean)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScriptLocation_Default()
	 * @model default="false" required="true"
	 * @generated
	 */
	boolean isDefault();

	/**
	 * Sets the value of the ' {@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isDefault <em>Default</em>}' attribute. <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * 
	 * @param value
	 *            the new value of the '<em>Default</em>' attribute.
	 * @see #isDefault()
	 * @generated
	 */
	void setDefault(boolean value);

	/**
	 * Returns the value of the '<em><b>Scripts</b></em>' containment reference list. The list contents are of type
	 * {@link org.eclipse.ease.ui.scripts.repository.IScript}. It is bidirectional and its opposite is
	 * '{@link org.eclipse.ease.ui.scripts.repository.IScript#getEntry <em>Entry</em>}'. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Scripts</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * 
	 * @return the value of the '<em>Scripts</em>' containment reference list.
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScriptLocation_Scripts()
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getEntry
	 * @model opposite="entry" containment="true"
	 * @generated
	 */
	EList<IScript> getScripts();

} // IScriptLocation
