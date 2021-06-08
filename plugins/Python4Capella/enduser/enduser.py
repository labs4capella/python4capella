# name                 : CapellaScript Sample
# script-type          : Python
# description          : CapellaScript Sample
# popup                : enableFor(org.polarsys.capella.core.data.la.LogicalComponent)

loadModule('/System/Platform')
loadModule('/System/UI')
include('workspace://CapellaScripting/advanced/capella.py')
if False:
    from advanced.capella import *
include('workspace://CapellaScripting/advanced/requirement.py')
if False:
    from advanced.requirement import *

lc = LogicalComponent(getSelection().getFirstElement())
print(lc.get_name() + "'s realizing components")
for rc in lc.get_realizing_physical_components():
    rc = Component(rc)
    print(" - " + rc.get_name())
print("")

print(str(len(lc.get_requirements())) + " attached requirements")
print("")

for rd in lc.get_representation_descriptors():
    rd = DRepresentationDescriptor(rd)
    print("exporting " + rd.get_name())
    rd.export_image("/tmp/" + rd.get_name() + ".jpg")
