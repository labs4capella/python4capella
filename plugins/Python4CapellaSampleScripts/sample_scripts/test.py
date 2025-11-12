# name                 : Compute cost
# script-type          : Python
# description          : Compute cost
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for the requirement API
include('workspace://Python4Capella/simplified_api/requirement.py')
if False:
    from simplified_api.requirement import *

aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
#aird_path = '/In-Flight Entertainment System.team/In-Flight Entertainment System.team.aird'

# aird_path = '/Leo/Leo.aird'
model = CapellaModel()
model.open(aird_path)
se = model.get_system_engineering()

print([feature.getName() for feature in LogicalActor.e_class.getEStructuralFeatures()])

##########################################################################

# def get_extensions(e_obj, cls):
#     """Gets the List of extensions with the given type for the given EObject"""
#     res = []
#     for ext in JavaList(e_obj.get_java_object().getOwnedExtensions(), cls):
#         if isinstance(ext, cls):
#             res.append(ext)
#
#     return res
#
# for recCat in get_extensions(se, RecCatalog):
#     print("- ", recCat.get_name())

##########################################################################

# Add a functional chain involvement function
# ‘Func1’ and ‘Func2’ are the Functions;
# ‘FuncEx’ is the functional exchange; and
# ‘FC’ is the Functional Chain
# see https://forum.mbse-capella.org/t/add-a-function-to-an-functional-chain/10637/4

# FCIF1 = create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementFunction")
# FCIF1.setInvolved(Func1.get_java_object())
# FC.get_java_object().getOwnedFunctionalChainInvolvements().add(FCIF1)
# FCIF2 = create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementFunction")
# FCIF2.setInvolved(Func2.get_java_object())
# FC.get_java_object().getOwnedFunctionalChainInvolvements().add(FCIF2)
# FCIL = create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementLink")
# FCIL.setInvolved(FuncEx.get_java_object())
# FCIL.setSource(FCIF1)
# FCIL.setTarget(FCIF2)
# FC.get_java_object().getOwnedFunctionalChainInvolvements().add(FCIL)
# print("FCIF1.getInvolvedElement()", FCIF1.getInvolvedElement())
# print("FCIF2.getInvolvedElement()", FCIF2.getInvolvedElement())
# print("FCIL.getInvolvedElement()", FCIL.getInvolvedElement())
# print("FCIF1.getInvolver()", FCIF1.getInvolver())
# print("FCIF2.getInvolver()", FCIF2.getInvolver())
# print("FCIL.getInvolver()", FCIL.getInvolver())
# print("FCIL.getSource()", FCIL.getSource())
# print("FCIL.getTarget()", FCIL.getTarget())


##########################################################################

# lc = LogicalComponent()
# interface = Interface()
# interface.set_name("MyInterface")
# interfaceUse = create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "InterfaceUse")
# lc.get_java_object().getOwnedInterfaceUses().add(interfaceUse)
# org.polarsys.capella.core.model.helpers.CapellaElementExt.creationService(interfaceUse)
# interfaceUse.setUsedInterface(interface.get_java_object())
# for i in lc.get_used_interfaces():
#     print(i.get_name())

##########################################################################

# LC1 = SystemEngineering(se.get_java_object())
# LC2 = SystemEngineering(se.get_java_object())
#
# jo_LC1 = LC1.get_java_object()
# jo_LC2 = LC2.get_java_object()
#
# print()
# print('LC1 =', LC1)
# print('LC2 =', LC2)
# print()
# print('LC1 is LC2:', LC1 is LC2)
# print('LC1 == LC2:', LC1 == LC2 )
# print('LC1 in [ LC2 ]:', LC1 in [ LC2 ])
#
# print()
# print('jo_LC1 =', jo_LC1)
# print('jo_LC2 =', jo_LC2)
# print()
# print('jo_LC1 is jo_LC2:', jo_LC1 is jo_LC2)
# print('jo_LC1 == jo_LC2:', jo_LC1 == jo_LC2)
# print('jo_LC1 in [ jo_LC2 ]:', jo_LC1 in [ jo_LC2 ])


##########################################################################

