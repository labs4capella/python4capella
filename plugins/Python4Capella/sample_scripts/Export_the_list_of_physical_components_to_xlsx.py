#
# This script loads the Capella model passed as first argument and list its root PhysicalComponent to an xlsx file.
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - you can run this script by launching the contextual menu "Run As / EASE Script..." 
#    on this script. 
#    - By default, the model selected is IFE sample (aird path of the model written below)

#  - you can also run this script according to a configuration (script selected, arguments) 
#    and modify the configuration by launching the contextual menu "Run As / Run configurations..." 
#    on this script. 
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Export_the_list_of_physical_components_to_xlsx.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Export_the_list_of_physical_components_to_xlsx.py"
#    - define the path to the aird file as first argument in "Script arguments" area: "/In-Flight Entertainment System/In-Flight Entertainment System.aird" (for instance)
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
# gets the SystemEngineering
se = model.get_system_engineering()

# create  a folder in the project
model_path = CapellaPlatform.getModelPath(se)
project_name = model_path[0:(model_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, "Python4Capella_exported_xlsx")
xlsx_file_name = CapellaPlatform.getAbsolutePath(folder) + "/" + se.get_name() + "_physical_components.xlsx"


print("writing " + xlsx_file_name)

# create a workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active


# list the name of physical components
for index, pc in enumerate(se.get_physical_architecture().get_physical_component_pkg().get_owned_physical_components(), start=1):
    #: :type pc: PhysicalComponent
    # append the names in the worksheet
    ws["A" + str(index)] = pc.get_name()
    
# Save the xlsx file
wb.save(xlsx_file_name)

# refresh 
CapellaPlatform.refresh(folder)
