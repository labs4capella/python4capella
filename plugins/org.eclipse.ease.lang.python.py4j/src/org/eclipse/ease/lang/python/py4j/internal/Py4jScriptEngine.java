/*******************************************************************************
 * Copyright (c) 2016 Kichwa Coders and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Jonah Graham (Kichwa Coders) - initial API and implementation
 *******************************************************************************/
package org.eclipse.ease.lang.python.py4j.internal;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.URIUtil;
import org.eclipse.core.variables.IStringVariableManager;
import org.eclipse.core.variables.VariablesPlugin;
import org.eclipse.ease.AbstractReplScriptEngine;
import org.eclipse.ease.Logger;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptEngineException;
import org.eclipse.ease.ScriptExecutionException;
import org.eclipse.ease.ScriptResult;
import org.eclipse.ease.classloader.EaseClassLoader;
import org.eclipse.ease.debugging.ScriptStackTrace;
import org.eclipse.ease.tools.RunnableWithResult;
import org.eclipse.jface.preference.IPreferenceStore;
import org.eclipse.swt.widgets.Display;
import org.osgi.framework.Bundle;

import py4j.ClientServer;
import py4j.ClientServer.ClientServerBuilder;
import py4j.JavaServer;
import py4j.Py4JException;

public class Py4jScriptEngine extends AbstractReplScriptEngine {

	/**
	 * The ID of the Engine, to match the declaration in the plugin.xml.
	 */
	public static final String ENGINE_ID = "org.eclipse.ease.lang.python.py4j.engine";

	// TODO: Add preference for this
	private static final int PYTHON_STARTUP_TIMEOUT_SECONDS = 10;

	// TODO: Add preference for this
	private static final int PYTHON_SHUTDOWN_TIMEOUT_SECONDS = 10;

	/**
	 * Path within this plug-in to the main python file.
	 */
	private static final String PYSRC_EASE_PY4J_MAIN_PY = "/pysrc/ease_py4j_main.py";

	/**
	 * The ID of the py4j sources plug-in, needs to match the name of the dependent plug-in.
	 */
	private static final String PY4J_PYTHON_BUNDLE_ID = "py4j-python";

	/**
	 * Standard StreamGobbler.
	 */
	private static final class StreamGobbler implements Runnable {
		private final InputStream fReader;
		private final OutputStream fWriter;
		private final String fStreamName;

		private StreamGobbler(final InputStream stream, final OutputStream output, final String streamName) {
			fReader = stream;
			fWriter = output;
			fStreamName = streamName;
		}

		@Override
		public void run() {
			try {
				final byte[] bytes = new byte[512];
				int readCount;
				while ((readCount = fReader.read(bytes)) >= 0) {
					try {
						fWriter.write(bytes, 0, readCount);
					} catch (final IOException e) {
						Logger.error(Activator.PLUGIN_ID, "Failed to write data read from Python's " + fStreamName + " stream.", e);
					}
				}
			} catch (final IOException e) {
				Logger.error(Activator.PLUGIN_ID, "Failed to read data from Python's " + fStreamName + " stream.", e);
			}
		}
	}

	private ClientServer fGatewayServer;
	protected IPythonSideEngine fPythonSideEngine;
	private Process fPythonProcess;
	private Thread fInputGobbler;
	private Thread fErrorGobbler;

	private CountDownLatch fPythonStartupComplete;

	public Py4jScriptEngine() {
		super("Python (Py4J)");
	}

