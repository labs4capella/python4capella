/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.impl.ENotificationImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.Test#getStackTrace <em>Stack Trace</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.Test#getDurationLimit <em>Duration Limit</em>}</li>
 * </ul>
 *
 * @generated
 */
public class Test extends TestEntity implements ITest {
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
	 * The default value of the '{@link #getDurationLimit() <em>Duration Limit</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDurationLimit()
	 * @generated
	 * @ordered
	 */
	protected static final long DURATION_LIMIT_EDEFAULT = -1L;
	/**
	 * The cached value of the '{@link #getDurationLimit() <em>Duration Limit</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDurationLimit()
	 * @generated
	 * @ordered
	 */
	protected long durationLimit = DURATION_LIMIT_EDEFAULT;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	protected Test() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.TEST;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public long getDurationLimit() {
		return durationLimit;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setDurationLimit(long newDurationLimit) {
		long oldDurationLimit = durationLimit;
		durationLimit = newDurationLimit;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST__DURATION_LIMIT, oldDurationLimit, durationLimit));
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
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST__STACK_TRACE, oldStackTrace, stackTrace));
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
			case IRuntimePackage.TEST__STACK_TRACE:
				return getStackTrace();
			case IRuntimePackage.TEST__DURATION_LIMIT:
				return getDurationLimit();
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
			case IRuntimePackage.TEST__STACK_TRACE:
				setStackTrace((ScriptStackTrace)newValue);
				return;
			case IRuntimePackage.TEST__DURATION_LIMIT:
				setDurationLimit((Long)newValue);
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
			case IRuntimePackage.TEST__STACK_TRACE:
				setStackTrace(STACK_TRACE_EDEFAULT);
				return;
			case IRuntimePackage.TEST__DURATION_LIMIT:
				setDurationLimit(DURATION_LIMIT_EDEFAULT);
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
			case IRuntimePackage.TEST__STACK_TRACE:
				return STACK_TRACE_EDEFAULT == null ? stackTrace != null : !STACK_TRACE_EDEFAULT.equals(stackTrace);
			case IRuntimePackage.TEST__DURATION_LIMIT:
				return durationLimit != DURATION_LIMIT_EDEFAULT;
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
				case IRuntimePackage.TEST__STACK_TRACE: return IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE;
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
				case IRuntimePackage.STACK_TRACE_CONTAINER__STACK_TRACE: return IRuntimePackage.TEST__STACK_TRACE;
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
		result.append(", durationLimit: ");
		result.append(durationLimit);
		result.append(')');
		return result.toString();
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void setEndTimestamp(long newEndTimestamp) {
		super.setEndTimestamp(newEndTimestamp);

		if ((getDurationLimit() > 0) && (getDurationLimit() < getDuration())) {
			final ITestResult result = IRuntimeFactory.eINSTANCE.createTestResult();
			result.setMessage("Test timeout: lasted " + getDuration() + " ms, limit was set to " + getDurationLimit() + " ms");
			result.setStackTrace(getStackTrace());

			final ITestSuiteDefinition definition = (getTestSuite() != null) ? getTestSuite().getDefinition() : null;
			if ((definition != null) && (definition.getFlag(Flag.PROMOTE_FAILURE_TO_ERROR, false)))
				result.setStatus(TestStatus.ERROR);
			else
				result.setStatus(TestStatus.FAILURE);

			getResults().add(result);
		}
	}
} // Test
