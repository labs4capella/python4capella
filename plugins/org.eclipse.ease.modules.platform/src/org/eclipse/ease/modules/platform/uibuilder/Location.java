/*******************************************************************************
 * Copyright (c) 2019 Christian Pontesegger and others.
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

package org.eclipse.ease.modules.platform.uibuilder;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.layout.GridData;

public class Location {
	private static final Pattern LAYOUT_PATTERN = Pattern.compile("(?:(\\d+)(?:-(\\d+))?/(\\d+)(?:-(\\d+))?)?(?:\\s*([<>ox])(!?))?(?:\\s*([\\^vox])(!?))?");

	public static int DYNAMIC_POSITION = -1;

	private final Point fPosition = new Point(DYNAMIC_POSITION, DYNAMIC_POSITION);
	private final GridData fGridData = new GridData();

	public Location(Point position) {
		fPosition.x = position.x;
		fPosition.y = position.y;
	}

	public Location() {
		this((String) null);
	}

	public Location(String layout) {
		if (layout == null)
			layout = "<^";

		final Matcher matcher = LAYOUT_PATTERN.matcher(layout);
		if (matcher.matches()) {
			if (matcher.group(1) != null) {

				fPosition.x = Integer.parseInt(matcher.group(1));
				fPosition.y = Integer.parseInt(matcher.group(3));

				fGridData.horizontalSpan = (matcher.group(2) != null) ? ((Integer.parseInt(matcher.group(2)) - fPosition.x) + 1) : 1;
				fGridData.verticalSpan = (matcher.group(4) != null) ? ((Integer.parseInt(matcher.group(4)) - fPosition.y) + 1) : 1;

				// sanity checks
				if (fPosition.x < 1)
					throw new IllegalArgumentException("Column cannot be < 1");

				if (fPosition.y < 1)
					throw new IllegalArgumentException("Row cannot be < 1");

				if (fGridData.horizontalSpan < 1)
					throw new IllegalArgumentException("Column span cannot be < 1");

				if (fGridData.verticalSpan < 1)
					throw new IllegalArgumentException("Row span cannot be < 1");
			}

			if (matcher.group(5) != null) {
				switch (matcher.group(5)) {
				case "x":
					fGridData.horizontalAlignment = SWT.CENTER;
					break;
				case ">":
					fGridData.horizontalAlignment = SWT.RIGHT;
					break;
				case "o":
					fGridData.horizontalAlignment = SWT.FILL;
					break;
				case "<":
					// fall through
				default:
					fGridData.horizontalAlignment = SWT.LEFT;
					break;
				}

			} else
				fGridData.horizontalAlignment = SWT.LEFT;

			fGridData.grabExcessHorizontalSpace = ("!".equals(matcher.group(6)));

			if (matcher.group(7) != null) {
				switch (matcher.group(7)) {
				case "x":
					fGridData.verticalAlignment = SWT.CENTER;
					break;
				case "v":
					fGridData.verticalAlignment = SWT.BOTTOM;
					break;
				case "o":
					fGridData.verticalAlignment = SWT.FILL;
					break;
				case "^":
					// fall through
				default:
					fGridData.verticalAlignment = SWT.TOP;
					break;
				}

			} else
				fGridData.verticalAlignment = SWT.TOP;

			fGridData.grabExcessVerticalSpace = ("!".equals(matcher.group(8)));

		} else
			throw new IllegalArgumentException("Cannot parse location: " + layout);
	}

	public Point getPosition() {
		return fPosition;
	}

	public GridData getLayoutData() {
		return fGridData;
	}
}
