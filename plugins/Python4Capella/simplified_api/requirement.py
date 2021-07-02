include('workspace://Python4Capella/simplified_api/capellamodeller.py')
if False:
    from simplified_api.capellamodeller import *

class RequirementAddOn():
    @staticmethod
    def get_requirement_modules(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        se = capellaModel.get_system_engineering()
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if extension.eClass().getName() == "CapellaModule" and extension.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                    res.append(CapellaModule(extension))
        return res
    @staticmethod
    def get_incoming_requirements(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if relation.eClass().getName() == "CapellaIncomingRelation" and relation.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                        res.append(Requirement(requirement))
                        break
                try:
                    res.index(requirement)
                    break
                except ValueError:
                    continue
        return res
    @staticmethod
    def get_outgoing_requirements(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if relation.eClass().getName() == "CapellaOutgoingRelation" and relation.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                        res.append(Requirement(requirement))
                        break
                try:
                    res.index(requirement)
                    break
                except ValueError:
                    continue
        return res
    @staticmethod
    def get_relation_type(eObject1, eObject2):
        raise AttributeError("TODO")
        

class CapellaModule(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaModule"))
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
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)

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
    def get_chapter_name(self):
        return self.get_java_object().getReqIFChapterName()
    def set_chapter_name(self, value):
        self.get_java_object().setReqIFChapterName(value)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)
    def get_text(self):
        return self.get_java_object().getReqIFText()
    def set_text(self, value):
        self.get_java_object().setReqIFText(value)
    def get_owned_attributes(self):
        return create_e_list(self.get_java_object().getOwnedAttributes(), Attribute)
    def get_incoming_Linked_elems(self):
        raise AttributeError("TODO")
    def get_outgoing_Linked_elems(self):
        raise AttributeError("TODO")

class Attribute(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Attribute"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_value(self):
        raise AttributeError("TODO")
    def set_value(self, value):
        raise AttributeError("TODO")
    def get_kind(self):
        raise AttributeError("TODO")
    def set_kind(self, value):
        raise AttributeError("TODO")

# TODO create enum AttributeKind
#class AttributeKind(Enum):
#    boolean = 1
    

class Folder(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Folder"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)
