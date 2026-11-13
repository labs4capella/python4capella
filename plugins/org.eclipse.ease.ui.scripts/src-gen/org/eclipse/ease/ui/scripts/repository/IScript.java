/*******************************************************************************
 * Copyright (c) 2014 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/
/**
 */
package org.eclipse.ease.ui.scripts.repository;

import java.util.Map;

import org.eclipse.core.runtime.IPath;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.service.ScriptType;
import org.eclipse.emf.common.util.EMap;

/**
 * <!-- begin-user-doc --> A representation of the model object ' <em><b>Script</b></em>'. <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScript#getTimestamp <em>Timestamp</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScript#getEntry <em>Entry</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScript#getScriptKeywords <em>Script Keywords</em>}</li>
 * <li>{@link org.eclipse.ease.ui.scripts.repository.IScript#getUserKeywords <em>User Keywords</em>}</li>
 * </ul>
 *
 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScript()
 * @model
 * @generated
 */
public interface IScript extends IRawLocation {
	/**
	 * Returns the value of the '<em><b>Timestamp</b></em>' attribute. The default value is <code>"-1"</code>. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Timestamp</em>' attribute isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>Timestamp</em>' attribute.
	 * @see #setTimestamp(long)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScript_Timestamp()
	 * @model default="-1" required="true"
	 * @generated
	 */
	long getTimestamp();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.ui.scripts.repository.IScript#getTimestamp <em>Timestamp</em>}' attribute. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Timestamp</em>' attribute.
	 * @see #getTimestamp()
	 * @generated
	 */
	void setTimestamp(long value);

	/**
	 * Returns the value of the '<em><b>Entry</b></em>' container reference. It is bidirectional and its opposite is '
	 * {@link org.eclipse.ease.ui.scripts.repository.IScriptLocation#getScripts <em>Scripts</em>}'. <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Entry</em>' reference isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>Entry</em>' container reference.
	 * @see #setEntry(IScriptLocation)
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScript_Entry()
	 * @see org.eclipse.ease.ui.scripts.repository.IScriptLocation#getScripts
	 * @model opposite="scripts" required="true" transient="false"
	 * @generated
	 */
	IScriptLocation getEntry();

	/**
	 * Sets the value of the '{@link org.eclipse.ease.ui.scripts.repository.IScript#getEntry <em>Entry</em>}' container reference. <!-- begin-user-doc --> <!--
	 * end-user-doc -->
	 *
	 * @param value
	 *            the new value of the '<em>Entry</em>' container reference.
	 * @see #getEntry()
	 * @generated
	 */
	void setEntry(IScriptLocation value);

	/**
	 * Returns the value of the '<em><b>Script Keywords</b></em>' map. The key is of type {@link java.lang.String}, and the value is of type
	 * {@link java.lang.String}, <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Script Keywords</em>' map isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>Script Keywords</em>' map.
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScript_ScriptKeywords()
	 * @model mapType="org.eclipse.ease.ui.scripts.repository.KeywordMap<org.eclipse.emf.ecore.EString, org.eclipse.emf.ecore.EString>"
	 * @generated
	 */
	EMap<String, String> getScriptKeywords();

	/**
	 * Returns the value of the '<em><b>User Keywords</b></em>' map. The key is of type {@link java.lang.String}, and the value is of type
	 * {@link java.lang.String}, <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>User Keywords</em>' map isn't clear, there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 *
	 * @return the value of the '<em>User Keywords</em>' map.
	 * @see org.eclipse.ease.ui.scripts.repository.IRepositoryPackage#getScript_UserKeywords()
	 * @model mapType="org.eclipse.ease.ui.scripts.repository.KeywordMap<org.eclipse.emf.ecore.EString, org.eclipse.emf.ecore.EString>"
	 * @generated
	 */
	EMap<String, String> getUserKeywords();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @model
	 * @generated
	 */
	IScriptEngine run();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @model kind="operation"
	 * @generated
	 */
	String getName();

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 *
	 * @model kind="operation" dataType="org.eclipse.ease.ui.scripts.repository.Path"
	 * @generated
	 */
	IPath getPath();

	/**
	 * Get all parameters stored for this script. Merges script parameters and user defined parameters. User parameters have higher relevance.
	 *
	 * @generated NOT
	 */
	Map<String, String> getKeywords();

	/**
	 * Get script type.
	 *
	 * @generated NOT
	 */
	ScriptType getType();

	/**
	 * Verify if this is a remote script. Remote scripts are not stored on a local file system.
	 *
	 * @generated NOT
	 */
	boolean isRemote();

	/**
	 * Run script with startup parameters.
	 *
	 * @param parameters
	 *            startup parameters passed to the script
	 * @return script engine
	 *
	 * @generated NOT
	 */
	IScriptEngine run(String... parameters);

	/**
	 * Run script with named startup parameters.
	 *
	 * @param parameters
	 *            startup parameters passed to the script
	 * @return script engine
	 *
	 * @generated NOT
	 */
	IScriptEngine run(Map<String, Object> parameters);

	/**
	 * Prepare a script engine ready to run. The script is already scheduled for execution. Typically used when the launching application wants to modify engine
	 * parameters or inject variables before the launch.
	 *
	 * @return script engine
	 *
	 * @generated NOT
	 */
	IScriptEngine prepareEngine();

	/**
	 * Parse the script source for keywords and replace cached keywords.
	 *
	 * @generated NOT
	 */
	void refreshScriptKeywords();

	void setUserKeyword(String keyword, String value);
} // IScript
