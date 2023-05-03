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
import java.util.Scanner;
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
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.safety.Whitelist;
import org.polarsys.capella.common.data.modellingcore.AbstractNamedElement;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.ui.toolkit.browser.category.CategoryRegistry;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;
import org.polarsys.capella.core.data.capellacore.AbstractPropertyValue;
import org.polarsys.capella.core.data.capellacore.CapellaElement;
import org.polarsys.capella.core.data.capellacore.Feature;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.capellacore.PropertyValueGroup;
import org.polarsys.capella.core.data.capellacore.StringPropertyValue;
import org.polarsys.capella.core.data.capellacore.TypedElement;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.DataPkg;
import org.polarsys.capella.core.data.information.MultiplicityElement;
import org.polarsys.capella.core.data.information.Operation;
import org.polarsys.capella.core.data.information.Parameter;
import org.polarsys.capella.core.data.information.ParameterDirection;
import org.polarsys.capella.core.data.information.Property;
import org.polarsys.capella.core.data.information.datatype.Enumeration;
import org.polarsys.capella.core.data.information.datavalue.LiteralNumericValue;
import org.polarsys.capella.core.data.information.datavalue.NumericValue;
import org.polarsys.capella.core.data.information.util.PropertyNamingHelper;

public class ProduceCapellaPythonAPIFromCapellaHandler extends AbstractHandler {

	private final List<EPackage> ePackages = initEPackages();

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

		DataPkg requirementPkg = null;
		DataPkg pvmtPkg = null;
		for (DataPkg pkg : root.getOwnedDataPkgs()) {
			if ("PVMT".equals(pkg.getName())) {
				pvmtPkg = pkg;
			} else if ("Requirement".equals(pkg.getName())) {
				requirementPkg = pkg;
			} else {
				remainingClasses.addAll(pkg.getOwnedClasses());
			}
		}

		writeOneFile(remainingClasses, "capella");

		remainingClasses.clear();
		remainingClasses.addAll(pvmtPkg.getOwnedClasses());
		writeOneFile(remainingClasses, "pvmt");

