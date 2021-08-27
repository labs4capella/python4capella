#
# This script loads the Capella model passed as first argument and list its root LogicalComponent.
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - launch the contextual menu "Run As / Run configurations..." on this script
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "list_logical_components.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/list_logical_components.py"
#    - define the path to the aird file as first argument in "Script arguments" area: "/In-Flight Entertainment System/In-Flight Entertainment System.aird" (for instance)

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

#check parameter numbers
if len(argv) != 1:
    print("You need one parameter the .aird file path:")
    print("For instance: \"/In-Flight Entertainment System/In-Flight Entertainment System.aird\"")
    quit()

# Load the Capella model from the first argument of the script
aird_path = argv[0]
model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print(se.get_name())

# print the name of each LogicalComponent
for lc in se.get_logical_architecture().get_logical_component_pkg().get_owned_logical_components():
    #: :type lc: LogicalComponent
    print(" - " + lc.get_name())
