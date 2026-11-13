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
package org.eclipse.ease.ui.scripts.repository.util;

import java.util.Map;
import org.eclipse.ease.ui.scripts.repository.IRawLocation;
import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ease.ui.scripts.repository.IStorage;
import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.Notifier;
import org.eclipse.emf.common.notify.impl.AdapterFactoryImpl;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> The <b>Adapter Factory</b> for the model. It provides an adapter <code>createXXX</code> method for each class of the model. <!--
 * end-user-doc -->
 * 
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage
 * @generated
 */
public class RepositoryAdapterFactory extends AdapterFactoryImpl {
	/**
	 * The cached model package. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	protected static IRepositoryPackage modelPackage;

	/**
	 * Creates an instance of the adapter factory. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public RepositoryAdapterFactory() {
		if (modelPackage == null) {
			modelPackage = IRepositoryPackage.eINSTANCE;
		}
	}

	/**
	 * Returns whether this factory is applicable for the type of the object. <!-- begin-user-doc --> This implementation returns <code>true</code> if the
	 * object is either the model's package or is an instance object of the model. <!-- end-user-doc -->
	 * 
	 * @return whether this factory is applicable for the type of the object.
	 * @generated
	 */
	@Override
	public boolean isFactoryForType(Object object) {
		if (object == modelPackage) {
			return true;
		}
		if (object instanceof EObject) {
			return ((EObject) object).eClass().getEPackage() == modelPackage;
		}
		return false;
	}

	/**
	 * The switch that delegates to the <code>createXXX</code> methods. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	protected RepositorySwitch<Adapter> modelSwitch = new RepositorySwitch<Adapter>() {
		@Override
		public Adapter caseScript(IScript object) {
			return createScriptAdapter();
		}

		@Override
		public Adapter caseRawLocation(IRawLocation object) {
			return createRawLocationAdapter();
		}

		@Override
		public Adapter caseStorage(IStorage object) {
			return createStorageAdapter();
		}

		@Override
		public Adapter caseScriptLocation(IScriptLocation object) {
			return createScriptLocationAdapter();
		}

		@Override
		public Adapter caseKeywordMap(Map.Entry<String, String> object) {
			return createKeywordMapAdapter();
		}

		@Override
		public Adapter defaultCase(EObject object) {
			return createEObjectAdapter();
		}
	};

	/**
	 * Creates an adapter for the <code>target</code>. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @param target
	 *            the object to adapt.
	 * @return the adapter for the <code>target</code>.
	 * @generated
	 */
	@Override
	public Adapter createAdapter(Notifier target) {
		return modelSwitch.doSwitch((EObject) target);
	}

	/**
	 * Creates a new adapter for an object of class '{@link org.eclipse.ease.ui.scripts.repository.IScript <em>Script</em>}'. <!-- begin-user-doc --> This
	 * default implementation returns null so that we can easily ignore cases; it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript
	 * @generated
	 */
	public Adapter createScriptAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation <em>Raw Location</em>}'. <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases; it's useful to ignore a case when inheritance will catch all the cases
	 * anyway. <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation
	 * @generated
	 */
	public Adapter createRawLocationAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link org.eclipse.ease.ui.scripts.repository.IStorage <em>Storage</em>}'. <!-- begin-user-doc --> This
	 * default implementation returns null so that we can easily ignore cases; it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @see org.eclipse.ease.ui.scripts.repository.IStorage
	 * @generated
	 */
	public Adapter createStorageAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation <em>Script Location</em>}'. <!--
	 * begin-user-doc --> This default implementation returns null so that we can easily ignore cases; it's useful to ignore a case when inheritance will catch
	 * all the cases anyway. <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation
	 * @generated
	 */
	public Adapter createScriptLocationAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link java.util.Map.Entry <em>Keyword Map</em>}'. <!-- begin-user-doc --> This default implementation
	 * returns null so that we can easily ignore cases; it's useful to ignore a case when inheritance will catch all the cases anyway. <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @see java.util.Map.Entry
	 * @generated
	 */
	public Adapter createKeywordMapAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for the default case. <!-- begin-user-doc --> This default implementation returns null. <!-- end-user-doc -->
	 * 
	 * @return the new adapter.
	 * @generated
	 */
	public Adapter createEObjectAdapter() {
		return null;
	}

} // RepositoryAdapterFactory
