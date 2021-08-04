package org.eclipse.python4capella.validation;

import java.util.List;

import org.eclipse.core.resources.IMarker;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.emf.ecore.EObject;
import org.polarsys.capella.common.ef.command.AbstractReadWriteCommand;
import org.polarsys.capella.common.helpers.TransactionHelper;
import org.polarsys.capella.core.data.information.Property;
import org.polarsys.capella.core.validation.ui.ide.quickfix.AbstractCapellaMarkerResolution;

public class SetPropReadOnly extends AbstractCapellaMarkerResolution {

	public SetPropReadOnly() {
	}

	@Override
	public void run(IMarker marker) {
		final List<EObject> modelElements = getModelElements(marker);
		if (!modelElements.isEmpty()) {
			TransactionHelper.getExecutionManager(modelElements).execute(new AbstractReadWriteCommand() {
				public void run() {
					for (EObject obj : modelElements) {
						if (obj instanceof Property) {
			            	Property prop = (Property) obj;
			            	prop.setIsReadOnly(true);
			            }
					}
				}
			});
		}
		// remove the validation message
	    try {
			marker.delete();
		} catch (CoreException e) {
			// no nothing
		}
	}
}
