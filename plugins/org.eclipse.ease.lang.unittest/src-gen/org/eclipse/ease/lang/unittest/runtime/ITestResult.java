/**
 */
package org.eclipse.ease.lang.unittest.runtime;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Test Result</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getStatus <em>Status</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getMessage <em>Message</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestResult()
 * @model
 * @generated
 */
public interface ITestResult extends IStackTraceContainer {
	/**
	 * Returns the value of the '<em><b>Status</b></em>' attribute.
	 * The literals are from the enumeration {@link org.eclipse.ease.lang.unittest.runtime.TestStatus}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Status</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Status</em>' attribute.
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @see #setStatus(TestStatus)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestResult_Status()
	 * @model
	 * @generated
	 */
	TestStatus getStatus();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getStatus <em>Status</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Status</em>' attribute.
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @see #getStatus()
	 * @generated
	 */
	void setStatus(TestStatus value);

	/**
	 * Returns the value of the '<em><b>Message</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Message</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Message</em>' attribute.
	 * @see #setMessage(String)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestResult_Message()
	 * @model
	 * @generated
	 */
	String getMessage();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getMessage <em>Message</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Message</em>' attribute.
	 * @see #getMessage()
	 * @generated
	 */
	void setMessage(String value);

} // ITestResult
