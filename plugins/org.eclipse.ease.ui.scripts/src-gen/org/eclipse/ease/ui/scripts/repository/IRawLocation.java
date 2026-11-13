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

import java.io.InputStream;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> A representation of the model object '<em><b>Raw Location</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#getLocation <em>Location</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#isUpdatePending <em>Update Pending</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getRawLocation()
 * @model
 * @generated
 */
public interface IRawLocation extends EObject {
	/**
	 * Returns the value of the '<em><b>Location</b></em>' attribute. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Location</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * 
	 * @return the value of the '<em>Location</em>' attribute.
	 * @see #setLocation(String)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getRawLocation_Location()
	 * @model required="true"
	 * @generated
	 */
	String getLocation();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#getLocation <em>Location</em>}' attribute. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @param value
	 *            the new value of the '<em>Location</em>' attribute.
	 * @see #getLocation()
	 * @generated
	 */
	void setLocation(String value);

	/**
	 * Returns the value of the '<em><b>Update Pending</b></em>' attribute. The default value is <code>"false"</code>. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Update Pending</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * 
	 * @return the value of the '<em>Update Pending</em>' attribute.
	 * @see #setUpdatePending(boolean)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getRawLocation_UpdatePending()
	 * @model default="false" required="true" transient="true"
	 * @generated
	 */
	boolean isUpdatePending();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#isUpdatePending <em>Update Pending</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @param value
	 *            the new value of the '<em>Update Pending</em>' attribute.
	 * @see #isUpdatePending()
	 * @generated
	 */
	void setUpdatePending(boolean value);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @model kind="operation"
	 * @generated
	 */
	Object getResource();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @model kind="operation" dataType="org.eclipse.ease.ui.scripts.repository.InputStream"
	 * @generated
	 */
	InputStream getInputStream();

} // IRawLocation
