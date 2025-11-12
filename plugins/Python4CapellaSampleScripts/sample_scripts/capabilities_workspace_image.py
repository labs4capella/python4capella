# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for the requirement API
include('workspace://Python4Capella/simplified_api/requirement.py')
if False:
    from simplified_api.requirement import *



def need_style_change(capability):
    return True


def change_diagram_element_style(representation_element):
    print("found")
    style = representation_element.getOwnedStyle()
    helper = org.eclipse.sirius.diagram.ui.business.api.image.WorkspaceImageHelper()
    helper.updateStyle(style, "In-Flight Entertainment System/music.svg")
    style.setShowIcon(True)
    style.setLabelPosition(org.eclipse.sirius.diagram.LabelPosition.NODE_LITERAL)

aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()

# start a transaction to modify the Capella model
model.start_transaction()
try:
    capabilities = se.get_all_contents_by_type(Capability)
    for capability in capabilities:
        print(capability.get_name())
        if need_style_change(capability):
            print("  - " + capability.get_name())
            for diagram in capability.get_representing_diagrams():
                print("    - " + diagram.get_name())
                # at this point we use the Java API
                for representation_element in diagram.get_java_object().getRepresentation().getOwnedRepresentationElements():
                    if representation_element.getTarget() == capability.get_java_object():
                        change_diagram_element_style(representation_element)
except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()

# save the Capella model
model.save()
