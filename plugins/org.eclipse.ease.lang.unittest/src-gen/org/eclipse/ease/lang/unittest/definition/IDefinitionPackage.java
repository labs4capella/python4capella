/**
 */
package org.eclipse.ease.lang.unittest.definition;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EEnum;
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
 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionFactory
 * @model kind="package"
 *        extendedMetaData="qualified='false'"
 * @generated
 */
public interface IDefinitionPackage extends EPackage {
	/**
	 * The package name.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	String eNAME = "definition";

	/**
	 * The package namespace URI.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_URI = "http://eclipse.org/ease/unittest/testsuite/1.0";

	/**
	 * The package namespace name.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_PREFIX = "definition";

	/**
	 * The singleton instance of the package.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	IDefinitionPackage eINSTANCE = org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage.init();

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition <em>Test Suite Definition</em>}' class. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getTestSuiteDefinition()
	 * @generated
	 */
	int TEST_SUITE_DEFINITION = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__NAME = 0;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__DESCRIPTION = 1;

	/**
	 * The feature id for the '<em><b>Include Filter</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__INCLUDE_FILTER = 2;

	/**
	 * The feature id for the '<em><b>Exclude Filter</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__EXCLUDE_FILTER = 3;

	/**
	 * The feature id for the '<em><b>Disabled Resources</b></em>' attribute list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__DISABLED_RESOURCES = 4;

	/**
	 * The feature id for the '<em><b>Variables</b></em>' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__VARIABLES = 5;

	/**
	 * The feature id for the '<em><b>Custom Code</b></em>' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__CUSTOM_CODE = 6;

	/**
	 * The feature id for the '<em><b>Flags</b></em>' map.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__FLAGS = 7;

	/**
	 * The feature id for the '<em><b>Version</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__VERSION = 8;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION__RESOURCE = 9;

	/**
	 * The number of structural features of the '<em>Test Suite Definition</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION_FEATURE_COUNT = 10;

	/**
	 * The operation id for the '<em>Get Custom Code</em>' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION___GET_CUSTOM_CODE__STRING = 0;

	/**
	 * The operation id for the '<em>Get Variable</em>' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION___GET_VARIABLE__STRING = 1;

	/**
	 * The number of operations of the '<em>Test Suite Definition</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_DEFINITION_OPERATION_COUNT = 2;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.definition.impl.Variable <em>Variable</em>}' class.
	 * <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.definition.impl.Variable
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getVariable()
	 * @generated
	 */
	int VARIABLE = 1;

	/**
	 * The feature id for the '<em><b>Full Name</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE__FULL_NAME = 0;

	/**
	 * The feature id for the '<em><b>Content</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE__CONTENT = 1;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE__DESCRIPTION = 2;

	/**
	 * The feature id for the '<em><b>Enum Provider ID</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE__ENUM_PROVIDER_ID = 3;

	/**
	 * The number of structural features of the '<em>Variable</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE_FEATURE_COUNT = 4;

	/**
	 * The operation id for the '<em>Get Name</em>' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE___GET_NAME = 0;

	/**
	 * The operation id for the '<em>Get Path</em>' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE___GET_PATH = 1;

	/**
	 * The number of operations of the '<em>Variable</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VARIABLE_OPERATION_COUNT = 2;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.definition.impl.FlagToStringMap <em>Flag To String Map</em>}' class. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see org.eclipse.ease.lang.unittest.definition.impl.FlagToStringMap
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getFlagToStringMap()
	 * @generated
	 */
	int FLAG_TO_STRING_MAP = 2;

