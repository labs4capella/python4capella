/**
 */
package org.eclipse.ease.lang.unittest.definition;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.eclipse.emf.common.util.Enumerator;

/**
 * <!-- begin-user-doc --> A representation of the literals of the enumeration '<em><b>Flag</b></em>', and utility methods for working with them. <!--
 * end-user-doc -->
 * @see org.eclipse.ease.lang.unittest.definition.IDefinitionPackage#getFlag()
 * @model
 * @generated
 */
public enum Flag implements Enumerator {
	/**
	 * The '<em><b>UNDEFINED</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #UNDEFINED_VALUE
	 * @generated
	 * @ordered
	 */
	UNDEFINED(0, "UNDEFINED", "UNDEFINED"),
	/**
	 * The '<em><b>THREAD COUNT</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #THREAD_COUNT_VALUE
	 * @generated
	 * @ordered
	 */
	THREAD_COUNT(1, "THREAD_COUNT", "THREAD_COUNT"),

	/**
	 * The '<em><b>PROMOTE FAILURE TO ERROR</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #PROMOTE_FAILURE_TO_ERROR_VALUE
	 * @generated
	 * @ordered
	 */
	PROMOTE_FAILURE_TO_ERROR(2, "PROMOTE_FAILURE_TO_ERROR", "PROMOTE_FAILURE_TO_ERROR"),
	/**
	 * The '<em><b>STOP SUITE ON ERROR</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #STOP_SUITE_ON_ERROR_VALUE
	 * @generated
	 * @ordered
	 */
	STOP_SUITE_ON_ERROR(3, "STOP_SUITE_ON_ERROR", "STOP_SUITE_ON_ERROR"),
	/**
	 * The '<em><b>RUN TEARDOWN ON ERROR</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #RUN_TEARDOWN_ON_ERROR_VALUE
	 * @generated
	 * @ordered
	 */
	RUN_TEARDOWN_ON_ERROR(4, "RUN_TEARDOWN_ON_ERROR", "RUN_TEARDOWN_ON_ERROR"),
	/**
	 * The '<em><b>PREFERRED ENGINE ID</b></em>' literal object.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @see #PREFERRED_ENGINE_ID_VALUE
	 * @generated
	 * @ordered
	 */
	PREFERRED_ENGINE_ID(5, "PREFERRED_ENGINE_ID", "PREFERRED_ENGINE_ID");

	/**
	 * The '<em><b>UNDEFINED</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>UNDEFINED</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #UNDEFINED
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int UNDEFINED_VALUE = 0;

	/**
	 * The '<em><b>THREAD COUNT</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>THREAD COUNT</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #THREAD_COUNT
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int THREAD_COUNT_VALUE = 1;

	/**
	 * The '<em><b>PROMOTE FAILURE TO ERROR</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>PROMOTE FAILURE TO ERROR</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #PROMOTE_FAILURE_TO_ERROR
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int PROMOTE_FAILURE_TO_ERROR_VALUE = 2;

	/**
	 * The '<em><b>STOP SUITE ON ERROR</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>STOP SUITE ON ERROR</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #STOP_SUITE_ON_ERROR
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int STOP_SUITE_ON_ERROR_VALUE = 3;

	/**
	 * The '<em><b>RUN TEARDOWN ON ERROR</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>RUN TEARDOWN ON ERROR</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #RUN_TEARDOWN_ON_ERROR
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int RUN_TEARDOWN_ON_ERROR_VALUE = 4;

	/**
	 * The '<em><b>PREFERRED ENGINE ID</b></em>' literal value.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of '<em><b>PREFERRED ENGINE ID</b></em>' literal object isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @see #PREFERRED_ENGINE_ID
	 * @model
	 * @generated
	 * @ordered
	 */
	public static final int PREFERRED_ENGINE_ID_VALUE = 5;

	/**
	 * An array of all the '<em><b>Flag</b></em>' enumerators.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private static final Flag[] VALUES_ARRAY = new Flag[] {
			UNDEFINED,
			THREAD_COUNT,
			PROMOTE_FAILURE_TO_ERROR,
			STOP_SUITE_ON_ERROR,
			RUN_TEARDOWN_ON_ERROR,
			PREFERRED_ENGINE_ID,
		};

	/**
	 * A public read-only list of all the '<em><b>Flag</b></em>' enumerators.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	public static final List<Flag> VALUES = Collections.unmodifiableList(Arrays.asList(VALUES_ARRAY));

	/**
	 * Returns the '<em><b>Flag</b></em>' literal with the specified literal value.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @param literal the literal.
	 * @return the matching enumerator or <code>null</code>.
	 * @generated
	 */
	public static Flag get(String literal) {
		for (int i = 0; i < VALUES_ARRAY.length; ++i) {
			Flag result = VALUES_ARRAY[i];
			if (result.toString().equals(literal)) {
				return result;
			}
		}
		return null;
	}

	/**
	 * Returns the '<em><b>Flag</b></em>' literal with the specified name.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @param name the name.
	 * @return the matching enumerator or <code>null</code>.
	 * @generated
	 */
	public static Flag getByName(String name) {
		for (int i = 0; i < VALUES_ARRAY.length; ++i) {
			Flag result = VALUES_ARRAY[i];
			if (result.getName().equals(name)) {
				return result;
			}
		}
		return null;
	}

	/**
	 * Returns the '<em><b>Flag</b></em>' literal with the specified integer value.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @param value the integer value.
	 * @return the matching enumerator or <code>null</code>.
	 * @generated
	 */
	public static Flag get(int value) {
		switch (value) {
			case UNDEFINED_VALUE: return UNDEFINED;
			case THREAD_COUNT_VALUE: return THREAD_COUNT;
			case PROMOTE_FAILURE_TO_ERROR_VALUE: return PROMOTE_FAILURE_TO_ERROR;
			case STOP_SUITE_ON_ERROR_VALUE: return STOP_SUITE_ON_ERROR;
			case RUN_TEARDOWN_ON_ERROR_VALUE: return RUN_TEARDOWN_ON_ERROR;
			case PREFERRED_ENGINE_ID_VALUE: return PREFERRED_ENGINE_ID;
		}
		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private final int value;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private final String name;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private final String literal;

	/**
	 * Only this class can construct instances.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	private Flag(int value, String name, String literal) {
		this.value = value;
		this.name = name;
		this.literal = literal;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public int getValue() {
	  return value;
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
	public String getLiteral() {
	  return literal;
	}

	/**
	 * Returns the literal value of the enumerator, which is its string representation.
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		return literal;
	}

} // Flag