	@Override
	protected void setupEngine() throws ScriptEngineException {
		try {
			fPythonStartupComplete = new CountDownLatch(1);
			fGatewayServer = new ClientServerBuilder(this).javaPort(0).pythonPort(0).build();
			fGatewayServer.startServer(true);
			final int javaListeningPort = ((JavaServer) fGatewayServer.getJavaServer()).getListeningPort();

			fPythonProcess = startPythonProcess(javaListeningPort);
			fInputGobbler = new Thread(new StreamGobbler(fPythonProcess.getInputStream(), getOutputStream(), "stdout"),
					"EASE py4j engine output stream gobbler");
			fInputGobbler.start();
			fErrorGobbler = new Thread(new StreamGobbler(fPythonProcess.getErrorStream(), getErrorStream(), "stderr"), "EASE py4j engine error stream gobbler");
			fErrorGobbler.start();

			// TODO Handle python's stdin (fPythonProcess.getOutputStream())

			if (!fPythonStartupComplete.await(PYTHON_STARTUP_TIMEOUT_SECONDS, TimeUnit.SECONDS)) {
				throw new ScriptEngineException("Python process did not start within " + PYTHON_STARTUP_TIMEOUT_SECONDS + " seconds");
			}
		} catch (final ScriptEngineException e) {
			teardownEngine();
			throw e;
		} catch (final Exception e) {
			teardownEngine();
			throw new ScriptEngineException("Failed to start Python process. Please check the setting for the Python interpreter"
					+ " in Preferences -> Scripting -> Python Scripting:\n" + e.getMessage(), e);
		}
	}

	private Process startPythonProcess(final int javaListeningPort) throws IOException, MalformedURLException, URISyntaxException, CoreException {
		final ProcessBuilder pb = new ProcessBuilder();

		final IPreferenceStore preferenceStore = Activator.getDefault().getPreferenceStore();
		String interpreter = preferenceStore.getString(Py4JScriptEnginePrefConstants.INTERPRETER);
		final boolean ignorePythonEnvVariables = preferenceStore.getBoolean(Py4JScriptEnginePrefConstants.IGNORE_PYTHON_ENV_VARIABLES);
		final IStringVariableManager variableManager = VariablesPlugin.getDefault().getStringVariableManager();
		interpreter = variableManager.performStringSubstitution(interpreter);

		pb.command().add(interpreter);
		pb.command().add("-u");
		if (ignorePythonEnvVariables) {
			pb.command().add("-E");
		}
		pb.command().add(getPy4jEaseMainPy().toString());
		pb.command().add(Integer.toString(javaListeningPort));
		pb.command().addAll(getPythonPathAdditions());

		return pb.start();
	}

	private List<String> getPythonPathAdditions() throws IOException {
		final List<String> pathAdditions = new ArrayList<>();

		pathAdditions.add(getPy4jPythonSrc().toString());

		// Add EASE Python directory to python path
		final Bundle bundle = Platform.getBundle("org.eclipse.ease.lang.python");
		try {
			URL url = bundle.getEntry("pysrc");
			url = FileLocator.toFileURL(url);
			final URI uri = new URI(url.getProtocol(), url.getPath(), null);
			pathAdditions.add(new File(uri).getAbsolutePath());

		} catch (final IllegalStateException e) {
			Logger.error(Activator.PLUGIN_ID, "Cannot get entry pysrc because the plugin has not been initialized properly.", e);

		} catch (final IOException | URISyntaxException e) {
			Logger.error(Activator.PLUGIN_ID, "Cannot append additional Python modules to search path.", e);
		}
		return pathAdditions;
	}

	private File getPy4jPythonSrc() throws IOException {
		final File py4jPythonBundleFile = FileLocator.getBundleFile(Platform.getBundle(PY4J_PYTHON_BUNDLE_ID));
		final File py4jPythonSrc = new File(py4jPythonBundleFile, "/src");
		final File py4j = new File(py4jPythonSrc, "py4j");
		if (!py4j.exists() || !py4j.isDirectory()) {
			throw new IOException("Failed to find py4j python directory, expected it here: " + py4j);
		}
		return py4jPythonSrc;
	}

	private File getPy4jEaseMainPy() throws MalformedURLException, IOException, URISyntaxException {
		final URL url = new URL("platform:/plugin/" + Activator.PLUGIN_ID + PYSRC_EASE_PY4J_MAIN_PY);
		final URL fileURL = FileLocator.toFileURL(url);
		final File py4jEaseMain = new File(URIUtil.toURI(fileURL));
		if (!py4jEaseMain.exists()) {
			throw new IOException("Failed to find " + PYSRC_EASE_PY4J_MAIN_PY + ", expected it here: " + py4jEaseMain);
		}
		return py4jEaseMain;
	}

