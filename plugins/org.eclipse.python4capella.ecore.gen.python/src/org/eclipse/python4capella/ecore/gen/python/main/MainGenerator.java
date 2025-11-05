//Start of user code copyright
/**
 *  Copyright (c) 2023, 2025 THALES GLOBAL SERVICES
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
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.eclipse.acceleo.Module;
import org.eclipse.acceleo.Template;
import org.eclipse.acceleo.aql.AcceleoUtil;
import org.eclipse.acceleo.aql.evaluation.AcceleoEvaluator;
import org.eclipse.acceleo.aql.evaluation.AcceleoProfilerEvaluator;
import org.eclipse.acceleo.aql.evaluation.GenerationResult;
import org.eclipse.acceleo.aql.evaluation.strategy.DefaultGenerationStrategy;
import org.eclipse.acceleo.aql.evaluation.strategy.DefaultWriterFactory;
import org.eclipse.acceleo.aql.evaluation.strategy.IAcceleoGenerationStrategy;
import org.eclipse.acceleo.aql.parser.AcceleoParser;
import org.eclipse.acceleo.aql.parser.ModuleLoader;
import org.eclipse.acceleo.aql.profiler.IProfiler;
import org.eclipse.acceleo.aql.profiler.ProfileResource;
import org.eclipse.acceleo.query.AQLUtils;
import org.eclipse.acceleo.query.ast.ASTNode;
import org.eclipse.acceleo.query.ast.EClassifierTypeLiteral;
import org.eclipse.acceleo.query.ast.TypeLiteral;
import org.eclipse.acceleo.query.runtime.impl.namespace.ClassLoaderQualifiedNameResolver;
import org.eclipse.acceleo.query.runtime.impl.namespace.JavaLoader;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameQueryEnvironment;
import org.eclipse.acceleo.query.runtime.namespace.IQualifiedNameResolver;
import org.eclipse.emf.common.util.BasicDiagnostic;
import org.eclipse.emf.common.util.BasicMonitor.Printing;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.common.util.Monitor;
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
	 * @generated
	 */
	public static void main(String[] args) {
		if (args.length == 2) {
			final List<String> resources = new ArrayList<>();
			for (String resource : args[0].split(",")) {
				resources.add(resource.trim());
			}
			final String target = args[1];
			final MainGenerator generator = new MainGenerator(resources, target);
			generator.generate(getMonitor());
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
	 * Gets the progress {@link Monitor}.
	 * 
	 * @return the progress {@link Monitor}
	 * @generated
	 */
	private static Monitor getMonitor() {
		return new Printing(new PrintStream(System.out));
	}

	/**
	 * Generates.
	 * 
	 * @param monitor
	 *            the progress {@link Monitor}
	 * @generated
	 */
	public void generate(Monitor monitor) {
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

		standaloneInitialization(resourceSetForModels);

		// prepare Acceleo environment
		final IQualifiedNameResolver resolver = createResolver();
		final IQualifiedNameQueryEnvironment queryEnvironment = createAcceleoQueryEnvironment(options,
				resolver, resourceSetForModels);
		final AcceleoEvaluator evaluator = createAcceleoEvaluator(targetURI, resolver, queryEnvironment);
		final IAcceleoGenerationStrategy strategy = createGenerationStrategy(resourceSetForModels);

		final Module module = (Module)resolver.resolve(moduleQualifiedName);
		final Set<String> nsURIs = AQLUtils.getAllNeededEPackages(resolver, moduleQualifiedName);
		AQLUtils.registerEPackages(queryEnvironment, EPackage.Registry.INSTANCE, nsURIs);
		final URI logURI = AcceleoUtil.getlogURI(targetURI, options.get(AcceleoUtil.LOG_URI_OPTION));
		final List<Template> mainTemplates = getTemplates(module);

		monitor.beginTask("Generating", resources.size() + 1 + mainTemplates.size() * resources.size() + 1);
		// load models
		final List<Resource> modelResources = loadResources(resourceSetForModels, resources, monitor);

		monitor.subTask("Before generation");
		beforeGeneration(evaluator, queryEnvironment, module, resourceSetForModels, strategy, targetURI,
				logURI);
		monitor.worked(1);
		try {
			final Map<EClass, List<EObject>> valuesCache = new LinkedHashMap<>();
			for (Template template : mainTemplates) {
				final EClassifierTypeLiteral eClassifierTypeLiteral = (EClassifierTypeLiteral)template
						.getParameters().get(0).getType().getAst();
				final List<EObject> values = getValues(queryEnvironment, valuesCache, eClassifierTypeLiteral,
						resourceSetForModels, modelResources, monitor);

				final String parameterName = template.getParameters().get(0).getName();
				Map<String, Object> variables = new LinkedHashMap<>();
				for (EObject value : values) {
					variables.put(parameterName, value);
					AcceleoUtil.generate(template, variables, evaluator, queryEnvironment, strategy,
							targetURI, logURI, monitor);
					if (monitor.isCanceled()) {
						return;
					}
				}
				monitor.worked(1);
				if (monitor.isCanceled()) {
					return;
				}
			}
		} finally {
			if (evaluator instanceof AcceleoProfilerEvaluator) {
				IProfiler profiler = ((AcceleoProfilerEvaluator)evaluator).getProfiler();
				ProfileResource profileResource = profiler.getResource();
				profileResource.setStartResource(resolver.getSourceURI(moduleQualifiedName).toString());
				try {
					profiler.save(URI.createURI(targetURI.toString() + "/" + module.getName() + ".mtlp"));
				} catch (IOException e) {
					final Diagnostic diagnostic = new BasicDiagnostic(Diagnostic.ERROR, getClass()
							.getCanonicalName(), 0, e.getMessage(), new Object[] {e });
					evaluator.getGenerationResult().addDiagnostic(diagnostic);
				}
			}
			AQLUtils.cleanResourceSetForModels(generationKey, resourceSetForModels);
			AcceleoUtil.cleanServices(queryEnvironment, resourceSetForModels);
			printDiagnostics(evaluator.getGenerationResult());
			monitor.subTask("After generation");
			afterGeneration(evaluator.getGenerationResult());
			monitor.worked(1);
		}

	}

	/**
	 * Gets the {@link List} of {@link Template} to generate for the given {@link Module}.
	 * 
	 * @param module
	 *            the {@link Module}
	 * @return the {@link List} of {@link Template} to generate for the given {@link Module}
	 * @generated
	 */
	protected List<Template> getTemplates(Module module) {
		return AcceleoUtil.getMainTemplates(module);
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
	 *            the {@link ResourceSet} for models
	 * @param modelResources
	 *            the {@link List} of loaded {@link Resource}
	 * @param monitor
	 *            the progress {@link Monitor}, it must consumes the resources.size()
	 * @return the {@link List} of {@link EObject} values to use
	 * @generated
	 */
	protected List<EObject> getValues(IQualifiedNameQueryEnvironment queryEnvironment,
			Map<EClass, List<EObject>> valuesCache, TypeLiteral type, ResourceSet resourceSetForModels,
			List<Resource> modelResources, Monitor monitor) {
		final List<EObject> values = AcceleoUtil.getValues(type, queryEnvironment, modelResources,
				valuesCache, monitor);
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
		// res.put(AQLUtils.INSTALL_CROSS_REFERENCE_ADAPTER_OPTION, Boolean.TRUE.toString());
		// res.put(AQLUtils.PROPERTIES_URIS_OPTION, "file1.properties,file2.properties");

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
	 * @param monitor
	 *            the progress {@link Monitor}, it must consumes the number of resources
	 * @return the {@link List} of loaded {@link Resource}
	 * @generated
	 */
	protected List<Resource> loadResources(ResourceSet resourceSetForModels, List<String> resources,
			Monitor monitor) {
		final List<Resource> res = new ArrayList<>();

		for (String resource : resources) {
			monitor.subTask("Loading " + resource);
			final Resource loaded = resourceSetForModels.getResource(URI.createURI(resource, true), true);
			if (loaded != null) {
				res.add(loaded);
			}
			monitor.worked(1);
			if (monitor.isCanceled()) {
				break;
			}
		}

		return res;
	}

	/**
	 * Creates the {@link IQualifiedNameResolver}.
	 * 
	 * @return the created {@link IQualifiedNameResolver}
	 * @generated
	 */
	protected IQualifiedNameResolver createResolver() {
		final IQualifiedNameResolver resolver = new ClassLoaderQualifiedNameResolver(this.getClass()
				.getClassLoader(), EPackage.Registry.INSTANCE, AcceleoParser.QUALIFIER_SEPARATOR);

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

		return queryEnvironment;
	}

	/**
	 * Creates the {@link AcceleoEvaluator}
	 * 
	 * @param targetURI
	 *            the target {@link URI}
	 * @param resolver
	 *            the {@link IQualifiedNameResolver}
	 * @param queryEnvironment
	 *            the {@link IQualifiedNameQueryEnvironment}
	 * @return the created {@link AcceleoEvaluator}
	 * @generated
	 */
	protected AcceleoEvaluator createAcceleoEvaluator(URI targetURI, IQualifiedNameResolver resolver,
			IQualifiedNameQueryEnvironment queryEnvironment) {
		final AcceleoEvaluator evaluator = new AcceleoEvaluator(queryEnvironment.getLookupEngine(), System
				.lineSeparator());

		// final Representation profilerModelRepresentation = Representation.TREE;
		// final IProfiler profiler = ProfilerUtils.getProfiler(getModuleQualifiedName(),
		// profilerModelRepresentation, ProfilerPackage.eINSTANCE.getProfilerFactory());
		// final AcceleoEvaluator evaluator = new AcceleoProfilerEvaluator(queryEnvironment.getLookupEngine(),
		// System
		// .lineSeparator(), profiler);

		resolver.addLoader(new ModuleLoader(new AcceleoParser(), evaluator));
		resolver.addLoader(new JavaLoader(AcceleoParser.QUALIFIER_SEPARATOR, false));

		return evaluator;
	}

	/**
	 * Creates the {@link IAcceleoGenerationStrategy}
	 * 
	 * @param resourceSetForModels
	 *            the {@link ResourceSet} containing loaded models
	 * @return the created {@link IAcceleoGenerationStrategy}
	 * @generated
	 */
	protected IAcceleoGenerationStrategy createGenerationStrategy(ResourceSet resourceSetForModels) {
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
	 *            the {@link URI} for logging if any, <code>null</code> otherwise
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
		printSummary(System.out, generationResult);
	}

	/**
	 * Prints the generation summary.
	 * 
	 * @param stream
	 *            the {@link PrintStream}
	 * @param result
	 *            the {@link GenerationResult}
	 * @generated
	 */
	private void printSummary(PrintStream stream, GenerationResult result) {
		int nbErrors = 0;
		int nbWarnings = 0;
		int nbInfos = 0;
		for (Diagnostic diagnostic : result.getDiagnostic().getChildren()) {
			switch (diagnostic.getSeverity()) {
				case Diagnostic.ERROR:
					nbErrors++;
					break;

				case Diagnostic.WARNING:
					nbWarnings++;
					break;

				case Diagnostic.INFO:
					nbInfos++;
					break;

				default:
					break;
			}
		}

		stream.print("Files: " + result.getGeneratedFiles().size());
		stream.print(", Lost Files: " + result.getLostFiles().size());
		stream.print(", Errors: " + nbErrors);
		stream.print(", Warnings: " + nbWarnings);
		stream.print(", Infos: " + nbInfos);
		stream.println(".");
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
	protected void printDiagnostic(PrintStream stream, Diagnostic diagnostic, String indentation) {
		String nextIndentation = indentation;
		if (diagnostic.getMessage() != null) {
			stream.print(indentation);
			switch (diagnostic.getSeverity()) {
				case Diagnostic.INFO:
					stream.print("INFO ");
					break;

				case Diagnostic.WARNING:
					stream.print("WARNING ");
					break;

				case Diagnostic.ERROR:
					stream.print("ERROR ");
					break;
			}
			if (!diagnostic.getData().isEmpty() && diagnostic.getData().get(0) instanceof ASTNode) {
				stream.print(AcceleoUtil.getLocation((ASTNode)diagnostic.getData().get(0)));
			}
			stream.println(": " + diagnostic.getMessage().replaceAll("\n", "\n" + nextIndentation));
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
