'''
Created on 17 oct 2023

@author: Cesar Munuera
@contact: cesarmunuera@anzenengineering.com
@organization: Anzen Aerospace Engineering

@see: This python module contains classes to support the CapellaTypesFolder and derived objects
'''

include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
include('workspace://Python4Capella/simplified_api/requirement_header.py')
if False:
    from simplified_api.requirement_header import *


class CapellaTypesFolder(EObject):
    """
    Java class: org.polarsys.capella.vp.requirements.CapellaRequirements.CapellaTypesFolder
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaTypesFolder")

    def __init__(self, java_object=None):
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

    def get_owned_definition_types(self):
        return self.get_java_object().getOwnedDefinitionTypes()

    def get_owned_types(self):
        return self.get_java_object().getOwnedTypes()

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
    
    def set_data_type_definition(self, defType):
        """
        Set the given Definition Type to the list of Definition Types from the Capella Types Folder
        from model.
        :param defType: Definition Type to be added.
        """
        self.get_owned_definition_types().add(defType.get_java_object())

    
class AttributeDefinition(EObject):

    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.AttributeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AttributeDefinition")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))     
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
 
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    
    def set_long_name(self, name):
        self.get_java_object().setReqIFLongName(name)
    
    def set_data_type_definition(self, dataTypeDef):
        self.get_java_object().setDefinitionType(dataTypeDef.get_java_object())
        
    def get_data_type_definition(self):
        return self.get_java_object().getDefinitionType()


class AttributeDefinitionEnumeration(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.AttributeDefinitionEnumeration
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AttributeDefinitionEnumeration")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))     
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
 
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    
    def set_long_name(self, name):
        self.get_java_object().setReqIFLongName(name)
    
    def set_data_type_definition(self, dataTypeDef):
        self.get_java_object().setDefinitionType(dataTypeDef.get_java_object())
        
    def get_data_type_definition(self):
        return self.get_java_object().getDefinitionType()
    
    
class RequirementType(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.RequirementType
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "RequirementType")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))     
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
 
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    
    def set_long_name(self, name):
        self.get_java_object().setReqIFLongName(name)
        
    def get_owned_attributes(self):
        return self.get_java_object().getOwnedAttributes()
    
    def set_attibute_definition(self, attrDef):
        """
        Set the given Attribute Definition.
        :param attrDef: Attribute definition.
        """
        self.get_java_object().getOwnedAttributes().add(attrDef.get_java_object())
    
    
class DataTypeDefinition(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.DataTypeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "DataTypeDefinition")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))     
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
 
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    
    def set_long_name(self, name):
        self.get_java_object().setReqIFLongName(name)
    
    def set_description(self, description):
        self.get_java_object().setReqIFDescription(description)
        
    def get_description(self):
        self.get_java_object().getReqIFDescription()


class EnumerationDataTypeDefinition(EObject):
    """
    Java class: org.polarsys.kitalpha.vp.requirements.Requirements.EnumerationDataTypeDefinition
    """
    e_class = get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "EnumerationDataTypeDefinition")

    def __init__(self, java_object=None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))     
        elif isinstance(java_object, RequirementType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
 
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    
    def set_long_name(self, name):
        self.get_java_object().setReqIFLongName(name)
        
    def get_specified_values(self):
        return self.get_java_object().getSpecifiedValues()
    
    def set_values(self, value):
        """
        Create an enum value, set there the given string value.
        Then, set this enum to a Enumeration Data Type as value.
        :param value: string with value.
        """
        enum = EnumValue()
        enum.set_long_name(value)
        self.get_specified_values().add(enum.get_java_object())
