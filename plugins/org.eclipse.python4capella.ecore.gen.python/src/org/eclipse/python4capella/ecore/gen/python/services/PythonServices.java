/**
 *  Copyright (c) 2023 THALES GLOBAL SERVICES
 *  This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License 2.0
 *  which accompanies this distribution, and is available at
 *  https://www.eclipse.org/legal/epl-2.0/
 *
 *  SPDX-License-Identifier: EPL-2.0
 *
 *  Contributors:
 *       Obeo - Initial API and implementation
 */
package org.eclipse.python4capella.ecore.gen.python.services;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.impl.BasicEObjectImpl;

/**
 * Python utilty class.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public final class PythonServices {

	private PythonServices() {
		// nothing to do here
	}

	/**
	 * Converts camel case name to Python name.
	 * 
	 * @param name the name to convert
	 * @return the Python name
	 */
	public static String getPythonName(String name) {
		final StringBuilder res = new StringBuilder();

		for (int i = 0; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isUpperCase(c)) {
				res.append("_");
				res.append(Character.toLowerCase(c));
			} else {
				res.append(c);
			}
		}

		return res.toString();
	}

	/**
	 * Gets the instance {@link Class} name for the given {@link EClass}.
	 * 
	 * @param eCls the {@link EClass}
	 * @return the instance {@link Class} name for the given {@link EClass}
	 */
	public static String getInstanceClassName(EClass eCls) {
		final String res;

		final Class<?> cls = eCls.getInstanceClass();
		if (cls != null) {
			res = cls.getCanonicalName();
		} else if (eCls.getInstanceClassName() != null) {
			res = eCls.getInstanceClassName();
		} else if (eCls.getInstanceTypeName() != null) {
			res = eCls.getInstanceTypeName();
		} else {
			res = "";
		}

		return res;
	}

	/**
	 * Gets the Python type name of the given {@link EClassifier}.
	 * 
	 * @param eClassifier the {@link EClassifier}
	 * @return the Python type name of the given {@link EClassifier}
	 */
	public static String getPythonName(EClassifier eClassifier) {
		final String res;

		if (eClassifier instanceof EEnum) {
			res = eClassifier.getName();
		} else if (eClassifier instanceof EDataType) {
			final String pythonName = getPythonName((EDataType) eClassifier);
			if (pythonName != null) {
				res = pythonName;
			} else {
				res = eClassifier.getName();
			}
		} else {
			res = eClassifier.getName();
		}

		return res;
	}

	private static String getPythonName(EDataType dataType) {
		final String res;

		final String instanceClassName = dataType.getInstanceClassName();
		if (instanceClassName != null) {
			switch (instanceClassName) {
				case "java.lang.String":
					res = "str";
					break;

				case "boolean":
				case "java.lang.Boolean":
					res = "bool";
					break;

				case "float":
				case "java.lang.Float":
				case "double":
				case "java.lang.Double":
					res = "float";
					break;

				case "int":
				case "java.lang.Integer":
				case "long":
				case "java.lang.Long":
				case "short":
				case "java.lang.Short":
				case "char":
				case "java.lang.Character":
					res = "int";
					break;

				default:
					res = null;
					break;
			}
		} else if (dataType.eIsProxy() && dataType instanceof BasicEObjectImpl) {
			final String uri = ((BasicEObjectImpl) dataType).eProxyURI().toString();
			final int index = uri.lastIndexOf("#//");
			if (index >= 0) {
				final String type = uri.substring(index + "#//".length());
				switch (type) {
					case "EString":
						res = "str";
						break;

					case "EBoolean":
						res = "bool";
						break;

					case "EFloat":
					case "EFloatObject":
					case "EDouble":
					case "EDoubleObject":
						res = "float";
						break;

					case "EInt":
					case "EIntegerObject":
					case "ELong":
					case "ELongObject":
					case "EShort":
					case "EShortObject":
					case "EChar":
					case "ECharacterObject":
						res = "int";
						break;

					default:
						res = null;
						break;
				}
			} else {
				res = null;
			}
		} else {
			res = null;
		}

		return res;
	}

	/**
	 * Tells if the given {@link EDataType} needs a Python class.
	 * 
	 * @param dataType the {@link EDataType}
	 * @return <code>true</code> if the given {@link EDataType} needs a Python
	 *         class, <code>false</code> otherwise
	 */
	public static boolean needPythonClass(EDataType dataType) {
		return getPythonName(dataType) == null;
	}

}
