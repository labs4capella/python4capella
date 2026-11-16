/**
 */
package org.eclipse.ease.lang.unittest.runtime;

import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Stack Trace Container</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer#getStackTrace <em>Stack Trace</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getStackTraceContainer()
 * @model
 * @generated
 */
public interface IStackTraceContainer extends EObject {
	/**
	 * Returns the value of the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Stack Trace</em>' attribute list isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Stack Trace</em>' attribute.
	 * @see #setStackTrace(ScriptStackTrace)
	 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimePackage#getStackTraceContainer_StackTrace()
	 * @model dataType="org.eclipse.ease.lang.unittest.runtime.ScriptStackTrace" transient="true"
	 * @generated
	 */
	ScriptStackTrace getStackTrace();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer#getStackTrace <em>Stack Trace</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Stack Trace</em>' attribute.
	 * @see #getStackTrace()
	 * @generated
	 */
	void setStackTrace(ScriptStackTrace value);

} // IStackTraceContainer
