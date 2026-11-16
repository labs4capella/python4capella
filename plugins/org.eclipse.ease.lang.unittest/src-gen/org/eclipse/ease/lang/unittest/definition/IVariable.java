/**
 */
package org.eclipse.ease.lang.unittest.definition;

import org.eclipse.core.runtime.IPath;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> A representation of the model object '<em><b>Variable</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.IVariable#getFullName <em>Full Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.IVariable#getContent <em>Content</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.IVariable#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID <em>Enum Provider ID</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getVariable()
 * @model
 * @generated
 */
public interface IVariable extends EObject {
	/**
	 * Returns the value of the '<em><b>Full Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Full Name</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Full Name</em>' attribute.
	 * @see #setFullName(IPath)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getVariable_FullName()
	 * @model dataType="org.eclipse.ease.lang.unittest.definition.Path"
	 * @generated
	 */
	IPath getFullName();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getFullName <em>Full Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Full Name</em>' attribute.
	 * @see #getFullName()
	 * @generated
	 */
	void setFullName(IPath value);

	/**
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Name</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	String getName();

	/**
	 * Returns the value of the '<em><b>Content</b></em>' attribute.
	 * The default value is <code>""</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Content</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Content</em>' attribute.
	 * @see #setContent(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getVariable_Content()
	 * @model default=""
	 *        extendedMetaData="kind='element' name='content'"
	 * @generated
	 */
	String getContent();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getContent <em>Content</em>}' attribute.
	 * <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * @param value the new value of the '<em>Content</em>' attribute.
	 * @see #getContent()
	 * @generated
	 */
	void setContent(String value);

	/**
	 * Returns the value of the '<em><b>Description</b></em>' attribute.
	 * The default value is <code>""</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Description</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Description</em>' attribute.
	 * @see #setDescription(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getVariable_Description()
	 * @model default=""
	 *        extendedMetaData="kind='element' name='description'"
	 * @generated
	 */
	String getDescription();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getDescription <em>Description</em>}' attribute.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @param value the new value of the '<em>Description</em>' attribute.
	 * @see #getDescription()
	 * @generated
	 */
	void setDescription(String value);

	/**
	 * Returns the value of the '<em><b>Enum Provider ID</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Enum Provider ID</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Enum Provider ID</em>' attribute.
	 * @see #isSetEnumProviderID()
	 * @see #unsetEnumProviderID()
	 * @see #setEnumProviderID(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getVariable_EnumProviderID()
	 * @model unsettable="true"
	 * @generated
	 */
	String getEnumProviderID();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID <em>Enum Provider ID</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @param value
	 *            the new value of the '<em>Enum Provider ID</em>' attribute.
	 * @see #isSetEnumProviderID()
	 * @see #unsetEnumProviderID()
	 * @see #getEnumProviderID()
	 * @generated
	 */
	void setEnumProviderID(String value);

	/**
	 * Unsets the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID <em>Enum Provider ID</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @see #isSetEnumProviderID()
	 * @see #getEnumProviderID()
	 * @see #setEnumProviderID(String)
	 * @generated
	 */
	void unsetEnumProviderID();

	/**
	 * Returns whether the value of the '{@link org.eclipse.ease.lang.unittest.definition.IVariable#getEnumProviderID <em>Enum Provider ID</em>}' attribute is set.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return whether the value of the '<em>Enum Provider ID</em>' attribute is set.
	 * @see #unsetEnumProviderID()
	 * @see #getEnumProviderID()
	 * @see #setEnumProviderID(String)
	 * @generated
	 */
	boolean isSetEnumProviderID();

	/**
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Path</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @model kind="operation" dataType="org.eclipse.ease.lang.unittest.definition.Path"
	 * @generated
	 */
	IPath getPath();

} // IVariable
