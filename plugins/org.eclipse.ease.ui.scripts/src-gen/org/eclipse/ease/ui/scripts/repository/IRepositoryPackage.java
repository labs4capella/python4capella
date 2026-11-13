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

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

/**
 * <!-- begin-user-doc --> The <b>Package</b> for the model. It contains accessors for the meta objects to represent
 * <ul>
 * <li>each class,</li>
 * <li>each feature of each class,</li>
 * <li>each operation of each class,</li>
 * <li>each enum,</li>
 * <li>and each data type</li>
 * </ul>
 * <!-- end-user-doc -->
 * 
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryFactory
 * @model kind="package"
 * @generated
 */
public interface IRepositoryPackage extends EPackage {
	/**
	 * The package name. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	String eNAME = "repository";

	/**
	 * The package namespace URI. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	String eNS_URI = "repository";

	/**
	 * The package namespace name. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	String eNS_PREFIX = "repository";

	/**
	 * The singleton instance of the package. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	IRepositoryPackage eINSTANCE = org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl.init();

	/**
	 * The meta object id for the ' {@link org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl <em>Raw Location</em>}' class. <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getRawLocation()
	 * @generated
	 */
	int RAW_LOCATION = 1;

	/**
	 * The feature id for the '<em><b>Location</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION__LOCATION = 0;

	/**
	 * The feature id for the '<em><b>Update Pending</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION__UPDATE_PENDING = 1;

	/**
	 * The number of structural features of the '<em>Raw Location</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION_FEATURE_COUNT = 2;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION___GET_RESOURCE = 0;

	/**
	 * The operation id for the '<em>Get Input Stream</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION___GET_INPUT_STREAM = 1;

	/**
	 * The number of operations of the '<em>Raw Location</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int RAW_LOCATION_OPERATION_COUNT = 2;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl <em>Script</em>}' class. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @see org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getScript()
	 * @generated
	 */
	int SCRIPT = 0;

	/**
	 * The feature id for the '<em><b>Location</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__LOCATION = RAW_LOCATION__LOCATION;

	/**
	 * The feature id for the '<em><b>Update Pending</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__UPDATE_PENDING = RAW_LOCATION__UPDATE_PENDING;

	/**
	 * The feature id for the '<em><b>Timestamp</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__TIMESTAMP = RAW_LOCATION_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Entry</b></em>' container reference. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__ENTRY = RAW_LOCATION_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Script Keywords</b></em>' map. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__SCRIPT_KEYWORDS = RAW_LOCATION_FEATURE_COUNT + 2;

	/**
	 * The feature id for the '<em><b>User Keywords</b></em>' map. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT__USER_KEYWORDS = RAW_LOCATION_FEATURE_COUNT + 3;

	/**
	 * The number of structural features of the '<em>Script</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_FEATURE_COUNT = RAW_LOCATION_FEATURE_COUNT + 4;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT___GET_RESOURCE = RAW_LOCATION___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Get Input Stream</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT___GET_INPUT_STREAM = RAW_LOCATION___GET_INPUT_STREAM;

	/**
	 * The operation id for the '<em>Run</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT___RUN = RAW_LOCATION_OPERATION_COUNT + 0;

	/**
	 * The operation id for the '<em>Get Name</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT___GET_NAME = RAW_LOCATION_OPERATION_COUNT + 1;

	/**
	 * The operation id for the '<em>Get Path</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT___GET_PATH = RAW_LOCATION_OPERATION_COUNT + 2;

	/**
	 * The number of operations of the '<em>Script</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_OPERATION_COUNT = RAW_LOCATION_OPERATION_COUNT + 3;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.ui.scripts.repository.impl.StorageImpl <em>Storage</em>}' class. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @see org.eclipse.ease.ui.scripts.repository.impl.StorageImpl
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getStorage()
	 * @generated
	 */
	int STORAGE = 2;

	/**
	 * The feature id for the '<em><b>Entries</b></em>' containment reference list. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int STORAGE__ENTRIES = 0;

	/**
	 * The number of structural features of the '<em>Storage</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int STORAGE_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Storage</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int STORAGE_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptLocationImpl <em>Script Location</em>}' class. <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.ease.ui.scripts.repository.impl.ScriptLocationImpl
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getScriptLocation()
	 * @generated
	 */
	int SCRIPT_LOCATION = 3;

