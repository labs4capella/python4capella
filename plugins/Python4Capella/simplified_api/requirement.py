include('capella.py')
if False:
    from simplified_api.capella import *
include('requirement_header.py')
if False:
    from simplified_api.requirement_header import *


class RequirementAddOn(JavaObject):
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
        container = capellaElement.get_java_object()
        if container is None:
            return container
        else:
            system_engineering_e_class = get_e_classifier("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering")
            if system_engineering_e_class.isInstance(container):
                return SystemEngineering(container)
            else:
                return RequirementAddOn.get_system_engineering(JavaObject(container.eContainer()))
    @staticmethod
    def get_requirement_modules(capellaElement: CapellaElement) -> List[CapellaModule]:
        """
        Parameters: model: CapellaModel
        Returns: CapellaModule[*]
        status: KO
        """
        #: :type capellaElement: CapellaElement
        res = []
        se = RequirementAddOn.get_system_engineering(capellaElement)
        capella_module_e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaModule")
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if capella_module_e_class.isInstance(extension):
                    res.append(CapellaModule(extension))
        return res
    @staticmethod
    def get_incoming_requirements(capellaElement: CapellaElement) -> List[Requirement]:
        """
        Parameters: elem: CapellaElement
        Returns: Requirement[*]
        status: OK
        """
        res = []
        #: :type capellaElement: CapellaElement
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        capella_incoming_relation_e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaIncomingRelation")
        for relation in e_inverse_by_name(capellaElement.get_java_object(), "target"):
            if capella_incoming_relation_e_class.isInstance(relation.get_java_object()):
                capella_element = relation.get_java_object().getSource()
                if capella_element is not None:
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    @staticmethod
    def get_outgoing_requirements(capellaElement: CapellaElement) -> List[Requirement]:
        """
        Parameters: elem: CapellaElement
        Returns: Requirement[*]
        status: KO
        """
        res = []
        #: :type capellaElement: CapellaElement
        capella_outgoing_relation_e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation")
        for extension in capellaElement.get_java_object().getOwnedExtensions():
            if capella_outgoing_relation_e_class.isInstance(extension):
                res.append(Requirement(extension.getTarget()))
        return res
    def get_relation_type(self, elem1: EObject, elem2: EObject) -> str:
        """
        Parameters: elem1: EObject, elem2: EObject
        Returns: String
        status: KO
        """
        raise AttributeError("TODO")
    @staticmethod
    def get_capella_types_folders(capellaElement: CapellaElement):
        """
        Parameters: elem: CapellaElement
        Returns: CapellaTypesFolder[*]
        """
        """
        Get the Capella Types Folder from the given Capella Element.
        """
        res = []
        se = RequirementAddOn.get_system_engineering(capellaElement)
        capella_types_folder_e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaTypesFolder")
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if capella_types_folder_e_class.isInstance(extension):
                    res.append(CapellaTypesFolder(extension))
        return res