# def get_representation_definition_by_name(session, name):
#     for viewpoint in JavaList(java.util.ArrayList(session.getSelectedViewpoints(True)), EObject):
#         for representation_definition in viewpoint.get_java_object().getOwnedRepresentations():
#             if representation_definition.getName() == name:
#                 return representation_definition
#     return None
#
# session = Sirius.get_session(se.get_java_object())
# monitor = org.eclipse.core.runtime.NullProgressMonitor()
#
# entertain_during_flight_oc = se.get_all_contents_by_type(OperationalCapability)[0]
# description = get_representation_definition_by_name(session, "Operational Interaction Scenario")
#
# cabin_crew = None
# pilot = None
# for actor in se.get_all_contents_by_type(OperationalActor):
#     if actor.get_name() == "Cabin Crew":
#         cabin_crew = actor
#     elif actor.get_name() == "Pilot":
#         pilot = actor
#
# model.start_transaction()
# try:
#     # create semantic elements
#     my_scenario = Scenario()
#     entertain_during_flight_oc.get_owned_scenarios().add(my_scenario)
#     org.polarsys.capella.core.model.helpers.CapellaElementExt.creationService(my_scenario.get_java_object())
#     my_scenario.set_name("My Scenario")
#     cabin_crew_ir = InstanceRole()
#     my_scenario.get_owned_instance_roles().add(cabin_crew_ir)
#     org.polarsys.capella.core.model.helpers.CapellaElementExt.creationService(cabin_crew_ir.get_java_object())
#     cabin_crew_ir.get_java_object().setRepresentedInstance(cabin_crew.get_java_object().getAbstractTypedElements()[0])
#     pilot_ir = InstanceRole()
#     my_scenario.get_owned_instance_roles().add(pilot_ir)
#     org.polarsys.capella.core.model.helpers.CapellaElementExt.creationService(pilot_ir.get_java_object())
#     pilot_ir.get_java_object().setRepresentedInstance(pilot.get_java_object().getAbstractTypedElements()[0])
#
#     # create the diagram
#     semantic = my_scenario.get_java_object()
#     new_represenation = org.eclipse.sirius.business.api.dialect.DialectManager.INSTANCE.createRepresentation("[OES] My Scenario", semantic, description, session, monitor)
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     # if everything is ok we commit the transaction
#     model.commit_transaction()

# save the Capella model
# model.save()


##########################################################################

# for chain in se.get_all_contents_by_type(FunctionalChain):
#     print(chain.get_name())
#     for diagram in chain.get_owned_diagrams():
#         print("  -", diagram.get_name())

##########################################################################

# for link in se.get_all_contents_by_type(PhysicalLink):
#     ends = link.get_connected_physical_ports()
#     if len(ends) == 2:
#         comp_a, comp_b = ends[0].get_container(), ends[1].get_container()
#         print(comp_a, "->", comp_b)

##########################################################################

# def get_representation_definition_by_name(session, name):
#     for viewpoint in JavaList(java.util.ArrayList(session.getSelectedViewpoints(True)), EObject):
#         for representation_definition in viewpoint.get_java_object().getOwnedRepresentations():
#             if representation_definition.getName() == name:
#                 return representation_definition
#     return None
#
# session = Sirius.get_session(se.get_java_object())
# representation_definition = get_representation_definition_by_name(session, "Logical Data Flow Blank")
# print(representation_definition)
#
# myLogicalFunction = se.get_all_contents_by_type(LogicalFunction)[0]
# for available in JavaList(java.util.ArrayList(org.eclipse.sirius.business.api.dialect.DialectManager.INSTANCE.getAvailableRepresentationDescriptions(session.getSelectedViewpoints(True), myLogicalFunction.get_java_object())), EObject):
#     print(available.get_java_object().getName())

##########################################################################

# session = Sirius.get_session(se.get_java_object())
# diagram = Sirius.get_all_diagrams(session)[0]
# semantic = diagram.getTarget()
# description = diagram.getDescription()
# monitor = org.eclipse.core.runtime.NullProgressMonitor()
#
# model.start_transaction()
# try:
#     new_represenation = org.eclipse.sirius.business.api.dialect.DialectManager.INSTANCE.createRepresentation("My Representation", semantic, description, session, monitor)
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     # if everything is ok we commit the transaction
#     model.commit_transaction()
#
# # save the Capella model
# model.save()



##########################################################################

# import os 
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

##########################################################################

