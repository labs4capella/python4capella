/**
 */
package org.eclipse.ease.lang.unittest.runtime;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

/**
 * <!-- begin-user-doc -->
 * The <b>Package</b> for the model.
 * It contains accessors for the meta objects to represent
 * <ul>
 *   <li>each class,</li>
 *   <li>each feature of each class,</li>
 *   <li>each operation of each class,</li>
 *   <li>each enum,</li>
 *   <li>and each data type</li>
 * </ul>
 * <!-- end-user-doc -->
 * @see org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory
 * @model kind="package"
 * @generated
 */
public interface IRuntimePackage extends EPackage {
	/**
	 * The package name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNAME = "runtime";

	/**
	 * The package namespace URI.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_URI = "http://eclipse.org/ease/unittest/runtime";

	/**
	 * The package namespace name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_PREFIX = "runtime";

	/**
	 * The singleton instance of the package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	IRuntimePackage eINSTANCE = org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage.init();

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity <em>Test Entity</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestEntity
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestEntity()
	 * @generated
	 */
	int TEST_ENTITY = 0;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__DESCRIPTION = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__NAME = 1;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__ENTITY_STATUS = 2;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__END_TIMESTAMP = 3;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__START_TIMESTAMP = 4;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__PARENT = 5;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__METADATA = 6;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__DURATION = 7;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__RESULTS = 8;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__ESTIMATED_DURATION = 9;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY__TERMINATED = 10;

	/**
	 * The number of structural features of the '<em>Test Entity</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY_FEATURE_COUNT = 11;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_STATUS = 0;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_ROOT = 1;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___HAS_ERROR = 2;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_TEST_SUITE = 3;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_RESOURCE = 4;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___RESET = 5;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY = 6;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_WORST_RESULT = 7;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE = 8;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_RESULTS__TESTSTATUS = 9;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___GET_FULL_PATH = 10;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___SET_DISABLED__STRING = 11;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY___IS_DISABLED = 12;

	/**
	 * The number of operations of the '<em>Test Entity</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_ENTITY_OPERATION_COUNT = 13;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestContainer <em>Test Container</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestContainer
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestContainer()
	 * @generated
	 */
	int TEST_CONTAINER = 1;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__DESCRIPTION = TEST_ENTITY__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__NAME = TEST_ENTITY__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__ENTITY_STATUS = TEST_ENTITY__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__END_TIMESTAMP = TEST_ENTITY__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__START_TIMESTAMP = TEST_ENTITY__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__PARENT = TEST_ENTITY__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__METADATA = TEST_ENTITY__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__DURATION = TEST_ENTITY__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__RESULTS = TEST_ENTITY__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__ESTIMATED_DURATION = TEST_ENTITY__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__TERMINATED = TEST_ENTITY__TERMINATED;

	/**
	 * The feature id for the '<em><b>Children</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__CHILDREN = TEST_ENTITY_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER__RESOURCE = TEST_ENTITY_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Test Container</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER_FEATURE_COUNT = TEST_ENTITY_FEATURE_COUNT + 2;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_STATUS = TEST_ENTITY___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_ROOT = TEST_ENTITY___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___HAS_ERROR = TEST_ENTITY___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_TEST_SUITE = TEST_ENTITY___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_RESOURCE = TEST_ENTITY___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___RESET = TEST_ENTITY___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___RUN__ITESTEXECUTIONSTRATEGY = TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_WORST_RESULT = TEST_ENTITY___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_RESULTS__TESTSTATUS = TEST_ENTITY___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_FULL_PATH = TEST_ENTITY___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___SET_DISABLED__STRING = TEST_ENTITY___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___IS_DISABLED = TEST_ENTITY___IS_DISABLED;

	/**
	 * The operation id for the '<em>Get Test</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_TEST__STRING = TEST_ENTITY_OPERATION_COUNT + 0;

	/**
	 * The operation id for the '<em>Get Child Containers</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER___GET_CHILD_CONTAINERS = TEST_ENTITY_OPERATION_COUNT + 1;

	/**
	 * The number of operations of the '<em>Test Container</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CONTAINER_OPERATION_COUNT = TEST_ENTITY_OPERATION_COUNT + 2;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.Test <em>Test</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.Test
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTest()
	 * @generated
	 */
	int TEST = 2;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__DESCRIPTION = TEST_ENTITY__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__NAME = TEST_ENTITY__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__ENTITY_STATUS = TEST_ENTITY__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__END_TIMESTAMP = TEST_ENTITY__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__START_TIMESTAMP = TEST_ENTITY__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__PARENT = TEST_ENTITY__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__METADATA = TEST_ENTITY__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__DURATION = TEST_ENTITY__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__RESULTS = TEST_ENTITY__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__ESTIMATED_DURATION = TEST_ENTITY__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__TERMINATED = TEST_ENTITY__TERMINATED;

