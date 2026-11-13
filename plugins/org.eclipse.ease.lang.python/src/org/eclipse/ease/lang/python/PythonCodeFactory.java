/*******************************************************************************
 * Copyright (c) 2013, 2016 Atos and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Arthur Daussy - initial implementation
 *     Christian Pontesegger - simplified to use base class
 *******************************************************************************/
package org.eclipse.ease.lang.python;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

import org.eclipse.ease.AbstractCodeFactory;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ScriptResult;
import org.eclipse.ease.modules.EnvironmentModule;
import org.eclipse.ease.modules.IEnvironment;
import org.eclipse.ease.modules.ModuleHelper;
import org.eclipse.ease.tools.StringTools;

public class PythonCodeFactory extends AbstractCodeFactory {

	private static final List<String> RESERVED_KEYWORDS = Arrays.asList("and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else",
			"except", "exec", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "not", "or", "pass", "print", "raise", "return", "try",
			"while", "with", "yield",

			// built in functions
			"__import__", "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", "callable", "chr", "classmethod", "compile", "complex", "delattr",
			"dict", "dir", "divmod", "enumerate", "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help",
			"hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list", "locals", "map", "max", "memoryview", "min", "next", "object",
			"oct", "open", "ord", "pow", "print", "property", "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", "str",
			"sum", "super", "tuple", "type", "vars", "zip");
	/**
	 * List of Java primitive types as they need to be handled differently from normal classes when getting their py4j representation.
	 *
	 * bytes are handled differently as Python has native bytearray type.
	 */
	private static final List<Class<?>> PRIMITIVES = Arrays.asList(short.class, int.class, long.class, float.class, double.class, boolean.class, char.class);

	/**
	 * Returns the Python (py4j) identifier for the given class.
	 *
	 * @param cls
	 *            Class to get py4j identifier for.
	 * @return py4j class identifier.
	 */
	protected static String getPythonClassIdentifier(Class<?> cls) {
		if (PRIMITIVES.contains(cls)) {
			return String.format("gateway.jvm.%s", cls.getName());
		} else {
			return cls.getName();
		}
	}

	private static String toSafeNameStatic(String name) {
		while (RESERVED_KEYWORDS.contains(name))
			return toSafeNameStatic(name + "_");

		return name;
	}

	private static String indent(String code, String indentation) {
		if (code.isEmpty())
			return code;

		return indentation + code.replaceAll("\n", "\n" + indentation).trim() + "\n";
	}

	/**
	 * Create wrapper code to convert all array parameters to actual Java arrays.
	 *
	 * @param parameters
	 *            List of parameters to create array conversion for.
	 * @return Wrapper code for performing array conversion.
	 */
	protected static String buildArrayConversions(List<Parameter> parameters) {
		return parameters.stream().map(PythonCodeFactory::buildArrayConversion).collect(Collectors.joining(StringTools.LINE_DELIMITER));
	}

	/**
	 * Create wrapper code to convert an array parameter to actual Java array.
	 *
	 * Generated code will have the following look: {@code
	 * 	try:
	 * 		tmp = gateway.new_array([array type], len([value to be converted]))
	 *      for index, value in enumerate([value to be converted]):
	 *          tmp[index] = value
	 *      [value to be converted] = tmp
	 *  except NameError:
	 *      pass
	 *  }
	 *
	 * @param parameter
	 *            Parameter to create conversion code for.
	 * @return Wrapper code for performing array conversion.
	 */
	protected static String buildArrayConversion(Parameter parameter) {
		final StringBuilder builder = new StringBuilder();
		if (parameter.getClazz().isArray()) {
			final String arrayType = getPythonClassIdentifier(parameter.getClazz().getComponentType());
			final String variableName = toSafeNameStatic(parameter.getName());
			builder.append(String.format("if %s is not None:", variableName)).append(StringTools.LINE_DELIMITER);
			builder.append("    try:").append(StringTools.LINE_DELIMITER);
			builder.append(String.format("        tmp = gateway.new_array(%s, len(%s))", arrayType, variableName)).append(StringTools.LINE_DELIMITER);
			builder.append(String.format("        for index, value in enumerate(%s):", variableName)).append(StringTools.LINE_DELIMITER);
			builder.append("            tmp[index] = value").append(StringTools.LINE_DELIMITER);
			builder.append(String.format("        %s =  tmp", variableName)).append(StringTools.LINE_DELIMITER);
			builder.append("    except NameError:").append(StringTools.LINE_DELIMITER);
			builder.append("        pass").append(StringTools.LINE_DELIMITER);
		}
		return builder.toString();
	}

