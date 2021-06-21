# name                 : Export Diagrams
# script-type          : Python
# description          : Exports diagrams from the selected LogicalComponent
# popup                : enableFor(org.polarsys.capella.core.data.la.LogicalComponent)

#
# This script contribute a menu "Export Diagrams" on LogicalComponents.
# You can right click on a LogicalComponent to access the menu.
#

# includes needed to interact with the Eclipse platform
loadModule('/System/Platform')
loadModule('/System/UI')
# include needed for the Capella simplified API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# Creates a LogicalComponent from the current selection
lc = LogicalComponent(getSelection().getFirstElement())

print(lc.get_name() + "'s realizing components")
for rc in lc.get_realizing_physical_components():
    #: :type rc: Component
    print(" - " + rc.get_name())
print("")

# Iterates over representations to export them
for rd in lc.get_representation_descriptors():
    #: :type rd: DRepresentationDescriptor
    print("exporting " + rd.get_name())
    rd.export_image("/tmp/" + rd.get_name() + ".jpg")
