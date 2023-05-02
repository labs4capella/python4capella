include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
include('workspace://Python4Capella/simplified_api/pvmt_header.py')
if False:
    from simplified_api.pvmt_header import *


class PVMT(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        JavaObject.__init__(self, java_object)
    @staticmethod
    def get_p_v_names(elem: CapellaElement) -> List[str]:
        """
        Parameters: elem: CapellaElement
        Returns: String[*]
        status: OK
        """
        #: :type elem: CapellaElement
        res = []
        for group in elem.get_java_object().getOwnedPropertyValueGroups():
            for pv in group.getOwnedPropertyValues():
                res.append(pv.getName())
        return res
    @staticmethod
    def is_p_v_defined(elem: CapellaElement, PVName: str) -> bool:
        """
        Parameters: elem: CapellaElement, PVName: String
        Returns: Boolean
        status: OK
        """
        return PVName in PVMT.get_p_v_names(elem)
    @staticmethod
    def get_p_v_value(elem: CapellaElement, PVName: str) -> str:
        """
        Parameters: elem: CapellaElement, PVName: String
        Returns: String
        status: OK
        """
        for group in elem.get_java_object().getOwnedPropertyValueGroups():
            for pv in group.getOwnedPropertyValues():
                if PVName == pv.getName():
                    if pv.eClass().getName() == "BooleanPropertyValue":
                        return str(pv.isValue())
                    elif pv.eClass().getName() == "EnumerationPropertyValue":
                        if pv.getValue() is not None:
                            return pv.getValue().getName()
                        else:
                            return None
                    else:
                        return str(pv.getValue())
        return None


