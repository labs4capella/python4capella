package org.eclipse.python4capella.gen.handlers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.lang.reflect.Field;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringJoiner;
import java.util.stream.Collectors;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.ui.handlers.HandlerUtil;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.ui.toolkit.browser.category.CategoryRegistry;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;
import org.polarsys.capella.core.data.capellacore.Feature;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.DataPkg;
import org.polarsys.capella.core.data.information.Operation;
import org.polarsys.capella.core.data.information.Parameter;
import org.polarsys.capella.core.data.information.ParameterDirection;
import org.polarsys.capella.core.data.information.Property;
import org.polarsys.capella.core.data.information.datavalue.LiteralNumericValue;
import org.polarsys.capella.core.data.information.datavalue.NumericValue;

public class ProduceCapellaPythonAPIFromCapellaHandler extends AbstractHandler {

	private final List<EPackage> ePackages = initEPackages();

	private final Map<String, String> featureRenames = initFeatureRenames();

	final Map<String, List<ICategory>> queries = getQueryMapping();

	/**
	 * The new line separator.
	 */
	private static final String NL = System.lineSeparator();

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		DataPkg root = (DataPkg) ((IStructuredSelection) HandlerUtil.getCurrentSelection(event)).getFirstElement();

		// generateMultiFiles(root);
		generateOneFile(root);