# handler = org.polarsys.capella.core.sirius.ui.handlers.RefreshDiagramsCommandHandler()
# session = Sirius.get_session(se.get_java_object())
# capellaProject = org.polarsys.capella.core.sirius.ui.helper.SessionHelper.getCapellaProject(session)
# display = org.eclipse.swt.widgets.Display.getDefault()
# representationDescriptors = handler.getSubRepresentations(capellaProject, session)
# job = org.polarsys.capella.core.sirius.ui.handlers.RefreshDiagramsCommandHandler.RefreshDiagramsJob(handler, representationDescriptors, session, display)
# job.setUser(True);
# job.schedule();
# job.join()


##########################################################################

# loadModule('/System/UI');
# loadModule('/System/UI Builder');
#
# def check_all():
#     if instance.check_all.getSelection():
#         for name in instance.pvg_names:
#             checkbox_name = f"checkbox_{name}"
#             checkbox_instance = getattr(instance, checkbox_name)
#             checkbox_instance.setSelection(True)
#     else:
#         for name in instance.pvg_names:
#             checkbox_name = f"checkbox_{name}"
#             checkbox_instance = getattr(instance, checkbox_name)
#             checkbox_instance.setSelection(False)
#
# def other_callback():
#     print("other callback")
#
# class PvmtDialogPVG:
#     def __init__(self, pvg_names: list):
#         self.pvg_names = pvg_names  # List of names for checkboxes
#         self.check_all = None
#         self.check_none = None
#         self.prova = "prova"
#
#     def build(self):
#         self.labelFirstName = createLabel("Available Checkboxes:", "1/1 <x")
#
#
#         for name in self.pvg_names:
#             # Create a main checkbox for each pvg_name
#             checkbox_name = f"checkbox_{name}"
#             checkbox = createCheckBox(name, False, "other_callback()")
#             setattr(self, checkbox_name, checkbox)  
#
#         self.check_all = createCheckBox("SELECT ALL", False, "check_all()")
#
#     def evaluate(self, javaDialog):
#         selected_names = []
#         if javaDialog.getData(self.check_all):
#             selected_names = self.pvg_names
#         else:
#             for name in self.pvg_names:
#                 checkbox_name = f"checkbox_{name}"  # access the checkbox
#                 checkbox = getattr(self, checkbox_name, None)  # Get the checkbox attribute
#                 if checkbox and javaDialog.getData(checkbox):
#                     selected_names.append(name)
#         return selected_names
#
#
# list_checks = ['a', 'b', 'c', 'd', 'e']  # List of checkbox labels
# instance = PvmtDialogPVG(list_checks)
# title = "Checkbox Example"
# sub_title = "Select the checkboxes"
# javaDialog = createDialog("instance.build()", title, sub_title);
# result = executeUI("javaDialog.open()");
# if result == 0: 
#     selected_pvg_names = instance.evaluate(javaDialog)
#     print("Selected Checkboxes: " + str(selected_pvg_names))

##########################################################################

# fe = ComponentExchange()
# kind = get_enum_literal("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchangeKind", "FLOW")
# fe.get_java_object().setKind(kind)
# print(fe.get_java_object().getKind())
#
# pfip = ComponentPort()
# orientation = get_enum_literal("http://www.polarsys.org/capella/core/fa/" + capella_version(), "OrientationPortKind", "IN")
# pfip.get_java_object().setOrientation(orientation)
# print(pfip.get_java_object().getOrientation())
#
# port_kind = get_enum_literal("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentPortKind", "FLOW")
# pfip.get_java_object().setKind(port_kind)
# print(pfip.get_java_object().getKind())

##########################################################################

# functions = se.get_all_contents_by_type(PhysicalFunction)
# function = functions[0]
# runnables = se.get_all_contents_by_type(Runnable)
# runnable = runnables[0]
#
# Runnable(None, se)

##########################################################################

#gets the SystemEngineering and print its name
#
# # get the first class from the Capella model
# my_class = se.get_all_contents_by_type(Class)[0]
#
# model.start_transaction()
# try:
#     new_prop = PropertyValue()
#     my_class.get_owned_property_values().add(new_prop)
#     org.polarsys.capella.core.model.helpers.CapellaElementExt.creationService(new_prop.get_java_object())
#     new_prop.set_name("SomeProperty")
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     # if everything is ok we commit the transaction
#     model.commit_transaction()
#
# # save the Capella model
# model.save()


##########################################################################