	/**
	 * The feature id for the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__STACK_TRACE = TEST_ENTITY_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Duration Limit</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST__DURATION_LIMIT = TEST_ENTITY_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Test</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FEATURE_COUNT = TEST_ENTITY_FEATURE_COUNT + 2;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_STATUS = TEST_ENTITY___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_ROOT = TEST_ENTITY___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___HAS_ERROR = TEST_ENTITY___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_TEST_SUITE = TEST_ENTITY___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_RESOURCE = TEST_ENTITY___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___RESET = TEST_ENTITY___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___RUN__ITESTEXECUTIONSTRATEGY = TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_WORST_RESULT = TEST_ENTITY___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_RESULTS__TESTSTATUS = TEST_ENTITY___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___GET_FULL_PATH = TEST_ENTITY___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___SET_DISABLED__STRING = TEST_ENTITY___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST___IS_DISABLED = TEST_ENTITY___IS_DISABLED;

	/**
	 * The number of operations of the '<em>Test</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_OPERATION_COUNT = TEST_ENTITY_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestSuite <em>Test Suite</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestSuite
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestSuite()
	 * @generated
	 */
	int TEST_SUITE = 3;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__DESCRIPTION = TEST_CONTAINER__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__NAME = TEST_CONTAINER__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__ENTITY_STATUS = TEST_CONTAINER__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__END_TIMESTAMP = TEST_CONTAINER__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__START_TIMESTAMP = TEST_CONTAINER__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__PARENT = TEST_CONTAINER__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__METADATA = TEST_CONTAINER__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__DURATION = TEST_CONTAINER__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__RESULTS = TEST_CONTAINER__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__ESTIMATED_DURATION = TEST_CONTAINER__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__TERMINATED = TEST_CONTAINER__TERMINATED;

	/**
	 * The feature id for the '<em><b>Children</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__CHILDREN = TEST_CONTAINER__CHILDREN;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__RESOURCE = TEST_CONTAINER__RESOURCE;

	/**
	 * The feature id for the '<em><b>Active Tests</b></em>' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__ACTIVE_TESTS = TEST_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Definition</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__DEFINITION = TEST_CONTAINER_FEATURE_COUNT + 1;

	/**
	 * The feature id for the '<em><b>Master Engine</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE__MASTER_ENGINE = TEST_CONTAINER_FEATURE_COUNT + 2;

	/**
	 * The number of structural features of the '<em>Test Suite</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_FEATURE_COUNT = TEST_CONTAINER_FEATURE_COUNT + 3;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_STATUS = TEST_CONTAINER___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_ROOT = TEST_CONTAINER___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___HAS_ERROR = TEST_CONTAINER___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_TEST_SUITE = TEST_CONTAINER___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_RESOURCE = TEST_CONTAINER___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___RESET = TEST_CONTAINER___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___RUN__ITESTEXECUTIONSTRATEGY = TEST_CONTAINER___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_WORST_RESULT = TEST_CONTAINER___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_CONTAINER___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_RESULTS__TESTSTATUS = TEST_CONTAINER___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_FULL_PATH = TEST_CONTAINER___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___SET_DISABLED__STRING = TEST_CONTAINER___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___IS_DISABLED = TEST_CONTAINER___IS_DISABLED;

	/**
	 * The operation id for the '<em>Get Test</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_TEST__STRING = TEST_CONTAINER___GET_TEST__STRING;

	/**
	 * The operation id for the '<em>Get Child Containers</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE___GET_CHILD_CONTAINERS = TEST_CONTAINER___GET_CHILD_CONTAINERS;

	/**
	 * The number of operations of the '<em>Test Suite</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_SUITE_OPERATION_COUNT = TEST_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestFolder <em>Test Folder</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestFolder
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestFolder()
	 * @generated
	 */
	int TEST_FOLDER = 4;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__DESCRIPTION = TEST_CONTAINER__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__NAME = TEST_CONTAINER__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__ENTITY_STATUS = TEST_CONTAINER__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__END_TIMESTAMP = TEST_CONTAINER__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__START_TIMESTAMP = TEST_CONTAINER__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__PARENT = TEST_CONTAINER__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__METADATA = TEST_CONTAINER__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__DURATION = TEST_CONTAINER__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__RESULTS = TEST_CONTAINER__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__ESTIMATED_DURATION = TEST_CONTAINER__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__TERMINATED = TEST_CONTAINER__TERMINATED;