	/**
	 * The feature id for the '<em><b>Location</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION__LOCATION = RAW_LOCATION__LOCATION;

	/**
	 * The feature id for the '<em><b>Update Pending</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION__UPDATE_PENDING = RAW_LOCATION__UPDATE_PENDING;

	/**
	 * The feature id for the '<em><b>Recursive</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION__RECURSIVE = RAW_LOCATION_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Default</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION__DEFAULT = RAW_LOCATION_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Scripts</b></em>' containment reference list. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION__SCRIPTS = RAW_LOCATION_FEATURE_COUNT + 2;

	/**
	 * The number of structural features of the '<em>Script Location</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION_FEATURE_COUNT = RAW_LOCATION_FEATURE_COUNT + 3;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION___GET_RESOURCE = RAW_LOCATION___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Get Input Stream</em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION___GET_INPUT_STREAM = RAW_LOCATION___GET_INPUT_STREAM;

	/**
	 * The number of operations of the '<em>Script Location</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int SCRIPT_LOCATION_OPERATION_COUNT = RAW_LOCATION_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.ui.scripts.repository.impl.KeywordMapImpl <em>Keyword Map</em>}' class. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @see org.eclipse.ease.ui.scripts.repository.impl.KeywordMapImpl
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getKeywordMap()
	 * @generated
	 */
	int KEYWORD_MAP = 4;

	/**
	 * The feature id for the '<em><b>Key</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int KEYWORD_MAP__KEY = 0;

	/**
	 * The feature id for the '<em><b>Value</b></em>' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int KEYWORD_MAP__VALUE = 1;

	/**
	 * The number of structural features of the '<em>Keyword Map</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int KEYWORD_MAP_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Keyword Map</em>' class. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 * @ordered
	 */
	int KEYWORD_MAP_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '<em>Path</em>' data type. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.core.runtime.IPath
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getPath()
	 * @generated
	 */
	int PATH = 5;

	/**
	 * The meta object id for the '<em>Input Stream</em>' data type. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see java.io.InputStream
	 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getInputStream()
	 * @generated
	 */
	int INPUT_STREAM = 6;

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.ui.scripts.repository.IScript <em>Script</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for class '<em>Script</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript
	 * @generated
	 */
	EClass getScript();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.ui.scripts.repository.IScript#getTimestamp <em>Timestamp</em>}'. <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Timestamp</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getTimestamp()
	 * @see #getScript()
	 * @generated
	 */
	EAttribute getScript_Timestamp();

	/**
	 * Returns the meta object for the container reference '{@link org.eclipse.ease.ui.scripts.repository.IScript#getEntry <em>Entry</em>}'. <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the container reference '<em>Entry</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getEntry()
	 * @see #getScript()
	 * @generated
	 */
	EReference getScript_Entry();

	/**
	 * Returns the meta object for the map '{@link org.eclipse.ease.ui.scripts.repository.IScript#getScriptKeywords <em>Script Keywords</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the map '<em>Script Keywords</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getScriptKeywords()
	 * @see #getScript()
	 * @generated
	 */
	EReference getScript_ScriptKeywords();

	/**
	 * Returns the meta object for the map '{@link org.eclipse.ease.ui.scripts.repository.IScript#getUserKeywords <em>User Keywords</em>}'. <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the map '<em>User Keywords</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getUserKeywords()
	 * @see #getScript()
	 * @generated
	 */
	EReference getScript_UserKeywords();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.ui.scripts.repository.IScript#run() <em>Run</em>}' operation. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @return the meta object for the '<em>Run</em>' operation.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#run()
	 * @generated
	 */
	EOperation getScript__Run();

	/**
	 * Returns the meta object for the ' {@link org.eclipse.ease.ui.scripts.repository.IScript#getName() <em>Get Name</em>}' operation. <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * 
	 * @return the meta object for the '<em>Get Name</em>' operation.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getName()
	 * @generated
	 */
	EOperation getScript__GetName();

