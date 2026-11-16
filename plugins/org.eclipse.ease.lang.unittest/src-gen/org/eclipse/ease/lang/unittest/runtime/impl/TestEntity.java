/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import java.lang.reflect.InvocationTargetException;
import java.util.Collection;
import java.util.stream.Collectors;

import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.lang.unittest.UnitTestHelper;
import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.ease.lang.unittest.runtime.IMetadata;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.notify.Notifier;
import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;
import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test Entity</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getName <em>Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getEntityStatus <em>Entity Status</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getEndTimestamp <em>End Timestamp</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getStartTimestamp <em>Start Timestamp</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getParent <em>Parent</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getMetadata <em>Metadata</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getDuration <em>Duration</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getResults <em>Results</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#getEstimatedDuration <em>Estimated Duration</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity#isTerminated <em>Terminated</em>}</li>
 * </ul>
 *
 * @generated
 */
public abstract class TestEntity extends MinimalEObjectImpl.Container implements ITestEntity {
	/**
	 * The default value of the '{@link #getDescription() <em>Description</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDescription()
	 * @generated
	 * @ordered
	 */
	protected static final String DESCRIPTION_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getDescription() <em>Description</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDescription()
	 * @generated
	 * @ordered
	 */
	protected String description = DESCRIPTION_EDEFAULT;

	/**
	 * The default value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected static final String NAME_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected String name = NAME_EDEFAULT;

	/**
	 * The default value of the '{@link #getEntityStatus() <em>Entity Status</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEntityStatus()
	 * @generated
	 * @ordered
	 */
	protected static final TestStatus ENTITY_STATUS_EDEFAULT = TestStatus.NOT_RUN;

	/**
	 * The cached value of the '{@link #getEntityStatus() <em>Entity Status</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEntityStatus()
	 * @generated
	 * @ordered
	 */
	protected TestStatus entityStatus = ENTITY_STATUS_EDEFAULT;

	/**
	 * The default value of the '{@link #getEndTimestamp() <em>End Timestamp</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEndTimestamp()
	 * @generated
	 * @ordered
	 */
	protected static final long END_TIMESTAMP_EDEFAULT = 0L;

	/**
	 * The cached value of the '{@link #getEndTimestamp() <em>End Timestamp</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEndTimestamp()
	 * @generated
	 * @ordered
	 */
	protected long endTimestamp = END_TIMESTAMP_EDEFAULT;

	/**
	 * The default value of the '{@link #getStartTimestamp() <em>Start Timestamp</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getStartTimestamp()
	 * @generated
	 * @ordered
	 */
	protected static final long START_TIMESTAMP_EDEFAULT = 0L;

	/**
	 * The cached value of the '{@link #getStartTimestamp() <em>Start Timestamp</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getStartTimestamp()
	 * @generated
	 * @ordered
	 */
	protected long startTimestamp = START_TIMESTAMP_EDEFAULT;

	/**
	 * The cached value of the '{@link #getMetadata() <em>Metadata</em>}' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getMetadata()
	 * @generated
	 * @ordered
	 */
	protected EList<IMetadata> metadata;

	/**
	 * The default value of the '{@link #getDuration() <em>Duration</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDuration()
	 * @generated
	 * @ordered
	 */
	protected static final long DURATION_EDEFAULT = 0L;

	/**
	 * The cached value of the '{@link #getResults() <em>Results</em>}' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getResults()
	 * @generated
	 * @ordered
	 */
	protected EList<ITestResult> results;

	/**
	 * The default value of the '{@link #getEstimatedDuration() <em>Estimated Duration</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEstimatedDuration()
	 * @generated
	 * @ordered
	 */
	protected static final long ESTIMATED_DURATION_EDEFAULT = -1L;

	/**
	 * The cached value of the '{@link #getEstimatedDuration() <em>Estimated Duration</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEstimatedDuration()
	 * @generated
	 * @ordered
	 */
	protected long estimatedDuration = ESTIMATED_DURATION_EDEFAULT;

