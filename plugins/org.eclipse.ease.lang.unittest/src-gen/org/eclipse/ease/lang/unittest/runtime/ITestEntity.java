/**
 */
package org.eclipse.ease.lang.unittest.runtime;

import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc --> A representation of the model object '<em><b>Test Entity</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getName <em>Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEntityStatus <em>Entity Status</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEndTimestamp <em>End Timestamp</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStartTimestamp <em>Start Timestamp</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent <em>Parent</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getMetadata <em>Metadata</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDuration <em>Duration</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResults <em>Results</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEstimatedDuration <em>Estimated Duration</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#isTerminated <em>Terminated</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity()
 * @model abstract="true"
 * @generated
 */
public interface ITestEntity extends EObject {

	/**
	 * EMF event to indicate we should run custom code.
	 *
	 * @generated NOT
	 */
	public static final int CUSTOM_CODE = Notification.EVENT_TYPE_COUNT + 1;

	/**
	 * Name for test to represent errors outside of test methods.
	 *
	 * @generated NOT
	 */
	public static final String GLOBAL_SCOPE_TEST = "[Global Scope]";

	/**
	 * Returns the value of the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Description</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Description</em>' attribute.
	 * @see #setDescription(String)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Description()
	 * @model
	 * @generated
	 */
	String getDescription();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDescription <em>Description</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Description</em>' attribute.
	 * @see #getDescription()
	 * @generated
	 */
	void setDescription(String value);

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Name</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Entity Status</b></em>' attribute.
	 * The literals are from the enumeration {@link org.eclipse.ease.lang.unittest.runtime.TestStatus}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Entity Status</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Entity Status</em>' attribute.
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @see #setEntityStatus(TestStatus)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_EntityStatus()
	 * @model
	 * @generated
	 */
	TestStatus getEntityStatus();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEntityStatus <em>Entity Status</em>}' attribute.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @param value the new value of the '<em>Entity Status</em>' attribute.
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @see #getEntityStatus()
	 * @generated
	 */
	void setEntityStatus(TestStatus value);

	/**
	 * Returns the value of the '<em><b>End Timestamp</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>End Timestamp</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>End Timestamp</em>' attribute.
	 * @see #setEndTimestamp(long)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_EndTimestamp()
	 * @model default="0"
	 * @generated
	 */
	long getEndTimestamp();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEndTimestamp <em>End Timestamp</em>}' attribute.
	 * <!-- begin-user-doc
	 * --> <!-- end-user-doc -->
	 * @param value the new value of the '<em>End Timestamp</em>' attribute.
	 * @see #getEndTimestamp()
	 * @generated
	 */
	void setEndTimestamp(long value);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	TestStatus getStatus();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	ITestContainer getRoot();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	boolean hasError();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	ITestSuite getTestSuite();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	Object getResource();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	void reset();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model strategyDataType="org.eclipse.ease.lang.unittest.runtime.TestExecutionStrategy"
	 * @generated
	 */
	void run(ITestExecutionStrategy strategy);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	ITestResult getWorstResult();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model stackTraceDataType="org.eclipse.ease.lang.unittest.runtime.ScriptStackTrace"
	 * @generated
	 */
	ITestResult addError(String message, ScriptStackTrace stackTrace);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	EList<ITestResult> getResults(TestStatus status);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation" dataType="org.eclipse.ease.lang.unittest.runtime.Path"
	 * @generated
	 */
	IPath getFullPath();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	void setDisabled(String message);

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @model kind="operation"
	 * @generated
	 */
	boolean isDisabled();

	/**
	 * Returns the value of the '<em><b>Start Timestamp</b></em>' attribute.
	 * The default value is <code>"0"</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Start Timestamp</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Start Timestamp</em>' attribute.
	 * @see #setStartTimestamp(long)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_StartTimestamp()
	 * @model default="0"
	 * @generated
	 */
	long getStartTimestamp();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStartTimestamp <em>Start Timestamp</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Start Timestamp</em>' attribute.
	 * @see #getStartTimestamp()
	 * @generated
	 */
	void setStartTimestamp(long value);

	/**
	 * Returns the value of the '<em><b>Parent</b></em>' container reference.
	 * It is bidirectional and its opposite is '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildren <em>Children</em>}'.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Parent</em>' container reference isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Parent</em>' container reference.
	 * @see #setParent(ITestContainer)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Parent()
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildren
	 * @model opposite="children" transient="false"
	 * @generated
	 */
	ITestContainer getParent();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent <em>Parent</em>}' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Parent</em>' container reference.
	 * @see #getParent()
	 * @generated
	 */
	void setParent(ITestContainer value);

	/**
	 * Returns the value of the '<em><b>Metadata</b></em>' containment reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.runtime.IMetadata}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Metadata</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Metadata</em>' containment reference list.
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Metadata()
	 * @model containment="true"
	 * @generated
	 */
	EList<IMetadata> getMetadata();

	/**
	 * Returns the value of the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Duration</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Duration</em>' attribute.
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Duration()
	 * @model transient="true" changeable="false" volatile="true" derived="true"
	 * @generated
	 */
	long getDuration();

	/**
	 * Returns the value of the '<em><b>Results</b></em>' containment reference list.
	 * The list contents are of type {@link org.eclipse.ease.lang.unittest.runtime.ITestResult}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Results</em>' containment reference list isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Results</em>' containment reference list.
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Results()
	 * @model containment="true"
	 * @generated
	 */
	EList<ITestResult> getResults();

	/**
	 * Returns the value of the '<em><b>Estimated Duration</b></em>' attribute.
	 * The default value is <code>"-1"</code>.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Estimated Duration</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Estimated Duration</em>' attribute.
	 * @see #setEstimatedDuration(long)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_EstimatedDuration()
	 * @model default="-1"
	 * @generated
	 */
	long getEstimatedDuration();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEstimatedDuration <em>Estimated Duration</em>}' attribute. <!--
	 * begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Estimated Duration</em>' attribute.
	 * @see #getEstimatedDuration()
	 * @generated
	 */
	void setEstimatedDuration(long value);

	/**
	 * Returns the value of the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Terminated</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Terminated</em>' attribute.
	 * @see #setTerminated(boolean)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getTestEntity_Terminated()
	 * @model
	 * @generated
	 */
	boolean isTerminated();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#isTerminated <em>Terminated</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Terminated</em>' attribute.
	 * @see #isTerminated()
	 * @generated
	 */
	void setTerminated(boolean value);

} // ITestEntity
