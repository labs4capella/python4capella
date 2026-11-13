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

import java.util.ArrayList;
import java.util.List;

import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.graphics.Rectangle;
import org.eclipse.swt.widgets.Control;

public class ViewModel {

	private final List<Object> fElements = new ArrayList<>();
	private int fRows = 0;
	private int fColumns = 0;

	private final IRenderer fRenderer;

	public ViewModel(IRenderer renderer) {
		fRenderer = renderer;
		fRenderer.setViewModel(this);
	}

	public List<Object> getElements() {
		return fElements;
	}

	public void insertElement(Object element, Location location) {

		if ((location.getPosition().x == Location.DYNAMIC_POSITION) || (location.getPosition().y == Location.DYNAMIC_POSITION)) {
			// find position to insert

			// default
			location.getPosition().x = 1;
			location.getPosition().y = 1;

			for (int index = fElements.size() - 1; index >= 0; index--) {
				if (!(fElements.get(index) instanceof IPlaceHolder) && !(fElements.get(index) instanceof Reference)) {
					final Point target = indexToPoint(index + 1);
					location.getPosition().x = target.x;
					location.getPosition().y = target.y;
					break;
				}
			}
		}

		// now we got a fixed position to insert
		ensureColumnCount((location.getPosition().x + location.getLayoutData().horizontalSpan) - 1);
		ensureRowCount((location.getPosition().y + location.getLayoutData().verticalSpan) - 1);

		splitSpanElements(new Rectangle(location.getPosition().x, location.getPosition().y, location.getLayoutData().horizontalSpan,
				location.getLayoutData().verticalSpan));

		replaceElementAt(location.getPosition(), element);
		if ((location.getLayoutData().horizontalSpan > 1) || (location.getLayoutData().verticalSpan > 1)) {
			final Reference reference = new Reference(element);
			for (int width = 0; width < location.getLayoutData().horizontalSpan; width++) {
				for (int height = 0; height < location.getLayoutData().verticalSpan; height++) {
					if ((width > 0) || (height > 0))
						replaceElementAt(new Point(location.getPosition().x + width, location.getPosition().y + height), reference);
				}
			}
		}

		if (element instanceof Control)
			((Control) element).setLayoutData(location.getLayoutData());
	}

	public int getColumnCount() {
		return fColumns;
	}

	public int getRowCount() {
		return fRows;
	}

	private void replaceElementAt(Point position, Object element) {
		final int index = pointToIndex(position);
		final Object oldElement = fElements.remove(index);
		if (oldElement instanceof Control)
			((Control) oldElement).dispose();

		fElements.add(index, element);
	}

	private void splitSpanElements(Rectangle rectangle) {
		for (int column = rectangle.x; column < (rectangle.x + rectangle.width); column++) {
			for (int row = rectangle.y; row < (rectangle.y + rectangle.height); row++) {
				final Object element = fElements.get(pointToIndex(new Point(column, row)));
				if (element instanceof Reference)
					splitElement(((Reference) element).getDelegate());
			}
		}
	}

	private void splitElement(Object elementToSplit) {
		for (int index = 0; index < fElements.size(); index++) {
			if (fElements.get(index).equals(elementToSplit)) {

				final Point position = indexToPoint(index);
				replaceElementAt(position, fRenderer.createPlaceHolder(position));

			} else if ((fElements.get(index) instanceof Reference) && (((Reference) fElements.get(index)).getDelegate().equals(elementToSplit))) {
				final Point position = indexToPoint(index);
				replaceElementAt(position, fRenderer.createPlaceHolder(position));
			}
		}
	}

	public Point indexToPoint(int index) {
		return new Point((index % fColumns) + 1, (index / fColumns) + 1);
	}

	private int pointToIndex(Point point) {
		return (((point.y - 1) * fColumns) + point.x) - 1;
	}

	private void ensureColumnCount(int columns) {
		while (fColumns < columns)
			addColumn();
	}

	private void addColumn() {
		if (fElements.isEmpty()) {
			final IPlaceHolder placeHolder = fRenderer.createPlaceHolder(new Point(1, 1));
			fElements.add(placeHolder);
			fRows = 1;
			fColumns = 1;

		} else {
			for (int row = fRows - 1; row >= 0; row--) {
				final Point position = new Point(fColumns + 1, row + 1);
				final IPlaceHolder placeHolder = fRenderer.createPlaceHolder(position);
				fElements.add(pointToIndex(position), placeHolder);
			}
			fColumns++;
		}
	}

	private void ensureRowCount(int rows) {
		while (fRows < rows)
			addRow();
	}

	private void addRow() {
		if (fElements.isEmpty()) {
			final IPlaceHolder placeHolder = fRenderer.createPlaceHolder(new Point(1, 1));
			fElements.add(placeHolder);
			fRows = 1;
			fColumns = 1;

		} else {
			fRows++;
			for (int column = 1; column <= fColumns; column++) {
				final IPlaceHolder placeHolder = fRenderer.createPlaceHolder(new Point(column, fRows));
				fElements.add(placeHolder);
			}
		}
	}

	public void setColumnCount(int columns) {
		ensureColumnCount(columns);
	}
}
