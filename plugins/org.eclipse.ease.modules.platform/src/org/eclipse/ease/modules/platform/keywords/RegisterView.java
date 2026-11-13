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

package org.eclipse.ease.modules.platform.keywords;

import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.e4.ui.model.application.MApplication;
import org.eclipse.e4.ui.model.application.descriptor.basic.MPartDescriptor;
import org.eclipse.e4.ui.workbench.IWorkbench;
import org.eclipse.e4.ui.workbench.modeling.EModelService;
import org.eclipse.ease.modules.platform.PluginConstants;
import org.eclipse.ease.modules.platform.uibuilder.UIBuilderModule;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ui.PlatformUI;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class RegisterView implements EventHandler {

	public static MApplication getApplication() {
		return PlatformUI.getWorkbench().getService(IWorkbench.class).getApplication();
	}

	private static MPartDescriptor createPartDescriptor() {
		final EModelService modelService = PlatformUI.getWorkbench().getService(EModelService.class);
		return modelService.createModelElement(MPartDescriptor.class);
	}

	private static String getCategory(String viewName) {
		final IPath viewPath = new Path(viewName);
		return (viewPath.segmentCount() >= 2) ? viewPath.segment(0) : "Scripted Views";
	}

	private static String getLabel(String viewName) {
		final IPath viewPath = new Path(viewName);
		return viewPath.lastSegment();
	}

	@Override
	public void handleEvent(Event event) {
		final IScript script = (IScript) event.getProperty("script");

		final String value = (String) event.getProperty("value");
		final String oldValue = (String) event.getProperty("oldValue");

		if ((oldValue != null) && (!oldValue.isEmpty()))
			removeContribution(script, oldValue);

		if ((value != null) && (!value.isEmpty()))
			addContribution(script, value);

	}

	private void addContribution(IScript script, String viewName) {
		String iconUri = script.getKeywords().get("image");
		iconUri = (iconUri == null) ? "platform:/plugin/" + PluginConstants.PLUGIN_ID + "/icons/eview16/scripted_view.png" : iconUri;

		final MPartDescriptor partDescriptor = createPartDescriptor();
		partDescriptor.setCategory(getCategory(viewName));
		partDescriptor.setAllowMultiple(false);
		partDescriptor.setCloseable(true);
		partDescriptor.setLabel(getLabel(viewName));
		partDescriptor.setIconURI(iconUri);
		partDescriptor.setContributionURI("bundleclass://" + PluginConstants.PLUGIN_ID + "/" + ScriptedView.class.getName());
		partDescriptor.setElementId(UIBuilderModule.getDynamicViewId());
		partDescriptor.getProperties().put("script", script.getPath().toString());

		// needed to be displayed in the Show views dialog
		partDescriptor.getTags().add("View");

		// do not store permanently in the workbench model
		partDescriptor.getPersistedState().put(IWorkbench.PERSIST_STATE, Boolean.FALSE.toString());

		getApplication().getDescriptors().add(partDescriptor);
	}

	private void removeContribution(IScript script, String viewName) {
		final String category = getCategory(viewName);
		final String label = getLabel(viewName);

		for (final MPartDescriptor descriptor : getApplication().getDescriptors()) {
			if ((label.equals(descriptor.getLabel())) && (category.equals(descriptor.getCategory()))) {
				getApplication().getDescriptors().remove(descriptor);
				break;
			}
		}
	}
}
