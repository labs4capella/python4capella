package org.eclipse.ease.modules.platform;

import java.io.File;
import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

import org.eclipse.core.commands.Command;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.commands.NotEnabledException;
import org.eclipse.core.commands.NotHandledException;
import org.eclipse.core.commands.common.NotDefinedException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.core.runtime.preferences.IEclipsePreferences;
import org.eclipse.core.runtime.preferences.InstanceScope;
import org.eclipse.e4.core.services.events.IEventBroker;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.commands.ICommandService;
import org.eclipse.ui.services.IEvaluationService;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;
import org.osgi.service.prefs.BackingStoreException;

/**
 * Provides global platform functions like preferences, event bus or the command framework.
 */
public class PlatformModule extends ScriptingModule {

	/**
	 *
	 */
	private static final String KEEP_PROCESS_OUTPUT = "keep";
	/** Module identifier. */
	public static final String MODULE_ID = "/System/Platform";

	/**
	 * Adapt object to target type. Try to get an adapter for an object.
	 *
	 * @param source
	 *            object to adapt
	 * @param target
	 *            target class to adapt to
	 * @return adapted object or <code>null</code>
	 */
	@WrapToScript
	public Object adapt(final Object source, final Class<?> target) {
		return Platform.getAdapterManager().getAdapter(source, target);
	}

	/**
	 * Get a platform service.
	 *
	 * @param type
	 *            service type
	 * @return service instance or <code>null</code>
	 */
	@WrapToScript
	public Object getService(final Class<?> type) {
		return PlatformUI.getWorkbench().getService(type);
	}

	/**
	 * Execute a command from the command framework. As we have no UI available, we do not pass a control to the command. Hence HandlerUtil.getActive...
	 * commands will very likely fail.
	 *
	 * @param commandId
	 *            full id of the command to execute
	 * @param parameters
	 *            command parameters
	 * @throws ExecutionException
	 *             If the handler has problems executing this command.
	 * @throws NotDefinedException
	 *             If the command you are trying to execute is not defined.
	 * @throws NotEnabledException
	 *             If the command you are trying to execute is not enabled.
	 * @throws NotHandledException
	 *             If there is no handler.
	 */
	@WrapToScript
	public void executeCommand(final String commandId, @ScriptParameter(defaultValue = ScriptParameter.NULL) final Map<String, String> parameters)
			throws ExecutionException, NotDefinedException, NotEnabledException, NotHandledException {
		final Map<String, String> commandParameters = (parameters != null) ? parameters : new HashMap<>();
		final ICommandService commandService = (ICommandService) getService(ICommandService.class);
		final IEvaluationService evaluationService = (IEvaluationService) getService(IEvaluationService.class);

		final Command command = commandService.getCommand(commandId);
		command.executeWithChecks(new ExecutionEvent(command, commandParameters, null, evaluationService.getCurrentState()));
	}

	/**
	 * Get a system property or environment value. First we try to look up a system property. If not found we query the environment for the key.
	 *
	 * @param key
	 *            key to query
	 * @return system property/environment variable for <i>key</i>
	 */
	@WrapToScript
	public String getSystemProperty(final String key) {
		final String value = System.getProperty(key);

		return (value != null) ? value : System.getenv(key);
	}

	/**
	 * Run an external process. The process is started in the background and a {@link Process} object is returned. Query the result for finished state, output
	 * and error streams of the executed process. Output and error streams need to be consumed, otherwise the running process may stall (or even die) in case
	 * that the buffers are full. Setting parameters <i>output</i> and <i>error</i> to <code>null</code> will automatically discard the produced data.
	 *
	 * @param name
	 *            program to run (with full path if necessary)
	 * @param args
	 *            program arguments
	 * @param output
	 *            output file location to redirect output to.
	 *            <ul>
	 *            <li>"system.out": use the default output of the application</li>
	 *            <li>null: discard output</li>
	 *            <li>"keep": do nothing, let the script deal with it</li>
	 *            <li>any other: file location to redirect to. Accepts absolute file paths and workspace urls (see
	 *            {@module org.eclipse.ease.modules.platform.resources.ResourcesModule})</li>
	 *            </ul>
	 * @param error
	 *            error stream to redirect output to.
	 *            <ul>
	 *            <li>"system.err": use the default output of the application</li>
	 *            <li>null: discard output</li>
	 *            <li>"keep": do nothing, let the script deal with it</li>
	 *            <li>any other: file location to redirect to. Accepts absolute file paths and workspace urls (see
	 *            {@module org.eclipse.ease.modules.platform.resources.ResourcesModule})</li>
	 *            </ul>
	 * @return process object to track process execution
	 * @throws IOException
	 *             if an I/O error occurs
	 */
	@WrapToScript
	public Process runProcess(final String name, @ScriptParameter(defaultValue = ScriptParameter.NULL) final String[] args,
			@ScriptParameter(defaultValue = "system.out") String output, @ScriptParameter(defaultValue = "system.err") String error) throws IOException {
		final List<String> arguments = new ArrayList<>();
		arguments.add(name);
		if (args != null)
			arguments.addAll(Arrays.asList(args));

		final ProcessBuilder builder = new ProcessBuilder(arguments);

		if (output == null) {
			builder.redirectOutput(Redirect.DISCARD);

		} else if ("system.out".equalsIgnoreCase(output))
			builder.redirectOutput(Redirect.INHERIT);

		else if (!KEEP_PROCESS_OUTPUT.equalsIgnoreCase(output)) {
			final File target = ResourceTools.toFile(ResourceTools.resolve(output, getScriptEngine().getExecutedFile()));
			builder.redirectOutput(target);
		}

		if (error == null) {
			builder.redirectError(Redirect.DISCARD);

		} else if ("system.err".equalsIgnoreCase(error))
			builder.redirectError(Redirect.INHERIT);

		else if (!KEEP_PROCESS_OUTPUT.equalsIgnoreCase(error)) {
			final File target = ResourceTools.toFile(ResourceTools.resolve(output, getScriptEngine().getExecutedFile()));
			builder.redirectError(target);
		}

		return builder.start();
	}

