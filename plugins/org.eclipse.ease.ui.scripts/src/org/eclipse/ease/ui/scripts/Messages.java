/*******************************************************************************
 * Copyright (c) 2018 Bachmann electronic GmbH and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Bachmann electronic GmbH - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.ui.scripts;

import org.eclipse.osgi.util.NLS;

/**
 * @author schreibm
 *
 */
public class Messages extends NLS {
	private static final String BUNDLE_NAME = "org.eclipse.ease.ui.scripts.messages"; //$NON-NLS-1$
	public static String AddKeywordDialog_createNew;
	public static String AddKeywordDialog_emptyKey;
	public static String AddKeywordDialog_emptyValue;
	public static String AddKeywordDialog_keyAlreadyExists;
	public static String AddKeywordDialog_keyword;
	public static String AddKeywordDialog_text;
	public static String AddKeywordDialog_value;
	public static String AllKeywordsSection_keyword;
	public static String AllKeywordsSection_value;
	public static String ExpressionComposite_3;
	public static String ExpressionComposite_add;
	public static String ExpressionComposite_delete;
	public static String ExpressionComposite_expression;
	public static String LocationsPage_addURI;
	public static String LocationsPage_default;
	public static String LocationsPage_defaultUpperCase;
	public static String LocationsPage_delete;
	public static String LocationsPage_enterURI;
	public static String LocationsPage_enterURIToAdd;
	public static String LocationsPage_filesystem;
	public static String LocationsPage_location;
	public static String LocationsPage_provideLocation;
	public static String LocationsPage_recursive;
	public static String LocationsPage_selectFolder;
	public static String LocationsPage_workspace;
	public static String ScriptContextMenuEntries_edit;
	public static String ScriptContextMenuEntries_run;
	public static String ScriptDropin_scripts;
	public static String ScriptSelectionDialog_cancel;
	public static String ScriptSelectionDialog_open;
	public static String ScriptSelectionDialog_scriptBrowser;
	public static String ScriptUIIntegrationSection_allFiles;
	public static String ScriptUIIntegrationSection_browseLocal;
	public static String ScriptUIIntegrationSection_browseWorkspace;
	public static String ScriptUIIntegrationSection_description;
	public static String ScriptUIIntegrationSection_descriptionTooltip;
	public static String ScriptUIIntegrationSection_enterDisplayName;
	public static String ScriptUIIntegrationSection_expressionDialogTitle;
	public static String ScriptUIIntegrationSection_image;
	public static String ScriptUIIntegrationSection_images;
	public static String ScriptUIIntegrationSection_imageUri;
	public static String ScriptUIIntegrationSection_lockAndFeel;
	public static String ScriptUIIntegrationSection_menu;
	public static String ScriptUIIntegrationSection_menuAndToolbars;
	public static String ScriptUIIntegrationSection_menuToolTip;
	public static String ScriptUIIntegrationSection_name;
	public static String ScriptUIIntegrationSection_popup;
	public static String ScriptUIIntegrationSection_popupToolTip;
	public static String ScriptUIIntegrationSection_selectImage;
	public static String ScriptUIIntegrationSection_selectImageForScript;
	public static String ScriptUIIntegrationSection_toolbar;
	public static String ScriptUIIntegrationSection_toolbarToolTip;
	public static String SelectScriptStorageDialog_browse;
	public static String SelectScriptStorageDialog_fileSystem;
	public static String SelectScriptStorageDialog_selectFolder;
	public static String SelectScriptStorageDialog_storageDescription;
	public static String SelectScriptStorageDialog_storageLocation;
	public static String SelectScriptStorageDialog_storeInSettings;
	public static String SelectScriptStorageDialog_storeInWorkspace;
	public static String SignaturePreferencePage_allowLocalScript;
	public static String SignaturePreferencePage_allowRemoteScript;
	public static String SignaturePreferencePage_easeSecurity;
	public static String ToggleScriptRecording_couldNotStore;
	public static String ToggleScriptRecording_enterUniqueName;
	public static String ToggleScriptRecording_nameAlreadyInUse;
	public static String ToggleScriptRecording_saveError;
	public static String ToggleScriptRecording_saveScript;
	public static String URIValidator_invalidUri;
	public static String URIValidator_relativeUri;
	static {
		// initialize resource bundle
		NLS.initializeMessages(BUNDLE_NAME, Messages.class);
	}

	private Messages() {
	}
}
