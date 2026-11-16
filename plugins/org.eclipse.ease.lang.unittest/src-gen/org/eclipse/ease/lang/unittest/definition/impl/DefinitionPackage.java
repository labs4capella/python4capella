/**
 */
package org.eclipse.ease.lang.unittest.definition.impl;

import java.util.Map;

import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ICode;
import org.eclipse.ease.lang.unittest.definition.IDefinitionFactory;
import org.eclipse.ease.lang.unittest.definition.IDefinitionPackage;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.definition.IVariable;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage;
import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

import org.eclipse.emf.ecore.impl.EPackageImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model <b>Package</b>. <!-- end-user-doc -->
 * @generated
 */
public class DefinitionPackage extends EPackageImpl implements IDefinitionPackage {
	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testSuiteDefinitionEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass variableEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass flagToStringMapEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass codeEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EEnum flagEEnum = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EDataType pathEDataType = null;

	/**
	 * Creates an instance of the model <b>Package</b>, registered with
	 * {@link org.eclipse.emf.ecore.EPackage.Registry EPackage.Registry} by the package
	 * package URI value.
	 * <p>Note: the correct way to create the package is via the static
	 * factory method {@link #init init()}, which also performs
	 * initialization of the package, or returns the registered package,
	 * if one already exists.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see org.eclipse.emf.ecore.EPackage.Registry
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#eNS_URI
	 * @see #init()
	 * @generated
	 */
	private DefinitionPackage() {
		super(eNS_URI, IDefinitionFactory.eINSTANCE);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private static boolean isInited = false;

	/**
	 * Creates, registers, and initializes the <b>Package</b> for this model, and for any others upon which it depends.
	 *
	 * <p>This method is used to initialize {@link IDefinitionPackage#eINSTANCE} when that field is accessed.
	 * Clients should not invoke it directly. Instead, they should simply access that field to obtain the package.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #eNS_URI
	 * @see #createPackageContents()
	 * @see #initializePackageContents()
	 * @generated
	 */
	public static IDefinitionPackage init() {
		if (isInited) return (IDefinitionPackage)EPackage.Registry.INSTANCE.getEPackage(IDefinitionPackage.eNS_URI);

		// Obtain or create and register package
		Object registeredDefinitionPackage = EPackage.Registry.INSTANCE.get(eNS_URI);
		DefinitionPackage theDefinitionPackage = registeredDefinitionPackage instanceof DefinitionPackage ? (DefinitionPackage)registeredDefinitionPackage : new DefinitionPackage();

		isInited = true;

		// Obtain or create and register interdependencies
		Object registeredPackage = EPackage.Registry.INSTANCE.getEPackage(IRuntimePackage.eNS_URI);
		RuntimePackage theRuntimePackage = (RuntimePackage)(registeredPackage instanceof RuntimePackage ? registeredPackage : IRuntimePackage.eINSTANCE);

		// Create package meta-data objects
		theDefinitionPackage.createPackageContents();
		theRuntimePackage.createPackageContents();

		// Initialize created meta-data
		theDefinitionPackage.initializePackageContents();
		theRuntimePackage.initializePackageContents();

		// Mark meta-data to indicate it can't be changed
		theDefinitionPackage.freeze();

		// Update the registry and return the package
		EPackage.Registry.INSTANCE.put(IDefinitionPackage.eNS_URI, theDefinitionPackage);
		return theDefinitionPackage;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestSuiteDefinition() {
		return testSuiteDefinitionEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_Name() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_Description() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_IncludeFilter() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_ExcludeFilter() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(3);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_DisabledResources() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(4);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestSuiteDefinition_Variables() {
		return (EReference)testSuiteDefinitionEClass.getEStructuralFeatures().get(5);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestSuiteDefinition_CustomCode() {
		return (EReference)testSuiteDefinitionEClass.getEStructuralFeatures().get(6);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestSuiteDefinition_Flags() {
		return (EReference)testSuiteDefinitionEClass.getEStructuralFeatures().get(7);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_Version() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(8);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuiteDefinition_Resource() {
		return (EAttribute)testSuiteDefinitionEClass.getEStructuralFeatures().get(9);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestSuiteDefinition__GetCustomCode__String() {
		return testSuiteDefinitionEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestSuiteDefinition__GetVariable__String() {
		return testSuiteDefinitionEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getVariable() {
		return variableEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getVariable_FullName() {
		return (EAttribute)variableEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getVariable_Content() {
		return (EAttribute)variableEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getVariable_Description() {
		return (EAttribute)variableEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getVariable_EnumProviderID() {
		return (EAttribute)variableEClass.getEStructuralFeatures().get(3);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getVariable__GetName() {
		return variableEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getVariable__GetPath() {
		return variableEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getFlagToStringMap() {
		return flagToStringMapEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getFlagToStringMap_Key() {
		return (EAttribute)flagToStringMapEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getFlagToStringMap_Value() {
		return (EAttribute)flagToStringMapEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getCode() {
		return codeEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getCode_Location() {
		return (EAttribute)codeEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getCode_Content() {
		return (EAttribute)codeEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EEnum getFlag() {
		return flagEEnum;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EDataType getPath() {
		return pathEDataType;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IDefinitionFactory getDefinitionFactory() {
		return (IDefinitionFactory)getEFactoryInstance();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private boolean isCreated = false;

	/**
	 * Creates the meta-model objects for the package.  This method is
	 * guarded to have no affect on any invocation but its first.
	 * <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * @generated
	 */
	public void createPackageContents() {
		if (isCreated) return;
		isCreated = true;

		// Create classes and their features
		testSuiteDefinitionEClass = createEClass(TEST_SUITE_DEFINITION);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__NAME);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__DESCRIPTION);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__INCLUDE_FILTER);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__EXCLUDE_FILTER);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__DISABLED_RESOURCES);
		createEReference(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__VARIABLES);
		createEReference(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__CUSTOM_CODE);
		createEReference(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__FLAGS);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__VERSION);
		createEAttribute(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION__RESOURCE);
		createEOperation(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION___GET_CUSTOM_CODE__STRING);
		createEOperation(testSuiteDefinitionEClass, TEST_SUITE_DEFINITION___GET_VARIABLE__STRING);

		variableEClass = createEClass(VARIABLE);
		createEAttribute(variableEClass, VARIABLE__FULL_NAME);
		createEAttribute(variableEClass, VARIABLE__CONTENT);
		createEAttribute(variableEClass, VARIABLE__DESCRIPTION);
		createEAttribute(variableEClass, VARIABLE__ENUM_PROVIDER_ID);
		createEOperation(variableEClass, VARIABLE___GET_NAME);
		createEOperation(variableEClass, VARIABLE___GET_PATH);

		flagToStringMapEClass = createEClass(FLAG_TO_STRING_MAP);
		createEAttribute(flagToStringMapEClass, FLAG_TO_STRING_MAP__KEY);
		createEAttribute(flagToStringMapEClass, FLAG_TO_STRING_MAP__VALUE);

		codeEClass = createEClass(CODE);
		createEAttribute(codeEClass, CODE__LOCATION);
		createEAttribute(codeEClass, CODE__CONTENT);

		// Create enums
		flagEEnum = createEEnum(FLAG);

		// Create data types
		pathEDataType = createEDataType(PATH);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
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
		if (isInitialized) return;
		isInitialized = true;

		// Initialize package
		setName(eNAME);
		setNsPrefix(eNS_PREFIX);
		setNsURI(eNS_URI);

		// Create type parameters

		// Set bounds for type parameters

		// Add supertypes to classes

		// Initialize classes, features, and operations; add parameters
		initEClass(testSuiteDefinitionEClass, ITestSuiteDefinition.class, "TestSuiteDefinition", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getTestSuiteDefinition_Name(), ecorePackage.getEString(), "name", null, 0, 1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_Description(), ecorePackage.getEString(), "description", null, 0, 1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_IncludeFilter(), ecorePackage.getEString(), "includeFilter", "", 0, 1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_ExcludeFilter(), ecorePackage.getEString(), "excludeFilter", "", 0, 1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_DisabledResources(), this.getPath(), "disabledResources", null, 0, -1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestSuiteDefinition_Variables(), this.getVariable(), null, "variables", null, 0, -1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestSuiteDefinition_CustomCode(), this.getCode(), null, "customCode", null, 0, -1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestSuiteDefinition_Flags(), this.getFlagToStringMap(), null, "flags", null, 0, -1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_Version(), ecorePackage.getEString(), "version", "", 1, 1, ITestSuiteDefinition.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuiteDefinition_Resource(), ecorePackage.getEJavaObject(), "resource", null, 0, 1, ITestSuiteDefinition.class, IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		EOperation op = initEOperation(getTestSuiteDefinition__GetCustomCode__String(), this.getCode(), "getCustomCode", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, ecorePackage.getEString(), "location", 0, 1, IS_UNIQUE, IS_ORDERED);

		op = initEOperation(getTestSuiteDefinition__GetVariable__String(), this.getVariable(), "getVariable", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, ecorePackage.getEString(), "name", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEClass(variableEClass, IVariable.class, "Variable", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getVariable_FullName(), this.getPath(), "fullName", null, 0, 1, IVariable.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getVariable_Content(), ecorePackage.getEString(), "content", "", 0, 1, IVariable.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getVariable_Description(), ecorePackage.getEString(), "description", "", 0, 1, IVariable.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getVariable_EnumProviderID(), ecorePackage.getEString(), "enumProviderID", null, 0, 1, IVariable.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEOperation(getVariable__GetName(), ecorePackage.getEString(), "getName", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getVariable__GetPath(), this.getPath(), "getPath", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEClass(flagToStringMapEClass, Map.Entry.class, "FlagToStringMap", !IS_ABSTRACT, !IS_INTERFACE, !IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getFlagToStringMap_Key(), this.getFlag(), "key", null, 0, 1, Map.Entry.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getFlagToStringMap_Value(), ecorePackage.getEString(), "value", null, 0, 1, Map.Entry.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(codeEClass, ICode.class, "Code", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getCode_Location(), ecorePackage.getEString(), "location", null, 0, 1, ICode.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getCode_Content(), ecorePackage.getEString(), "content", "", 0, 1, ICode.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		// Initialize enums and add enum literals
		initEEnum(flagEEnum, Flag.class, "Flag");
		addEEnumLiteral(flagEEnum, Flag.UNDEFINED);
		addEEnumLiteral(flagEEnum, Flag.THREAD_COUNT);
		addEEnumLiteral(flagEEnum, Flag.PROMOTE_FAILURE_TO_ERROR);
		addEEnumLiteral(flagEEnum, Flag.STOP_SUITE_ON_ERROR);
		addEEnumLiteral(flagEEnum, Flag.RUN_TEARDOWN_ON_ERROR);
		addEEnumLiteral(flagEEnum, Flag.PREFERRED_ENGINE_ID);

		// Initialize data types
		initEDataType(pathEDataType, IPath.class, "Path", IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);

		// Create resource
		createResource(eNS_URI);

		// Create annotations
		// http:///org/eclipse/emf/ecore/util/ExtendedMetaData
		createExtendedMetaDataAnnotations();
	}

	/**
	 * Initializes the annotations for <b>http:///org/eclipse/emf/ecore/util/ExtendedMetaData</b>.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	protected void createExtendedMetaDataAnnotations() {
		String source = "http:///org/eclipse/emf/ecore/util/ExtendedMetaData";
		addAnnotation
		  (this,
		   source,
		   new String[] {
			   "qualified", "false"
		   });
		addAnnotation
		  (testSuiteDefinitionEClass,
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "TestSuite"
		   });
		addAnnotation
		  (getTestSuiteDefinition_Description(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "description"
		   });
		addAnnotation
		  (getTestSuiteDefinition_IncludeFilter(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "includeFilter"
		   });
		addAnnotation
		  (getTestSuiteDefinition_ExcludeFilter(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "excludeFilter"
		   });
		addAnnotation
		  (getTestSuiteDefinition_DisabledResources(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "disabledResource"
		   });
		addAnnotation
		  (getTestSuiteDefinition_Variables(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "variable",
			   "namespace", "##targetNamespace"
		   });
		addAnnotation
		  (getTestSuiteDefinition_Flags(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "flag",
			   "namespace", "##targetNamespace"
		   });
		addAnnotation
		  (getVariable_Content(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "content"
		   });
		addAnnotation
		  (getVariable_Description(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "description"
		   });
		addAnnotation
		  (getCode_Content(),
		   source,
		   new String[] {
			   "kind", "element",
			   "name", "content"
		   });
	}

} // DefinitionPackage
