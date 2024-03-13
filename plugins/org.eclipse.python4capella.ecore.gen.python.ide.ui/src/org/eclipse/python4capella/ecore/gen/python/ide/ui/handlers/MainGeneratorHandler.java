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
package org.eclipse.python4capella.ecore.gen.python.ide.ui.handlers;

import java.util.Iterator;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.python4capella.ecore.gen.python.ide.ui.MainGeneratorEclipse;
import org.eclipse.ui.handlers.HandlerUtil;

/**
 * Command handler for org::eclipse::python4capella::ecore::gen::python::main::main.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 */
public class MainGeneratorHandler extends AbstractHandler {

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		final IStructuredSelection selection = HandlerUtil.getCurrentStructuredSelection(event);

		final Iterator<?> it = selection.iterator();
		while (it.hasNext()) {
			final Object selected = it.next();
			if (selected instanceof EPackage) {
				final MainGeneratorEclipse generator = new MainGeneratorEclipse((EPackage)selected);
				generator.generate();
			}
		}

		return null;
	}

}
