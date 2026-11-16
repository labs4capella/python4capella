/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.lang.unittest.runtime.*;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestClass;
import org.eclipse.ease.lang.unittest.runtime.ITestFile;
import org.eclipse.ease.lang.unittest.runtime.ITestFolder;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.impl.EFactoryImpl;
import org.eclipse.emf.ecore.plugin.EcorePlugin;

/**
 * <!-- begin-user-doc --> An implementation of the model <b>Factory</b>. <!-- end-user-doc -->
 * @generated
 */
public class RuntimeFactory extends EFactoryImpl implements IRuntimeFactory {
	/**
	 * Creates the default factory implementation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public static IRuntimeFactory init() {
		try {
			IRuntimeFactory theRuntimeFactory = (IRuntimeFactory)EPackage.Registry.INSTANCE.getEFactory(IRuntimePackage.eNS_URI);
			if (theRuntimeFactory != null) {
				return theRuntimeFactory;
			}
		}
		catch (Exception exception) {
			EcorePlugin.INSTANCE.log(exception);
		}
		return new RuntimeFactory();
	}

	/**
	 * Creates an instance of the factory.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public RuntimeFactory() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EObject create(EClass eClass) {
		switch (eClass.getClassifierID()) {
			case IRuntimePackage.TEST: return createTest();
			case IRuntimePackage.TEST_SUITE: return createTestSuite();
			case IRuntimePackage.TEST_FOLDER: return createTestFolder();
			case IRuntimePackage.TEST_CLASS: return createTestClass();
			case IRuntimePackage.TEST_RESULT: return createTestResult();
			case IRuntimePackage.TEST_FILE: return createTestFile();
			case IRuntimePackage.STACK_TRACE_CONTAINER: return createStackTraceContainer();
			case IRuntimePackage.METADATA: return createMetadata();
			default:
				throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object createFromString(EDataType eDataType, String initialValue) {
		switch (eDataType.getClassifierID()) {
			case IRuntimePackage.TEST_STATUS:
				return createTestStatusFromString(eDataType, initialValue);
			default:
				throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String convertToString(EDataType eDataType, Object instanceValue) {
		switch (eDataType.getClassifierID()) {
			case IRuntimePackage.TEST_STATUS:
				return convertTestStatusToString(eDataType, instanceValue);
			default:
				throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITest createTest() {
		Test test = new Test();
		return test;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestSuite createTestSuite() {
		TestSuite testSuite = new TestSuite();
		return testSuite;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestFolder createTestFolder() {
		TestFolder testFolder = new TestFolder();
		return testFolder;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestClass createTestClass() {
		TestClass testClass = new TestClass();
		return testClass;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestResult createTestResult() {
		TestResult testResult = new TestResult();
		return testResult;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestFile createTestFile() {
		TestFile testFile = new TestFile();
		return testFile;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IStackTraceContainer createStackTraceContainer() {
		StackTraceContainer stackTraceContainer = new StackTraceContainer();
		return stackTraceContainer;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IMetadata createMetadata() {
		Metadata metadata = new Metadata();
		return metadata;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public TestStatus createTestStatusFromString(EDataType eDataType, String initialValue) {
		TestStatus result = TestStatus.get(initialValue);
		if (result == null) throw new IllegalArgumentException("The value '" + initialValue + "' is not a valid enumerator of '" + eDataType.getName() + "'");
		return result;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public String convertTestStatusToString(EDataType eDataType, Object instanceValue) {
		return instanceValue == null ? null : instanceValue.toString();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	public IScriptEngine createScriptEngineFromString(EDataType eDataType, String initialValue) {
		if ((initialValue == null) || (initialValue.isEmpty()))
			return null;

		throw new RuntimeException("Script engine lookup not implemented");
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IRuntimePackage getRuntimePackage() {
		return (IRuntimePackage)getEPackage();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @deprecated
	 * @generated
	 */
	@Deprecated
	public static IRuntimePackage getPackage() {
		return IRuntimePackage.eINSTANCE;
	}

} // RuntimeFactory
