package org.eclipse.ease.ui.scripts.keywordhandler;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.core.commands.Command;
import org.eclipse.core.commands.Parameterization;
import org.eclipse.core.commands.ParameterizedCommand;
import org.eclipse.core.commands.common.NotDefinedException;
import org.eclipse.ease.Logger;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.handler.RunScript;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.jface.bindings.Binding;
import org.eclipse.jface.bindings.keys.KeyBinding;
import org.eclipse.jface.bindings.keys.KeySequence;
import org.eclipse.jface.bindings.keys.ParseException;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.commands.ICommandService;
import org.eclipse.ui.internal.keys.BindingService;
import org.eclipse.ui.keys.IBindingService;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class KeyHandler implements EventHandler {

	private final Map<IScript, Binding> fActiveBindings = new HashMap<IScript, Binding>();

	@Override
	public void handleEvent(final Event event) {
		final IBindingService bindingService = PlatformUI.getWorkbench().getService(IBindingService.class);

		final IScript script = (IScript) event.getProperty("script");
		String value = (String) event.getProperty("value");

		Binding oldBinding = fActiveBindings.get(script);
		if (oldBinding != null) {
			// remove binding
			if (bindingService instanceof BindingService)
				((BindingService) bindingService).removeBinding(fActiveBindings.get(script));
		}

		if (value != null) {
			// add binding
			try {

				final ICommandService commandService = PlatformUI.getWorkbench().getService(ICommandService.class);
				Command runScriptCommand = commandService.getCommand(RunScript.COMMAND_ID);

				Parameterization parameter = new Parameterization(runScriptCommand.getParameters()[0], script.getPath().toString());

				ParameterizedCommand command = new ParameterizedCommand(runScriptCommand, new Parameterization[] { parameter });
				KeySequence instance = KeySequence.getInstance(value);
				KeyBinding binding = new KeyBinding(instance, command, bindingService.getDefaultSchemeId(), "org.eclipse.ui.contexts.window", null, null, null,
						Binding.SYSTEM);

				// currently this is not public API
				if (bindingService instanceof BindingService) {
					((BindingService) bindingService).addBinding(binding);
					fActiveBindings.put(script, binding);
				}

			} catch (ParseException e) {
				Logger.error(Activator.PLUGIN_ID, "Invalid keyboard shortcut for script: " + script.getLocation(), e);

			} catch (NotDefinedException e) {
				// this should not happen
				Logger.error(Activator.PLUGIN_ID, "Could not detect runScript command");
			}
		}
	}
}
