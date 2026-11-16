/**
 */
package org.eclipse.ease.lang.unittest.runtime.impl;

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimePackage;
import org.eclipse.ease.lang.unittest.runtime.ITest;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.util.EObjectContainmentWithInverseEList;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test Container</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestContainer#getChildren <em>Children</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.runtime.impl.TestContainer#getResource <em>Resource</em>}</li>
 * </ul>
 *
 * @generated
 */
public abstract class TestContainer extends TestEntity implements ITestContainer {
	/**
	 * The cached value of the '{@link #getChildren() <em>Children</em>}' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getChildren()
	 * @generated
	 * @ordered
	 */
	protected EList<ITestEntity> children;

	/**
	 * The default value of the '{@link #getResource() <em>Resource</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getResource()
	 * @generated
	 * @ordered
	 */
	protected static final Object RESOURCE_EDEFAULT = null;
	/**
	 * The cached value of the '{@link #getResource() <em>Resource</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getResource()
	 * @generated
	 * @ordered
	 */
	protected Object resource = RESOURCE_EDEFAULT;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	protected TestContainer() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRuntimePackage.Literals.TEST_CONTAINER;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public EList<ITestEntity> getChildrenGen() {
		if (children == null) {
			children = new EObjectContainmentWithInverseEList<ITestEntity>(ITestEntity.class, this, IRuntimePackage.TEST_CONTAINER__CHILDREN, IRuntimePackage.TEST_ENTITY__PARENT);
		}
		return children;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object getResource() {
		return resource;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setResource(Object newResource) {
		Object oldResource = resource;
		resource = newResource;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRuntimePackage.TEST_CONTAINER__RESOURCE, oldResource, resource));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ITest getTest(String name) {
		for (final ITestEntity child : getCopyOfChildren()) {
			if ((child instanceof ITest) && (name.equals(child.getName())))
				return (ITest) child;
		}

		// no global scope available yet
		final ITest test = IRuntimeFactory.eINSTANCE.createTest();
		test.setName(name);
		test.setEntityStatus(TestStatus.RUNNING);

		synchronized (this) {
			getChildren().add(test);
		}

		return test;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public NotificationChain eInverseAdd(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				return ((InternalEList<InternalEObject>)(InternalEList<?>)getChildren()).basicAdd(otherEnd, msgs);
		}
		return super.eInverseAdd(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				return ((InternalEList<?>)getChildren()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				return getChildren();
			case IRuntimePackage.TEST_CONTAINER__RESOURCE:
				return getResource();
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
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				getChildren().clear();
				getChildren().addAll((Collection<? extends ITestEntity>)newValue);
				return;
			case IRuntimePackage.TEST_CONTAINER__RESOURCE:
				setResource(newValue);
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
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				getChildren().clear();
				return;
			case IRuntimePackage.TEST_CONTAINER__RESOURCE:
				setResource(RESOURCE_EDEFAULT);
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
			case IRuntimePackage.TEST_CONTAINER__CHILDREN:
				return children != null && !children.isEmpty();
			case IRuntimePackage.TEST_CONTAINER__RESOURCE:
				return RESOURCE_EDEFAULT == null ? resource != null : !RESOURCE_EDEFAULT.equals(resource);
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
		switch (operationID) {
			case IRuntimePackage.TEST_CONTAINER___GET_TEST__STRING:
				return getTest((String)arguments.get(0));
			case IRuntimePackage.TEST_CONTAINER___GET_CHILD_CONTAINERS:
				return getChildContainers();
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
		result.append(" (resource: ");
		result.append(resource);
		result.append(')');
		return result.toString();
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void run(ITestExecutionStrategy strategy) {
		setEntityStatus(TestStatus.RUNNING);

		for (final ITestContainer child : getChildContainers()) {
			if (!isTerminated())
				strategy.execute(child);
		}

		setEntityStatus(TestStatus.FINISHED);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public EList<ITestContainer> getChildContainers() {
		final EList<ITestContainer> result = new BasicEList<>();
		for (final Object child : getCopyOfChildren()) {
			if (child instanceof ITestContainer)
				result.add((ITestContainer) child);
		}

		return result;
	}

	/**
	 * @generated NOT
	 */
	@Override
	public TestStatus getStatus() {
		int status = super.getStatus().getValue();

		for (final ITestEntity child : getCopyOfChildren())
			status = Math.max(status, child.getStatus().getValue());

		return TestStatus.get(status);
	}

	/**
	 * @generated NOT
	 */
	@Override
	public boolean hasError() {
		for (final ITestEntity child : getCopyOfChildren()) {
			if (child.hasError())
				return true;
		}

		return super.hasError();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void reset() {
		// remove single tests
		synchronized (this) {
			for (final Object child : getCopyOfChildren()) {
				if (child instanceof ITest)
					getChildren().remove(child);
			}
		}

		super.reset();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public long getEstimatedDuration() {
		long duration = super.getEstimatedDuration();
		final List<ITestEntity> children = getCopyOfChildren();
		if ((duration < 0) && (!children.isEmpty())) {
			// try to fetch duration from child elements. If one of them does not have an estimation
			duration = 0;

			for (final ITestEntity child : children) {
				final long childDuration = child.getEstimatedDuration();
				if (childDuration < 0)
					return childDuration;

				duration += childDuration;
			}

			return duration;
		}

		return super.getEstimatedDuration();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void setTerminated(boolean newTerminated) {
		super.setTerminated(newTerminated);

		for (final ITestEntity child : getCopyOfChildren())
			child.setTerminated(newTerminated);
	}

	@Override
	public synchronized EList<ITestEntity> getChildren() {
		return getChildrenGen();
	}

	@Override
	public synchronized List<ITestEntity> getCopyOfChildren() {
		return new ArrayList<>(getChildrenGen());
	}
} // TestContainer
