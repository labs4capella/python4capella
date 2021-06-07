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

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EPackage;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.kitalpha.emde.model.ElementExtension;
import org.polarsys.kitalpha.emde.model.ExtensibleElement;

/**
 * EASE module for Capella.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 *
 */
public class CapellaModule {

	/**
	 * Gets the {@link List} of {@link ElementExtension} with the given
	 * {@link EPackage#getNsURI() nsURI} and {@link EClass#getName() eclass name}
	 * type for the given {@link ExtensibleElement}.
	 * 
	 * @param element    the {@link ExtensibleElement}
	 * @param nsURI      the {@link EPackage#getNsURI() nsURI}
	 * @param eClassName the {@link EClass#getName() eclass name}
	 * @return the {@link List} of {@link ElementExtension} with the given
	 *         {@link EPackage#getNsURI() nsURI} and {@link EClass#getName() eclass
	 *         name} type for the given {@link ExtensibleElement}
	 */
	@WrapToScript
	public List<ElementExtension> getExtensions(ExtensibleElement element, String nsURI, String eClassName) {
		final List<ElementExtension> res = new ArrayList<>();

		final EClassifier eClassifier = EPackage.Registry.INSTANCE.getEPackage(nsURI).getEClassifier(eClassName);

		for (ElementExtension extension : element.getOwnedExtensions()) {
			if (eClassifier.isInstance(extension)) {
				res.add(extension);
			}
		}

		return res;
	}

	/**
	 * Calls the {@link IQuery} by its {@link Class#getCanonicalName() class
	 * canonical name} on the given {@link Object}.
	 * 
	 * @param queryClass the {@link Class#getCanonicalName() class canonical name}
	 * @param object     the {@link Object}
	 * @return result of the call
	 */
	@WrapToScript
	public List<Object> callQuery(String queryClass, Object object) {
		try {
			IQuery query = (IQuery) getClass().getClassLoader().loadClass(queryClass).getConstructor().newInstance();
			return query.compute(object);
		} catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException
				| NoSuchMethodException | SecurityException | ClassNotFoundException e) {
			throw new IllegalStateException(queryClass + " query can't be loaded.", e);
		}
	}

//	@WrapToScript
//	public boolean isInstanceOf(Object element, String className) {
//		if (element != null && className != null) {
//			try {
//				Class<?> forName = Class.forName(className);
//				return forName.isAssignableFrom(element.getClass());
//			} catch (ClassNotFoundException e) {
//				e.printStackTrace();
//			}
//		}
//		return false;
//	}
//
//	@WrapToScript
//	public boolean isCapellaRootElement(Object element) {
//		return element instanceof SystemEngineering;
//	}
//
//	@WrapToScript
//	public ComponentArchitecture getPackage(SystemEngineering se, String packageName) {
//		if (se != null) {
//			return se.getContainedPhysicalArchitectures().get(0);
//		}
//		return null;
//	}
//
//	@WrapToScript
//	public PhysicalComponent getPhysicalSystem(ComponentArchitecture pa) {
//		if (pa instanceof PhysicalArchitecture) {
//			return ((PhysicalArchitecture) pa).getOwnedPhysicalComponentPkg().getOwnedPhysicalComponents().get(0);
//		}
//		return null;
//	}
//
//	@WrapToScript
//	public Collection<PhysicalComponent> getPhysicalComponents(PhysicalComponent ps) {
//		if (ps != null) {
//			Collection<PhysicalComponent> temp = new ArrayList<PhysicalComponent>();
//			Collection<PhysicalComponent> result = new ArrayList<PhysicalComponent>();
//			temp.addAll(ps.getSubPhysicalComponents().get(0).getOwnedPhysicalComponents());
//			result.addAll(ps.getSubPhysicalComponents().get(0).getOwnedPhysicalComponents());
//			for (PhysicalComponent pc : temp) {
//				if (pc != null) {
//					result.addAll(pc.getOwnedPhysicalComponents());
//				}
//			}
//			return result;
//		}
//		return Collections.emptyList();
//	}
//
//	@WrapToScript
//	public boolean isComponentLinkedTo(PhysicalComponent pc1, PhysicalComponent pc2) {
//		if (pc1 != null && pc2 != null && !pc1.equals(pc2)) {
//			EList<PhysicalPort> sourcePorts = pc1.getContainedPhysicalPorts();
//			EList<PhysicalPort> targetPorts = pc2.getContainedPhysicalPorts();
//			for (PhysicalPort sourcePort : sourcePorts) {
//				EList<PhysicalLink> links = sourcePort.getInvolvedLinks();
//				for (PhysicalLink link : links) {
//					PhysicalPort targetPhysicalPort = link.getTargetPhysicalPort();
//					if (sourcePort.equals(link.getSourcePhysicalPort()) && targetPhysicalPort != null
//							&& targetPorts.contains(targetPhysicalPort)) {
//						return true;
//					}
//				}
//			}
//		}
//		return false;
//	}
//
//	@WrapToScript
//	public HSSFWorkbook createExcel() {
//		HSSFWorkbook book = new HSSFWorkbook();
//		book.createSheet("Capella");
//		return book;
//	}
//
//	@WrapToScript
//	public void addLine(HSSFWorkbook book, int i, EObject e) {
//		HSSFSheet sheet = book.getSheet("Capella");
//		HSSFRow row = sheet.createRow(i + 1);
//		HSSFCell cell = row.createCell(0);
//		cell.setCellValue(getName(e));
//	}
//
//	@WrapToScript
//	public void addColumn(HSSFWorkbook book, int i, EObject e) {
//		HSSFSheet sheet = book.getSheet("Capella");
//		HSSFRow row = sheet.getRow(0);
//		if (row == null) {
//			row = sheet.createRow(0);
//		}
//		HSSFCell cell = row.createCell(i + 1);
//		cell.setCellValue(getName(e));
//	}
//
//	@WrapToScript
//	public void addCell(HSSFWorkbook book, int rowIndex, int columnIndex, String value) {
//		HSSFSheet sheet = book.getSheet("Capella");
//		HSSFRow row = sheet.getRow(rowIndex + 1);
//		if (row == null) {
//			row = sheet.createRow(rowIndex + 1);
//		}
//		HSSFCell cell = row.getCell(columnIndex + 1);
//		if (cell == null) {
//			cell = row.createCell(columnIndex + 1);
//		}
//		cell.setCellValue(value);
//	}
//
//	@WrapToScript
//	public void writeExcel(HSSFWorkbook book, String absolutePath) {
//		try {
//			File f = new File(absolutePath);
//			f.createNewFile();
//			FileOutputStream outputStream = new FileOutputStream(absolutePath);
//			book.write(outputStream);
//			outputStream.close();
//		} catch (IOException e) {
//			e.printStackTrace();
//		}
//	}
//
//	private String getName(EObject e) {
//		EAttribute namingAttribute = NameHelper.getNamingAttribute(e);
//		if (namingAttribute != null) {
//			Object name = e.eGet(namingAttribute);
//			if (name != null) {
//				return name.toString();
//			}
//		}
//		return "NO NAME";
//	}

}
