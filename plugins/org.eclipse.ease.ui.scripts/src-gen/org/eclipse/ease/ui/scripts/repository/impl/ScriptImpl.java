/**
 * Copyright (c) 2013 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 */
package org.eclipse.ease.ui.scripts.repository.impl;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.InvocationTargetException;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.core.runtime.preferences.InstanceScope;
import org.eclipse.e4.core.services.events.IEventBroker;
import org.eclipse.ease.AbstractCodeParser;
import org.eclipse.ease.Activator;
import org.eclipse.ease.ICodeParser;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.Logger;
import org.eclipse.ease.service.EngineDescription;
import org.eclipse.ease.service.IScriptService;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.ease.tools.NullOutputStream;
import org.eclipse.ease.ui.console.ScriptConsole;
import org.eclipse.ease.ui.preferences.IPreferenceConstants;
import org.eclipse.ease.ui.scripts.repository.IRepositoryPackage;
import org.eclipse.ease.ui.scripts.repository.IRepositoryService;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.scripts.repository.IScriptLocation;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.common.util.EMap;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.util.EcoreEMap;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.ecore.util.InternalEList;
import org.eclipse.ui.PlatformUI;
import org.osgi.service.prefs.Preferences;

/**
 * <!-- begin-user-doc --> An implementation of the model object ' <em><b>Script</b></em>'. <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl#getTimestamp <em>Timestamp</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl#getEntry <em>Entry</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl#getScriptKeywords <em>Script Keywords</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.impl.ScriptImpl#getUserKeywords <em>User Keywords</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ScriptImpl extends RawLocationImpl implements IScript {
	/**
	 * The default value of the '{@link #getTimestamp() <em>Timestamp</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getTimestamp()
	 * @generated
	 * @ordered
	 */
	protected static final long TIMESTAMP_EDEFAULT = -1L;

	/**
	 * The cached value of the '{@link #getTimestamp() <em>Timestamp</em>}' attribute. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getTimestamp()
	 * @generated
	 * @ordered
	 */
	protected long timestamp = TIMESTAMP_EDEFAULT;

	/**
	 * The cached value of the '{@link #getScriptKeywords() <em>Script Keywords</em>}' map. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getScriptKeywords()
	 * @generated
	 * @ordered
	 */
	protected EMap<String, String> scriptKeywords;

	/**
	 * The cached value of the '{@link #getUserKeywords() <em>User Keywords</em>}' map. <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @see #getUserKeywords()
	 * @generated
	 * @ordered
	 */
	protected EMap<String, String> userKeywords;

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	protected ScriptImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return IRepositoryPackage.Literals.SCRIPT;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public long getTimestamp() {
		return timestamp;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setTimestamp(long newTimestamp) {
		final long oldTimestamp = timestamp;
		timestamp = newTimestamp;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRepositoryPackage.SCRIPT__TIMESTAMP, oldTimestamp, timestamp));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public IScriptLocation getEntry() {
		if (eContainerFeatureID() != IRepositoryPackage.SCRIPT__ENTRY)
			return null;
		return (IScriptLocation) eInternalContainer();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	public NotificationChain basicSetEntry(IScriptLocation newEntry, NotificationChain msgs) {
		msgs = eBasicSetContainer((InternalEObject) newEntry, IRepositoryPackage.SCRIPT__ENTRY, msgs);
		return msgs;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void setEntry(IScriptLocation newEntry) {
		if ((newEntry != eInternalContainer()) || ((eContainerFeatureID() != IRepositoryPackage.SCRIPT__ENTRY) && (newEntry != null))) {
			if (EcoreUtil.isAncestor(this, newEntry))
				throw new IllegalArgumentException("Recursive containment not allowed for " + toString());
			NotificationChain msgs = null;
			if (eInternalContainer() != null)
				msgs = eBasicRemoveFromContainer(msgs);
			if (newEntry != null)
				msgs = ((InternalEObject) newEntry).eInverseAdd(this, IRepositoryPackage.SCRIPT_LOCATION__SCRIPTS, IScriptLocation.class, msgs);
			msgs = basicSetEntry(newEntry, msgs);
			if (msgs != null)
				msgs.dispatch();
		} else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, IRepositoryPackage.SCRIPT__ENTRY, newEntry, newEntry));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public EMap<String, String> getScriptKeywords() {
		if (scriptKeywords == null) {
			scriptKeywords = new EcoreEMap<>(IRepositoryPackage.Literals.KEYWORD_MAP, KeywordMapImpl.class, this, IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS);
		}

		return scriptKeywords;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public EMap<String, String> getUserKeywords() {
		if (userKeywords == null) {
			userKeywords = new EcoreEMap<>(IRepositoryPackage.Literals.KEYWORD_MAP, KeywordMapImpl.class, this, IRepositoryPackage.SCRIPT__USER_KEYWORDS);
		}
		return userKeywords;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public NotificationChain eInverseAdd(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__ENTRY:
			if (eInternalContainer() != null)
				msgs = eBasicRemoveFromContainer(msgs);
			return basicSetEntry((IScriptLocation) otherEnd, msgs);
		}
		return super.eInverseAdd(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__ENTRY:
			return basicSetEntry(null, msgs);
		case IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS:
			return ((InternalEList<?>) getScriptKeywords()).basicRemove(otherEnd, msgs);
		case IRepositoryPackage.SCRIPT__USER_KEYWORDS:
			return ((InternalEList<?>) getUserKeywords()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public NotificationChain eBasicRemoveFromContainerFeature(NotificationChain msgs) {
		switch (eContainerFeatureID()) {
		case IRepositoryPackage.SCRIPT__ENTRY:
			return eInternalContainer().eInverseRemove(this, IRepositoryPackage.SCRIPT_LOCATION__SCRIPTS, IScriptLocation.class, msgs);
		}
		return super.eBasicRemoveFromContainerFeature(msgs);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__TIMESTAMP:
			return getTimestamp();
		case IRepositoryPackage.SCRIPT__ENTRY:
			return getEntry();
		case IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS:
			if (coreType)
				return getScriptKeywords();
			else
				return getScriptKeywords().map();
		case IRepositoryPackage.SCRIPT__USER_KEYWORDS:
			if (coreType)
				return getUserKeywords();
			else
				return getUserKeywords().map();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__TIMESTAMP:
			setTimestamp((Long) newValue);
			return;
		case IRepositoryPackage.SCRIPT__ENTRY:
			setEntry((IScriptLocation) newValue);
			return;
		case IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS:
			((EStructuralFeature.Setting) getScriptKeywords()).set(newValue);
			return;
		case IRepositoryPackage.SCRIPT__USER_KEYWORDS:
			((EStructuralFeature.Setting) getUserKeywords()).set(newValue);
			return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__TIMESTAMP:
			setTimestamp(TIMESTAMP_EDEFAULT);
			return;
		case IRepositoryPackage.SCRIPT__ENTRY:
			setEntry((IScriptLocation) null);
			return;
		case IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS:
			getScriptKeywords().clear();
			return;
		case IRepositoryPackage.SCRIPT__USER_KEYWORDS:
			getUserKeywords().clear();
			return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
		case IRepositoryPackage.SCRIPT__TIMESTAMP:
			return timestamp != TIMESTAMP_EDEFAULT;
		case IRepositoryPackage.SCRIPT__ENTRY:
			return getEntry() != null;
		case IRepositoryPackage.SCRIPT__SCRIPT_KEYWORDS:
			return (scriptKeywords != null) && !scriptKeywords.isEmpty();
		case IRepositoryPackage.SCRIPT__USER_KEYWORDS:
			return (userKeywords != null) && !userKeywords.isEmpty();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
		switch (operationID) {
		case IRepositoryPackage.SCRIPT___RUN:
			run();
			return null;
		case IRepositoryPackage.SCRIPT___GET_NAME:
			return getName();
		case IRepositoryPackage.SCRIPT___GET_PATH:
			return getPath();
		}
		return super.eInvoke(operationID, arguments);
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy())
			return super.toString();

		final StringBuffer result = new StringBuffer(super.toString());
		result.append(" (timestamp: ");
		result.append(timestamp);
		result.append(')');
		return result.toString();
	}

	@Override
	public Map<String, String> getKeywords() {
		// first merge script parameters
		final Map<String, String> parameters = new HashMap<>(getScriptKeywords().map());

		// now apply user parameters, as they have higher priority
		parameters.putAll(getUserKeywords().map());

		return parameters;
	}

	@Override
	public ScriptType getType() {
		final IScriptService scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);
		ScriptType type = null;

		// script type as provided in metadata
		final String identifier = getKeywords().get("script-type");
		if (identifier != null)
			type = scriptService.getAvailableScriptTypes().get(identifier);

		// script type from file
		if (type == null)
			type = scriptService.getScriptType(getLocation());

		// TODO get content type from raw file data (read file)

		return type;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public String getName() {
		return getPath().lastSegment();
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public IPath getPath() {
		final String name = getKeywords().get("name");
		if (name != null)
			return new Path(name).makeAbsolute();

		String relativePath = getLocation().substring(getEntry().getLocation().length());
		if (isRemote()) {
			try {
				relativePath = URLDecoder.decode(relativePath, "UTF-8");
			} catch (final UnsupportedEncodingException e) {
				// UTF-8 not available, no pretty print available
			}
		}
		return new Path(relativePath).makeAbsolute();
	}

	@Override
	public IScriptEngine prepareEngine() {
		final EngineDescription engineDescription = getEngineDescription();
		if (engineDescription != null) {
			final IScriptEngine engine = engineDescription.createEngine();

			final String ioTarget = getKeywords().get("io");
			if ("system".equalsIgnoreCase(ioTarget)) {
				// nothing to do, scripts default to System.out ...

				// reveal job to the user
				if (engine instanceof Job) {
					((Job) engine).setSystem(false);
					((Job) engine).setName("EASE script: " + getName());
				}

			} else if ("none".equalsIgnoreCase(ioTarget)) {
				// no output at all
				engine.setOutputStream(new NullOutputStream());
				engine.setErrorStream(new NullOutputStream());
				engine.setInputStream(new ByteArrayInputStream(new byte[0]));

				// reveal job to the user
				if (engine instanceof Job) {
					((Job) engine).setSystem(false);
					((Job) engine).setName("EASE script: " + getName());
				}

			} else {
				// any other case, create console
				final ScriptConsole console = ScriptConsole.create(engine.getName() + ": " + getPath(), engine);
				engine.setOutputStream(console.getOutputStream());
				engine.setErrorStream(console.getErrorStream());
				engine.setInputStream(console.getInputStream());
			}

			// check for remote scripts
			if (isRemote()) {
				// verify that remote access is allowed
				final Preferences prefs = InstanceScope.INSTANCE.getNode(Activator.PLUGIN_ID).node(Activator.PREFERENCES_NODE_SCRIPTS);
				final boolean allowRemoteAccess = prefs.getBoolean(IPreferenceConstants.SCRIPTS_ALLOW_REMOTE_ACCESS,
						IPreferenceConstants.DEFAULT_SCRIPTS_ALLOW_REMOTE_ACCESS);

				if (!allowRemoteAccess) {
					engine.getErrorStream().println("Remote script source detected. Access is disabled in preferences.");
					return null;
				}
			}

			Object executionContent = getResource();
			if (executionContent == null)
				executionContent = getInputStream();

			engine.execute(executionContent);

			return engine;

		} else
			Logger.error(org.eclipse.ease.ui.scripts.Activator.PLUGIN_ID, "Could not detect script engine for " + this);

		return null;
	}

	@Override
	public IScriptEngine run() {
		return run(new String[0]);
	}

	@Override
	public IScriptEngine run(final String... parameters) {
		final IScriptEngine engine = prepareEngine();

		if (engine != null) {
			engine.setVariable("argv", parameters);
			engine.schedule();

			final IEventBroker fEventBroker = PlatformUI.getWorkbench().getService(IEventBroker.class);
			if (fEventBroker != null) {
				final HashMap<String, Object> eventData = new HashMap<>();
				eventData.put("script", this);
				fEventBroker.post(IRepositoryService.BROKER_CHANNEL_SCRIPTS_RUN, eventData);
			}
		}

		return engine;
	}

	@Override
	public IScriptEngine run(final Map<String, Object> parameters) {
		final IScriptEngine engine = prepareEngine();

		if (engine != null) {
			for (final Entry<String, Object> entry : parameters.entrySet())
				engine.setVariable(entry.getKey(), entry.getValue());

			engine.schedule();
		}

		return engine;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	private EngineDescription getEngineDescription() {
		final IScriptService scriptService = PlatformUI.getWorkbench().getService(IScriptService.class);

		final String engineIDs = getKeywords().get("script-engine");
		if (engineIDs == null) {
			final ScriptType type = getType();
			if (type != null) {
				return scriptService.getEngine(type.getName());
			} else {
				return null;
			}
		}

		// work through whitelist, prepare blacklist
		final HashSet<String> blacklist = new HashSet<>();
		for (final String id : engineIDs.split(",")) {
			final EngineDescription engineDescription = scriptService.getEngineByID(id.trim());
			if (engineDescription != null)
				return engineDescription;

			if (id.trim().startsWith("!"))
				blacklist.add(id.trim().substring(1));
		}

		// no engine from whitelist found, find potential engine not part of
		// blacklist
		for (final EngineDescription description : scriptService.getEngines(getType().getName())) {
			if (!blacklist.contains(description.getID()))
				return description;
		}

		// no suitable engine found
		return null;
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public boolean isRemote() {
		final Object resource = getResource();
		return (!(resource instanceof IFile)) && (!(resource instanceof File)) && (!getLocation().toString().startsWith("platform:/"));
	}

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @generated NOT
	 */
	@Override
	public void refreshScriptKeywords() {
		final ScriptType type = getType();
		if (type != null) {
			final ICodeParser parser = type.getCodeParser();
			if (parser != null) {
				final String comment = parser.getHeaderComment(getInputStream());
				getScriptKeywords().clear();
				getScriptKeywords().putAll(AbstractCodeParser.extractKeywords(comment));
			}
		}
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see org.eclipse.ease.ui.scripts.repository.IScript#setUserParameter(java.lang.String, java.lang.String)
	 */
	@Override
	public void setUserKeyword(String keyword, String value) {
		final String oldContent = getKeywords().get(keyword);

		if (value == null)
			getUserKeywords().remove(keyword);
		else
			getUserKeywords().put(keyword, value);

		final String newContent = getKeywords().get(keyword);

		if (newContent != oldContent)
			// changed script parameters, push events
			fireKeywordEvent(keyword, newContent, oldContent);
	}

	public void fireKeywordEvent(final String key, final String value, final String oldValue) {
		final Object service = PlatformUI.getWorkbench().getService(IEventBroker.class);
		if (service instanceof IEventBroker) {
			final HashMap<String, Object> eventData = new HashMap<>();
			eventData.put("script", this);
			eventData.put("keyword", key);
			eventData.put("value", value);
			eventData.put("oldValue", oldValue);
			((IEventBroker) service).post(IRepositoryService.BROKER_CHANNEL_SCRIPT_KEYWORDS + key, eventData);
		}
	}

} // ScriptImpl
