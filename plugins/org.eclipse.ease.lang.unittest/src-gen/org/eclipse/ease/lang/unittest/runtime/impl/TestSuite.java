/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import java.util.Collection;

import org.eclipse.ease.AbstractScriptEngine;
import org.eclipse.ease.IReplEngine;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptEngineInterruptedException;
import org.eclipse.ease.ScriptExecutionException;
import org.eclipse.ease.ScriptResult;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.TestSuiteScriptEngine;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ICode;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.util.EObjectResolvingEList;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test Suite</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestSuite#getActiveTests <em>Active Tests</em>}</li>
 * <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestSuite#getDefinition <em>Definition</em>}</li>
 * <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestSuite#getMasterEngine <em>Master Engine</em>}</li>
 * </ul>
 *
 * @generated
 */
public class TestSuite extends TestContainer implements ITestSuite {
	/**
	 * The cached value of the '{@link #getActiveTests() <em>Active Tests</em>}' reference list. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getActiveTests()
	 * @generated
	 * @ordered
	 */
	protected EList<ITestEntity> activeTests;

	/**
	 * The cached value of the '{@link #getDefinition() <em>Definition</em>}' reference. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getDefinition()
	 * @generated
	 * @ordered
	 */
	protected ITestSuiteDefinition definition;

	/**
	 * The default value of the '{@link #getMasterEngine() <em>Master Engine</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getMasterEngine()
	 * @generated
	 * @ordered
	 */
	protected static final IScriptEngine MASTER_ENGINE_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getMasterEngine() <em>Master Engine</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getMasterEngine()
	 * @generated
	 * @ordered
	 */
	protected IScriptEngine masterEngine = MASTER_ENGINE_EDEFAULT;

	private IScriptEngine fSetupEngine;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	protected TestSuite() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.TEST_SUITE;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public EList<ITestEntity> getActiveTests() {
		if (activeTests == null) {
			activeTests = new EObjectResolvingEList<>(ITestEntity.class, this, IRuntimePackage.TEST_SUITE__ACTIVE_TESTS);
		}
		return activeTests;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public ITestSuiteDefinition getDefinition() {
		if ((definition != null) && definition.eIsProxy()) {
			final InternalEObject oldDefinition = (InternalEObject) definition;
			definition = (ITestSuiteDefinition) eResolveProxy(oldDefinition);
			if (definition != oldDefinition) {
				if (eNotificationRequired())
					eNotify(new ENotificationImpl(this, Notification.RESOLVE, IRuntimePackage.TEST_SUITE__DEFINITION, oldDefinition, definition));
			}
		}
		return definition;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	public ITestSuiteDefinition basicGetDefinition() {
		return definition;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setDefinition(ITestSuiteDefinition newDefinition) {
		final ITestSuiteDefinition oldDefinition = definition;
		definition = newDefinition;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_SUITE__DEFINITION, oldDefinition, definition));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public IScriptEngine getMasterEngine() {
		return masterEngine;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setMasterEngine(IScriptEngine newMasterEngine) {
		final IScriptEngine oldMasterEngine = masterEngine;
		masterEngine = newMasterEngine;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_SUITE__MASTER_ENGINE, oldMasterEngine, masterEngine));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
		case IRuntimePackage.TEST_SUITE__ACTIVE_TESTS:
			return getActiveTests();
		case IRuntimePackage.TEST_SUITE__DEFINITION:
			if (resolve)
				return getDefinition();
			return basicGetDefinition();
		case IRuntimePackage.TEST_SUITE__MASTER_ENGINE:
			return getMasterEngine();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
		case IRuntimePackage.TEST_SUITE__ACTIVE_TESTS:
			getActiveTests().clear();
			getActiveTests().addAll((Collection<? extends ITestEntity>) newValue);
			return;
		case IRuntimePackage.TEST_SUITE__DEFINITION:
			setDefinition((ITestSuiteDefinition) newValue);
			return;
		case IRuntimePackage.TEST_SUITE__MASTER_ENGINE:
			setMasterEngine((IScriptEngine) newValue);
			return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
		case IRuntimePackage.TEST_SUITE__ACTIVE_TESTS:
			getActiveTests().clear();
			return;
		case IRuntimePackage.TEST_SUITE__DEFINITION:
			setDefinition((ITestSuiteDefinition) null);
			return;
		case IRuntimePackage.TEST_SUITE__MASTER_ENGINE:
			setMasterEngine(MASTER_ENGINE_EDEFAULT);
			return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
		case IRuntimePackage.TEST_SUITE__ACTIVE_TESTS:
			return (activeTests != null) && !activeTests.isEmpty();
		case IRuntimePackage.TEST_SUITE__DEFINITION:
			return definition != null;
		case IRuntimePackage.TEST_SUITE__MASTER_ENGINE:
			return MASTER_ENGINE_EDEFAULT == null ? masterEngine != null : !MASTER_ENGINE_EDEFAULT.equals(masterEngine);
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy())
			return super.toString();

		final StringBuilder result = new StringBuilder(super.toString());
		result.append(" (masterEngine: ");
		result.append(masterEngine);
		result.append(')');
		return result.toString();
	}

