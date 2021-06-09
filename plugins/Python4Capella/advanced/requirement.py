include('workspace://Python4Capella/advanced/capella.py')
if False:
    from advanced.capella import *

class Requirement(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Requirement"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

def get_requirements(self):
    res = [] #: :type res: list(Requirement)
    for e in get_extensions(self, "http://www.polarsys.org/kitalpha/requirements", "Requirement"):
        res.append(Requirement(e))
    return res
setattr(ExtensibleElement, "get_requirements", get_requirements)        
