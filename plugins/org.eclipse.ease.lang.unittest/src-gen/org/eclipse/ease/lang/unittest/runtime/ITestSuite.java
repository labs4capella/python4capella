/**
 */
package org.eclipse.ease.lang.unittest.runtime;

import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Test Suite</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getActiveTests <em>Active Tests</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getDefinition <em>Definition</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getMasterEngine <em>Master Engine</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestSuite()
 * @model
 * @generated
 */
public interface ITestSuite extends ITestContainer {

	/**
	 * Returns the value of the '<em><b>Active Tests</b></em>' reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.runtime.ITestEntity}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Active Tests</em>' reference list isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Active Tests</em>' reference list.
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestSuite_ActiveTests()
	 * @model
	 * @generated
	 */
	EList<ITestEntity> getActiveTests();

	/**
	 * Returns the value of the '<em><b>Definition</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Definition</em>' reference isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Definition</em>' reference.
	 * @see #setDefinition(ITestSuiteDefinition)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestSuite_Definition()
	 * @model
	 * @generated
	 */
	ITestSuiteDefinition getDefinition();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getDefinition <em>Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Definition</em>' reference.
	 * @see #getDefinition()
	 * @generated
	 */
	void setDefinition(ITestSuiteDefinition value);

	/**
	 * Returns the value of the '<em><b>Master Engine</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Master Engine</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Master Engine</em>' attribute.
	 * @see #setMasterEngine(IScriptEngine)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestSuite_MasterEngine()
	 * @model dataType="org.eclipse.ease.lang.unittest.runtime.ScriptEngine" transient="true"
	 * @generated
	 */
	IScriptEngine getMasterEngine();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getMasterEngine <em>Master Engine</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Master Engine</em>' attribute.
	 * @see #getMasterEngine()
	 * @generated
	 */
	void setMasterEngine(IScriptEngine value);
} // ITestSuite
