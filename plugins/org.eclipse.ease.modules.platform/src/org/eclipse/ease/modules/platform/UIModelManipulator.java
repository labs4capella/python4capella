package org.eclipse.ease.modules.platform;

import java.util.List;

import org.eclipse.e4.ui.model.application.MApplication;
import org.eclipse.e4.ui.model.application.descriptor.basic.MPartDescriptor;
import org.eclipse.e4.ui.model.application.ui.MElementContainer;
import org.eclipse.e4.ui.model.application.ui.MUIElement;
import org.eclipse.e4.ui.model.application.ui.advanced.MPerspective;
import org.eclipse.e4.ui.model.application.ui.advanced.MPerspectiveStack;
import org.eclipse.e4.ui.model.application.ui.advanced.MPlaceholder;
import org.eclipse.e4.ui.model.application.ui.basic.MBasicFactory;
import org.eclipse.e4.ui.model.application.ui.basic.MPart;
import org.eclipse.e4.ui.model.application.ui.basic.MPartSashContainer;
import org.eclipse.e4.ui.model.application.ui.basic.MPartSashContainerElement;
import org.eclipse.e4.ui.model.application.ui.basic.MPartStack;
import org.eclipse.e4.ui.workbench.IWorkbench;
import org.eclipse.e4.ui.workbench.modeling.EModelService;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Control;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.views.IViewDescriptor;
import org.eclipse.ui.views.IViewRegistry;

public class UIModelManipulator {

	/**
	 * Find ID for a given view name. If <i>name</i> already contains a valid id, it will be returned.
	 *
	 * @param name
	 *            name of view
	 * @return view ID or <code>null</code>
	 */
	public static String getIDForName(final String name) {
		// look for a matching part descriptor
		final EModelService modelService = PlatformUI.getWorkbench().getService(EModelService.class);

		final IWorkbench workbench = PlatformUI.getWorkbench().getService(IWorkbench.class);
		final MApplication mApplication = workbench.getApplication();

		final List<MPartDescriptor> descriptors = modelService.findElements(mApplication, null, MPartDescriptor.class, null);
		for (final MPartDescriptor descriptor : descriptors) {
			if ((name.equals(descriptor.getElementId())) || (name.equals(descriptor.getLabel())))
				return descriptor.getElementId();
		}

		final List<MPart> partDescriptors = modelService.findElements(mApplication, null, MPart.class, null);
		for (final MPart descriptor : partDescriptors) {
			if ((name.equals(descriptor.getElementId())) || (name.equals(descriptor.getLabel())))
				return descriptor.getElementId();
		}

		// last resort: query view registry
		// see Bug 548226: some view IDs are not available in the model
		final IViewRegistry viewRegistry = PlatformUI.getWorkbench().getViewRegistry();
		for (final IViewDescriptor descriptor : viewRegistry.getViews()) {
			if ((name.equals(descriptor.getId())) || (name.equals(descriptor.getLabel())))
				return descriptor.getId();
		}

		return null;
	}

	/**
	 * Find the UI element for a given <i>id</i>.
	 *
	 * @param id
	 *            id to look for
	 * @return UI element instance or <code>null</code>
	 */
	public static MUIElement findElement(String id) {
		final EModelService modelService = PlatformUI.getWorkbench().getService(EModelService.class);

		final IWorkbench workbench = PlatformUI.getWorkbench().getService(IWorkbench.class);
		final MApplication mApplication = workbench.getApplication();
		final List<MPlaceholder> placeholders = modelService.findElements(mApplication, null, MPlaceholder.class, null);

		final MPerspective perspective = getCurrentPerspective();
		for (final MPlaceholder placeholder : placeholders) {
			if (placeholder.getElementId().equals(id)) {
				if (perspectiveContains(perspective, placeholder))
					return placeholder;
			}
		}

		final List<MPart> parts = modelService.findElements(mApplication, null, MPart.class, null);

		for (final MPart part : parts) {
			if (part.getElementId().equals(id)) {
				if (perspectiveContains(perspective, part))
					return part;
			}
		}

		return null;
	}

	/**
	 * Verify that a perspective contains a given element
	 *
	 * @param perspective
	 *            expected target perspective
	 * @param uiElement
	 *            element to look for
	 * @return <code>true</code> when perspective contains element
	 */
	private static boolean perspectiveContains(MPerspective perspective, MUIElement uiElement) {
		if (uiElement.getParent() == null)
			return false;

		if (perspective.equals(uiElement.getParent()))
			return true;

		return perspectiveContains(perspective, uiElement.getParent());
	}

