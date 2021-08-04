package validationRules;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.validation.AbstractModelConstraint;
import org.eclipse.emf.validation.IValidationContext;
import org.polarsys.capella.core.data.information.AggregationKind;
import org.polarsys.capella.core.data.information.Property;

public class PropertyContainentROCheck extends AbstractModelConstraint {

	public PropertyContainentROCheck() {
	}

	@Override
	public IStatus validate(IValidationContext ctx) {
		EObject obj = ctx.getTarget();
		if (obj instanceof Property) {
			Property prop = (Property) obj;
			if (prop.getAggregationKind().equals(AggregationKind.COMPOSITION)) {
				if (!prop.isIsReadOnly()) {
					return ctx.createFailureStatus(prop.getName());
				}
			}
		}
		return ctx.createSuccessStatus();
	}

}
