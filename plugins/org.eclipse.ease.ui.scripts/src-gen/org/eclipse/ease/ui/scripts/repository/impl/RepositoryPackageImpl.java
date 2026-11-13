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
import org.eclipse.ease.ui.scripts.repository.IRawLocation;
import org.eclipse.ease.ui.scripts.repository.IRepositoryFactory;
import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ease.ui.scripts.repository.IStorage;
import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.emf.ecore.impl.EPackageImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model <b>Package</b>. <!-- end-user-doc -->
 * 
 * @generated
 */
public class RepositoryPackageImpl extends EPackageImpl implements IRepositoryPackage {
	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EClass scriptEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EClass rawLocationEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EClass storageEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EClass scriptLocationEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EClass keywordMapEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EDataType pathEDataType = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private EDataType inputStreamEDataType = null;

	/**
	 * Creates an instance of the model <b>Package</b>, registered with {@link org.eclipse.emf.ecore.EPackage.Registry EPackage.Registry} by the package package
	 * URI value.
	 * <p>
	 * Note: the correct way to create the package is via the static factory method {@link #init init()}, which also performs initialization of the package, or
	 * returns the registered package, if one already exists. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.emf.ecore.EPackage.Registry
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#eNS_URI
	 * @see #init()
	 * @generated
	 */
	private RepositoryPackageImpl() {
		super(eNS_URI, IRepositoryFactory.eINSTANCE);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private static boolean isInited = false;

	/**
	 * Creates, registers, and initializes the <b>Package</b> for this model, and for any others upon which it depends.
	 *
	 * <p>
	 * This method is used to initialize {@link IRepositoryPackage#eINSTANCE} when that field is accessed. Clients should not invoke it directly. Instead, they
	 * should simply access that field to obtain the package. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see #eNS_URI
	 * @see #createPackageContents()
	 * @see #initializePackageContents()
	 * @generated
	 */
	public static IRepositoryPackage init() {
		if (isInited)
			return (IRepositoryPackage) EPackage.Registry.INSTANCE.getEPackage(IRepositoryPackage.eNS_URI);

		// Obtain or create and register package
		RepositoryPackageImpl theRepositoryPackage = (RepositoryPackageImpl) (EPackage.Registry.INSTANCE.get(eNS_URI) instanceof RepositoryPackageImpl
				? EPackage.Registry.INSTANCE.get(eNS_URI) : new RepositoryPackageImpl());

		isInited = true;

		// Create package meta-data objects
		theRepositoryPackage.createPackageContents();

		// Initialize created meta-data
		theRepositoryPackage.initializePackageContents();

		// Mark meta-data to indicate it can't be changed
		theRepositoryPackage.freeze();

		// Update the registry and return the package
		EPackage.Registry.INSTANCE.put(IRepositoryPackage.eNS_URI, theRepositoryPackage);
		return theRepositoryPackage;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EClass getScript() {
		return scriptEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EAttribute getScript_Timestamp() {
		return (EAttribute) scriptEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EReference getScript_Entry() {
		return (EReference) scriptEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public EReference getScript_ScriptKeywords() {
		return (EReference) scriptEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public EReference getScript_UserKeywords() {
		return (EReference) scriptEClass.getEStructuralFeatures().get(3);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EOperation getScript__Run() {
		return scriptEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EOperation getScript__GetName() {
		return scriptEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EOperation getScript__GetPath() {
		return scriptEClass.getEOperations().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EClass getRawLocation() {
		return rawLocationEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EAttribute getRawLocation_Location() {
		return (EAttribute) rawLocationEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EAttribute getRawLocation_UpdatePending() {
		return (EAttribute) rawLocationEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EOperation getRawLocation__GetResource() {
		return rawLocationEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EOperation getRawLocation__GetInputStream() {
		return rawLocationEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EClass getStorage() {
		return storageEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EReference getStorage_Entries() {
		return (EReference) storageEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EClass getScriptLocation() {
		return scriptLocationEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EAttribute getScriptLocation_Recursive() {
		return (EAttribute) scriptLocationEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EAttribute getScriptLocation_Default() {
		return (EAttribute) scriptLocationEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EReference getScriptLocation_Scripts() {
		return (EReference) scriptLocationEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public EClass getKeywordMap() {
		return keywordMapEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public EAttribute getKeywordMap_Key() {
		return (EAttribute) keywordMapEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public EAttribute getKeywordMap_Value() {
		return (EAttribute) keywordMapEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EDataType getPath() {
		return pathEDataType;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public EDataType getInputStream() {
		return inputStreamEDataType;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public IRepositoryFactory getRepositoryFactory() {
		return (IRepositoryFactory) getEFactoryInstance();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private boolean isCreated = false;

	/**
	 * Creates the meta-model objects for the package. This method is guarded to have no affect on any invocation but its first. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @generated
	 */
	public void createPackageContents() {
		if (isCreated)
			return;
		isCreated = true;

		// Create classes and their features
		scriptEClass = createEClass(SCRIPT);
		createEAttribute(scriptEClass, SCRIPT__TIMESTAMP);
		createEReference(scriptEClass, SCRIPT__ENTRY);
		createEReference(scriptEClass, SCRIPT__SCRIPT_KEYWORDS);
		createEReference(scriptEClass, SCRIPT__USER_KEYWORDS);
		createEOperation(scriptEClass, SCRIPT___RUN);
		createEOperation(scriptEClass, SCRIPT___GET_NAME);
		createEOperation(scriptEClass, SCRIPT___GET_PATH);

		rawLocationEClass = createEClass(RAW_LOCATION);
		createEAttribute(rawLocationEClass, RAW_LOCATION__LOCATION);
		createEAttribute(rawLocationEClass, RAW_LOCATION__UPDATE_PENDING);
		createEOperation(rawLocationEClass, RAW_LOCATION___GET_RESOURCE);
		createEOperation(rawLocationEClass, RAW_LOCATION___GET_INPUT_STREAM);

		storageEClass = createEClass(STORAGE);
		createEReference(storageEClass, STORAGE__ENTRIES);

		scriptLocationEClass = createEClass(SCRIPT_LOCATION);
		createEAttribute(scriptLocationEClass, SCRIPT_LOCATION__RECURSIVE);
		createEAttribute(scriptLocationEClass, SCRIPT_LOCATION__DEFAULT);
		createEReference(scriptLocationEClass, SCRIPT_LOCATION__SCRIPTS);

		keywordMapEClass = createEClass(KEYWORD_MAP);
		createEAttribute(keywordMapEClass, KEYWORD_MAP__KEY);
		createEAttribute(keywordMapEClass, KEYWORD_MAP__VALUE);

		// Create data types
		pathEDataType = createEDataType(PATH);
		inputStreamEDataType = createEDataType(INPUT_STREAM);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private boolean isInitialized = false;

	/**
	 * Complete the initialization of the package and its meta-model. This method is guarded to have no affect on any invocation but its first. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	public void initializePackageContents() {
		if (isInitialized)
			return;
		isInitialized = true;

		// Initialize package
		setName(eNAME);
		setNsPrefix(eNS_PREFIX);
		setNsURI(eNS_URI);

		// Create type parameters

		// Set bounds for type parameters

		// Add supertypes to classes
		scriptEClass.getESuperTypes().add(this.getRawLocation());
		scriptLocationEClass.getESuperTypes().add(this.getRawLocation());

		// Initialize classes, features, and operations; add parameters
		initEClass(scriptEClass, IScript.class, "Script", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getScript_Timestamp(), ecorePackage.getELong(), "timestamp", "-1", 1, 1, IScript.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE,
				!IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getScript_Entry(), this.getScriptLocation(), this.getScriptLocation_Scripts(), "entry", null, 1, 1, IScript.class, !IS_TRANSIENT,
				!IS_VOLATILE, IS_CHANGEABLE, !IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getScript_ScriptKeywords(), this.getKeywordMap(), null, "scriptKeywords", null, 0, -1, IScript.class, !IS_TRANSIENT, !IS_VOLATILE,
				IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getScript_UserKeywords(), this.getKeywordMap(), null, "userKeywords", null, 0, -1, IScript.class, !IS_TRANSIENT, !IS_VOLATILE,
				IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEOperation(getScript__Run(), null, "run", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getScript__GetName(), ecorePackage.getEString(), "getName", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getScript__GetPath(), this.getPath(), "getPath", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEClass(rawLocationEClass, IRawLocation.class, "RawLocation", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getRawLocation_Location(), ecorePackage.getEString(), "location", null, 1, 1, IRawLocation.class, !IS_TRANSIENT, !IS_VOLATILE,
				IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getRawLocation_UpdatePending(), ecorePackage.getEBoolean(), "updatePending", "false", 1, 1, IRawLocation.class, IS_TRANSIENT,
				!IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEOperation(getRawLocation__GetResource(), ecorePackage.getEJavaObject(), "getResource", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getRawLocation__GetInputStream(), this.getInputStream(), "getInputStream", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEClass(storageEClass, IStorage.class, "Storage", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEReference(getStorage_Entries(), this.getScriptLocation(), null, "entries", null, 0, -1, IStorage.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE,
				IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(scriptLocationEClass, IScriptLocation.class, "ScriptLocation", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getScriptLocation_Recursive(), ecorePackage.getEBoolean(), "recursive", "false", 1, 1, IScriptLocation.class, !IS_TRANSIENT,
				!IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getScriptLocation_Default(), ecorePackage.getEBoolean(), "default", "false", 1, 1, IScriptLocation.class, !IS_TRANSIENT, !IS_VOLATILE,
				IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getScriptLocation_Scripts(), this.getScript(), this.getScript_Entry(), "scripts", null, 0, -1, IScriptLocation.class, !IS_TRANSIENT,
				!IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(keywordMapEClass, Map.Entry.class, "KeywordMap", !IS_ABSTRACT, !IS_INTERFACE, !IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getKeywordMap_Key(), ecorePackage.getEString(), "key", null, 1, 1, Map.Entry.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE,
				!IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getKeywordMap_Value(), ecorePackage.getEString(), "value", null, 1, 1, Map.Entry.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE,
				!IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		// Initialize data types
		initEDataType(pathEDataType, IPath.class, "Path", IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);
		initEDataType(inputStreamEDataType, InputStream.class, "InputStream", IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);

		// Create resource
		createResource(eNS_URI);
	}

} // RepositoryPackageImpl