	/**
	 * Convert integer parameters to double when the Java interface requires double/float. When integers are passed in python, Py4J does not automatically
	 * convert these numbers to double/float if required. Therefore we have to do this in the wrapper code.
	 *
	 * @param parameters
	 *            method parameters
	 * @return number conversion code
	 */
	private static String buildNumberConversions(List<Parameter> parameters) {
		final StringBuilder builder = new StringBuilder();
		for (final Parameter parameter : parameters) {
			if ((double.class.equals(parameter.getClazz())) || (Double.class.equals(parameter.getClazz())) || (float.class.equals(parameter.getClazz()))
					|| (Float.class.equals(parameter.getClazz()))) {
				builder.append(String.format("%s = float(%s)", parameter.getName(), parameter.getName()));
				builder.append(StringTools.LINE_DELIMITER);
			}
		}

		return builder.toString();
	}

	@Override
	protected String toSafeName(String name) {
		return toSafeNameStatic(name);
	}

	@Override
	protected String createFieldWrapper(IEnvironment environment, String identifier, Field field) {
		final StringBuilder pythonCode = new StringBuilder();

		pythonCode.append(String.format("import sys%n"));

		pythonCode.append(String.format("if \"py4j\" in sys.modules:%n"));
		pythonCode.append(String.format("    %s = py4j.java_gateway.get_field(%s, \"%s\")%n", field.getName(), identifier, field.getName()));
		pythonCode.append(String.format("else:%n"));
		pythonCode.append(String.format("    %s = %s.%s%n", field.getName(), identifier, field.getName()));

		return pythonCode.toString();
	}

	@Override
	public String createFunctionWrapper(IEnvironment environment, final String moduleVariable, final Method method) {

		final StringBuilder pythonCode = new StringBuilder();

		// parse parameters
		final List<Parameter> parameters = ModuleHelper.getParameters(method);

		// build parameter string
		final StringBuilder methodSignature = new StringBuilder();
		final StringBuilder methodCall = new StringBuilder();

		for (final Parameter parameter : parameters) {
			methodSignature.append(", ").append(toSafeName(parameter.getName()));
			methodCall.append(", ").append(toSafeName(parameter.getName()));
			if (parameter.isOptional())
				methodSignature.append(" = ").append(getDefaultValue(parameter));
		}

		if (methodSignature.length() > 2) {
			methodSignature.delete(0, 2);
			methodCall.delete(0, 2);
		}

		final String body = buildMethodBody(parameters, method, moduleVariable, environment);

		// build function declarations
		for (final String name : getMethodNames(method)) {
			if (!isValidMethodName(name)) {
				Logger.error(Activator.PLUGIN_ID,
						"The method name \"" + name + "\" from the module \"" + moduleVariable + "\" can not be wrapped because it's name is reserved");

			} else if (!name.isEmpty()) {
				pythonCode.append("def ").append(name).append('(').append(methodSignature).append("):\n");
				pythonCode.append(indent(body, "    "));
				pythonCode.append('\n');
				pythonCode.append(name).append(".__ease__ = True\n");
				pythonCode.append('\n');
			}
		}

		return pythonCode.toString();
	}

