#
# This script loads the Capella model passed as first argument and list its root LogicalComponent.
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - right click this script and select the Run As / Run configuration menu
#    - define the path to the aird file as first argument
#      for instance: "/In-Flight Entertainment System/In-Flight Entertainment System.aird"
#

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
