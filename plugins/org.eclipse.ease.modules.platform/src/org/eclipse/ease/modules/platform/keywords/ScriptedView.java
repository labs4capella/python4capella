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

import java.util.HashMap;
import java.util.Map;

import org.eclipse.e4.ui.model.application.ui.basic.MPart;
import org.eclipse.e4.ui.workbench.modeling.EPartService;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.IWorkbenchListener;
import org.eclipse.ui.PlatformUI;

public class ScriptedView {

	public static final String SCRIPT_VARIABLE_VIEW = "view";
	public static final String SCRIPT_VARIABLE_COMPOSITE = "viewComposite";

	private Composite fParent;
	private IScriptEngine fScriptEngine;

	@jakarta.inject.Inject
	public ScriptedView(MPart part) {
		final IRepositoryService repositoryService = PlatformUI.getWorkbench().getService(IRepositoryService.class);
		final IScript script = repositoryService.getScript(part.getProperties().get("script"));

		createPartControl((Composite) part.getWidget(), script);

		// make sure to close this window before we terminate. Eclipse would store it in its layout actually destroying all layout data.
		final EPartService partService = PlatformUI.getWorkbench().getService(EPartService.class);
		PlatformUI.getWorkbench().addWorkbenchListener(new IWorkbenchListener() {

			@Override
			public boolean preShutdown(org.eclipse.ui.IWorkbench workbench, boolean forced) {
				partService.hidePart(part, true);
				fScriptEngine.terminate();
				return true;
			}

			@Override
			public void postShutdown(org.eclipse.ui.IWorkbench workbench) {
			}
		});
	}

	public void createPartControl(Composite parent, IScript script) {
		fParent = parent;

		final Map<String, Object> parameters = new HashMap<>();
		parameters.put(SCRIPT_VARIABLE_VIEW, this);
		parameters.put(SCRIPT_VARIABLE_COMPOSITE, parent);

		fScriptEngine = script.run(parameters);
		parent.addDisposeListener(e -> {
			fScriptEngine.terminate();
		});
	}

	/**
	 * Get the root composite for this view.
	 *
	 * @return root composite
	 */
	public Composite getComposite() {
		return fParent;
	}
}
