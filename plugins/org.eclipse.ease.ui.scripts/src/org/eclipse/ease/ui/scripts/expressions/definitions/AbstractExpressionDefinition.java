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
package org.eclipse.ease.ui.scripts.expressions.definitions;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;

import org.eclipse.core.expressions.Expression;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.ease.ui.scripts.expressions.ICompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.CellEditor;
import org.eclipse.jface.viewers.ComboBoxViewerCellEditor;
import org.eclipse.jface.viewers.TextCellEditor;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;

public abstract class AbstractExpressionDefinition implements IExpressionDefinition {

	public static class Parameter {

		private final String fName;
		private String fValue;
		private String[] fAllowedValues = null;

		public Parameter(String name, String value) {
			fName = name;
			fValue = value;
		}

		public CellEditor getCellEditor(Composite parent) {
			if (fAllowedValues == null)
				return new TextCellEditor(parent);

			final ComboBoxViewerCellEditor comboBoxViewerCellEditor = new ComboBoxViewerCellEditor(parent, SWT.READ_ONLY);
			comboBoxViewerCellEditor.setContentProvider(ArrayContentProvider.getInstance());
			comboBoxViewerCellEditor.setInput(fAllowedValues);
			return comboBoxViewerCellEditor;
		}

		public void setEditorValue(String value) {
			setValue(value);
		}

		public Object getEditorValue() {
			if (fAllowedValues == null)
				return getValue();

			return Arrays.asList(fAllowedValues).indexOf(getValue());
		}

		public String getName() {
			return fName;
		}

		public String getValue() {
			return fValue;
		}

		public void setValue(String value) {
			fValue = value;
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = (prime * result) + ((fName == null) ? 0 : fName.hashCode());
			return result;
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			final Parameter other = (Parameter) obj;
			if (fName == null) {
				if (other.fName != null)
					return false;
			} else if (!fName.equals(other.fName))
				return false;
			return true;
		}

		/**
		 * @param allowedValues
		 */
		public void setAllowedValues(String[] allowedValues) {
			fAllowedValues = allowedValues;
		}
	}

	private ICompositeExpressionDefinition fParent = null;

	private Collection<Parameter> fParameters = null;

	private IConfigurationElement fConfigurationElement;

	@Override
	public void setParent(ICompositeExpressionDefinition parent) {
		fParent = parent;
	}

	@Override
	public ICompositeExpressionDefinition getParent() {
		return fParent;
	}

	public Collection<Parameter> getParameters() {
		return (fParameters != null) ? fParameters : Collections.emptySet();
	}

	protected String getParameter(String key) {
		for (final Parameter parameter : getParameters()) {
			if (parameter.getName().equals(key))
				return parameter.getValue();
		}

		return null;
	}

	@Override
	public boolean hasParameter(String key) {
		for (final Parameter parameter : getParameters()) {
			if (parameter.getName().equals(key))
				return true;
		}

		return false;
	}

	@Override
	public void setParameter(String key, String value) {
		if (fParameters == null)
			fParameters = new HashSet<>();

		for (final Parameter parameter : getParameters()) {
			if (parameter.getName().equals(key)) {
				parameter.setValue(value);
				return;
			}
		}

		getParameters().add(new Parameter(key, value));
	}

	@Override
	public void setParameterValues(String key, String[] allowedValues) {

		for (final Parameter parameter : getParameters()) {
			if (parameter.getName().equals(key)) {
				parameter.setAllowedValues(allowedValues);
				return;
			}
		}
	}

	@Override
	public String serialize() {
		final StringBuilder builder = new StringBuilder();
		builder.append(toString());
		builder.append('(');
		builder.append(serializeParameters());
		builder.append(')');
		return builder.toString();
	}

	protected String serializeParameters() {
		final StringBuilder builder = new StringBuilder();
		for (final Parameter entry : getParameters()) {
			builder.append(entry.getName());
			builder.append('=');
			builder.append(entry.getValue());
			builder.append(", ");
		}
		if (!getParameters().isEmpty())
			builder.delete(builder.length() - 2, builder.length());

		return builder.toString();
	}

	@Override
	public String toString() {
		final String name = fConfigurationElement.getAttribute("name");
		return (name != null) ? name : super.toString();
	}

	@Override
	public String getDescription() {
		return fConfigurationElement.getAttribute("description");
	}

	public void setConfiguration(IConfigurationElement configurationElement) {
		fConfigurationElement = configurationElement;
	}

	protected IConfigurationElement getConfigurationElement() {
		return fConfigurationElement;
	}

	@Override
	public abstract Expression toCoreExpression();
}
