package org.eclipse.python4capella.gen.handlers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringJoiner;
import java.util.stream.Collectors;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.ui.handlers.HandlerUtil;
import org.polarsys.capella.core.data.capellacore.Feature;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.capellacore.TypedElement;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.DataPkg;
import org.polarsys.capella.core.data.information.Operation;
import org.polarsys.capella.core.data.information.Parameter;
import org.polarsys.capella.core.data.information.ParameterDirection;
import org.polarsys.capella.core.data.information.Property;
import org.polarsys.capella.core.data.information.datavalue.LiteralNumericValue;
import org.polarsys.capella.core.data.information.datavalue.NumericValue;

public class ProduceCapellaPythonTestsFromCapellaHandler extends AbstractHandler {

	/**
	 * The new line separator.
	 */
	private static final String NL = System.lineSeparator();

	private Map<Class, Class> concreteClass = new HashMap<Class, Class>();

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		DataPkg root = (DataPkg) ((IStructuredSelection) HandlerUtil.getCurrentSelection(event)).getFirstElement();

		for (DataPkg pkg : root.getOwnedDataPkgs()) {
			for (Class cls : pkg.getOwnedClasses()) {
				if (!cls.isAbstract()) {
					concreteClass.put(cls, cls);
					for (Class superCls : getAllSuperClasses(cls)) {
						if (superCls.isAbstract()) {
							concreteClass.put(superCls, cls);
						}
					}
				}
			}
		}

