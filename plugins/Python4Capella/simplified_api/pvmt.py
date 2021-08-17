include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *


class PVMT(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PVMT):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_p_v_names(self, elem):
        raise AttributeError("TODO")
    def is_p_v_defined(self, elem, PVName):
        raise AttributeError("TODO")
    def get_p_v_value(self, elem, PVName):
        raise AttributeError("TODO")


