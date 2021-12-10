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
        raise AttributeError("TODO")
    def get_attribute(self, attributeName):
        """
        status: KO
        """
        raise AttributeError("TODO")
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


