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
package org.eclipse.python4capella.tests;

import static org.junit.Assert.assertEquals;

import org.eclipse.ease.modules.ModuleDefinition;
import org.eclipse.ease.modules.ModuleHelper;
import org.eclipse.python4capella.modules.CapellaModule;
import org.eclipse.python4capella.modules.EMFModule;
import org.eclipse.python4capella.modules.JavaModule;
import org.eclipse.python4capella.modules.SiriusModule;
import org.junit.Test;

public class ModulesTests {

	@Test
	public void capellaModuleIsRegistred() {
		final ModuleDefinition definition = ModuleHelper.resolveModuleName("/Capella/Capella");

		assertEquals("Capella", definition.getName());
		assertEquals(CapellaModule.class, definition.getModuleClass());
	}

	@Test
	public void emfModuleIsRegistred() {
		final ModuleDefinition definition = ModuleHelper.resolveModuleName("/Capella/EMF");

		assertEquals("EMF", definition.getName());
		assertEquals(EMFModule.class, definition.getModuleClass());
	}

	@Test
	public void javaModuleIsRegistred() {
		final ModuleDefinition definition = ModuleHelper.resolveModuleName("/Capella/Java");

		assertEquals("Java", definition.getName());
		assertEquals(JavaModule.class, definition.getModuleClass());
	}

	@Test
	public void siriusModuleIsRegistred() {
		final ModuleDefinition definition = ModuleHelper.resolveModuleName("/Capella/Sirius");

		assertEquals("Sirius", definition.getName());
		assertEquals(SiriusModule.class, definition.getModuleClass());
	}

}
