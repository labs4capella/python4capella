/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Stack Trace Container</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.StackTraceContainer#getStackTrace <em>Stack Trace</em>}</li>
 * </ul>
 *
 * @generated
 */
public class StackTraceContainer extends MinimalEObjectImpl.Container implements IStackTraceContainer {
	/**
	 * The default value of the '{@link #getStackTrace() <em>Stack Trace</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getStackTrace()
	 * @generated
	 * @ordered
	 */
	protected static final ScriptStackTrace STACK_TRACE_EDEFAULT = null;
	/**
	 * The cached value of the '{@link #getStackTrace() <em>Stack Trace</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getStackTrace()
	 * @generated
	 * @ordered
	 */
	protected ScriptStackTrace stackTrace = STACK_TRACE_EDEFAULT;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	protected StackTraceContainer() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.STACK_TRACE_CONTAINER;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ScriptStackTrace getStackTrace() {
		return stackTrace;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public void setStackTraceGen(ScriptStackTrace newStackTrace) {
		ScriptStackTrace oldStackTrace = stackTrace;
		stackTrace = newStackTrace;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE, oldStackTrace, stackTrace));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void setStackTrace(ScriptStackTrace newStackTrace) {
		// we need to clone the trace as it may change when the script engine continues
		setStackTraceGen((newStackTrace != null) ? newStackTrace.clone() : newStackTrace);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE:
				return getStackTrace();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE:
				setStackTrace((ScriptStackTrace)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE:
				setStackTrace(STACK_TRACE_EDEFAULT);
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE:
				return STACK_TRACE_EDEFAULT == null ? stackTrace != null : !STACK_TRACE_EDEFAULT.equals(stackTrace);
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy()) return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (stackTrace: ");
		result.append(stackTrace);
		result.append(')');
		return result.toString();
	}

} // StackTraceContainer
