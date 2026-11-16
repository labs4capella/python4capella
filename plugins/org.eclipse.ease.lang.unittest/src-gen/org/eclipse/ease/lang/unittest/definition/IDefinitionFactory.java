/**
 */
package org.eclipse.ease.lang.unittest.definition;

import org.eclipse.emf.ecore.EFactory;

/**
 * <!-- begin-user-doc --> The <b>Factory</b> for the model. It provides a create method for each non-abstract class of the model. <!-- end-user-doc -->
 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage
 * @generated
 */
public interface IDefinitionFactory extends EFactory {
	/**
	 * The singleton instance of the factory.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	IDefinitionFactory eINSTANCE = org.eclipse.ease.lang.unittest.definition.impl.DefinitionFactory.init();

	/**
	 * Returns a new object of class '<em>Test Suite Definition</em>'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return a new object of class '<em>Test Suite Definition</em>'.
	 * @generated
	 */
	ITestSuiteDefinition createTestSuiteDefinition();

	/**
	 * Returns a new object of class '<em>Variable</em>'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return a new object of class '<em>Variable</em>'.
	 * @generated
	 */
	IVariable createVariable();

	/**
	 * Returns a new object of class '<em>Code</em>'.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return a new object of class '<em>Code</em>'.
	 * @generated
	 */
	ICode createCode();

	/**
	 * Returns the package supported by this factory.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @return the package supported by this factory.
	 * @generated
	 */
	IDefinitionPackage getDefinitionPackage();

} // IDefinitionFactory
