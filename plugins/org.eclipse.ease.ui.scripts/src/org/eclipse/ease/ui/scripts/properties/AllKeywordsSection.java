/*******************************************************************************
 * Copyright (c) 2016 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.properties;

import java.util.Map.Entry;

import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.layout.TableColumnLayout;
import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.CellEditor;
import org.eclipse.jface.viewers.ColumnLabelProvider;
import org.eclipse.jface.viewers.ColumnWeightData;
import org.eclipse.jface.viewers.EditingSupport;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.jface.viewers.TableViewerColumn;
import org.eclipse.jface.viewers.TextCellEditor;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.jface.viewers.ViewerComparator;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.FillLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Menu;
import org.eclipse.swt.widgets.Table;
import org.eclipse.swt.widgets.TableColumn;
import org.eclipse.ui.IWorkbenchPart;
import org.eclipse.ui.plugin.AbstractUIPlugin;
import org.eclipse.ui.views.properties.tabbed.AbstractPropertySection;
import org.eclipse.ui.views.properties.tabbed.TabbedPropertySheetPage;

public class AllKeywordsSection extends AbstractPropertySection {

	private TableViewer fTableViewer;

	@Override
	public void createControls(Composite parent, TabbedPropertySheetPage aTabbedPropertySheetPage) {
		super.createControls(parent, aTabbedPropertySheetPage);

		final Composite mainComposite = getWidgetFactory().createComposite(parent, SWT.NONE);
		final FillLayout fl_mainComposite = new FillLayout(SWT.VERTICAL);
		fl_mainComposite.marginWidth = 5;
		fl_mainComposite.marginHeight = 5;
		mainComposite.setLayout(fl_mainComposite);

		final Composite tableComposite = getWidgetFactory().createComposite(mainComposite, SWT.NONE);
		getWidgetFactory().paintBordersFor(tableComposite);

		final TableColumnLayout tcl_composite = new TableColumnLayout();
		tableComposite.setLayout(tcl_composite);

		fTableViewer = new TableViewer(tableComposite, SWT.BORDER | SWT.FULL_SELECTION);
		final Table table = fTableViewer.getTable();
		table.setHeaderVisible(true);
		table.setLinesVisible(true);

		getWidgetFactory().paintBordersFor(table);

		final TableViewerColumn tableViewerColumn = new TableViewerColumn(fTableViewer, SWT.NONE);
		final TableColumn tblclmnKeyword = tableViewerColumn.getColumn();
		tcl_composite.setColumnData(tblclmnKeyword, new ColumnWeightData(2, ColumnWeightData.MINIMUM_WIDTH, true));
		tblclmnKeyword.setText(Messages.AllKeywordsSection_keyword);
		tableViewerColumn.setLabelProvider(new ColumnLabelProvider() {

			@SuppressWarnings("unchecked")
			@Override
			public String getText(Object element) {
				return ((Entry<String, ?>) element).getKey();
			}

			@Override
			public Image getImage(Object element) {
				final String scriptValue = getScript().getScriptKeywords().get(((Entry<?, ?>) element).getKey());
				final boolean isScriptKeyword = (((Entry<?, ?>) element).getValue().equals(scriptValue));

				if (isScriptKeyword)
					return AbstractUIPlugin.imageDescriptorFromPlugin("org.eclipse.ease.ui", "/icons/eobj16/script.png").createImage();
				else
					return Activator.getImageDescriptor("/icons/eobj16/user.png").createImage();
			}
		});

		final TableViewerColumn tableViewerColumn_1 = new TableViewerColumn(fTableViewer, SWT.NONE);
		final TableColumn tblclmnValue = tableViewerColumn_1.getColumn();
		tcl_composite.setColumnData(tblclmnValue, new ColumnWeightData(5, ColumnWeightData.MINIMUM_WIDTH, true));
		tblclmnValue.setText(Messages.AllKeywordsSection_value);

		fTableViewer.setContentProvider(ArrayContentProvider.getInstance());
		tableViewerColumn_1.setLabelProvider(new ColumnLabelProvider() {

			@SuppressWarnings("unchecked")
			@Override
			public String getText(Object element) {
				return ((Entry<?, String>) element).getValue();
			}
		});

		tableViewerColumn_1.setEditingSupport(new EditingSupport(fTableViewer) {

			@Override
			protected void setValue(Object element, Object value) {
				final String targetValue = (value.toString().trim().isEmpty()) ? null : value.toString().trim();
				getScript().setUserKeyword(((Entry<?, ?>) element).getKey().toString(), targetValue);
				refresh();
			}

			@Override
			protected Object getValue(Object element) {
				return ((Entry<?, ?>) element).getValue().toString();
			}

			@Override
			protected CellEditor getCellEditor(Object element) {
				return new TextCellEditor(table);
			}

			@Override
			protected boolean canEdit(Object element) {
				return true;
			}
		});

		fTableViewer.setComparator(new ViewerComparator() {
			@SuppressWarnings("unchecked")
			@Override
			public int compare(Viewer viewer, Object e1, Object e2) {
				return ((Entry<String, String>) e1).getKey().compareToIgnoreCase(((Entry<String, String>) e2).getKey());
			}
		});
	}

	private boolean fContextMenuRegistered = false;

	@Override
	public void setInput(IWorkbenchPart part, ISelection selection) {
		super.setInput(part, selection);

		// register context menu
		if (!fContextMenuRegistered) {
			final MenuManager menuManager = new MenuManager();
			final Menu contextMenu = menuManager.createContextMenu(fTableViewer.getTable());
			fTableViewer.getTable().setMenu(contextMenu);
			getPart().getSite().registerContextMenu("org.eclipse.ease.scripts.properties.allKeywords", menuManager, fTableViewer);

			fContextMenuRegistered = true;
		}
	}

	@Override
	public boolean shouldUseExtraSpace() {
		return true;
	}

	@Override
	public void refresh() {
		fTableViewer.setInput(getScript().getKeywords().entrySet());
		fTableViewer.refresh();
	}

	public IScript getScript() {
		final ISelection selection = getSelection();
		if (selection instanceof IStructuredSelection) {
			final Object candidate = ((IStructuredSelection) selection).getFirstElement();
			return (IScript) ((candidate instanceof IScript) ? candidate : null);
		}

		return null;
	}
}
