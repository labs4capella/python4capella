/*******************************************************************************
 * Copyright (c) 2015 Christian Pontesegger and others.
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
package org.eclipse.ease.lang.unittest.reporters;

import org.eclipse.ease.lang.unittest.runtime.ITestEntity;

/**
 * Interface for a test report generator.
 */
public interface IReportGenerator {
	/**
	 * Creates report data as string.
	 *
	 * @param title
	 *            report title
	 * @param description
	 *            generic description
	 * @param testEntity
	 *            test element to be exported
	 * @return String containing full test report
	 */
	String createReport(final String title, final String description, final ITestEntity testEntity);

	/**
	 * Creates report data as string.
	 *
	 * @param title
	 *            report title
	 * @param description
	 *            generic description
	 * @param testEntity
	 *            test element to be exported
	 * @param reportData
	 *            additional report data. Specific to report type. Could be <code>null</code>
	 * @return String containing full test report
	 */
	default String createReport(final String title, final String description, final ITestEntity testEntity, Object reportData) {
		return createReport(title, description, testEntity);
	}

	/**
	 * Returns the default file extension to be used for this kind of report without the preceding dot (eg "txt").
	 *
	 * @return file extension to be used
	 */
	String getDefaultExtension();
}
