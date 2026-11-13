/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/
/**
 */
package org.eclipse.ease.ui.scripts.repository;

import org.eclipse.emf.ecore.EFactory;

/**
 * <!-- begin-user-doc --> The <b>Factory</b> for the model. It provides a create method for each non-abstract class of the model. <!-- end-user-doc -->
 * 
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage
 * @generated
 */
public interface IRepositoryFactory extends EFactory {
	/**
	 * The singleton instance of the factory. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	IRepositoryFactory eINSTANCE = org.eclipse.ease.ui.scripts.repository.impl.RepositoryFactoryImpl.init();

	/**
	 * Returns a new object of class '<em>Script</em>'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return a new object of class '<em>Script</em>'.
	 * @generated
	 */
	IScript createScript();

	/**
	 * Returns a new object of class '<em>Raw Location</em>'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return a new object of class '<em>Raw Location</em>'.
	 * @generated
	 */
	IRawLocation createRawLocation();

	/**
	 * Returns a new object of class '<em>Storage</em>'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return a new object of class '<em>Storage</em>'.
	 * @generated
	 */
	IStorage createStorage();

	/**
	 * Returns a new object of class '<em>Script Location</em>'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return a new object of class '<em>Script Location</em>'.
	 * @generated
	 */
	IScriptLocation createScriptLocation();

	/**
	 * Returns the package supported by this factory. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the package supported by this factory.
	 * @generated
	 */
	IRepositoryPackage getRepositoryPackage();

} // IRepositoryFactory
