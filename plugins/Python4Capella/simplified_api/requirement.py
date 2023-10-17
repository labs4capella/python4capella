include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
include('workspace://Python4Capella/simplified_api/requirement_header.py')
if False:
    from simplified_api.requirement_header import *
include('workspace://Python4Capella/simplified_api/requirement_types.py')
if False:
    from simplified_api.requirement_types import *

class RequirementAddOn(JavaObject):
    """
    """

    def __init__(self, java_object=None):
        """
        """
        JavaObject.__init__(self, java_object)

    @staticmethod
    def get_system_engineering(capellaElement: CapellaElement) -> SystemEngineering:
        """
        """
        container = capellaElement.get_java_object().eContainer()
        if container is None:
            return container
        else:
            if container.eClass().getName() == "SystemEngineering" and container.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/core/modeller"):
                return SystemEngineering(container)
            else:
                return RequirementAddOn.get_system_engineering(JavaObject(container))

    @staticmethod
    def get_requirement_modules(capellaElement: CapellaElement) -> List[CapellaModule]:
        """
        Parameters: model: CapellaModel
        Returns: CapellaModule[*]
        status: KO
        """
        # : :type capellaElement: CapellaElement
        res = []
        se = RequirementAddOn.get_system_engineering(capellaElement)
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if extension.eClass().getName() == "CapellaModule" and extension.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
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
        # : :type capellaElement: CapellaElement
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for relation in e_inverse_by_name(capellaElement.get_java_object(), "target"):
            if relation.get_java_object().eClass().getName() == "CapellaIncomingRelation" and relation.get_java_object().eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
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
        # : :type capellaElement: CapellaElement
        for extension in capellaElement.get_java_object().getOwnedExtensions():
            if extension.eClass().getName() == "CapellaOutgoingRelation" and extension.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                res.append(Requirement(extension.getTarget()))
        return res

    def get_relation_type(self, elem1: EObject, elem2: EObject) -> str:
        """
        Parameters: elem1: EObject, elem2: EObject
        Returns: String
        status: KO
        """
        raise AttributeError("TODO")


class CapellaModule(EObject):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaModule
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaModule")

    def __init__(self, java_object=None):
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
    
    def add_requirement(self, requirement):
        """
        Add the given requirement into the requirement list of the module.
        """
        self.get_java_object().getOwnedRequirements().add(requirement.get_java_object())

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


class Requirement(EObject):
    """
    Java class: org.polarsys.capella.core.data.requirement.Requirement
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Requirement")

    def __init__(self, java_object=None):
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

    def set_attribute(self, attribute):
        """
        Set the given attribute into the requirement.
        :param attr: Attribute to be setted.
        """
        self.get_java_object().getOwnedAttributes().add(attribute.get_java_object())

    def get_incoming_linked_elems(self) -> List[EObject]:
        """
        Returns: EObject[*]
        status: OK
        """
        res = []
        # : :type capellaElement: CapellaElement
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for relation in e_inverse_by_name(self.get_java_object(), "target"):
            if relation.get_java_object().eClass().getName() == "CapellaOutgoingRelation" and relation.get_java_object().eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
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
    
    def set_requirement_type_to_requirement(self, reqType):
        """
        Set the given Requirement Type.
        :param reqType: Requirement Type.
        """
        self.get_java_object().setRequirementType(reqType.get_java_object())
    
    def remove_all_attributes(self):
        """
        Remove all attributes from the requirement.
        :param req: Requirement.
        """
        size = self.get_java_object().getOwnedAttributes().size()
    
        for _ in range(size):
            attr = self.get_java_object().getOwnedAttributes().get(0)
            self.get_java_object().getOwnedAttributes().remove(attr)


class Folder(Requirement):
    """
    Java class: org.polarsys.capella.core.data.capellamodeller.Folder
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Folder")

    def __init__(self, java_object=None):
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

    def __init__(self, java_object=None, kind="StringValueAttribute"):
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

    def get_definition(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDefinition()

    def set_definition(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDefinition(value)

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
        Returns: String
        """
        self.get_java_object().setValue(value)


class ReqIFElement(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.ReqIFElement
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "ReqIFElement")

    def __init__(self, java_object=None):
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

    def __init__(self, java_object=None):
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

    def __init__(self, java_object=None):
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

    def __init__(self, java_object=None):
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
        Returns: Requirement
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
        Returns: CapellaElement
        """
        self.get_java_object().setTarget(value.get_java_object())


class CapellaOutgoingRelation(AbstractRelation):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaOutgoingRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation")

    def __init__(self, java_object=None):
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
        Returns: CapellaElement
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
        Returns: Requirement
        """
        self.get_java_object().setTarget(value.get_java_object())


class InternalRelation(AbstractRelation):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.InternalRelation
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "InternalRelation")

    def __init__(self, java_object=None):
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
        Returns: Requirement
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
        Returns: Requirement
        """
        self.get_java_object().setTarget(value.get_java_object())


class AbstractType(CapellaElement):
    """
    Java class: org.polarsys.capella.common.data.modellingcore.AbstractType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/core/" + capella_version(), "AbstractType")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))


class RelationType(AbstractType):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.RelationType
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "RelationType")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, RelationType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

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


