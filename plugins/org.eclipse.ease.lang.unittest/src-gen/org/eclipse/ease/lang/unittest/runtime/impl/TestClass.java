/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestClass;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.impl.ENotificationImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test Class</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestClass#getStackTrace <em>Stack Trace</em>}</li>
 * </ul>
 *
 * @generated
 */
public class TestClass extends TestContainer implements ITestClass {
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
	protected TestClass() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.TEST_CLASS;
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
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_CLASS__STACK_TRACE, oldStackTrace, stackTrace));
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
			case IRuntimePackage.TEST_CLASS__STACK_TRACE:
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
			case IRuntimePackage.TEST_CLASS__STACK_TRACE:
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
			case IRuntimePackage.TEST_CLASS__STACK_TRACE:
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
			case IRuntimePackage.TEST_CLASS__STACK_TRACE:
				return STACK_TRACE_EDEFAULT == null ? stackTrace != null : !STACK_TRACE_EDEFAULT.equals(stackTrace);
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public int eBaseStructuralFeatureID(int derivedFeatureID, Class<?> baseClass) {
		if (baseClass == IStackTraceContainer.class) {
			switch (derivedFeatureID) {
				case IRuntimePackage.TEST_CLASS__STACK_TRACE: return IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE;
				default: return -1;
			}
		}
		return super.eBaseStructuralFeatureID(derivedFeatureID, baseClass);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public int eDerivedStructuralFeatureID(int baseFeatureID, Class<?> baseClass) {
		if (baseClass == IStackTraceContainer.class) {
			switch (baseFeatureID) {
				case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE: return IRuntimePackage.TEST_CLASS__STACK_TRACE;
				default: return -1;
			}
		}
		return super.eDerivedStructuralFeatureID(baseFeatureID, baseClass);
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

} // TestClass
