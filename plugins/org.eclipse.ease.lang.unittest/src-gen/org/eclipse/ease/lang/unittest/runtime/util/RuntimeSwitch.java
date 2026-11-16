/**
 */
package org.eclipse.ease.lang.unittest.runtime.util;

import org.eclipse.ease.lang.unittest.runtime.*;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;

import org.eclipse.emf.ecore.util.Switch;

/**
 * <!-- begin-user-doc -->
 * The <b>Switch</b> for the model's inheritance hierarchy.
 * It supports the call {@link #doSwitch(EObject) doSwitch(object)}
 * to invoke the <code>caseXXX</code> method for each class of the model,
 * starting with the actual class of the object
 * and proceeding up the inheritance hierarchy
 * until a non-null result is returned,
 * which is the result of the switch.
 * <!-- end-user-doc -->
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage
 * @generated
 */
public class RuntimeSwitch<T> extends Switch<T> {
	/**
	 * The cached model package
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected static IRuntimePackage modelPackage;

	/**
	 * Creates an instance of the switch.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public RuntimeSwitch() {
		if (modelPackage == null) {
			modelPackage = IRuntimePackage.eINSTANCE;
		}
	}

	/**
	 * Checks whether this is a switch for the given package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param ePackage the package in question.
	 * @return whether this is a switch for the given package.
	 * @generated
	 */
	@Override
	protected boolean isSwitchFor(EPackage ePackage) {
		return ePackage == modelPackage;
	}

	/**
	 * Calls <code>caseXXX</code> for each class of the model until one returns a non null result; it yields that result.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the first non-null result returned by a <code>caseXXX</code> call.
	 * @generated
	 */
	@Override
	protected T doSwitch(int classifierID, EObject theEObject) {
		switch (classifierID) {
			case IRuntimePackage.TEST_ENTITY: {
				ITestEntity testEntity = (ITestEntity)theEObject;
				T result = caseTestEntity(testEntity);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_CONTAINER: {
				ITestContainer testContainer = (ITestContainer)theEObject;
				T result = caseTestContainer(testContainer);
				if (result == null) result = caseTestEntity(testContainer);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST: {
				ITest test = (ITest)theEObject;
				T result = caseTest(test);
				if (result == null) result = caseTestEntity(test);
				if (result == null) result = caseStackTraceContainer(test);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_SUITE: {
				ITestSuite testSuite = (ITestSuite)theEObject;
				T result = caseTestSuite(testSuite);
				if (result == null) result = caseTestContainer(testSuite);
				if (result == null) result = caseTestEntity(testSuite);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_FOLDER: {
				ITestFolder testFolder = (ITestFolder)theEObject;
				T result = caseTestFolder(testFolder);
				if (result == null) result = caseTestContainer(testFolder);
				if (result == null) result = caseTestEntity(testFolder);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_CLASS: {
				ITestClass testClass = (ITestClass)theEObject;
				T result = caseTestClass(testClass);
				if (result == null) result = caseTestContainer(testClass);
				if (result == null) result = caseStackTraceContainer(testClass);
				if (result == null) result = caseTestEntity(testClass);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_RESULT: {
				ITestResult testResult = (ITestResult)theEObject;
				T result = caseTestResult(testResult);
				if (result == null) result = caseStackTraceContainer(testResult);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.TEST_FILE: {
				ITestFile testFile = (ITestFile)theEObject;
				T result = caseTestFile(testFile);
				if (result == null) result = caseTestContainer(testFile);
				if (result == null) result = caseTestEntity(testFile);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.STACK_TRACE_CONTAINER: {
				IStackTraceContainer stackTraceContainer = (IStackTraceContainer)theEObject;
				T result = caseStackTraceContainer(stackTraceContainer);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			case IRuntimePackage.METADATA: {
				IMetadata metadata = (IMetadata)theEObject;
				T result = caseMetadata(metadata);
				if (result == null) result = caseStackTraceContainer(metadata);
				if (result == null) result = defaultCase(theEObject);
				return result;
			}
			default: return defaultCase(theEObject);
		}
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Entity</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Entity</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestEntity(ITestEntity object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Container</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Container</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestContainer(ITestContainer object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTest(ITest object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Suite</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Suite</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestSuite(ITestSuite object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Folder</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Folder</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestFolder(ITestFolder object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Class</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Class</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestClass(ITestClass object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test Result</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test Result</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestResult(ITestResult object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Test File</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Test File</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseTestFile(ITestFile object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Stack Trace Container</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Stack Trace Container</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseStackTraceContainer(IStackTraceContainer object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>Metadata</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>Metadata</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject) doSwitch(EObject)
	 * @generated
	 */
	public T caseMetadata(IMetadata object) {
		return null;
	}

	/**
	 * Returns the result of interpreting the object as an instance of '<em>EObject</em>'.
	 * <!-- begin-user-doc -->
	 * This implementation returns null;
	 * returning a non-null result will terminate the switch, but this is the last case anyway.
	 * <!-- end-user-doc -->
	 * @param object the target of the switch.
	 * @return the result of interpreting the object as an instance of '<em>EObject</em>'.
	 * @see #doSwitch(org.eclipse.emf.ecore.EObject)
	 * @generated
	 */
	@Override
	public T defaultCase(EObject object) {
		return null;
	}

} //RuntimeSwitch