	/**
	 * The feature id for the '<em><b>Children</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__CHILDREN = TEST_CONTAINER__CHILDREN;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER__RESOURCE = TEST_CONTAINER__RESOURCE;

	/**
	 * The number of structural features of the '<em>Test Folder</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER_FEATURE_COUNT = TEST_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_STATUS = TEST_CONTAINER___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_ROOT = TEST_CONTAINER___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___HAS_ERROR = TEST_CONTAINER___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_TEST_SUITE = TEST_CONTAINER___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_RESOURCE = TEST_CONTAINER___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___RESET = TEST_CONTAINER___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___RUN__ITESTEXECUTIONSTRATEGY = TEST_CONTAINER___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_WORST_RESULT = TEST_CONTAINER___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_CONTAINER___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_RESULTS__TESTSTATUS = TEST_CONTAINER___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_FULL_PATH = TEST_CONTAINER___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___SET_DISABLED__STRING = TEST_CONTAINER___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___IS_DISABLED = TEST_CONTAINER___IS_DISABLED;

	/**
	 * The operation id for the '<em>Get Test</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_TEST__STRING = TEST_CONTAINER___GET_TEST__STRING;

	/**
	 * The operation id for the '<em>Get Child Containers</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER___GET_CHILD_CONTAINERS = TEST_CONTAINER___GET_CHILD_CONTAINERS;

	/**
	 * The number of operations of the '<em>Test Folder</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FOLDER_OPERATION_COUNT = TEST_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestClass <em>Test Class</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestClass
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestClass()
	 * @generated
	 */
	int TEST_CLASS = 5;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__DESCRIPTION = TEST_CONTAINER__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__NAME = TEST_CONTAINER__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__ENTITY_STATUS = TEST_CONTAINER__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__END_TIMESTAMP = TEST_CONTAINER__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__START_TIMESTAMP = TEST_CONTAINER__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__PARENT = TEST_CONTAINER__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__METADATA = TEST_CONTAINER__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__DURATION = TEST_CONTAINER__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__RESULTS = TEST_CONTAINER__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__ESTIMATED_DURATION = TEST_CONTAINER__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__TERMINATED = TEST_CONTAINER__TERMINATED;

	/**
	 * The feature id for the '<em><b>Children</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__CHILDREN = TEST_CONTAINER__CHILDREN;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__RESOURCE = TEST_CONTAINER__RESOURCE;

	/**
	 * The feature id for the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS__STACK_TRACE = TEST_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>Test Class</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS_FEATURE_COUNT = TEST_CONTAINER_FEATURE_COUNT + 1;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_STATUS = TEST_CONTAINER___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_ROOT = TEST_CONTAINER___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___HAS_ERROR = TEST_CONTAINER___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_TEST_SUITE = TEST_CONTAINER___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_RESOURCE = TEST_CONTAINER___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___RESET = TEST_CONTAINER___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___RUN__ITESTEXECUTIONSTRATEGY = TEST_CONTAINER___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_WORST_RESULT = TEST_CONTAINER___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_CONTAINER___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_RESULTS__TESTSTATUS = TEST_CONTAINER___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_FULL_PATH = TEST_CONTAINER___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___SET_DISABLED__STRING = TEST_CONTAINER___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___IS_DISABLED = TEST_CONTAINER___IS_DISABLED;

	/**
	 * The operation id for the '<em>Get Test</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_TEST__STRING = TEST_CONTAINER___GET_TEST__STRING;

	/**
	 * The operation id for the '<em>Get Child Containers</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS___GET_CHILD_CONTAINERS = TEST_CONTAINER___GET_CHILD_CONTAINERS;

	/**
	 * The number of operations of the '<em>Test Class</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_CLASS_OPERATION_COUNT = TEST_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.StackTraceContainer <em>Stack Trace Container</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.StackTraceContainer
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getStackTraceContainer()
	 * @generated
	 */
	int STACK_TRACE_CONTAINER = 8;

	/**
	 * The feature id for the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int STACK_TRACE_CONTAINER__STACK_TRACE = 0;

	/**
	 * The number of structural features of the '<em>Stack Trace Container</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int STACK_TRACE_CONTAINER_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Stack Trace Container</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int STACK_TRACE_CONTAINER_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestResult <em>Test Result</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestResult
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestResult()
	 * @generated
	 */
	int TEST_RESULT = 6;

	/**
	 * The feature id for the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_RESULT__STACK_TRACE = STACK_TRACE_CONTAINER__STACK_TRACE;

	/**
	 * The feature id for the '<em><b>Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_RESULT__STATUS = STACK_TRACE_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Message</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_RESULT__MESSAGE = STACK_TRACE_CONTAINER_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Test Result</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_RESULT_FEATURE_COUNT = STACK_TRACE_CONTAINER_FEATURE_COUNT + 2;

	/**
	 * The number of operations of the '<em>Test Result</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_RESULT_OPERATION_COUNT = STACK_TRACE_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestFile <em>Test File</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestFile
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestFile()
	 * @generated
	 */
	int TEST_FILE = 7;

