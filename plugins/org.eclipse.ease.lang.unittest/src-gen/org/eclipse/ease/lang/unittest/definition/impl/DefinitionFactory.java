/**
 */
package org.eclipse.ease.lang.unittest.definition.impl;

import java.util.Map;

import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.lang.unittest.definition.*;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.impl.EFactoryImpl;
import org.eclipse.emf.ecore.plugin.EcorePlugin;

/**
 * <!-- begin-user-doc --> An implementation of the model <b>Factory</b>. <!-- end-user-doc -->
 * @generated
 */
public class DefinitionFactory extends EFactoryImpl implements IDefinitionFactory {
	/**
	 * Creates the default factory implementation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public static IDefinitionFactory init() {
		try {
			IDefinitionFactory theDefinitionFactory = (IDefinitionFactory)EPackage.Registry.INSTANCE.getEFactory(IDefinitionPackage.eNS_URI);
			if (theDefinitionFactory != null) {
				return theDefinitionFactory;
			}
		}
		catch (Exception exception) {
			EcorePlugin.INSTANCE.log(exception);
		}
		return new DefinitionFactory();
	}

	/**
	 * Creates an instance of the factory.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public DefinitionFactory() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EObject create(EClass eClass) {
		switch (eClass.getClassifierID()) {
			case IDefinitionPackage.TEST_SUITE_DEFINITION: return createTestSuiteDefinition();
			case IDefinitionPackage.VARIABLE: return createVariable();
			case IDefinitionPackage.FLAG_TO_STRING_MAP: return (EObject)createFlagToStringMap();
			case IDefinitionPackage.CODE: return createCode();
			default:
				throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object createFromString(EDataType eDataType, String initialValue) {
		switch (eDataType.getClassifierID()) {
			case IDefinitionPackage.FLAG:
				return createFlagFromString(eDataType, initialValue);
			case IDefinitionPackage.PATH:
				return createPathFromString(eDataType, initialValue);
			default:
				throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String convertToString(EDataType eDataType, Object instanceValue) {
		switch (eDataType.getClassifierID()) {
			case IDefinitionPackage.FLAG:
				return convertFlagToString(eDataType, instanceValue);
			case IDefinitionPackage.PATH:
				return convertPathToString(eDataType, instanceValue);
			default:
				throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ITestSuiteDefinition createTestSuiteDefinition() {
		TestSuiteDefinition testSuiteDefinition = new TestSuiteDefinition();
		return testSuiteDefinition;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IVariable createVariable() {
		Variable variable = new Variable();
		return variable;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public Map.Entry<Flag, String> createFlagToStringMap() {
		FlagToStringMap flagToStringMap = new FlagToStringMap();
		return flagToStringMap;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ICode createCode() {
		Code code = new Code();
		return code;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public Flag createFlagFromString(EDataType eDataType, String initialValue) {
		Flag result = Flag.get(initialValue);
		if (result == null) throw new IllegalArgumentException("The value '" + initialValue + "' is not a valid enumerator of '" + eDataType.getName() + "'");
		return result;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public String convertFlagToString(EDataType eDataType, Object instanceValue) {
		return instanceValue == null ? null : instanceValue.toString();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	public IPath createPathFromString(EDataType eDataType, String initialValue) {
		return new Path(initialValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	public String convertPathToString(EDataType eDataType, Object instanceValue) {
		if (instanceValue instanceof IPath)
			return ((IPath) instanceValue).toPortableString();

		return super.convertToString(eDataType, instanceValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public IDefinitionPackage getDefinitionPackage() {
		return (IDefinitionPackage)getEPackage();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @deprecated
	 * @generated
	 */
	@Deprecated
	public static IDefinitionPackage getPackage() {
		return IDefinitionPackage.eINSTANCE;
	}

} // DefinitionFactory
