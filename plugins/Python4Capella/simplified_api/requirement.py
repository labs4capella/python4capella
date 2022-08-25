include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *


class RequirementAddOn(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        JavaObject.__init__(self, java_object)
    @staticmethod
    def get_system_engineering(capellaElement):
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
    def get_requirement_modules(capellaElement):
        """
        status: KO
        """
        #: :type capellaElement: CapellaElement
        res = []
        se = RequirementAddOn.get_system_engineering(capellaElement)
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if extension.eClass().getName() == "CapellaModule" and extension.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                    res.append(CapellaModule(extension))
        return res
    @staticmethod
    def get_incoming_requirements(capellaElement):
        """
        status: OK
        """
        res = []
        #: :type capellaElement: CapellaElement
        for relation in e_inverse(capellaElement.get_java_object(), "target"):
            if relation.eClass().getName() == "CapellaIncomingRelation" and relation.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                capella_element = relation.getSource()
                if capella_element is not None:
                    e_object_class = getattr(sys.modules["__main__"], "EObject")
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    @staticmethod
    def get_outgoing_requirements(capellaElement):
        """
        status: OK
        """
        res = []
        #: :type capellaElement: CapellaElement
        for extension in capellaElement.get_java_object().getOwnedExtensions():
            if extension.eClass().getName() == "CapellaOutgoingRelation" and extension.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                res.append(Requirement(extension.getTarget()))
        return res
    def get_relation_type(self, elem1, elem2):
        """
        status: KO
        """
        raise AttributeError("TODO")

class CapellaModule(EObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaModule"))
        elif isinstance(java_object, CapellaModule):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_requirements(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)
    def get_id(self):
        """
        """
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        """
        """
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        """
        """
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        """
        """
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        """
        """
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        """
        """
        self.get_java_object().setReqIFName(value)
    def get_prefix(self):
        """
        """
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        """
        """
        self.get_java_object().setReqIFPrefix(value)

class Requirement(EObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Requirement"))
        elif isinstance(java_object, Requirement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_id(self):
        """
        """
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        """
        """
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        """
        """
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        """
        """
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        """
        """
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        """
        """
        self.get_java_object().setReqIFName(value)
    def get_chapter_name(self):
        """
        """
        return self.get_java_object().getReqIFChapterName()
    def set_chapter_name(self, value):
        """
        """
        self.get_java_object().setReqIFChapterName(value)
    def get_description(self):
        """
        """
        return self.get_java_object().getReqIFDescription()
    def set_description(self, value):
        """
        """
        self.get_java_object().setReqIFDescription(value)
    def get_prefix(self):
        """
        """
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        """
        """
        self.get_java_object().setReqIFPrefix(value)
    def get_text(self):
        """
        """
        return self.get_java_object().getReqIFText()
    def set_text(self, value):
        """
        """
        self.get_java_object().setReqIFText(value)
    def get_all_attributes(self):
        """
        status: KO
        """
        res = []
        for child in self.get_java_object().eContents():
             specific_cls_name = child.eClass().getName()
             if (specific_cls_name == "StringValueAttribute") or \
                (specific_cls_name == "IntegerValueAttribute") or \
                (specific_cls_name == "EnumerationValueAttribute") or \
                (specific_cls_name == "BooleanValueAttribute") or \
                (specific_cls_name == "RealValueAttribute"):
                 res.append(Attribute(child))
        return res
    def get_attribute(self, attributeName):
        """
        status: KO
        """
        for attr in self.get_all_attributes():
            if attributeName == attr.get_definition().getReqIFLongName():
                return attr
        return None
    def set_attribute(self, attributeName, value):
        """
        status: KO
        """
        raise AttributeError("TODO")
    def get_incoming_linked_elems(self):
        """
        status: OK
        """
        res = []
        #: :type capellaElement: CapellaElement
        for relation in e_inverse(self.get_java_object(), "target"):
            if relation.eClass().getName() == "CapellaOutgoingRelation" and relation.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                capella_element = relation.getSource()
                if capella_element is not None:
                    e_object_class = getattr(sys.modules["__main__"], "EObject")
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    def get_outgoing_linked_elems(self):
        """
        status: OK
        """
        res = []
        for relation in self.java_object.getOwnedRelations():
            if relation.eClass().getName() == "CapellaIncomingRelation":
                capella_element = relation.getTarget()
                if capella_element is not None:
                    e_object_class = getattr(sys.modules["__main__"], "EObject")
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res
    def get_owned_relations(self):
        """
        """
        return create_e_list(self.java_object.getOwnedRelations(), AbstractRelation)


class Folder(Requirement):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Folder"))
        elif isinstance(java_object, Folder):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_requirements(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)

class Attribute(EObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Attribute"))
        elif isinstance(java_object, Attribute):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    
    def get_definition(self):
        """
        """
        return self.get_java_object().getDefinition()
    
    def get_value(self):
        """
        """
        return self.get_java_object().getValue()
    
class ReqIFElement(EObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "ReqIFElement"))
        elif isinstance(java_object, ReqIFElement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
            

class AbstractRelation(ReqIFElement):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
            
    def get_relation_type(self):
        """
        """
        return RelationType(self.get_java_object().getRelationType())
    def set_relation_type(self, value):
        """
        """
        self.get_java_object().setRelationType(value.get_java_object())

class CapellaIncomingRelation(AbstractRelation):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
           JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaIncomingRelation"))
        elif isinstance(java_object, CapellaIncomingRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)  
    def set_source(self, value):
        """
        """
        self.get_java_object().setSource(value.get_java_object())
    def set_target(self, value):
        """
        """
        self.get_java_object().setTarget(value.get_java_object())
        

class CapellaOutgoingRelation(AbstractRelation):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
           JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation"))
        elif isinstance(java_object, CapellaOutgoingRelation):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)  
    def set_source(self, value):
        """
        """
        self.get_java_object().setSource(value.get_java_object())
    def set_target(self, value):
        """
        """
        self.get_java_object().setTarget(value.get_java_object())


class AbstractType(CapellaElement):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "AbstractType"))
        elif isinstance(java_object, AbstractType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    
class RelationType(AbstractType):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "RelationType"))
        elif isinstance(java_object, RelationType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

    @staticmethod
    def get_relation_types(architecture):
        """
        """
        res = []
        for fld in architecture.get_java_object().eContents():
            if fld.eClass().getName() == "CapellaTypesFolder":
                for rel in fld.eContents():
                    if rel.eClass().getName() == "RelationType":
                        res.append(RelationType(rel))
        
        return res
    
    @staticmethod
    def get_relation_type_by_name(architecture, name):
        """
        """
        for rel in RelationType.get_relation_types(architecture):
            if rel.get_name() == name:
                return rel
        return None
    
    def get_name(self):
        """
        """
        return self.get_java_object().getReqIFLongName()
        