	/**
	 * The feature id for the '<em><b>Description</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__DESCRIPTION = TEST_CONTAINER__DESCRIPTION;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__NAME = TEST_CONTAINER__NAME;

	/**
	 * The feature id for the '<em><b>Entity Status</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__ENTITY_STATUS = TEST_CONTAINER__ENTITY_STATUS;

	/**
	 * The feature id for the '<em><b>End Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__END_TIMESTAMP = TEST_CONTAINER__END_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Start Timestamp</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__START_TIMESTAMP = TEST_CONTAINER__START_TIMESTAMP;

	/**
	 * The feature id for the '<em><b>Parent</b></em>' container reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__PARENT = TEST_CONTAINER__PARENT;

	/**
	 * The feature id for the '<em><b>Metadata</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__METADATA = TEST_CONTAINER__METADATA;

	/**
	 * The feature id for the '<em><b>Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__DURATION = TEST_CONTAINER__DURATION;

	/**
	 * The feature id for the '<em><b>Results</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__RESULTS = TEST_CONTAINER__RESULTS;

	/**
	 * The feature id for the '<em><b>Estimated Duration</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__ESTIMATED_DURATION = TEST_CONTAINER__ESTIMATED_DURATION;

	/**
	 * The feature id for the '<em><b>Terminated</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__TERMINATED = TEST_CONTAINER__TERMINATED;

	/**
	 * The feature id for the '<em><b>Children</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__CHILDREN = TEST_CONTAINER__CHILDREN;

	/**
	 * The feature id for the '<em><b>Resource</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__RESOURCE = TEST_CONTAINER__RESOURCE;

	/**
	 * The feature id for the '<em><b>Insertion Order</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE__INSERTION_ORDER = TEST_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>Test File</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE_FEATURE_COUNT = TEST_CONTAINER_FEATURE_COUNT + 1;

	/**
	 * The operation id for the '<em>Get Status</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_STATUS = TEST_CONTAINER___GET_STATUS;

	/**
	 * The operation id for the '<em>Get Root</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_ROOT = TEST_CONTAINER___GET_ROOT;

	/**
	 * The operation id for the '<em>Has Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___HAS_ERROR = TEST_CONTAINER___HAS_ERROR;

	/**
	 * The operation id for the '<em>Get Test Suite</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_TEST_SUITE = TEST_CONTAINER___GET_TEST_SUITE;

	/**
	 * The operation id for the '<em>Get Resource</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_RESOURCE = TEST_CONTAINER___GET_RESOURCE;

	/**
	 * The operation id for the '<em>Reset</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___RESET = TEST_CONTAINER___RESET;

	/**
	 * The operation id for the '<em>Run</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___RUN__ITESTEXECUTIONSTRATEGY = TEST_CONTAINER___RUN__ITESTEXECUTIONSTRATEGY;

	/**
	 * The operation id for the '<em>Get Worst Result</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_WORST_RESULT = TEST_CONTAINER___GET_WORST_RESULT;

	/**
	 * The operation id for the '<em>Add Error</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___ADD_ERROR__STRING_SCRIPTSTACKTRACE = TEST_CONTAINER___ADD_ERROR__STRING_SCRIPTSTACKTRACE;

	/**
	 * The operation id for the '<em>Get Results</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_RESULTS__TESTSTATUS = TEST_CONTAINER___GET_RESULTS__TESTSTATUS;

	/**
	 * The operation id for the '<em>Get Full Path</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_FULL_PATH = TEST_CONTAINER___GET_FULL_PATH;

	/**
	 * The operation id for the '<em>Set Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___SET_DISABLED__STRING = TEST_CONTAINER___SET_DISABLED__STRING;

	/**
	 * The operation id for the '<em>Is Disabled</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___IS_DISABLED = TEST_CONTAINER___IS_DISABLED;

	/**
	 * The operation id for the '<em>Get Test</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_TEST__STRING = TEST_CONTAINER___GET_TEST__STRING;

	/**
	 * The operation id for the '<em>Get Child Containers</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE___GET_CHILD_CONTAINERS = TEST_CONTAINER___GET_CHILD_CONTAINERS;

	/**
	 * The number of operations of the '<em>Test File</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int TEST_FILE_OPERATION_COUNT = TEST_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.Metadata <em>Metadata</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.Metadata
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getMetadata()
	 * @generated
	 */
	int METADATA = 9;

	/**
	 * The feature id for the '<em><b>Stack Trace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int METADATA__STACK_TRACE = STACK_TRACE_CONTAINER__STACK_TRACE;

	/**
	 * The feature id for the '<em><b>Key</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int METADATA__KEY = STACK_TRACE_CONTAINER_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Value</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int METADATA__VALUE = STACK_TRACE_CONTAINER_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Metadata</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int METADATA_FEATURE_COUNT = STACK_TRACE_CONTAINER_FEATURE_COUNT + 2;

	/**
	 * The number of operations of the '<em>Metadata</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int METADATA_OPERATION_COUNT = STACK_TRACE_CONTAINER_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link org.eclipse.ease.lang.unittest.runtime.TestStatus <em>Test Status</em>}' enum.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestStatus()
	 * @generated
	 */
	int TEST_STATUS = 10;

	/**
	 * The meta object id for the '<em>Script Engine</em>' data type.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.IScriptEngine
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getScriptEngine()
	 * @generated
	 */
	int SCRIPT_ENGINE = 11;

	/**
	 * The meta object id for the '<em>Throwable</em>' data type.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see java.lang.Throwable
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getThrowable()
	 * @generated
	 */
	int THROWABLE = 12;

	/**
	 * The meta object id for the '<em>Script Stack Trace</em>' data type.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.debugging.ScriptStackTrace
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getScriptStackTrace()
	 * @generated
	 */
	int SCRIPT_STACK_TRACE = 13;


