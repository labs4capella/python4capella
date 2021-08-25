include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *


class RequirementAddOn(JavaObject):
    def __init__(self, java_object = None):
        EObject.__init__(self, java_object)
    @staticmethod
    def get_requirement_modules(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        se = capellaModel.get_system_engineering()
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if extension.eClass().getName() == "CapellaModule" and extension.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                    res.append(CapellaModule(extension))
        return res
    @staticmethod
    def get_incoming_requirements(capellaElement):
        res = []
        #: :type capellaElement: CapellaElement
        capellaModel = CapellaModel()
        capellaModel.open(capellaElement)
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if capellaElement.get_java_object() == relation.getTarget() and relation.eClass().getName() == "CapellaIncomingRelation" and relation.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                        res.append(Requirement(relation.getSource()))
        return res
    @staticmethod
    def get_outgoing_requirements(capellaElement):
        res = []
        #: :type capellaElement: CapellaElement
        capellaModel = CapellaModel()
        capellaModel.open(capellaElement)
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if capellaElement.get_java_object() == relation.getSource() and relation.eClass().getName() == "CapellaOutgoingRelation" and relation.eClass().getEPackage().getNsURI().startswith("http://www.polarsys.org/capella/requirements"):
                        res.append(Requirement(relation.getTarget()))
        return res
    def get_relation_type(self, elem1, elem2):
        raise AttributeError("TODO")

class CapellaModule(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaModule"))
        elif isinstance(java_object, CapellaModule):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)
    def get_id(self):
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)

class Requirement(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Requirement"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_chapter_name(self):
        return self.get_java_object().getReqIFChapterName()
    def set_chapter_name(self, value):
        self.get_java_object().setReqIFChapterName(value)
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)
    def get_text(self):
        return self.get_java_object().getReqIFText()
    def set_text(self, value):
        self.get_java_object().setReqIFText(value)
    def get_all_attributes(self):
        raise AttributeError("TODO")
    def get_attribute(self, attributeName):
        raise AttributeError("TODO")
    def set_attribute(self, attributeName, value):
        raise AttributeError("TODO")
    def get_incoming_linked_elems(self):
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
    def get_outgoing_linked_elems(self):
        res = []
        for relation in self.java_object.getOwnedRelations():
            if relation.eClass().getName() == "CapellaOutgoingRelation":
                capella_element = relation.getSource()
                if capella_element is not None:
                    e_object_class = getattr(sys.modules["__main__"], "EObject")
                    specific_cls = e_object_class.get_class(capella_element)
                    if specific_cls is not None:
                        res.append(specific_cls(capella_element))
        return res

class Folder(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Folder"))
        elif isinstance(java_object, Folder):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)


