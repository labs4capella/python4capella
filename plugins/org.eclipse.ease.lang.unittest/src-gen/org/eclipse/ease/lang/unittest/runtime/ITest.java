/**
 */
package org.eclipse.ease.lang.unittest.runtime;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Test</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITest#getDurationLimit <em>Duration Limit</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTest()
 * @model
 * @generated
 */
public interface ITest extends ITestEntity, IStackTraceContainer {
	/**
	 * Returns the value of the '<em><b>Duration Limit</b></em>' attribute.
	 * The default value is <code>"-1"</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Duration Limit</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Duration Limit</em>' attribute.
	 * @see #setDurationLimit(long)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTest_DurationLimit()
	 * @model default="-1"
	 * @generated
	 */
	long getDurationLimit();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITest#getDurationLimit <em>Duration Limit</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Duration Limit</em>' attribute.
	 * @see #getDurationLimit()
	 * @generated
	 */
	void setDurationLimit(long value);

} // ITest
