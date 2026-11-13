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
package org.eclipse.ease.ui.scripts.expressions.ui;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.commands.IExecutionListener;
import org.eclipse.core.commands.NotHandledException;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.expressions.ExpressionTools;
import org.eclipse.ease.ui.scripts.expressions.ExpressionTools.ExpressionDescription;
import org.eclipse.ease.ui.scripts.expressions.ICompositeExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.definitions.AbstractExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.definitions.AbstractExpressionDefinition.Parameter;
import org.eclipse.ease.ui.scripts.expressions.definitions.RootExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.handler.CreateExpressionHandler;
import org.eclipse.ease.ui.scripts.expressions.handler.DeleteExpressionHandler;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.action.Separator;
import org.eclipse.jface.layout.TreeColumnLayout;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.jface.viewers.CellEditor;
import org.eclipse.jface.viewers.ColumnLabelProvider;
import org.eclipse.jface.viewers.ColumnWeightData;
import org.eclipse.jface.viewers.EditingSupport;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.jface.viewers.TreeViewerColumn;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.KeyEvent;
import org.eclipse.swt.events.KeyListener;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.FillLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Menu;
import org.eclipse.swt.widgets.Tree;
import org.eclipse.swt.widgets.TreeColumn;
import org.eclipse.ui.IWorkbenchPartSite;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.commands.ICommandService;
import org.eclipse.ui.menus.CommandContributionItem;
import org.eclipse.ui.menus.CommandContributionItemParameter;

public class ExpressionComposite extends Composite {

	private TreeViewer fTreeViewer;
	private Tree fTree;
	private final IWorkbenchPartSite fSite;
	private IExecutionListener fCommandExecutionListener;
	private String[] fFilterIds = null;
	private List<CommandContributionItem> fContributionItems = null;

	public ExpressionComposite(IWorkbenchPartSite site, Composite parent, int style) {
		super(parent, style);
		fSite = (site != null) ? site : PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().getActivePart().getSite();

		createPartControl(this);
	}

	public void createPartControl(Composite parent) {
		setLayout(new FillLayout(SWT.HORIZONTAL));

		final Composite composite = new Composite(this, SWT.NONE);
		final TreeColumnLayout tcl_composite = new TreeColumnLayout();
		composite.setLayout(tcl_composite);

		fTreeViewer = new TreeViewer(composite, SWT.BORDER);
		fTree = fTreeViewer.getTree();

		final TreeViewerColumn treeViewerColumn = new TreeViewerColumn(fTreeViewer, SWT.NONE);
		final TreeColumn treeColumn = treeViewerColumn.getColumn();
		tcl_composite.setColumnData(treeColumn, new ColumnWeightData(1, ColumnWeightData.MINIMUM_WIDTH, true));
		treeViewerColumn.setLabelProvider(new ColumnLabelProvider() {
			@Override
			public String getText(Object element) {
				if (element instanceof Parameter)
					return ((Parameter) element).getName() + ": " + ((Parameter) element).getValue();

				return super.getText(element);
			}

			@Override
			public Image getImage(Object element) {
				if (element instanceof Parameter)
					return Activator.getImageDescriptor("/icons/eobj16/expression_parameter.png").createImage();

				else {
					final ExpressionDescription description = ExpressionTools.loadDescriptions().get(element.toString());
					if (description != null) {
						final ImageDescriptor imageDescriptor = description.getImageDescriptor();
						if (imageDescriptor != null)
							return imageDescriptor.createImage();
					}
				}

				return Activator.getImageDescriptor("/icons/eobj16/expression.png").createImage();
			}
		});

		treeViewerColumn.setEditingSupport(new EditingSupport(fTreeViewer) {

			@SuppressWarnings("unchecked")
			@Override
			protected void setValue(Object element, Object value) {
				((Parameter) element).setEditorValue(value.toString());
				fTreeViewer.refresh(element);
			}

			@Override
			protected Object getValue(Object element) {
				return ((Parameter) element).getEditorValue();
			}

			@Override
			protected CellEditor getCellEditor(Object element) {
				return ((Parameter) element).getCellEditor(fTree);
			}

			@Override
			protected boolean canEdit(Object element) {
				return (element instanceof Parameter);
			}
		});

		fTreeViewer.setContentProvider(new ExpressionContentProvider());

		fTree.addKeyListener(new KeyListener() {

			@Override
			public void keyReleased(KeyEvent e) {
			}

			@Override
			public void keyPressed(KeyEvent e) {
				if (e.character == SWT.DEL) {
					for (final Object element : fTreeViewer.getStructuredSelection().toList()) {
						if (element instanceof AbstractExpressionDefinition) {
							final ICompositeExpressionDefinition parent = ((AbstractExpressionDefinition) element).getParent();
							if (parent != null)
								parent.removeChild((AbstractExpressionDefinition) element);
						}
					}

					fTreeViewer.refresh();
				}
			}
		});

		setExpression(null, Messages.ExpressionComposite_3);

		// create context menu
		createContextMenu();

		// react on expression command executions and update tree
		final ICommandService service = fSite.getService(ICommandService.class);
		fCommandExecutionListener = new IExecutionListener() {

			@Override
			public void preExecute(String commandId, ExecutionEvent event) {
			}

			@Override
			public void postExecuteSuccess(String commandId, Object returnValue) {
				if (!fTreeViewer.getTree().isDisposed()) {
					if (commandId.startsWith(CreateExpressionHandler.COMMAND_ID_ROOT))
						fTreeViewer.refresh();
				} else
					service.removeExecutionListener(this);
			}

			@Override
			public void postExecuteFailure(String commandId, ExecutionException exception) {
			}

			@Override
			public void notHandled(String commandId, NotHandledException exception) {
			}
		};
		service.addExecutionListener(fCommandExecutionListener);
	}

