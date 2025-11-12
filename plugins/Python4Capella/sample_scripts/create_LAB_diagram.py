# name                 : Generate LAB diagram
# script-type          : Python
# description          : Creates a LAB diagram for the selected element
# popup                : enableFor(org.polarsys.capella.core.data.la.LogicalComponent)
#
# This script create a new Logical Architecture Blank diagram for the selected LogicalComponent.
# To run it:
#  - selected a LogicalComponent in the project explorer
#  - right click on it
#  - select the "Generate LAB diagram" menu

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/diagram.py')
if False:
    from simplified_api.diagram import *

# we define a function that will recursively walk the given LogicalComponent and it's children to apply the given mapping.
def create_logical_component_mappings(parentContainer, logical_component, mapping):
    for child in logical_component.get_owned_logical_components():
        # the semantic element of the "LAB Logical Component" is the component Part
        newContainer = apply_mapping(parentContainer, mappingComponent, child.get_java_object().getAbstractTypedElements()[0])
        newContainer.getSemanticElements().add(logical_component.get_java_object())
        # we call the same function on the child LogicalComponent
        create_logical_component_mappings(newContainer, child, mapping)


# Retrieve the Element from the current selection and its aird model path
selected_elem = LogicalComponent(CapellaPlatform.getFirstSelectedElement())
aird_path = '/'+ CapellaPlatform.getModelPath(selected_elem)

# we get all objects needed to create a new "Logical Architecture Blank" diagram
session = Sirius.get_session(selected_elem.get_java_object())
representationDefinition = get_representation_definition_by_name(session, "Logical Architecture Blank")



model = CapellaModel()
model.open(aird_path)
model.start_transaction()
try:
    # we create the representation
    newRepresentation = create_representation(session, selected_elem, representationDefinition, "[LAB] " + selected_elem.get_name() + " (generated)")

    # we recursively walk the component and its children to create a "LAB Logical Component"
    mappingComponent = get_representation_mapping_by_name(representationDefinition, "LAB Logical Component")
    create_logical_component_mappings(newRepresentation, selected_elem, mappingComponent)
except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()

# save the Capella model
model.save()
