/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.preferences;

import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.emf.common.util.URI;
import org.eclipse.jface.dialogs.IInputValidator;

public class URIValidator implements IInputValidator {

	@Override
	public String isValid(String text) {
		try {
			if (URI.createURI(text).isRelative())
				return Messages.URIValidator_relativeUri;
		} catch (Exception e) {
			return Messages.URIValidator_invalidUri;
		}

		return null;
	}
}