	/**
	 * Returns the meta object for the ' {@link org.eclipse.ease.ui.scripts.repository.IScript#getPath() <em>Get Path</em>}' operation. <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * 
	 * @return the meta object for the '<em>Get Path</em>' operation.
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#getPath()
	 * @generated
	 */
	EOperation getScript__GetPath();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation <em>Raw Location</em>}'. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @return the meta object for class '<em>Raw Location</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation
	 * @generated
	 */
	EClass getRawLocation();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#getLocation <em>Location</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Location</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation#getLocation()
	 * @see #getRawLocation()
	 * @generated
	 */
	EAttribute getRawLocation_Location();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#isUpdatePending <em>Update Pending</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Update Pending</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation#isUpdatePending()
	 * @see #getRawLocation()
	 * @generated
	 */
	EAttribute getRawLocation_UpdatePending();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#getResource() <em>Get Resource</em>}' operation. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the '<em>Get Resource</em>' operation.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation#getResource()
	 * @generated
	 */
	EOperation getRawLocation__GetResource();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.ui.scripts.repository.IRawLocation#getInputStream() <em>Get Input Stream</em>}' operation. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the '<em>Get Input Stream</em>' operation.
	 * @see org.eclipse.ease.ui.scripts.repository.IRawLocation#getInputStream()
	 * @generated
	 */
	EOperation getRawLocation__GetInputStream();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.ui.scripts.repository.IStorage <em>Storage</em>}'. <!-- begin-user-doc --> <!-- end-user-doc
	 * -->
	 * 
	 * @return the meta object for class '<em>Storage</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IStorage
	 * @generated
	 */
	EClass getStorage();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.ui.scripts.repository.IStorage#getEntries <em>Entries</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the containment reference list '<em>Entries</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IStorage#getEntries()
	 * @see #getStorage()
	 * @generated
	 */
	EReference getStorage_Entries();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation <em>Script Location</em>}'. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * 
	 * @return the meta object for class '<em>Script Location</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation
	 * @generated
	 */
	EClass getScriptLocation();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isRecursive <em>Recursive</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Recursive</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation#isRecursive()
	 * @see #getScriptLocation()
	 * @generated
	 */
	EAttribute getScriptLocation_Recursive();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#isDefault <em>Default</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Default</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation#isDefault()
	 * @see #getScriptLocation()
	 * @generated
	 */
	EAttribute getScriptLocation_Default();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#getScripts <em>Scripts</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the containment reference list '<em>Scripts</em>'.
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation#getScripts()
	 * @see #getScriptLocation()
	 * @generated
	 */
	EReference getScriptLocation_Scripts();

	/**
	 * Returns the meta object for class '{@link java.util.Map.Entry <em>Keyword Map</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for class '<em>Keyword Map</em>'.
	 * @see java.util.Map.Entry
	 * @model keyDataType="org.eclipse.emf.ecore.EString" keyRequired="true" valueDataType="org.eclipse.emf.ecore.EString" valueRequired="true"
	 * @generated
	 */
	EClass getKeywordMap();

	/**
	 * Returns the meta object for the attribute '{@link java.util.Map.Entry <em>Key</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Key</em>'.
	 * @see java.util.Map.Entry
	 * @see #getKeywordMap()
	 * @generated
	 */
	EAttribute getKeywordMap_Key();

	/**
	 * Returns the meta object for the attribute '{@link java.util.Map.Entry <em>Value</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Value</em>'.
	 * @see java.util.Map.Entry
	 * @see #getKeywordMap()
	 * @generated
	 */
	EAttribute getKeywordMap_Value();

	/**
	 * Returns the meta object for data type ' {@link org.eclipse.core.runtime.IPath <em>Path</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for data type '<em>Path</em>'.
	 * @see org.eclipse.core.runtime.IPath
	 * @model instanceClass="org.eclipse.core.runtime.IPath"
	 * @generated
	 */
	EDataType getPath();

	/**
	 * Returns the meta object for data type '{@link java.io.InputStream <em>Input Stream</em>}'. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for data type '<em>Input Stream</em>'.
	 * @see java.io.InputStream
	 * @model instanceClass="java.io.InputStream"
	 * @generated
	 */
	EDataType getInputStream();

	/**
	 * Returns the factory that creates the instances of the model. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	IRepositoryFactory getRepositoryFactory();

	/**
	 * <!-- begin-user-doc --> Defines literals for the meta objects that represent
	 * <ul>
	 * <li>each class,</li>
	 * <li>each feature of each class,</li>
	 * <li>each operation of each class,</li>
	 * <li>each enum,</li>
	 * <li>and each data type</li>
	 * </ul>
	 * <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the ' {@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl <em>Script</em>}' class. <!-- begin-user-doc --> <!--
		 * end-user-doc -->
		 * 
		 * @see org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getScript()
		 * @generated
		 */
		EClass SCRIPT = eINSTANCE.getScript();

		/**
		 * The meta object literal for the '<em><b>Timestamp</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute SCRIPT__TIMESTAMP = eINSTANCE.getScript_Timestamp();

		/**
		 * The meta object literal for the '<em><b>Entry</b></em>' container reference feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EReference SCRIPT__ENTRY = eINSTANCE.getScript_Entry();

		/**
		 * The meta object literal for the '<em><b>Script Keywords</b></em>' map feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EReference SCRIPT__SCRIPT_KEYWORDS = eINSTANCE.getScript_ScriptKeywords();

		/**
		 * The meta object literal for the '<em><b>User Keywords</b></em>' map feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EReference SCRIPT__USER_KEYWORDS = eINSTANCE.getScript_UserKeywords();

		/**
		 * The meta object literal for the '<em><b>Run</b></em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EOperation SCRIPT___RUN = eINSTANCE.getScript__Run();

		/**
		 * The meta object literal for the '<em><b>Get Name</b></em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EOperation SCRIPT___GET_NAME = eINSTANCE.getScript__GetName();

		/**
		 * The meta object literal for the '<em><b>Get Path</b></em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EOperation SCRIPT___GET_PATH = eINSTANCE.getScript__GetPath();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl <em>Raw Location</em>}' class. <!--
		 * begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getRawLocation()
		 * @generated
		 */
		EClass RAW_LOCATION = eINSTANCE.getRawLocation();

		/**
		 * The meta object literal for the '<em><b>Location</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute RAW_LOCATION__LOCATION = eINSTANCE.getRawLocation_Location();

		/**
		 * The meta object literal for the '<em><b>Update Pending</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute RAW_LOCATION__UPDATE_PENDING = eINSTANCE.getRawLocation_UpdatePending();

		/**
		 * The meta object literal for the '<em><b>Get Resource</b></em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EOperation RAW_LOCATION___GET_RESOURCE = eINSTANCE.getRawLocation__GetResource();

		/**
		 * The meta object literal for the '<em><b>Get Input Stream</b></em>' operation. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EOperation RAW_LOCATION___GET_INPUT_STREAM = eINSTANCE.getRawLocation__GetInputStream();

		/**
		 * The meta object literal for the ' {@link org.eclipse.ease.ui.scripts.repository.impl.StorageImpl <em>Storage</em>}' class. <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.ease.ui.scripts.repository.impl.StorageImpl
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getStorage()
		 * @generated
		 */
		EClass STORAGE = eINSTANCE.getStorage();

		/**
		 * The meta object literal for the '<em><b>Entries</b></em>' containment reference list feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EReference STORAGE__ENTRIES = eINSTANCE.getStorage_Entries();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptLocationImpl <em>Script Location</em>}' class. <!--
		 * begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.ease.ui.scripts.repository.impl.ScriptLocationImpl
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getScriptLocation()
		 * @generated
		 */
		EClass SCRIPT_LOCATION = eINSTANCE.getScriptLocation();

		/**
		 * The meta object literal for the '<em><b>Recursive</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute SCRIPT_LOCATION__RECURSIVE = eINSTANCE.getScriptLocation_Recursive();

		/**
		 * The meta object literal for the '<em><b>Default</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute SCRIPT_LOCATION__DEFAULT = eINSTANCE.getScriptLocation_Default();

		/**
		 * The meta object literal for the '<em><b>Scripts</b></em>' containment reference list feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EReference SCRIPT_LOCATION__SCRIPTS = eINSTANCE.getScriptLocation_Scripts();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.ui.scripts.repository.impl.KeywordMapImpl <em>Keyword Map</em>}' class. <!-- begin-user-doc
		 * --> <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.ease.ui.scripts.repository.impl.KeywordMapImpl
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getKeywordMap()
		 * @generated
		 */
		EClass KEYWORD_MAP = eINSTANCE.getKeywordMap();

		/**
		 * The meta object literal for the '<em><b>Key</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute KEYWORD_MAP__KEY = eINSTANCE.getKeywordMap_Key();

		/**
		 * The meta object literal for the '<em><b>Value</b></em>' attribute feature. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @generated
		 */
		EAttribute KEYWORD_MAP__VALUE = eINSTANCE.getKeywordMap_Value();

		/**
		 * The meta object literal for the '<em>Path</em>' data type. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.core.runtime.IPath
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getPath()
		 * @generated
		 */
		EDataType PATH = eINSTANCE.getPath();

		/**
		 * The meta object literal for the '<em>Input Stream</em>' data type. <!-- begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @see java.io.InputStream
		 * @see org.eclipse.ease.ui.scripts.repository.impl.RepositoryPackageImpl#getInputStream()
		 * @generated
		 */
		EDataType INPUT_STREAM = eINSTANCE.getInputStream();

	}

} // IRepositoryPackage
