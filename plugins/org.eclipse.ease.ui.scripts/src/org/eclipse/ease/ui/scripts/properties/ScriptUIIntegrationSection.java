/*******************************************************************************
 * Copyright (c) 2016 Christian Pontesegger and others.
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
package org.eclipse.ease.ui.scripts.properties;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.databinding.DataBindingContext;
import org.eclipse.core.databinding.observable.value.AbstractObservableValue;
import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.e4.core.contexts.IEclipseContext;
import org.eclipse.e4.ui.model.application.MApplication;
import org.eclipse.e4.ui.model.application.descriptor.basic.MPartDescriptor;
import org.eclipse.e4.ui.model.application.ui.basic.MWindow;
import org.eclipse.e4.ui.workbench.IWorkbench;
import org.eclipse.e4.ui.workbench.modeling.EModelService;
import org.eclipse.e4.ui.workbench.modeling.EPartService;
import org.eclipse.ease.tools.ResourceTools;
import org.eclipse.ease.ui.scripts.Activator;
import org.eclipse.ease.ui.scripts.Messages;
import org.eclipse.ease.ui.scripts.expressions.IExpressionDefinition;
import org.eclipse.ease.ui.scripts.expressions.ui.ExpressionDialog;
import org.eclipse.ease.ui.scripts.repository.IScript;
import org.eclipse.ease.ui.tools.LocationImageDescriptor;
import org.eclipse.jface.databinding.swt.ISWTObservableValue;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.window.Window;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.dialogs.ElementTreeSelectionDialog;
import org.eclipse.ui.forms.widgets.ExpandableComposite;
import org.eclipse.ui.forms.widgets.Section;
import org.eclipse.ui.internal.dialogs.ShowViewDialog;
import org.eclipse.ui.model.BaseWorkbenchContentProvider;
import org.eclipse.ui.model.WorkbenchLabelProvider;
import org.eclipse.ui.views.properties.tabbed.AbstractPropertySection;
import org.eclipse.ui.views.properties.tabbed.TabbedPropertySheetPage;

public class ScriptUIIntegrationSection extends AbstractPropertySection {

	private static final class KeywordObservableValue extends AbstractObservableValue<String> {

		private final IScript fScript;
		private final String fKeyword;

		private KeywordObservableValue(IScript script, String keyword) {
			fScript = script;
			fKeyword = keyword;
		}

		@Override
		public Object getValueType() {
			return String.class;
		}

		@Override
		protected String doGetValue() {
			return fScript.getUserKeywords().get(fKeyword);
		}

		@Override
		protected void doSetValue(String value) {
			fScript.setUserKeyword(fKeyword, value.trim().isEmpty() ? null : value.trim());
		}
	}

	private Text fTxtName;
	private Text fTxtImage;
	private Text fTxtDescription;
	private Text fTxtToolbar;
	private Text fTxtMenu;
	private Text fTxtPopup;
	private Label fLblImagePic;
	private Section fSctnLookFeel;
	private Section fSctnMenusToolbars;

	/**
	 * @wbp.parser.entryPoint
	 */
	@Override
	public void createControls(final Composite parent, TabbedPropertySheetPage aTabbedPropertySheetPage) {
		super.createControls(parent, aTabbedPropertySheetPage);

		parent.setLayout(new GridLayout(1, false));

		fSctnLookFeel = getWidgetFactory().createSection(parent, ExpandableComposite.FOCUS_TITLE | ExpandableComposite.TWISTIE | ExpandableComposite.TITLE_BAR);
		fSctnLookFeel.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		getWidgetFactory().paintBordersFor(fSctnLookFeel);
		fSctnLookFeel.setText(Messages.ScriptUIIntegrationSection_lockAndFeel);
		fSctnLookFeel.setExpanded(true);

		final Composite composite = getWidgetFactory().createComposite(fSctnLookFeel, SWT.NONE);
		getWidgetFactory().paintBordersFor(composite);
		fSctnLookFeel.setClient(composite);
		composite.setLayout(new GridLayout(4, false));

		final Label lblName = getWidgetFactory().createLabel(composite, Messages.ScriptUIIntegrationSection_name, SWT.NONE);
		lblName.setLayoutData(new GridData(SWT.RIGHT, SWT.CENTER, false, false, 1, 1));

		fTxtName = getWidgetFactory().createText(composite, "", SWT.NONE);
		fTxtName.setToolTipText(Messages.ScriptUIIntegrationSection_enterDisplayName);
		fTxtName.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 3, 1));
		// fTxtName.addModifyListener(new KeywordModifyListener("name"));

		final Composite composite_2 = getWidgetFactory().createComposite(composite, SWT.NONE);
		composite_2.setLayoutData(new GridData(SWT.RIGHT, SWT.FILL, false, false, 1, 1));
		getWidgetFactory().paintBordersFor(composite_2);
		final GridLayout gl_composite_2 = new GridLayout(2, false);
		gl_composite_2.horizontalSpacing = 0;
		gl_composite_2.verticalSpacing = 0;
		gl_composite_2.marginWidth = 0;
		composite_2.setLayout(gl_composite_2);

		fLblImagePic = getWidgetFactory().createLabel(composite_2, "", SWT.NONE);
		final GridData gd_lblImagePic = new GridData(SWT.RIGHT, SWT.CENTER, true, false, 1, 1);
		gd_lblImagePic.widthHint = 20;
		gd_lblImagePic.heightHint = 20;
		fLblImagePic.setLayoutData(gd_lblImagePic);

		final Label lblImage = getWidgetFactory().createLabel(composite_2, Messages.ScriptUIIntegrationSection_image, SWT.NONE);
		lblImage.setLayoutData(new GridData(SWT.RIGHT, SWT.CENTER, false, false, 1, 1));

		fTxtImage = getWidgetFactory().createText(composite, "", SWT.NONE);
		fTxtImage.setToolTipText(Messages.ScriptUIIntegrationSection_imageUri);
		fTxtImage.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		fTxtImage.addModifyListener(e -> updateImagePreview());

		final Button btnBrowseWorkspace = getWidgetFactory().createButton(composite, "", SWT.NONE);
		btnBrowseWorkspace.setImage(PlatformUI.getWorkbench().getSharedImages().getImage(org.eclipse.ui.ide.IDE.SharedImages.IMG_OBJ_PROJECT));
		btnBrowseWorkspace.setToolTipText(Messages.ScriptUIIntegrationSection_browseWorkspace);
		btnBrowseWorkspace.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) {

				final ElementTreeSelectionDialog dialog = new ElementTreeSelectionDialog(parent.getShell(), new WorkbenchLabelProvider(),
						new BaseWorkbenchContentProvider() {
							@Override
							public Object[] getChildren(Object element) {

								final List<Object> result = new ArrayList<>();
								for (final Object candidate : super.getChildren(element)) {
									if (candidate instanceof IFile) {
										final String extension = ((IFile) candidate).getFileExtension();
										if (("png".equalsIgnoreCase(extension)) || ("gif".equalsIgnoreCase(extension)) || ("ico".equalsIgnoreCase(extension)))
											result.add(candidate);
									} else if (candidate instanceof IContainer) {
										if (containsImages((IContainer) candidate))
											result.add(candidate);
									}
								}

								return result.toArray(new Object[result.size()]);
							}

							private boolean containsImages(IContainer container) {
								try {
									// parse files
									for (final IResource member : container.members()) {
										final String extension = member.getFileExtension();
										if (("png".equalsIgnoreCase(extension)) || ("gif".equalsIgnoreCase(extension)) || ("ico".equalsIgnoreCase(extension)))
											return true;
									}

									// parse subfolders
									for (final IResource member : container.members()) {
										if ((member instanceof IContainer) && (containsImages((IContainer) member)))
											return true;
									}
								} catch (final CoreException e) {
									// ignore
								}

								return false;
							}

						});
				dialog.setTitle(Messages.ScriptUIIntegrationSection_selectImage);
				dialog.setMessage(Messages.ScriptUIIntegrationSection_selectImageForScript);
				dialog.setInput(ResourcesPlugin.getWorkspace().getRoot());
				if (dialog.open() == Window.OK) {
					final Object result = dialog.getFirstResult();
					if (result instanceof IFile)
						fTxtImage.setText("workspace:/" + ((IFile) result).getFullPath().toPortableString());
				}
			}
		});

		final Button btnBrowseFileSystem = getWidgetFactory().createButton(composite, "", SWT.NONE);
		btnBrowseFileSystem.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) {
				final FileDialog fileDialog = new FileDialog(parent.getShell(), SWT.OPEN);
				fileDialog.setFilterNames(new String[] { Messages.ScriptUIIntegrationSection_images, Messages.ScriptUIIntegrationSection_allFiles });
				fileDialog.setFilterExtensions(new String[] { "*.png;*.gif;*.ico", "*.*" });

				final String location = fileDialog.open();
				if (location != null)
					fTxtImage.setText(new File(location).toURI().toString());
			}
		});
		btnBrowseFileSystem.setImage(PlatformUI.getWorkbench().getSharedImages().getImage(ISharedImages.IMG_OBJ_FOLDER));
		btnBrowseFileSystem.setToolTipText(Messages.ScriptUIIntegrationSection_browseLocal);

		final Label label_2 = getWidgetFactory().createLabel(composite, Messages.ScriptUIIntegrationSection_description, SWT.NONE);
		label_2.setLayoutData(new GridData(SWT.RIGHT, SWT.TOP, false, false, 1, 1));

		fTxtDescription = getWidgetFactory().createText(composite, "", SWT.WRAP | SWT.V_SCROLL | SWT.MULTI);
		fTxtDescription.setToolTipText(Messages.ScriptUIIntegrationSection_descriptionTooltip);
		final GridData gd_text_2 = new GridData(SWT.FILL, SWT.CENTER, true, false, 3, 1);
		gd_text_2.heightHint = 62;
		fTxtDescription.setLayoutData(gd_text_2);

		fSctnMenusToolbars = getWidgetFactory().createSection(parent,
				ExpandableComposite.FOCUS_TITLE | ExpandableComposite.TWISTIE | ExpandableComposite.TITLE_BAR);
		fSctnMenusToolbars.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		getWidgetFactory().paintBordersFor(fSctnMenusToolbars);
		fSctnMenusToolbars.setText(Messages.ScriptUIIntegrationSection_menuAndToolbars);
		fSctnMenusToolbars.setExpanded(true);

		final Composite composite_1 = getWidgetFactory().createComposite(fSctnMenusToolbars, SWT.NONE);
		getWidgetFactory().paintBordersFor(composite_1);
		fSctnMenusToolbars.setClient(composite_1);
		composite_1.setLayout(new GridLayout(4, false));

		final Label lblToolbar = getWidgetFactory().createLabel(composite_1, Messages.ScriptUIIntegrationSection_toolbar, SWT.NONE);
		lblToolbar.setLayoutData(new GridData(SWT.RIGHT, SWT.CENTER, false, false, 1, 1));

		fTxtToolbar = getWidgetFactory().createText(composite_1, "", SWT.NONE);
		fTxtToolbar.setToolTipText(Messages.ScriptUIIntegrationSection_toolbarToolTip);
		fTxtToolbar.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));

		addBrowseButton(composite_1, fTxtToolbar);
		addBuildExpressionButton(composite_1, fTxtToolbar);

		final Label lblMenu = getWidgetFactory().createLabel(composite_1, Messages.ScriptUIIntegrationSection_menu, SWT.NONE);
		lblMenu.setLayoutData(new GridData(SWT.RIGHT, SWT.CENTER, false, false, 1, 1));

		fTxtMenu = getWidgetFactory().createText(composite_1, "", SWT.NONE);
		fTxtMenu.setToolTipText(Messages.ScriptUIIntegrationSection_menuToolTip);
		fTxtMenu.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));

		addBrowseButton(composite_1, fTxtMenu);
		addBuildExpressionButton(composite_1, fTxtMenu);

		final Label lblPopup = getWidgetFactory().createLabel(composite_1, Messages.ScriptUIIntegrationSection_popup, SWT.NONE);
		lblPopup.setLayoutData(new GridData(SWT.RIGHT, SWT.CENTER, false, false, 1, 1));

		fTxtPopup = getWidgetFactory().createText(composite_1, "", SWT.NONE);
		fTxtPopup.setToolTipText(Messages.ScriptUIIntegrationSection_popupToolTip);
		fTxtPopup.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));

		addBrowseButton(composite_1, fTxtPopup);
		addBuildExpressionButton(composite_1, fTxtPopup);
	}

	private void updateImagePreview() {
		Image newImage = null;

		if (!fTxtImage.getText().isEmpty()) {
			String imageLocation = ResourceTools.toAbsoluteLocation(fTxtImage.getText(), getScript().getLocation());
			if (imageLocation == null)
				// fallback: try direct user input
				imageLocation = fTxtImage.getText().trim();

			final ImageDescriptor descriptor = LocationImageDescriptor.createFromLocation(imageLocation);
			if (descriptor != null)
				newImage = descriptor.createImage();
		}

		final Image oldImage = fLblImagePic.getImage();
		fLblImagePic.setImage(newImage);
		if (oldImage != null)
			oldImage.dispose();
	}

	private DataBindingContext fContext = null;

	@Override
	public void refresh() {
		if (fContext != null)
			fContext.dispose();

		fContext = new DataBindingContext();

		final IScript script = getScript();
		final String[] keywords = new String[] { "name", "image", "description", "toolbar", "menu", "popup" };
		final Text[] widgets = new Text[] { fTxtName, fTxtImage, fTxtDescription, fTxtToolbar, fTxtMenu, fTxtPopup };

		for (int index = 0; index < Math.min(keywords.length, widgets.length); index++) {
			// update widget text
			final String value = script.getKeywords().get(keywords[index]);
			widgets[index].setText((value != null) ? value : "");

			// add context binding
			final ISWTObservableValue sourceValue = WidgetProperties.text(SWT.Modify).observeDelayed(300, widgets[index]);
			final KeywordObservableValue targetValue = new KeywordObservableValue(script, keywords[index]);

			fContext.bindValue(targetValue, sourceValue, null, null);
		}

		// set image
		updateImagePreview();

		// refresh sections
		fSctnLookFeel.layout();
		fSctnMenusToolbars.layout();
	}

	private void addBuildExpressionButton(final Composite parent, final Text text) {

		final Button btnBuildExpression = getWidgetFactory().createButton(parent, "", SWT.NONE);
		final ImageDescriptor imageDescriptor = Activator.getImageDescriptor("/icons/eobj16/expression.png");
		btnBuildExpression.setImage(imageDescriptor.createImage());

		btnBuildExpression.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) {
				final ExpressionDialog dialog = new ExpressionDialog(null, Messages.ScriptUIIntegrationSection_expressionDialogTitle, "enabledWhen");
				if (Window.OK == dialog.open()) {
					final IExpressionDefinition expression = dialog.getExpression();
					text.setText(text.getText() + " enabledWhen(" + expression.serialize() + ")");
				}
			}
		});
	}

	private void addBrowseButton(final Composite parent, final Text text) {
		final Button btnBrowse = getWidgetFactory().createButton(parent, "", SWT.NONE);

		final ImageDescriptor imageDescriptor = Activator.getImageDescriptor("/icons/eobj16/select_view.png");
		btnBrowse.setImage(imageDescriptor.createImage());

		btnBrowse.addSelectionListener(new SelectionAdapter() {
			@SuppressWarnings("restriction")
			@Override
			public void widgetSelected(SelectionEvent e) {

				final Shell shell = parent.getShell();
				final IWorkbenchWindow workbenchWindow = PlatformUI.getWorkbench().getActiveWorkbenchWindow();
				final IEclipseContext ctx = workbenchWindow.getService(IEclipseContext.class);
				final EModelService modelService = workbenchWindow.getService(EModelService.class);
				final MWindow window = workbenchWindow.getService(MWindow.class);

				final EPartService partService = workbenchWindow.getService(EPartService.class);

				final IWorkbench workbench = ctx.get(IWorkbench.class);
				final MApplication app = workbench.getApplication();

				final ShowViewDialog dialog = new ShowViewDialog(shell, app, window, modelService, partService, ctx);

				if (dialog.open() == Window.OK) {
					final MPartDescriptor[] descriptors = dialog.getSelection();

					for (final MPartDescriptor descriptor : descriptors) {
						text.setText(descriptor.getElementId());
					}
				}
			}
		});
	}

	protected IScript getScript() {
		final ISelection selection = getSelection();
		if (selection instanceof IStructuredSelection) {
			final Object candidate = ((IStructuredSelection) selection).getFirstElement();
			return (IScript) ((candidate instanceof IScript) ? candidate : null);
		}

		return null;
	}
}
