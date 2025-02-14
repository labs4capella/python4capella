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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Status;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.transaction.RollbackException;
import org.eclipse.emf.transaction.Transaction;
import org.eclipse.emf.transaction.impl.InternalTransaction;
import org.eclipse.emf.transaction.impl.InternalTransactionalEditingDomain;
import org.eclipse.emf.transaction.internal.EMFTransactionPlugin;
import org.eclipse.emf.transaction.internal.EMFTransactionStatusCodes;
import org.eclipse.emf.transaction.internal.l10n.Messages;
import org.eclipse.sirius.business.api.dialect.DialectManager;
import org.eclipse.sirius.business.api.query.DRepresentationDescriptorQuery;
import org.eclipse.sirius.business.api.query.EObjectQuery;
import org.eclipse.sirius.business.api.session.Session;
import org.eclipse.sirius.business.api.session.SessionManager;
import org.eclipse.sirius.common.tools.api.resource.ImageFileFormat;
import org.eclipse.sirius.diagram.DDiagram;
import org.eclipse.sirius.diagram.DDiagramElement;
import org.eclipse.sirius.ui.business.api.dialect.DialectUIManager;
import org.eclipse.sirius.ui.business.api.dialect.ExportFormat;
import org.eclipse.sirius.ui.tools.api.actions.export.SizeTooLargeException;
import org.eclipse.sirius.viewpoint.DRepresentation;
import org.eclipse.sirius.viewpoint.DRepresentationDescriptor;
import org.eclipse.sirius.viewpoint.DRepresentationElement;
import org.eclipse.sirius.viewpoint.description.Viewpoint;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.application.WorkbenchAdvisor;
import org.polarsys.capella.core.data.capellacore.EnumerationPropertyLiteral;
import org.polarsys.capella.core.data.capellamodeller.ModelRoot;
import org.polarsys.capella.core.data.capellamodeller.Project;
import org.polarsys.capella.core.data.capellamodeller.SystemEngineering;
import org.polarsys.capella.core.data.cs.Part;
import org.polarsys.capella.core.diagram.helpers.DiagramHelper;
import org.polarsys.capella.core.diagram.helpers.RepresentationAnnotationHelper;

