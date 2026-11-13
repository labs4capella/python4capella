/*******************************************************************************
 * Copyright (c) 2018 Bachmann electronic GmbH and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Bachmann electronic GmbH - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.modules.platform.build;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.IncrementalProjectBuilder;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;

/**
 * Provides capabilities to build workspace projects.
 *
 * <p>
 * A simple example of its use is:
 *
 * <pre>
 * loadModule("/System/Build");
 * build("MyProject", FULL_BUILD);
 * </pre>
 *
 * to trigger a full build of the project "MyProject".
 * </p>
 */
public class BuildModule extends AbstractScriptModule {

	/** Build kind constant indicating a full build request (6) */
	@WrapToScript
	public static final int FULL_BUILD = IncrementalProjectBuilder.FULL_BUILD;

	/** Build kind constant indicating a clean build request (15) */
	@WrapToScript
	public static final int CLEAN_BUILD = IncrementalProjectBuilder.CLEAN_BUILD;

	/** Build kind constant indicating an incremental build request (10). */
	@WrapToScript
	public static final int INCREMENTAL_BUILD = IncrementalProjectBuilder.INCREMENTAL_BUILD;

	private final IWorkspaceRoot fRoot;

	public BuildModule() {
		this(ResourcesPlugin.getWorkspace().getRoot());
	}

	protected BuildModule(IWorkspaceRoot root) {
		fRoot = root;
	}

	/**
	 * Builds a project with the given name and build kind.
	 *
	 * @scriptExample buildProject("myproject", CLEAN_BUILD); to make a clean build on the project "myproject"
	 * @param projectName
	 *            the project name
	 * @param buildKind
	 *            one of {@module #FULL_BUILD}, {@module #CLEAN_BUILD}, {@module #INCREMENTAL_BUILD}
	 * @throws CoreException
	 *             if the build fails
	 */
	@WrapToScript
	public void build(String projectName, @ScriptParameter(defaultValue = "6") int buildKind) throws CoreException {
		final IProject project = fRoot.getProject(projectName);
		if (project.isAccessible()) {
			project.build(buildKind, new NullProgressMonitor());
		}
	}

}
