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
    @staticmethod
    def get_p_v_names(elem):
        #: :type elem: CapellaElement
        res = []
        for group in elem.get_java_object().getOwnedPropertyValueGroups():
            for pv in group.getOwnedPropertyValues():
                res.append(pv.getName())
        return res
    @staticmethod
    def is_p_v_defined(elem, PVName):
        return PVName in PVMT.get_p_v_names(elem)
    @staticmethod
    def get_p_v_value(elem, PVName):
        for group in elem.get_java_object().getOwnedPropertyValueGroups():
            for pv in group.getOwnedPropertyValues():
                if PVName == pv.getName():
                    if pv.eClass().getName() == "BooleanPropertyValue":
                        return str(pv.isValue())
                    else:
                        return str(pv.getValue())
        return None
