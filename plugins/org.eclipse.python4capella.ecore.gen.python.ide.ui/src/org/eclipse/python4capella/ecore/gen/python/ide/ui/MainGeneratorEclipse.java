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

import org.eclipse.acceleo.aql.evaluation.GenerationResult;
import org.eclipse.acceleo.aql.ide.ui.dialog.AbstractResourceSelectionDialog;
import org.eclipse.acceleo.aql.ide.ui.dialog.FolderSelectionDialog;
import org.eclipse.acceleo.query.ast.TypeLiteral;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameQueryEnvironment;
import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.jface.dialogs.IDialogConstants;
import org.eclipse.python4capella.ecore.gen.python.main.MainGenerator;
import org.eclipse.ui.PlatformUI;

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
	 */
	private final List<EObject> value;

	/**
	 * Constructor.
	 * 
	 * @param selected
	 *            the selected {@link EPackage}
	 * @generated
	 */
	public MainGeneratorEclipse(EPackage selected) {
		super(Collections.emptyList(), getTarget(selected));
		this.value = Collections.singletonList(selected);
	}

	/**
	 * @generated
	 */
	@Override
	protected List<EObject> getValues(IQualifiedNameQueryEnvironment queryEnvironment,
			Map<EClass, List<EObject>> valuesCache, TypeLiteral type, ResourceSet resourceSetForModels) {
		return value;
	}

	/**
	 * Gets the target folder for the selected {@link EPackage}.
	 * 
	 * @param selected
	 *            the model {@link EPackage}
	 * @return the target folder for the selected {@link EPackage}
	 * @generated
	 */
	private static String getTarget(EPackage selected) {
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
			switch (diagnostic.getSeverity()) {
				case Diagnostic.INFO:
					Activator.getDefault().log(new Status(IStatus.INFO, diagnostic.getSource(), diagnostic
							.getMessage(), diagnostic.getException()));
					break;

				case Diagnostic.WARNING:
					Activator.getDefault().log(new Status(IStatus.WARNING, diagnostic.getSource(), diagnostic
							.getMessage(), diagnostic.getException()));
					break;

				case Diagnostic.ERROR:
					Activator.getDefault().log(new Status(IStatus.ERROR, diagnostic.getSource(), diagnostic
							.getMessage(), diagnostic.getException()));
					break;
			}
		}
		for (Diagnostic child : diagnostic.getChildren()) {
			printDiagnostic(child);
		}
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
				Activator.getDefault().log(new Status(IStatus.ERROR, getClass(), "could not refresh "
						+ targetWorkspaceContainer.getFullPath(), e));
			}
		}
	}

}
