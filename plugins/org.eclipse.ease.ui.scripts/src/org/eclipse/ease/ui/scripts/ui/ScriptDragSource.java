/*******************************************************************************
 * Copyright (c) 2013 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.ui;

import org.eclipse.jface.util.LocalSelectionTransfer;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.swt.dnd.DND;
import org.eclipse.swt.dnd.DragSource;
import org.eclipse.swt.dnd.DragSourceEvent;
import org.eclipse.swt.dnd.Transfer;
import org.eclipse.swt.dnd.TreeDragSourceEffect;

/**
 * Source for a script D&amp;D event.
 */
public class ScriptDragSource extends TreeDragSourceEffect {

	private final TreeViewer fTree;

	/**
	 * Constructor. Gets its macros from a tree selection.
	 *
	 * @param tree
	 *            tree to read from
	 */
	public ScriptDragSource(final TreeViewer tree) {
		super(tree.getTree());
		fTree = tree;
	}

	/**
	 * Does everything to add drag support to a given tree.
	 *
	 * @param treeViewer
	 *            tree to add drag support to
	 */
	public static final void addDragSupport(final TreeViewer treeViewer) {
		final DragSource source = new DragSource(treeViewer.getTree(), DND.DROP_MOVE | DND.DROP_COPY);
		source.setTransfer(new Transfer[] { LocalSelectionTransfer.getTransfer() });
		source.addDragListener(new ScriptDragSource(treeViewer));
	}

	@Override
	public final void dragSetData(final DragSourceEvent event) {
		LocalSelectionTransfer.getTransfer().setSelection(fTree.getSelection());
	}
}
