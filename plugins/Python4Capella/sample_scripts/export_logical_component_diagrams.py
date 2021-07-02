# name                 : Export Diagrams
# script-type          : Python
# description          : Exports diagrams from the selected LogicalComponent
# popup                : enableFor(org.polarsys.capella.core.data.la.LogicalComponent)

#
# This script contribute a menu "Export Diagrams" on LogicalComponents.
# You can right click on a LogicalComponent to access the menu.
# It will create a "Python4Capella_exported_diagrams" in your Capella project
# and export diagrams to it.

# includes needed to interact with the Eclipse platform
loadModule('/System/Platform')
loadModule('/System/UI')
loadModule('/System/Resources')
# include needed for the Capella simplified API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# Creates a LogicalComponent from the current selection
lc = LogicalComponent(getSelection().getFirstElement())

# create  a folder in the project
model_path = lc.get_java_object().eResource().getURI().toPlatformString(True);
project_name = model_path[1:(model_path.index("/", 1) + 1)]
project = getProject(project_name)
folder = project.getFolder("Python4Capella_exported_diagrams")
if not folder.exists():
    folder.create(True, True, None)


# Iterates over representations to export them
for rd in lc.get_representation_descriptors():
    #: :type rd: DRepresentationDescriptor
    print("exporting " + rd.get_name())
    rd.export_image(folder.getLocation().toString() + "/" + rd.get_name() + ".jpg")

folder.refreshLocal(2, None)