# import json
#
# def createView(param0):
#     pass
# def createLabel(param0, param1):
#     pass
# def createText(param0):
#     pass
# def createComboViewer(param0, null, param2):
#     pass
# def createSeparator(true, param1):
#     pass
# def createButton(param0, saveAddress, param2):
#     pass
#
# loadModule("/System/UI Builder");
# loadModule("/System/UI");
# loadModule('/System/Resources');
#
# part = createView("Create Contact");
#
# createLabel("First Name:", "1/1 >x");
#
# txtFirstName = createText("2-4/1 o!");
# createLabel("Last Name:", "1/2 >x");
# txtLastName = createText("2-4/2 o!");
#
# createLabel("Phone:", "1/3 >x");
# txtPhone = createText("2-4/3 o!");
#
# createLabel("ZIP Code:", "1/4 >x");
# txtZipCode = createText("2/4 o");
#
# createLabel("Country:", "3/4 >x");
#
# cmbCountry = createComboViewer([ "Austria", "Germany", "India", "USA" ])
#
# createSeparator(True, "1-4/5 o")
#
# def save_address():
#     address = {
#         "lastName": txtLastName.getText(),
#         "firstName": txtFirstName.getText(),
#         "phone": txtPhone.getText(),
#         "zipCode": txtZipCode.getText(),
#         "country": cmbCountry.getSelection().getFirstElement()
#     }
#     data = json.dumps(address)
#     bundle = org.eclipse.core.runtime.Platform.getBundle("org.eclipse.e4.ui.workbench")
#     bundleContext = bundle.getBundleContext()
#     eclipseCtx = org.eclipse.e4.core.contexts.EclipseContextFactory.getServiceContext(bundleContext)
#     partService = eclipseCtx.get("org.eclipse.e4.ui.workbench.modeling.EPartService")
#     partService.hidePart(part, True)
#
# createButton("Save", "save_address()", "4/6 >")

##########################################################################

# # we get the Node PC Part and Behavior PC Part
# my_node_pc_part = None
# my_behavior_pc_part = None
# part_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Part")
# for part in JavaList(eAllContentsByType(se.get_java_object(), part_e_class), EObject):
#     print(part)
#     if part.get_java_object().getName() == "My Behavior PC":
#         my_behavior_pc_part = part.get_java_object()
#     if part.get_java_object().getName() == "My Node PC":
#         my_node_pc_part = part.get_java_object()
#     if my_behavior_pc_part and my_node_pc_part:
#         break
#
# print(my_node_pc_part)
# print(my_behavior_pc_part)
#
# # we create the PartDeploymentLink
# link = create_e_object("http://www.polarsys.org/capella/core/pa/deployment/" + capella_version(), "PartDeploymentLink")
# link.setLocation(my_node_pc_part)
# link.setDeployedElement(my_behavior_pc_part)
#
# model.start_transaction()
# try:
#     # add the link to the Node PC Part
#     my_node_pc_part.getOwnedDeploymentLinks().add(link)
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     # if everything is ok we commit the transaction
#     model.commit_transaction()
#
# # save the Capella model
# model.save()

##########################################################################


# loadModule('/System/UI')
# loadModule('/System/UI Builder')
# loadModule('/System/Resources')
#
# print("System Engineering:", se.get_name())
#
# def get_model_hierarchy():
#     """Retrieve only the Operational Analysis as the root element for the TreeViewer."""
#     operational_analysis = se.get_operational_analysis()
#     if operational_analysis:
#         print("Root Element Retrieved:", operational_analysis.get_name())
#         return [operational_analysis.get_java_object()]  # Return the actual Operational Analysis object
#     else:
#         print("No Operational Analysis found.")
#         return None
#
# def get_children(element):
#     """Retrieve children by navigating the containment structure using eContainer."""
#     print("get_children()", element)
#     try:
#         children = element.eContents()
#         print(f"{element.getName()} has {len(children)} children.")
#         res = children
#         print(res)
#         return res
#     except Exception:
#         return None
#
# def get_name_label(element):
#     """Retrieve children by navigating the containment structure using eContainer."""
#     print("get_name_label()", element)
#     try:
#         return element.getName()
#     except Exception:
#         return "<No name>"
#
# def get_size_label(element):
#     """Callback function to provide a size metric for each element."""
#     try:
#         child_count = len(element.eContents())
#         return f"{child_count} children"
#     except Exception:
#         return "No children"
#
# # UI setup with tree viewer, columns, and comparator
# createView("Operational Analysis Hierarchy")
# viewer = createTreeViewer(get_model_hierarchy(), "get_children(getProviderElement())")
#
# # Create columns for the viewer
# createViewerColumn(viewer, "Element", createLabelProvider("get_name_label(getProviderElement())"), 4)
# createViewerColumn(viewer, "Size", createLabelProvider("get_size_label(getProviderElement())"), 1)
#
# # Add comparator to sort elements
# # createComparator(viewer, "return (getProviderElement().get_all_contents() != null) ? 1 : 2;")


