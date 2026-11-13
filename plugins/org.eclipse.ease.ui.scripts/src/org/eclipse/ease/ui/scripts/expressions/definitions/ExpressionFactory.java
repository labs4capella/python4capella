/*******************************************************************************
 * Copyright (c) 2020 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.ui.scripts.expressions.definitions;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.List;

import org.eclipse.core.expressions.Expression;

public class ExpressionFactory {

	private static ExpressionFactory fInstance = new ExpressionFactory();

	public static ExpressionFactory getInstance() {
		return fInstance;
	}

	public static Class<?> loadClazz(String name) {
		try {
			return ExpressionFactory.class.getClassLoader().loadClass("org.eclipse.core.internal.expressions." + name);
		} catch (final ClassNotFoundException e) {
			try {
				return ExpressionFactory.class.getClassLoader().loadClass("org.eclipse.core.expressions." + name);
			} catch (final ClassNotFoundException e1) {
				throw new RuntimeException("Could not find class " + name, e1);
			}
		}
	}

	public Expression createAndExpression(List<Expression> children) {
		return createCompositeExpression("AndExpression", children);
	}

	public Expression createOrExpression(List<Expression> children) {
		return createCompositeExpression("OrExpression", children);
	}

	private Expression createCompositeExpression(String type, List<Expression> children) {
		final Class<?> clazz = loadClazz(type);
		try {
			final Object instance = clazz.newInstance();

			if (instance instanceof Expression) {
				addChildren(instance, children);
				return (Expression) instance;
			}
		} catch (InstantiationException | IllegalAccessException e) {
			throw new RuntimeException("Could not create instance of " + type, e);

		}

		throw new RuntimeException("Created instance is not an Expression");
	}

	public void addChildren(Object instance, List<Expression> children) {
		try {
			final Method addMethod = instance.getClass().getMethod("add", Expression.class);

			for (final Expression child : children)
				addMethod.invoke(instance, child);

		} catch (NoSuchMethodException | SecurityException | IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
			throw new RuntimeException("Could not add child expressions", e);
		}
	}

	public Expression createWithExpression(String parameter) {
		final Class<?> clazz = loadClazz("WithExpression");

		try {
			final Object instance = clazz.getConstructor(String.class).newInstance(parameter);
			if (instance instanceof Expression)
				return (Expression) instance;

			throw new RuntimeException("Created instance is not an Expression");

		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
				| SecurityException e) {
			throw new RuntimeException("Could not create instance of WithExpression");
		}
	}

	public Expression createReferenceExpression(String parameter) {
		final Class<?> clazz = loadClazz("ReferenceExpression");

		try {
			final Object instance = clazz.getConstructor(String.class).newInstance(parameter);
			if (instance instanceof Expression)
				return (Expression) instance;

			throw new RuntimeException("Created instance is not an Expression");

		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
				| SecurityException e) {
			throw new RuntimeException("Could not create instance of ReferenceExpression");
		}
	}

	public Expression createEqualsExpression(String parameter) {
		final Class<?> clazz = loadClazz("EqualsExpression");

		try {
			final Object instance = clazz.getConstructor(Object.class).newInstance(parameter);
			if (instance instanceof Expression)
				return (Expression) instance;

			throw new RuntimeException("Created instance is not an Expression");

		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
				| SecurityException e) {
			throw new RuntimeException("Could not create instance of EqualsExpression");
		}
	}

	public Expression createCountExpression(String parameter) {
		final Class<?> clazz = loadClazz("CountExpression");

		try {
			final Object instance = clazz.getConstructor(String.class).newInstance(parameter);
			if (instance instanceof Expression)
				return (Expression) instance;

			throw new RuntimeException("Created instance is not an Expression");

		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
				| SecurityException e) {
			throw new RuntimeException("Could not create instance of CountExpression");
		}
	}

	public Expression createTestExpression(String namespace, String property, Object[] args, Object expectedValue, boolean forcePluginActivation) {
		final Class<?> clazz = loadClazz("TestExpression");

		try {
			final Object instance = clazz.getConstructor(String.class, String.class, Object[].class, Object.class, boolean.class).newInstance(namespace,
					property, args, expectedValue, forcePluginActivation);
			if (instance instanceof Expression)
				return (Expression) instance;

			throw new RuntimeException("Created instance is not an Expression");

		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
				| SecurityException e) {
			throw new RuntimeException("Could not create instance of TestExpression");
		}
	}
}
