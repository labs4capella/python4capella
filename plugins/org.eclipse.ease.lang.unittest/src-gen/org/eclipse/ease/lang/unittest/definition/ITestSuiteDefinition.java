/**
 */
package org.eclipse.ease.lang.unittest.definition;

import org.eclipse.core.runtime.IPath;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.common.util.EMap;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> A representation of the model object '<em><b>Test Suite Definition</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getName <em>Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getIncludeFilter <em>Include Filter</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getExcludeFilter <em>Exclude Filter</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDisabledResources <em>Disabled Resources</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVariables <em>Variables</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getCustomCode <em>Custom Code</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getFlags <em>Flags</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVersion <em>Version</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getResource <em>Resource</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition()
 * @model extendedMetaData="kind='element' name='TestSuite'"
 * @generated
 */
public interface ITestSuiteDefinition extends EObject {

	/**
	 * @generated NOT
	 */
	String CODE_LOCATION_TESTSUITE_SETUP = "TestSuite Setup";
	/**
	 * @generated NOT
	 */
	String CODE_LOCATION_TESTSUITE_TEARDOWN = "TestSuite Teardown";
	/**
	 * @generated NOT
	 */
	String CODE_LOCATION_TESTFILE_SETUP = "TestFile Setup";
	/**
	 * @generated NOT
	 */
	String CODE_LOCATION_TESTFILE_TEARDOWN = "TestFile Teardown";

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Name</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Description</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Description</em>' attribute.
	 * @see #setDescription(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Description()
	 * @model extendedMetaData="kind='element' name='description'"
	 * @generated
	 */
	String getDescription();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getDescription <em>Description</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Description</em>' attribute.
	 * @see #getDescription()
	 * @generated
	 */
	void setDescription(String value);

	/**
	 * Returns the value of the '<em><b>Include Filter</b></em>' attribute.
	 * The default value is <code>""</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Include Filter</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Include Filter</em>' attribute.
	 * @see #setIncludeFilter(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_IncludeFilter()
	 * @model default=""
	 *        extendedMetaData="kind='element' name='includeFilter'"
	 * @generated
	 */
	String getIncludeFilter();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getIncludeFilter <em>Include Filter</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Include Filter</em>' attribute.
	 * @see #getIncludeFilter()
	 * @generated
	 */
	void setIncludeFilter(String value);

	/**
	 * Returns the value of the '<em><b>Exclude Filter</b></em>' attribute.
	 * The default value is <code>""</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Exclude Filter</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Exclude Filter</em>' attribute.
	 * @see #setExcludeFilter(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_ExcludeFilter()
	 * @model default=""
	 *        extendedMetaData="kind='element' name='excludeFilter'"
	 * @generated
	 */
	String getExcludeFilter();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getExcludeFilter <em>Exclude Filter</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Exclude Filter</em>' attribute.
	 * @see #getExcludeFilter()
	 * @generated
	 */
	void setExcludeFilter(String value);

	/**
	 * Returns the value of the '<em><b>Disabled Resources</b></em>' attribute list. The list contents are of type {@link org.eclipse.core.runtime.IPath}. <!--
	 * begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Disabled Resources</em>' attribute list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>Disabled Resources</em>' attribute list.
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_DisabledResources()
	 * @model dataType="org.eclipse.ease.lang.unittest.definition.Path" extendedMetaData="kind='element' name='disabledResource'"
	 * @generated
	 */
	EList<IPath> getDisabledResources();

	/**
	 * Returns the value of the '<em><b>Variables</b></em>' containment reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.definition.IVariable}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Variables</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Variables</em>' containment reference list.
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Variables()
	 * @model containment="true"
	 *        extendedMetaData="kind='element' name='variable' namespace='##targetNamespace'"
	 * @generated
	 */
	EList<IVariable> getVariables();

	/**
	 * Returns the value of the '<em><b>Custom Code</b></em>' containment reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.definition.ICode}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Custom Code</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Custom Code</em>' containment reference list.
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_CustomCode()
	 * @model containment="true"
	 * @generated
	 */
	EList<ICode> getCustomCode();

	/**
	 * Returns the value of the '<em><b>Flags</b></em>' map.
	 * The key is of type {@link org.eclipse.ease.lang.unittest.definition.Flag},
	 * and the value is of type {@link java.lang.String},
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Flags</em>' map isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Flags</em>' map.
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Flags()
	 * @model mapType="org.eclipse.ease.lang.unittest.definition.FlagToStringMap&lt;org.eclipse.ease.lang.unittest.definition.Flag, org.eclipse.emf.ecore.EString&gt;"
	 *        extendedMetaData="kind='element' name='flag' namespace='##targetNamespace'"
	 * @generated
	 */
	EMap<Flag, String> getFlags();

	/**
	 * Returns the value of the '<em><b>Version</b></em>' attribute.
	 * The default value is <code>""</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Version</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Version</em>' attribute.
	 * @see #setVersion(String)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Version()
	 * @model default="" required="true"
	 * @generated
	 */
	String getVersion();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getVersion <em>Version</em>}' attribute.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @param value the new value of the '<em>Version</em>' attribute.
	 * @see #getVersion()
	 * @generated
	 */
	void setVersion(String value);

	/**
	 * Returns the value of the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Resource</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Resource</em>' attribute.
	 * @see #setResource(Object)
	 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getTestSuiteDefinition_Resource()
	 * @model transient="true"
	 * @generated
	 */
	Object getResource();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition#getResource <em>Resource</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Resource</em>' attribute.
	 * @see #getResource()
	 * @generated
	 */
	void setResource(Object value);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	ICode getCustomCode(String location);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	IVariable getVariable(String name);

	/**
	 * @generated NOT
	 */
	<T> T getFlag(Flag identifier, T defaultValue);

	/**
	 * @generated NOT
	 */
	void setVariable(String identifier, String content);

	/**
	 * @generated NOT
	 */
	void setFlag(String identifier, String value);
} // ITestSuiteDefinition