##########################################################################


# model.start_transaction()
#
#
# def getSequenceLinksDict(se):
#     res = {}
#     res['INCOMING'] = {}
#     res['OUTGOING'] = {}
#
#     e_class_SequenceLink = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "SequenceLink")
#     it = se.get_java_object().eAllContents()
#     while it.hasNext():
#         eObj = it.next()
#         if e_class_SequenceLink.isInstance(eObj):
#             # incoming sequence links
#             incoming_sequence_links = res['INCOMING'].get(eObj.getTarget())
#             if not incoming_sequence_links:
#                 incoming_sequence_links = []
#                 res['INCOMING'][eObj.getTarget()] = incoming_sequence_links
#             incoming_sequence_links.append(eObj)
#             # outgoing sequence links
#             outgoing_sequence_links = res['OUTGOING'].get(eObj.getSource())
#             if not outgoing_sequence_links:
#                 outgoing_sequence_links = []
#                 res['OUTGOING'][eObj.getSource()] = outgoing_sequence_links
#             outgoing_sequence_links.append(eObj)
#
#     return res
#
# def getIncomingSequenceLinks(sequence_link_dict, fcif):
#     res = sequence_link_dict['INCOMING'].get(fcif)
#
#     if not res:
#         res = []
#
#     return res
#
# def getOutgoingSequenceLinks(sequence_link_dict, fcif):
#     res = sequence_link_dict['OUTGOING'].get(fcif)
#
#     if not res:
#         res = []
#
#     return res
#
# try:
#     # collect incoming/outgoing sequence links dict
#     sequence_link_dict = getSequenceLinksDict(se)
#     # print(sequence_link_dict)
#
#     # collect FunctionalChainInvolvementFunction
#     functional_chain_fnvolvement_functions = []
#     e_class_FunctionalChainInvolvementFunction = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementFunction")
#     it = se.get_java_object().eAllContents()
#     while it.hasNext():
#         eObj = it.next()
#         if e_class_FunctionalChainInvolvementFunction.isInstance(eObj) and eObj.getInvolvedElement() == None:
#             functional_chain_fnvolvement_functions.append(eObj)
#
#     # change sequence links
#     for fcif in functional_chain_fnvolvement_functions:
#         incomingSequenceLinks = getIncomingSequenceLinks(sequence_link_dict, fcif)
#         outgoingSequenceLinks = getOutgoingSequenceLinks(sequence_link_dict, fcif)
#         # print("FunctionalChainInvolvementFunction", fcif.getId(), "incoming size", len(incomingSequenceLinks), "outgoing size", len(outgoingSequenceLinks))
#         if len(incomingSequenceLinks) == 1 and len(outgoingSequenceLinks) == 1:
#             # to add a new sequence link
#             # newSequenceLink = create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "SequenceLink")
#             # sequenceLink.eContainer().getOwnedSequenceLinks.add(newSequenceLink)
#             incomingSequenceLink = incomingSequenceLinks[0]
#             outgoingSequenceLink = outgoingSequenceLinks[0]
#             print("incoming", incomingSequenceLink.getId(), incomingSequenceLink.getSource().getId(), "->", incomingSequenceLink.getTarget().getId())
#             print("outgoing", outgoingSequenceLink.getId(), outgoingSequenceLink.getSource().getId(), "->", outgoingSequenceLink.getTarget().getId())
#             incomingSequenceLink.setTarget(outgoingSequenceLink.getTarget())
#             delete_e_object(fcif)
#             delete_e_object(outgoingSequenceLink)
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     # if everything is ok we commit the transaction
#     model.commit_transaction()
#
# # save the Capella model
# model.save()


##########################################################################


