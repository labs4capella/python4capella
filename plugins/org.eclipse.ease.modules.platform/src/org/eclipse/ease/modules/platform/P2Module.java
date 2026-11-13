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

package org.eclipse.ease.modules.platform;

import java.net.URI;
import java.util.Collection;
import java.util.HashSet;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.OperationCanceledException;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.equinox.p2.core.IProvisioningAgent;
import org.eclipse.equinox.p2.core.ProvisionException;
import org.eclipse.equinox.p2.metadata.IInstallableUnit;
import org.eclipse.equinox.p2.operations.InstallOperation;
import org.eclipse.equinox.p2.operations.ProvisioningJob;
import org.eclipse.equinox.p2.operations.ProvisioningSession;
import org.eclipse.equinox.p2.operations.UpdateOperation;
import org.eclipse.equinox.p2.query.IQuery;
import org.eclipse.equinox.p2.query.IQueryResult;
import org.eclipse.equinox.p2.query.QueryUtil;
import org.eclipse.equinox.p2.repository.artifact.IArtifactRepositoryManager;
import org.eclipse.equinox.p2.repository.metadata.IMetadataRepositoryManager;
import org.eclipse.ui.PlatformUI;

/**
 * This module allows to interact with the eclipse p2 system that allows to modify the installed components.
 */
public class P2Module {

	/**
	 * Silently update the current installation using registered p2 sites.
	 */
	@WrapToScript
	public void checkForUpdates() {
		final IProvisioningAgent agent = PlatformUI.getWorkbench().getService(IProvisioningAgent.class);
		ProvisioningSession session = new ProvisioningSession(agent);

		UpdateOperation operation = new UpdateOperation(session);
		IStatus status = operation.resolveModal(null);
		if (status.getCode() != UpdateOperation.STATUS_NOTHING_TO_UPDATE) {

			if (status.getSeverity() == IStatus.CANCEL)
				throw new OperationCanceledException();

			if (status.getSeverity() != IStatus.ERROR) {
				ProvisioningJob job = operation.getProvisioningJob(null);
				status = job.runModal(null);
				if (status.getSeverity() == IStatus.CANCEL)
					throw new OperationCanceledException();
			}
		}

		if (status.getSeverity() == IStatus.ERROR)
			throw new RuntimeException(status.getMessage(), status.getException());
	}

	/**
	 * Register a new p2 update site.
	 *
	 * @param updateSite
	 *            site to register
	 * @throws ProvisionException
	 *             when repository cannot be created/loaded
	 * @throws OperationCanceledException
	 *             when user cancels the operation
	 */
	@WrapToScript
	public void registerUpdateSite(final String updateSite) throws ProvisionException, OperationCanceledException {
		URI location = URI.create(updateSite);

		final IProvisioningAgent agent = PlatformUI.getWorkbench().getService(IProvisioningAgent.class);

		// add metadata repository
		IMetadataRepositoryManager metadataManager = (IMetadataRepositoryManager) agent.getService(IMetadataRepositoryManager.SERVICE_NAME);
		if (metadataManager != null) {
			// for convenience create and add a repository here
			try {
				metadataManager.loadRepository(location, null);
			} catch (ProvisionException e) {
				// could not load a repo at that location so create one as a convenience
				String repositoryName = location + " - metadata"; //$NON-NLS-1$
				metadataManager.createRepository(location, repositoryName, IMetadataRepositoryManager.TYPE_SIMPLE_REPOSITORY, null);
			}

		} else
			throw new IllegalStateException("No metadata repository manager found"); //$NON-NLS-1$

		// add artifact repository
		IArtifactRepositoryManager artifactManager = (IArtifactRepositoryManager) agent.getService(IArtifactRepositoryManager.SERVICE_NAME);
		if (artifactManager != null) {
			try {
				artifactManager.loadRepository(location, null);
			} catch (ProvisionException e) {
				// could not load a repo at that location so create one as a convenience
				String repositoryName = location + " - artifacts"; //$NON-NLS-1$
				artifactManager.createRepository(location, repositoryName, IArtifactRepositoryManager.TYPE_SIMPLE_REPOSITORY, null);
			}

		} else
			throw new IllegalStateException("No metadata repository manager found"); //$NON-NLS-1$
	}

	/**
	 * Install a component into the running system.
	 * 
	 * @param component
	 *            component id. Either the name of a plugin or the id of a feature (= feature.name<i>.feature.group</i>)
	 */
	@WrapToScript
	public void install(final String component) {

		final IProvisioningAgent agent = PlatformUI.getWorkbench().getService(IProvisioningAgent.class);
		ProvisioningSession session = new ProvisioningSession(agent);

		// get installable units
		Collection<IInstallableUnit> installableUnits = new HashSet<IInstallableUnit>();
		IQuery<IInstallableUnit> query = QueryUtil.createIUQuery(component);
		// extract latest version only
		query = QueryUtil.createLatestQuery(query);

		IMetadataRepositoryManager metadataManager = (IMetadataRepositoryManager) agent.getService(IMetadataRepositoryManager.SERVICE_NAME);
		IQueryResult<IInstallableUnit> queryResult = metadataManager.query(query, null);

		if (!queryResult.toSet().isEmpty()) {
			InstallOperation op = new InstallOperation(session, queryResult.toSet());
			IStatus result = op.resolveModal(null);
			if (result.isOK()) {
				op.getProvisioningJob(null).schedule();
			}
		}
	}
}
