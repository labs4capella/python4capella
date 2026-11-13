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
package org.eclipse.ease.ui.scripts.keywordhandler;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.e4.core.services.events.IEventBroker;
import org.eclipse.e4.ui.model.application.ui.SideValue;
import org.eclipse.e4.ui.model.application.ui.basic.MWindow;
import org.eclipse.e4.ui.model.application.ui.menu.MToolBar;
import org.eclipse.e4.ui.workbench.IWorkbench;
import org.eclipse.e4.ui.workbench.modeling.EModelService;
import org.eclipse.e4.ui.workbench.renderers.swt.ToolBarManagerRenderer;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.action.ToolBarManager;
import org.eclipse.ui.IViewPart;
import org.eclipse.ui.IWindowListener;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.internal.WorkbenchPage;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.ui.progress.UIJob;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class ToolbarHandler implements EventHandler {

	/** Trace enablement for the script UI integration. */
	public static final boolean TRACE_UI_INTEGRATION = Activator.getDefault().isDebugging()
			&& "true".equalsIgnoreCase(Platform.getDebugOption(Activator.PLUGIN_ID + "/debug/UIIntegration"));

	private static final String MAIN = "Main";
	private static final Map<String, SideValue> positions = Map.of("TopLeft", SideValue.TOP, //
			"TopRight", SideValue.TOP, //
			"BottomLeft", SideValue.BOTTOM, //
			"BottomRight", SideValue.BOTTOM, //
			"Left", SideValue.LEFT, //
			"Right", SideValue.RIGHT //
	);

	private static final String VIEW_ATTRIBUTE_NAME = "name";

	public static class Location {

		public String fScheme;
		public String fTargetID;
		public String fName;

		public Location(final String scheme, final String location) {
			fScheme = scheme;

			final String[] tokens = location.split("\\|");
			if (MAIN.equals(tokens[0])) {
				// special case for main toolbar
				fTargetID = MAIN;
				if (tokens.length == 1)
					fName = "TopLeft";
				else if ((tokens.length >= 2) && (!tokens[1].isEmpty()) && positions.containsKey(tokens[1]))
					fName = tokens[1];
			} else {
				// try to find a view with matching ID or matching title
				final IConfigurationElement[] config = Platform.getExtensionRegistry().getConfigurationElementsFor("org.eclipse.ui.views");
				for (final IConfigurationElement e : config) {
					if ("view".equals(e.getName())) {
						final String id = e.getAttribute("id");
						if (id.equals(tokens[0])) {
							fTargetID = id;
							break;
						}

						final String name = e.getAttribute(VIEW_ATTRIBUTE_NAME);
						if (name.equals(tokens[0])) {
							fTargetID = id;
							break;
						}
					}
				}

				if (fTargetID != null) {
					if ((tokens.length >= 2) && (!tokens[1].isEmpty()))
						fName = tokens[1];
				}
			}

		}

		public String getID() {
			return fScheme + ":" + (MAIN.equals(fTargetID) ? fName : fTargetID);
		}
	}

	private class UIIntegrationJob extends UIJob {

		private UIIntegrationJob() {
			super("Update toolbar scripts");
		}

		@Override
		public IStatus runInUIThread(final IProgressMonitor monitor) {
			if (PlatformUI.getWorkbench().getActiveWorkbenchWindow() == null) {
				// we might get called before the workbench is loaded.
				// in that case delay execution until the workbench is ready
				PlatformUI.getWorkbench().addWindowListener(new IWindowListener() {

					@Override
					public void windowOpened(final IWorkbenchWindow window) {
					}

					@Override
					public void windowDeactivated(final IWorkbenchWindow window) {
					}

					@Override
					public void windowClosed(final IWorkbenchWindow window) {
					}

					@Override
					public void windowActivated(final IWorkbenchWindow window) {
						PlatformUI.getWorkbench().removeWindowListener(this);
						schedule(300);
					}
				});

				return Status.CANCEL_STATUS;
			}

			List<Event> keywordEvents;
			List<Event> refreshEvents;
			synchronized (ToolbarHandler.this) {
				keywordEvents = fKeywordEvents;
				fKeywordEvents = new ArrayList<>();

				refreshEvents = fRefreshEvents;
				fRefreshEvents = new ArrayList<>();
			}

			// do not process the same script multiple times in the same event loop
			final Collection<IScript> processedScripts = new HashSet<>();

			for (final Event event : keywordEvents) {
				final IScript script = (IScript) event.getProperty("script");
				processedScripts.add(script);

				final String value = (String) event.getProperty("value");
				final String oldValue = (String) event.getProperty("oldValue");

				if ((oldValue != null) && (!oldValue.isEmpty()))
					removeContribution(script, oldValue);

				if ((value != null) && (!value.isEmpty()))
					addContribution(script, value);
			}

			// refresh scripts where appearance was updated
			for (final Event event : refreshEvents) {
				final IScript script = (IScript) event.getProperty("script");
				if (!processedScripts.contains(script)) {
					removeContribution(script, script.getKeywords().get(getHandlerType()));
					addContribution(script, script.getKeywords().get(getHandlerType()));
				}
			}

			return Status.OK_STATUS;
		}

	}

	/**
	 * @param value
	 */
	public Collection<Location> toLocations(final String value) {
		final Collection<Location> locations = new HashSet<>();

		for (final String part : value.split(";"))
			locations.add(new Location(getHandlerType(), part));

		return locations;
	}

	/** Event process job. */
	private final Job fUpdateUIJob = new UIIntegrationJob();

	/** Event queue to be processed. Main events for location additions/removals. */
	private List<Event> fKeywordEvents = new ArrayList<>();

	/** Event queue to be processed. Refresh events due to name/image changes. */
	private List<Event> fRefreshEvents = new ArrayList<>();

	/** UI contribution factories. */
	protected final Map<String, ScriptContributionFactory> fContributionFactories = new HashMap<>();

	public ToolbarHandler() {
		final IEventBroker eventBroker = PlatformUI.getWorkbench().getService(IEventBroker.class);
		eventBroker.subscribe(IRepositoryService.BROKER_CHANNEL_SCRIPT_KEYWORDS + "name", this);
		eventBroker.subscribe(IRepositoryService.BROKER_CHANNEL_SCRIPT_KEYWORDS + "image", this);
	}

	@Override
	public void handleEvent(final Event event) {
		final IScript script = (IScript) event.getProperty("script");
		final String keyword = (String) event.getProperty("keyword");

		synchronized (this) {
			if (("image".equals(keyword)) || ("name".equals(keyword))) {
				if (script.getKeywords().get(getHandlerType()) != null) {
					fRefreshEvents.add(event);
					fUpdateUIJob.schedule(300);
				}

			} else {
				fKeywordEvents.add(event);
				fUpdateUIJob.schedule(300);
			}
		}
	}

	/**
	 * Add a toolbar script contribution.
	 *
	 * @param script
	 *            script to add
	 * @param value
	 *            toolbar keyword value
	 */
	protected void addContribution(final IScript script, final String value) {

		// process each location
		for (final Location location : toLocations(value)) {
			Logger.trace(Activator.PLUGIN_ID, TRACE_UI_INTEGRATION, Activator.PLUGIN_ID,
					"Adding script \"" + script.getName() + "\" to " + location.fScheme + ":" + location.fTargetID);

			if (MAIN.equals(location.fTargetID) && (location.fName != null)) {
				final ScriptContributionFactory contributionFactory = getContributionFactory(location.getID());
				contributionFactory.addScript(script);

				final MToolBar toolbar = getToolBarModel(location);
				if (toolbar.getRenderer() == null)
					return;
				final ToolBarManager toolBarManager = ((ToolBarManagerRenderer) toolbar.getRenderer()).getManager(toolbar);

				contributionFactory.setAffectedContribution(toolBarManager);
				toolBarManager.add(new ScriptContributionItem(script));
				toolBarManager.update(true);
				toolbar.setVisible(true);
				((WorkbenchPage) PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage()).updateActionBars();
			} else if (location.fTargetID != null) {
				final IViewPart view = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().findView(location.fTargetID);

				// update contribution factory
				getContributionFactory(location.getID()).addScript(script);

				if ((view instanceof ViewPart) && (view.getViewSite() != null)) {
					// the view is already rendered, contributions will not be
					// considered anymore so add item directly
					// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=452203 for
					// details

					getContributionFactory(location.getID()).setAffectedContribution(view.getViewSite().getActionBars().getToolBarManager());
					view.getViewSite().getActionBars().getToolBarManager().add(new ScriptContributionItem(script));
					view.getViewSite().getActionBars().updateActionBars();
				}
			}
		}
	}

	private MToolBar getToolBarModel(final Location location) {
		final EModelService service = PlatformUI.getWorkbench().getService(EModelService.class);
		final IWorkbench workbench = PlatformUI.getWorkbench().getService(IWorkbench.class);
		final MWindow window = service.getTopLevelWindowFor(workbench.getApplication().getSelectedElement());
		final MToolBar toolbar = (MToolBar) service.find("org.eclipse.ease.ui.scripts.toolbar." + location.fName.toLowerCase(), window);
		return toolbar;
	}

	/**
	 * Remove a toolbar script contribution.
	 *
	 * @param script
	 *            script to remove
	 * @param value
	 *            toolbar keyword value
	 */
	protected void removeContribution(final IScript script, final String value) {
		// process each location
		for (final Location location : toLocations(value)) {
			Logger.trace(Activator.PLUGIN_ID, TRACE_UI_INTEGRATION, Activator.PLUGIN_ID,
					"Removing script \"" + script.getName() + "\" from " + location.fScheme + ":" + location.fTargetID);

			// update contribution
			getContributionFactory(location.getID()).removeScript(script);

			if (MAIN.equals(location.fTargetID) && (location.fName != null)) {
				final MToolBar toolbar = getToolBarModel(location);
				if (toolbar.getRenderer() == null)
					return;
				final ToolBarManager toolBarManager = ((ToolBarManagerRenderer) toolbar.getRenderer()).getManager(toolbar);

				toolBarManager.remove(script.getLocation());
				toolBarManager.update(false);
				toolbar.setVisible(toolBarManager.getControl().getItemCount() != 0);
				((WorkbenchPage) PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage()).updateActionBars();
			} else if (location.fTargetID != null) {
				final IViewPart view = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage().findView(location.fTargetID);
				if ((view instanceof ViewPart) && (view.getViewSite() != null)) {
					// the view is already rendered, contributions will not be
					// considered anymore so remove item directly
					// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=452203 for
					// details
					view.getViewSite().getActionBars().getToolBarManager().remove(script.getLocation());
					view.getViewSite().getActionBars().updateActionBars();
				}
			}
		}
	}

	protected ScriptContributionFactory getContributionFactory(final String location) {
		if (!fContributionFactories.containsKey(location))
			fContributionFactories.put(location, new ScriptContributionFactory(location));

		return fContributionFactories.get(location);
	}

	protected String getHandlerType() {
		return "toolbar";
	}
}
