/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.definition.IDefinitionPackage;
import org.eclipse.ease.lang.unittest.definition.impl.DefinitionPackage;
import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.ease.lang.unittest.runtime.IMetadata;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestClass;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestFile;
import org.eclipse.ease.lang.unittest.runtime.ITestFolder;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
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
public class RuntimePackage extends EPackageImpl implements IRuntimePackage {
	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testEntityEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testContainerEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testSuiteEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testFolderEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testClassEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testResultEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EClass testFileEClass = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	private EClass stackTraceContainerEClass = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	private EClass metadataEClass = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EEnum testStatusEEnum = null;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private EDataType scriptEngineEDataType = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	private EDataType throwableEDataType = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	private EDataType scriptStackTraceEDataType = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	private EDataType testExecutionStrategyEDataType = null;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
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
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#eNS_URI
	 * @see #init()
	 * @generated
	 */
	private RuntimePackage() {
		super(eNS_URI, IRuntimeFactory.eINSTANCE);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private static boolean isInited = false;

	/**
	 * Creates, registers, and initializes the <b>Package</b> for this model, and for any others upon which it depends.
	 *
	 * <p>This method is used to initialize {@link IRuntimePackage#eINSTANCE} when that field is accessed.
	 * Clients should not invoke it directly. Instead, they should simply access that field to obtain the package.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #eNS_URI
	 * @see #createPackageContents()
	 * @see #initializePackageContents()
	 * @generated
	 */
	public static IRuntimePackage init() {
		if (isInited) return (IRuntimePackage)EPackage.Registry.INSTANCE.getEPackage(IRuntimePackage.eNS_URI);

		// Obtain or create and register package
		Object registeredRuntimePackage = EPackage.Registry.INSTANCE.get(eNS_URI);
		RuntimePackage theRuntimePackage = registeredRuntimePackage instanceof RuntimePackage ? (RuntimePackage)registeredRuntimePackage : new RuntimePackage();

		isInited = true;

		// Obtain or create and register interdependencies
		Object registeredPackage = EPackage.Registry.INSTANCE.getEPackage(IDefinitionPackage.eNS_URI);
		DefinitionPackage theDefinitionPackage = (DefinitionPackage)(registeredPackage instanceof DefinitionPackage ? registeredPackage : IDefinitionPackage.eINSTANCE);

		// Create package meta-data objects
		theRuntimePackage.createPackageContents();
		theDefinitionPackage.createPackageContents();

		// Initialize created meta-data
		theRuntimePackage.initializePackageContents();
		theDefinitionPackage.initializePackageContents();

		// Mark meta-data to indicate it can't be changed
		theRuntimePackage.freeze();

		// Update the registry and return the package
		EPackage.Registry.INSTANCE.put(IRuntimePackage.eNS_URI, theRuntimePackage);
		return theRuntimePackage;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestEntity() {
		return testEntityEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_Description() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_Name() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_EntityStatus() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_EndTimestamp() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(3);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_StartTimestamp() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(4);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestEntity_Parent() {
		return (EReference)testEntityEClass.getEStructuralFeatures().get(5);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestEntity_Metadata() {
		return (EReference)testEntityEClass.getEStructuralFeatures().get(6);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_Duration() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(7);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestEntity_Results() {
		return (EReference)testEntityEClass.getEStructuralFeatures().get(8);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_EstimatedDuration() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(9);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestEntity_Terminated() {
		return (EAttribute)testEntityEClass.getEStructuralFeatures().get(10);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetStatus() {
		return testEntityEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetRoot() {
		return testEntityEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__HasError() {
		return testEntityEClass.getEOperations().get(2);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetTestSuite() {
		return testEntityEClass.getEOperations().get(3);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetResource() {
		return testEntityEClass.getEOperations().get(4);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__Reset() {
		return testEntityEClass.getEOperations().get(5);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__Run__ITestExecutionStrategy() {
		return testEntityEClass.getEOperations().get(6);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetWorstResult() {
		return testEntityEClass.getEOperations().get(7);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__AddError__String_ScriptStackTrace() {
		return testEntityEClass.getEOperations().get(8);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetResults__TestStatus() {
		return testEntityEClass.getEOperations().get(9);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__GetFullPath() {
		return testEntityEClass.getEOperations().get(10);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__SetDisabled__String() {
		return testEntityEClass.getEOperations().get(11);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestEntity__IsDisabled() {
		return testEntityEClass.getEOperations().get(12);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestContainer() {
		return testContainerEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestContainer_Children() {
		return (EReference)testContainerEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestContainer_Resource() {
		return (EAttribute)testContainerEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestContainer__GetTest__String() {
		return testContainerEClass.getEOperations().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EOperation getTestContainer__GetChildContainers() {
		return testContainerEClass.getEOperations().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTest() {
		return testEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTest_DurationLimit() {
		return (EAttribute)testEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestSuite() {
		return testSuiteEClass;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestSuite_ActiveTests() {
		return (EReference)testSuiteEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EReference getTestSuite_Definition() {
		return (EReference)testSuiteEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestSuite_MasterEngine() {
		return (EAttribute)testSuiteEClass.getEStructuralFeatures().get(2);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestFolder() {
		return testFolderEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestClass() {
		return testClassEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestResult() {
		return testResultEClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestResult_Status() {
		return (EAttribute)testResultEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestResult_Message() {
		return (EAttribute)testResultEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getTestFile() {
		return testFileEClass;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getTestFile_InsertionOrder() {
		return (EAttribute)testFileEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getStackTraceContainer() {
		return stackTraceContainerEClass;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getStackTraceContainer_StackTrace() {
		return (EAttribute)stackTraceContainerEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EClass getMetadata() {
		return metadataEClass;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getMetadata_Key() {
		return (EAttribute)metadataEClass.getEStructuralFeatures().get(0);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EAttribute getMetadata_Value() {
		return (EAttribute)metadataEClass.getEStructuralFeatures().get(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EEnum getTestStatus() {
		return testStatusEEnum;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EDataType getScriptEngine() {
		return scriptEngineEDataType;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EDataType getThrowable() {
		return throwableEDataType;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EDataType getScriptStackTrace() {
		return scriptStackTraceEDataType;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EDataType getTestExecutionStrategy() {
		return testExecutionStrategyEDataType;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
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
	public IRuntimeFactory getRuntimeFactory() {
		return (IRuntimeFactory)getEFactoryInstance();
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
		testEntityEClass = createEClass(TEST_ENTITY);
		createEAttribute(testEntityEClass, TEST_ENTITY__DESCRIPTION);
		createEAttribute(testEntityEClass, TEST_ENTITY__NAME);
		createEAttribute(testEntityEClass, TEST_ENTITY__ENTITY_STATUS);
		createEAttribute(testEntityEClass, TEST_ENTITY__END_TIMESTAMP);
		createEAttribute(testEntityEClass, TEST_ENTITY__START_TIMESTAMP);
		createEReference(testEntityEClass, TEST_ENTITY__PARENT);
		createEReference(testEntityEClass, TEST_ENTITY__METADATA);
		createEAttribute(testEntityEClass, TEST_ENTITY__DURATION);
		createEReference(testEntityEClass, TEST_ENTITY__RESULTS);
		createEAttribute(testEntityEClass, TEST_ENTITY__ESTIMATED_DURATION);
		createEAttribute(testEntityEClass, TEST_ENTITY__TERMINATED);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_STATUS);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_ROOT);
		createEOperation(testEntityEClass, TEST_ENTITY___HAS_ERROR);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_TEST_SUITE);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_RESOURCE);
		createEOperation(testEntityEClass, TEST_ENTITY___RESET);
		createEOperation(testEntityEClass, TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_WORST_RESULT);
		createEOperation(testEntityEClass, TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_RESULTS__TESTSTATUS);
		createEOperation(testEntityEClass, TEST_ENTITY___GET_FULL_PATH);
		createEOperation(testEntityEClass, TEST_ENTITY___SET_DISABLED__STRING);
		createEOperation(testEntityEClass, TEST_ENTITY___IS_DISABLED);

		testContainerEClass = createEClass(TEST_CONTAINER);
		createEReference(testContainerEClass, TEST_CONTAINER__CHILDREN);
		createEAttribute(testContainerEClass, TEST_CONTAINER__RESOURCE);
		createEOperation(testContainerEClass, TEST_CONTAINER___GET_TEST__STRING);
		createEOperation(testContainerEClass, TEST_CONTAINER___GET_CHILD_CONTAINERS);

		testEClass = createEClass(TEST);
		createEAttribute(testEClass, TEST__DURATION_LIMIT);

		testSuiteEClass = createEClass(TEST_SUITE);
		createEReference(testSuiteEClass, TEST_SUITE__ACTIVE_TESTS);
		createEReference(testSuiteEClass, TEST_SUITE__DEFINITION);
		createEAttribute(testSuiteEClass, TEST_SUITE__MASTER_ENGINE);

		testFolderEClass = createEClass(TEST_FOLDER);

		testClassEClass = createEClass(TEST_CLASS);

		testResultEClass = createEClass(TEST_RESULT);
		createEAttribute(testResultEClass, TEST_RESULT__STATUS);
		createEAttribute(testResultEClass, TEST_RESULT__MESSAGE);

		testFileEClass = createEClass(TEST_FILE);
		createEAttribute(testFileEClass, TEST_FILE__INSERTION_ORDER);

		stackTraceContainerEClass = createEClass(STACK_TRACE_CONTAINER);
		createEAttribute(stackTraceContainerEClass, STACK_TRACE_CONTAINER__STACK_TRACE);

		metadataEClass = createEClass(METADATA);
		createEAttribute(metadataEClass, METADATA__KEY);
		createEAttribute(metadataEClass, METADATA__VALUE);

		// Create enums
		testStatusEEnum = createEEnum(TEST_STATUS);

		// Create data types
		scriptEngineEDataType = createEDataType(SCRIPT_ENGINE);
		throwableEDataType = createEDataType(THROWABLE);
		scriptStackTraceEDataType = createEDataType(SCRIPT_STACK_TRACE);
		testExecutionStrategyEDataType = createEDataType(TEST_EXECUTION_STRATEGY);
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

		// Obtain other dependent packages
		IDefinitionPackage theDefinitionPackage = (IDefinitionPackage)EPackage.Registry.INSTANCE.getEPackage(IDefinitionPackage.eNS_URI);

		// Create type parameters

		// Set bounds for type parameters

		// Add supertypes to classes
		testContainerEClass.getESuperTypes().add(this.getTestEntity());
		testEClass.getESuperTypes().add(this.getTestEntity());
		testEClass.getESuperTypes().add(this.getStackTraceContainer());
		testSuiteEClass.getESuperTypes().add(this.getTestContainer());
		testFolderEClass.getESuperTypes().add(this.getTestContainer());
		testClassEClass.getESuperTypes().add(this.getTestContainer());
		testClassEClass.getESuperTypes().add(this.getStackTraceContainer());
		testResultEClass.getESuperTypes().add(this.getStackTraceContainer());
		testFileEClass.getESuperTypes().add(this.getTestContainer());
		metadataEClass.getESuperTypes().add(this.getStackTraceContainer());

		// Initialize classes, features, and operations; add parameters
		initEClass(testEntityEClass, ITestEntity.class, "TestEntity", IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getTestEntity_Description(), ecorePackage.getEString(), "description", null, 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_Name(), ecorePackage.getEString(), "name", null, 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_EntityStatus(), this.getTestStatus(), "entityStatus", null, 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_EndTimestamp(), ecorePackage.getELong(), "endTimestamp", "0", 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_StartTimestamp(), ecorePackage.getELong(), "startTimestamp", "0", 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestEntity_Parent(), this.getTestContainer(), this.getTestContainer_Children(), "parent", null, 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestEntity_Metadata(), this.getMetadata(), null, "metadata", null, 0, -1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_Duration(), ecorePackage.getELong(), "duration", null, 0, 1, ITestEntity.class, IS_TRANSIENT, IS_VOLATILE, !IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, IS_DERIVED, IS_ORDERED);
		initEReference(getTestEntity_Results(), this.getTestResult(), null, "results", null, 0, -1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_EstimatedDuration(), ecorePackage.getELong(), "estimatedDuration", "-1", 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestEntity_Terminated(), ecorePackage.getEBoolean(), "terminated", null, 0, 1, ITestEntity.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEOperation(getTestEntity__GetStatus(), this.getTestStatus(), "getStatus", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__GetRoot(), this.getTestContainer(), "getRoot", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__HasError(), ecorePackage.getEBoolean(), "hasError", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__GetTestSuite(), this.getTestSuite(), "getTestSuite", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__GetResource(), ecorePackage.getEJavaObject(), "getResource", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__Reset(), null, "reset", 0, 1, IS_UNIQUE, IS_ORDERED);

		EOperation op = initEOperation(getTestEntity__Run__ITestExecutionStrategy(), null, "run", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, this.getTestExecutionStrategy(), "strategy", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__GetWorstResult(), this.getTestResult(), "getWorstResult", 0, 1, IS_UNIQUE, IS_ORDERED);

		op = initEOperation(getTestEntity__AddError__String_ScriptStackTrace(), this.getTestResult(), "addError", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, ecorePackage.getEString(), "message", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, this.getScriptStackTrace(), "stackTrace", 0, 1, IS_UNIQUE, IS_ORDERED);

		op = initEOperation(getTestEntity__GetResults__TestStatus(), this.getTestResult(), "getResults", 0, -1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, this.getTestStatus(), "status", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__GetFullPath(), this.getPath(), "getFullPath", 0, 1, IS_UNIQUE, IS_ORDERED);

		op = initEOperation(getTestEntity__SetDisabled__String(), null, "setDisabled", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, ecorePackage.getEString(), "message", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestEntity__IsDisabled(), ecorePackage.getEBoolean(), "isDisabled", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEClass(testContainerEClass, ITestContainer.class, "TestContainer", IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEReference(getTestContainer_Children(), this.getTestEntity(), this.getTestEntity_Parent(), "children", null, 0, -1, ITestContainer.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, IS_COMPOSITE, !IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestContainer_Resource(), ecorePackage.getEJavaObject(), "resource", null, 0, 1, ITestContainer.class, IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		op = initEOperation(getTestContainer__GetTest__String(), this.getTest(), "getTest", 0, 1, IS_UNIQUE, IS_ORDERED);
		addEParameter(op, ecorePackage.getEString(), "name", 0, 1, IS_UNIQUE, IS_ORDERED);

		initEOperation(getTestContainer__GetChildContainers(), this.getTestContainer(), "getChildContainers", 0, -1, IS_UNIQUE, IS_ORDERED);

		initEClass(testEClass, ITest.class, "Test", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getTest_DurationLimit(), ecorePackage.getELong(), "durationLimit", "-1", 0, 1, ITest.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(testSuiteEClass, ITestSuite.class, "TestSuite", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEReference(getTestSuite_ActiveTests(), this.getTestEntity(), null, "activeTests", null, 0, -1, ITestSuite.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_COMPOSITE, IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEReference(getTestSuite_Definition(), theDefinitionPackage.getTestSuiteDefinition(), null, "definition", null, 0, 1, ITestSuite.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_COMPOSITE, IS_RESOLVE_PROXIES, !IS_UNSETTABLE, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestSuite_MasterEngine(), this.getScriptEngine(), "masterEngine", null, 0, 1, ITestSuite.class, IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(testFolderEClass, ITestFolder.class, "TestFolder", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);

		initEClass(testClassEClass, ITestClass.class, "TestClass", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);

		initEClass(testResultEClass, ITestResult.class, "TestResult", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getTestResult_Status(), this.getTestStatus(), "status", null, 0, 1, ITestResult.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getTestResult_Message(), ecorePackage.getEString(), "message", null, 0, 1, ITestResult.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(testFileEClass, ITestFile.class, "TestFile", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getTestFile_InsertionOrder(), ecorePackage.getEInt(), "insertionOrder", null, 0, 1, ITestFile.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(stackTraceContainerEClass, IStackTraceContainer.class, "StackTraceContainer", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getStackTraceContainer_StackTrace(), this.getScriptStackTrace(), "stackTrace", null, 0, 1, IStackTraceContainer.class, IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		initEClass(metadataEClass, IMetadata.class, "Metadata", !IS_ABSTRACT, !IS_INTERFACE, IS_GENERATED_INSTANCE_CLASS);
		initEAttribute(getMetadata_Key(), ecorePackage.getEString(), "key", null, 0, 1, IMetadata.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);
		initEAttribute(getMetadata_Value(), ecorePackage.getEJavaObject(), "value", null, 0, 1, IMetadata.class, !IS_TRANSIENT, !IS_VOLATILE, IS_CHANGEABLE, !IS_UNSETTABLE, !IS_ID, IS_UNIQUE, !IS_DERIVED, IS_ORDERED);

		// Initialize enums and add enum literals
		initEEnum(testStatusEEnum, TestStatus.class, "TestStatus");
		addEEnumLiteral(testStatusEEnum, TestStatus.NOT_RUN);
		addEEnumLiteral(testStatusEEnum, TestStatus.FINISHED);
		addEEnumLiteral(testStatusEEnum, TestStatus.DISABLED);
		addEEnumLiteral(testStatusEEnum, TestStatus.PASS);
		addEEnumLiteral(testStatusEEnum, TestStatus.FAILURE);
		addEEnumLiteral(testStatusEEnum, TestStatus.ERROR);
		addEEnumLiteral(testStatusEEnum, TestStatus.RUNNING);

		// Initialize data types
		initEDataType(scriptEngineEDataType, IScriptEngine.class, "ScriptEngine", !IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);
		initEDataType(throwableEDataType, Throwable.class, "Throwable", !IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);
		initEDataType(scriptStackTraceEDataType, ScriptStackTrace.class, "ScriptStackTrace", !IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);
		initEDataType(testExecutionStrategyEDataType, ITestExecutionStrategy.class, "TestExecutionStrategy", !IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);
		initEDataType(pathEDataType, IPath.class, "Path", !IS_SERIALIZABLE, !IS_GENERATED_INSTANCE_CLASS);

		// Create resource
		createResource(eNS_URI);
	}

} // RuntimePackage