		remainingClasses.clear();
		remainingClasses.addAll(requirementPkg.getOwnedClasses());
		writeOneFile(remainingClasses, "requirement");
	}

	private void writeOneFile(final Set<Class> remainingClasses, String fileName) {
		final List<Class> orderedClasses = new ArrayList<>();
		final Set<Class> knwonClasses = new HashSet<>();
		while (!remainingClasses.isEmpty()) {
			int lastSize = remainingClasses.size();
			final List<Class> toRemove = new ArrayList<>();
			for (Class cls : remainingClasses) {
				if (knwonClasses.containsAll(getSuperClasses(cls))) {
					orderedClasses.add(cls);
					knwonClasses.add(cls);
					toRemove.add(cls);
				}
			}
			remainingClasses.removeAll(toRemove);
			if (lastSize == remainingClasses.size()) {
				orderedClasses.addAll(remainingClasses);
				break;
			}
		}

		final File file = new File("/tmp/capella/" + fileName + ".py");
		final File file_header = new File("/tmp/capella/" + fileName + "_header.py");
		try {
			if (!file.exists()) {
				file.getParentFile().mkdirs();
				file.createNewFile();
			}
			if (!file_header.exists()) {
				file_header.getParentFile().mkdirs();
				file_header.createNewFile();
			}
			try (OutputStream os = new FileOutputStream(file);
					OutputStream os_header = new FileOutputStream(file_header)) {
				os.write(getHeader(fileName).getBytes());
				for (Class cls : orderedClasses) {
					os.write(NL.getBytes());
					os.write(generateClass(cls).getBytes());
					os_header.write(generateClassHeader(cls).getBytes());
					os_header.write(NL.getBytes());
				}
				os.write(NL.getBytes());
				final String additions = getPackageAdditions(fileName);
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

	private String generateClassHeader(Class cls) {
		final StringBuilder res = new StringBuilder();

		res.append("class " + cls.getName() + ":" + NL);
		res.append("    pass" + NL);

		return res.toString();
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
			final Set<Class> remainingClasses = new LinkedHashSet<>();
			for (Class cls : pkg.getOwnedClasses()) {
				remainingClasses.add(cls);
			}

			final List<Class> orderedClasses = new ArrayList<>();
			final Set<Class> knwonClasses = new HashSet<>();
			while (!remainingClasses.isEmpty()) {
				final List<Class> toRemove = new ArrayList<>();
				for (Class cls : remainingClasses) {
					final List<Class> superClasses = getSuperClasses(cls);
					for (Class superClass : new ArrayList<>(superClasses)) {
						if (superClass.eContainer() != pkg) {
							superClasses.remove(superClass);
						}
					}
					if (knwonClasses.containsAll(superClasses)) {
						orderedClasses.add(cls);
						knwonClasses.add(cls);
						toRemove.add(cls);
					}
				}
				remainingClasses.removeAll(toRemove);
			}

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
					final String additions = getPackageAdditions(pkg.getName());
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
	}

	private String generateClass(Class cls) {
		final StringBuilder res = new StringBuilder();

		final String superClassNames;
		if (cls.getSuperGeneralizations().isEmpty() && !"CapellaModel".equals(cls.getName())) {
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
		res.append(getDocumentation(cls, false));
		final String initCursomization = getClassCustomization(cls.getName() + ".__init__", null);
		if (!initCursomization.trim().isEmpty()) {
			res.append(initCursomization);
		} else {
			res.append(generateClassInit(cls));
		}
		for (Feature feature : cls.getOwnedFeatures()) {
			final String featureCustomization = getClassCustomization(cls.getName() + "." + feature.getName(), feature);
			if (!featureCustomization.trim().isEmpty()) {
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

	/**
	 * Gets the Python documentation from the given {@link CapellaElement}.
	 * 
	 * @param element  the {@link CapellaElement}
	 * @param isSetter tells if the setter status should be used
	 * @return the Python documentation from the given {@link CapellaElement}
	 */
	private String getDocumentation(CapellaElement element, boolean isSetter) {
		final StringBuilder res = new StringBuilder();

		String padding = "    ";
		if (!(element instanceof Class)) {
			padding = padding + padding;
		}

		res.append(padding + "\"\"\"" + NL);
		if (element instanceof Class) {
			final EClass eCls = findCorrespondingEClass((Class) element);
			if (eCls != null) {
				final java.lang.Class<?> instanceCls = eCls.getInstanceClass();
				if (instanceCls != null) {
					res.append(padding + "Java class: " + instanceCls.getCanonicalName() + NL);
				}
			}
		} else if (element instanceof Property || element instanceof Operation) {
			if (element instanceof Operation) {
				StringJoiner joiner = new StringJoiner(", ");
				Parameter returnPrameter = null;
				for (Parameter parameter : ((Operation) element).getOwnedParameters()) {
					if (parameter.getDirection() == ParameterDirection.RETURN) {
						returnPrameter = parameter;
					} else {
						joiner.add(parameter.getName() + ": " + getTypeAndCardinality(parameter));
					}
				}
				final String parametersString = joiner.toString();
				if (!parametersString.isBlank()) {
					res.append(padding + "Parameters: " + parametersString + NL);
				}
				if (returnPrameter != null) {
					res.append(padding + "Returns: " + getTypeAndCardinality(returnPrameter) + NL);
				}
			} else if (element instanceof Property) {
				if (isSetter) {
					res.append(padding + "Parameters: value: " + getTypeAndCardinality((TypedElement) element) + NL);
				} else {
					res.append(padding + "Returns: " + getTypeAndCardinality((TypedElement) element) + NL);
				}
			}
			CapellaElement container = (CapellaElement) element.eContainer();
			statusFound: for (PropertyValueGroup group : container.getOwnedPropertyValueGroups()) {
				if ("ImplementationStatus".equals(group.getName())) {
					for (AbstractPropertyValue property : group.getOwnedPropertyValues()) {
						final String propertyName;
						if (element instanceof Property) {
							if (isSetter) {
								propertyName = property.getName() + "_getter";
							} else {
								propertyName = property.getName() + "_setter";
							}
						} else {
							propertyName = property.getName();
						}
						if (property instanceof StringPropertyValue
								&& ((AbstractNamedElement) element).getName().equals(propertyName)) {
							res.append(padding + "status: " + ((StringPropertyValue) property).getValue() + NL);
							break statusFound;
						}
					}
				}
			}
		}

		if (element != null && element.getDescription() != null && !element.getDescription().isEmpty()) {
			final Document document = Jsoup.parse(element.getDescription());
			// makes html() preserve linebreaks and spacing
			document.outputSettings(new Document.OutputSettings().prettyPrint(false));
			document.select("br").append("\\n");
			document.select("p").prepend("\\n");
			document.select("li").prepend("\\n");
			final String htmlString = document.html().replaceAll("\\\\n", "\n");
			final String text = Jsoup.clean(htmlString, "", Whitelist.none(),
					new Document.OutputSettings().prettyPrint(false));
			try (Scanner scanner = new Scanner(text)) {
				while (scanner.hasNextLine()) {
					final String line = scanner.nextLine();
					if (!line.trim().isEmpty()) {
						res.append(padding + line + NL);
					}
				}
			}
		}
		res.append(padding + "\"\"\"" + NL);

		return res.toString();
	}

	private String getTypeAndCardinality(TypedElement typedElement) {
		final StringBuilder res = new StringBuilder();

		if (typedElement.getType() instanceof Enumeration) {
			res.append("String");
		} else {
			res.append(typedElement.getType().getLabel());
		}
		if (typedElement instanceof MultiplicityElement) {
			res.append(PropertyNamingHelper.multiplicityToStringDisplay((MultiplicityElement) typedElement));
		}

		return res.toString();
	}

	private String getTypeAnnotation(TypedElement typedElement) {
		final StringBuilder res = new StringBuilder();

		final String typeName;
		if (typedElement.getType() instanceof Enumeration) {
			typeName = "str";
		} else if ("String".equals(typedElement.getType().getLabel())) {
			typeName = "str";
		} else if ("Integer".equals(typedElement.getType().getLabel())) {
			typeName = "int";
		} else if ("Boolean".equals(typedElement.getType().getLabel())) {
			typeName = "bool";
		} else if ("PythonClass".equals(typedElement.getType().getLabel())) {
			typeName = "type";
		} else {
			typeName = typedElement.getType().getLabel();
		}
		if (typedElement instanceof MultiplicityElement) {
			final MultiplicityElement multiplicity = (MultiplicityElement) typedElement;
			if (multiplicity.getOwnedMaxCard() instanceof LiteralNumericValue
					&& "*".equals(((LiteralNumericValue) multiplicity.getOwnedMaxCard()).getValue())) {
				res.append("List[" + typeName + "]");
			} else {
				res.append(typeName);
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
					final String queryGetterName = "get_" + getCategoryPythonName(category.getName());
					if (featureGetterName.equals(queryGetterName)) {
						res.append("    def " + queryGetterName + "(self):" + NL);
						res.append(getDocumentation(feature, false));
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

			res.append("    e_class = get_e_classifier(" + nsURIString + ", \"" + cls.getName() + "\")" + NL);
			res.append("    def __init__(self, java_object = None):" + NL);
			res.append("        if java_object is None:" + NL);
			res.append("            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))" + NL);
		} else {
			res.append("    def __init__(self, java_object = None):" + NL);
			res.append("        if java_object is None:" + NL);
			res.append("            raise ValueError(\"No matching EClass for this type\")" + NL);
		}

		res.append("        elif isinstance(java_object, " + cls.getName() + "):" + NL);
		res.append("            JavaObject.__init__(self, java_object.get_java_object())" + NL);
		if (eCls != null) {
			res.append("        elif self.e_class.isInstance(java_object):" + NL);
			res.append("            JavaObject.__init__(self, java_object)" + NL);
			res.append("        else:" + NL);
			res.append(
					"            raise AttributeError(\"Passed object is not compatible with \" + self.__class__.__name__ + \": \" + str(java_object))"
							+ NL);
		} else {
			res.append("        else:" + NL);
			res.append("            JavaObject.__init__(self, java_object)" + NL);
		}

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

		if (property.getType() != null) {
			final String attributeName = getPythonName(property.getName());
			final String getterName = "get_" + attributeName;
			final String setterName = "set_" + attributeName;

			if (isScalar(property)) {
				if (isAttribute(property)) {
					res.append("    def " + getterName + "(self) -> " + getTypeAnnotation(property) + ":" + NL);
					res.append(getDocumentation(property, false));
					res.append("        return self.get_java_object()." + getJavaGetterName(cls, property) + "()" + NL);
					res.append("    def " + setterName + "(self, value: " + getTypeAnnotation(property) + "):" + NL);
					res.append(getDocumentation(property, false));
					res.append("        self.get_java_object()." + getJavaSetterName(cls, property) + "(value)" + NL);
				} else {
					res.append("    def " + getterName + "(self) -> " + getTypeAnnotation(property) + ":" + NL);
					res.append(getDocumentation(property, false));
					res.append(
							"        value =  self.get_java_object()." + getJavaGetterName(cls, property) + "()" + NL);
					res.append("        if value is None:" + NL);
					res.append("            return value" + NL);
					res.append("        else:" + NL);
					res.append("            e_object_class = getattr(sys.modules[\"__main__\"], \"EObject\")" + NL);
					res.append("            specific_cls = e_object_class.get_class(value)" + NL);
					res.append("            return specific_cls(value)" + NL);
					if (!property.isIsReadOnly() && !property.isIsDerived()) {
						res.append(
								"    def " + setterName + "(self, value: " + getTypeAnnotation(property) + "):" + NL);
						res.append(getDocumentation(property, true));
						res.append("        return self.get_java_object()." + getJavaSetterName(cls, property)
								+ "(value.get_java_object())" + NL);
					}
				}
			} else {
				res.append("    def " + getterName + "(self) -> " + getTypeAnnotation(property) + ":" + NL);
				res.append(getDocumentation(property, false));
				res.append("        return create_e_list(self.get_java_object()." + getJavaGetterName(cls, property)
						+ "(), " + property.getType().getLabel() + ")" + NL);
			}
		}

		return res.toString();
	}

	private String generateOperation(Operation operation) {
		final StringBuilder res = new StringBuilder();

		final StringJoiner joiner = new StringJoiner(", ");
		joiner.add("self");
		Parameter returnParameter = null;
		for (Parameter parameter : operation.getOwnedParameters()) {
			if (parameter.getDirection() == ParameterDirection.RETURN) {
				returnParameter = parameter;
			} else {
				joiner.add(parameter.getName() + ": " + getTypeAnnotation(parameter));
			}
		}

		final String returnType;
		if (returnParameter != null) {
			returnType = " -> " + getTypeAnnotation(returnParameter);
		} else {
			returnType = "";
		}

		res.append("    def " + getPythonName(operation.getName()) + "(" + joiner.toString() + ")" + returnType + ":"
				+ NL);
		res.append(getDocumentation(operation, false));
		res.append("        raise AttributeError(\"TODO\")" + NL);

		return res.toString();
	}

	private String getJavaGetterName(Class cls, Property property) {
		final String javaName = getJavaName(property);

		if ("Boolean".equals(property.getType().getLabel())) {
			return "is" + Character.toUpperCase(javaName.charAt(0)) + javaName.substring(1);
		} else {
			return "get" + Character.toUpperCase(javaName.charAt(0)) + javaName.substring(1);
		}
	}

	private String getJavaName(Property property) {
		String res = property.getName();

		for (PropertyValueGroup group : property.getOwnedPropertyValueGroups()) {
			for (AbstractPropertyValue pv : group.getOwnedPropertyValues()) {
				if ("name".equals(pv.getName())) {
					res = ((StringPropertyValue) pv).getValue();
				}
			}
		}

		return res;
	}

	private String getJavaSetterName(Class cls, Property property) {
		final String javaName = getJavaName(property);

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

		for (Object obj : new ArrayList<>(EPackage.Registry.INSTANCE.values())) {
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

	private String getClassCustomization(String clsNameAndFeatureName, CapellaElement element) {
		StringBuilder res = new StringBuilder();

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/customizations/classes/" + clsNameAndFeatureName + ".txt");) {
			if (is != null) {
				final List<String> lines = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
						.collect(Collectors.toList());
				for (String line : lines) {
					if (!line.trim().isEmpty()) {
						res.append(line + NL);
						if (line.trim().startsWith("def ")) {
							res.append(getDocumentation(element, line.trim().startsWith("def set_")));
						}
					}
				}
			}
		} catch (Exception e) {
			// nothing to do here
			e.printStackTrace();
		}

		return res.toString();
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
