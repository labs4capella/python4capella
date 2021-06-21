#
# This script loads the IFE Capella model and list all its LogicalComponent.
# To run it:
#  - enable Developer capabilities if not alreadey done (see documentation in the help menu)
#  - right click this script and select the Run As / EASE Script menu
#

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capellamodeller.py')
if False:
    from simplified_api.capellamodeller import *

# Load the IFE example
model = CapellaModel("/In-Flight Entertainment System/In-Flight Entertainment System.aird")

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print(se.get_name())

# print the name of each LogicalComponent
for lc in se.get_all(LogicalComponent):
    #: :type lc: LogicalComponent
    print(" - " + lc.get_name())
