//Start of user code copyright
/*******************************************************************************
 *  Copyright (c) 2024 Obeo. 
 *  All rights reserved. This program and the accompanying materials
 *  are made available under the terms of the Eclipse Public License v2.0
 *  which accompanies this distribution, and is available at
 *  http://www.eclipse.org/legal/epl-v20.html
 *   
 *   Contributors:
 *       Obeo - initial API and implementation
 *  
 *******************************************************************************/
//End of user code

package org.eclipse.python4capella.ecore.gen.python.ide.ui;

//Start of user code imports

import java.io.File;
import java.io.PrintStream;
import java.util.Collections;
import java.util.List;
import java.util.Map;

import org.eclipse.acceleo.aql.AcceleoUtil;
import org.eclipse.acceleo.aql.evaluation.GenerationResult;
import org.eclipse.acceleo.aql.ide.ui.dialog.AbstractResourceSelectionDialog;
import org.eclipse.acceleo.aql.ide.ui.dialog.FolderSelectionDialog;
import org.eclipse.acceleo.aql.parser.AcceleoParser;
import org.eclipse.acceleo.query.ast.ASTNode;
import org.eclipse.acceleo.query.ast.TypeLiteral;
import org.eclipse.acceleo.query.ide.runtime.impl.namespace.OSGiQualifiedNameResolver;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameQueryEnvironment;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameResolver;
import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.python4capella.ecore.gen.python.main.MainGenerator;
import org.eclipse.ui.PlatformUI;
import org.osgi.framework.Bundle;

//End of user code

/**
 * Eclipse launcher for org::eclipse::python4capella::ecore::gen::python::main::main.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 * @generated
 */
public class MainGeneratorEclipse extends MainGenerator {

	/**
	 * The selected value.
	 * 
	 * @generated
	 */
	private final List<EObject> values;

	/**
	 * Constructor.
	 * 
	 * @param selected
	 *            the selected {@link IFile}
	 * @generated
	 */
	public MainGeneratorEclipse(IFile selected) {
		super(Collections.singletonList(selected.getLocation().toString()), getTarget(selected));
		this.values = null;
	}

	/**
	 * Constructor.
	 * 
	 * @param selected
	 *            the selected {@link EPackage}
	 * @generated
	 */
	public MainGeneratorEclipse(EPackage selected) {
		super(Collections.emptyList(), getTarget(selected));
		this.values = Collections.singletonList(selected);
	}

	/**
	 * @generated
	 */
	@Override
	protected List<EObject> getValues(IQualifiedNameQueryEnvironment queryEnvironment,
			Map<EClass, List<EObject>> valuesCache, TypeLiteral type, ResourceSet resourceSetForModels) {
		final List<EObject> res;

		if (values != null) {
			res = values;
		} else {
			res = super.getValues(queryEnvironment, valuesCache, type, resourceSetForModels);
		}

		return res;

	}

	/**
	 * @generated
	 */
	@Override
	protected void loadResources(ResourceSet resourceSetForModels, List<String> resources) {
		for (String resource : resources) {
			resourceSetForModels.getResource(URI.createFileURI(resource), true);
		}
	}

	/**
	 * @generated
	 */
	@Override
	protected void standaloneInitialization(ResourceSet resourceSetForModels) {
		// nothing to do here
	}

	/**
	 * @generated
	 */
	@Override
	protected IQualifiedNameResolver createResolver() {
		final String bundleIdentifier = "org.eclipse.python4capella.ecore.gen.python";
		final Bundle bundle = Platform.getBundle(bundleIdentifier);
		if (bundle == null || bundle.getState() == Bundle.UNINSTALLED) {
			Activator.getDefault().log(new Status(IStatus.ERROR, getClass(), "The Bundle " + bundleIdentifier
					+ " must be available in the target platform."));
		}
		return new OSGiQualifiedNameResolver(bundle, AcceleoParser.QUALIFIER_SEPARATOR);
	}

