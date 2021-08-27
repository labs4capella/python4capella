'''
This script allows to extract a pseudo-hierarchy of elements defined in Physical Architecture starting from the Node PC,
getting the sub-NodePC and deployed BehaviorPV, from the BehaviorPV getting the sub-Behavior PV and allocated functions

It will create a folder result in the selected Capella project with the resulting xlsx file.
'''
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - launch the contextual menu "Run As / Run configurations..." on this scr
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Need4.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Need4.py"
#

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
    
# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *
    
# include needed to read/write xlsx files
from openpyxl import *

# we define a generic method to retrieve the sub-elements of any kind of element
def getSubElements(ws, i, j, elem):
    ws.cell(row = i, column = j).value = elem.get_name()
    i = i+1
    if (isinstance(elem, NodePC)):
        npc = elem
        #: :type npc: NodePC
        # if we have a NodePC we want the sub-NodePC and deployed BehaviorPC
        for subPC in npc.get_owned_physical_components():
            i = getSubElements(ws, i, j+1, subPC)
        for bpc in npc.get_deployed_behavior_p_cs():
            i = getSubElements(ws, i, j+1, bpc)
    if isinstance(elem, BehaviorPC):
        bpc = elem
        #: :type bpc: BehaviorPC
        # if we have a BehaviorPC we want the sub-BehaviorPC and allocated Functions
        for subPC in bpc.get_owned_physical_components():
            i = getSubElements(ws, i, j+1, subPC)
        for func in bpc.get_allocated_functions():
            i = getSubElements(ws, i, j+1, func)
    # we have nothing more to do if we have a function
    return i

# change this path to execute the script on your model
aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print('starting export of model ' + se.get_name())

# preparing excel file export
project_name = aird_path[0:(aird_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, 'results')
xlsx_file_name = CapellaPlatform.getAbsolutePath(folder) + '/' + 'Need4.xlsx'
# create a workbook
workbook = Workbook()

# writing excel file header
worksheet = workbook.active
worksheet.title = 'PA export'
worksheet["A1"] = 'Elem 1'
worksheet["B1"] = 'Elem 2'
worksheet["C1"] = 'Elem 3'
worksheet["D1"] = 'Elem 4'
worksheet["E1"] = 'Elem 5'
worksheet["F1"] = 'Elem 6'
worksheet["G1"] = 'Elem 7'
worksheet["H1"] = 'Elem 8'
worksheet["I1"] = 'Elem 9'

i=2

# retrieving elements from the model
for npc in se.get_physical_architecture().get_physical_system().get_owned_physical_components():
    if (isinstance(npc, NodePC)):
        i = getSubElements(worksheet, i, 1, npc)
        
# Save the xlsx file
workbook.save(xlsx_file_name)

print('saving excel file')

# refresh 
CapellaPlatform.refresh(folder)