/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
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
package org.eclipse.ease.modules.platform;

import java.io.File;
import java.net.URI;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.debug.core.ILaunch;
import org.eclipse.debug.core.ILaunchConfiguration;
import org.eclipse.ease.IDebugEngine;
import org.eclipse.ease.IExecutionListener;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.IScriptable;
import org.eclipse.ease.Logger;
import org.eclipse.ease.Script;
import org.eclipse.ease.ScriptResult;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.ease.service.EngineDescription;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptService;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ease.ui.launching.EaseLaunchDelegate;
import org.eclipse.ui.PlatformUI;

/**
 * Commands to launch additional script engines.
 */
public class ScriptingModule extends AbstractScriptModule {

	/** Module identifier. */
	public static final String MODULE_ID = "/System/Scripting";

	/**
	 * Split a string with comma separated arguments.
	 *
	 * @param arguments
	 *            comma separated arguments
	 * @return trimmed list of arguments
	 */
	public static final String[] extractArguments(final String arguments) {
		final ArrayList<String> args = new ArrayList<>();

		if (arguments != null) {
			for (final String token : arguments.split(",")) {
				if (!token.isBlank())
					args.add(token.trim());
			}
		}

		return args.toArray(new String[0]);
	}

	/**
	 * Create a new script engine instance.
	 *
	 * @param identifier
	 *            engine ID, literal engine name or accepted file extension
	 * @return script engine instance (not started) or <code>null</code>
	 */
	@WrapToScript
	public static IScriptEngine createScriptEngine(final String identifier) {
		IScriptService scriptService;
		try {
			scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);
		} catch (final IllegalStateException e) {
			// in headless mode the workbench is not ready
			scriptService = ScriptService.getInstance();
		}

		// by ID
		EngineDescription engine = scriptService.getEngineByID(identifier);
		if (engine != null)
			return engine.createEngine();

		// by literal name
		final Collection<EngineDescription> engines = scriptService.getEngines();
		for (final EngineDescription description : engines) {
			if (description.getName().equals(identifier))
				return description.createEngine();
		}

		// by script type
		engine = scriptService.getEngine(identifier);
		if (engine != null)
			return engine.createEngine();

