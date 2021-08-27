# name                 : Export Diagrams
# script-type          : Python
# description          : Exports diagrams of the selected Element
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)

#
# This script contributes a menu "Export Diagrams" on any CapellaElement in the Project Explorer.
# To run it:
# You can right click on a Capella element to access the menu "Export Diagrams".
# It will create a folder "Python4Capella_exported_diagrams" in your Capella project
# and export diagrams to it.
# It only exports the diagrams directly defined under the first selected element!

# include needed for the Capella simplified API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

# Retrieve the Element from the current selection
elem = CapellaElement(CapellaPlatform.getFirstSelectedElement())


# create  a folder in the project
model_path = CapellaPlatform.getModelPath(elem)
project_name = model_path[0:(model_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, "Python4Capella_exported_diagrams")

# Iterates over representations to export them
for diagram in elem.get_owned_diagrams():
    #: :type diagram: Diagram
    print("exporting " + diagram.get_name())
    diagram.export_as_image(CapellaPlatform.getAbsolutePath(folder) + "/" + diagram.get_name() + ".jpg")

CapellaPlatform.refresh(folder)
print("export completed")