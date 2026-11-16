/*******************************************************************************
 * Copyright (c) 2017 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.lang.unittest;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Pattern;

import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IMarker;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.ease.debugging.IScriptDebugFrame;
import org.eclipse.ease.lang.unittest.definition.IDefinitionPackage;
import org.eclipse.ease.lang.unittest.definition.ITestSuiteDefinition;
import org.eclipse.ease.lang.unittest.definition.util.DefinitionResourceFactory;
import org.eclipse.ease.lang.unittest.runtime.IRuntimeFactory;
import org.eclipse.ease.lang.unittest.runtime.IStackTraceContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestContainer;
import org.eclipse.ease.lang.unittest.runtime.ITestEntity;
import org.eclipse.ease.lang.unittest.runtime.ITestFile;
import org.eclipse.ease.lang.unittest.runtime.ITestFolder;
import org.eclipse.ease.lang.unittest.runtime.ITestResult;
import org.eclipse.ease.lang.unittest.runtime.ITestSuite;
import org.eclipse.ease.lang.unittest.runtime.TestStatus;
import org.eclipse.ease.lang.unittest.runtime.impl.TestEntity;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;
import org.eclipse.ui.texteditor.MarkerUtilities;

public final class UnitTestHelper {

	@Deprecated
	private UnitTestHelper() {
		throw new IllegalStateException("Constructor not meant to be called");
	}

	/**
	 * Create error markers in the workspace.
	 *
	 * @param result
	 *            result to create markers for
	 * @param testEntity
	 */
	public static void createWorkspaceMarker(final ITestResult result, TestEntity testEntity) {
		// add error marker
		if ((result.getStatus().getValue() == TestStatus.ERROR_VALUE) || (result.getStatus().getValue() == TestStatus.FAILURE_VALUE)) {

			List<IScriptDebugFrame> trace = result.getStackTrace();
			if ((trace == null) && (testEntity instanceof IStackTraceContainer))
				trace = ((IStackTraceContainer) testEntity).getStackTrace();

			if (trace != null) {
				for (final IScriptDebugFrame element : trace) {
					if (element.getScript() != null) {
						final Object file = element.getScript().getFile();
						if ((file instanceof IFile) && (((IFile) file).exists())) {
							try {
								final HashMap<String, Object> attributes = new HashMap<>();
								attributes.put(IMarker.LINE_NUMBER, element.getLineNumber());
								attributes.put(IMarker.SEVERITY, IMarker.SEVERITY_ERROR);
								attributes.put(IMarker.MESSAGE, result.getMessage());
								MarkerUtilities.createMarker((IFile) file, attributes, PluginConstants.PLUGIN_ID + ".scriptassertion");
							} catch (final CoreException e) {
								// silently fail; if we create log infos here this might flood the error log
							}
						}
					}
				}
			}
		}
	}

	/**
	 * Remove all test assertion error markers from a given resource.
	 *
	 * @param file
	 *            resource to remove markers from
	 */
	public static void removeErrorMarkers(IFile file) {
		try {
			file.deleteMarkers(PluginConstants.PLUGIN_ID + ".scriptassertion", false, IResource.DEPTH_ZERO);
		} catch (final CoreException e) {
			// fail gracefully, we cannot do much if markers cannot be deleted
		}
	}

	/**
	 * Find all matching files for given filters. Filter strings are paths and URIs that may contain wildcards using ANT style. Therefore '*' denotes a folder,
	 * while '**' denotes a folder hierarchy.
	 *
	 * @param filters
	 *            filters to search files for
	 * @param suite
	 *            testsuite resource for relative filters
	 * @return Map of {@link File}/IFile instances. The value contains the filter expression that lead to the match.
	 */
	public static Map<Object, String> getTestFilesFromFilter(String[] filters, Object suite) {
		final Map<Object, String> testFiles = new LinkedHashMap<>();

		for (final String token : filters) {
			if (!token.isBlank())
				testFiles.putAll(createTests(token, suite));
		}

		return testFiles;
	}

	private static Map<Object, String> createTests(String filter, Object suite) {
		final Map<Object, String> testFiles = new HashMap<>();

		final Pattern pattern = buildPattern(filter);

		if (filter.contains("*")) {

			// calculate fixed part to denote base folder
			String fixedPart = filter.substring(0, filter.indexOf('*'));
			if (fixedPart.contains("/"))
				fixedPart = fixedPart.substring(0, fixedPart.lastIndexOf('/') + 1);

			// now fixedPart should point to a folder location
			final Object folder = ResourceTools.resolve(fixedPart, suite);
			final String folderLocation = ResourceTools.toAbsoluteLocation(folder, null);

			final List<Object> children = new ArrayList<>();

			children.addAll(Arrays.asList(getChildren(folder)));

			while (!children.isEmpty()) {
				final Object child = children.remove(0);

				if (ResourceTools.isFile(child)) {
					final String fileLocation = ResourceTools.toAbsoluteLocation(child, null);
					String relativeLocation = fileLocation.substring(folderLocation.length());
					if (relativeLocation.startsWith("/"))
						relativeLocation = relativeLocation.substring(1);

					final String relevantPath = fixedPart + relativeLocation;
					if (pattern.matcher(relevantPath).matches())
						testFiles.put(child, filter);

				} else if (ResourceTools.isFolder(child)) {
					children.addAll(0, Arrays.asList(getChildren(child)));
				}
			}
		} else {
			// just a plain file address
			final Object candidate = ResourceTools.resolve(filter, suite);
			if (ResourceTools.exists(candidate))
				testFiles.put(candidate, filter);
		}

		return testFiles;
	}

	private static Object[] getChildren(Object folder) {
		try {
			if (folder instanceof IContainer)
				return ((IContainer) folder).members();
		} catch (final CoreException e) {
			// TODO handle this exception (but for now, at least know it happened)
			throw new RuntimeException(e);
		}

		if (folder instanceof File)
			return ((File) folder).listFiles();

		return new Object[0];
	}

	private static Pattern buildPattern(String filter) {
		if (filter.endsWith("/"))
			filter += "**";

		filter = filter.replaceAll("[\\<\\(\\[\\{\\\\\\^\\-\\=\\$\\!\\|\\]\\}\\)‌​\\?\\*\\+\\.\\>]", "\\\\$0");
		filter = filter.replaceAll("\\Q\\*\\*\\E", ".*");
		filter = filter.replaceAll("\\Q\\*\\E", "[^\\/]*");

		return Pattern.compile(filter);
	}

	/**
	 * Creates a test structure for a given set of test files. Automatically creates folders to match the file structure the files are located in.
	 *
	 * @param acceptedFiles
	 *            map of accepted files
	 * @return root elements of the created file structure.
	 */
	public static List<ITestEntity> createTestStructure(Map<Object, String> acceptedFiles) {
		final List<ITestEntity> testRoot = new ArrayList<>();

		int insertionIndex = 1;

		for (final Entry<Object, String> entry : acceptedFiles.entrySet()) {
			String testFileLocation = ResourceTools.toAbsoluteLocation(entry.getKey(), null);
			testFileLocation = testFileLocation.replace("://", "/").replace(":/", "/");
			final IPath testFilePath = new Path(testFileLocation).makeAbsolute();

			final ITestFile testFile = IRuntimeFactory.eINSTANCE.createTestFile();
			testFile.setResource(entry.getKey());
			testFile.setName(testFilePath.lastSegment());
			testFile.setDescription(entry.getValue());
			testFile.setInsertionOrder(insertionIndex++);

			final ITestFolder container = createTestFolder(testFilePath.removeLastSegments(1), testRoot);
			container.getChildren().add(testFile);
		}

		return testRoot;
	}

	private static ITestFolder createTestFolder(IPath path, List<ITestEntity> rootElements) {
		if (path.segmentCount() > 1) {
			final ITestFolder targetFolder = createTestFolder(path.removeLastSegments(1), rootElements);

			for (final ITestEntity entity : targetFolder.getChildren()) {
				if ((entity instanceof ITestFolder) && (path.lastSegment().equals(entity.getName())))
					return (ITestFolder) entity;
			}

			// entry not found, create one
			final ITestFolder newFolder = IRuntimeFactory.eINSTANCE.createTestFolder();
			newFolder.setName(path.lastSegment());

			targetFolder.getChildren().add(newFolder);
			return newFolder;

		} else {
			for (final ITestEntity entity : rootElements) {
				if ((entity instanceof ITestFolder) && (path.lastSegment().equals(entity.getName())))
					return (ITestFolder) entity;
			}

			// entry not found, create one
			final ITestFolder newFolder = IRuntimeFactory.eINSTANCE.createTestFolder();
			newFolder.setName(path.lastSegment());

			rootElements.add(newFolder);
			return newFolder;
		}
	}

	public static ITestSuiteDefinition loadTestSuite(InputStream stream) throws IOException {
		// load resource
		final ResourceSet resourceSet = new ResourceSetImpl();

		resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().put(Resource.Factory.Registry.DEFAULT_EXTENSION, new XMIResourceFactoryImpl());
		resourceSet.getPackageRegistry().put("http://eclipse.org/ease/unittest/testsuite/1.0", IDefinitionPackage.eINSTANCE);
		resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().put("suite", new DefinitionResourceFactory());
		final Resource resource = resourceSet.createResource(URI.createURI("*.suite"));

		resource.load(stream, null);
		final EObject content = resource.getContents().get(0);

		if (content instanceof ITestSuiteDefinition)
			return (ITestSuiteDefinition) content;

		return null;
	}

	/**
	 * Serialize a testsuite definition to a byte array.
	 *
	 * @param testSuiteDefinition
	 *            test suite definition to serialize
	 * @return xml representation of definition
	 * @throws IOException
	 *             not expected as ByteArrayOutputStream does not throw
	 */
	public static byte[] serializeTestSuite(ITestSuiteDefinition testSuiteDefinition) throws IOException {
		final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

		final ResourceSet resourceSet = new ResourceSetImpl();

		resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().put(Resource.Factory.Registry.DEFAULT_EXTENSION, new XMIResourceFactoryImpl());
		resourceSet.getPackageRegistry().put("http://eclipse.org/ease/unittest/testsuite/1.0", IDefinitionPackage.eINSTANCE);
		resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().put("suite", new DefinitionResourceFactory());

		final Resource resource = resourceSet.createResource(URI.createURI("*.suite"));
		resource.getContents().add(testSuiteDefinition);

		resource.save(outputStream, Collections.EMPTY_MAP);

		return outputStream.toByteArray();
	}

	/**
	 * Create a runtime representation of a given test suite definition.
	 *
	 * @param definition
	 *            definition to create runtime information from
	 * @return runtime information root element
	 */
	public static ITestSuite createRuntimeSuite(ITestSuiteDefinition definition) {
		final String[] includeFilters = (definition.getIncludeFilter() != null) ? definition.getIncludeFilter().split("\r?\n") : new String[0];
		final String[] excludeFilters = (definition.getExcludeFilter() != null) ? definition.getExcludeFilter().split("\r?\n") : new String[0];

		final Map<Object, String> includedFiles = UnitTestHelper.getTestFilesFromFilter(includeFilters, definition.getResource());
		final Map<Object, String> excludedFiles = UnitTestHelper.getTestFilesFromFilter(excludeFilters, definition.getResource());

		includedFiles.keySet().removeAll(excludedFiles.keySet());

		final List<ITestEntity> testStructure = UnitTestHelper.createTestStructure(includedFiles);

		final ITestSuite testSuite = IRuntimeFactory.eINSTANCE.createTestSuite();
		testSuite.getChildren().addAll(testStructure);
		testSuite.setName(definition.getName());

		testSuite.setDefinition(definition);

		return testSuite;
	}

	public static Collection<ITestFile> getTestFiles(ITestContainer testContainer) {
		if (testContainer instanceof ITestFile)
			return Arrays.asList((ITestFile) testContainer);

		final Collection<ITestFile> testFiles = new HashSet<>();

		for (final ITestContainer child : testContainer.getChildContainers())
			testFiles.addAll(getTestFiles(child));

		return testFiles;
	}
}