	/**
	 * The meta object id for the '<em>Test Execution Strategy</em>' data type.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestExecutionStrategy()
	 * @generated
	 */
	int TEST_EXECUTION_STRATEGY = 14;


	/**
	 * The meta object id for the '<em>Path</em>' data type.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see org.eclipse.core.runtime.IPath
	 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getPath()
	 * @generated
	 */
	int PATH = 15;


	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity <em>Test Entity</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Entity</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity
	 * @generated
	 */
	EClass getTestEntity();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDescription <em>Description</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Description</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDescription()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_Description();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getName()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_Name();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEntityStatus <em>Entity Status</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Entity Status</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEntityStatus()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_EntityStatus();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEndTimestamp <em>End Timestamp</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>End Timestamp</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEndTimestamp()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_EndTimestamp();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStartTimestamp <em>Start Timestamp</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Start Timestamp</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStartTimestamp()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_StartTimestamp();

	/**
	 * Returns the meta object for the container reference '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent <em>Parent</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the container reference '<em>Parent</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getParent()
	 * @see #getTestEntity()
	 * @generated
	 */
	EReference getTestEntity_Parent();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getMetadata <em>Metadata</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Metadata</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getMetadata()
	 * @see #getTestEntity()
	 * @generated
	 */
	EReference getTestEntity_Metadata();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDuration <em>Duration</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Duration</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getDuration()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_Duration();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResults <em>Results</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Results</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResults()
	 * @see #getTestEntity()
	 * @generated
	 */
	EReference getTestEntity_Results();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEstimatedDuration <em>Estimated Duration</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Estimated Duration</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getEstimatedDuration()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_EstimatedDuration();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#isTerminated <em>Terminated</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Terminated</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#isTerminated()
	 * @see #getTestEntity()
	 * @generated
	 */
	EAttribute getTestEntity_Terminated();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStatus() <em>Get Status</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Status</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getStatus()
	 * @generated
	 */
	EOperation getTestEntity__GetStatus();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getRoot() <em>Get Root</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Root</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getRoot()
	 * @generated
	 */
	EOperation getTestEntity__GetRoot();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#hasError() <em>Has Error</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Has Error</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#hasError()
	 * @generated
	 */
	EOperation getTestEntity__HasError();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getTestSuite() <em>Get Test Suite</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Test Suite</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getTestSuite()
	 * @generated
	 */
	EOperation getTestEntity__GetTestSuite();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResource() <em>Get Resource</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Resource</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResource()
	 * @generated
	 */
	EOperation getTestEntity__GetResource();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#reset() <em>Reset</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Reset</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#reset()
	 * @generated
	 */
	EOperation getTestEntity__Reset();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#run(org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy) <em>Run</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Run</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#run(org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy)
	 * @generated
	 */
	EOperation getTestEntity__Run__ITestExecutionStrategy();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getWorstResult() <em>Get Worst Result</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Worst Result</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getWorstResult()
	 * @generated
	 */
	EOperation getTestEntity__GetWorstResult();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#addError(java.lang.String, org.eclipse.ease.debugging.ScriptStackTrace) <em>Add Error</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Add Error</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#addError(java.lang.String, org.eclipse.ease.debugging.ScriptStackTrace)
	 * @generated
	 */
	EOperation getTestEntity__AddError__String_ScriptStackTrace();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResults(org.eclipse.ease.lang.unittest.runtime.TestStatus) <em>Get Results</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Results</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getResults(org.eclipse.ease.lang.unittest.runtime.TestStatus)
	 * @generated
	 */
	EOperation getTestEntity__GetResults__TestStatus();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#getFullPath() <em>Get Full Path</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Full Path</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#getFullPath()
	 * @generated
	 */
	EOperation getTestEntity__GetFullPath();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#setDisabled(java.lang.String) <em>Set Disabled</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Set Disabled</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#setDisabled(java.lang.String)
	 * @generated
	 */
	EOperation getTestEntity__SetDisabled__String();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestEntity#isDisabled() <em>Is Disabled</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Is Disabled</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestEntity#isDisabled()
	 * @generated
	 */
	EOperation getTestEntity__IsDisabled();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer <em>Test Container</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Container</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer
	 * @generated
	 */
	EClass getTestContainer();

	/**
	 * Returns the meta object for the containment reference list '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildren <em>Children</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Children</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildren()
	 * @see #getTestContainer()
	 * @generated
	 */
	EReference getTestContainer_Children();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getResource <em>Resource</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Resource</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer#getResource()
	 * @see #getTestContainer()
	 * @generated
	 */
	EAttribute getTestContainer_Resource();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getTest(java.lang.String) <em>Get Test</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Test</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer#getTest(java.lang.String)
	 * @generated
	 */
	EOperation getTestContainer__GetTest__String();

