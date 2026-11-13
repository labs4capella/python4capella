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

import org.eclipse.swt.SWT;
import org.eclipse.swt.custom.ScrolledComposite;
import org.eclipse.swt.events.PaintEvent;
import org.eclipse.swt.events.PaintListener;
import org.eclipse.swt.graphics.Point;
import org.eclipse.swt.graphics.Rectangle;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;

public class CompositeRenderer implements IRenderer, PaintListener {

	private final Composite fParent;
	private ViewModel fViewModel;
	private boolean fShowGrid = false;

	public CompositeRenderer(Composite parent) {
		fParent = parent;
	}

	@Override
	public void setViewModel(ViewModel viewModel) {
		fViewModel = viewModel;
	}

	@Override
	public IPlaceHolder createPlaceHolder(Point position) {
		final LabelPlaceHolder placeHolder = new LabelPlaceHolder(fParent, position.y, position.x);
		placeHolder.setVisible(fShowGrid);
		return placeHolder;
	}

	public Composite getParent() {
		return fParent;
	}

	private GridLayout getLayout() {
		return (GridLayout) getParent().getLayout();
	}

	public void update() {
		Control predecessor = null;
		for (final Object element : fViewModel.getElements()) {
			if (element instanceof Control) {
				((Control) element).moveBelow(predecessor);
				predecessor = (Control) element;
			}
		}

		getLayout().numColumns = fViewModel.getColumnCount();

		getParent().layout(true);

		if (getParent().getParent() instanceof ScrolledComposite) {
			((ScrolledComposite) getParent().getParent()).setMinSize(getParent().computeSize(SWT.DEFAULT, SWT.DEFAULT));
			getParent().getParent().layout(true);
		}
	}

	public void setShowGrid(boolean showGrid) {
		fShowGrid = showGrid;

		if (showGrid)
			getParent().addPaintListener(this);
		else
			getParent().removePaintListener(this);

		for (final Object element : fViewModel.getElements()) {
			if (element instanceof LabelPlaceHolder)
				((LabelPlaceHolder) element).setVisible(showGrid);
		}
	}

	@Override
	public void paintControl(PaintEvent e) {
		e.gc.setForeground(Display.getCurrent().getSystemColor(SWT.COLOR_RED));

		final List<Rectangle> columns = new ArrayList<>();
		while (columns.size() < fViewModel.getColumnCount())
			columns.add(new Rectangle(0, 0, 0, 0));

		final List<Rectangle> rows = new ArrayList<>();
		while (rows.size() < fViewModel.getRowCount())
			rows.add(new Rectangle(0, 0, 0, 0));

		for (final Object element : fViewModel.getElements()) {
			if (element instanceof Control) {
				final Rectangle bounds = ((Control) element).getBounds();
				final Point columnRowLocation = fViewModel.indexToPoint(fViewModel.getElements().indexOf(element));

				final Rectangle column = columns.get(columnRowLocation.x - 1);
				final Rectangle row = rows.get(columnRowLocation.y - 1);

				if (((GridData) ((Control) element).getLayoutData()).horizontalSpan == 1)
					merge(bounds, column);

				if (((GridData) ((Control) element).getLayoutData()).verticalSpan == 1)
					merge(bounds, row);
			}
		}

		final Rectangle firstRow = rows.get(0);
		final Rectangle lastRow = rows.get(rows.size() - 1);
		for (final Rectangle rectangle : columns) {
			rectangle.y = firstRow.y;
			rectangle.height = (lastRow.y + lastRow.height) - firstRow.y;

			e.gc.drawRectangle(rectangle.x - 3, rectangle.y - 3, rectangle.width + 5, rectangle.height + 5);
		}

		final Rectangle firstColumn = columns.get(0);
		final Rectangle lastColumn = columns.get(columns.size() - 1);
		for (final Rectangle rectangle : rows) {
			rectangle.x = firstColumn.x;
			rectangle.width = (lastColumn.x + lastColumn.width) - firstColumn.x;

			e.gc.drawRectangle(rectangle.x - 3, rectangle.y - 3, rectangle.width + 5, rectangle.height + 5);
		}
	}

	private void merge(Rectangle source, Rectangle target) {
		if (target.x == 0)
			target.x = source.x;

		if (target.y == 0)
			target.y = source.y;

		if (target.width == 0)
			target.width = source.width;

		if (target.height == 0)
			target.height = source.height;

		target.add(source);
	}
}
