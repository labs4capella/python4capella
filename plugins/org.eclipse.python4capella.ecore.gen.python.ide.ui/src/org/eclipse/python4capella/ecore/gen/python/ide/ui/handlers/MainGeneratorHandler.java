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

package org.eclipse.python4capella.ecore.gen.python.ide.ui.handlers;

//Start of user code imports

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.SubMonitor;
import org.eclipse.emf.common.util.BasicMonitor;
import org.eclipse.emf.common.util.Monitor;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.jface.operation.IRunnableWithProgress;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.python4capella.ecore.gen.python.ide.ui.Activator;
import org.eclipse.python4capella.ecore.gen.python.ide.ui.MainGeneratorEclipse;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.handlers.HandlerUtil;

//End of user code

/**
 * Command handler for org::eclipse::python4capella::ecore::gen::python::main::main.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 * @generated
 */
public class MainGeneratorHandler extends AbstractHandler {

	/**
	 * @generated
	 */
	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		final IStructuredSelection selection = HandlerUtil.getCurrentStructuredSelection(event);

		final IRunnableWithProgress generateRunnable = new IRunnableWithProgress() {

			@Override
			public void run(IProgressMonitor monitor) throws InvocationTargetException, InterruptedException {
				final Iterator<?> it = selection.iterator();
				final List<Object> selectedList = new ArrayList<>();
				while (it.hasNext()) {
					selectedList.add(it.next());
				}
				final SubMonitor subMonitor = SubMonitor.convert(monitor, selectedList.size());
				for (Object selected : selectedList) {
					final Monitor childMonitor = BasicMonitor.toMonitor(subMonitor.split(1));
					final MainGeneratorEclipse generator;
					try {
						if (selected instanceof EPackage) {
							generator = new MainGeneratorEclipse((EPackage)selected);
							generator.generate(childMonitor);
						} else if (selected instanceof IFile) {
							generator = new MainGeneratorEclipse((IFile)selected);
							generator.generate(childMonitor);
						}
					} finally {
						childMonitor.done();
					}
					if (monitor.isCanceled()) {
						break;
					}
				}
			}
		};

		try {
			PlatformUI.getWorkbench().getProgressService().run(true, true, generateRunnable);
		} catch (InvocationTargetException e) {
			Activator.getDefault().log(new Status(IStatus.ERROR, getClass(), "Couldn't generate.", e
					.getTargetException()));
		} catch (InterruptedException e) {
			Activator.getDefault().log(new Status(IStatus.ERROR, getClass(), "Couldn't generate.", e));
		}

		return null;
	}

}