	/**
	 * Read a preferences value. The <i>defaultValue</i> is optional, but contains type information if used. Provide instances of Boolean, Integer, Double,
	 * Float, Long, byte[], or String to get the appropriate return value of same type.
	 *
	 * @param node
	 *            node to read from
	 * @param key
	 *            key name to read from
	 * @param defaultValue
	 *            default value to use, if value is not set
	 * @return preference value or <code>null</code>
	 */
	@WrapToScript
	public Object readPreferences(final String node, final String key, @ScriptParameter(defaultValue = "") final Object defaultValue) {

		final IEclipsePreferences root = InstanceScope.INSTANCE.getNode(node);
		if (root != null) {
			if (defaultValue instanceof Boolean)
				return root.getBoolean(key, (Boolean) defaultValue);

			else if (defaultValue instanceof Integer)
				return root.getInt(key, (Integer) defaultValue);

			else if (defaultValue instanceof Double)
				return root.getDouble(key, (Double) defaultValue);

			else if (defaultValue instanceof Float)
				return root.getFloat(key, (Float) defaultValue);

			else if (defaultValue instanceof Long)
				return root.getLong(key, (Long) defaultValue);

			else if (defaultValue instanceof byte[])
				return root.getByteArray(key, (byte[]) defaultValue);

			else
				return root.get(key, Objects.toString(Objects.requireNonNullElse(defaultValue, "")));
		}

		return null;
	}

	/**
	 * Set a preferences value. Valid types for <i>value</i> are: Boolean, Integer, Double, Float, Long, byte[], and String.
	 *
	 * @param node
	 *            node to write to
	 * @param key
	 *            key to store to
	 * @param value
	 *            value to store
	 * @throws BackingStoreException
	 *             when preferences cannot be persisted
	 */
	@WrapToScript
	public void writePreferences(final String node, final String key, final Object value) throws BackingStoreException {

		final IEclipsePreferences root = InstanceScope.INSTANCE.getNode(node);
		if (root != null) {
			root.put(key, Objects.toString(Objects.requireNonNullElse(value, "")));
			root.flush();

		} else
			throw new BackingStoreException(String.format("Cannot locate preferences for '%s'", node));
	}

	/**
	 * Post an event on the event broker. If <i>delay</i> is set, the event will be posted after the given amount of time asynchronously. In any case this
	 * method returns immediately.
	 *
	 * @param topic
	 *            topic to post
	 * @param data
	 *            topic data
	 * @param delay
	 *            delay to post this even in [ms]
	 */
	@WrapToScript
	public void postEvent(final String topic, final @ScriptParameter(defaultValue = ScriptParameter.NULL) Object data,
			@ScriptParameter(defaultValue = "0") final long delay) {

		if (delay > 0) {
			final Job job = new Job("Post event") {

				@Override
				protected IStatus run(final IProgressMonitor monitor) {
					postEvent(topic, data, 0);
					return Status.OK_STATUS;
				}
			};
			job.setSystem(true);
			job.schedule(delay);

		} else {
			final IEventBroker service = PlatformUI.getWorkbench().getService(IEventBroker.class);
			if (service != null)
				service.post(topic, data);
			else
				throw new RuntimeException("Broker service not available");
		}
	}

	/**
	 * Wait for a given event on the event bus.
	 *
	 * @param topic
	 *            topic to subscribe for
	 * @param timeout
	 *            maximum time to wait for event in [ms]. Use 0 to wait without timeout.
	 * @return posted event or <code>null</code> in case of a timeout
	 * @throws InterruptedException
	 *             when the script thread gets interrupted
	 */
	@WrapToScript
	public Event waitForEvent(final String topic, @ScriptParameter(defaultValue = "0") final long timeout) throws InterruptedException {
		final IEventBroker service = PlatformUI.getWorkbench().getService(IEventBroker.class);
		if (service != null) {
			final WaitingEventHandler handler = new WaitingEventHandler();

			synchronized (handler) {
				service.subscribe(topic, handler);
				handler.wait(timeout);
				service.unsubscribe(handler);

				return handler.fEvent;
			}

		} else
			throw new RuntimeException("Broker service not available");
	}

	/**
	 * Event handler to wait for a given topic.
	 */
	private class WaitingEventHandler implements EventHandler {
		private Event fEvent = null;

		@Override
		public synchronized void handleEvent(final Event event) {
			fEvent = event;
			notify();
		}
	}
}
