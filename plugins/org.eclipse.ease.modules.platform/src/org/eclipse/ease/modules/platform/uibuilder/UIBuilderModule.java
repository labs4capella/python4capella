/*******************************************************************************
 * Copyright (c) 2019 Christian Pontesegger and others.
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

package org.eclipse.ease.modules.platform.uibuilder;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.ExecutionException;

import org.eclipse.e4.ui.model.application.ui.basic.MBasicFactory;
import org.eclipse.e4.ui.model.application.ui.basic.MPart;
import org.eclipse.e4.ui.workbench.IWorkbench;
import org.eclipse.e4.ui.workbench.modeling.EPartService;
import org.eclipse.e4.ui.workbench.modeling.EPartService.PartState;
import org.eclipse.ease.IReplEngine;
import org.eclipse.ease.IScriptEngine;
import org.eclipse.ease.modules.AbstractScriptModule;
import org.eclipse.ease.modules.IEnvironment;
import org.eclipse.ease.modules.ScriptParameter;
import org.eclipse.ease.modules.WrapToScript;
import org.eclipse.ease.modules.platform.PluginConstants;
import org.eclipse.ease.modules.platform.UIModule;
import org.eclipse.ease.modules.platform.keywords.ScriptedView;
import org.eclipse.ease.tools.RunnableWithResult;
import org.eclipse.ease.ui.tools.LocationImageDescriptor;
import org.eclipse.jface.layout.AbstractColumnLayout;
import org.eclipse.jface.layout.TableColumnLayout;
import org.eclipse.jface.layout.TreeColumnLayout;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.jface.resource.JFaceResources;
import org.eclipse.jface.resource.LocalResourceManager;
import org.eclipse.jface.resource.ResourceManager;
import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.BaseLabelProvider;
import org.eclipse.jface.viewers.CellLabelProvider;
import org.eclipse.jface.viewers.ColumnLabelProvider;
import org.eclipse.jface.viewers.ColumnViewer;
import org.eclipse.jface.viewers.ColumnWeightData;
import org.eclipse.jface.viewers.ComboViewer;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.ListViewer;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.StructuredSelection;
import org.eclipse.jface.viewers.StructuredViewer;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.jface.viewers.TableViewerColumn;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.jface.viewers.TreeViewerColumn;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.jface.viewers.ViewerColumn;
import org.eclipse.jface.viewers.ViewerComparator;
import org.eclipse.swt.SWT;
import org.eclipse.swt.custom.ScrolledComposite;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Group;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.ProgressBar;
import org.eclipse.swt.widgets.TableColumn;
import org.eclipse.swt.widgets.Text;
import org.eclipse.swt.widgets.TreeColumn;
import org.eclipse.ui.IWorkbenchListener;
import org.eclipse.ui.PlatformUI;

/**
 * Create UI elements by adding SWT controls via script commands to a dynamic {@link GridLayout}. Each element allows to provide layout data, which accepts a
 * fairly simple syntax: &lt;coordinates&gt; &lt;horizontal align&gt; &lt;vertical align&gt;
 *
 * <dl>
 * <dt>coordinates</dt>
 * <dd>Provides X/Y coordinates for elements in the grid where 1/1 denotes the upper left corner. 2/1 would create the element in the second column of the first
 * row. Coordinates may also provide rowSpan/columnSpan information: 1-3/2-3 would create the element spanning columns 1 to 3 in rows 2 to 3.
 * {@module #showGrid(boolean)} adds visual indications to help layouting.</dd>
 *
 * <dt>horizontal alignment</dt>
 * <dd>
 * <ul>
 * <li>&lt; ... align left</li>
 * <li>x ... align center</li>
 * <li>&gt; ... align right</li>
 * <li>o ... fill</li>
 * <li>o! ... grab horizontal space (! may be added to any alignment)</li>
 * </ul>
 * </dd>
 *
 * <dt>vertical alignment</dt>
 * <dd>
 * <ul>
 * <li>^ ... align top</li>
 * <li>x ... align middle</li>
 * <li>v ... align bottom</li>
 * <li>o ... fill</li>
 * <li>o! ... grab vertical space (! may be added to any alignment)</li>
 * </ul>
 * </dd>
 * </dl>
 *
 * <p>
 * Most methods of this module deal with SWT components. To access them the code needs to be run in the UI thread. See
 * {@module org.eclipse.ease.modules.platform.ui#executeUI(Object)} for more information.
 * </p>
 *
 * <p>
 * Whenever callback code is registered the executing engine is automatically set to be kept alive after script execution. This is required as callback
 * execution needs a script engine.
 * </p>
 */
public class UIBuilderModule extends AbstractScriptModule {

	private static int fCounter = 1;

	public static String getDynamicViewId() {
		return "org.eclipse.ease.view.dynamic." + fCounter++;
	}

	/** Holds viewModel, renderer, and further elements for created composites. */
	private final List<UICompositor> fUICompositors = new ArrayList<>();

	/** Holds the current event during event callbacks. */
	private volatile Object fUiEvent = null;

