//Start of user code copyright
/**
 *  Copyright (c) 2023 THALES GLOBAL SERVICES
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
//End of user code
package org.eclipse.python4capella.ecore.gen.python.main;

//Start of user code imports

import java.io.File;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.acceleo.Module;
import org.eclipse.acceleo.Template;
import org.eclipse.acceleo.aql.AcceleoUtil;
import org.eclipse.acceleo.aql.evaluation.AcceleoEvaluator;
import org.eclipse.acceleo.aql.evaluation.GenerationResult;
import org.eclipse.acceleo.aql.evaluation.strategy.DefaultGenerationStrategy;
import org.eclipse.acceleo.aql.evaluation.strategy.DefaultWriterFactory;
import org.eclipse.acceleo.aql.evaluation.strategy.IAcceleoGenerationStrategy;
import org.eclipse.acceleo.aql.parser.AcceleoParser;
import org.eclipse.acceleo.aql.parser.ModuleLoader;
import org.eclipse.acceleo.query.AQLUtils;
import org.eclipse.acceleo.query.ast.EClassifierTypeLiteral;
import org.eclipse.acceleo.query.ast.TypeLiteral;
import org.eclipse.acceleo.query.runtime.impl.namespace.ClassLoaderQualifiedNameResolver;
import org.eclipse.acceleo.query.runtime.impl.namespace.JavaLoader;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameQueryEnvironment;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameResolver;
import org.eclipse.acceleo.query.services.ResourceServices;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EcorePackage;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;

//End of user code

/**
 * Standalone launcher for org::eclipse::python4capella::ecore::gen::python::main::main.
 * 
 * @author <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
 * @generated
 */
public class MainGenerator {

	/**
	 * The {@link List} of resources to load.
	 * 
	 * @generated
	 */
	protected final List<String> resources;

	/**
	 * The target folder for the generation.
	 * 
	 * @generated
	 */
	protected final String target;

	/**
	 * Constructor.
	 * 
	 * @param resources
	 *            the {@link List} of model resources to load
	 * @param target
	 *            the target folder for the generation
	 * @generated
	 */
	public MainGenerator(List<String> resources, String target) {
		this.resources = resources;
		this.target = target;
	}

	/**
	 * Main entry point.
	 * 
	 * @param args
	 *            resources separated by a comma, target folder
	 */
	public static void main(String[] args) {
		if (args.length == 2) {
			final List<String> resources = new ArrayList<>();
			for (String resource : args[0].split(",")) {
				resources.add(resource.trim());
			}
			final String target = args[1];
			final MainGenerator generator = new MainGenerator(resources, target);
			generator.generate();
		} else {
			printUsage();
		}

	}

	/**
	 * Print the usage.
	 * 
	 * @generated
	 */
	private static void printUsage() {
		System.out.println("Usage: <resources> <target>");
		System.out.println("Example: model1.xmi,model2.xmi src-gen/");
	}

	/**
	 * Registers the given {@link EPackage} in the given {@link IQualifiedNameQueryEnvironment} recursively.
	 * 
	 * @param environment
	 *            the {@link IQualifiedNameQueryEnvironment}
	 * @param ePackage
	 *            the {@link EPackage}
	 * @generated
	 */
	private static void registerEPackage(IQualifiedNameQueryEnvironment environment, EPackage ePackage) {
		environment.registerEPackage(ePackage);
		for (EPackage child : ePackage.getESubpackages()) {
			registerEPackage(environment, child);
		}
	}

	/**
	 * Generates.
	 * 
	 * @generated
	 */
	public void generate() {
		// inputs
		final String moduleQualifiedName = getModuleQualifiedName();
		final URI targetURI = getTargetURI(target);
		final Map<String, String> options = getOptions();

		// create the resource set used to load models
		final Object generationKey = new Object();
		final List<Exception> exceptions = new ArrayList<>();
		final ResourceSet resourceSet = createDefaultResourceSet();
		final ResourceSet resourceSetForModels = createResourceSetForModel(generationKey, options, exceptions,
				resourceSet);

		// load models
		standaloneInitialization(resourceSetForModels);
		loadResources(resourceSetForModels, resources);

		// prepare Acceleo environment
		final IQualifiedNameResolver resolver = createResolver();
		final IQualifiedNameQueryEnvironment queryEnvironment = createAcceleoQueryEnvironment(options,
				resolver, resourceSetForModels);
		AcceleoEvaluator evaluator = createAcceleoEvaluator(resolver, queryEnvironment);
		final IAcceleoGenerationStrategy strategy = createGenerationStrategy(resourceSetForModels);

		final Module module = (Module)resolver.resolve(moduleQualifiedName);
		final URI logURI = AcceleoUtil.getlogURI(targetURI, options.get(AcceleoUtil.LOG_URI_OPTION));
		beforeGeneration(evaluator, queryEnvironment, module, resourceSetForModels, strategy, targetURI,
				logURI);
		try {
			final Map<EClass, List<EObject>> valuesCache = new LinkedHashMap<>();
			for (Template template : getTemplates(module)) {
				final EClassifierTypeLiteral eClassifierTypeLiteral = (EClassifierTypeLiteral)template
						.getParameters().get(0).getType().getAst();
				final List<EObject> values = getValues(queryEnvironment, valuesCache, eClassifierTypeLiteral,
						resourceSetForModels);

				final String parameterName = template.getParameters().get(0).getName();
				Map<String, Object> variables = new LinkedHashMap<>();
				for (EObject value : values) {
					variables.put(parameterName, value);
					AcceleoUtil.generate(template, variables, evaluator, queryEnvironment, strategy,
							targetURI, logURI);
				}
			}
		} finally {
			AQLUtils.cleanResourceSetForModels(generationKey, resourceSetForModels);
			AcceleoUtil.cleanServices(queryEnvironment, resourceSetForModels);
			printDiagnostics(evaluator.getGenerationResult());
			afterGeneration(evaluator.getGenerationResult());
		}

	}

