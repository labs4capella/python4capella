package validationRules;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.validation.AbstractModelConstraint;
import org.eclipse.emf.validation.IValidationContext;
import org.polarsys.capella.core.data.information.AggregationKind;
import org.polarsys.capella.core.data.information.Association;
import org.polarsys.capella.core.data.information.Property;

public class AssociationNavigationCheck extends AbstractModelConstraint {

	public AssociationNavigationCheck() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public IStatus validate(IValidationContext ctx) {
		EObject obj = ctx.getTarget();
		if (obj instanceof Association) {
			boolean problem = false; 
			Association assos = (Association) obj;
			
			// if both members are navigable => OK
			if (assos.getNavigableMembers().size() == 2) {
				return ctx.createSuccessStatus();
			} else {
				Property navProp = assos.getNavigableMembers().get(0);
				if (navProp.getAggregationKind().equals(AggregationKind.COMPOSITION)) {
					// it's a composition => OK
					return ctx.createSuccessStatus();
				} else {
					// we have an error
					Property ownedProp = assos.getOwnedMembers().get(0);
					return ctx.createFailureStatus(navProp.getName(), ownedProp.getName(), 
							navProp.getAbstractType().getName(), ownedProp.getAbstractType().getName());					
				}
			}
		}
		return ctx.createSuccessStatus();
	}

}