	/** Holds the current element during label/content provider callbacks. */
	private Object fProviderElement = null;

	private ScriptableDialog fScriptableDialog;

	private final LifecycleManager fLifecycleManager = new LifecycleManager();

	@Override
	public void initialize(IScriptEngine engine, IEnvironment environment) {
		super.initialize(engine, environment);

		final Object composite = getScriptEngine().getVariable(ScriptedView.SCRIPT_VARIABLE_COMPOSITE);
		if (composite instanceof Composite)
			pushComposite((Composite) composite);
	}

	/**
	 * Create a view with scripted content. Automatically sets the active composite for further commands. This view will not be stored when the workbench gets
	 * closed.
	 *
	 * @param title
	 *            view title
	 * @param iconUri
	 *            URI of view icon to be used
	 * @param relativeTo
	 *            name/ID of an existing view to put this view relative to
	 * @param position
	 *            one of
	 *            <ul>
	 *            <li>x,o ... same stack</li>
	 *            <li>v ... below target view</li>
	 *            <li>^ ... above target view</li>
	 *            <li>&lt; ... left of target view</li>
	 *            <li>&gt; ... right of target view</li>
	 *            </ul>
	 * @return view instance
	 * @throws Throwable
	 *             when the view cannot be created
	 */
	@WrapToScript
	public MPart createView(@ScriptParameter(defaultValue = "Dynamic View") String title, @ScriptParameter(defaultValue = ScriptParameter.NULL) String iconUri,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) String relativeTo, @ScriptParameter(defaultValue = "x") String position) throws Throwable {

		final MPart part = createDynamicPart(title, iconUri);
		fLifecycleManager.add(part);

		if (relativeTo != null)
			UIModule.moveView(part.getElementId(), relativeTo, position);

		fUICompositors.clear();
		pushComposite((Composite) part.getWidget());

		return part;
	}

	private MPart createDynamicPart(String title, String iconUri) throws Throwable {
		final RunnableWithResult<MPart> runnable = new RunnableWithResult<>() {

			@Override
			public MPart runWithTry() throws Throwable {
				final EPartService partService = PlatformUI.getWorkbench().getService(EPartService.class);

				// create part
				final MPart part = MBasicFactory.INSTANCE.createPart();
				part.setLabel(title);
				if (iconUri != null)
					part.setIconURI(iconUri);
				else
					part.setIconURI("platform:/plugin/" + PluginConstants.PLUGIN_ID + "/icons/eview16/scripted_view.png");

				part.setElementId(getDynamicViewId());
				part.setCloseable(true);
				part.getPersistedState().put(IWorkbench.PERSIST_STATE, Boolean.FALSE.toString());

				partService.showPart(part, PartState.VISIBLE);

				// make sure to close this window before we terminate. Eclipse would store it in its layout actually destroying all layout data.
				PlatformUI.getWorkbench().addWorkbenchListener(new IWorkbenchListener() {

					@Override
					public boolean preShutdown(org.eclipse.ui.IWorkbench workbench, boolean forced) {
						partService.hidePart(part, true);
						return true;
					}

					@Override
					public void postShutdown(org.eclipse.ui.IWorkbench workbench) {
					}
				});

				final Object widget = part.getWidget();
				if (widget instanceof Composite)
					((Composite) widget).addDisposeListener(l -> fLifecycleManager.remove(part));

				return part;
			}
		};

		Display.getDefault().syncExec(runnable);

		return runnable.getResultOrThrow();
	}

	/**
	 * Create a dialog with scripted content. To populate the dialog we need to provide a callback method that creates UI elements for the dialog area. After
	 * the setup the dialog can be shown by calling dialog.open(). To retrieve input data after the dialog got closed call dialog.getData(uiComponent).
	 *
	 * @param layoutCode
	 *            script code to be called when dialog window is created
	 * @param title
	 *            dialog title text displayed in header area
	 * @param message
	 *            dialog info message displayed in header area
	 * @return dialog instance
	 * @throws Throwable
	 *             when dialog cannot be created.
	 */
	@WrapToScript
	public ScriptableDialog createDialog(Object layoutCode, @ScriptParameter(defaultValue = "Dialog") String title,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) String message) throws Throwable {
		return runInUIThread(new RunnableWithResult<ScriptableDialog>() {
			@Override
			public ScriptableDialog runWithTry() throws Throwable {
				final ScriptableDialog dialog = new ScriptableDialog(Display.getDefault().getActiveShell(), new DialogRunnable() {

					@Override
					public void run() {
						fLifecycleManager.add(getDialog());

						fUICompositors.clear();
						pushComposite(getComposite());

						fScriptableDialog = getDialog();
						try {
							getScriptEngine().inject(layoutCode, false);

						} catch (final ExecutionException e) {
							// nothing to do
						} finally {
							fScriptableDialog = null;

							getComposite().addDisposeListener(l -> fLifecycleManager.remove(getDialog()));
						}
					}
				});

				dialog.setTitleText(title);
				dialog.setMessageText(message);

				return dialog;
			}
		});
	}

	/**
	 * Sets the active composite for further commands. The composite layout will be set to {@link GridLayout} if not already done. When creating multiple
	 * composites you may return to a previous one using {@module #popComposite()}.
	 *
	 * @param composite
	 *            composite to be used
	 */
	@WrapToScript
	public void pushComposite(Composite composite) {
		Display.getDefault().syncExec(() -> {
			if ((composite.getLayout() == null) || !(composite.getLayout() instanceof GridLayout)) {
				final GridLayout gridLayout = new GridLayout();
				gridLayout.numColumns = 1;

				composite.setLayout(gridLayout);
			}
		});

		fUICompositors.add(0, new UICompositor(composite));
	}

	/**
	 * Remove the current composite from the composite stack. For the topmost composite this method does nothing.
	 *
	 * @return current composite after the removal
	 */
	@WrapToScript
	public Composite popComposite() {
		if (fUICompositors.size() > 1)
			fUICompositors.remove(0);

		return getComposite();
	}

	/**
	 * Get the active composite.
	 *
	 * @return active composite or <code>null</code>
	 */
	@WrapToScript
	public Composite getComposite() {
		return getUICompositor().getComposite();
	}

	/**
	 * Set the minimum column count. If the current column count is already equal or higher then this method does nothing.
	 *
	 * @param columns
	 *            minimum amount of columns
	 */
	@WrapToScript
	public void setColumnCount(int columns) {
		Display.getDefault().syncExec(() -> {
			getUICompositor().fViewModel.setColumnCount(columns);
			getUICompositor().update();
		});
	}

	/**
	 * Create a label.
	 *
	 * @param labelOrImage
	 *            label text or image to be used
	 * @param layout
	 *            layout data (see module documentation)
	 * @return label instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Label createLabel(Object labelOrImage, @ScriptParameter(defaultValue = "<") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Label>() {
			@Override
			public Label runWithTry() throws Throwable {
				final Label swtLabel = new Label(getUICompositor().getComposite(), SWT.NONE);
				if (labelOrImage instanceof Image)
					swtLabel.setImage((Image) labelOrImage);
				else
					swtLabel.setText(labelOrImage.toString());

				getUICompositor().insertElement(swtLabel, new Location(layout));

				return swtLabel;
			}
		});
	}

	/**
	 * Create a new composite. To activate the composite (and create elements inside) use {@module #pushComposite(Composite)}.
	 *
	 * @param layout
	 *            layout data (see module documentation)
	 * @return composite instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Composite createComposite(@ScriptParameter(defaultValue = "o! o!") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Composite>() {
			@Override
			public Composite runWithTry() throws Throwable {
				final Composite composite = new Composite(getUICompositor().getComposite(), SWT.NONE);
				getUICompositor().insertElement(composite, new Location(layout));

				return composite;
			}
		});
	}

	/**
	 * Create a new composite inside of a scrolled composite. Scrollbars will be added dynamically in case the content does not fit into the composite area. To
	 * activate the composite (and create elements inside) use {@module #pushComposite(Composite)}.
	 *
	 * @param layout
	 *            layout data (see module documentation)
	 * @return composite instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Composite createScrolledComposite(@ScriptParameter(defaultValue = "o! o!") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Composite>() {
			@Override
			public Composite runWithTry() throws Throwable {
				final ScrolledComposite scrolledComposite = new ScrolledComposite(getUICompositor().getComposite(), SWT.BORDER | SWT.H_SCROLL | SWT.V_SCROLL);
				scrolledComposite.setExpandHorizontal(true);
				scrolledComposite.setExpandVertical(true);

				final Composite composite = new Composite(scrolledComposite, SWT.NONE);
				scrolledComposite.setContent(composite);

				getUICompositor().insertElement(scrolledComposite, new Location(layout));

				return composite;
			}
		});
	}

	/**
	 * Create a separator.
	 *
	 * @param horizontal
	 *            <code>true</code> for horizontal, <code>false</code> for vertical
	 * @param layout
	 *            layout data (see module documentation)
	 * @return separator instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Label createSeparator(@ScriptParameter(defaultValue = "true") boolean horizontal, @ScriptParameter(defaultValue = "o") String layout)
			throws Throwable {
		return runInUIThread(new RunnableWithResult<Label>() {
			@Override
			public Label runWithTry() throws Throwable {
				final Label swtLabel = new Label(getUICompositor().getComposite(), SWT.SEPARATOR | (horizontal ? SWT.HORIZONTAL : SWT.VERTICAL));

				getUICompositor().insertElement(swtLabel, new Location(layout));

				return swtLabel;
			}
		});
	}

	/**
	 * Create a progress bar.
	 *
	 * @param value
	 *            start value of the progress bar
	 * @param maximum
	 *            maximum value of the progress bar
	 * @param layout
	 *            layout data (see module documentation)
	 * @return progress bar instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public ProgressBar createProgressBar(@ScriptParameter(defaultValue = "0") int value, @ScriptParameter(defaultValue = "100") int maximum,
			@ScriptParameter(defaultValue = "o") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<ProgressBar>() {
			@Override
			public ProgressBar runWithTry() throws Throwable {
				final ProgressBar progressBar = new ProgressBar(getUICompositor().getComposite(), SWT.NONE);
				progressBar.setMaximum(maximum);
				progressBar.setSelection(value);

				getUICompositor().insertElement(progressBar, new Location(layout));

				return progressBar;
			}
		});
	}

	/**
	 * Create a group composite. Further create commands will target this composite. To revert back to the parent use {@module #popComposite()}.
	 *
	 * @param label
	 *            group label
	 * @param layout
	 *            layout data (see module documentation)
	 * @return group instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Group createGroup(@ScriptParameter(defaultValue = ScriptParameter.NULL) String label, @ScriptParameter(defaultValue = "o o") String layout)
			throws Throwable {
		return runInUIThread(new RunnableWithResult<Group>() {
			@Override
			public Group runWithTry() throws Throwable {
				final Group group = new Group(getUICompositor().getComposite(), SWT.NONE);
				if (label != null)
					group.setText(label);

				getUICompositor().insertElement(group, new Location(layout));
				pushComposite(group);

				return group;
			}
		});
	}

	/**
	 * Create a single line text input.
	 *
	 * @param layout
	 *            layout data (see module documentation)
	 * @return text instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Text createText(@ScriptParameter(defaultValue = "o!") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Text>() {
			@Override
			public Text runWithTry() throws Throwable {
				final Text text = new Text(getUICompositor().getComposite(), SWT.BORDER);

				getUICompositor().insertElement(text, new Location(layout));

				return text;
			}
		});
	}

	/**
	 * Create a multi line text input.
	 *
	 * @param layout
	 *            layout data (see module documentation)
	 * @return text instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Text createTextBox(@ScriptParameter(defaultValue = "o!") String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Text>() {
			@Override
			public Text runWithTry() throws Throwable {
				final Text text = new Text(getUICompositor().getComposite(), SWT.BORDER | SWT.MULTI | SWT.WRAP);

				getUICompositor().insertElement(text, new Location(layout));

				return text;
			}
		});
	}

	/**
	 * Create an image instance. Images will not directly be displayed. Instead they can be used when creating controls or views. When an image is created, its
	 * lifecycle gets bound to the current composite. When the composite gets disposed also all images bound to that composite get disposed.
	 *
	 * @param location
	 *            location to create image from
	 * @return image instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Image createImage(String location) throws Throwable {
		return runInUIThread(new RunnableWithResult<Image>() {
			@Override
			public Image runWithTry() throws Throwable {
				return getUICompositor().getResourceManager().createImageWithDefault(LocationImageDescriptor.createFromLocation(location));
			}
		});
	}

	/**
	 * Get the current element for the label/content provider. Only valid while a provider callback is evaluated.
	 *
	 * @return the element for the current provider evaluation or <code>null</code>
	 */
	@WrapToScript
	public Object getProviderElement() {
		return fProviderElement;
	}

	/**
	 * Create a label provider to be used for combos, lists or tables. While the callback is executed you may call {@module #getProviderElement()} to get the
	 * current element.
	 *
	 * @param textCallback
	 *            script callback to return the text for the element
	 * @param imageCallback
	 *            script callback to return an {@link Image} or {@link ImageDescriptor} for the element
	 * @return label provider instance
	 */
	@WrapToScript
	public ColumnLabelProvider createLabelProvider(@ScriptParameter(defaultValue = ScriptParameter.NULL) Object textCallback,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object imageCallback) {

		if ((textCallback != null) || (imageCallback != null))
			keepScriptEngineAlive();

		return new GenericLabelProvider() {
			@Override
			public String getText(Object element) {
				if (textCallback != null) {
					try {
						fProviderElement = element;
						final Object result = getScriptEngine().inject(textCallback, false);

						if (result != null)
							return result.toString();

					} catch (final Throwable e) {
						// silently swallow
					} finally {
						fProviderElement = null;
					}
				}

				return super.getText(element);
			}

			@Override
			public Image getImage(Object element) {
				if (imageCallback != null) {
					try {
						fProviderElement = element;
						final Object result = getScriptEngine().inject(imageCallback, false);

						if (result instanceof Image)
							return (Image) result;

						if (result instanceof ImageDescriptor)
							return getUICompositor().getResourceManager().createImage((ImageDescriptor) result);

					} catch (final Throwable e) {
						// silently swallow
					} finally {
						fProviderElement = null;
					}
				}

				return super.getImage(element);
			}
		};
	}

	/**
	 * Create a table viewer. To enhance look and feel create columns using {@module #createViewerColumn(ColumnViewer, String, BaseLabelProvider, int)}.
	 *
	 * @param elements
	 *            table elements to display
	 * @param callback
	 *            callback when selection changes. Use {module #getUiEvent()} to access the {@link SelectionChangedEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return table viewer instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public TableViewer createTableViewer(Object[] elements, @ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback,
			@ScriptParameter(defaultValue = "o! o!") String layout) throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<TableViewer>() {
			@Override
			public TableViewer runWithTry() throws Throwable {

				final Composite composite = new Composite(getUICompositor().getComposite(), SWT.NONE);
				final TableColumnLayout tcl_composite = new TableColumnLayout();
				composite.setLayout(tcl_composite);

				final TableViewer tableViewer = new TableViewer(composite, SWT.BORDER | SWT.FULL_SELECTION);
				tableViewer.getTable().setLinesVisible(true);
				tableViewer.getTable().setHeaderVisible(false);

				tableViewer.setContentProvider(ArrayContentProvider.getInstance());
				tableViewer.setInput(elements);

				if (callback != null)
					tableViewer.addSelectionChangedListener(event -> runEventCallback(event, callback));

				getUICompositor().insertElement(composite, new Location(layout));

				if (fScriptableDialog != null)
					fScriptableDialog.registerViewer(tableViewer.getControl(), tableViewer);

				return tableViewer;
			}
		});
	}

	/**
	 * Create a tree viewer. To enhance look and feel create columns using {@module #createViewerColumn(ColumnViewer, String, BaseLabelProvider, int)}.
	 *
	 * @param rootElements
	 *            tree root elements to display
	 * @param getChildrenCallback
	 *            script callback to return element children. During the callback {@link #getProviderElement()} can be used to retrieve the current element.
	 * @param callback
	 *            callback when selection changes. Use {module #getUiEvent()} to access the {@link SelectionChangedEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return tree viewer instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public TreeViewer createTreeViewer(Object[] rootElements, Object getChildrenCallback, @ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback,
			@ScriptParameter(defaultValue = "o! o!") String layout) throws Throwable {

		if ((getChildrenCallback != null) || (callback != null))
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<TreeViewer>() {
			@Override
			public TreeViewer runWithTry() throws Throwable {

				final Composite composite = new Composite(getUICompositor().getComposite(), SWT.NONE);
				final TreeColumnLayout tcl_composite = new TreeColumnLayout();
				composite.setLayout(tcl_composite);

				final TreeViewer treeViewer = new TreeViewer(composite, SWT.BORDER);
				treeViewer.getTree().setLinesVisible(false);
				treeViewer.getTree().setHeaderVisible(false);

				treeViewer.setContentProvider(new ITreeContentProvider() {

					@Override
					public boolean hasChildren(Object element) {
						final Object[] children = getChildren(element);
						return (children != null) && (children.length > 0);
					}

					@Override
					public Object getParent(Object element) {
						return null;
					}

					@Override
					public Object[] getElements(Object inputElement) {
						return rootElements;
					}

					@Override
					public Object[] getChildren(Object parentElement) {
						if (getChildrenCallback != null) {
							try {
								fProviderElement = parentElement;
								final Object result = getScriptEngine().inject(getChildrenCallback, false);

								if (result instanceof Object[])
									return (Object[]) result;

								if (result instanceof Object)
									return new Object[] { result };

							} catch (final Exception e) {
								// silently swallow
							} finally {
								fProviderElement = null;
							}
						}

						return new Object[0];
					}
				});
				treeViewer.setInput(rootElements);

				if (callback != null)
					treeViewer.addSelectionChangedListener(event -> runEventCallback(event, callback));

				getUICompositor().insertElement(composite, new Location(layout));

				if (fScriptableDialog != null)
					fScriptableDialog.registerViewer(treeViewer.getControl(), treeViewer);

				return treeViewer;
			}
		});
	}

	/**
	 * Create a column for a table viewer. The viewer will automatically use a weighted layout for columns, distributing the horizontal space on all columns
	 * depending on their weight.
	 *
	 * @param viewer
	 *            viewer to create column for
	 * @param title
	 *            column title
	 * @param labelProvider
	 *            label provider for column
	 * @param weight
	 *            column weight
	 * @return table viewer column
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public ViewerColumn createViewerColumn(ColumnViewer viewer, String title,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) BaseLabelProvider labelProvider, @ScriptParameter(defaultValue = "1") int weight)
			throws Throwable {

		return runInUIThread(new RunnableWithResult<ViewerColumn>() {
			@Override
			public ViewerColumn runWithTry() throws Throwable {

				ViewerColumn column;
				final AbstractColumnLayout tcl_composite = (AbstractColumnLayout) viewer.getControl().getParent().getLayout();
				if (viewer instanceof TableViewer) {
					column = new TableViewerColumn((TableViewer) viewer, SWT.NONE);
					final TableColumn tblclmnNewColumn = ((TableViewerColumn) column).getColumn();

					tcl_composite.setColumnData(tblclmnNewColumn, new ColumnWeightData(weight, ColumnWeightData.MINIMUM_WIDTH, true));
					if (title != null) {
						tblclmnNewColumn.setText(title);
						((TableViewer) viewer).getTable().setHeaderVisible(true);
					}

				} else if (viewer instanceof TreeViewer) {
					column = new TreeViewerColumn((TreeViewer) viewer, SWT.NONE);
					final TreeColumn trclmnNewColumn = ((TreeViewerColumn) column).getColumn();

					tcl_composite.setColumnData(trclmnNewColumn, new ColumnWeightData(weight, ColumnWeightData.MINIMUM_WIDTH, true));
					if (title != null) {
						trclmnNewColumn.setText(title);
						((TreeViewer) viewer).getTree().setHeaderVisible(true);
					}

				} else
					throw new IllegalArgumentException("viewer is neither a TableViewer nor a TreeViewer");

				// add label provider
				if (labelProvider instanceof CellLabelProvider)
					column.setLabelProvider((CellLabelProvider) labelProvider);

				else if (labelProvider instanceof LabelProvider) {
					column.setLabelProvider(new GenericLabelProvider() {
						@Override
						public String getText(Object element) {
							return ((LabelProvider) labelProvider).getText(element);
						}

						@Override
						public Image getImage(Object element) {
							return ((LabelProvider) labelProvider).getImage(element);
						}
					});

				} else
					column.setLabelProvider(new GenericLabelProvider());

				// layout to recalculate column size
				viewer.getControl().getParent().layout(true);
				getUICompositor().update();

				viewer.refresh(true);

				return column;
			}
		});
	}

	/**
	 * Create a push button.
	 *
	 * @param labelOrImage
	 *            button text or image to be used
	 * @param callback
	 *            callback code when button gets pressed. Use {module #getUiEvent()} to access the {@link SelectionEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return button instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Button createButton(Object labelOrImage, Object callback, @ScriptParameter(defaultValue = ScriptParameter.NULL) String layout) throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<Button>() {
			@Override
			public Button runWithTry() throws Throwable {
				final Button button = new Button(getUICompositor().getComposite(), SWT.NONE);
				if (labelOrImage instanceof Image)
					button.setImage((Image) labelOrImage);
				else
					button.setText(labelOrImage.toString());

				button.addSelectionListener(new SelectionAdapter() {

					@Override
					public void widgetSelected(SelectionEvent e) {
						runEventCallback(e, callback);
					}
				});

				getUICompositor().insertElement(button, new Location(layout));

				return button;
			}
		});
	}

	/**
	 * Create a checkbox.
	 *
	 * @param label
	 *            checkbox text
	 * @param selected
	 *            initial state of the checkbox
	 * @param callback
	 *            callback code when the checkbox gets ticked/unticked. Use {module #getUiEvent()} to access the {@link SelectionEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return checkbox instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Button createCheckBox(String label, @ScriptParameter(defaultValue = "true") boolean selected,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback, @ScriptParameter(defaultValue = ScriptParameter.NULL) String layout)
			throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<Button>() {
			@Override
			public Button runWithTry() throws Throwable {
				final Button button = new Button(getUICompositor().getComposite(), SWT.CHECK);
				button.setText(label);
				button.setSelection(selected);

				if (callback != null) {
					button.addSelectionListener(new SelectionAdapter() {

						@Override
						public void widgetSelected(SelectionEvent e) {
							runEventCallback(e, callback);
						}
					});
				}

				getUICompositor().insertElement(button, new Location(layout));

				return button;
			}
		});
	}

	/**
	 * Create a radio button.
	 *
	 * @param label
	 *            radio text
	 * @param selected
	 *            initial state of the checkbox
	 * @param callback
	 *            callback code when the radio button gets ticked/unticked. Use {module #getUiEvent()} to access the {@link SelectionEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return radio button instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public Button createRadioButton(String label, @ScriptParameter(defaultValue = "true") boolean selected,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback, @ScriptParameter(defaultValue = ScriptParameter.NULL) String layout)
			throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<Button>() {
			@Override
			public Button runWithTry() throws Throwable {
				final Button button = new Button(getUICompositor().getComposite(), SWT.RADIO);
				button.setText(label);
				button.setSelection(selected);

				if (callback != null) {
					button.addSelectionListener(new SelectionAdapter() {

						@Override
						public void widgetSelected(SelectionEvent e) {
							if (button.getSelection())
								runEventCallback(e, callback);
						}
					});
				}

				getUICompositor().insertElement(button, new Location(layout));

				return button;
			}
		});
	}

	/**
	 * Create a combo box. The first element will automatically be selected.
	 *
	 * @param elements
	 *            combo elements to display.
	 * @param editable
	 *            set to <code>true</code> to allow users to enter custom entries
	 * @param callback
	 *            callback code when selection changes. Use {module #getUiEvent()} to access the {@link SelectionChangedEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return combo viewer instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public ComboViewer createComboViewer(Object[] elements, @ScriptParameter(defaultValue = "false") boolean editable,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback, @ScriptParameter(defaultValue = ScriptParameter.NULL) String layout)
			throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<ComboViewer>() {
			@Override
			public ComboViewer runWithTry() throws Throwable {
				final ComboViewer comboViewer = new ComboViewer(getUICompositor().getComposite(), SWT.BORDER | (editable ? 0 : SWT.READ_ONLY));
				comboViewer.setLabelProvider(new GenericLabelProvider());
				comboViewer.setContentProvider(ArrayContentProvider.getInstance());
				comboViewer.setInput(elements);

				comboViewer.setSelection(new StructuredSelection(elements[0]));

				if (callback != null)
					comboViewer.addSelectionChangedListener(event -> runEventCallback(event, callback));

				getUICompositor().insertElement(comboViewer.getControl(), new Location(layout));

				if (fScriptableDialog != null)
					fScriptableDialog.registerViewer(comboViewer.getControl(), comboViewer);

				return comboViewer;
			}
		});
	}

	/**
	 * Create a comparator (sorter) to be used for combos, lists or tables. The comparator is automatically attached to the provided viewer.
	 *
	 * @param viewer
	 *            viewer to create the comparator for
	 * @param categoryCallback
	 *            script callback to return the category type for an element. The element can be retrieved with {@module #getProviderElement()}. The return type
	 *            is expected to be an integer. Lower numbers get displayed first.
	 * @param compareCallback
	 *            script callback to return the comparison result of 2 elements. The elements are stored as array in {@module #getProviderElement()}. The return
	 *            type is expected to be an integer. If &lt;0 then the first element gets listed first, &gt;0 lists the 2nd element first
	 * @return the viewer comparator
	 * @throws Throwable
	 *             when comparator cannot be set
	 */
	@WrapToScript
	public ViewerComparator createComparator(StructuredViewer viewer, @ScriptParameter(defaultValue = ScriptParameter.NULL) Object categoryCallback,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) Object compareCallback) throws Throwable {

		if ((categoryCallback != null) || (compareCallback != null))
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<ViewerComparator>() {

			@Override
			public ViewerComparator runWithTry() throws Throwable {

				viewer.setComparator(new ViewerComparator() {
					@Override
					public int category(Object element) {

						if (categoryCallback != null) {
							try {
								fProviderElement = element;
								final Object result = getScriptEngine().inject(categoryCallback, false);

								if (result != null)
									return Integer.parseInt(result.toString());

							} catch (final Throwable e) {
								// silently swallow
							} finally {
								fProviderElement = null;
							}
						}

						return super.category(element);
					}

					@Override
					public int compare(Viewer viewer, Object e1, Object e2) {
						if (compareCallback != null) {
							try {
								fProviderElement = new Object[] { e1, e2 };

								final Object result = getScriptEngine().inject(compareCallback, false);

								if (result != null)
									return Integer.parseInt(result.toString());

							} catch (final Throwable e) {
								// silently swallow
							} finally {
								fProviderElement = null;
							}
						}

						return super.compare(viewer, e1, e2);
					}
				});

				return viewer.getComparator();
			}
		});
	}

	/**
	 * Create a list viewer.
	 *
	 * @param elements
	 *            list elements to display
	 * @param callback
	 *            callback when selection changes. Use {module #getUiEvent()} to access the {@link SelectionChangedEvent}.
	 * @param layout
	 *            layout data (see module documentation)
	 * @return list viewer instance
	 * @throws Throwable
	 *             on any SWT error
	 */
	@WrapToScript
	public ListViewer createListViewer(Object[] elements, @ScriptParameter(defaultValue = ScriptParameter.NULL) Object callback,
			@ScriptParameter(defaultValue = ScriptParameter.NULL) String layout) throws Throwable {

		if (callback != null)
			keepScriptEngineAlive();

		return runInUIThread(new RunnableWithResult<ListViewer>() {
			@Override
			public ListViewer runWithTry() throws Throwable {
				final ListViewer listViewer = new ListViewer(getUICompositor().getComposite());
				listViewer.setLabelProvider(new GenericLabelProvider());
				listViewer.setContentProvider(ArrayContentProvider.getInstance());
				listViewer.setInput(elements);

				if (callback != null)
					listViewer.addSelectionChangedListener(event -> runEventCallback(event, callback));

				getUICompositor().insertElement(listViewer.getControl(), new Location(layout));

				if (fScriptableDialog != null)
					fScriptableDialog.registerViewer(listViewer.getControl(), listViewer);

				return listViewer;
			}
		});
	}

	/**
	 * Add a generic control.
	 *
	 * @param control
	 *            control to add
	 * @param layout
	 *            layout data (see module documentation)
	 * @return control instance
	 * @throws Throwable
	 *             when control cannot be added
	 */
	@WrapToScript
	public Control addControl(Control control, @ScriptParameter(defaultValue = ScriptParameter.NULL) String layout) throws Throwable {
		return runInUIThread(new RunnableWithResult<Control>() {
			@Override
			public Control runWithTry() throws Throwable {
				getUICompositor().insertElement(control, new Location(layout));

				return control;
			}
		});
	}

	/**
	 * Remove a control.
	 *
	 * @param controlOrLocation
	 *            either the control instance returned from a create* method or the coordinates the control is created in.
	 */
	@WrapToScript
	public void removeControl(Object controlOrLocation) {
		Location location = null;

		if (controlOrLocation instanceof Viewer)
			controlOrLocation = ((Viewer) controlOrLocation).getControl();

		if (controlOrLocation instanceof Control) {
			final int index = Arrays.asList(getUICompositor().getComposite().getChildren()).indexOf(controlOrLocation);
			location = new Location(getUICompositor().fViewModel.indexToPoint(index));

		} else
			location = new Location(controlOrLocation.toString());

		if (location != null)
			getUICompositor().insertElement(getUICompositor().fRenderer.createPlaceHolder(location.getPosition()), location);
	}

	/**
	 * Display a grid aiding in layouting. When the grid is displayed, empty cells do show a label with their location coordinates.
	 *
	 * @param showGrid
	 *            <code>true</code> to display.
	 */
	@WrapToScript
	public void showGrid(@ScriptParameter(defaultValue = "true") boolean showGrid) {
		Display.getDefault().syncExec(() -> {

			getUICompositor().setShowGrid(showGrid);
		});
	}

	/**
	 * Get the current event in case we are within a UI callback method.
	 *
	 * @return current UI event or <code>null</code>
	 */
	@WrapToScript
	public Object getUiEvent() {
		return fUiEvent;
	}

	/**
	 * Make sure that script engine does not get terminated. This is necessary whenever callbacks are registered.
	 */
	private void keepScriptEngineAlive() {
		if (getScriptEngine() instanceof IReplEngine) {
			fLifecycleManager.setScriptEngineTerminateState(((IReplEngine) getScriptEngine()).getTerminateOnIdle());
			((IReplEngine) getScriptEngine()).setTerminateOnIdle(false);
		}
	}

	private <T> T runInUIThread(RunnableWithResult<T> runnable) throws Throwable {
		Display.getDefault().syncExec(runnable);

		return runnable.getResultOrThrow();
	}

	private void runEventCallback(Object event, Object callback) {
		fUiEvent = event;
		try {
			getScriptEngine().inject(callback, false);
		} catch (final Throwable e) {
			// silently swallow
		} finally {
			fUiEvent = null;
		}
	}

	private UICompositor getUICompositor() {
		return fUICompositors.get(0);
	}

	private class UICompositor {

		private final ViewModel fViewModel;
		private final CompositeRenderer fRenderer;
		private ResourceManager fResourceManager = null;

		public UICompositor(Composite composite) {
			fRenderer = new CompositeRenderer(composite);
			fViewModel = new ViewModel(fRenderer);
		}

		public Composite getComposite() {
			return fRenderer.getParent();
		}

		public void insertElement(Object element, Location location) {
			fViewModel.insertElement(element, location);
			update();
		}

		public void setShowGrid(boolean showGrid) {
			for (final UICompositor compositor : fUICompositors)
				compositor.fRenderer.setShowGrid(showGrid);

			update();
		}

		public void update() {
			getUICompositor().fRenderer.update();
		}

		public ResourceManager getResourceManager() {
			if (fResourceManager == null)
				fResourceManager = new LocalResourceManager(JFaceResources.getResources(), getComposite());

			return fResourceManager;
		}
	}

	private class GenericLabelProvider extends ColumnLabelProvider {

		@Override
		public String getText(Object element) {
			if (element != null) {
				String text = callMethod("getName", String.class, element);
				if (text != null)
					return text;

				text = callMethod("getIdentifier", String.class, element);
				if (text != null)
					return text;
			}

			return super.getText(element);
		}

		@SuppressWarnings("unchecked")
		private <T> T callMethod(String methodName, Class<T> returnType, Object element) {
			final Class<? extends Object> elementClass = element.getClass();
			try {
				final Method method = elementClass.getMethod(methodName);
				if (method != null) {
					if (returnType.isAssignableFrom(method.getReturnType()))
						return (T) method.invoke(element);
				}

			} catch (final Exception e) {
				// silently swallow
			}

			return null;
		}
	}

	/**
	 * Manages script termination when last created object gets destroyed.
	 */
	private class LifecycleManager {

		private final Collection<Object> fCreatedElements = new HashSet<>();
		private Boolean fInitialTerminateOnIdle = null;

		public void add(Object element) {
			fCreatedElements.add(element);
		}

		public void remove(Object element) {
			fCreatedElements.remove(element);

			if (fCreatedElements.isEmpty()) {
				if (fInitialTerminateOnIdle != null) {
					if (getScriptEngine() instanceof IReplEngine)
						((IReplEngine) getScriptEngine()).setTerminateOnIdle(fInitialTerminateOnIdle);
				}
			}
		}

		public void setScriptEngineTerminateState(boolean terminateOnIdle) {
			fInitialTerminateOnIdle = terminateOnIdle;
		}
	}
}
