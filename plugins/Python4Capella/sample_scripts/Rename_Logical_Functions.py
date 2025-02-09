# name                 : Rename Logical Functions
# script-type          : Python
# description          : add a short ID on Logical Fonctions
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)
'''
This script loads the Capella model passed as first argument and add a "short ID" to all logical fontions
'''

# 
# To run it:
#  - add this script location in the scripting preferences of not already done during the installation
#  - select a CapellaElement and right click on it
#  - select the "Rename Logical Functions" menu

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# Retrieve the Element from the current selection and its aird model path
selected_elem = CapellaElement(CapellaPlatform.getFirstSelectedElement())
aird_path = '/'+ CapellaPlatform.getModelPath(selected_elem)

'''
# change this path to execute the script on your model (here is the IFE sample). 
# Uncomment it if you want to use the "Run configuration" instead
aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
'''
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

# Initialize counter for Logical Fonctions
i = 1
prefixLogFunc = "LF-"

# Number of decimals in the code (e.g. LogSys999)
decimals = 3

# Retrieve existing id if any
print("Getting existing IDs...")
codesList =[]
for lf in se.get_all_contents_by_type(LogicalFunction):
    codeLenght = len(prefixLogFunc) + decimals
    if lf.get_name()[:len(prefixLogFunc)] == prefixLogFunc:
        codesList.append(lf.get_name()[:codeLenght])
       
# start transaction to make modifications in the model
model.start_transaction()

print("Renaming ...")

# Add the id to objects (if not present)
try:
    # Rename the system
    for lf in se.get_all_contents_by_type(LogicalFunction):
        autoNo = prefixLogFunc + str(i).zfill(decimals)
        
        if lf.get_name()[:len(prefixLogFunc)] != prefixLogFunc:
            while autoNo in codesList:
                i = i + 1
                autoNo = prefixLogFunc + str(i).zfill(decimals)
            lf.set_name(autoNo + " - " + lf.get_name())
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
