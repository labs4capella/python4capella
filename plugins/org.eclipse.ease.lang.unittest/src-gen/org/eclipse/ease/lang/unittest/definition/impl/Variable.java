/**
 */
package org.eclipse.ease.lang.unittest.definition.impl;

import java.lang.reflect.InvocationTargetException;

import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.lang.unittest.definition.IDefinitionPackage;
import org.eclipse.ease.lang.unittest.definition.IVariable;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Variable</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.Variable#getFullName <em>Full Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.Variable#getContent <em>Content</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.Variable#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.Variable#getEnumProviderID <em>Enum Provider ID</em>}</li>
 * </ul>
 *
 * @generated
 */
public class Variable extends MinimalEObjectImpl.Container implements IVariable {
	/**
	 * The default value of the '{@link #getFullName() <em>Full Name</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getFullName()
	 * @generated
	 * @ordered
	 */
	protected static final IPath FULL_NAME_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getFullName() <em>Full Name</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getFullName()
	 * @generated
	 * @ordered
	 */
	protected IPath fullName = FULL_NAME_EDEFAULT;

	/**
	 * The default value of the '{@link #getContent() <em>Content</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getContent()
	 * @generated
	 * @ordered
	 */
	protected static final String CONTENT_EDEFAULT = "";

	/**
	 * The cached value of the '{@link #getContent() <em>Content</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getContent()
	 * @generated
	 * @ordered
	 */
	protected String content = CONTENT_EDEFAULT;

	/**
	 * The default value of the '{@link #getDescription() <em>Description</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDescription()
	 * @generated
	 * @ordered
	 */
	protected static final String DESCRIPTION_EDEFAULT = "";

	/**
	 * The cached value of the '{@link #getDescription() <em>Description</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDescription()
	 * @generated
	 * @ordered
	 */
	protected String description = DESCRIPTION_EDEFAULT;

	/**
	 * The default value of the '{@link #getEnumProviderID() <em>Enum Provider ID</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEnumProviderID()
	 * @generated
	 * @ordered
	 */
	protected static final String ENUM_PROVIDER_ID_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getEnumProviderID() <em>Enum Provider ID</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getEnumProviderID()
	 * @generated
	 * @ordered
	 */
	protected String enumProviderID = ENUM_PROVIDER_ID_EDEFAULT;

	/**
	 * This is true if the Enum Provider ID attribute has been set.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	protected boolean enumProviderIDESet;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	protected Variable() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IDefinitionPackage.Literals.VARIABLE;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IPath getFullName() {
		return fullName;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setFullName(IPath newFullName) {
		IPath oldFullName = fullName;
		fullName = newFullName;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.VARIABLE__FULL_NAME, oldFullName, fullName));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated NOT
	 */
	@Override
	public String getName() {
		return getFullName().lastSegment();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getContent() {
		return content;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setContent(String newContent) {
		String oldContent = content;
		content = newContent;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.VARIABLE__CONTENT, oldContent, content));
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
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.VARIABLE__DESCRIPTION, oldDescription, description));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getEnumProviderID() {
		return enumProviderID;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setEnumProviderID(String newEnumProviderID) {
		String oldEnumProviderID = enumProviderID;
		enumProviderID = newEnumProviderID;
		boolean oldEnumProviderIDESet = enumProviderIDESet;
		enumProviderIDESet = true;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID, oldEnumProviderID, enumProviderID, !oldEnumProviderIDESet));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void unsetEnumProviderID() {
		String oldEnumProviderID = enumProviderID;
		boolean oldEnumProviderIDESet = enumProviderIDESet;
		enumProviderID = ENUM_PROVIDER_ID_EDEFAULT;
		enumProviderIDESet = false;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.UNSET, IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID, oldEnumProviderID, ENUM_PROVIDER_ID_EDEFAULT, oldEnumProviderIDESet));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean isSetEnumProviderID() {
		return enumProviderIDESet;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated NOT
	 */
	@Override
	public IPath getPath() {
		return getFullName().removeLastSegments(1);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case IDefinitionPackage.VARIABLE__FULL_NAME:
				return getFullName();
			case IDefinitionPackage.VARIABLE__CONTENT:
				return getContent();
			case IDefinitionPackage.VARIABLE__DESCRIPTION:
				return getDescription();
			case IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID:
				return getEnumProviderID();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case IDefinitionPackage.VARIABLE__FULL_NAME:
				setFullName((IPath)newValue);
				return;
			case IDefinitionPackage.VARIABLE__CONTENT:
				setContent((String)newValue);
				return;
			case IDefinitionPackage.VARIABLE__DESCRIPTION:
				setDescription((String)newValue);
				return;
			case IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID:
				setEnumProviderID((String)newValue);
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
			case IDefinitionPackage.VARIABLE__FULL_NAME:
				setFullName(FULL_NAME_EDEFAULT);
				return;
			case IDefinitionPackage.VARIABLE__CONTENT:
				setContent(CONTENT_EDEFAULT);
				return;
			case IDefinitionPackage.VARIABLE__DESCRIPTION:
				setDescription(DESCRIPTION_EDEFAULT);
				return;
			case IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID:
				unsetEnumProviderID();
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
			case IDefinitionPackage.VARIABLE__FULL_NAME:
				return FULL_NAME_EDEFAULT == null ? fullName != null : !FULL_NAME_EDEFAULT.equals(fullName);
			case IDefinitionPackage.VARIABLE__CONTENT:
				return CONTENT_EDEFAULT == null ? content != null : !CONTENT_EDEFAULT.equals(content);
			case IDefinitionPackage.VARIABLE__DESCRIPTION:
				return DESCRIPTION_EDEFAULT == null ? description != null : !DESCRIPTION_EDEFAULT.equals(description);
			case IDefinitionPackage.VARIABLE__ENUM_PROVIDER_ID:
				return isSetEnumProviderID();
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
			case IDefinitionPackage.VARIABLE___GET_NAME:
				return getName();
			case IDefinitionPackage.VARIABLE___GET_PATH:
				return getPath();
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
		result.append(" (fullName: ");
		result.append(fullName);
		result.append(", content: ");
		result.append(content);
		result.append(", description: ");
		result.append(description);
		result.append(", enumProviderID: ");
		if (enumProviderIDESet) result.append(enumProviderID); else result.append("<unset>");
		result.append(')');
		return result.toString();
	}

} // Variable
