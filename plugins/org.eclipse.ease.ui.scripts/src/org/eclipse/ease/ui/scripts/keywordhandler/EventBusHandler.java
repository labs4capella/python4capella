package org.eclipse.ease.ui.scripts.keywordhandler;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.e4.core.services.events.IEventBroker;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ui.PlatformUI;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class EventBusHandler implements EventHandler {

	private static class ScriptEventHandler implements EventHandler {

		private final IScript fScript;

		public ScriptEventHandler(final IScript script) {
			fScript = script;
		}

		@Override
		public void handleEvent(final Event event) {
			IScriptEngine engine = fScript.prepareEngine();
			if (engine != null) {
				engine.setVariable("event", event);
				engine.schedule();
			}
		}
	}

	private final Map<IScript, ScriptEventHandler> fRegisteredHandlers = new HashMap<IScript, ScriptEventHandler>();

	@Override
	public void handleEvent(final Event event) {
		IEventBroker service = PlatformUI.getWorkbench().getService(IEventBroker.class);
		if (service != null) {

			final IScript script = (IScript) event.getProperty("script");
			String topic = (String) event.getProperty("value");

			// eventually remove old handler
			ScriptEventHandler handler = fRegisteredHandlers.get(script);
			if (handler != null)
				service.unsubscribe(handler);

			if (topic != null) {
				handler = new ScriptEventHandler(script);
				service.subscribe(topic, handler);
				fRegisteredHandlers.put(script, handler);
			}
		}
	}
}
