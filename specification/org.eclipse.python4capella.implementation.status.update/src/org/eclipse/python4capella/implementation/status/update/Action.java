package org.eclipse.python4capella.implementation.status.update;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.xml.XMLConstants;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.diffmerge.diffdata.EComparison;
import org.eclipse.emf.diffmerge.diffdata.impl.EComparisonImpl;
import org.eclipse.emf.diffmerge.generic.api.Role;
import org.eclipse.emf.diffmerge.impl.policies.DefaultDiffPolicy;
import org.eclipse.emf.diffmerge.impl.policies.DefaultMatchPolicy;
import org.eclipse.emf.diffmerge.impl.policies.DefaultMergePolicy;
import org.eclipse.emf.diffmerge.impl.scopes.SubtreeModelScope;
import org.eclipse.emf.diffmerge.ui.util.DiffMergeDialog;
import org.eclipse.emf.diffmerge.ui.viewers.EMFDiffNode;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.emf.transaction.util.TransactionUtil;
import org.eclipse.jface.action.IAction;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.IObjectActionDelegate;
import org.eclipse.ui.IWorkbenchPart;
import org.polarsys.capella.core.data.capellacore.AbstractPropertyValue;
import org.polarsys.capella.core.data.capellacore.CapellacoreFactory;
import org.polarsys.capella.core.data.capellacore.Generalization;
import org.polarsys.capella.core.data.capellacore.PropertyValueGroup;
import org.polarsys.capella.core.data.capellacore.StringPropertyValue;
import org.polarsys.capella.core.data.capellamodeller.SystemEngineering;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.Operation;
import org.polarsys.capella.core.data.information.Property;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Action implements IObjectActionDelegate {

	private Shell shell;
	private SystemEngineering se;
	private SystemEngineering copySE;
	private static String pvgName = "ImplementationStatus";

	public Action() {
		super();
	}

	@Override
	public void run(IAction action) {

		// open window to select the xml file with the result of tests
		FileDialog dialog = new FileDialog(shell, SWT.OPEN);
		dialog.setFilterExtensions(new String[] { "*.xml" });
		String filePath = dialog.open();

		if (filePath != null) {

			String fileName = filePath.substring(filePath.lastIndexOf("\\") + 1, filePath.length());

			// prepare a copy of the model to perform modifications
			copySE = EcoreUtil.copy(se);

			List<String> testedElements = new ArrayList<String>();

			// parsing the xml file
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			System.out.println("Starting XML parsing");
			try {

				// optional, but recommended
				// process XML securely, avoid attacks like XML External Entities (XXE)
				dbf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

				// parse XML file
				DocumentBuilder db = dbf.newDocumentBuilder();

				Document doc = db.parse(new File(filePath));

				// optional, but recommended
				// http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
				doc.getDocumentElement().normalize();

				// get all of the test cases
				NodeList list = doc.getElementsByTagName("testcase");

				for (int i = 0; i < list.getLength(); i++) {
					System.out.println(" - Analyzing Node " + (i + 1) + "/" + list.getLength());
					Node node = list.item(i);
					if (node.getNodeType() == Node.ELEMENT_NODE) {
						Element element = (Element) node;
						String testName = element.getAttribute("name");
						Boolean isSetter;
						if (testName.endsWith("_setter")) {
							isSetter = true;
							testName = testName.substring(0, testName.length() - "_setter".length());
						} else if (testName.endsWith("_getter")) {
							isSetter = false;
							testName = testName.substring(0, testName.length() - "_getter".length());
						} else {
							isSetter = null;
						}
						List<String> listString = getElementAndFeatureName(testName);
						String className = listString.get(0);
						String featureNameWithUnderscore = listString.get(1);
						String featureName = switchToCamelCase(featureNameWithUnderscore);
						if (isSetter == null) {
//							featureName = featureName;
						} else if (isSetter) {
							featureName = featureName + "_setter";
						} else {
							featureName = featureName + "_getter";
						}

						// we add in the list of tested elements (to later check the untested elements)
						testedElements.add(className + ";" + featureName);
						// we check if we find the class and feature in order to avoid importing not
						// implemented stuff
						Class myClass = findClassByName(className);
						if (myClass != null) {
							if (getAllFeatures(myClass).contains(featureName)) {
								final String testResult;
								if (element.getElementsByTagName("error").getLength() > 0) {
									testResult = "KO";
								} else {
									testResult = "OK";
								}
								updateImplementationStatus(myClass, featureName, testResult);
							}
						}
					}
				}

			} catch (ParserConfigurationException | SAXException | IOException e) {
				e.printStackTrace();
			}

			System.out.println("XML parsing done");
			System.out.println("Adding status NOT_IMPLEMENTED");
			// add status "NOT_IMPLEMENTED" if the class/feature is not found in xml file +
			// remove old statuses
			TreeIterator<EObject> it = copySE.eAllContents();
			while (it.hasNext()) {
				EObject obj = it.next();
				if (obj instanceof Class) {
					Class myClass = (Class) obj;
					String className = myClass.getName();
					List<String> features = getAllFeatures(myClass);
					// add status "NOT_IMPLEMENTED"
					for (String featureName : features) {
						if (!testedElements.contains(className + ";" + featureName)) {
							updateImplementationStatus(myClass, featureName,  "NOT_IMPLEMENTED");
						}
					}
					// remove old tags
					PropertyValueGroup pvg = null;
					for (PropertyValueGroup pvgit : myClass.getOwnedPropertyValueGroups()) {
						if (pvgit.getName().equals(pvgName)) {
							pvg = pvgit;
							break;
						}
					}
					if (pvg != null) {
						List<AbstractPropertyValue> toBeDestroyed = new ArrayList<AbstractPropertyValue>();
						for (AbstractPropertyValue pv : pvg.getOwnedPropertyValues()) {
							if (!features.contains(pv.getName())) {
								toBeDestroyed.add(pv);
							}
						}
						for (AbstractPropertyValue apv : toBeDestroyed) {
							apv.destroy();
						}
					}
				}
			}

			System.out.println("preparing diff/merge");
			// preparing diff / merge
			SubtreeModelScope targetScope = new SubtreeModelScope(copySE) {
				public Object getOriginator() {
					return fileName;
				};
			};
			SubtreeModelScope referenceScope = new SubtreeModelScope(se) {
				@Override
				public Object getOriginator() {
					return se.getName();
				}
			};

			DefaultMatchPolicy matchPolicy = new DefaultMatchPolicy();
			DefaultDiffPolicy diffPolicy = new DefaultDiffPolicy();
			DefaultMergePolicy mergePolicy = new DefaultMergePolicy();

			EComparisonImpl comparison = new EComparisonImpl(targetScope, referenceScope);
			comparison.compute(matchPolicy, diffPolicy, mergePolicy, new NullProgressMonitor());
			TransactionalEditingDomain domain = TransactionUtil.getEditingDomain(se);

			final EMFDiffNode diffNode = new EMFDiffNode((EComparison) comparison, domain, false, true);
			diffNode.setReferenceRole(Role.REFERENCE);
			final Display display = Display.getDefault();
			display.syncExec(new Runnable() {
				public void run() {
					DiffMergeDialog dialog = new DiffMergeDialog(display.getActiveShell(),
							"Confirm Implementation Status update", diffNode);
					dialog.open();
				}
			});
		}
	}

	@Override
	public void selectionChanged(IAction action, ISelection selection) {
		if (selection instanceof IStructuredSelection) {
			IStructuredSelection ss = (IStructuredSelection) selection;
			if (ss.getFirstElement() instanceof SystemEngineering) {
				se = (SystemEngineering) ss.getFirstElement();
			}
		}
	}

	@Override
	public void setActivePart(IAction action, IWorkbenchPart targetPart) {
		shell = targetPart.getSite().getShell();
	}

	private List<String> getElementAndFeatureName(String testName) {
		List<String> result = new ArrayList<String>();
		int i = testName.indexOf("_");
		// we remove the first part which is normally "test_"
		String subString = testName.substring(i + 1);
		int j = subString.indexOf("_");
		result.add(subString.substring(0, j));
		result.add(subString.substring(j + 1, subString.length()));
		return result;
	}

	private Class findClassByName(String className) {
		TreeIterator<EObject> it = copySE.eAllContents();
		while (it.hasNext()) {
			EObject obj = it.next();
			if (obj instanceof Class) {
				Class thisClass = (Class) obj;
				if (thisClass.getName().equals(className)) {
					return thisClass;
				}
			}
		}
		return null;
	}

	private List<String> getAllFeatures(Class myClass) {
		List<String> features = new ArrayList<String>();
		for (Property att : getAllProperties(myClass)) {
			features.add(att.getName() + "_getter");
			if (!att.isIsReadOnly()) {
				features.add(att.getName() + "_setter");
			}
		}
		for (Operation op : getAllOperations(myClass)) {
			features.add(op.getName());
		}
		return features;
	}

	private String switchToCamelCase(String text) {
		int i = text.indexOf("_");
		if (i == -1) {
			return text;
		}
		return text.substring(0, i) + text.substring(i + 1, i + 2).toUpperCase()
				+ switchToCamelCase(text.substring(i + 2, text.length()));
	}

	private void updateImplementationStatus(Class myClass, String featureName, String result) {
		if (myClass != null) {
			// only specialized classes are tested, so we can skip abstract classes
			if (!myClass.isAbstract()) {
				// now trying to get the PV Group
				PropertyValueGroup pvg = null;
				for (PropertyValueGroup pvgit : myClass.getOwnedPropertyValueGroups()) {
					if (pvgit.getName().equals(pvgName)) {
						pvg = pvgit;
						break;
					}
				}
				if (pvg == null) {
					pvg = CapellacoreFactory.eINSTANCE.createPropertyValueGroup();
					pvg.setName(pvgName);
					myClass.getOwnedPropertyValueGroups().add(pvg);
				}

				// now trying to get the right PV
				StringPropertyValue pv = null;
				for (AbstractPropertyValue apv : pvg.getOwnedPropertyValues()) {
					if (apv instanceof StringPropertyValue) {
						StringPropertyValue spv = (StringPropertyValue) apv;
						if (spv.getName().equals(featureName)) {
							pv = spv;
							break;
						}
					}
				}
				if (pv != null) {
					if (!pv.getValue().equals(result)) {
						pv.setValue(result);
					}
				} else {
					StringPropertyValue newPV = CapellacoreFactory.eINSTANCE.createStringPropertyValue();
					newPV.setName(featureName);
					newPV.setValue(result);
					pvg.getOwnedPropertyValues().add(newPV);
				}
			}
		}
	}

	public List<Class> getAllSuperTypes(Class myClass) {
		List<Class> result = new ArrayList<Class>();
		for (Generalization gen : myClass.getOwnedGeneralizations()) {
			if (gen.getSuper() instanceof Class) {
				Class supClass = (Class) gen.getSuper();
				for (Class supsupClass : getAllSuperTypes(supClass)) {
					if (!result.contains(supsupClass)) {
						result.add(supsupClass);
					}
				}
				if (!result.contains(supClass)) {
					result.add(supClass);
				}
			}
		}
		return result;
	}

	public List<Property> getAllProperties(Class myClass) {
		List<Property> result = new ArrayList<Property>();
		for (Class supClass : getAllSuperTypes(myClass)) {
			result.addAll(getProperties(supClass));
		}
		result.addAll(getProperties(myClass));
		return result;
	}

	public List<Property> getProperties(Class myClass) {
		return myClass.getContainedProperties();
	}

	public List<Operation> getAllOperations(Class myClass) {
		List<Operation> result = new ArrayList<Operation>();
		for (Class supClass : getAllSuperTypes(myClass)) {
			result.addAll(getOperations(supClass));
		}
		result.addAll(getOperations(myClass));
		return result;
	}

	public List<Operation> getOperations(Class myClass) {
		return myClass.getContainedOperations();
	}

}