	/**
	 * Get the currently active perspective.
	 *
	 * @return active perspective instance
	 */
	public static MPerspective getCurrentPerspective() {
		final EModelService modelService = PlatformUI.getWorkbench().getService(EModelService.class);

		final IWorkbench workbench = PlatformUI.getWorkbench().getService(IWorkbench.class);
		final MApplication mApplication = workbench.getApplication();
		final List<MPerspectiveStack> perspectiveStack = modelService.findElements(mApplication, null, MPerspectiveStack.class, null);

		return perspectiveStack.get(0).getSelectedElement();
	}

	/**
	 * Split a given {@link MPartStack}. Effectively we replace the part stack with a sash container and put the old part stack into the sash container.
	 *
	 * @param stack
	 *            stack to split
	 * @param position
	 *            where to put the existing stack within the sash. One of {@link SWT#TOP}, {@link SWT#BOTTOM}, {@link SWT#LEFT}, {@link SWT#RIGHT}
	 * @return newly created sash container
	 */
	public static MPartSashContainer splitPartStack(MElementContainer<MUIElement> stack, int position) {
		final MPartSashContainer newSashContainer = MBasicFactory.INSTANCE.createPartSashContainer();
		final MPartStack newPartStack = MBasicFactory.INSTANCE.createPartStack();

		final MElementContainer<MUIElement> parentContainer = stack.getParent();
		final int stackIndex = parentContainer.getChildren().indexOf(stack);

		parentContainer.getChildren().remove(stack);

		parentContainer.getChildren().add(stackIndex, newSashContainer);

		newSashContainer.setHorizontal((position == SWT.LEFT) || (position == SWT.RIGHT));

		newSashContainer.getChildren().add(newPartStack);
		newSashContainer.getChildren().add(((position == SWT.LEFT) || (position == SWT.TOP)) ? 0 : 1, (MPartSashContainerElement) stack);

		return newSashContainer;
	}

	/**
	 * Move a UI element to another container.
	 *
	 * @param uiElement
	 *            element to move
	 * @param targetContainer
	 *            target container to move to
	 */
	public static void move(MUIElement uiElement, MElementContainer<MUIElement> targetContainer) {
		remove(uiElement);
		add(uiElement, targetContainer);
	}

	/**
	 * Add a placeholder to a parent container.
	 *
	 * @param uiElement
	 *            element to add
	 * @param targetContainer
	 *            container to add placeholder to
	 */
	private static void add(MUIElement uiElement, MElementContainer<MUIElement> targetContainer) {
		targetContainer.getChildren().add(uiElement);
		if (targetContainer.getChildren().size() == 1)
			targetContainer.setSelectedElement(uiElement);
	}

	/**
	 * Remove a placeholder from its parent.
	 *
	 * @param uiElement
	 *            element to remove
	 */
	private static void remove(MUIElement uiElement) {
		final MElementContainer<MUIElement> parent = uiElement.getParent();
		parent.getChildren().remove(uiElement);

		reconcileContainer(parent);
	}

	/**
	 * Remove empty containers if there are any.
	 *
	 * @param container
	 *            container to reconcile
	 */
	public static void reconcileContainer(MElementContainer<MUIElement> container) {
		if (container.getChildren().isEmpty()) {
			final MElementContainer<MUIElement> sash = container.getParent();
			if (sash.getChildren().size() == 2) {
				// guess we have a sash here, remove and keep only 1 child of the sash

				// remove the empty container
				sash.getChildren().remove(container);
				Object widget = container.getWidget();
				if (widget instanceof Control)
					((Control) widget).dispose();

				// keep 2nd child element
				final MUIElement remainingContainer = sash.getChildren().remove(0);

				// remove sash
				final MElementContainer<MUIElement> sashParent = sash.getParent();
				final int sashIndex = sashParent.getChildren().indexOf(sash);
				sashParent.getChildren().remove(sash);

				widget = sash.getWidget();
				if (widget instanceof Control)
					((Control) widget).dispose();

				// replace sash with 2nd child element
				sashParent.getChildren().add(sashIndex, remainingContainer);
				sashParent.setSelectedElement(remainingContainer);
			}

		} else if (!container.getChildren().contains(container.getSelectedElement())) {
			// the selected element is gone, select a new one
			container.setSelectedElement(container.getChildren().get(0));
		}
	}
}
