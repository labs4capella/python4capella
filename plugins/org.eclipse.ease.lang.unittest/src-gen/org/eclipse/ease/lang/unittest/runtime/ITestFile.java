/**
 */
package org.eclipse.ease.lang.unittest.runtime;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Test File</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestFile#getInsertionOrder <em>Insertion Order</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestFile()
 * @model
 * @generated
 */
public interface ITestFile extends ITestContainer {

	/**
	 * Returns the value of the '<em><b>Insertion Order</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Insertion Order</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Insertion Order</em>' attribute.
	 * @see #setInsertionOrder(int)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestFile_InsertionOrder()
	 * @model
	 * @generated
	 */
	int getInsertionOrder();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestFile#getInsertionOrder <em>Insertion Order</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Insertion Order</em>' attribute.
	 * @see #getInsertionOrder()
	 * @generated
	 */
	void setInsertionOrder(int value);
} // ITestFile