/**
 * EASE module for Sirius.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
@SuppressWarnings("restriction")
public class SiriusModule {

	static {
		// initialize the workbench if needed
		if (!PlatformUI.isWorkbenchRunning()) {
			final Display display = PlatformUI.createDisplay();
			PlatformUI.createAndRunWorkbench(display, new WorkbenchAdvisor() {

				/**
				 * {@inheritDoc}
				 */
				@Override
				public boolean openWindows() {
					return false;
				}

				@Override
				public String getInitialWindowPerspectiveId() {
					return null;
				}

			});
		}
	}

	private final CapellaModule capellaModule = new CapellaModule();

	/**
	 * Mapping from a {@link Session} to its current {@link Transaction} if any.
	 */
	private final Map<Session, Stack<Transaction>> transactions = new HashMap<>();

	/**
	 * The {@link ExportFormat}.
	 */
	private static final ExportFormat FORMAT_DEFAULT = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.JPG);

	private static final ExportFormat FORMAT_SVG = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.SVG);

	private static final ExportFormat FORMAT_BMP = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.BMP);

	private static final ExportFormat FORMAT_GIF = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.GIF);

	private static final ExportFormat FORMAT_PNG = new ExportFormat(ExportFormat.ExportDocumentFormat.NONE,
			ImageFileFormat.PNG);

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
		if (session != null) {
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
					if (filePath.toUpperCase().endsWith("." + ImageFileFormat.PNG.getName())) {
						DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
								new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT_PNG,
								new NullProgressMonitor());
					} else if (filePath.toUpperCase().endsWith("." + ImageFileFormat.SVG.getName())) {
						DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
								new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT_SVG,
								new NullProgressMonitor());
					} else if (filePath.toUpperCase().endsWith("." + ImageFileFormat.GIF.getName())) {
						DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
								new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT_GIF,
								new NullProgressMonitor());
					} else if (filePath.toUpperCase().endsWith("." + ImageFileFormat.BMP.getName())) {
						DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
								new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT_BMP,
								new NullProgressMonitor());
					} else {
						DialectUIManager.INSTANCE.export(repDesc.getRepresentation(),
								new EObjectQuery(repDesc).getSession(), new Path(filePath), FORMAT_DEFAULT,
								new NullProgressMonitor());
					}

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

		if (session != null) {
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
		}

		return res;
	}

	/**
	 * Gets the {@link List} of {@link EObject} represented on the given
	 * {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @return the {@link List} of {@link EObject} represented on the given
	 *         {@link DRepresentationDescriptor}
	 */
	@WrapToScript
	public List<EObject> getRepresentedElements(DRepresentationDescriptor descriptor) {
		final List<EObject> res = new ArrayList<>();

		final DRepresentation representation = descriptor.getRepresentation();
		if (representation != null) {
			for (DRepresentationElement element : representation.getRepresentationElements()) {
				if (!(element instanceof DDiagramElement) || ((DDiagramElement) element).isVisible()) {
					final EObject target = element.getTarget();
					if (target instanceof Part) {
						res.add(((Part) target).getType());
					} else {
						res.add(target);
					}

				}
			}
		}

		return res;
	}

	/**
	 * Tells if the given {@link DRepresentationDescriptor} is visible in
	 * documentation.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * 
	 * @return <code>true</code> if the given {@link DRepresentationDescriptor} is
	 *         visible in documentation, <code>false</code> otherwise
	 */
	@WrapToScript
	public boolean isVisibleInDocumentation(DRepresentationDescriptor descriptor) {
		return RepresentationAnnotationHelper.isVisibleInDoc(descriptor);
	}

	/**
	 * Tells if the given {@link DRepresentationDescriptor} is visible for
	 * traceability.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * 
	 * @return <code>true</code> if the given {@link DRepresentationDescriptor} is
	 *         visible for traceability, <code>false</code> otherwise
	 */
	@WrapToScript
	public boolean isVisibleForTraceability(DRepresentationDescriptor descriptor) {
		return RepresentationAnnotationHelper.isVisibleInLM(descriptor);
	}

	/**
	 * Tells if the given {@link DRepresentationDescriptor} is syncronized.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @return <code>true</code> if the given {@link DRepresentationDescriptor} is
	 *         syncronized, <code>false</code> otherwise
	 */
	@WrapToScript
	public boolean isSynchronized(DRepresentationDescriptor descriptor) {
		return descriptor.getRepresentation() instanceof DDiagram
				&& ((DDiagram) descriptor.getRepresentation()).isSynchronized();
	}

	/**
	 * Gets the status of the given {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @return the status of the given {@link DRepresentationDescriptor}
	 */
	@WrapToScript
	public EnumerationPropertyLiteral getStatus(DRepresentationDescriptor descriptor) {
		return RepresentationAnnotationHelper.getProgressStatus(descriptor);
	}

	/**
	 * Sets the status of the given {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @param literal    the {@link EnumerationPropertyLiteral}
	 */
	@WrapToScript
	public void setStatus(DRepresentationDescriptor descriptor, EnumerationPropertyLiteral literal) {
		RepresentationAnnotationHelper.setProgressStatus(descriptor, literal);
	}

	/**
	 * Gets the review for the given {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @return the review for the given {@link DRepresentationDescriptor}
	 */
	@WrapToScript
	public String getReview(DRepresentationDescriptor descriptor) {
		return RepresentationAnnotationHelper.getStatusReview(descriptor);
	}

	/**
	 * Sets the review for the given {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @param review     the review
	 */
	@WrapToScript
	public void setReview(DRepresentationDescriptor descriptor, String review) {
		RepresentationAnnotationHelper.setStatusReview(descriptor, review);
	}

	/**
	 * Gets the {@link List} of all {@link DRepresentationDescriptor} for the given
	 * {@link Session}.
	 * 
	 * @param session the {@link Session}
	 * @return the {@link List} of all {@link DRepresentationDescriptor} for the
	 *         given {@link Session}
	 */
	@WrapToScript
	public List<DRepresentationDescriptor> getAllDiagrams(Session session) {
		final List<DRepresentationDescriptor> res = new ArrayList<>();

		if (session != null) {
			for (DRepresentationDescriptor descriptor : DialectManager.INSTANCE
					.getAllRepresentationDescriptors(session)) {
				res.add(descriptor);
			}
		}

		return res;
	}

	/**
	 * Gets the {@link List} of {@link DRepresentationDescriptor} for the given
	 * {@link Session}.
	 * 
	 * @param session the {@link Session}
	 * @return the {@link List} of {@link DRepresentationDescriptor} for the given
	 *         {@link Session}
	 */
	@WrapToScript
	public List<DRepresentationDescriptor> getDiagrams(Session session, String type) {
		final List<DRepresentationDescriptor> res = new ArrayList<>();

		for (DRepresentationDescriptor descriptor : DialectManager.INSTANCE.getAllRepresentationDescriptors(session)) {
			if (descriptor.getDescription().getName().equals(type)) {
				res.add(descriptor);
			}
		}

		return res;
	}

	/**
	 * Gets the {@link List} of {@link DRepresentationDescriptor} where the given
	 * {@link EObject} is represented.
	 * 
	 * @param eObject the {@link EObjectQuery}
	 * @return the {@link List} of {@link DRepresentationDescriptor} where the given
	 *         {@link EObject} is represented
	 */
	@WrapToScript
	public List<DRepresentationDescriptor> getRepresentingDiagrams(EObject eObject) {
		final List<DRepresentationDescriptor> res = new ArrayList<>();

		final Session session = new EObjectQuery(eObject).getSession();
		for (DRepresentationDescriptor descriptor : getAllDiagrams(session)) {
			if (getRepresentedElements(descriptor).contains(eObject)) {
				res.add(descriptor);
			}
		}

		return res;
	}

	/**
	 * Gets the {@link List} of {@link DRepresentationDescriptor} where the given
	 * {@link EObject} is a contextual element.
	 * 
	 * @param eObject the {@link EObjectQuery}
	 * @return the {@link List} of {@link DRepresentationDescriptor} where the given
	 *         {@link EObject} is a contextual element
	 */
	@WrapToScript
	public List<DRepresentationDescriptor> getContextualElementForDiagrams(EObject eObject) {
		final List<DRepresentationDescriptor> res = new ArrayList<>();

		final Session session = new EObjectQuery(eObject).getSession();
		for (DRepresentationDescriptor descriptor : getAllDiagrams(session)) {
			if (capellaModule.callQuery(
					"org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToContextualElement",
					descriptor).contains(eObject)) {
				res.add(descriptor);
			}
		}

		return res;
	}

	/**
	 * Gets the {@link Session} of the given {@link EObject}.
	 * 
	 * @param eObject the {@link EObject}
	 * @return the {@link Session} of the given {@link EObject} if any,
	 *         <code>null</code> otherwise
	 */
	@WrapToScript
	public Session getSession(EObject eObject) {
		return new EObjectQuery(eObject).getSession();
	}

	/**
	 * Starts a transaction for the given {@link Session}.
	 * 
	 * @param session the {@link Session}
	 */
	@WrapToScript
	public void startTransaction(Session session) {
		final InternalTransactionalEditingDomain internalDomain = (InternalTransactionalEditingDomain) session
				.getTransactionalEditingDomain();
		Transaction nested = null;

		try {
			nested = internalDomain.startTransaction(false, null);
		} catch (InterruptedException e) {
			// can't proceed with non-undoable changes
			internalDomain.getActiveTransaction().abort(new Status(IStatus.ERROR, EMFTransactionPlugin.getPluginId(),
					EMFTransactionStatusCodes.PRECOMMIT_INTERRUPTED, Messages.precommitInterrupted, e));
		}

		transactions.computeIfAbsent(session, s -> new Stack<Transaction>()).push(nested);
	}

	/**
	 * Commits the transaction for the given {@link Session}.
	 * 
	 * @param session the {@link Session}
	 */
	@WrapToScript
	public void commitTransaction(Session session) {
		final Transaction nested = getCurrentTransaction(session);

		final InternalTransactionalEditingDomain internalDomain = (InternalTransactionalEditingDomain) session
				.getTransactionalEditingDomain();
		final Transaction transaction = internalDomain.getActiveTransaction();
		if (nested != null) {
			if (transaction == null) {
				// failed to execute. Roll back
				nested.rollback();
			} else {
				try {
					nested.commit();
				} catch (RollbackException e) {
					// propagate the rollback
					((InternalTransaction) transaction).abort(e.getStatus());
				}
			}
		}

	}

	/**
	 * Rolls back the transaction for the given {@link Session}.
	 * 
	 * @param session the {@link Session}
	 */
	@WrapToScript
	public void rollbackTransaction(Session session) {
		final Transaction nested = getCurrentTransaction(session);

		if (nested != null) {
			nested.rollback();
		}
	}

	/**
	 * Gets the current {@link Transaction} for the given {@link Session}.
	 * 
	 * @param session the {@link Session}
	 * @return the current {@link Transaction} for the given {@link Session} if any,
	 *         <code>null</code> otherwise
	 */
	private Transaction getCurrentTransaction(Session session) {
		final Stack<Transaction> stack = transactions.get(session);
		if (stack == null || stack.isEmpty()) {
			throw new IllegalStateException("You need to call startTransaction() first.");
		}

		return stack.pop();
	}

	/**
	 * Creates a new {@link NullProgressMonitor}.
	 * 
	 * @return a new {@link NullProgressMonitor}
	 */
	@WrapToScript
	public IProgressMonitor createProgressMonitor() {
		return new NullProgressMonitor();
	}

	/**
	 * Gets the package name of the given {@link DRepresentationDescriptor}.
	 * 
	 * @param descriptor the {@link DRepresentationDescriptor}
	 * @return the package name of the given {@link DRepresentationDescriptor} if
	 *         any, <code>null</code> otherwise
	 */
	@WrapToScript
	public String getPackage(DRepresentationDescriptor descriptor) {
		return DiagramHelper.getService().getPackageName(descriptor);
	}
}
