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

import java.util.Collection;
import java.util.HashSet;

import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.ease.ui.scripts.repository.IStorage;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;
import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Storage</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.StorageImpl#getEntries <em>Entries</em>}</li>
 * </ul>
 *
 * @generated
 */
public class StorageImpl extends MinimalEObjectImpl.Container implements IStorage {
	/**
	 * The cached value of the '{@link #getEntries() <em>Entries</em>}' containment reference list. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getEntries()
	 * @generated
	 * @ordered
	 */
	protected EList<IScriptLocation> entries;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	protected StorageImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRepositoryPackage.Literals.STORAGE;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public EList<IScriptLocation> getEntries() {
		if (entries == null) {
			entries = new EObjectContainmentEList<>(IScriptLocation.class, this, IRepositoryPackage.STORAGE__ENTRIES);
		}
		return entries;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case IRepositoryPackage.STORAGE__ENTRIES:
			return ((InternalEList<?>) getEntries()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
		case IRepositoryPackage.STORAGE__ENTRIES:
			return getEntries();
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
		case IRepositoryPackage.STORAGE__ENTRIES:
			getEntries().clear();
			getEntries().addAll((Collection<? extends IScriptLocation>) newValue);
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
		case IRepositoryPackage.STORAGE__ENTRIES:
			getEntries().clear();
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
		case IRepositoryPackage.STORAGE__ENTRIES:
			return (entries != null) && !entries.isEmpty();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * @generated NOT
	 */
	@Override
	public Collection<IScript> getScripts() {
		final HashSet<IScript> scripts = new HashSet<>();

		for (final IScriptLocation entry : new HashSet<>(getEntries()))
			scripts.addAll(entry.getScripts());

		return scripts;
	}
} // StorageImpl
