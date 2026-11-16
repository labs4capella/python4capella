/**
 */
package org.eclipse.ease.lang.unittest.definition.impl;

import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.util.Collection;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.lang.unittest.definition.Flag;
import org.eclipse.ease.lang.unittest.definition.ICode;
import org.eclipse.ease.lang.unittest.definition.IDefinitionFactory;
import org.eclipse.ease.lang.unittest.definition.IDefinitionPackage;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.definition.IVariable;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.common.util.EMap;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;
import org.eclipse.emf.ecore.util.EDataTypeUniqueEList;
import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.EcoreEMap;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc --> An implementation of the model object '<em><b>Test Suite Definition</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getName <em>Name</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getDescription <em>Description</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getIncludeFilter <em>Include Filter</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getExcludeFilter <em>Exclude Filter</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getDisabledResources <em>Disabled Resources</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getVariables <em>Variables</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getCustomCode <em>Custom Code</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getFlags <em>Flags</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getVersion <em>Version</em>}</li>
 *   <li>{@link org.eclipse.ease.lang.unittest.definition.impl.TestSuiteDefinition#getResource <em>Resource</em>}</li>
 * </ul>
 *
 * @generated
 */
public class TestSuiteDefinition extends MinimalEObjectImpl.Container implements ITestSuiteDefinition {
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
	 * The default value of the '{@link #getIncludeFilter() <em>Include Filter</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getIncludeFilter()
	 * @generated
	 * @ordered
	 */
	protected static final String INCLUDE_FILTER_EDEFAULT = "";

	/**
	 * The cached value of the '{@link #getIncludeFilter() <em>Include Filter</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getIncludeFilter()
	 * @generated
	 * @ordered
	 */
	protected String includeFilter = INCLUDE_FILTER_EDEFAULT;

	/**
	 * The default value of the '{@link #getExcludeFilter() <em>Exclude Filter</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getExcludeFilter()
	 * @generated
	 * @ordered
	 */
	protected static final String EXCLUDE_FILTER_EDEFAULT = "";

	/**
	 * The cached value of the '{@link #getExcludeFilter() <em>Exclude Filter</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getExcludeFilter()
	 * @generated
	 * @ordered
	 */
	protected String excludeFilter = EXCLUDE_FILTER_EDEFAULT;

	/**
	 * The cached value of the '{@link #getDisabledResources() <em>Disabled Resources</em>}' attribute list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getDisabledResources()
	 * @generated
	 * @ordered
	 */
	protected EList<IPath> disabledResources;

	/**
	 * The cached value of the '{@link #getVariables() <em>Variables</em>}' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getVariables()
	 * @generated
	 * @ordered
	 */
	protected EList<IVariable> variables;

	/**
	 * The cached value of the '{@link #getCustomCode() <em>Custom Code</em>}' containment reference list.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getCustomCode()
	 * @generated
	 * @ordered
	 */
	protected EList<ICode> customCode;

	/**
	 * The cached value of the '{@link #getFlags() <em>Flags</em>}' map.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getFlags()
	 * @generated
	 * @ordered
	 */
	protected EMap<Flag, String> flags;

	/**
	 * The default value of the '{@link #getVersion() <em>Version</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getVersion()
	 * @generated
	 * @ordered
	 */
	protected static final String VERSION_EDEFAULT = "";

	/**
	 * The cached value of the '{@link #getVersion() <em>Version</em>}' attribute.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #getVersion()
	 * @generated
	 * @ordered
	 */
	protected String version = VERSION_EDEFAULT;

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
	protected TestSuiteDefinition() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IDefinitionPackage.Literals.TEST_SUITE_DEFINITION;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public String getNameGen() {
		return name;
	}

	/**
	 * @generated NOT
	 */
	@Override
	public String getName() {
		final String definitionName = getNameGen();

		if (definitionName != null)
			return definitionName;

		if (getResource() instanceof IFile)
			return ((IFile) getResource()).getName();

		if (getResource() instanceof File)
			return ((File) getResource()).getName();

		return null;
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
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__NAME, oldName, name));
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
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__DESCRIPTION, oldDescription, description));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getIncludeFilter() {
		return includeFilter;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setIncludeFilter(String newIncludeFilter) {
		String oldIncludeFilter = includeFilter;
		includeFilter = newIncludeFilter;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__INCLUDE_FILTER, oldIncludeFilter, includeFilter));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getExcludeFilter() {
		return excludeFilter;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setExcludeFilter(String newExcludeFilter) {
		String oldExcludeFilter = excludeFilter;
		excludeFilter = newExcludeFilter;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__EXCLUDE_FILTER, oldExcludeFilter, excludeFilter));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<IPath> getDisabledResources() {
		if (disabledResources == null) {
			disabledResources = new EDataTypeUniqueEList<IPath>(IPath.class, this, IDefinitionPackage.TEST_SUITE_DEFINITION__DISABLED_RESOURCES);
		}
		return disabledResources;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<IVariable> getVariables() {
		if (variables == null) {
			variables = new EObjectContainmentEList<IVariable>(IVariable.class, this, IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES);
		}
		return variables;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EList<ICode> getCustomCode() {
		if (customCode == null) {
			customCode = new EObjectContainmentEList<ICode>(ICode.class, this, IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE);
		}
		return customCode;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EMap<Flag, String> getFlags() {
		if (flags == null) {
			flags = new EcoreEMap<Flag,String>(IDefinitionPackage.Literals.FLAG_TO_STRING_MAP, FlagToStringMap.class, this, IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS);
		}
		return flags;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getVersion() {
		return version;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setVersion(String newVersion) {
		String oldVersion = version;
		version = newVersion;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__VERSION, oldVersion, version));
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
			eNotify(new ENotificationImpl(this, Notification.SET, IDefinitionPackage.TEST_SUITE_DEFINITION__RESOURCE, oldResource, resource));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public ICode getCustomCode(String location) {
		for (final ICode code : getCustomCode()) {
			if (code.getLocation().equals(location))
				return code;
		}

		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public IVariable getVariable(String name) {
		for (final IVariable variable : getVariables()) {
			if (variable.getName().equals(name))
				return variable;
		}

		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES:
				return ((InternalEList<?>)getVariables()).basicRemove(otherEnd, msgs);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE:
				return ((InternalEList<?>)getCustomCode()).basicRemove(otherEnd, msgs);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS:
				return ((InternalEList<?>)getFlags()).basicRemove(otherEnd, msgs);
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
			case IDefinitionPackage.TEST_SUITE_DEFINITION__NAME:
				return getName();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DESCRIPTION:
				return getDescription();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__INCLUDE_FILTER:
				return getIncludeFilter();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__EXCLUDE_FILTER:
				return getExcludeFilter();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DISABLED_RESOURCES:
				return getDisabledResources();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES:
				return getVariables();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE:
				return getCustomCode();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS:
				if (coreType) return getFlags();
				else return getFlags().map();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VERSION:
				return getVersion();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__RESOURCE:
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
			case IDefinitionPackage.TEST_SUITE_DEFINITION__NAME:
				setName((String)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DESCRIPTION:
				setDescription((String)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__INCLUDE_FILTER:
				setIncludeFilter((String)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__EXCLUDE_FILTER:
				setExcludeFilter((String)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DISABLED_RESOURCES:
				getDisabledResources().clear();
				getDisabledResources().addAll((Collection<? extends IPath>)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES:
				getVariables().clear();
				getVariables().addAll((Collection<? extends IVariable>)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE:
				getCustomCode().clear();
				getCustomCode().addAll((Collection<? extends ICode>)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS:
				((EStructuralFeature.Setting)getFlags()).set(newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VERSION:
				setVersion((String)newValue);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__RESOURCE:
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
			case IDefinitionPackage.TEST_SUITE_DEFINITION__NAME:
				setName(NAME_EDEFAULT);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DESCRIPTION:
				setDescription(DESCRIPTION_EDEFAULT);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__INCLUDE_FILTER:
				setIncludeFilter(INCLUDE_FILTER_EDEFAULT);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__EXCLUDE_FILTER:
				setExcludeFilter(EXCLUDE_FILTER_EDEFAULT);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DISABLED_RESOURCES:
				getDisabledResources().clear();
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES:
				getVariables().clear();
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE:
				getCustomCode().clear();
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS:
				getFlags().clear();
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VERSION:
				setVersion(VERSION_EDEFAULT);
				return;
			case IDefinitionPackage.TEST_SUITE_DEFINITION__RESOURCE:
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
			case IDefinitionPackage.TEST_SUITE_DEFINITION__NAME:
				return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DESCRIPTION:
				return DESCRIPTION_EDEFAULT == null ? description != null : !DESCRIPTION_EDEFAULT.equals(description);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__INCLUDE_FILTER:
				return INCLUDE_FILTER_EDEFAULT == null ? includeFilter != null : !INCLUDE_FILTER_EDEFAULT.equals(includeFilter);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__EXCLUDE_FILTER:
				return EXCLUDE_FILTER_EDEFAULT == null ? excludeFilter != null : !EXCLUDE_FILTER_EDEFAULT.equals(excludeFilter);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__DISABLED_RESOURCES:
				return disabledResources != null && !disabledResources.isEmpty();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VARIABLES:
				return variables != null && !variables.isEmpty();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__CUSTOM_CODE:
				return customCode != null && !customCode.isEmpty();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__FLAGS:
				return flags != null && !flags.isEmpty();
			case IDefinitionPackage.TEST_SUITE_DEFINITION__VERSION:
				return VERSION_EDEFAULT == null ? version != null : !VERSION_EDEFAULT.equals(version);
			case IDefinitionPackage.TEST_SUITE_DEFINITION__RESOURCE:
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
			case IDefinitionPackage.TEST_SUITE_DEFINITION___GET_CUSTOM_CODE__STRING:
				return getCustomCode((String)arguments.get(0));
			case IDefinitionPackage.TEST_SUITE_DEFINITION___GET_VARIABLE__STRING:
				return getVariable((String)arguments.get(0));
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
		result.append(" (name: ");
		result.append(name);
		result.append(", description: ");
		result.append(description);
		result.append(", includeFilter: ");
		result.append(includeFilter);
		result.append(", excludeFilter: ");
		result.append(excludeFilter);
		result.append(", disabledResources: ");
		result.append(disabledResources);
		result.append(", version: ");
		result.append(version);
		result.append(", resource: ");
		result.append(resource);
		result.append(')');
		return result.toString();
	}

	/**
	 * @generated NOT
	 */
	@Override
	@SuppressWarnings("unchecked")
	public <T> T getFlag(Flag identifier, T defaultValue) {
		final String value = getFlags().get(identifier);
		if (value == null)
			return defaultValue;

		if (defaultValue instanceof String)
			return (T) value.toString();

		if (defaultValue instanceof Boolean)
			return (T) new Boolean(Boolean.parseBoolean(value.toString()));

		if (defaultValue instanceof Integer) {
			try {
				return (T) new Integer(Integer.parseInt(value.toString()));
			} catch (final NumberFormatException e) {
			}
		}

		return null;
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void setVariable(String identifier, String content) {
		getOrCreateVariable(identifier).setContent(content);
	}

	/**
	 * @generated NOT
	 */
	private IVariable getOrCreateVariable(String identifier) {
		IVariable variable = getVariable(identifier);

		if (variable == null) {
			variable = IDefinitionFactory.eINSTANCE.createVariable();
			variable.setFullName(new Path(identifier));

			getVariables().add(variable);
		}

		return variable;
	}

	/**
	 * @generated NOT
	 */
	@Override
	public void setFlag(String identifier, String value) {
		final Flag flag = Flag.getByName(identifier);
		if (flag == null)
			throw new IllegalArgumentException(String.format("Flag %s is unknown", identifier));

		getFlags().put(flag, value);
	}

} // TestSuiteDefinition