	/**
	 * The default value of the '{@link #isTerminated() <em>Terminated</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #isTerminated()
	 * @generated
	 * @ordered
	 */
	protected static final boolean TERMINATED_EDEFAULT = false;

	/**
	 * The cached value of the '{@link #isTerminated() <em>Terminated</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #isTerminated()
	 * @generated
	 * @ordered
	 */
	protected boolean terminated = TERMINATED_EDEFAULT;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	protected TestEntity() {
		super();

		eAdapters().add(new Adapter() {

			@Override
			public void notifyChanged(Notification notification) {
				if ((getEntityStatus() != TestStatus.RUNNING) && (getEntityStatus() != TestStatus.NOT_RUN)
						&& (IRuntimePackage.Literals.TEST_ENTITY__ENTITY_STATUS.equals(notification.getFeature()))) {
					if (!isDisabled()) {
						// create error markers
						for (final ITestResult result : getResults())
							UnitTestHelper.createWorkspaceMarker(result, TestEntity.this);
					}
				}
			}

			@Override
			public Notifier getTarget() {
				return null;
			}

			@Override
			public void setTarget(Notifier newTarget) {
			}

			@Override
			public boolean isAdapterForType(Object type) {
				return true;
			}
		});
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.TEST_ENTITY;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getDescription() {
		return description;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setDescription(String newDescription) {
		String oldDescription = description;
		description = newDescription;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__DESCRIPTION, oldDescription, description));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getName() {
		return name;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setName(String newName) {
		String oldName = name;
		name = newName;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__NAME, oldName, name));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public TestStatus getEntityStatus() {
		return entityStatus;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public void setEntityStatusGen(TestStatus newEntityStatus) {
		TestStatus oldEntityStatus = entityStatus;
		entityStatus = newEntityStatus == null ? ENTITY_STATUS_EDEFAULT : newEntityStatus;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__ENTITY_STATUS, oldEntityStatus, entityStatus));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public TestStatus getStatus() {
		if (isDisabled())
			return TestStatus.DISABLED;

		int status = getEntityStatus().getValue();
		for (final ITestResult result : getResults()) {
			status = Math.max(status, result.getStatus().getValue());
		}

		return TestStatus.get(status);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ITestContainer getRoot() {
		if (getParent() != null)
			return getParent().getRoot();

		if (this instanceof ITestContainer)
			return (ITestContainer) this;

		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public boolean hasError() {
		return !getResults(TestStatus.ERROR).isEmpty();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ITestSuite getTestSuite() {
		if (this instanceof TestSuite)
			return (ITestSuite) this;

		final ITestContainer parent = getParent();
		if (parent != null)
			return parent.getTestSuite();

		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public Object getResource() {
		if (getParent() != null)
			return getParent().getResource();

		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void reset() {
		getMetadata().clear();
		getResults().clear();

		// set status after clearing results. This way we do not generate obsolete markers
		setEntityStatus(TestStatus.NOT_RUN);

		setStartTimestamp(0);
		setEndTimestamp(0);

		setTerminated(false);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void run(ITestExecutionStrategy strategy) {
		// TODO: implement this method
		// Ensure that you remove @generated or mark it @generated NOT
		throw new UnsupportedOperationException();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ITestResult getWorstResult() {
		return getResults().stream().sorted((s1, s2) -> s2.getStatus().compareTo(s1.getStatus())).findFirst().orElse(null);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ITestResult addError(String message, ScriptStackTrace trace) {

		final ITestResult result = IRuntimeFactory.eINSTANCE.createTestResult();
		result.setStatus(TestStatus.ERROR);
		result.setMessage(message);
		result.setStackTrace(trace);

		getResults().add(result);

		return result;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public EList<ITestResult> getResults(TestStatus status) {
		return new BasicEList<>(getResults().stream().filter(r -> r.getStatus().equals(status)).collect(Collectors.toList()));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public IPath getFullPath() {
		if (getParent() != null)
			return getParent().getFullPath().append(getName());

		return new Path(getName()).makeAbsolute();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void setDisabled(String message) {
		final ITestResult testResult = IRuntimeFactory.eINSTANCE.createTestResult();
		testResult.setMessage(message);
		testResult.setStatus(TestStatus.DISABLED);

		getResults().add(testResult);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public boolean isDisabled() {

		for (final ITestResult result : getResults()) {
			if (TestStatus.DISABLED.equals(result.getStatus()))
				return true;
		}

		return TestStatus.DISABLED.equals(getEntityStatus());
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseAdd(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case IRuntimePackage.TEST_ENTITY__PARENT:
				if (eInternalContainer() != null)
					msgs = eBasicRemoveFromContainer(msgs);
				return basicSetParent((ITestContainer)otherEnd, msgs);
		}
		return super.eInverseAdd(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public long getStartTimestamp() {
		return startTimestamp;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setStartTimestamp(long newStartTimestamp) {
		long oldStartTimestamp = startTimestamp;
		startTimestamp = newStartTimestamp;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__START_TIMESTAMP, oldStartTimestamp, startTimestamp));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestContainer getParent() {
		if (eContainerFeatureID() != IRuntimePackage.TEST_ENTITY__PARENT) return null;
		return (ITestContainer)eInternalContainer();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetParent(ITestContainer newParent, NotificationChain msgs) {
		msgs = eBasicSetContainer((InternalEObject)newParent, IRuntimePackage.TEST_ENTITY__PARENT, msgs);
		return msgs;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setParent(ITestContainer newParent) {
		if (newParent != eInternalContainer() || (eContainerFeatureID() != IRuntimePackage.TEST_ENTITY__PARENT && newParent != null)) {
			if (EcoreUtil.isAncestor(this, newParent))
				throw new IllegalArgumentException("Recursive containment not allowed for " + toString());
			NotificationChain msgs = null;
			if (eInternalContainer() != null)
				msgs = eBasicRemoveFromContainer(msgs);
			if (newParent != null)
				msgs = ((InternalEObject)newParent).eInverseAdd(this, IRuntimePackage.TEST_CONTAINER__CHILDREN, ITestContainer.class, msgs);
			msgs = basicSetParent(newParent, msgs);
			if (msgs != null) msgs.dispatch();
		}
		else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__PARENT, newParent, newParent));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<IMetadata> getMetadata() {
		if (metadata == null) {
			metadata = new EObjectContainmentEList<IMetadata>(IMetadata.class, this, IRuntimePackage.TEST_ENTITY__METADATA);
		}
		return metadata;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public long getDuration() {
		if (getEndTimestamp() > 0)
			return getEndTimestamp() - getStartTimestamp();

		if (getStartTimestamp() > 0)
			return System.currentTimeMillis() - getStartTimestamp();

		return 0;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<ITestResult> getResults() {
		if (results == null) {
			results = new EObjectContainmentEList<ITestResult>(ITestResult.class, this, IRuntimePackage.TEST_ENTITY__RESULTS);
		}
		return results;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public long getEstimatedDuration() {
		return estimatedDuration;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setEstimatedDuration(long newEstimatedDuration) {
		long oldEstimatedDuration = estimatedDuration;
		estimatedDuration = newEstimatedDuration;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__ESTIMATED_DURATION, oldEstimatedDuration, estimatedDuration));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean isTerminated() {
		return terminated;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setTerminated(boolean newTerminated) {
		boolean oldTerminated = terminated;
		terminated = newTerminated;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__TERMINATED, oldTerminated, terminated));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case IRuntimePackage.TEST_ENTITY__PARENT:
				return basicSetParent(null, msgs);
			case IRuntimePackage.TEST_ENTITY__METADATA:
				return ((InternalEList<?>)getMetadata()).basicRemove(otherEnd, msgs);
			case IRuntimePackage.TEST_ENTITY__RESULTS:
				return ((InternalEList<?>)getResults()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eBasicRemoveFromContainerFeature(NotificationChain msgs) {
		switch (eContainerFeatureID()) {
			case IRuntimePackage.TEST_ENTITY__PARENT:
				return eInternalContainer().eInverseRemove(this, IRuntimePackage.TEST_CONTAINER__CHILDREN, ITestContainer.class, msgs);
		}
		return super.eBasicRemoveFromContainerFeature(msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case IRuntimePackage.TEST_ENTITY__DESCRIPTION:
				return getDescription();
			case IRuntimePackage.TEST_ENTITY__NAME:
				return getName();
			case IRuntimePackage.TEST_ENTITY__ENTITY_STATUS:
				return getEntityStatus();
			case IRuntimePackage.TEST_ENTITY__END_TIMESTAMP:
				return getEndTimestamp();
			case IRuntimePackage.TEST_ENTITY__START_TIMESTAMP:
				return getStartTimestamp();
			case IRuntimePackage.TEST_ENTITY__PARENT:
				return getParent();
			case IRuntimePackage.TEST_ENTITY__METADATA:
				return getMetadata();
			case IRuntimePackage.TEST_ENTITY__DURATION:
				return getDuration();
			case IRuntimePackage.TEST_ENTITY__RESULTS:
				return getResults();
			case IRuntimePackage.TEST_ENTITY__ESTIMATED_DURATION:
				return getEstimatedDuration();
			case IRuntimePackage.TEST_ENTITY__TERMINATED:
				return isTerminated();
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
			case IRuntimePackage.TEST_ENTITY__DESCRIPTION:
				setDescription((String)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__NAME:
				setName((String)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__ENTITY_STATUS:
				setEntityStatus((TestStatus)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__END_TIMESTAMP:
				setEndTimestamp((Long)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__START_TIMESTAMP:
				setStartTimestamp((Long)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__PARENT:
				setParent((ITestContainer)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__METADATA:
				getMetadata().clear();
				getMetadata().addAll((Collection<? extends IMetadata>)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__RESULTS:
				getResults().clear();
				getResults().addAll((Collection<? extends ITestResult>)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__ESTIMATED_DURATION:
				setEstimatedDuration((Long)newValue);
				return;
			case IRuntimePackage.TEST_ENTITY__TERMINATED:
				setTerminated((Boolean)newValue);
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
			case IRuntimePackage.TEST_ENTITY__DESCRIPTION:
				setDescription(DESCRIPTION_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__NAME:
				setName(NAME_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__ENTITY_STATUS:
				setEntityStatus(ENTITY_STATUS_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__END_TIMESTAMP:
				setEndTimestamp(END_TIMESTAMP_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__START_TIMESTAMP:
				setStartTimestamp(START_TIMESTAMP_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__PARENT:
				setParent((ITestContainer)null);
				return;
			case IRuntimePackage.TEST_ENTITY__METADATA:
				getMetadata().clear();
				return;
			case IRuntimePackage.TEST_ENTITY__RESULTS:
				getResults().clear();
				return;
			case IRuntimePackage.TEST_ENTITY__ESTIMATED_DURATION:
				setEstimatedDuration(ESTIMATED_DURATION_EDEFAULT);
				return;
			case IRuntimePackage.TEST_ENTITY__TERMINATED:
				setTerminated(TERMINATED_EDEFAULT);
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
			case IRuntimePackage.TEST_ENTITY__DESCRIPTION:
				return DESCRIPTION_EDEFAULT == null ? description != null : !DESCRIPTION_EDEFAULT.equals(description);
			case IRuntimePackage.TEST_ENTITY__NAME:
				return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
			case IRuntimePackage.TEST_ENTITY__ENTITY_STATUS:
				return entityStatus != ENTITY_STATUS_EDEFAULT;
			case IRuntimePackage.TEST_ENTITY__END_TIMESTAMP:
				return endTimestamp != END_TIMESTAMP_EDEFAULT;
			case IRuntimePackage.TEST_ENTITY__START_TIMESTAMP:
				return startTimestamp != START_TIMESTAMP_EDEFAULT;
			case IRuntimePackage.TEST_ENTITY__PARENT:
				return getParent() != null;
			case IRuntimePackage.TEST_ENTITY__METADATA:
				return metadata != null && !metadata.isEmpty();
			case IRuntimePackage.TEST_ENTITY__DURATION:
				return getDuration() != DURATION_EDEFAULT;
			case IRuntimePackage.TEST_ENTITY__RESULTS:
				return results != null && !results.isEmpty();
			case IRuntimePackage.TEST_ENTITY__ESTIMATED_DURATION:
				return estimatedDuration != ESTIMATED_DURATION_EDEFAULT;
			case IRuntimePackage.TEST_ENTITY__TERMINATED:
				return terminated != TERMINATED_EDEFAULT;
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	@SuppressWarnings("unchecked")
	public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
		switch (operationID) {
			case IRuntimePackage.TEST_ENTITY___GET_STATUS:
				return getStatus();
			case IRuntimePackage.TEST_ENTITY___GET_ROOT:
				return getRoot();
			case IRuntimePackage.TEST_ENTITY___HAS_ERROR:
				return hasError();
			case IRuntimePackage.TEST_ENTITY___GET_TEST_SUITE:
				return getTestSuite();
			case IRuntimePackage.TEST_ENTITY___GET_RESOURCE:
				return getResource();
			case IRuntimePackage.TEST_ENTITY___RESET:
				reset();
				return null;
			case IRuntimePackage.TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY:
				run((ITestExecutionStrategy)arguments.get(0));
				return null;
			case IRuntimePackage.TEST_ENTITY___GET_WORST_RESULT:
				return getWorstResult();
			case IRuntimePackage.TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE:
				return addError((String)arguments.get(0), (ScriptStackTrace)arguments.get(1));
			case IRuntimePackage.TEST_ENTITY___GET_RESULTS__TESTSTATUS:
				return getResults((TestStatus)arguments.get(0));
			case IRuntimePackage.TEST_ENTITY___GET_FULL_PATH:
				return getFullPath();
			case IRuntimePackage.TEST_ENTITY___SET_DISABLED__STRING:
				setDisabled((String)arguments.get(0));
				return null;
			case IRuntimePackage.TEST_ENTITY___IS_DISABLED:
				return isDisabled();
		}
		return super.eInvoke(operationID, arguments);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy()) return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (description: ");
		result.append(description);
		result.append(", name: ");
		result.append(name);
		result.append(", entityStatus: ");
		result.append(entityStatus);
		result.append(", endTimestamp: ");
		result.append(endTimestamp);
		result.append(", startTimestamp: ");
		result.append(startTimestamp);
		result.append(", estimatedDuration: ");
		result.append(estimatedDuration);
		result.append(", terminated: ");
		result.append(terminated);
		result.append(')');
		return result.toString();
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void setEntityStatus(TestStatus value) {
		if (value == TestStatus.RUNNING)
			setStartTimestamp(System.currentTimeMillis());

		else
			setEndTimestamp(System.currentTimeMillis());

		// do this after setting timestamps as these could add some results due to timeouts
		setEntityStatusGen(value);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public long getEndTimestamp() {
		return endTimestamp;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setEndTimestamp(long newEndTimestamp) {
		long oldEndTimestamp = endTimestamp;
		endTimestamp = newEndTimestamp;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_ENTITY__END_TIMESTAMP, oldEndTimestamp, endTimestamp));
	}

} // TestEntity