	/**
	 * The feature id for the '<em><b>Key</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int FLAG_TO_STRING_MAP__KEY = 0;

	/**
	 * The feature id for the '<em><b>Value</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int FLAG_TO_STRING_MAP__VALUE = 1;

	/**
	 * The number of structural features of the '<em>Flag To String Map</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int FLAG_TO_STRING_MAP_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Flag To String Map</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int FLAG_TO_STRING_MAP_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.definition.impl.Code <em>Code</em>}' class. <!-- begin-user-doc --> <!-- end-user-doc
	 * -->
	 * 
	 * @see org.eclipse.ease.lang.unittest.definition.impl.Code
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getCode()
	 * @generated
	 */
	int CODE = 3;

	/**
	 * The feature id for the '<em><b>Location</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CODE__LOCATION = 0;

	/**
	 * The feature id for the '<em><b>Content</b></em>' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CODE__CONTENT = 1;

	/**
	 * The number of structural features of the '<em>Code</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CODE_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Code</em>' class.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CODE_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.definition.Flag <em>Flag</em>}' enum.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.definition.Flag
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getFlag()
	 * @generated
	 */
	int FLAG = 4;

	/**
	 * The meta object id for the '<em>Path</em>' data type.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see org.eclipse.core.runtime.IPath
	 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getPath()
	 * @generated
	 */
	int PATH = 5;

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition <em>Test Suite Definition</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for class '<em>Test Suite Definition</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition
	 * @generated
	 */
	EClass getTestSuiteDefinition();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getName <em>Name</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getName()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_Name();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDescription <em>Description</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Description</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDescription()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_Description();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getIncludeFilter <em>Include Filter</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Include Filter</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getIncludeFilter()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_IncludeFilter();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getExcludeFilter <em>Exclude Filter</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Exclude Filter</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getExcludeFilter()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_ExcludeFilter();