	/**
	 * Returns the meta object for the '{@link org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildContainers() <em>Get Child Containers</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Get Child Containers</em>' operation.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestContainer#getChildContainers()
	 * @generated
	 */
	EOperation getTestContainer__GetChildContainers();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITest <em>Test</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITest
	 * @generated
	 */
	EClass getTest();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITest#getDurationLimit <em>Duration Limit</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Duration Limit</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITest#getDurationLimit()
	 * @see #getTest()
	 * @generated
	 */
	EAttribute getTest_DurationLimit();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite <em>Test Suite</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Suite</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestSuite
	 * @generated
	 */
	EClass getTestSuite();

	/**
	 * Returns the meta object for the reference list '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getActiveTests <em>Active Tests</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference list '<em>Active Tests</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestSuite#getActiveTests()
	 * @see #getTestSuite()
	 * @generated
	 */
	EReference getTestSuite_ActiveTests();

	/**
	 * Returns the meta object for the reference '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getDefinition <em>Definition</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Definition</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestSuite#getDefinition()
	 * @see #getTestSuite()
	 * @generated
	 */
	EReference getTestSuite_Definition();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestSuite#getMasterEngine <em>Master Engine</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Master Engine</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestSuite#getMasterEngine()
	 * @see #getTestSuite()
	 * @generated
	 */
	EAttribute getTestSuite_MasterEngine();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestFolder <em>Test Folder</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Folder</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestFolder
	 * @generated
	 */
	EClass getTestFolder();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestClass <em>Test Class</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Class</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestClass
	 * @generated
	 */
	EClass getTestClass();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestResult <em>Test Result</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test Result</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestResult
	 * @generated
	 */
	EClass getTestResult();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getStatus <em>Status</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Status</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestResult#getStatus()
	 * @see #getTestResult()
	 * @generated
	 */
	EAttribute getTestResult_Status();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestResult#getMessage <em>Message</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Message</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestResult#getMessage()
	 * @see #getTestResult()
	 * @generated
	 */
	EAttribute getTestResult_Message();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.ITestFile <em>Test File</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Test File</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestFile
	 * @generated
	 */
	EClass getTestFile();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.ITestFile#getInsertionOrder <em>Insertion Order</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Insertion Order</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.ITestFile#getInsertionOrder()
	 * @see #getTestFile()
	 * @generated
	 */
	EAttribute getTestFile_InsertionOrder();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer <em>Stack Trace Container</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Stack Trace Container</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer
	 * @generated
	 */
	EClass getStackTraceContainer();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer#getStackTrace <em>Stack Trace</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Stack Trace</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer#getStackTrace()
	 * @see #getStackTraceContainer()
	 * @generated
	 */
	EAttribute getStackTraceContainer_StackTrace();

	/**
	 * Returns the meta object for class '{@link org.eclipse.ease.lang.unittest.runtime.IMetadata <em>Metadata</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Metadata</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.IMetadata
	 * @generated
	 */
	EClass getMetadata();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.IMetadata#getKey <em>Key</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Key</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.IMetadata#getKey()
	 * @see #getMetadata()
	 * @generated
	 */
	EAttribute getMetadata_Key();

	/**
	 * Returns the meta object for the attribute '{@link org.eclipse.ease.lang.unittest.runtime.IMetadata#getValue <em>Value</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Value</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.IMetadata#getValue()
	 * @see #getMetadata()
	 * @generated
	 */
	EAttribute getMetadata_Value();

	/**
	 * Returns the meta object for enum '{@link org.eclipse.ease.lang.unittest.runtime.TestStatus <em>Test Status</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for enum '<em>Test Status</em>'.
	 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
	 * @generated
	 */
	EEnum getTestStatus();

	/**
	 * Returns the meta object for data type '{@link org.eclipse.ease.IScriptEngine <em>Script Engine</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Script Engine</em>'.
	 * @see org.eclipse.ease.IScriptEngine
	 * @model instanceClass="org.eclipse.ease.IScriptEngine" serializeable="false"
	 * @generated
	 */
	EDataType getScriptEngine();

	/**
	 * Returns the meta object for data type '{@link java.lang.Throwable <em>Throwable</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Throwable</em>'.
	 * @see java.lang.Throwable
	 * @model instanceClass="java.lang.Throwable" serializeable="false"
	 * @generated
	 */
	EDataType getThrowable();

	/**
	 * Returns the meta object for data type '{@link org.eclipse.ease.debugging.ScriptStackTrace <em>Script Stack Trace</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Script Stack Trace</em>'.
	 * @see org.eclipse.ease.debugging.ScriptStackTrace
	 * @model instanceClass="org.eclipse.ease.debugging.ScriptStackTrace" serializeable="false"
	 * @generated
	 */
	EDataType getScriptStackTrace();

	/**
	 * Returns the meta object for data type '{@link org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy <em>Test Execution Strategy</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Test Execution Strategy</em>'.
	 * @see org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy
	 * @model instanceClass="org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy" serializeable="false"
	 * @generated
	 */
	EDataType getTestExecutionStrategy();

	/**
	 * Returns the meta object for data type '{@link org.eclipse.core.runtime.IPath <em>Path</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for data type '<em>Path</em>'.
	 * @see org.eclipse.core.runtime.IPath
	 * @model instanceClass="org.eclipse.core.runtime.IPath" serializeable="false"
	 * @generated
	 */
	EDataType getPath();