	public void pythonStartupComplete(final int pythonPort, final IPythonSideEngine pythonSideEngine) {
		final JavaServer javaServer = (JavaServer) fGatewayServer.getJavaServer();
		javaServer.resetCallbackClient(javaServer.getCallbackClient().getAddress(), pythonPort);
		fPythonSideEngine = pythonSideEngine;
		fPythonStartupComplete.countDown();
	}

	@Override
	protected Object execute(final Script script, final String fileName, final boolean uiThread) throws Throwable {
		if (uiThread) {
			// run in UI thread
			final RunnableWithResult<Object> runnable = new RunnableWithResult<>() {

				@Override
				public Object runWithTry() throws Throwable {
					return internalExecute(script, fileName);
				}
			};

			Display.getDefault().syncExec(runnable);
			return runnable.getResultOrThrow();

		} else {
			return internalExecute(script, fileName);
		}
	}

	protected Object internalExecute(final Script script, final String fileName) throws Throwable {

		if (hasVariable("argv"))
			fPythonSideEngine.executeScript("import sys\nsys.argv = argv\n", "<dynamic>");

		IInteractiveReturn interactiveReturn;
		if (script.isShellMode()) {
			interactiveReturn = fPythonSideEngine.executeInteractive(script.getCode());
		} else {
			interactiveReturn = fPythonSideEngine.executeScript(script.getCode(), fileName);
		}
		final Object exception = interactiveReturn.getException();
		if (exception instanceof Throwable) {
			throw (Throwable) exception;
		} else if (exception != null) {
			throw new ScriptExecutionException(new RuntimeException(Objects.toString(exception)), new ScriptStackTrace());
		} else {
			return interactiveReturn.getResult();
		}
	}

	@Override
	public void terminateCurrent() {
		// It isn't possible to safely/reliablily interrupt a thread in Python
	}

	@Override
	protected void teardownEngine() {

		if (fPythonSideEngine != null) {
			try {
				fPythonSideEngine.teardownEngine();
			} catch (final Py4JException e) {
				// ignore
			}
		}

		if (fPythonProcess != null) {
			fPythonProcess.destroy();

			try {
				fPythonProcess.waitFor(PYTHON_SHUTDOWN_TIMEOUT_SECONDS, TimeUnit.SECONDS);
			} catch (final InterruptedException e) {
				// ignore
			} finally {
				// The clean shutdown had a chance, if it is still around, kill it
				fPythonProcess.destroyForcibly();
			}
		}

		try {
			// Wait until the gobblers have shovelled all their
			// inputs before allowing the engine to considered terminated
			if (fInputGobbler != null)
				fInputGobbler.join();

			if (fErrorGobbler != null)
				fErrorGobbler.join();

		} catch (final InterruptedException e) {
			// ignore
		}

		if (fGatewayServer != null)
			fGatewayServer.shutdown();

		// allow for garbage collection
		fGatewayServer = null;
		fPythonSideEngine = null;
		fPythonProcess = null;
		fInputGobbler = null;
		fErrorGobbler = null;
	}

	@Override
	public void registerJar(final URL url) {
		ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
		if (!(classLoader instanceof EaseClassLoader)) {
			classLoader = new EaseClassLoader(classLoader);
			Thread.currentThread().setContextClassLoader(classLoader);
		}

		if (classLoader instanceof EaseClassLoader)
			((EaseClassLoader) classLoader).registerURL(this, url);
	}

	@Override
	protected Object internalGetVariable(final String name) {
		return fPythonSideEngine.internalGetVariable(name);
	}

	@Override
	protected Map<String, Object> internalGetVariables() {
		return fPythonSideEngine.internalGetVariables();
	}

	@Override
	protected boolean internalHasVariable(final String name) {
		return fPythonSideEngine.internalHasVariable(name);
	}

	@Override
	protected void internalSetVariable(final String name, final Object content) {
		fPythonSideEngine.internalSetVariable(name, content);
	}

	@SuppressWarnings("unchecked")
	@Override
	public <T> T getAdapter(final Class<T> adapter) {
		if (adapter.isInstance(fPythonProcess)) {
			return (T) fPythonProcess;
		}
		return super.getAdapter(adapter);
	}

	@Override
	public String toString(Object object) {
		if ((object == null) || (ScriptResult.VOID.equals(object)))
			return null;

		return super.toString(object);
	}
}
