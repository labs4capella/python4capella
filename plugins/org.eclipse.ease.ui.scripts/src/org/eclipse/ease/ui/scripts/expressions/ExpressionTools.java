/*******************************************************************************
 * Copyright (c) 2017 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.expressions;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.Platform;
import org.eclipse.ease.ui.scripts.expressions.definitions.AbstractCompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.definitions.AbstractExpressionDefinition;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.ui.plugin.AbstractUIPlugin;

public final class ExpressionTools {

	private static class ParameterDescription {

		private final IConfigurationElement fConfigurationElement;

		public ParameterDescription(IConfigurationElement configurationElement) {
			fConfigurationElement = configurationElement;
		}

		public String getName() {
			return fConfigurationElement.getAttribute("name");
		}

		public String getDefaultValue() {
			final String defaultValue = fConfigurationElement.getAttribute("defaultValue");
			return (defaultValue != null) ? defaultValue : "";
		}

		public String getType() {
			return fConfigurationElement.getAttribute("type");
		}
	}

	public static class ExpressionDescription {

		private final IConfigurationElement fConfigurationElement;

		public ExpressionDescription(IConfigurationElement configurationElement) {
			fConfigurationElement = configurationElement;
		}

		public String getName() {
			return fConfigurationElement.getAttribute("name");
		}

		public ImageDescriptor getImageDescriptor() {
			final String iconLocation = fConfigurationElement.getAttribute("icon");

			if ((iconLocation != null) && (!iconLocation.isEmpty()))
				return AbstractUIPlugin.imageDescriptorFromPlugin(fConfigurationElement.getContributor().getName(), iconLocation);

			return null;
		}

		public IExpressionDefinition createExpressionDefinition() {
			try {
				final Object candidate = fConfigurationElement.createExecutableExtension("class");
				if (candidate instanceof IExpressionDefinition) {

					if (candidate instanceof AbstractExpressionDefinition)
						((AbstractExpressionDefinition) candidate).setConfiguration(fConfigurationElement);

					// set default parameters
					for (final IConfigurationElement parameterElement : fConfigurationElement.getChildren("parameter")) {
						final ParameterDescription description = new ParameterDescription(parameterElement);

						((IExpressionDefinition) candidate).setParameter(description.getName(), description.getDefaultValue());

						switch (description.getType()) {
						case "boolean":
							((IExpressionDefinition) candidate).setParameterValues(description.getName(), new String[] { "true", "false" });
							break;
						default:
							// string parameter
						}
					}

					return (IExpressionDefinition) candidate;
				}
			} catch (final CoreException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			throw new RuntimeException("Could not create definition for expression");
		}
	}

	private static final String EXTENSION_EXPRESSION_ID = "org.eclipse.ease.ui.scripts.expressions";
	private static final String EXTENSION_DEFINITION_ID = "definition";

	@Deprecated
	private ExpressionTools() {
		throw new UnsupportedOperationException("Utility class shall not be isntantiated.");
	}

	public static Map<String, ExpressionDescription> loadDescriptions() {
		final Map<String, ExpressionDescription> descriptions = new HashMap<>();

		final IConfigurationElement[] config = Platform.getExtensionRegistry().getConfigurationElementsFor(EXTENSION_EXPRESSION_ID);
		for (final IConfigurationElement e : config) {
			if (EXTENSION_DEFINITION_ID.equals(e.getName())) {
				final ExpressionDescription description = new ExpressionDescription(e);
				descriptions.put(description.getName(), description);
			}
		}

		return descriptions;
	}

	public static IExpressionDefinition parse(String serializedExpression) {
		final int startBracketPos = serializedExpression.indexOf('(');
		if (startBracketPos > 0) {
			if (serializedExpression.charAt(serializedExpression.length() - 1) != ')')
				throw new IllegalArgumentException("Could not find closing bracket");

			// create expression stub
			final String identifier = serializedExpression.substring(0, startBracketPos);
			final IExpressionDefinition expression = createExpressionDefinition(identifier);

			// parse content
			final String content = serializedExpression.substring(startBracketPos + 1, serializedExpression.length() - 1);

			final List<String> tokens = tokenize(content);
			for (final String token : tokens) {
				final int equalsPos = token.indexOf('=');
				final int bracketPos = token.indexOf('(');
				if (((equalsPos > 0) && (bracketPos > 0) && (equalsPos < bracketPos)) || ((equalsPos > 0) && (bracketPos == -1))) {
					// we have a parameter
					final String key = token.substring(0, equalsPos).trim();
					final String value = token.substring(equalsPos + 1, token.length()).trim();

					if (expression.hasParameter(key))
						expression.setParameter(key, value);

				} else {
					// we have an expression
					if (expression instanceof AbstractCompositeExpressionDefinition)
						((AbstractCompositeExpressionDefinition) expression).addChild(parse(token));
					else
						throw new IllegalArgumentException("Child expression not valid for \"" + expression + "\"");
				}
			}

			return expression;
		}

		throw new IllegalArgumentException("Could not find opening bracket");
	}

	public static IExpressionDefinition createExpressionDefinition(String identifier) {
		final Map<String, ExpressionDescription> descriptions = loadDescriptions();

		if (descriptions.containsKey(identifier))
			return descriptions.get(identifier).createExpressionDefinition();

		throw new IllegalArgumentException("Unknown Expression type \"" + identifier + "\"");
	}

	private static List<String> tokenize(String content) {
		final List<String> tokens = new ArrayList<>();
		int startPos = 0;
		int brackets = 0;
		for (int index = 0; index < content.length(); index++) {
			if (content.charAt(index) == '(')
				brackets++;

			else if (content.charAt(index) == ')')
				brackets--;

			else if ((content.charAt(index) == ',') && (brackets == 0)) {
				tokens.add(content.substring(startPos, index).trim());
				startPos = index + 1;
			}
		}

		if (startPos < content.length())
			tokens.add(content.substring(startPos).trim());

		return tokens;
	}

}