	/**
	 * Gets the {@link List} of {@link Template} to generate for the given {@link Module}.
	 * 
	 * @param module
	 *            the {@link Module}
	 * @return the {@link List} of {@link Template} to generate for the given {@link Module}
	 */
	protected List<Template> getTemplates(Module module) {
		return AcceleoUtil.getMainTemplate(module);
	}

	/**
	 * Gets the {@link List} of {@link EObject} values to use.
	 * 
	 * @param queryEnvironment
	 *            the {@link IQualifiedNameQueryEnvironment}
	 * @param valuesCache
	 *            the cache for any previous values
	 * @param type
	 *            the {@link TypeLiteral}
	 * @param resourceSetForModels
	 *            the {@link ResourceServices} for models
	 * @return the {@link List} of {@link EObject} values to use
	 */
	protected List<EObject> getValues(IQualifiedNameQueryEnvironment queryEnvironment,
			final Map<EClass, List<EObject>> valuesCache, TypeLiteral type,
			ResourceSet resourceSetForModels) {
		final List<EObject> values = AcceleoUtil.getValues(type, queryEnvironment, resourceSetForModels
				.getResources(), valuesCache);
		return values;
	}

	/**
	 * Gets the module qualified name.
	 * 
	 * @return the module qualified name
	 * @generated
	 */
	protected String getModuleQualifiedName() {
		return "org::eclipse::python4capella::ecore::gen::python::main::main";
	}

	/**
	 * Gets the target folder {@link URI}.
	 * 
	 * @param target
	 *            the target folder {@link String}.
	 * @return the target folder {@link URI}
	 * @generated
	 */
	protected URI getTargetURI(String target) {
		return URI.createFileURI(new File(target).getAbsolutePath() + "/");
	}

	/**
	 * Gets the {@link Map} of options for the generation.
	 * 
	 * @return the {@link Map} of options for the generation
	 * @generated
	 */
	protected Map<String, String> getOptions() {
		Map<String, String> res = new LinkedHashMap<>();

		res.put(AcceleoUtil.LOG_URI_OPTION, "acceleo.log");
		res.put(AcceleoUtil.NEW_LINE_OPTION, System.lineSeparator());

		return res;
	}

	/**
	 * Creates the default {@link ResourceSet}.
	 * 
	 * @return the created default {@link ResourceSet}
	 * @generated
	 */
	protected ResourceSet createDefaultResourceSet() {
		return new ResourceSetImpl();
	}

	/**
	 * Creates the {@link ResourceSet} for models.
	 * 
	 * @param generationKey
	 *            the generation key
	 * @param options
	 *            the {@link Map} of options
	 * @param exceptions
	 *            the {@link List} of exceptions
	 * @param resourceSet
	 *            the default {@link ResourceSet}
	 * @return the created {@link ResourceSet} for models
	 * @generated
	 */
	protected ResourceSet createResourceSetForModel(Object generationKey, Map<String, String> options,
			List<Exception> exceptions, ResourceSet resourceSet) {
		final ResourceSet resourceSetForModels = AQLUtils.createResourceSetForModels(exceptions,
				generationKey, resourceSet, options);

		return resourceSetForModels;
	}

	/**
	 * Initializes the {@link ResourceSet} for models for standalone use.
	 * 
	 * @param resourceSetForModels
	 *            the {@link ResourceSet} for models
	 * @generated
	 */
	protected void standaloneInitialization(ResourceSet resourceSetForModels) {
		// initialize EPackages
		EcorePackage.eINSTANCE.getName();

		// register default XMI resource factory
		resourceSetForModels.getResourceFactoryRegistry().getExtensionToFactoryMap().put(
				Resource.Factory.Registry.DEFAULT_EXTENSION, new XMIResourceFactoryImpl());
	}

	/**
	 * Loads {@link Resource} in the given {@link ResourceSet} for models.
	 * 
	 * @param resourceSetForModels
	 *            the {@link ResourceSet} for models
	 * @param resources
	 *            the {@link List} of resource names to load
	 * @generated
	 */
	protected void loadResources(ResourceSet resourceSetForModels, List<String> resources) {
		for (String resource : resources) {
			resourceSetForModels.getResource(URI.createURI(resource, true), true);
		}
	}

