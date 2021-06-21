/**
 *   Copyright (c) 2021 THALES GLOBAL SERVICES
 *  This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License 2.0
 *  which accompanies this distribution, and is available at
 *  https://www.eclipse.org/legal/epl-2.0/
 *
 *  SPDX-License-Identifier: EPL-2.0
 *
 *  Contributors:
 *       Obeo - Initial API and implementation
 */
package org.eclipse.python4capella.modules;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.sirius.business.api.dialect.DialectManager;
import org.eclipse.sirius.business.api.query.DRepresentationDescriptorQuery;
import org.eclipse.sirius.business.api.query.EObjectQuery;
import org.eclipse.sirius.business.api.session.Session;
import org.eclipse.sirius.business.api.session.SessionManager;
import org.eclipse.sirius.common.tools.api.resource.ImageFileFormat;
import org.eclipse.sirius.ui.business.api.dialect.DialectUIManager;
import org.eclipse.sirius.ui.business.api.dialect.ExportFormat;
import org.eclipse.sirius.ui.tools.api.actions.export.SizeTooLargeException;
import org.eclipse.sirius.viewpoint.DRepresentation;
import org.eclipse.sirius.viewpoint.DRepresentationDescriptor;
import org.eclipse.sirius.viewpoint.description.Viewpoint;
import org.eclipse.swt.widgets.Display;
import org.polarsys.capella.core.data.capellamodeller.ModelRoot;
import org.polarsys.capella.core.data.capellamodeller.Project;
import org.polarsys.capella.core.data.capellamodeller.SystemEngineering;

/**
 * EASE module for Sirius.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class SiriusModule {

	/**
	 * The {@link ExportFormat}.
	 */
	private static final ExportFormat FORMAT = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.JPG);

	/**
	 * Gets the {@link DRepresentationDescriptor} for a given {@link EObject}.
	 * 
	 * @param eObj the {@link EObject}
	 * @return
	 */
	@WrapToScript
	public List<DRepresentationDescriptor> getRepresentationDescriptors(EObject eObj) {
		final List<DRepresentationDescriptor> res = new ArrayList<>();

		final Session session = new EObjectQuery(eObj).getSession();
		final Collection<DRepresentationDescriptor> repDescs = DialectManager.INSTANCE
				.getRepresentationDescriptors(eObj, session);
		// Filter representations to keep only those in a selected viewpoint
		final Collection<Viewpoint> selectedViewpoints = session.getSelectedViewpoints(false);

		for (DRepresentationDescriptor repDesc : repDescs) {
			boolean isDangling = new DRepresentationDescriptorQuery(repDesc).isDangling();
			if (!isDangling && repDesc.getDescription().eContainer() instanceof Viewpoint) {
				Viewpoint vp = (Viewpoint) repDesc.getDescription().eContainer();
				if (selectedViewpoints.contains(vp)) {
					res.add(repDesc);
				}
			}
		}

		return res;
	}

	/**
	 * Exports the given {@link DRepresentation} as an image file located at the
	 * given file path.
	 * 
	 * @param representation the {@link DRepresentation} to export
	 * @param filePath       the file path
	 * @throws SizeTooLargeException if the image is too large
	 */
	@WrapToScript
	public void exportImage(final DRepresentationDescriptor repDesc, final String filePath) {
		Display.getDefault().syncExec(new Runnable() {

			@Override
			public void run() {
				try {
					DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
							new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT,
							new NullProgressMonitor());
				} catch (SizeTooLargeException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Loads the {@link Session} at the given aird file path.
	 * 
	 * @param airdPath the aird path
	 * @return the loaded {@link Session}
	 */
	@WrapToScript
	public Session loadSiriusSession(String airdPath) {
		final Session session = SessionManager.INSTANCE.getSession(URI.createPlatformResourceURI(airdPath, true),
				new NullProgressMonitor());

		if (session != null && !session.isOpen()) {
			session.open(new NullProgressMonitor());
		}

		return session;
	}

	/**
	 * Gets the first {@link SystemEngineering} contained by the given
	 * {@link Session}.
	 * 
	 * @param session the {@link Session}
	 * @return the first {@link SystemEngineering} contained by the given
	 *         {@link Session} if any, <code>null</code> otherwise
	 */
	@WrapToScript
	public SystemEngineering getEngineering(Session session) {
		SystemEngineering res = null;

		found: for (Resource resource : session.getSemanticResources()) {
			for (EObject root : resource.getContents()) {
				if (root instanceof Project) {
					for (ModelRoot modelRoot : ((Project) root).getOwnedModelRoots()) {
						if (modelRoot instanceof SystemEngineering) {
							res = (SystemEngineering) modelRoot;
							break found;
						}
					}
				}
			}
		}

		return res;
	}

}
