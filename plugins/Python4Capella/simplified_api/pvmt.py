include('capella.py')
if False:
    from simplified_api.capella import *
include('pvmt_header.py')
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
    def get_system_engineering(capellaElement: CapellaElement) -> SystemEngineering:
        """
        """
        """
        """
        container = capellaElement.get_java_object()
        if container is None:
            return container
        else:
            system_engineering_e_class = get_e_classifier("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering")
            if system_engineering_e_class.isInstance(container):
                return SystemEngineering(container)
            else:
                return PVMT.get_system_engineering(JavaObject(container.eContainer()))
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
    @staticmethod
    def get_p_v_group_names(elem: CapellaElement) -> List[str]:
        """
        Parameters: elem: CapellaElement
        Returns: String[*]
        """
        #: :type elem: CapellaElement
        res = []
        for group in elem.get_java_object().getOwnedPropertyValueGroups():
            res.append(group.getName())
        return res
    @staticmethod
    def get_property_value_group(systemEngineering: SystemEngineering, propertyValuePackageName: str, propertyValueGroupName: str) -> PropertyValueGroup:
        """
        Parameters: systemEngineering: SystemEngineering, propertyValuePackageName: String, propertyValueGroupName: String
        Returns: PropertyValueGroup
        """
        project = systemEngineering.get_java_object().eContainer()
        for ext_package in project.getOwnedPropertyValuePkgs():
            if ext_package.getName() == "EXTENSIONS":
                for pv_package in ext_package.getOwnedPropertyValuePkgs():
                    if pv_package.getName() == propertyValuePackageName:
                        for pv_group in pv_package.getOwnedPropertyValueGroups():
                            if pv_group.getName() == propertyValueGroupName:
                                return PropertyValueGroup(pv_group)
    @staticmethod
    def get_property_value(systemEngineering: SystemEngineering, propertyValuePackageName: str, propertyValueGroupName: str, propertyValueName: str) -> PropertyValue:
        """
        Parameters: systemEngineering: SystemEngineering, propertyValuePackageName: String, propertyValueGroupName: String, propertyValueName: String
        Returns: PropertyValue
        """
        pvg = PVMT.get_property_value_group(systemEngineering, propertyValuePackageName, propertyValueGroupName)
        if pvg:
            for pv in pvg.get_owned_property_values():
                if pv.get_name() == propertyValueName:
                    return pv
    @staticmethod
    def get_enumeration_property_type(systemEngineering: SystemEngineering, propertyValuePackageName: str, typeName: str) -> EnumerationPropertyType:
        """
        Parameters: systemEngineering: SystemEngineering, propertyValuePackageName: String, typeName: String
        Returns: EnumerationPropertyType
        """
        project = systemEngineering.get_java_object().eContainer()
        for ext_package in project.getOwnedPropertyValuePkgs():
            if ext_package.getName() == "EXTENSIONS":
                for pv_package in ext_package.getOwnedPropertyValuePkgs():
                    if pv_package.getName() == propertyValuePackageName:
                        for type in pv_package.getOwnedEnumerationPropertyTypes():
                            if type.getName() == typeName:
                                return EnumerationPropertyType(type)
    @staticmethod
    def get_applied_property_value(elem: CapellaElement, propertyValuePackageName: str, propertyValueGroupName: str, propertyValueName: str) -> PropertyValue:
        """
        Parameters: elem: CapellaElement, propertyValuePackageName: String, propertyValueGroupName: String, propertyValueName: String
        Returns: PropertyValue
        """
        """
        Parameters: elem: CapellaElement, propertyValuePackageName: String, propertyValueGroupName: String, propertyValueName: String
        Returns: PropertyValue
        """
        systemEngineering = PVMT.get_system_engineering(elem)
        pv = PVMT.get_property_value(systemEngineering, propertyValuePackageName, propertyValueGroupName, propertyValueName)
        pvg = PropertyValueGroup(pv.get_java_object().eContainer())
        if pvg:
            for applied_pvg in elem.get_applied_property_value_groups():
                if applied_pvg.get_applied_property_value_groups().contains(pvg):
                    for owned_pv in applied_pvg.get_owned_property_values():
                        if owned_pv.get_applied_property_values().contains(pv):
                            return owned_pv
    @staticmethod
    def get_or_apply_property_value_group(elem: CapellaElement, propertyValuePackageName: str, propertyValueGroupName: str) -> PropertyValue:
        """
        Parameters: elem: CapellaElement, propertyValuePackageName: String, propertyValueGroupName: String
        Returns: PropertyValue
        """
        systemEngineering = PVMT.get_system_engineering(elem)
        pvg = PVMT.get_property_value_group(systemEngineering, propertyValuePackageName, propertyValueGroupName)
        if pvg:
            for applied_pvg in elem.get_applied_property_value_groups():
                if applied_pvg.get_applied_property_value_groups().contains(pvg):
                    return applied_pvg
            pvg_to_apply = PropertyValueGroup()
            pvg_to_apply.set_name(propertyValuePackageName + "." + propertyValueGroupName)
            pvg_to_apply.get_applied_property_value_groups().add(pvg)
            elem.get_applied_property_value_groups().add(pvg_to_apply)
            elem.get_owned_property_value_groups().add(pvg_to_apply)
            for pv in pvg.get_owned_property_values():
                pv_to_apply = PropertyValue(None, pv.get_java_object().eClass().getName())
                pv_to_apply.set_name(pv.get_name())
                pv_to_apply.get_applied_property_values().add(pv)
                pv_to_apply.set_value(pv.get_value())
                if pv.get_java_object().eClass().getName() == "EnumerationPropertyValue":
                    pv_to_apply.get_java_object().setType(pv.get_java_object().getType())
                pvg_to_apply.get_owned_property_values().add(pv_to_apply)
    @staticmethod
    def remove_applied_property_value_group(elem: CapellaElement, propertyValuePackageName: str, propertyValueGroupName: str):
        """
        Parameters: elem: CapellaElement, propertyValuePackageName: String, propertyValueGroupName: String
        """
        systemEngineering = PVMT.get_system_engineering(elem)
        pvg = PVMT.get_property_value_group(systemEngineering, propertyValuePackageName, propertyValueGroupName)
        if pvg:
            for applied_pvg in elem.get_applied_property_value_groups():
                if applied_pvg.get_applied_property_value_groups().contains(pvg):
                    elem.get_applied_property_value_groups().remove(applied_pvg)
                    elem.get_owned_property_value_groups().remove(applied_pvg)
                    EObject.delete_e_object(applied_pvg)
                    break


