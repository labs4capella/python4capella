#
# This script loads the Capella model passed as first argument and imports PhysicalComponent from an xlsx file.
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - launch the contextual menu "Run As / Run configurations..." on this script
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Import_physical_components_from_xlsx.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Import_physical_components_from_xlsx.py"
#    - define the path to the aird file as first argument and the xlsx file as second argument in "Script arguments" area: "/In-Flight Entertainment System/In-Flight Entertainment System.aird" "/Python4Capella/resources/physical_components.xlsx" (for instance)

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

#check parameter numbers
if len(argv) != 2:
    # use IFE default values
    aird_path = "/In-Flight Entertainment System/In-Flight Entertainment System.aird"
    xlsx_path = "/Python4Capella/resources/physical_components.xlsx"
else:
    # Load the Capella model from the first argument of the script
    aird_path = argv[0]
    xlsx_path = argv[1]

model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering
se = model.get_system_engineering()

# create  a folder in the project
xlsx_file = CapellaPlatform.getWorkspaceFile(xlsx_path)
xlsx_file_name = CapellaPlatform.getAbsolutePath(xlsx_file)

print("Read " + xlsx_file_name)

# load the workbook
wb = load_workbook(xlsx_file_name)

# grab the active worksheet
ws = wb.active

# get the PhysicalComponentPkg
pc_pkg = se.get_physical_architecture().get_physical_component_pkg()

# start a transaction to modify the Capella model
model.start_transaction()
try:
    # create physical components with the list of names in the xlsx file
    for row in ws.iter_rows():
        for cell in row:
            # create a PhysicalComponent
            pc = PhysicalComponent()
            #set its name
            print("* Create a new physical component with name " + cell.value)
            pc.set_name(cell.value)
            #add the new PhysicalComponent
            pc_pkg.get_owned_physical_components().add(pc)
except:
    # if something went wrong we rollback the transaction
    model.rollback_transaction()
    raise
else:
    # if everything is ok we commit the transaction
    model.commit_transaction()

# save the Capella model
model.save()