	/**
	 * Returns the meta object for the attribute list '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDisabledResources <em>Disabled Resources</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute list '<em>Disabled Resources</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDisabledResources()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_DisabledResources();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVariables <em>Variables</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Variables</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVariables()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EReference getTestSuiteDefinition_Variables();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getCustomCode <em>Custom Code</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Custom Code</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getCustomCode()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EReference getTestSuiteDefinition_CustomCode();

	/**
	 * Returns the meta object for the map '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getFlags <em>Flags</em>}'.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @return the meta object for the map '<em>Flags</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getFlags()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EReference getTestSuiteDefinition_Flags();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVersion <em>Version</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Version</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVersion()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_Version();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getResource <em>Resource</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Resource</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getResource()
	 * @see #getTestSuiteDefinition()
	 * @generated
	 */
	EAttribute getTestSuiteDefinition_Resource();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getCustomCode(java.lang.String) <em>Get Custom Code</em>}' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Custom Code</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getCustomCode(java.lang.String)
	 * @generated
	 */
	EOperation getTestSuiteDefinition__GetCustomCode__String();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVariable(java.lang.String) <em>Get Variable</em>}' operation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Variable</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVariable(java.lang.String)
	 * @generated
	 */
	EOperation getTestSuiteDefinition__GetVariable__String();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.definition.IVariable <em>Variable</em>}'.
	 * <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * @return the meta object for class '<em>Variable</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable
	 * @generated
	 */
	EClass getVariable();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getFullName <em>Full Name</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Full Name</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getFullName()
	 * @see #getVariable()
	 * @generated
	 */
	EAttribute getVariable_FullName();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getContent <em>Content</em>}'.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Content</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getContent()
	 * @see #getVariable()
	 * @generated
	 */
	EAttribute getVariable_Content();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getDescription <em>Description</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Description</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getDescription()
	 * @see #getVariable()
	 * @generated
	 */
	EAttribute getVariable_Description();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID <em>Enum Provider ID</em>}'. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the meta object for the attribute '<em>Enum Provider ID</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID()
	 * @see #getVariable()
	 * @generated
	 */
	EAttribute getVariable_EnumProviderID();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getName() <em>Get Name</em>}' operation.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Name</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getName()
	 * @generated
	 */
	EOperation getVariable__GetName();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getPath() <em>Get Path</em>}' operation.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Path</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.definition.IVariable#getPath()
	 * @generated
	 */
	EOperation getVariable__GetPath();

	/**
	 * Returns the meta object for class '{@link java.util.Map.Entry <em>Flag To String Map</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for class '<em>Flag To String Map</em>'.
	 * @see java.util.Map.Entry
	 * @model keyDataType="org.eclipse.ease.lang.unittest.definition.Flag"
	 *        valueDataType="org.eclipse.emf.ecore.EString"
	 * @generated
	 */
	EClass getFlagToStringMap();

	/**
	 * Returns the meta object for the attribute '{@link java.util.Map.Entry <em>Key</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Key</em>'.
	 * @see java.util.Map.Entry
	 * @see #getFlagToStringMap()
	 * @generated
	 */
	EAttribute getFlagToStringMap_Key();

	/**
	 * Returns the meta object for the attribute '{@link java.util.Map.Entry <em>Value</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Value</em>'.
	 * @see java.util.Map.Entry
	 * @see #getFlagToStringMap()
	 * @generated
	 */
	EAttribute getFlagToStringMap_Value();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.definition.ICode <em>Code</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for class '<em>Code</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ICode
	 * @generated
	 */
	EClass getCode();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ICode#getLocation <em>Location</em>}'.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Location</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ICode#getLocation()
	 * @see #getCode()
	 * @generated
	 */
	EAttribute getCode_Location();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.definition.ICode#getContent <em>Content</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Content</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.ICode#getContent()
	 * @see #getCode()
	 * @generated
	 */
	EAttribute getCode_Content();

	/**
	 * Returns the meta object for enum '{@link org.eclipse.ease.lang.unittest.definition.Flag <em>Flag</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for enum '<em>Flag</em>'.
	 * @see org.eclipse.ease.lang.unittest.definition.Flag
	 * @generated
	 */
	EEnum getFlag();

	/**
	 * Returns the meta object for data type '{@link org.eclipse.core.runtime.IPath <em>Path</em>}'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Path</em>'.
	 * @see org.eclipse.core.runtime.IPath
	 * @model instanceClass="org.eclipse.core.runtime.IPath"
	 * @generated
	 */
	EDataType getPath();

	/**
	 * Returns the factory that creates the instances of the model.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	IDefinitionFactory getDefinitionFactory();

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
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition <em>Test Suite Definition</em>}' class.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getTestSuiteDefinition()
		 * @generated
		 */
		EClass TEST_SUITE_DEFINITION = eINSTANCE.getTestSuiteDefinition();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__NAME = eINSTANCE.getTestSuiteDefinition_Name();

		/**
		 * The meta object literal for the '<em><b>Description</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__DESCRIPTION = eINSTANCE.getTestSuiteDefinition_Description();

		/**
		 * The meta object literal for the '<em><b>Include Filter</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__INCLUDE_FILTER = eINSTANCE.getTestSuiteDefinition_IncludeFilter();

		/**
		 * The meta object literal for the '<em><b>Exclude Filter</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__EXCLUDE_FILTER = eINSTANCE.getTestSuiteDefinition_ExcludeFilter();

		/**
		 * The meta object literal for the '<em><b>Disabled Resources</b></em>' attribute list feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__DISABLED_RESOURCES = eINSTANCE.getTestSuiteDefinition_DisabledResources();

		/**
		 * The meta object literal for the '<em><b>Variables</b></em>' containment reference list feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_SUITE_DEFINITION__VARIABLES = eINSTANCE.getTestSuiteDefinition_Variables();

		/**
		 * The meta object literal for the '<em><b>Custom Code</b></em>' containment reference list feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_SUITE_DEFINITION__CUSTOM_CODE = eINSTANCE.getTestSuiteDefinition_CustomCode();

		/**
		 * The meta object literal for the '<em><b>Flags</b></em>' map feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_SUITE_DEFINITION__FLAGS = eINSTANCE.getTestSuiteDefinition_Flags();

		/**
		 * The meta object literal for the '<em><b>Version</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__VERSION = eINSTANCE.getTestSuiteDefinition_Version();

		/**
		 * The meta object literal for the '<em><b>Resource</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE_DEFINITION__RESOURCE = eINSTANCE.getTestSuiteDefinition_Resource();

		/**
		 * The meta object literal for the '<em><b>Get Custom Code</b></em>' operation.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_SUITE_DEFINITION___GET_CUSTOM_CODE__STRING = eINSTANCE.getTestSuiteDefinition__GetCustomCode__String();

		/**
		 * The meta object literal for the '<em><b>Get Variable</b></em>' operation.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_SUITE_DEFINITION___GET_VARIABLE__STRING = eINSTANCE.getTestSuiteDefinition__GetVariable__String();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.definition.impl.Variable <em>Variable</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.definition.impl.Variable
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getVariable()
		 * @generated
		 */
		EClass VARIABLE = eINSTANCE.getVariable();

		/**
		 * The meta object literal for the '<em><b>Full Name</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute VARIABLE__FULL_NAME = eINSTANCE.getVariable_FullName();

		/**
		 * The meta object literal for the '<em><b>Content</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute VARIABLE__CONTENT = eINSTANCE.getVariable_Content();

		/**
		 * The meta object literal for the '<em><b>Description</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute VARIABLE__DESCRIPTION = eINSTANCE.getVariable_Description();

		/**
		 * The meta object literal for the '<em><b>Enum Provider ID</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute VARIABLE__ENUM_PROVIDER_ID = eINSTANCE.getVariable_EnumProviderID();

		/**
		 * The meta object literal for the '<em><b>Get Name</b></em>' operation.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EOperation VARIABLE___GET_NAME = eINSTANCE.getVariable__GetName();

		/**
		 * The meta object literal for the '<em><b>Get Path</b></em>' operation.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EOperation VARIABLE___GET_PATH = eINSTANCE.getVariable__GetPath();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.definition.impl.FlagToStringMap <em>Flag To String Map</em>}' class. <!--
		 * begin-user-doc --> <!-- end-user-doc -->
		 * 
		 * @see org.eclipse.ease.lang.unittest.definition.impl.FlagToStringMap
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getFlagToStringMap()
		 * @generated
		 */
		EClass FLAG_TO_STRING_MAP = eINSTANCE.getFlagToStringMap();

		/**
		 * The meta object literal for the '<em><b>Key</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute FLAG_TO_STRING_MAP__KEY = eINSTANCE.getFlagToStringMap_Key();

		/**
		 * The meta object literal for the '<em><b>Value</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute FLAG_TO_STRING_MAP__VALUE = eINSTANCE.getFlagToStringMap_Value();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.definition.impl.Code <em>Code</em>}' class.
		 * <!-- begin-user-doc --> <!--
		 * end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.definition.impl.Code
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getCode()
		 * @generated
		 */
		EClass CODE = eINSTANCE.getCode();

		/**
		 * The meta object literal for the '<em><b>Location</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute CODE__LOCATION = eINSTANCE.getCode_Location();

		/**
		 * The meta object literal for the '<em><b>Content</b></em>' attribute feature.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute CODE__CONTENT = eINSTANCE.getCode_Content();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.definition.Flag <em>Flag</em>}' enum.
		 * <!-- begin-user-doc --> <!--
		 * end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.definition.Flag
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getFlag()
		 * @generated
		 */
		EEnum FLAG = eINSTANCE.getFlag();

		/**
		 * The meta object literal for the '<em>Path</em>' data type.
		 * <!-- begin-user-doc --> <!-- end-user-doc -->
		 * @see org.eclipse.core.runtime.IPath
		 * @see org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage#getPath()
		 * @generated
		 */
		EDataType PATH = eINSTANCE.getPath();

	}

} // IDefinitionPackage
