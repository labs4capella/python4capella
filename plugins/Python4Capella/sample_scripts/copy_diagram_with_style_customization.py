# name                 : Copy diagram with style customization
# script-type          : Python
# description          : Creates a LAB diagram for the selected element
# popup                : enableFor(org.eclipse.sirius.viewpoint.DRepresentationDescriptor)
#
# This script create a copy of the selected diagram with customized style.
# To run it:
#  - selected a LogicalComponent in the project explorer
#  - right click on it
#  - select the "Copy diagram with style customization" menu

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/diagram.py')
if False:
    from simplified_api.diagram import *


# Retrieve the Element from the current selection and its aird model path
selected_diagram = Diagram(CapellaPlatform.getFirstSelectedElement())
aird_path = '/'+ CapellaPlatform.getModelPath(selected_diagram)

model = CapellaModel()
model.open(aird_path)
model.start_transaction()


EDGE_COLOR =  org.eclipse.sirius.viewpoint.RGBValues.create(0, 255, 0)
CONTAINER_COLOR =  org.eclipse.sirius.viewpoint.RGBValues.create(255, 255, 0)

try:
    # we create a copy of the selected diagram
    representation_copy = selected_diagram.copy(selected_diagram.get_name() + " (copy with customized style)")

    # we customize the style of each diagram element
    for diagramElement in representation_copy.get_java_object().getRepresentation().getRepresentationElements():
        style_customizations = {}
        if dEdgeEClass.isInstance(diagramElement):
            # if the current diagramElement is an edge
            style_customizations["strokeColor"] = EDGE_COLOR
            style_customizations["lineStyle"] = get_enum_literal("http://www.eclipse.org/sirius/diagram/1.1.0", "LineStyle", "dot")
            style_customizations["routingStyle"] = get_enum_literal("http://www.eclipse.org/sirius/diagram/1.1.0", "EdgeRouting", "manhattan")
        elif dNodeContainerEClass.isInstance(diagramElement):
            # if the current diagramElement is a container
            style_customizations["backgroundColor"] = CONTAINER_COLOR
            style_customizations["foregroundColor"] = CONTAINER_COLOR
        customize_style(diagramElement.getOwnedStyle(), style_customizations)
except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()

# save the Capella model
model.save()
