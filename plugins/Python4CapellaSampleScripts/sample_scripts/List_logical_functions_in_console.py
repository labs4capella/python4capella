# name                 : List logical functions in console
# script-type          : Python
# description          : List logical functions in console
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)
#
# This script loads the Capella model passed as first argument and list its root LogicalFunction.
# To run it:
#  - add this script location in the scripting preferences of not already done during the installation
#  - select a CapellaElement and right click on it
#  - select the "List logical functions in console" menu

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
print("The model name is " + se.get_name())

# print the name of each LogicalFunction
for lf in se.get_all_contents_by_type(LogicalFunction):
    #: :type lf: LogicalFunction
    print(" - " + lf.get_name())
