/*******************************************************************************
 * Copyright (c) 2013 Atos
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Arthur Daussy - initial implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.debug;

import org.eclipse.core.runtime.Platform;

public interface ITracingConstant {

	public static final boolean PYTHON_BOOT_STRAPPER_TRACING = org.eclipse.ease.Activator.getDefault().isDebugging()
			&& "true".equalsIgnoreCase(Platform.getDebugOption("org.eclipse.ease.lang.python/debug/PythonBootStrapper"));

}
