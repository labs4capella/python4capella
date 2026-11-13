/*******************************************************************************
 * Copyright (c) 2010 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     IBM Corporation - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.debugger.actions;

import org.eclipse.debug.ui.IDebugView;
import org.eclipse.ease.Activator;
import org.eclipse.jface.action.IAction;
import org.eclipse.jface.preference.IPreferenceStore;
import org.eclipse.jface.util.IPropertyChangeListener;
import org.eclipse.jface.util.PropertyChangeEvent;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.StructuredViewer;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.jface.viewers.ViewerFilter;
import org.eclipse.swt.widgets.Event;
import org.eclipse.ui.IActionDelegate2;
import org.eclipse.ui.IViewActionDelegate;
import org.eclipse.ui.IViewPart;

/**
 * Abstract action that can be used to update an {@link IDebugView}.
 *
 * @since 1.0
 */
public abstract class ViewFilterAction extends ViewerFilter implements IViewActionDelegate, IActionDelegate2 {

	private IViewPart fView;

	private IAction fAction;

	private final IPropertyChangeListener fListener = new Updater();

	class Updater implements IPropertyChangeListener {

		/*
		 * (non-Javadoc)
		 *
		 * @see org.eclipse.jface.util.IPropertyChangeListener#propertyChange(org.eclipse.jface.util.PropertyChangeEvent)
		 */
		@Override
		public void propertyChange(final PropertyChangeEvent event) {
			if (event.getProperty().equals(getPreferenceKey()) || event.getProperty().equals(getCompositeKey())) {
				fAction.setChecked(getPreferenceValue());
			}

		}

	}

	public ViewFilterAction() {
		super();
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IViewActionDelegate#init(org.eclipse.ui.IViewPart)
	 */
	@Override
	public void init(final IViewPart view) {
		fView = view;
		fAction.setChecked(getPreferenceValue());
		run(fAction);
		getPreferenceStore().addPropertyChangeListener(fListener);
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IActionDelegate2#init(org.eclipse.jface.action.IAction)
	 */
	@Override
	public void init(final IAction action) {
		fAction = action;
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IActionDelegate2#dispose()
	 */
	@Override
	public void dispose() {
		getPreferenceStore().removePropertyChangeListener(fListener);
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IActionDelegate2#runWithEvent(org.eclipse.jface.action.IAction, org.eclipse.swt.widgets.Event)
	 */
	@Override
	public void runWithEvent(final IAction action, final Event event) {
		run(action);
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IActionDelegate#run(org.eclipse.jface.action.IAction)
	 */
	@Override
	public void run(final IAction action) {
		StructuredViewer viewer = getStructuredViewer();
		ViewerFilter[] filters = viewer.getFilters();
		ViewerFilter filter = null;
		for (int i = 0; i < filters.length; i++) {
			if (filters[i] == this) {
				filter = filters[i];
				break;
			}
		}
		if (filter == null) {
			viewer.addFilter(this);
		} else {
			// only refresh is removing - adding will refresh automatically
			viewer.refresh();
		}
		IPreferenceStore store = getPreferenceStore();
		store.setValue(getPreferenceKey(), action.isChecked());
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ui.IActionDelegate#selectionChanged(org.eclipse.jface.action.IAction, org.eclipse.jface.viewers.ISelection)
	 */
	@Override
	public void selectionChanged(final IAction action, final ISelection selection) {
	}

	/**
	 * @return the {@link IPreferenceStore} to save the setting to
	 */
	protected IPreferenceStore getPreferenceStore() {
		return Activator.getDefault().getPreferenceStore();
	}

	/**
	 * Returns the value of this filters preference (on/off) for the given view.
	 *
	 * @return boolean
	 */
	protected boolean getPreferenceValue() {
		IPreferenceStore store = getPreferenceStore();
		return store.getBoolean(getPreferenceKey());
	}

	/**
	 * Returns the key for this action's preference.
	 *
	 * @return String
	 */
	protected abstract String getPreferenceKey();

	/**
	 * Returns the key used by this action to store its preference value/setting. Based on a base key (suffix) and part id (prefix).
	 *
	 * @return preference store key
	 */
	protected String getCompositeKey() {
		String baseKey = getPreferenceKey();
		String viewKey = getView().getSite().getId();
		return viewKey + "." + baseKey; //$NON-NLS-1$
	}

	/**
	 * @return the {@link IViewPart} handle
	 */
	protected IViewPart getView() {
		return fView;
	}

	/**
	 * @return the backing {@link StructuredViewer}
	 */
	protected StructuredViewer getStructuredViewer() {
		IDebugView view = (IDebugView) getView().getAdapter(IDebugView.class);
		if (view != null) {
			Viewer viewer = view.getViewer();
			if (viewer instanceof StructuredViewer) {
				return (StructuredViewer) viewer;
			}
		}
		return null;
	}

	/**
	 * Returns whether this action is selected/checked.
	 *
	 * @return whether this action is selected/checked
	 */
	protected boolean getValue() {
		return fAction.isChecked();
	}
}
