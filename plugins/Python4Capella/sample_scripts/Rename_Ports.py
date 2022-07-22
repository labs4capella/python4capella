# name                 : Rename Ports
# script-type          : Python
# description          : add the name of the functional exchange or component exchange or physical link to the name of the related ports
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)

'''
Author: Jean GODOT - ALL4TEC
Version: 20220425

This script loads the Capella model passed as first argument and add the name of the functional exchange or component exchange or physical link to the name of the related ports
from Tools.scripts.ndiff import fopen
'''

# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - you can run this script by launching the contextual menu "Run As / EASE Script..." 
#    on this script. 
#    - By default, the model selected is IFE sample (aird path of the model written below)

#  - you can also run this script according to a configuration (script selected, arguments) 
#    and modify the configuration by launching the contextual menu "Run As / Run configurations..." 
#    on this script. 
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Rename_Ports.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Rename_Ports.py"
#    - define the path to the aird file as first argument in "Script arguments" area: "/In-Flight Entertainment System/In-Flight Entertainment System.aird" (for instance)

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# Retrieve the Element from the current selection and its aird model path
selected_elem = CapellaElement(CapellaPlatform.getFirstSelectedElement())
aird_path = '/'+ CapellaPlatform.getModelPath(selected_elem)

'''
# change this path to execute the script on your model (here is the IFE sample). 
# Uncomment it if you want to use the "Run configuration" instead'''

aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'

'''
#Here is the "Run Configuration" part to uncomment if you want to use this functionality :

#check parameter numbers
if len(argv) != 1:
    # use IFE default values
    aird_path = "/In-Flight Entertainment System/In-Flight Entertainment System.aird"
else:
    # Load the Capella model from the first argument of the script
    aird_path = argv[0]
'''


model = CapellaModel()
model.open(aird_path)

# get the SystemEngineering and print its name
se = model.get_system_engineering()
print("Model opened:" + se.get_name())

# Initialize CONSTANTS: default ports names
DEFAULT_FUNCTION_SOURCE_PORT_NAME = "FOP"
DEFAULT_FUNCTION_TARGET_PORT_NAME = "FIP"
DEFAULT_COMPONENT_PORT_NAME = "CP"
DEFAULT_PHYSICAL_PORT_NAME = "PP"

# Initialize counter to count the number of renamed ports
nb_renamed_ports = 0
     
# start transaction to make modifications in the model
model.start_transaction()

print("Renaming ...")
print()

try:
    # Rename source and target ports of the functional exchanges
    print("FUNCTION PORTS:")
    # for all the functional exchanges
    for fe in se.get_all_contents_by_type(FunctionalExchange):        
        # get the name of the functional exchange
        fe_name = fe.get_name()
        # get the source port
        fe_sp = fe.get_source_port()
        if fe_sp != None :
            # get the current name of the source port
            name_sp = fe_sp.get_label()
            # check if the name of the source port has already been changed
            # Does it contain "FOP" and is it smaller than 7 characters "FOP xx -" (considering that xx will never be greater than 99) ?
            if (name_sp[:len(DEFAULT_FUNCTION_SOURCE_PORT_NAME)] == DEFAULT_FUNCTION_SOURCE_PORT_NAME) and (len(name_sp) < 7):
                # prepare the new name
                new_name_sp = name_sp + ' - ' + fe_name
                # set the new name to the source port
                fe_sp.set_name(new_name_sp)
                print("Rename: " + new_name_sp)
                nb_renamed_ports = nb_renamed_ports + 1
        
        # get the target port
        fe_tp = fe.get_target_port()
        if fe_tp != None :
            # get the current name of the target port
            name_tp = fe_tp.get_label()
            # check if the name of the target port has already been changed
            # Does it contain "FIP" and is it smaller than 7 characters "FIP xx -" (considering that xx will never be greater than 99) ?
            if (name_tp[:len(DEFAULT_FUNCTION_TARGET_PORT_NAME)] == DEFAULT_FUNCTION_TARGET_PORT_NAME) and (len(name_tp) < 7):
                # prepare the new name
                new_name_tp = name_tp + ' - ' + fe_name
                # set the new name to the source port
                fe_tp.set_name(new_name_tp)
                print("Rename: " + new_name_tp)
                nb_renamed_ports = nb_renamed_ports + 1
    print("Number of renamed ports :", nb_renamed_ports)
    print("\n")
    nb_renamed_ports = 0
    
    # Rename the component ports
    print("COMPONENT PORTS:")
    # for all the component ports
    for cp in se.get_all_contents_by_type(ComponentPort):       
        # get the current name of the component port
        name_cp = cp.get_name()
        # check if the name of the component port has already been changed
        # Does it contain "CP" and is it smaller than 6 characters "CP xx -" (considering that xx will never be greater than 99) ?
        if (name_cp[:len(DEFAULT_COMPONENT_PORT_NAME)] == DEFAULT_COMPONENT_PORT_NAME) and (len(name_cp) < 6):
            # get the related component exchanges
            ce_list = cp.get_component_exchanges()
            # get the size of the list of the component exchanges
            nb_ce = JavaList.size(ce_list)
            # if this list is not empty
            if nb_ce != 0:
                # get the first item of the list (always only one item ?)
                ce = JavaList.get(ce_list, 0)
                # get the name of the component exchange
                name_ce = ce.get_name()
                # prepare the new name
                new_name_cp = name_cp + " - " + name_ce
                # set the new name to the port
                cp.set_name(new_name_cp)
                print("Rename: " + new_name_cp)
                nb_renamed_ports = nb_renamed_ports + 1
    print("Number of renamed ports :", nb_renamed_ports)
    print("\n")
    nb_renamed_ports = 0
        
    # Rename the physical ports
    print("PHYSICAL PORTS:")
    # for all physical ports
    for pp in se.get_all_contents_by_type(PhysicalPort):
        # get the current name of the physical port  
        name_pp = pp.get_name()
        # check if the name of the physical port has already been changed
        # Does it contain "PP" and is it smaller than 6 characters "PP xx -" (considering that xx will never be greater than 99) ?
        if (name_pp[:len(DEFAULT_PHYSICAL_PORT_NAME)] == DEFAULT_PHYSICAL_PORT_NAME) and (len(name_pp) < 6):
            # get the list of the related physical links
            pl_list = pp.get_physical_links()
            # Rename only the physical ports which have only one physical links (0 physical links = port not used ; more than 1 physical links = delegation port)
            if (len(pl_list) == 1):
                # prepare the new name
                new_name_pp = name_pp + " - " + pl_list[0].get_name()
                # set the new name to the port
                pp.set_name(new_name_pp)
                print("Rename: " + new_name_pp)
                nb_renamed_ports = nb_renamed_ports + 1
    print("Number of renamed ports :", nb_renamed_ports)
    print("\n")

except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()
 
model.save()

print("Rename ended & model saved")
