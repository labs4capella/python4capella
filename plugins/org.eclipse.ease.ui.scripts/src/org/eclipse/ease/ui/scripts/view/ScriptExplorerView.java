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
package org.eclipse.ease.ui.scripts.view;

import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.ui.ScriptComposite;
import org.eclipse.jface.viewers.DoubleClickEvent;
import org.eclipse.jface.viewers.IDoubleClickListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.FillLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.ui.views.properties.IPropertySheetPage;
import org.eclipse.ui.views.properties.tabbed.ITabbedPropertySheetPageContributor;
import org.eclipse.ui.views.properties.tabbed.TabbedPropertySheetPage;

public class ScriptExplorerView extends ViewPart implements ITabbedPropertySheetPageContributor {
	public ScriptExplorerView() {
	}

	public static final String VIEW_ID = "org.eclipse.ease.ui.views.scriptExplorerView"; //$NON-NLS-1$
	private ScriptComposite fScriptComposite;

	/**
	 * Create contents of the view part.
	 *
	 * @param parent
	 */
	@Override
	public void createPartControl(final Composite parent) {
		parent.setLayout(new FillLayout(SWT.HORIZONTAL));

		fScriptComposite = new ScriptComposite(null, getSite(), parent, SWT.NONE);
		fScriptComposite.setDoubleClickListener(new IDoubleClickListener() {
			@Override
			public void doubleClick(final DoubleClickEvent event) {
				Object element = ((IStructuredSelection) event.getSelection()).getFirstElement();
				if (element instanceof IScript)
					((IScript) element).run();
			}
		});

		getSite().setSelectionProvider(fScriptComposite.getSelectionProvider());

	}

	public Object getAdapter(Class adapter) {
		if (adapter == IPropertySheetPage.class)
			return new TabbedPropertySheetPage(this);
		
		return super.getAdapter(adapter);
	}

	@Override
	public void setFocus() {
		fScriptComposite.setFocus();
	}

	@Override
	public String getContributorId() {
		return VIEW_ID;
	}
}