	/**
	 * Creates the {@link IQualifiedNameResolver}.
	 * 
	 * @return the created {@link IQualifiedNameResolver}
	 * @generated
	 */
	protected IQualifiedNameResolver createResolver() {
		final IQualifiedNameResolver resolver = new ClassLoaderQualifiedNameResolver(this.getClass()
				.getClassLoader(), AcceleoParser.QUALIFIER_SEPARATOR);

		return resolver;
	}

	/**
	 * Creates the {@link IQualifiedNameQueryEnvironment}.
	 * 
	 * @param options
	 *            the {@link Map} of options
	 * @param resolver
	 *            the {@link IQualifiedNameResolver}
	 * @param resourceSetForModels
	 *            the {@link ResourceSet} for models
	 * @return the created {@link IQualifiedNameQueryEnvironment}
	 * @generated
	 */
	protected IQualifiedNameQueryEnvironment createAcceleoQueryEnvironment(Map<String, String> options,
			IQualifiedNameResolver resolver, ResourceSet resourceSetForModels) {
		final IQualifiedNameQueryEnvironment queryEnvironment = AcceleoUtil.newAcceleoQueryEnvironment(
				options, resolver, resourceSetForModels, false);
		for (String nsURI : new ArrayList<String>(EPackage.Registry.INSTANCE.keySet())) {
			registerEPackage(queryEnvironment, EPackage.Registry.INSTANCE.getEPackage(nsURI));
		}

		return queryEnvironment;
	}

	/**
	 * Creates the {@link AcceleoEvaluator}
	 * 
	 * @param resolver
	 *            the {@link IQualifiedNameResolver}
	 * @param queryEnvironment
	 *            the {@link IQualifiedNameQueryEnvironment}
	 * @return the created {@link AcceleoEvaluator}
	 * @generated
	 */
	protected AcceleoEvaluator createAcceleoEvaluator(IQualifiedNameResolver resolver,
			IQualifiedNameQueryEnvironment queryEnvironment) {
		AcceleoEvaluator evaluator = new AcceleoEvaluator(queryEnvironment.getLookupEngine(), System
				.lineSeparator());
		resolver.addLoader(new ModuleLoader(new AcceleoParser(), evaluator));
		resolver.addLoader(new JavaLoader(AcceleoParser.QUALIFIER_SEPARATOR, false));

		return evaluator;
	}

	protected IAcceleoGenerationStrategy createGenerationStrategy(final ResourceSet resourceSetForModels) {
		final IAcceleoGenerationStrategy strategy = new DefaultGenerationStrategy(resourceSetForModels
				.getURIConverter(), new DefaultWriterFactory());

		return strategy;
	}

	/**
	 * Before the generation starts.
	 * 
	 * @param evaluator
	 *            the {@link AcceleoEvaluator}
	 * @param queryEnvironment
	 *            the {@link IQualifiedNameQueryEnvironment}
	 * @param module
	 *            the {@link Module}
	 * @param resourceSetForModels
	 *            the {@link ResourceSet} containing loaded models
	 * @param generationStrategy
	 *            the {@link IAcceleoGenerationStrategy}
	 * @param destination
	 *            destination {@link URI}
	 * @param logURI
	 *            the {@link URI} for logging if nay, <code>null</code> otherwise
	 * @generated
	 */
	protected void beforeGeneration(AcceleoEvaluator evaluator,
			IQualifiedNameQueryEnvironment queryEnvironment, Module module, ResourceSet resourceSetForModels,
			IAcceleoGenerationStrategy strategy, URI destination, URI logURI) {
		// this is called before the generation starts
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
			PrintStream stream;
			switch (generationResult.getDiagnostic().getSeverity()) {
				case Diagnostic.WARNING:
					stream = System.out;
					stream.println("WARNING");
					break;
				case Diagnostic.ERROR:
					// Fall-through
				default:
					// Shouldn't happen as we only show warnings and errors
					stream = System.err;
					stream.println("ERROR");
					break;
			}
			printDiagnostic(stream, generationResult.getDiagnostic(), "");
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
	 */
	protected void printDiagnostic(PrintStream stream, Diagnostic diagnostic, String indentation) {
		String nextIndentation = indentation;
		if (diagnostic.getMessage() != null) {
			stream.print(indentation);
			switch (diagnostic.getSeverity()) {
				case Diagnostic.INFO:
					stream.print("INFO: ");
					break;

				case Diagnostic.WARNING:
					stream.print("WARNING: ");
					break;

				case Diagnostic.ERROR:
					stream.print("ERROR: ");
					break;
			}
			stream.println(diagnostic.getMessage());
			nextIndentation += "\t";
		}
		for (Diagnostic child : diagnostic.getChildren()) {
			printDiagnostic(stream, child, nextIndentation);
		}
	}

	/**
	 * After the generation finished.
	 * 
	 * @param generationResult
	 *            the {@link GenerationResult}
	 * @generated
	 */
	protected void afterGeneration(GenerationResult generationResult) {
		// this is called after the generation finished
	}

}
