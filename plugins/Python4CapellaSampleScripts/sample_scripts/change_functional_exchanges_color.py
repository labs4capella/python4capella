# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for the requirement API
include('workspace://Python4Capella/simplified_api/requirement.py')
if False:
    from simplified_api.requirement import *



def need_style_change(chain):
    return True


def change_diagram_element_style(representation_element):
    # at this point we only have edge style for other styles see:
    # https://forum.mbse-capella.org/t/editing-requirements-format-with-p4c/6054
    print(representation_element.getOwnedStyle().getStrokeColor())
    # you can add org to known symbols to remove the error from the editor
    # https://github.com/labs4capella/python4capella/blob/master/doc/org.eclipse.python4capella.doc/doc/user/general/RemoveFalseErrors.textile
    color = org.eclipse.sirius.viewpoint.RGBValues.create(50, 50, 50)
    representation_element.getOwnedStyle().setStrokeColor(color)
    representation_element.getOwnedStyle().getCustomFeatures().add("strokeColor")


aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()

# start a transaction to modify the Capella model
model.start_transaction()
try:
    chains = se.get_all_contents_by_type(FunctionalChain)
    for capability in chains:
        print(capability.get_name())
        # here we call a query from the semantic browser
        for exchange in capella_query_by_name(capability, "Involved Exchanges", FunctionalExchange):
            if need_style_change(exchange):
                print("  - " + exchange.get_name())
                for diagram in exchange.get_representing_diagrams():
                    print("    - " + diagram.get_name())
                    # at this point we use the Java API
                    for representation_element in diagram.get_java_object().getRepresentation().getOwnedRepresentationElements():
                        if representation_element.getTarget() == exchange.get_java_object():
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