	/**
	 * Returns the factory that creates the instances of the model.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	IRuntimeFactory getRuntimeFactory();

	/**
	 * <!-- begin-user-doc -->
	 * Defines literals for the meta objects that represent
	 * <ul>
	 *   <li>each class,</li>
	 *   <li>each feature of each class,</li>
	 *   <li>each operation of each class,</li>
	 *   <li>each enum,</li>
	 *   <li>and each data type</li>
	 * </ul>
	 * <!-- end-user-doc -->
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestEntity <em>Test Entity</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestEntity
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestEntity()
		 * @generated
		 */
		EClass TEST_ENTITY = eINSTANCE.getTestEntity();

		/**
		 * The meta object literal for the '<em><b>Description</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__DESCRIPTION = eINSTANCE.getTestEntity_Description();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__NAME = eINSTANCE.getTestEntity_Name();

		/**
		 * The meta object literal for the '<em><b>Entity Status</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__ENTITY_STATUS = eINSTANCE.getTestEntity_EntityStatus();

		/**
		 * The meta object literal for the '<em><b>End Timestamp</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__END_TIMESTAMP = eINSTANCE.getTestEntity_EndTimestamp();

		/**
		 * The meta object literal for the '<em><b>Start Timestamp</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__START_TIMESTAMP = eINSTANCE.getTestEntity_StartTimestamp();

		/**
		 * The meta object literal for the '<em><b>Parent</b></em>' container reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_ENTITY__PARENT = eINSTANCE.getTestEntity_Parent();

		/**
		 * The meta object literal for the '<em><b>Metadata</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_ENTITY__METADATA = eINSTANCE.getTestEntity_Metadata();

		/**
		 * The meta object literal for the '<em><b>Duration</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__DURATION = eINSTANCE.getTestEntity_Duration();

		/**
		 * The meta object literal for the '<em><b>Results</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_ENTITY__RESULTS = eINSTANCE.getTestEntity_Results();

		/**
		 * The meta object literal for the '<em><b>Estimated Duration</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__ESTIMATED_DURATION = eINSTANCE.getTestEntity_EstimatedDuration();

		/**
		 * The meta object literal for the '<em><b>Terminated</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_ENTITY__TERMINATED = eINSTANCE.getTestEntity_Terminated();

		/**
		 * The meta object literal for the '<em><b>Get Status</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_STATUS = eINSTANCE.getTestEntity__GetStatus();

		/**
		 * The meta object literal for the '<em><b>Get Root</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_ROOT = eINSTANCE.getTestEntity__GetRoot();

		/**
		 * The meta object literal for the '<em><b>Has Error</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___HAS_ERROR = eINSTANCE.getTestEntity__HasError();

		/**
		 * The meta object literal for the '<em><b>Get Test Suite</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_TEST_SUITE = eINSTANCE.getTestEntity__GetTestSuite();

		/**
		 * The meta object literal for the '<em><b>Get Resource</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_RESOURCE = eINSTANCE.getTestEntity__GetResource();

		/**
		 * The meta object literal for the '<em><b>Reset</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___RESET = eINSTANCE.getTestEntity__Reset();

		/**
		 * The meta object literal for the '<em><b>Run</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___RUN__ITESTEXECUTIONSTRATEGY = eINSTANCE.getTestEntity__Run__ITestExecutionStrategy();

		/**
		 * The meta object literal for the '<em><b>Get Worst Result</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_WORST_RESULT = eINSTANCE.getTestEntity__GetWorstResult();

		/**
		 * The meta object literal for the '<em><b>Add Error</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___ADD_ERROR__STRING_SCRIPTSTACKTRACE = eINSTANCE.getTestEntity__AddError__String_ScriptStackTrace();

		/**
		 * The meta object literal for the '<em><b>Get Results</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_RESULTS__TESTSTATUS = eINSTANCE.getTestEntity__GetResults__TestStatus();

		/**
		 * The meta object literal for the '<em><b>Get Full Path</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___GET_FULL_PATH = eINSTANCE.getTestEntity__GetFullPath();

		/**
		 * The meta object literal for the '<em><b>Set Disabled</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___SET_DISABLED__STRING = eINSTANCE.getTestEntity__SetDisabled__String();

		/**
		 * The meta object literal for the '<em><b>Is Disabled</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_ENTITY___IS_DISABLED = eINSTANCE.getTestEntity__IsDisabled();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestContainer <em>Test Container</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestContainer
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestContainer()
		 * @generated
		 */
		EClass TEST_CONTAINER = eINSTANCE.getTestContainer();

