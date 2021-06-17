# name                 : CapellaScript Sample
# script-type          : Python
# description          : CapellaScript Sample
# popup                : enableFor(org.polarsys.capella.core.data.la.LogicalComponent)

loadModule('/System/Platform')
loadModule('/System/UI')
include('workspace://Python4Capella/advanced/capella.py')
if False:
    from advanced.capella import *
include('workspace://Python4Capella/advanced/requirement.py')
if False:
    from advanced.requirement import *

lc = LogicalComponent(getSelection().getFirstElement())
print(lc.get_name() + "'s realizing components")
for rc in lc.get_realizing_physical_components():
    #: :type rc: Component
    print(" - " + rc.get_name())
print("")

for rd in lc.get_representation_descriptors():
    #: :type rd: DRepresentationDescriptor
    print("exporting " + rd.get_name())
    rd.export_image("/tmp/" + rd.get_name() + ".jpg")