	@Override
	public void dispose() {
		final ICommandService service = fSite.getService(ICommandService.class);
		service.removeExecutionListener(fCommandExecutionListener);

		super.dispose();
	}

	private void createContextMenu() {
		final MenuManager menuManager = new MenuManager();

		// prepare dynamic contribution items
		prepareDynamicContributionItems();

		final CommandContributionItemParameter contributionParameters = new CommandContributionItemParameter(fSite, null, DeleteExpressionHandler.COMMAND_ID,
				null, null, null, null, Messages.ExpressionComposite_delete, null, Messages.ExpressionComposite_delete, SWT.PUSH, null, true);
		final CommandContributionItem deleteContributionItem = new CommandContributionItem(contributionParameters);

		final Menu menu = menuManager.createContextMenu(fTreeViewer.getControl());
		fTreeViewer.getControl().setMenu(menu);
		fSite.registerContextMenu(menuManager, fTreeViewer);

		menuManager.addMenuListener(manager -> {
			final Object element = fTreeViewer.getStructuredSelection().getFirstElement();
			final boolean showMenu = (element instanceof ICompositeExpressionDefinition) && (((ICompositeExpressionDefinition) element).acceptsChild());

			if (showMenu) {
				for (final CommandContributionItem item : fContributionItems)
					manager.add(item);

				manager.add(new Separator());
			}

			if ((element instanceof IExpressionDefinition) && (((IExpressionDefinition) element).getParent() != null))
				// add delete entry, keep this the last one so users do not pick it accidently
				manager.add(deleteContributionItem);
		});

		menuManager.setRemoveAllWhenShown(true);
	}

	private void prepareDynamicContributionItems() {
		fContributionItems = new ArrayList<>();
		final Map<String, ExpressionDescription> descriptions = ExpressionTools.loadDescriptions();
		final List<String> keys = new ArrayList<>(descriptions.keySet());
		// sort alphabetically
		Collections.sort(keys);

		// remove unwanted expressions
		if (fFilterIds != null)
			keys.retainAll(Arrays.asList(fFilterIds));

		for (final String key : keys) {
			final ExpressionDescription description = descriptions.get(key);
			final Map<String, String> parameters = new HashMap<>();
			parameters.put(CreateExpressionHandler.PARAMETER_TYPE, description.getName());

			final CommandContributionItemParameter contributionParameters = new CommandContributionItemParameter(fSite, null,
					CreateExpressionHandler.COMMAND_ID, parameters, description.getImageDescriptor(), null, null, description.getName(), null,
					Messages.ExpressionComposite_add + description.getName() + Messages.ExpressionComposite_expression, SWT.PUSH, null, true);
			fContributionItems.add(new CommandContributionItem(contributionParameters));
		}
	}

	public void setExpression(IExpressionDefinition expression, String rootName) {
		if ((fTree != null) && (!fTree.isDisposed())) {
			final RootExpressionDefinition root = new RootExpressionDefinition(rootName);
			if (expression != null)
				root.addChild(expression);

			fTreeViewer.setInput(new Object[] { root });
		}
	}

	public IExpressionDefinition getExpression() {
		if ((fTree != null) && (!fTree.isDisposed()))
			return (IExpressionDefinition) ((Object[]) fTreeViewer.getInput())[0];

		return null;
	}

	public void setAcceptedFilters(String[] filterIds) {
		fFilterIds = filterIds;
		prepareDynamicContributionItems();
	}
}
