/**
 */
package org.eclipse.ease.lang.unittest.runtime;

import java.util.List;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc --> A representation of the model object '<em><b>Test Container</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildren <em>Children</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getResource <em>Resource</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestContainer()
 * @model abstract="true"
 * @generated
 */
public interface ITestContainer extends ITestEntity {
	/**
	 * Returns the value of the '<em><b>Children</b></em>' containment reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.runtime.ITestEntity}.
	 * It is bidirectional and its opposite is '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent <em>Parent</em>}'.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Children</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Children</em>' containment reference list.
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestContainer_Children()
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent
	 * @model opposite="parent" containment="true"
	 * @generated
	 */
	EList<ITestEntity> getChildren();

	/**
	 * Returns the value of the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Resource</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Resource</em>' attribute.
	 * @see #setResource(Object)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestContainer_Resource()
	 * @model transient="true"
	 * @generated
	 */
	@Override
	Object getResource();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getResource <em>Resource</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Resource</em>' attribute.
	 * @see #getResource()
	 * @generated
	 */
	void setResource(Object value);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	ITest getTest(String name);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	EList<ITestContainer> getChildContainers();

	/**
	 * @generated NOT
	 */
	List<ITestEntity> getCopyOfChildren();
} // ITestContainer
