#
# This script loads the Capella model passed as first argument and add a "short ID" to all logical components, actors and the system
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - you can run this script by launching the contextual menu "Run As / EASE Script..." 
#    on this script. 
#    - By default, the model selected is IFE sample (aird path of the model written below)

#  - you can also run this script according to a configuration (script selected, arguments) 
#    and modify the configuration by launching the contextual menu "Run As / Run configurations..." 
#    on this script. 
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Autoname_Logical_Components_Actors_and_System.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Autoname_Logical_Components_Actors_and_System.py"
#    - define the path to the aird file as first argument in "Script arguments" area: "/In-Flight Entertainment System/In-Flight Entertainment System.aird" (for instance)

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# change this path to execute the script on your model (here is the IFE sample). 
# comment it if you want to use the "Run configuration" instead
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

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print("Model opened:" + se.get_name())

# Initialize counter for Logical Components
i = 1
prefixLogCom = "LC-"

# Initialize counter for Actors
j = 1
prefixLogAct = "LA-"

# Initialize counter for Logical System
k = 1
prefixLogSys = "LS-"

# Number of decimals in the code (e.g. LogSys999)
decimals = 3

# Retrieve existing id if any
print("Getting existing IDs...")
codesList =[]
for lc in se.get_all_contents_by_type(LogicalComponent):
    codeLenght = len(prefixLogCom) + decimals
    if lc.get_name()[:len(prefixLogCom)] == prefixLogCom:
        codesList.append(lc.get_name()[:codeLenght])

for lc in se.get_all_contents_by_type(LogicalSystem):
    codeLenght = len(prefixLogSys) + decimals
    if lc.get_name()[:len(prefixLogSys)] == prefixLogSys:
        codesList.append(lc.get_name()[:codeLenght])   

for lc in se.get_all_contents_by_type(LogicalActor):
    codeLenght = len(prefixLogAct) + decimals
    if lc.get_name()[:len(prefixLogAct)] == prefixLogAct:
        codesList.append(lc.get_name()[:codeLenght])           

# start transaction to make modifications in the model
model.start_transaction()

print("Renaming ...")

# Add the id to objects (if not present)
try:
    # Rename the system
    for lc in se.get_all_contents_by_type(LogicalSystem):
        autoNo = prefixLogSys + str(k).zfill(decimals)
        
        if lc.get_name()[:len(prefixLogSys)] != prefixLogSys:
            while autoNo in codesList:
                k = k + 1
                autoNo = prefixLogSys + str(k).zfill(decimals)
            lc.set_name(autoNo + " - " + lc.get_name())
            codesList.append(autoNo)
     
    # Rename the Actors
    for lc in se.get_all_contents_by_type(LogicalActor):
        autoNo = prefixLogAct+ str(j).zfill(decimals)
        if lc.get_name()[:len(prefixLogAct)] != prefixLogAct:
            while autoNo in codesList:
                j = j + 1
                autoNo = prefixLogAct+ str(j).zfill(decimals)
            lc.set_name(autoNo + " - " + lc.get_name())
            codesList.append(autoNo)
                   
    # Rename the components  
    for lc in se.get_all_contents_by_type(LogicalComponent):
        autoNo = prefixLogCom + str(i).zfill(decimals)
        if lc.get_name()[:len(prefixLogCom)] != prefixLogCom:
            while autoNo in codesList:
                i = i + 1
                autoNo = prefixLogCom + str(i).zfill(decimals)
            lc.set_name(autoNo + " - " + lc.get_name())
            codesList.append(autoNo)
except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()
 
model.save()

print("Rename ended & model saved")