	private String buildMethodBody(List<Parameter> parameters, Method method, String classIdentifier, IEnvironment environment) {
		final StringBuilder body = new StringBuilder();

		final String methodId = environment.registerMethod(method);

		// insert deprecation warnings
		if (ModuleHelper.isDeprecated(method))
			body.append(String.format("%s.printError(\"%s() is deprecated. Consider updating your code.\", True)%n",
					EnvironmentModule.getWrappedVariableName(environment), method.getName()));

		// Convert Lists to Java arrays
		body.append(buildArrayConversions(parameters)).append(StringTools.LINE_DELIMITER);

		// convert numbers to double/float where needed
		body.append(buildNumberConversions(parameters)).append(StringTools.LINE_DELIMITER);

		// check for callbacks
		body.append(String.format("if not %s.hasMethodCallback(\"%s\"):%n", EnvironmentModule.getWrappedVariableName(environment), methodId));
		if (Objects.equals(Void.TYPE, method.getReturnType())) {
			body.append(String.format("    %s.%s(%s)%n", classIdentifier, method.getName(), buildParameterList(parameters)));
			body.append(String.format("    return %s.VOID%n", ScriptResult.class.getName()));
		} else
			body.append(String.format("    return %s.%s(%s)%n", classIdentifier, method.getName(), buildParameterList(parameters)));

		body.append(StringTools.LINE_DELIMITER);

		// execution with callbacks
		body.append("else:").append(StringTools.LINE_DELIMITER);
		if (environment.getScriptEngine().getDescription().getID().startsWith("org.eclipse.ease.lang.python.py4j")) {
			// special handling for Py4J as it cannot use java varargs parameters directly
			body.append("    ").append("parameters_array = gateway.new_array(gateway.jvm.Object, ").append(parameters.size()).append(")")
					.append(StringTools.LINE_DELIMITER);
			for (int index = 0; index < parameters.size(); index++) {
				// Py4J cannot execute
				// gateway.new_array(gateway.jvm.Object, 1)[0] = None
				// as the default value for array elements is null anyway, we simply do not set those
				body.append("    if ").append(toSafeName(parameters.get(index).getName())).append(" != None:").append(StringTools.LINE_DELIMITER);
				body.append("        ").append("parameters_array[").append(index).append("] = ").append(toSafeName(parameters.get(index).getName()))
						.append(StringTools.LINE_DELIMITER);
			}

			body.append("    ").append(EnvironmentModule.getWrappedVariableName(environment)).append(".preMethodCallback(\"").append(methodId)
					.append("\", parameters_array)").append(StringTools.LINE_DELIMITER);

		} else {
			body.append("    ").append(EnvironmentModule.getWrappedVariableName(environment)).append(".preMethodCallback(\"").append(methodId).append("\"")
					.append(parameters.isEmpty() ? "" : ", ").append(buildParameterList(parameters)).append(")").append(StringTools.LINE_DELIMITER);
		}

		body.append("    ").append(RESULT_NAME).append(" = ").append(classIdentifier).append(".").append(method.getName()).append("(")
				.append(buildParameterList(parameters)).append(")").append(StringTools.LINE_DELIMITER);
		body.append("    ").append(EnvironmentModule.getWrappedVariableName(environment)).append(".postMethodCallback(\"").append(methodId).append("\"")
				.append(", ").append(RESULT_NAME).append(")").append(StringTools.LINE_DELIMITER);

		if (Objects.equals(Void.TYPE, method.getReturnType())) {
			body.append(String.format("    return %s.VOID%n", ScriptResult.class.getName()));
		} else
			body.append(String.format("    return %s%n", RESULT_NAME));

		return body.toString();
	}

	@Override
	public String getSaveVariableName(final String variableName) {
		return PythonHelper.getSaveName(variableName);
	}

	@Override
	public String classInstantiation(final Class<?> clazz, final String[] parameters) {
		final StringBuilder code = new StringBuilder();
		code.append(clazz.getCanonicalName());
		code.append('(');

		if (parameters != null) {
			for (final String parameter : parameters) {
				code.append(parameter);
				code.append(", ");
			}
			if (parameters.length > 0)
				code.delete(code.length() - 2, code.length());
		}

		code.append(')');

		return code.toString();
	}

	public boolean isValidMethodName(final String methodName) {
		return PythonHelper.isSaveName(methodName) && !RESERVED_KEYWORDS.contains(methodName);
	}

	@Override
	protected String getNullString() {
		return "None";
	}

	@Override
	protected String getTrueString() {
		return "True";
	}

	@Override
	protected String getFalseString() {
		return "False";
	}

	@Override
	protected String getSingleLineCommentToken() {
		return "# ";
	}

	@Override
	protected String getMultiLineCommentStartToken() {
		return "\"\"\"";
	}

	@Override
	protected String getMultiLineCommentEndToken() {
		return getMultiLineCommentStartToken();
	}

	@Override
	protected Object getLanguageIdentifier() {
		return "Python";
	}

	/**
	 * Create wrapper code for Pep302 import statements.
	 *
	 * @param environment
	 *            script environment instance
	 * @param instance
	 *            instance to wrap
	 * @param identifier
	 *            instance identifier to be used
	 * @return wrapper code to be loaded by python
	 */
	public String createPep302WrapperCode(EnvironmentModule environment, Object instance, String identifier) {
		return createWrapper(environment, instance, identifier, false, environment.getScriptEngine());
	}
}
