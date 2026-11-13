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
package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.InputStream;
import java.util.Map;
import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.ui.scripts.repository.*;
import org.eclipse.ease.ui.scripts.repository.IRawLocation;
import org.eclipse.ease.ui.scripts.repository.IRepositoryFactory;
import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ease.ui.scripts.repository.IStorage;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.impl.EFactoryImpl;
import org.eclipse.emf.ecore.plugin.EcorePlugin;

/**
 * <!-- begin-user-doc --> An implementation of the model <b>Factory</b>. <!-- end-user-doc -->
 * 
 * @generated
 */
public class RepositoryFactoryImpl extends EFactoryImpl implements IRepositoryFactory {
	/**
	 * Creates the default factory implementation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public static IRepositoryFactory init() {
		try {
			IRepositoryFactory theRepositoryFactory = (IRepositoryFactory) EPackage.Registry.INSTANCE.getEFactory(IRepositoryPackage.eNS_URI);
			if (theRepositoryFactory != null) {
				return theRepositoryFactory;
			}
		} catch (Exception exception) {
			EcorePlugin.INSTANCE.log(exception);
		}
		return new RepositoryFactoryImpl();
	}

	/**
	 * Creates an instance of the factory. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public RepositoryFactoryImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EObject create(EClass eClass) {
		switch (eClass.getClassifierID()) {
		case IRepositoryPackage.SCRIPT:
			return createScript();
		case IRepositoryPackage.RAW_LOCATION:
			return createRawLocation();
		case IRepositoryPackage.STORAGE:
			return createStorage();
		case IRepositoryPackage.SCRIPT_LOCATION:
			return createScriptLocation();
		case IRepositoryPackage.KEYWORD_MAP:
			return (EObject) createKeywordMap();
		default:
			throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public Object createFromString(EDataType eDataType, String initialValue) {
		switch (eDataType.getClassifierID()) {
		case IRepositoryPackage.PATH:
			return createPathFromString(eDataType, initialValue);
		case IRepositoryPackage.INPUT_STREAM:
			return createInputStreamFromString(eDataType, initialValue);
		default:
			throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public String convertToString(EDataType eDataType, Object instanceValue) {
		switch (eDataType.getClassifierID()) {
		case IRepositoryPackage.PATH:
			return convertPathToString(eDataType, instanceValue);
		case IRepositoryPackage.INPUT_STREAM:
			return convertInputStreamToString(eDataType, instanceValue);
		default:
			throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IScript createScript() {
		ScriptImpl script = new ScriptImpl();
		return script;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IRawLocation createRawLocation() {
		RawLocationImpl rawLocation = new RawLocationImpl();
		return rawLocation;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IStorage createStorage() {
		StorageImpl storage = new StorageImpl();
		return storage;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IScriptLocation createScriptLocation() {
		ScriptLocationImpl scriptLocation = new ScriptLocationImpl();
		return scriptLocation;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public Map.Entry<String, String> createKeywordMap() {
		KeywordMapImpl keywordMap = new KeywordMapImpl();
		return keywordMap;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public IPath createPathFromString(EDataType eDataType, String initialValue) {
		return (IPath) super.createFromString(eDataType, initialValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public String convertPathToString(EDataType eDataType, Object instanceValue) {
		return super.convertToString(eDataType, instanceValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public InputStream createInputStreamFromString(EDataType eDataType, String initialValue) {
		return (InputStream) super.createFromString(eDataType, initialValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public String convertInputStreamToString(EDataType eDataType, Object instanceValue) {
		return super.convertToString(eDataType, instanceValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IRepositoryPackage getRepositoryPackage() {
		return (IRepositoryPackage) getEPackage();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @deprecated
	 * @generated
	 */
	@Deprecated
	public static IRepositoryPackage getPackage() {
		return IRepositoryPackage.eINSTANCE;
	}

} // RepositoryFactoryImpl