# model.start_transaction()
# try:
#     it = se.get_java_object().eAllContents()
#     while it.hasNext():
#         eObj = it.next()
#         if eObj.eClass().getName() == "FunctionalChainInvolvementFunction": # and eObj.getInvolvedElement() == None:
#             fcif = eObj
#             print("FunctionalChainInvolvementFunction", fcif.getId(), "incoming size", fcif.getIncomingInvolvementLinks().size(), "outgoing size", fcif.getOutgoingInvolvementLinks().size())
#             if fcif.getIncomingInvolvementLinks().size() == 1 and fcif.getOutgoingInvolvementLinks().size() == 1:
#                 newLink = create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementLink")
#                 incomingLink = fcif.getIncomingInvolvementLinks().get(0)
#                 outgoingLink = fcif.getOutgoingInvolvementLinks().get(0)
#                 incomingLink.setTarget(outgoingLink.getTarget())
#                 delete_e_object(fcif)
#                 delete_e_object(outgoingLink)
#                 break
# except:
#     # if something went wrong we rollback the transaction
#     model.rollback_transaction()
#     raise
# else:
#     model.rollback_transaction()
#     # if everything is ok we commit the transaction
#     #model.commit_transaction()
#
# # save the Capella model
# #model.save()


##########################################################################


# for functional_chain in se.get_all_contents_by_type(FunctionalChain):
#     print(type(functional_chain).__name__, functional_chain.get_name())
#     for functional_exchange in functional_chain.get_query_result("Involved Exchanges"):
#         print(" -", type(functional_exchange).__name__, functional_exchange.get_name())


##########################################################################

# uri = org.eclipse.emf.common.util.URI.createFileURI('/home/development/git/capella2modelica/Capella2Modelica/pvmt/Modelica_Interface-6.0.vpd')
# rs = org.eclipse.emf.ecore.resource.impl.ResourceSetImpl()
# r = rs.getResource(uri, True)
# for myVdpRoot in r.getContents():
#     print("VdpRoot", myVdpRoot.getName())
#     for myEnumerationDefinition in myVdpRoot.getEnumerations():
#         print("  ","EnumerationDefinition", myEnumerationDefinition.getName())
#         for myEnumerationLiteral in myEnumerationDefinition.getLiterals():
#             print("    ","EnumerationLiteral", myEnumerationLiteral.getName(), myEnumerationLiteral.getColor(), myEnumerationLiteral.getLabelColor())
#
# color_e_class = get_e_classifier("http://www.thalesgroup.com/vpd", "Color")
# myColor = create_e_object_from_e_classifier(color_e_class)
# myColor.setRed(100)
# myColor.setGreen(100)
# myColor.setBlue(100)
# myColor.setAlpha(0)
# myEnumerationLiteral.setColor(myColor)

##########################################################################

# print("Project System:", se.get_name())
# for lc in se.get_all_contents_by_type(LogicalComponent):
#     print("  - Logical Component:", lc.get_name())
#
# for lib in model.get_referenced_libraries():
#     lib_se = lib.get_system_engineering()
#     print("Library System:", lib_se.get_name())
#     for lc in lib_se.get_all_contents_by_type(LogicalComponent):
#         print("  - Logical Component:", lc.get_name())


##########################################################################

# file = showFileSelectionDialog("/tmp", 1, "Open a file", "this open a file for...")            
# print(file)


# folder = showFolderSelectionDialog("/tmp", "Open a folder", "this open a folder for...")            
# print(folder)

##########################################################################

# for diagram in model.get_diagrams("Component Exchanges Scenario"):
#     print("Diagram", diagram.get_name())
#     for element in diagram.get_represented_elements():
#         if isinstance(element, StateFragment):
#             print(" -", "StateFragment", element.get_id())
#             requirements = element.get_query_result("Allocated Requirements")
#             for requirement in requirements:
#                 print("   -","Allocated Requirement", requirement.get_name())


##########################################################################


# for pc in se.get_all_contents_by_type(PhysicalComponent):
    # # for part in e_inverse_by_name(pc.get_java_object(), "type"):
        # requirements = pc.get_query_result("Allocated Requirements")
        # if requirements:
            # print("PhysicalComponent", pc.get_name())
            # for requirement in requirements:
                # print(" -","Allocated Requirement", requirement.get_name())

##########################################################################