		/**
		 * The meta object literal for the '<em><b>Children</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_CONTAINER__CHILDREN = eINSTANCE.getTestContainer_Children();

		/**
		 * The meta object literal for the '<em><b>Resource</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_CONTAINER__RESOURCE = eINSTANCE.getTestContainer_Resource();

		/**
		 * The meta object literal for the '<em><b>Get Test</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_CONTAINER___GET_TEST__STRING = eINSTANCE.getTestContainer__GetTest__String();

		/**
		 * The meta object literal for the '<em><b>Get Child Containers</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation TEST_CONTAINER___GET_CHILD_CONTAINERS = eINSTANCE.getTestContainer__GetChildContainers();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.Test <em>Test</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.Test
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTest()
		 * @generated
		 */
		EClass TEST = eINSTANCE.getTest();

		/**
		 * The meta object literal for the '<em><b>Duration Limit</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST__DURATION_LIMIT = eINSTANCE.getTest_DurationLimit();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestSuite <em>Test Suite</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestSuite
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestSuite()
		 * @generated
		 */
		EClass TEST_SUITE = eINSTANCE.getTestSuite();

		/**
		 * The meta object literal for the '<em><b>Active Tests</b></em>' reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_SUITE__ACTIVE_TESTS = eINSTANCE.getTestSuite_ActiveTests();

		/**
		 * The meta object literal for the '<em><b>Definition</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference TEST_SUITE__DEFINITION = eINSTANCE.getTestSuite_Definition();

		/**
		 * The meta object literal for the '<em><b>Master Engine</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_SUITE__MASTER_ENGINE = eINSTANCE.getTestSuite_MasterEngine();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestFolder <em>Test Folder</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestFolder
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestFolder()
		 * @generated
		 */
		EClass TEST_FOLDER = eINSTANCE.getTestFolder();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestClass <em>Test Class</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestClass
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestClass()
		 * @generated
		 */
		EClass TEST_CLASS = eINSTANCE.getTestClass();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestResult <em>Test Result</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestResult
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestResult()
		 * @generated
		 */
		EClass TEST_RESULT = eINSTANCE.getTestResult();

		/**
		 * The meta object literal for the '<em><b>Status</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_RESULT__STATUS = eINSTANCE.getTestResult_Status();

		/**
		 * The meta object literal for the '<em><b>Message</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_RESULT__MESSAGE = eINSTANCE.getTestResult_Message();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.TestFile <em>Test File</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.TestFile
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestFile()
		 * @generated
		 */
		EClass TEST_FILE = eINSTANCE.getTestFile();

		/**
		 * The meta object literal for the '<em><b>Insertion Order</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute TEST_FILE__INSERTION_ORDER = eINSTANCE.getTestFile_InsertionOrder();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.StackTraceContainer <em>Stack Trace Container</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.StackTraceContainer
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getStackTraceContainer()
		 * @generated
		 */
		EClass STACK_TRACE_CONTAINER = eINSTANCE.getStackTraceContainer();

		/**
		 * The meta object literal for the '<em><b>Stack Trace</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute STACK_TRACE_CONTAINER__STACK_TRACE = eINSTANCE.getStackTraceContainer_StackTrace();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.impl.Metadata <em>Metadata</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.Metadata
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getMetadata()
		 * @generated
		 */
		EClass METADATA = eINSTANCE.getMetadata();

		/**
		 * The meta object literal for the '<em><b>Key</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute METADATA__KEY = eINSTANCE.getMetadata_Key();

		/**
		 * The meta object literal for the '<em><b>Value</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute METADATA__VALUE = eINSTANCE.getMetadata_Value();

		/**
		 * The meta object literal for the '{@link org.eclipse.ease.lang.unittest.runtime.TestStatus <em>Test Status</em>}' enum.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.runtime.TestStatus
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestStatus()
		 * @generated
		 */
		EEnum TEST_STATUS = eINSTANCE.getTestStatus();

		/**
		 * The meta object literal for the '<em>Script Engine</em>' data type.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.IScriptEngine
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getScriptEngine()
		 * @generated
		 */
		EDataType SCRIPT_ENGINE = eINSTANCE.getScriptEngine();

		/**
		 * The meta object literal for the '<em>Throwable</em>' data type.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see java.lang.Throwable
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getThrowable()
		 * @generated
		 */
		EDataType THROWABLE = eINSTANCE.getThrowable();

		/**
		 * The meta object literal for the '<em>Script Stack Trace</em>' data type.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.debugging.ScriptStackTrace
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getScriptStackTrace()
		 * @generated
		 */
		EDataType SCRIPT_STACK_TRACE = eINSTANCE.getScriptStackTrace();

		/**
		 * The meta object literal for the '<em>Test Execution Strategy</em>' data type.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.ease.lang.unittest.execution.ITestExecutionStrategy
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getTestExecutionStrategy()
		 * @generated
		 */
		EDataType TEST_EXECUTION_STRATEGY = eINSTANCE.getTestExecutionStrategy();

		/**
		 * The meta object literal for the '<em>Path</em>' data type.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see org.eclipse.core.runtime.IPath
		 * @see org.eclipse.ease.lang.unittest.runtime.impl.RuntimePackage#getPath()
		 * @generated
		 */
		EDataType PATH = eINSTANCE.getPath();

	}

} //IRuntimePackage