		return null;
	}

	private void generateOneFile(DataPkg root) {

		final Set<Class> remainingClasses = new LinkedHashSet<>();
		for (DataPkg pkg : root.getOwnedDataPkgs()) {
			for (Class cls : pkg.getOwnedClasses()) {
				remainingClasses.add(cls);
			}
		}

		final List<Class> orderedClasses = new ArrayList<>();
		final Set<Class> knwonClasses = new HashSet<>();
		while (!remainingClasses.isEmpty()) {
			final List<Class> toRemove = new ArrayList<>();
			for (Class cls : remainingClasses) {
				if (knwonClasses.containsAll(getSuperClasses(cls))) {
					orderedClasses.add(cls);
					knwonClasses.add(cls);
					toRemove.add(cls);
				}
			}
			remainingClasses.removeAll(toRemove);
		}

		final File file = new File("/tmp/capella/" + "capella" + ".py");
		try {
			if (!file.exists()) {
				file.getParentFile().mkdirs();
				file.createNewFile();
			}
			try (OutputStream os = new FileOutputStream(file)) {
				os.write(getHeader("capella").getBytes());
				for (Class cls : orderedClasses) {
					os.write(NL.getBytes());
					os.write(generateClass(cls).getBytes());
				}
				os.write(NL.getBytes());
				final String additions = getPackageAdditions("capella");
				if (additions != null) {
					os.write(additions.getBytes());
				}
				os.write(NL.getBytes());
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private List<Class> getSuperClasses(Class cls) {
		List<Class> res = new ArrayList<>();

		for (GeneralizableElement superElement : cls.getSuper()) {
			if (superElement instanceof Class) {
				res.add((Class) superElement);
			}
		}

		return res;
	}

	private void generateMultiFiles(DataPkg root) {
		for (DataPkg pkg : root.getOwnedDataPkgs()) {
			final File file = new File("/tmp/capella/" + pkg.getName() + ".py");
			try {
				if (!file.exists()) {
					file.getParentFile().mkdirs();
					file.createNewFile();
				}
				try (OutputStream os = new FileOutputStream(file)) {
					os.write(getHeader(pkg.getName()).getBytes());
					for (Class cls : pkg.getOwnedClasses()) {
						os.write(NL.getBytes());
						os.write(generateClass(cls).getBytes());
					}
					os.write(NL.getBytes());
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	private String generateClass(Class cls) {
		final StringBuilder res = new StringBuilder();

		final String superClassNames;
		if (cls.getSuperGeneralizations().isEmpty()) {
			superClassNames = "JavaObject";
		} else {
			final StringJoiner joiner = new StringJoiner(", ");
			final List<Class> allSuperClasses = new ArrayList<>();
			for (GeneralizableElement superElement : cls.getSuper()) {
				if (superElement instanceof Class) {
					allSuperClasses.addAll(
							ProduceCapellaPythonTestsFromCapellaHandler.getAllSuperClasses((Class) superElement));
				}
			}
			for (GeneralizableElement superElement : cls.getSuper()) {
				if (!allSuperClasses.contains(superElement)) {
					joiner.add(superElement.getLabel());
				}
			}
			superClassNames = joiner.toString();
		}

		res.append("class " + cls.getName() + "(" + superClassNames + "):" + NL);
		final String initCursomization = getClassCustomization(cls.getName() + ".__init__");
		if (initCursomization != null) {
			res.append(initCursomization);
		} else {
			res.append(generateClassInit(cls));
		}
		for (Feature feature : cls.getOwnedFeatures()) {
			final String featureCustomization = getClassCustomization(cls.getName() + "." + feature.getName());
			if (featureCustomization != null) {
				res.append(featureCustomization);
			} else {
				final String generatedQuery = generateQuery(cls, feature);
				if (!generatedQuery.isEmpty()) {
					res.append(generatedQuery);
				} else {
					res.append(generateFeature(cls, feature));
				}
			}
		}

		return res.toString();
	}

	private String generateQuery(Class cls, Feature feature) {
		final StringBuilder res = new StringBuilder();

		final String attributeName = getPythonName(feature.getName());
		final String featureGetterName = "get_" + attributeName;
		final EClass eCls = findCorrespondingEClass(cls);
		if (eCls != null) {
			final List<ICategory> categories = queries.get(eCls.getInstanceClass().getCanonicalName());
			if (categories != null) {
				for (ICategory category : categories) {
					final IQuery query = getQuery(category);
					final String queryGetterName = "get_" + getCategoryPythonName(category.getName());
					if (featureGetterName.equals(queryGetterName)) {
						res.append("    def " + queryGetterName + "(self):" + NL);
						res.append("        return capella_query_by_name(self, \"" + category.getName() + "\")" + NL);
						break;
					}
				}
			}
		}

		return res.toString();
	}

	private String generateClassInit(Class cls) {
		final StringBuilder res = new StringBuilder();

		res.append("    def __init__(self, java_object = None):" + NL);
		res.append("        if java_object is None:" + NL);

		final EClass eCls = findCorrespondingEClass(cls);
		if (eCls != null) {
			final String nsURIString;
			if (eCls.getEPackage().getNsURI().contains("capella")) {
				nsURIString = "\""
						+ eCls.getEPackage().getNsURI().substring(0, eCls.getEPackage().getNsURI().lastIndexOf("/") + 1)
						+ "\"" + " + capella_version()";
			} else {
				nsURIString = "\"" + eCls.getEPackage().getNsURI() + "\"";
			}

			res.append("            EObject.__init__(self, create_e_object(" + nsURIString + ", \"" + cls.getName()
					+ "\"))" + NL);
		} else {
			res.append("            raise ValueError(\"No matching EClass for this type\")" + NL);
		}

		res.append("        elif isinstance(java_object, " + cls.getName() + "):" + NL);
		res.append("            EObject.__init__(self, java_object.get_java_object())" + NL);
		res.append("        else:" + NL);
		res.append("            EObject.__init__(self, java_object)" + NL);

		return res.toString();
	}

	private Object generateFeature(Class cls, Feature feature) {
		final StringBuilder res = new StringBuilder();

		if (feature instanceof Operation) {
			res.append(generateOperation((Operation) feature));
		} else if (feature instanceof Property) {
			res.append(generateProperty(cls, (Property) feature));
		}

		return res.toString();
	}

	private String generateProperty(Class cls, Property property) {
		final StringBuilder res = new StringBuilder();

		final String attributeName = getPythonName(property.getName());
		final String getterName = "get_" + attributeName;
		final String setterName = "set_" + attributeName;

		if (isScalar(property)) {
			if (isAttribute(property)) {
				res.append("    def " + getterName + "(self):" + NL);
				res.append("        return self.get_java_object()." + getJavaGetterName(cls, property) + "()" + NL);
				res.append("    def " + setterName + "(self, value):" + NL);
				res.append("        self.get_java_object()." + getJavaSetterName(cls, property) + "(value)" + NL);
			} else {
				res.append("    def " + getterName + "(self):" + NL);
				res.append("        value =  self.get_java_object()." + getJavaGetterName(cls, property) + "()" + NL);
				res.append("        if value is None:" + NL);
				res.append("            return value" + NL);
				res.append("        else:" + NL);
				res.append("            e_object_class = getattr(sys.modules[\"__main__\"], \"EObject\")" + NL);
				res.append("            specific_cls = e_object_class.get_class(value)" + NL);
				res.append("            return specific_cls(value)" + NL);
				if (!property.isIsReadOnly() && !property.isIsDerived()) {
					res.append("    def set_" + getPythonName(property.getName()) + "(self, value):" + NL);
					res.append("        return self.get_java_object()." + getJavaSetterName(cls, property)
							+ "(value.get_java_object())" + NL);
				}
			}
		} else {
			res.append("    def " + getterName + "(self):" + NL);
			res.append("        return create_e_list(self.get_java_object()." + getJavaGetterName(cls, property)
					+ "(), " + property.getType().getLabel() + ")" + NL);
		}

		return res.toString();
	}

	private String generateOperation(Operation operation) {
		final StringBuilder res = new StringBuilder();

		final StringJoiner joiner = new StringJoiner(", ");
		joiner.add("self");
		for (Parameter parameter : operation.getOwnedParameters()) {
			if (parameter.getDirection() != ParameterDirection.RETURN) {
				joiner.add(parameter.getName());
			}
		}

		res.append("    def " + getPythonName(operation.getName()) + "(" + joiner.toString() + "):" + NL);
		res.append("        raise AttributeError(\"TODO\")" + NL);

		return res.toString();
	}

	private String getJavaGetterName(Class cls, Property property) {
		final String javaName = featureRenames.getOrDefault(cls.getName() + "." + property.getName(),
				property.getName());

		if ("Boolean".equals(property.getType().getLabel())) {
			return "is" + Character.toUpperCase(javaName.charAt(0)) + javaName.substring(1);
		} else {
			return "get" + Character.toUpperCase(javaName.charAt(0)) + javaName.substring(1);
		}
	}

	private String getJavaSetterName(Class cls, Property property) {
		final String javaName = featureRenames.getOrDefault(cls.getName() + "." + property.getName(),
				property.getName());

		return "set" + Character.toUpperCase(javaName.charAt(0)) + javaName.substring(1);
	}

	private String getHeader(String pkgName) {
		final StringBuilder res = new StringBuilder();

		final String imports = getPackageImports(pkgName);
		if (imports != null) {
			res.append(imports);
		}

		res.append(NL);

		return res.toString();
	}

	private boolean isScalar(Property property) {
		final NumericValue ownedMaxCard = property.getOwnedMaxCard();
		return ownedMaxCard instanceof LiteralNumericValue
				&& "1".equals(((LiteralNumericValue) ownedMaxCard).getValue());
	}

	private boolean isAttribute(Property property) {
		return "String".equals(property.getType().getLabel()) || "Boolean".equals(property.getType().getLabel())
				|| "Integer".equals(property.getType().getLabel()) || "Float".equals(property.getType().getLabel());
	}

	public static String getPythonName(String name) {
		final StringBuilder res = new StringBuilder();

		for (int i = 0; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isUpperCase(c)) {
				res.append("_");
				res.append(Character.toLowerCase(c));
			} else {
				res.append(c);
			}
		}

		return res.toString();
	}

	private List<EPackage> initEPackages() {
		final List<EPackage> res = new ArrayList<>();

		for (Object obj : new ArrayList(EPackage.Registry.INSTANCE.values())) {
			if (obj instanceof EPackage.Descriptor && isEPackageOfInterest(((EPackage.Descriptor) obj).getEPackage())) {
				res.add(((EPackage.Descriptor) obj).getEPackage());
			} else if (obj instanceof EPackage && isEPackageOfInterest((EPackage) obj)) {
				res.add((EPackage) obj);
			}
		}

		return res;
	}

	private boolean isEPackageOfInterest(EPackage ePackage) {
		return ePackage != null && ePackage.getNsURI() != null && (ePackage.getNsURI().contains("capella")
				|| ePackage.getNsURI().contains("kitalpha") || ePackage.getNsURI().contains("sirius"));
	}

	private EClass findCorrespondingEClass(Class cls) {
		EClassifier res = null;

		for (EPackage ePkg : ePackages) {
			res = ePkg.getEClassifier(cls.getLabel());
			if (res instanceof EClass) {
				break;
			}
		}

		return (EClass) res;
	}

	private String getClassCustomization(String clsNameAndFeatureName) {
		String res = null;

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/customizations/classes/" + clsNameAndFeatureName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));
		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private String getPackageImports(String packageName) {
		String res = null;

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/customizations/packages/" + packageName + ".imports.txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));
		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private String getPackageAdditions(String packageName) {
		String res = null;

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/additions/packages/" + packageName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));
		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private Map<String, String> initFeatureRenames() {
		final Map<String, String> res = new HashMap<>();

		res.put("AbstractCapability.extendedCapabilities", "extendedAbstractCapabilities");
		res.put("AbstractCapability.extendingCapabilities", "extendingAbstractCapabilities");
		res.put("AbstractCapability.includedCapabilities", "includedAbstractCapabilities");
		res.put("AbstractCapability.includingCapabilities", "includingAbstractCapabilities");
		res.put("AbstractState.realizedStates", "realizedAbstractStates");
		res.put("AbstractState.realizingStates", "realizingAbstractStates");
		res.put("AbstractSystemCapability.involvedFunctions", "involvedAbstractFunctions");
		res.put("CapellaElement.visibleForTraceability", "visibleInLM");
		res.put("CapellaElement.visibleInDocumentation", "visibleInDoc");
		res.put("EPBSArchitecture.capabilityRealizationPkg", "containedCapabilityRealizationPkg");
		res.put("EPBSArchitecture.configurationItemPkg", "ownedConfigurationItemPkg");
		res.put("EPBSArchitecture.dataPkg", "ownedDataPkg");
		res.put("FunctionalChain.involvedFunctionalChains", "realizedFunctionalChains");
		res.put("FunctionPort.allocatorComponentPort", "representedComponentPort");
		res.put("LogicalArchitecture.capabilityRealizationPkg", "containedCapabilityRealizationPkg");
		res.put("LogicalArchitecture.dataPkg", "ownedDataPkg");
		res.put("LogicalArchitecture.interfacePkg", "ownedInterfacePkg");
		res.put("LogicalArchitecture.logicalComponentPkg", "ownedLogicalComponentPkg");
		res.put("LogicalArchitecture.logicalFunctionPkg", "containedLogicalFunctionPkg");
		res.put("Node.physicalLinks", "involvedLinks");
		res.put("OperationalAnalysis.dataPkg", "ownedDataPkg");
		res.put("OperationalAnalysis.entityPkg", "ownedEntityPkg");
		res.put("OperationalAnalysis.interfacePkg", "ownedInterfacePkg");
		res.put("OperationalAnalysis.operationalActivityPkg", "containedOperationalActivityPkg");
		res.put("OperationalAnalysis.operationalCapabilityPkg", "containedOperationalCapabilityPkg");
		res.put("PhysicalArchitecture.capabilityRealizationPkg", "containedCapabilityRealizationPkg");
		res.put("PhysicalArchitecture.dataPkg", "ownedDataPkg");
		res.put("PhysicalArchitecture.interfacePkg", "ownedInterfacePkg");
		res.put("PhysicalArchitecture.physicalComponentPkg", "ownedPhysicalComponentPkg");
		res.put("PhysicalArchitecture.physicalFunctionPkg", "containedPhysicalFunctionPkg");
		res.put("PhysicalPort.physicalLinks", "involvedLinks");
		res.put("State.availableCapabilities", "availableAbstractCapabilities");
		res.put("SystemAnalysis.capabilityPkg", "containedCapabilityPkg");
		res.put("SystemAnalysis.dataPkg", "ownedDataPkg");
		res.put("SystemAnalysis.interfacePkg", "ownedInterfacePkg");
		res.put("SystemAnalysis.missionPkg", "ownedMissionPkg");
		res.put("SystemAnalysis.systemComponentPkg", "ownedSystemComponentPkg");
		res.put("SystemAnalysis.systemFunctionPkg", "containedSystemFunctionPkg");
		res.put("Diagram.description", "documentation");
		res.put("PrimitiveDataType.realizedInformations", "RealizedDataTypes");
		res.put("PrimitiveDataType.realizingInformations", "RealizingDataTypes");

		// requirement renames
		res.put("CapellaModule.id", "ReqIFIdentifier");
		res.put("CapellaModule.longName", "ReqIFLongName");
		res.put("CapellaModule.name", "ReqIFName");
		res.put("CapellaModule.prefix", "ReqIFPrefix");
		res.put("Requirement.id", "ReqIFIdentifier");
		res.put("Requirement.longName", "ReqIFLongName");
		res.put("Requirement.name", "ReqIFName");
		res.put("Requirement.chapterName", "ReqIFChapterName");
		res.put("Requirement.prefix", "ReqIFPrefix");
		res.put("Requirement.text", "ReqIFText");
		res.put("Attribute.name", "ReqIFName");

		// isHuman
		res.put("SystemActor.isHuman", "human");
		res.put("LogicalComponent.isHuman", "human");
		res.put("LogicalActor.isHuman", "human");
		res.put("PhysicalActor.isHuman", "human");
		res.put("PhysicalComponent.isHuman", "human");

		return res;
	}

	private Map<String, List<ICategory>> getQueryMapping() {
		final Map<String, List<ICategory>> res = new HashMap<>();

		final CategoryRegistry registry = CategoryRegistry.getInstance();
		final Set<String> fields = new HashSet<>();
		fields.add("currentElementRegistry");
		fields.add("diagramElementRegistry");
		fields.add("referencedElementRegistry");
		fields.add("referencingElementRegistry");
		fields.add("relatedElementsRegistry");
		for (Field field : registry.getClass().getDeclaredFields()) {
			if (fields.contains(field.getName())) {
				field.setAccessible(true);
				try {
					HashMap<String, ICategory> map = (HashMap<String, ICategory>) field.get(registry);
					for (ICategory category : map.values()) {
						res.computeIfAbsent(category.getTypeFullyQualifiedName(), t -> new ArrayList<>()).add(category);
					}
				} catch (IllegalArgumentException | IllegalAccessException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}

		return res;
	}

	private IQuery getQuery(ICategory category) {
		for (Field field : category.getClass().getDeclaredFields()) {
			if ("categoryQuery".equals(field.getName())) {
				field.setAccessible(true);
				try {
					return (IQuery) field.get(category);
				} catch (IllegalArgumentException | IllegalAccessException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		throw new IllegalStateException();
	}

	private String getCategoryPythonName(String name) {
		final StringBuilder res = new StringBuilder();

		res.append(Character.toLowerCase(name.charAt(0)));
		for (int i = 1; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isLetterOrDigit(c)) {
				res.append(c);
			} else if (c == ' ') {
				// skip
			} else {
				break;
			}
		}

		if (res.charAt(res.length() - 1) == '_') {
			return getPythonName(res.substring(0, res.length() - 1).trim());
		} else {
			return getPythonName(res.toString().trim());
		}
	}

}