# d_annotation_e_class = get_e_classifier("http://www.eclipse.org/sirius/description/1.1.0", "DAnnotation")
# annotation = create_e_object_from_e_classifier(d_annotation_e_class)
# annotation.setSource("http://www.polarsys.org/capella/core/ProgressStatus")
# diagram.get_java_object().getEAnnotations().add(annotation)
# # remove old value if the annotation already exists
# annotation.getReferences().clear()
# # add the new status
# annotation.getReferences().add(new_status.get_java_object())
#
# annotation = create_e_object_from_e_classifier(d_annotation_e_class)
# annotation.setSource("http://www.polarsys.org/capella/core/StatusReview")
# diagram.get_java_object().getEAnnotations().add(annotation)
# annotation.getDetails().put("value", "New description")

######################################

#for diagram in model.get_all_diagrams():
#    print("Diagram", diagram.get_name())
#    progress = None
#    description = None
#    for annotation in diagram.get_java_object().getEAnnotations():
#        if annotation.getSource() == "http://www.polarsys.org/capella/core/ProgressStatus" and not annotation.getReferences().isEmpty():
#            progress = EnumerationPropertyLiteral(annotation.getReferences().get(0))
#        if annotation.getSource() == "http://www.polarsys.org/capella/core/StatusReview":
#            description = annotation.getDetails().get("value")
#    if progress:
#        print(" - progress:", progress.get_name())
#    if description:
#        print(" - description", description)


##########################################################################

# functional_chain_involvement_function_e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChainInvolvementFunction")
#
# # FunctionalChainInvolvementFunction are wrapped as CapellaElement in Python since we don't have the specific type
# for ffcf in JavaList(eAllContentsByType(se.get_java_object(), functional_chain_involvement_function_e_class), CapellaElement):
#     print("FunctionalChainInvolvementFunction", ffcf.get_id())
#
# myFunctionalChainInvolvementFunction = CapellaElement(createFromEClassifier(functional_chain_involvement_function_e_class))
# myConstraint = Constraint()
# myFunctionalChainInvolvementFunction.get_owned_constraints().append(myConstraint)
# myConstraint.get_java_object().getConstrainedElements().add(myFunctionalChainInvolvementFunction.get_java_object())
# myConstraint.set_specification(None)

##########################################################################

# for diagram in model.get_all_diagrams():
#     if diagram.get_java_object().getDescription().getName() == "Component Exchanges Scenario":
#         print("Diagram", diagram.get_name())
#         for element in diagram.get_represented_elements():
#             if isinstance(element, StateFragment):
#                 print("  -", "StateFragment", element.get_id())
#                 for function in element.get_query_result("Related Functions"):
#                     print("    -","Function",function.get_name())
                

##########################################################################

# project = se.get_java_object().eContainer()
# for pkg in project.getOwnedPropertyValuePkgs():
#     print("PropertyValuePkg", pkg.getName())
#     for pkgChild in pkg.getOwnedPropertyValuePkgs():
#         print("-", "PropertyValuePkg", pkgChild.getName())
#         for type in pkgChild.getOwnedEnumerationPropertyTypes():
#             print("  -", "EnumerationPropertyType", type.getName())

##########################################################################

# for scenario in se.get_all_contents_by_type(Scenario):
#     print("Scenario",scenario.get_name())
#     for function in scenario.get_query_result("Related Functions"):
#         print("-","Function",function.get_name())

##########################################################################



# myRequirement = Requirement()
# myFunction = PhysicalFunction()
#
# newCapellaIncomingRelation = CapellaIncomingRelation()
# myRequirement.get_owned_relations().add(newCapellaIncomingRelation)
#
# newCapellaIncomingRelation.set_source(myRequirement)
# newCapellaIncomingRelation.set_target(myFunction)


# print("System:",se.get_name())
# execution_e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "Execution")
# for execution in JavaList(eAllContentsByType(se.get_java_object(), execution_e_class), EObject):
#     print(" - ","Execution:", execution.get_java_object().getId())
#     if execution.get_java_object().getStart() and execution.get_java_object().getStart().getMessage() and execution.get_java_object().getStart().getMessage().getSendingFunction():
#         print("   - ", "Start message sending function:", execution.get_java_object().getStart().getMessage().getSendingFunction().getName())
#     if execution.get_java_object().getStart() and execution.get_java_object().getStart().getMessage() and execution.get_java_object().getStart().getMessage().getReceivingFunction():
#         print("   - ", "Start message receiving function:", execution.get_java_object().getStart().getMessage().getReceivingFunction().getName())
    
    


