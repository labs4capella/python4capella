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

import org.eclipse.ease.ui.completion.IHelpResolver;

/**
 * Custom {@link IHelpResolver} for Python objects.
 * 
 * Actual help resolving is done in Python and this class only stores the
 * results.
 */
public class PythonHelpResolver implements IHelpResolver {
	/**
	 * Help as plain string.
	 */
	private final String fPlain;

	/**
	 * Help as formatted HTML string.
	 */
	private final String fHtml;

	/**
	 * Constructor only stores parameters to members.
	 * 
	 * @param plain
	 *            see {@link #fPlain}
	 * @param html
	 *            see {@link #fHtml}
	 */
	public PythonHelpResolver(final String plain, final String html) {
		fPlain = plain;
		fHtml = html;
	}

	@Override
	public String resolveHelp() {
		return fPlain;
	}

	@Override
	public String resolveHTMLHelp() {
		return fHtml;
	}

}
