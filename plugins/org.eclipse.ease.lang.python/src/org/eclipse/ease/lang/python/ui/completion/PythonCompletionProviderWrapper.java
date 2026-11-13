/*******************************************************************************
 * Copyright (c) 2017 Martin Kloesch and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Martin Kloesch - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.python.ui.completion;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collection;

import org.eclipse.ease.ICompletionContext;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Logger;
import org.eclipse.ease.lang.python.Activator;
import org.eclipse.ease.lang.python.debugger.ResourceHelper;
import org.eclipse.ease.ui.completion.ScriptCompletionProposal;
import org.eclipse.ease.ui.completion.provider.ICompletionProvider;

/**
 * {@link ICompletionProvider} dispatching actual completion calculation to Python.
 */
public class PythonCompletionProviderWrapper implements ICompletionProvider {
	/**
	 * {@link ICompletionProvider} counterpart in Python world.
	 */
	private ICompletionProvider fPythonProvider = null;

	/**
	 * Sets the Python counterpart for the {@link ICompletionProvider}.
	 *
	 * @param provider
	 *            Python {@link ICompletionProvider}.
	 */
	public void setPythonPprovider(ICompletionProvider provider) {
		fPythonProvider = provider;
	}

	@Override
	public Collection<ScriptCompletionProposal> getProposals(ICompletionContext context) {
		if (!isActive(context)) {
			return new ArrayList<>();
		}

		final IScriptEngine engine = context.getScriptEngine();
		if (engine != null) {
			if (fPythonProvider == null) {
				try {
					final InputStream stream = ResourceHelper.getResourceStream("org.eclipse.ease.lang.python", "pysrc/autocomplete.py");

					// Inject variable first, then instantiate rest via script
					engine.setVariable("_pyease_jedi_completion_provider_wrapper", this);
					engine.inject(stream, false);
				} catch (final Throwable e) {
					Logger.error(Activator.PLUGIN_ID, "Cannot instantiate completion provider in Python world.", e);
					return new ArrayList<>();
				}
			}

			// Double check that everything worked
			if (fPythonProvider != null) {
				return fPythonProvider.getProposals(context);
			}

		}
		return new ArrayList<>();
	}

	@Override
	public boolean isActive(ICompletionContext context) {
		if (fPythonProvider == null) {
			return (context.getScriptEngine() != null) && context.getScriptEngine().getDescription().supports("Python");
		} else {
			return fPythonProvider.isActive(context);
		}
	}
}