##########################################################################

    

# part_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Part")
# myBehaviorPC = BehaviorPC()
# myBehaviorPC.get_java_object().getOwnedFeatures().add(create_e_object_from_e_classifier(part_e_class))
# myNodePC = NodePC()
# myNodePC.get_java_object().getOwnedFeatures().add(create_e_object_from_e_classifier(part_e_class))
#
#
# def get_part(component):
#     part_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Part")
#     for feature in component.get_java_object().getOwnedFeatures():
#         if part_e_class.isInstance(feature):
#             return feature
#
#
# myNodePCPart = get_part(myNodePC)
# myBehaviorPCPart = get_part(myBehaviorPC)
#
# if myNodePCPart and myBehaviorPCPart:
#     part_deployment_link_e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/" + capella_version(), "PartDeploymentLink")
#     link = create_e_object_from_e_classifier(part_deployment_link_e_class)
#     link.setLocation(myNodePC.get_java_object())
#     link.setDeployedElement(myBehaviorPCPart)
#     myNodePCPart.getOwnedDeploymentLinks().add(link)
# else:
#     print("can't find one part")
        
    

##########################################################################

# myPhysicalComponent = PhysicalComponent()
# myPhysicalPort = PhysicalPort()
#
# # add the port to the component
# myPhysicalComponent.get_java_object().getOwnedFeatures().add(myPhysicalPort.get_java_object())
#
# myInterface = Interface()
#
# myPhysicalPort.get_java_object().getProvidedInterfaces().add(myInterface.get_java_object())
#
# myComponentExchange = ComponentExchange()
# myOtherPhysicalPort = PhysicalPort()
#
# myPhysicalComponent.get_java_object().getOwnedFeatures().add(myOtherPhysicalPort.get_java_object())
#
# myPhysicalComponent.get_java_object().getOwnedComponentExchanges().add(myComponentExchange.get_java_object())
# myComponentExchange.get_java_object().setSource(myPhysicalPort.get_java_object())
# myComponentExchange.get_java_object().setTarget(myOtherPhysicalPort.get_java_object())

##########################################################################

# CP = ComponentPort()
# fip = FunctionInputPort()
#
# allocation = create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "PortAllocation")
# allocation.setSourceElement(CP.get_java_object())
# allocation.setTargetElement(fip.get_java_object())
# CP.get_java_object().getOwnedPortAllocations().add(allocation)


# for diag in JavaList(org.eclipse.sirius.business.api.dialect.DialectManager.INSTANCE.getAllRepresentationDescriptors(model.session),Diagram):
#     print('- ', diag.get_name())
    

# diagram_name = "[LAB] IFE System - All Components, CEs"
# for diag in model.get_all_diagrams():
#     if diag.get_name() == diagram_name:
#         for comp in diag.get_represented_elements():
#             if isinstance(comp, LogicalComponent):
#                 print(comp.get_name())

# part_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Part")
# if part_e_class.isInstance(selected_obj.get_java_object()):
#     e_object_class = getattr(sys.modules["__main__"], "EObject")
#     value = selected_obj.get_java_object().getAbstractType()
#     specific_cls = e_object_class.get_class(value)
#     if specific_cls is not None:
#         selected_obj = specific_cls(value)
#     else:
#         selected_obj = CapellaElement(value)
#
# print(selected_obj, selected_obj.get_java_object())


# for exchange_item in se.get_all_contents_by_type(ExchangeItem):
#     print(exchange_item.get_name())
#     for element in exchange_item.get_owned_elements():
#         print(' - ', element.get_name(), element.get_java_object().getType().getName(), element.get_java_object().getOwnedMinCard().getValue(), element.get_java_object().getOwnedMaxCard().getValue())


# for logical_component in se.get_logical_architecture().get_logical_component_pkg().get_owned_logical_components():
#     for arch_component in logical_component.get_owned_logical_components():
#         print(arch_component.get_name())
#         sums = {}
#         for child_component in arch_component.get_all_contents_by_type(LogicalComponent):
#             print(child_component.get_name())
#             for prop in child_component.get_owned_property_values():
#                 print(' - ', prop.get_name(), ' ', prop.get_value())
#                 sums[prop.get_name()] = sums.get(prop.get_name(), 0) + prop.get_value()
#         print('    sums', sums)
        