		// giving up
		return null;
	}

	/**
	 * Retrieve a list of available script engines.
	 *
	 * @return array of engine IDs
	 */
	@WrapToScript
	public static String[] listScriptEngines() {
		final List<String> result = new ArrayList<>();

		IScriptService scriptService;
		try {
			scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);
		} catch (final IllegalStateException e) {
			// in headless mode the workbench is not ready
			scriptService = ScriptService.getInstance();
		}

		for (final EngineDescription description : scriptService.getEngines())
			result.add(description.getID());

		return result.toArray(new String[result.size()]);
	}

	/**
	 * Fork a new script engine and execute provided resource.
	 *
	 * @param resource
	 *            resource to execute (path, URI or file instance)
	 * @param arguments
	 *            optional script arguments delimited by commas ','. When the string arguments contains commas ',', or for arguments that are not string, the
	 *            caller may set a shared object with {@module #setSharedObject(String, Object, boolean, boolean)} and pass the key here. The callee can then
	 *            retrieve it with the {@module #getSharedObject(String)} method.
	 * @param engineIdOrExtension
	 *            engine ID to be used or a file extension to look for engines (eg: js)
	 * @return execution result
	 */
	@WrapToScript
	public ScriptResult fork(final Object resource, @ScriptParameter(defaultValue = ScriptParameter.NULL) final String arguments,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) String engineIdOrExtension) {

		final ILaunch currentLaunch = getScriptEngine().getLaunch();
		final boolean useDebugger = (currentLaunch != null) && (currentLaunch.getDebugTarget() != null);

		IScriptService scriptService;
		try {
			scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);
		} catch (final IllegalStateException e) {
			// in headless mode the workbench is not ready
			scriptService = ScriptService.getInstance();
		}

		EngineDescription description = null;
		if (engineIdOrExtension != null) {
			description = scriptService.getEngineByID(engineIdOrExtension);

			if (description == null) {
				final ScriptType scriptType = scriptService.getScriptType("." + engineIdOrExtension);
				if (scriptType != null) {
					if (useDebugger)
						description = scriptType.getDebugEngine();

					if (description == null)
						description = scriptType.getEngine();
				}
			}

			if (description == null)
				throw new RuntimeException("No script engine found for ID = \"" + engineIdOrExtension + "\"");
		}

		if (description == null) {
			// try to find engine for script type
			final String location = ResourceTools.toAbsoluteLocation(resource, getScriptEngine().getExecutedFile());
			final ScriptType scriptType = scriptService.getScriptType(location);
			if (scriptType != null) {
				if (useDebugger)
					description = scriptType.getDebugEngine();

				if (description == null)
					description = scriptType.getEngine();
			}
		}

		if (description != null) {
			final IScriptEngine engine = description.createEngine();

			// connect streams
			engine.setOutputStream(getScriptEngine().getOutputStream());
			engine.setErrorStream(getScriptEngine().getErrorStream());
			engine.setInputStream(getScriptEngine().getInputStream());
			engine.setCloseStreamsOnTerminate(false);

			// setup debugger
			if ((useDebugger) && (engine instanceof IDebugEngine)) {
				final ILaunchConfiguration launchConfiguration = currentLaunch.getLaunchConfiguration();
				if (launchConfiguration != null) {
					((IDebugEngine) engine).setupDebugger(currentLaunch, EaseLaunchDelegate.getSuspendOnStartupValue(launchConfiguration),
							EaseLaunchDelegate.getSuspendOnScriptLoadValue(launchConfiguration),
							EaseLaunchDelegate.getDisplayDynamicCodeValue(launchConfiguration));

				}
			}

			// set input parameters
			engine.setVariable("argv", extractArguments(arguments));

			Object scriptObject = ResourceTools.resolve(resource, getScriptEngine().getExecutedFile());
			if (scriptObject == null) {
				// no file available, try to resolve URI
				scriptObject = URI.create(resource.toString());
			}

			final ScriptResult result = engine.execute(scriptObject);
			engine.schedule();
			return result;
		}

		throw new RuntimeException("No script engine found for source \"" + resource + "\"");
	}

	/**
	 * Wait for a script engine to shut down. If <i>timeout</i> is set to 0 this method will wait endlessly.
	 *
	 * @param engine
	 *            script engine to wait for
	 * @param timeout
	 *            time to wait for shutdown [ms]
	 * @return <code>true</code> when engine is shut down
	 */
	@WrapToScript
	public static boolean join(final IScriptEngine engine, @ScriptParameter(defaultValue = "0") final long timeout) {
		if (engine instanceof Job) {
			final long stopWaitingTime = System.currentTimeMillis() + timeout;
			try {
				while (((Job) engine).getState() != Job.NONE) {
					final long now = System.currentTimeMillis();
					if (timeout == 0)
						Thread.sleep(1000);

					else if (stopWaitingTime > now)
						Thread.sleep(Math.min(stopWaitingTime - now, 1000));

					else
						// timeout depleted
						return false;
				}
			} catch (final InterruptedException e) {
				// we got interrupted - ev the current engine is shutting down?
				return false;
			}

			// job terminated
			return true;
		}

		// cannot evaluate engine state
		throw new RuntimeException("Cannot evaluate engine state");
	}

	/**
	 * Run a code fragment in a synchronized block. Executes <i>code</i> within a synchronized block on the <i>monitor</i> object. The code object might be a
	 * {@link String}, {@link File}, {@link IFile} or any other object that can be adapted to {@link IScriptable}.
	 *
	 * @param monitor
	 *            monitor to synchronize on
	 * @param code
	 *            code to run.
	 * @return execution result of executed code
	 * @throws ExecutionException
	 *             when execution of <i>code</i> fails
	 */
	@WrapToScript
	public Object executeSync(final Object monitor, final Object code) throws ExecutionException {
		synchronized (monitor) {
			return getScriptEngine().inject(code, false);
		}
	}

	/**
	 * Causes the current thread to wait until either another thread invokes the {@link java.lang.Object#notify()} method or the
	 * {@link java.lang.Object#notifyAll()} method for this object, or a specified amount of time has elapsed. Calls the java method monitor.wait(timeout).
	 *
	 * @param monitor
	 *            monitor to wait for
	 * @param timeout
	 *            max timeout (0 does not time out)
	 * @throws InterruptedException
	 *             when wait gets interrupted
	 */
	@WrapToScript
	public static void wait(final Object monitor, @ScriptParameter(defaultValue = "0") final long timeout) throws InterruptedException {
		synchronized (monitor) {
			monitor.wait(timeout);
		}
	}

	/**
	 * Wakes up a single thread that is waiting on the monitor. Calls the java method monitor.notify().
	 *
	 * @param monitor
	 *            monitor to notify
	 */
	@WrapToScript
	public static void notify(final Object monitor) {
		synchronized (monitor) {
			monitor.notify();
		}
	}

	/**
	 * Wakes up all threads that are waiting on the monitor. Calls the java method monitor.notifyAll().
	 *
	 * @param monitor
	 *            monitor to notify
	 */
	@WrapToScript
	public static void notifyAll(final Object monitor) {
		synchronized (monitor) {
			monitor.notifyAll();
		}
	}

	/**
	 * Add an object to the shared object store. The shared object store allows to share java instances between several script engines. By default objects are
	 * stored until the script engine providing it is terminated. This helps to avoid polluting the java heap. When <i>permanent</i> is set to <code>true</code>
	 * , this object will be stored forever.
	 *
	 * @param key
	 *            key to store the object
	 * @param object
	 *            instance to store
	 * @param permanent
	 *            flag indicating permanent storage
	 * @param writable
	 *            flag indicating that any engine may write this value
	 * @throws IllegalAccessException
	 *             when scriptEngine is not the owner of the shared object
	 */
	@WrapToScript
	public void setSharedObject(final String key, final Object object, @ScriptParameter(defaultValue = ScriptParameter.FALSE) final boolean permanent,
			@ScriptParameter(defaultValue = ScriptParameter.FALSE) final boolean writable) throws IllegalAccessException {
		ScriptStorage.getInstance().put(key, object, getScriptEngine(), permanent, writable);
	}

	/**
	 * Get an object from the shared object store.
	 *
	 * @param key
	 *            key to retrieve object for
	 * @return shared object or <code>null</code>
	 */
	@WrapToScript
	public Object getSharedObject(final String key) {
		return ScriptStorage.getInstance().get(key);
	}

	/**
	 * Storage element for {@link ScriptStorage}.
	 */
	private static class StorageElement {
		public Object fElement;
		public Object fOwner;
		public boolean fPermanent;
		private final boolean fWritable;

		public StorageElement(final Object element, final Object owner, final boolean permanent, final boolean writable) {
			fElement = element;
			fOwner = owner;
			fPermanent = permanent;
			fWritable = writable;
		}
	}

	/**
	 * Storage singleton to share objects. This class is synchronized.
	 */
	private static class ScriptStorage implements IExecutionListener {
		private static ScriptStorage fInstance = null;

		/**
		 * Get the singleton instance.
		 *
		 * @return singleton ScriptStorage
		 */
		public synchronized static ScriptStorage getInstance() {
			if (fInstance == null)
				fInstance = new ScriptStorage();

			return fInstance;
		}

		/** Stored elements. */
		private final Map<String, StorageElement> fElements = new HashMap<>();

		/**
		 * Retrieve a shared object.
		 *
		 * @param key
		 *            key to retrieve object for
		 * @return shared object or <code>null</code>
		 */
		public synchronized Object get(final String key) {
			final StorageElement storedElement = fElements.get(key);
			return (storedElement != null) ? storedElement.fElement : null;
		}

		/**
		 * @param key
		 *            key to store the object
		 * @param object
		 *            instance to store
		 * @param scriptEngine
		 *            script engine asking for storage
		 * @param permanent
		 *            flag indicating permanent storage
		 * @param writable
		 *            flag indicating that any engine may write this value
		 * @throws IllegalAccessException
		 *             when scriptEngine is not the owner of the shared object
		 */
		public synchronized void put(final String key, final Object object, final IScriptEngine scriptEngine, final boolean permanent, final boolean writable)
				throws IllegalAccessException {
			if (fElements.containsKey(key))
				remove(key, scriptEngine);

			fElements.put(key, new StorageElement(object, getOwner(scriptEngine), permanent, writable));

			if (!permanent)
				scriptEngine.addExecutionListener(this);
		}

		/**
		 * @param key
		 * @param scriptEngine
		 * @throws IllegalAccessException
		 *             when scriptEngine is not the owner of the shared object
		 */
		public synchronized void remove(final String key, final IScriptEngine scriptEngine) throws IllegalAccessException {
			if (fElements.containsKey(key)) {
				// verify that current scriptEngine is the owner of this value or the object is writable
				final StorageElement element = fElements.get(key);
				if ((element.fWritable) || (element.fOwner.equals(getOwner(scriptEngine)))) {

					// remove element
					fElements.remove(key);
				} else
					throw new IllegalAccessException("Engine is not the owner of shared object \"" + key + "\"");
			}
		}

		/**
		 * Get unique token for object owner.
		 *
		 * @param engine
		 *            script engine owner
		 * @return owner token
		 */
		private static Object getOwner(final IScriptEngine engine) {
			// we do not want to keep the whole script engine around as owner for permanent objects as script engines are big objects.
			return engine.hashCode();
		}

		@Override
		public synchronized void notify(final IScriptEngine engine, final Script script, final int status) {
			if (status == IExecutionListener.ENGINE_END) {

				// clean up owned elements
				for (final String key : new HashSet<>(fElements.keySet())) {
					final StorageElement element = fElements.get(key);
					if ((element.fOwner.equals(getOwner(engine)) && (!element.fPermanent))) {
						try {
							remove(key, engine);
						} catch (final IllegalAccessException e) {
							// we already checked that we are the owner, so this should not happen
							Logger.error(PluginConstants.PLUGIN_ID, "Error while cleaning up shared objects", e);
						}
					}
				}

				if (fElements.isEmpty())
					// we are empty, clean up singleton
					fInstance = null;

				engine.removeExecutionListener(this);
			}
		}
	}
}