	/**
	 * Gets the target folder for the selected {@link EPackage} or selected {@link IFile}.
	 * 
	 * @param selected
	 *            the model {@link EPackage} or selected {@link IFile}
	 * @return the target folder for the selected {@link EPackage} or selected {@link IFile}
	 * @generated
	 */
	private static String getTarget(Object selected) {
		final String res;

		final AbstractResourceSelectionDialog dialog = new FolderSelectionDialog(PlatformUI.getWorkbench()
				.getActiveWorkbenchWindow().getShell(), "Select the destination folder", "");
		final int dialogResult = dialog.open();
		if ((dialogResult == IDialogConstants.OK_ID) && dialog.getFileName() != null && !dialog.getFileName()
				.isEmpty()) {
			final Path location = new Path(dialog.getFileName());
			IWorkspaceRoot workspaceRoot = ResourcesPlugin.getWorkspace().getRoot();
			if (location.segmentCount() == 1) {
				res = workspaceRoot.getProject(location.segment(0)).getLocation().toFile().getAbsolutePath();
			} else {
				res = workspaceRoot.getFolder(location).getLocation().toFile().getAbsolutePath();
			}
		} else {
			res = null;
		}

		return res;
	}

	/**
	 * @generated
	 */
	@Override
	public void generate() {
		if (target != null) {
			super.generate();
		}
	}

	/**
	 * Prints the diagnostics for the given {@link GenerationResult}.
	 * 
	 * @param generationResult
	 *            the {@link GenerationResult}
	 * @generated
	 */
	protected void printDiagnostics(GenerationResult generationResult) {
		if (generationResult.getDiagnostic().getSeverity() > Diagnostic.INFO) {
			printDiagnostic(generationResult.getDiagnostic());
		}
		printSummary(generationResult);
	}

	/**
	 * Prints the given {@link Diagnostic} for the given {@link PrintStream}.
	 * 
	 * @param stream
	 *            the {@link PrintStream}
	 * @param diagnostic
	 *            the {@link Diagnostic}
	 * @param indentation
	 *            the current indentation
	 * @generated
	 */
	protected void printDiagnostic(Diagnostic diagnostic) {
		if (diagnostic.getMessage() != null) {
			final String location;
			if (!diagnostic.getData().isEmpty() && diagnostic.getData().get(0) instanceof ASTNode) {
				location = AcceleoUtil.getLocation((ASTNode)diagnostic.getData().get(0)) + ": ";
			} else {
				location = "";
			}
			switch (diagnostic.getSeverity()) {
				case Diagnostic.INFO:
					Activator.getDefault().log(new Status(IStatus.INFO, diagnostic.getSource(), location
							+ diagnostic.getMessage(), diagnostic.getException()));
					break;

				case Diagnostic.WARNING:
					Activator.getDefault().log(new Status(IStatus.WARNING, diagnostic.getSource(), location
							+ diagnostic.getMessage(), diagnostic.getException()));
					break;

				case Diagnostic.ERROR:
					Activator.getDefault().log(new Status(IStatus.ERROR, diagnostic.getSource(), location
							+ diagnostic.getMessage(), diagnostic.getException()));
					break;
			}
		}
		for (Diagnostic child : diagnostic.getChildren()) {
			printDiagnostic(child);
		}
	}

	/**
	 * Prints the summary of the generation.
	 * 
	 * @param result
	 *            the {@link GenerationResult}
	 * @generated
	 */
	protected void printSummary(GenerationResult result) {
		int nbErrors = 0;
		int nbWarnings = 0;
		int nbInfos = 0;
		for (Diagnostic diagnostic : result.getDiagnostic().getChildren()) {
			switch (diagnostic.getSeverity()) {
				case Diagnostic.ERROR:
					nbErrors++;
					break;

				case Diagnostic.WARNING:
					nbWarnings++;
					break;

				case Diagnostic.INFO:
					nbInfos++;
					break;

				default:
					break;
			}
		}

		final String message = "Files: " + result.getGeneratedFiles().size() + ", Lost Files: " + result
				.getLostFiles().size() + ", Errors: " + nbErrors + ", Warnings: " + nbWarnings + ", Infos: "
				+ nbInfos + ".";
		Activator.getDefault().log(new Status(IStatus.INFO, getClass(), message));
	}

	/**
	 * @generated
	 */
	@Override
	protected void afterGeneration(GenerationResult generationResult) {
		super.afterGeneration(generationResult);

		// refresh if the generated files are in the workspace
		final File targetFolder = new File(target);
		final IContainer targetWorkspaceContainer = ResourcesPlugin.getWorkspace().getRoot()
				.getContainerForLocation(new Path(targetFolder.getAbsolutePath()));
		if (targetWorkspaceContainer != null) {
			try {
				targetWorkspaceContainer.refreshLocal(IResource.DEPTH_INFINITE, new NullProgressMonitor());
			} catch (CoreException e) {
				Activator.getDefault().log(new Status(IStatus.ERROR, Activator.PLUGIN_ID, "could not refresh "
						+ targetWorkspaceContainer.getFullPath(), e));
			}
		}
	}

}
