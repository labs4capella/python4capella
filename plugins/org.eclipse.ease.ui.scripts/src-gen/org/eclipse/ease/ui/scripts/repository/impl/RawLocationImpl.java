/**
 * Copyright (c) 2013 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 */
package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.InputStream;
import java.lang.reflect.InvocationTargetException;

import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ease.ui.scripts.repository.IRawLocation;
import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Raw Location</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl#getLocation <em>Location</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.RawLocationImpl#isUpdatePending <em>Update Pending</em>}</li>
 * </ul>
 *
 * @generated
 */
public class RawLocationImpl extends MinimalEObjectImpl.Container implements IRawLocation {
	/**
	 * The default value of the '{@link #getLocation() <em>Location</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getLocation()
	 * @generated
	 * @ordered
	 */
	protected static final String LOCATION_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getLocation() <em>Location</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getLocation()
	 * @generated
	 * @ordered
	 */
	protected String location = LOCATION_EDEFAULT;

	/**
	 * The default value of the '{@link #isUpdatePending() <em>Update Pending</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #isUpdatePending()
	 * @generated
	 * @ordered
	 */
	protected static final boolean UPDATE_PENDING_EDEFAULT = false;

	/**
	 * The cached value of the '{@link #isUpdatePending() <em>Update Pending</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #isUpdatePending()
	 * @generated
	 * @ordered
	 */
	protected boolean updatePending = UPDATE_PENDING_EDEFAULT;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	protected RawLocationImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRepositoryPackage.Literals.RAW_LOCATION;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public String getLocation() {
		return location;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setLocation(String newLocation) {
		final String oldLocation = location;
		location = newLocation;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRepositoryPackage.RAW_LOCATION__LOCATION, oldLocation, location));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public boolean isUpdatePending() {
		return updatePending;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setUpdatePending(boolean newUpdatePending) {
		final boolean oldUpdatePending = updatePending;
		updatePending = newUpdatePending;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRepositoryPackage.RAW_LOCATION__UPDATE_PENDING, oldUpdatePending, updatePending));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public Object getResource() {
		return ResourceTools.resolve(getLocation());
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public InputStream getInputStream() {
		return ResourceTools.getInputStream(getLocation());
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
		case IRepositoryPackage.RAW_LOCATION__LOCATION:
			return getLocation();
		case IRepositoryPackage.RAW_LOCATION__UPDATE_PENDING:
			return isUpdatePending();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
		case IRepositoryPackage.RAW_LOCATION__LOCATION:
			setLocation((String) newValue);
			return;
		case IRepositoryPackage.RAW_LOCATION__UPDATE_PENDING:
			setUpdatePending((Boolean) newValue);
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
		case IRepositoryPackage.RAW_LOCATION__LOCATION:
			setLocation(LOCATION_EDEFAULT);
			return;
		case IRepositoryPackage.RAW_LOCATION__UPDATE_PENDING:
			setUpdatePending(UPDATE_PENDING_EDEFAULT);
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
		case IRepositoryPackage.RAW_LOCATION__LOCATION:
			return LOCATION_EDEFAULT == null ? location != null : !LOCATION_EDEFAULT.equals(location);
		case IRepositoryPackage.RAW_LOCATION__UPDATE_PENDING:
			return updatePending != UPDATE_PENDING_EDEFAULT;
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
		switch (operationID) {
		case IRepositoryPackage.RAW_LOCATION___GET_RESOURCE:
			return getResource();
		case IRepositoryPackage.RAW_LOCATION___GET_INPUT_STREAM:
			return getInputStream();
		}
		return super.eInvoke(operationID, arguments);
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

		final StringBuffer result = new StringBuffer(super.toString());
		result.append(" (location: ");
		result.append(location);
		result.append(", updatePending: ");
		result.append(updatePending);
		result.append(')');
		return result.toString();
	}

} // RawLocationImpl