		final File file = new File("/tmp/capella/" + "capella" + "_tests.py");
		try {
			if (!file.exists()) {
				file.getParentFile().mkdirs();
				file.createNewFile();
			}
			try (OutputStream os = new FileOutputStream(file)) {
				os.write(getHeader(root, "capella").getBytes());
				for (DataPkg pkg : root.getOwnedDataPkgs()) {
					for (Class cls : pkg.getOwnedClasses()) {
						if (!cls.isAbstract()) {
							final Set<Feature> allFeatures = getAllFeatures(cls);
							for (Feature feature : allFeatures) {
								os.write(getTest(cls, feature).getBytes());
							}
						}
					}
				}
				os.write(getTestAdditions("capella").getBytes());
				os.write(NL.getBytes());
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return null;
	}

	private String getTestAdditions(String pkgName) {
		String res = "";

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/additions/tests/" + pkgName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));

		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	public static List<Class> getAllSuperClasses(Class cls) {
		final List<Class> res = new ArrayList<>();

		for (GeneralizableElement superType : cls.getSuper()) {
			if (superType instanceof Class) {
				res.add((Class) superType);
				res.addAll(getAllSuperClasses((Class) superType));
			}
		}

		return res;
	}

	private Set<Feature> getAllFeatures(Class cls) {
		final Set<Feature> res = new LinkedHashSet<>();

		for (Class superType : getAllSuperClasses(cls)) {
			res.addAll(superType.getOwnedFeatures());
		}
		res.addAll(cls.getOwnedFeatures());

		return res;
	}

	private String getHeader(DataPkg root, String clsLabel) {
		final StringBuilder res = new StringBuilder();

//		for (DataPkg pkg : root.getOwnedDataPkgs()) {
		res.append("include('workspace://Python4Capella/simplified_api/" + "capella" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "capella" + " import *" + NL);
		res.append("include('workspace://Python4Capella/simplified_api/" + "pvmt" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "pvmt" + " import *" + NL);
		res.append("include('workspace://Python4Capella/simplified_api/" + "requirement" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "requirement" + " import *" + NL);
//		}
		res.append(NL);
		res.append("import unittest" + NL);
		res.append(NL);
		res.append("class " + clsLabel + "_tests(unittest.TestCase):" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTest(Class cls, Feature feature) {
		final StringBuilder res = new StringBuilder();

		if (feature instanceof Operation) {
			res.append(getTest(cls, (Operation) feature));
		} else if (feature instanceof Property) {
			res.append(getTestGetter(cls, (Property) feature));
			if (!((Property) feature).isIsReadOnly()) {
				res.append(getTestSetter(cls, (Property) feature));
			}
		}

		return res.toString();
	}

	private String getTest(Class cls, Operation operation) {
		final StringBuilder res = new StringBuilder();

		final String pythonName = ProduceCapellaPythonAPIFromEcoreHandler.getPythonName(operation.getName());
		res.append("    def test_" + cls.getName() + "_" + pythonName + "(self):" + NL);
		res.append("        tested = " + cls.getName() + "()" + NL);
		if ("CapellaModel".equals(cls.getName())) {
			res.append("        tested.open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")"
					+ NL);
		}

		int index = 1;
		final StringJoiner joiner = new StringJoiner(", ");
		for (Parameter parameter : operation.getOwnedParameters()) {
			if (parameter.getDirection() != ParameterDirection.RETURN) {
				final String paramName = "param" + index++;
				res.append("        " + paramName + " = " + getTestValue(cls, parameter) + NL);
				if ("CapellaModel".equals(parameter.getType().getLabel())) {
					res.append("        " + paramName
							+ ".open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")" + NL);
				}
				joiner.add(paramName);
			}
		}

		res.append("        tested." + pythonName + "(" + joiner.toString() + ")" + NL);
		res.append("        pass" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTestGetter(Class cls, Property property) {
		final StringBuilder res = new StringBuilder();

		final String pythonName = ProduceCapellaPythonAPIFromEcoreHandler.getPythonName(property.getName());
		final String testName = "test_" + cls.getName() + "_" + pythonName + "_getter";
		res.append("    def " + testName + "(self):" + NL);
		res.append("        tested = " + cls.getName() + "()" + NL);
		if ("CapellaModel".equals(cls.getName())) {
			res.append("        tested.open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")"
					+ NL);
		}
		if (isScalar(property)) {
			res.append("        tested.get_" + pythonName + "()" + NL);
		} else {
			// collection
			res.append("        tested.get_" + pythonName + "()" + NL);
		}
		res.append("        pass" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTestSetter(Class cls, Property property) {
		final StringBuilder res = new StringBuilder();

		final String pythonName = ProduceCapellaPythonAPIFromEcoreHandler.getPythonName(property.getName());
		final String testName = "test_" + cls.getName() + "_" + pythonName + "_setter";
		res.append("    def " + testName + "(self):" + NL);
		res.append("        tested = " + cls.getName() + "()" + NL);
		if ("CapellaModel".equals(cls.getName())) {
			res.append("        tested.open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")"
					+ NL);
		}
		if (isScalar(property)) {
			res.append("        value = " + getTestValue(cls, property) + NL);
			res.append("        tested.set_" + pythonName + "(value)" + NL);
		} else {
			// collection
			res.append("        value = " + getTestValue(cls, property) + NL);
			res.append("        tested.get_" + pythonName + "().add(value)" + NL);
		}
		res.append("        pass" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTestValue(Class cls, TypedElement typedElement) {
		final String res;

		if ("Boolean".equals(typedElement.getType().getLabel())) {
			res = "True";
		} else if ("Float".equals(typedElement.getType().getLabel())) {
			res = "3.14";
		} else if ("Integer".equals(typedElement.getType().getLabel())) {
			res = "42";
		} else if ("String".equals(typedElement.getType().getLabel())) {
			res = "\"value\"";
		} else {
			if (typedElement.getType() instanceof Class && ((Class) typedElement.getType()).isAbstract()) {
				res = concreteClass.get(typedElement.getType()).getLabel() + "()";
			} else {
				res = typedElement.getType().getLabel() + "()";
			}
		}

		return res;
	}

	private boolean isScalar(Property property) {
		final NumericValue ownedMaxCard = property.getOwnedMaxCard();
		return ownedMaxCard instanceof LiteralNumericValue
				&& "1".equals(((LiteralNumericValue) ownedMaxCard).getValue());
	}

}