	/**
	 * @generated NOT
	 */
	@Override
	public ITestSuite getTestSuite() {
		return this;
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void run(ITestExecutionStrategy strategy) {
		setEntityStatus(TestStatus.RUNNING);

		try {
			// testsuite setup
			runSetupTeardownCode(ITestSuiteDefinition.CODE_LOCATION_TESTSUITE_SETUP, strategy);

			if (!hasSetupError()) {
				// not calling super.run() here as we do want to have full control on the entityStatus
				for (final ITestContainer child : getChildContainers()) {
					if (!isTerminated())
						strategy.execute(child);
				}
			}

			if ((!hasError()) || ((getDefinition() != null) && (getDefinition().getFlag(Flag.RUN_TEARDOWN_ON_ERROR, true))))
				runSetupTeardownCode(ITestSuiteDefinition.CODE_LOCATION_TESTSUITE_TEARDOWN, strategy);

		} finally {
			if (getMasterEngine() != null)
				setMasterEngine(null);

			if (fSetupEngine != null) {
				fSetupEngine.terminate();
				fSetupEngine = null;
			}

			// make sure all tests are marked as finished
			for (final ITestEntity test : getCopyOfChildren()) {
				if (TestStatus.RUNNING.equals(test.getStatus()))
					test.setEntityStatus(TestStatus.PASS);
			}

			setEntityStatus(TestStatus.FINISHED);
		}
	}

	/**
	 * @generated NOT
	 */
	private boolean hasSetupError() {
		for (final ITestEntity child : getCopyOfChildren()) {
			if ((child instanceof ITest) && (child.hasError()))
				return true;
		}

		return false;
	}

	/**
	 * @generated NOT
	 */
	private void runSetupTeardownCode(String codeLocation, ITestExecutionStrategy strategy) {
		final ITestSuiteDefinition definition = getDefinition();
		if (definition != null) {
			final ICode customCode = definition.getCustomCode(codeLocation);
			if ((customCode != null) && (!customCode.getContent().trim().isEmpty())) {
				if (fSetupEngine == null) {
					fSetupEngine = strategy.createScriptEngine(this, null);

					if (fSetupEngine instanceof AbstractScriptEngine)
						((AbstractScriptEngine) fSetupEngine).setExecutionRootFile(getResource());

					fSetupEngine.setVariable(TestSuiteScriptEngine.TEST_SUITE_VARIABLE, this);

					if (fSetupEngine instanceof IReplEngine) {
						((IReplEngine) fSetupEngine).setTerminateOnIdle(false);
						fSetupEngine.schedule();
					}
				}

				if (fSetupEngine != null) {
					try {
						final ScriptResult result = fSetupEngine.execute(new Script(customCode.getLocation(), customCode.getContent()));
						result.get();
					} catch (final ScriptEngineInterruptedException e) {
						getTest("[user event]").addError("Aborted by user", new ScriptStackTrace());
					} catch (final ScriptExecutionException e) {
						getTest("[" + codeLocation + "]").addError(e.getMessage(), e.getScriptStackTrace());
					}
				} else {
					getTest("[" + codeLocation + "]").addError(
							"Could not create setup/teardown engine. Please select an appropriate engine on the Overview tab of the *.suite file.", null);
				}
			}
		}
	}

} // TestSuite
