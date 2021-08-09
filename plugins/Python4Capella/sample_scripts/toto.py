# name                 : Toto
# script-type          : Python
# description          : Toto
# popup                : enableFor(org.polarsys.capella.core.data.capellacore.CapellaElement)

include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

# Retrieve the Element from the current selection
elem = CapellaElement(CapellaPlatform.getFirstSelectedElement())

# create  a folder in the project
model_path = CapellaPlatform.getModelPath(elem)

print(model_path)