class CapellaModule(EObject):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaModule
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaModule")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaModule):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_requirements(self) -> List[Requirement]:
        """
        Returns: Requirement[*]
        """
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)
    def get_id(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFLongName(value)
    def get_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFName()
    def set_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFName(value)
    def get_prefix(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFPrefix(value)
    def get_module_type(self) -> ModuleType:
        """
        Returns: ModuleType[0..1]
        """
        value =  self.get_java_object().getModuleType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_module_type(self, value: ModuleType):
        """
        Parameters: value: ModuleType[0..1]
        """
        return self.get_java_object().setModuleType(value.get_java_object())
    def get_owned_attributes(self) -> List[Attribute]:
        """
        Returns: Attribute[*]
        """
        return create_e_list(self.get_java_object().getOwnedAttributes(), Attribute)

class Requirement(EObject):
    """
    Java class: org.polarsys.capella.core.data.requirement.Requirement
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Requirement")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Requirement):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFName()
    def set_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFName(value)
    def get_chapter_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFChapterName()
    def set_chapter_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFChapterName(value)
    def get_prefix(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFPrefix(value)
    def get_text(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFText()
    def set_text(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFText(value)
    def get_owned_attributes(self) -> List[Attribute]:
        """
        Returns: Attribute[*]
        """
        return create_e_list(self.get_java_object().getOwnedAttributes(), Attribute)
    def get_owned_relations(self) -> List[AbstractRelation]:
        """
        Returns: AbstractRelation[*]
        """
        return create_e_list(self.get_java_object().getOwnedRelations(), AbstractRelation)
    def get_all_attributes(self) -> List[Attribute]:
        """
        Returns: String[*]
        status: OK
        """
        res = []
        for child in self.get_java_object().eContents():
            specific_cls_name = child.eClass().getName()
            if specific_cls_name in ["StringValueAttribute", "IntegerValueAttribute", "EnumerationValueAttribute", "BooleanValueAttribute", "RealValueAttribute"]:
                res.append(Attribute(child))
        return res
    def get_attribute(self, attributeName: str) -> Attribute:
        """
        Parameters: attributeName: String
        Returns: String
        status: OK
        """
        for attr in self.get_all_attributes():
            if attributeName == attr.get_definition().getReqIFLongName():
                return attr
        return None
    def set_attribute(self, attributeName: str, value: str):
        """
        Parameters: attributeName: String, value: String
        status: KO
        """
        raise AttributeError("TODO")
    def get_incoming_linked_elems(self) -> List[EObject]:
        """
        Returns: EObject[*]
        status: OK
        """
        res = []
        #: :type capellaElement: CapellaElement
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        capella_outgoing_relation_e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation")
        for relation in e_inverse_by_name(self.get_java_object(), "target"):
            if capella_outgoing_relation_e_class.isInstance(relation.get_java_object()):
                capella_element = relation.get_java_object().getSource()
                if capella_element is not None:
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    def get_outgoing_linked_elems(self) -> List[EObject]:
        """
        Returns: EObject[*]
        status: OK
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for relation in self.java_object.getOwnedRelations():
            if relation.eClass().getName() == "CapellaIncomingRelation":
                capella_element = relation.getTarget()
                if capella_element is not None:
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    def get_requirement_type(self) -> RequirementType:
        """
        Returns: RequirementType[0..1]
        """
        value =  self.get_java_object().getRequirementType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_requirement_type(self, value: RequirementType):
        """
        Parameters: value: RequirementType[0..1]
        """
        return self.get_java_object().setRequirementType(value.get_java_object())
    def get_id(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFLongName(value)
    def get_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFDescription()
    def set_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFDescription(value)

class Folder(Requirement):
    """
    Java class: org.polarsys.capella.core.data.capellamodeller.Folder
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Folder")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Folder):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_requirements(self) -> List[Requirement]:
        """
        Returns: Requirement[*]
        """
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)

class Attribute(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.Attribute
    """
    def __init__(self, java_object = None, kind = "StringValueAttribute"):
        """
        """
        if java_object is None:
            if kind in ["StringValueAttribute", "IntegerValueAttribute", "EnumerationValueAttribute", "BooleanValueAttribute", "RealValueAttribute"]:
                JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", kind))
            else:
                raise ValueError("kind must be either \"StringValueAttribute\", \"IntegerValueAttribute\", \"EnumerationValueAttribute\", \"BooleanValueAttribute\", or \"RealValueAttribute\"")
        elif isinstance(java_object, Attribute):
            JavaObject.__init__(self, java_object.get_java_object())
        elif get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Attribute").isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_definition(self) -> AttributeDefinition:
        """
        Returns: AttributeDefinition
        """
        value =  self.get_java_object().getDefinition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_definition(self, value: AttributeDefinition):
        """
        Parameters: value: AttributeDefinition
        """
        return self.get_java_object().setDefinition(value.get_java_object())
    def get_value(self) -> Any:
        """
        Returns: String
        """
        if self.get_java_object().eClass().getName() == "BooleanValueAttribute":
            return self.get_java_object().isValue()
        else:
            return self.get_java_object().getValue()
    def set_value(self, value):
        """
        Parameters: value: String
        """
        self.get_java_object().setValue(value)

class ReqIFElement(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.ReqIFElement
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "ReqIFElement")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ReqIFElement):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_id(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFLongName(value)
    def get_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReqIFDescription()
    def set_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReqIFDescription(value)

class EnumValue(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.EnumValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "EnumValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class AbstractRelation(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.AbstractRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AbstractRelation")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_relation_type(self):
        """
        Returns: RelationType
        """
        return capella_query_by_name(self, "Relation Type")

class CapellaIncomingRelation(AbstractRelation):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaIncomingRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaIncomingRelation")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaIncomingRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source(self) -> Requirement:
        """
        Returns: Requirement
        """
        value = self.get_java_object().getSource()
        if value is None:
            return value
        else:
            return Requirement(value)
    def set_source(self, value: Requirement):
        """
        Parameters: value: Requirement
        """
        self.get_java_object().setSource(value.get_java_object())
    def get_target(self) -> CapellaElement:
        """
        Returns: CapellaElement
        """
        value = self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is None:
                return None
            else:
                return specific_cls(value)
    def set_target(self, value: CapellaElement):
        """
        Parameters: value: CapellaElement
        """
        self.get_java_object().setTarget(value.get_java_object())

class CapellaOutgoingRelation(AbstractRelation):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaOutgoingRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaOutgoingRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source(self) -> CapellaElement:
        """
        Returns: CapellaElement
        """
        value = self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is None:
                return None
            else:
                return specific_cls(value)
    def set_source(self, value: CapellaElement):
        """
        Parameters: value: CapellaElement
        """
        self.get_java_object().setSource(value.get_java_object())
    def get_target(self) -> Requirement:
        """
        Returns: Requirement
        """
        value = self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            return Requirement(value)
    def set_target(self, value: Requirement):
        """
        Parameters: value: Requirement
        """
        self.get_java_object().setTarget(value.get_java_object())

class InternalRelation(AbstractRelation):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.InternalRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "InternalRelation")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, InternalRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source(self) -> Requirement:
        """
        Returns: Requirement
        """
        value = self.get_java_object().getSource()
        if value is None:
            return value
        else:
            return Requirement(value)
    def set_source(self, value: Requirement):
        """
        Parameters: value: Requirement
        """
        self.get_java_object().setSource(value.get_java_object())
    def get_target(self) -> Requirement:
        """
        Returns: Requirement
        """
        value = self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            return Requirement(value)
    def set_target(self, value: Requirement):
        """
        Parameters: value: Requirement
        """
        self.get_java_object().setTarget(value.get_java_object())

class AbstractType(ReqIFElement):
    """
    Java class: org.polarsys.capella.common.data.modellingcore.AbstractType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/core/" + capella_version(), "AbstractType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_attributes(self) -> List[AttributeDefinition]:
        """
        Returns: AttributeDefinition[*]
        """
        return create_e_list(self.get_java_object().getOwnedAttributes(), AttributeDefinition)

class RelationType(AbstractType):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.RelationType
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "RelationType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, RelationType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    @staticmethod
    def get_relation_types(architecture: Any) -> RelationType:
        """
        Returns: String
        status: KO
        """
        res = []
        for fld in architecture.get_java_object().eContents():
            if fld.eClass().getName() == "CapellaTypesFolder":
                for rel in fld.eContents():
                    if rel.eClass().getName() == "RelationType":
                        res.append(RelationType(rel))
        return res
    @staticmethod
    def get_relation_type_by_long_name(architecture: Any, long_name: str) -> RelationType:
        """
        Parameters: name: String
        Returns: String
        status: KO
        """
        for rel in RelationType.get_relation_types(architecture):
            if rel.get_long_name() == long_name:
                return rel
        return None

class TypesFolder(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.TypesFolder
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "TypesFolder")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, TypesFolder):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_definition_types(self) -> List[DataTypeDefinition]:
        """
        Returns: DataTypeDefinition[*]
        """
        return create_e_list(self.get_java_object().getOwnedDefinitionTypes(), DataTypeDefinition)
    def get_owned_types(self) -> List[AbstractType]:
        """
        Returns: AbstractType[*]
        """
        return create_e_list(self.get_java_object().getOwnedTypes(), AbstractType)

class CapellaTypesFolder(TypesFolder):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaTypesFolder
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaTypesFolder")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaTypesFolder):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class AttributeDefinition(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.AttributeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AttributeDefinition")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AttributeDefinition):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_default_value(self) -> Attribute:
        """
        Returns: Attribute[0..1]
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_value(self, value: Attribute):
        """
        Parameters: value: Attribute[0..1]
        """
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_definition_type(self) -> DataTypeDefinition:
        """
        Returns: DataTypeDefinition[0..1]
        """
        value =  self.get_java_object().getDefinitionType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_definition_type(self, value: DataTypeDefinition):
        """
        Parameters: value: DataTypeDefinition[0..1]
        """
        return self.get_java_object().setDefinitionType(value.get_java_object())

class AttributeDefinitionEnumeration(AttributeDefinition):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.AttributeDefinitionEnumeration
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AttributeDefinitionEnumeration")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AttributeDefinitionEnumeration):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_multi_valued(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMultiValued()
    def set_multi_valued(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMultiValued(value)

class RequirementType(AbstractType):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.RequirementType
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "RequirementType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class ModuleType(AbstractType):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.ModuleType
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "ModuleType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ModuleType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class DataTypeDefinition(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.DataTypeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "DataTypeDefinition")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, DataTypeDefinition):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class EnumerationDataTypeDefinition(ReqIFElement):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.EnumerationDataTypeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "EnumerationDataTypeDefinition")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumerationDataTypeDefinition):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_specified_values(self):
        """
        Returns: EnumValue[*]
        """
        return capella_query_by_name(self, "Specified Values")


