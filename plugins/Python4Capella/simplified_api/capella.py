include('../java_api/EMF_API.py')
if False:
    from java_api.EMF_API import *
include('../java_api/Capella_API.py')
if False:
    from java_api.Capella_API import *
include('../java_api/Sirius_API.py')
if False:
    from java_api.Sirius_API import *
include('../utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *
include('../simplified_api/capella_header.py')
if False:
    from simplified_api.capella_header import *


class CapellaModel():
    """
    A Capella model. Used to defined the content of a model, and how to read a model
    """
    def start_transaction(self):
        """
        """
        Sirius.start_transaction(self.session)
    def commit_transaction(self):
        """
        """
        Sirius.commit_transaction(self.session)
    def rollback_transaction(self):
        """
        """
        Sirius.rollback_transaction(self.session)
    def get_system_engineering(self) -> SystemEngineering:
        """
        Returns: SystemEngineering
        """
        if self.session is None:
            return None
        else:
            return SystemEngineering(Sirius.get_system_engineering(self.session))
    def get_progress_status(self) -> str:
        """
        Returns: EnumerationPropertyType
        """
        value =  self.get_system_engineering().get_java_object().getStatus()
        if value is None:
            return value
        else:
            return value.getName()
    def get_referenced_libraries(self) -> List[CapellaLibrary]:
        """
        Returns: CapellaLibrary[*]
        """
        return get_libraries(self.get_system_engineering())
    def get_all_diagrams(self) -> List[Diagram]:
        """
        Returns: Diagram[*]
        """
        res = []
        descriptors = Sirius.get_all_diagrams(self.session)
        for descriptor in descriptors:
            res.append(Diagram(descriptor))
        return res
    def get_diagrams(self, diagram_type: str) -> List[Diagram]:
        """
        Parameters: diagramType: String
        Returns: Diagram[*]
        status: OK
        """
        return Sirius.get_diagrams(self.session, diagram_type)
    def open(self, obj: Any):
        """
        Parameters: path: String
        status: KO
        """
        # obj can be a path to the .aird file or an EObject
        if isinstance(obj, str) or isinstance(obj, unicode):
            if CapellaPlatform.getWorkspaceFile(obj) is None:
                raise AttributeError("the .aird file doesn't exist: " + obj)
            self.session = Sirius.load_session(obj)
        elif isinstance(obj, EObject):
            self.session = Sirius.get_session(obj.get_java_object())
        else:
            raise AttributeError("You can pass a path to the .aird file or an EObject.")
    def create(self, path: str):
        """
        Parameters: path: String
        status: KO
        """
        raise AttributeError("TODO")
    def save(self):
        """
        status: OK
        """
        self.session.save(Sirius.createProgressMonitor())

class CapellaLibrary(CapellaModel):
    """
    A Capella Library. A library is a model which can be referenced by other models in order to reuse its content
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaLibrary):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class EObject(JavaObject):
    """
    A generic object. Defines generic relations which are available for all elements
    """
    @staticmethod
    def get_class(e_object: EObject) -> type:
        """
        """
        try:
            res = getattr(sys.modules["__main__"], e_object.eClass().getName())
        except AttributeError:
            res = None
        if res == LogicalComponent:
            if e_object.isActor():
                res = LogicalActor
            elif is_system(e_object):
                res = LogicalSystem
        if res == PhysicalComponent:
            if e_object.isActor():
                res = PhysicalActor
            elif is_system(e_object):
                res = PhysicalSystem
            else:
                if e_object.getNature().getName() == "UNSET":
                    res = PhysicalComponent
                elif e_object.getNature().getName() == "BEHAVIOR":
                    res = BehaviorPC
                elif e_object.getNature().getName() == "NODE":
                    res = NodePC
                else:
                    raise AttributeError("Passed physical component has unexpected nature.")
        if res == None and e_object.eClass().getName() == "Entity":
            if e_object.isActor():
                res = OperationalActor
            else:
                res = OperationalEntity
        if res == None and e_object.eClass().getName() == "CatalogElement":
            if e_object.getKind().getName() == "REC":
                res = REC
            elif e_object.getKind().getName() == "RPL":
                res = RPL
            else:
                raise AttributeError("Passed catalog element has unexpected kind.")
        if res == None and e_object.eClass().getName() == "InteractionOperand":
            res = Operand
        if res == None and e_object.eClass().getName() == "Service":
            res = Operation
        if res == None and e_object.eClass().getName() == "SystemComponent":
            if e_object.isActor():
                res = SystemActor
            elif is_system(e_object):
                res = System
        if res == None and e_object.eClass().getName() in ["BooleanPropertyValue", "EnumerationPropertyValue", "FloatPropertyValue", "IntegerPropertyValue", "StringPropertyValue"]:
            res = PropertyValue
        if res == None and e_object.eClass().getName() in ["ChoicePseudoState", "DeepHistoryPseudoState", "EntryPointPseudoState", "ExitPointPseudoState", "ForkPseudoState", "InitialPseudoState", "JoinPseudoState", "ShallowHistoryPseudoState", "TerminatePseudoState"]:
            res = Pseudostate
        if res == None and e_object.eClass().getName() == "FinalState":
            res = State
        if res == None and e_object.eClass().getName() == "Exception":
            res = CapellaException
        if res == None and e_object.eClass().getName() in ["StringValueAttribute", "IntegerValueAttribute", "EnumerationValueAttribute", "BooleanValueAttribute", "RealValueAttribute"]:
            if hasattr(sys.modules["__main__"], "Attribute"):
                res = getattr(sys.modules["__main__"], "Attribute")
            else:
                raise AttributeError("you need to import requirement.py to use StringValueAttribute, IntegerValueAttribute, EnumerationValueAttribute, BooleanValueAttribute, RealValueAttribute")
        return res
    @staticmethod
    def copy_e_object(e_object: EObject) -> EObject:
        """
        """
        return e_object.__class__(copy_e_object(e_object.get_java_object()))
    @staticmethod
    def copy_all_e_objects(e_objects: List[EObject]) -> List[EObject]:
        """
        """
        e_objs = []
        for  element in e_objects:
            e_objs.append(element.get_java_object());
        return copy_all_e_objects(e_objs)
    @staticmethod
    def delete_e_object(e_object: EObject):
        """
        """
        """
        """
        delete_e_object(e_object.get_java_object())
    @staticmethod
    def delete_all_e_objects(e_objects: List[EObject]):
        """
        """
        """
        """
        e_objs = []
        for  element in e_objects:
            e_objs.append(element.get_java_object());
        delete_all_e_objects(e_objs)
    def get_owned_diagrams(self) -> List[Diagram]:
        """
        Returns: Diagram[*]
        """
        return Sirius.get_representation_descriptors(self.get_java_object())
    def get_element_of_interest_for_diagrams(self) -> List[Diagram]:
        """
        Returns: Diagram[*]
        """
        return capella_query_by_name(self, "Element of Interest for Diagram", Diagram)
    def get_contextual_element_for_diagrams(self) -> List[Diagram]:
        """
        Returns: Diagram[*]
        """
        return Sirius.get_contextual_element_for_diagrams(self.get_java_object())
    def get_representing_diagrams(self) -> List[Diagram]:
        """
        Returns: Diagram[*]
        """
        return Sirius.get_representing_diagrams(self.get_java_object())
    def get__r_e_cs(self) -> List[REC]:
        """
        Returns: REC[*]
        """
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicableElements", self)
    def get__r_p_ls(self) -> List[RPL]:
        """
        Returns: RPL[*]
        """
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicas", self)
    def get_label(self) -> str:
        """
        Returns: String
        """
        return get_label(self)
    def get_element_type(self) -> str:
        """
        Returns: String
        """
        raise AttributeError("TODO")
    def get_container(self) -> EObject:
        """
        Returns: EObject
        """
        value = self.get_java_object().eContainer()
        if value is not None:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                return specific_cls(value)
        return None
    def get_container_by_type(self, cls: type) -> EObject:
        """
        Parameters: cls: PythonClass
        Returns: EObject
        """
        value = self.get_container()
        while value is not None and not isinstance(value, cls):
            value = value.get_container()
        return value
    def get_contents(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for value in self.get_java_object().eContents():
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                res.append(specific_cls(value))
        return res
    def get_all_contents(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return e_all_contents(self.get_java_object())
    def get_all_contents_by_type(self, cls: type) -> List[EObject]:
        """
        Parameters: cls: PythonClass
        Returns: EObject[*]
        """
        res = []
        for value in e_all_contents_by_type(self.get_java_object(), cls):
            if isinstance(value, cls):
                res.append(value)
        return res
    def get_available_s_b_queries(self) -> List[str]:
        """
        Returns: String[*]
        """
        return available_query_names(self)
    def get_query_result(self, name, cls = None) -> List[EObject]:
        """
        Parameters: queryName: String
        Returns: EObject[0..1]
        """
        return capella_query_by_name(self, name, cls)

class CapellaElement(EObject):
    """
    Java class: org.polarsys.capella.core.data.capellacore.CapellaElement
    A generic Capella model Element. Used to define generic attributes and relations inherited by most Capella elements
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "CapellaElement")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaElement):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_id(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getId()
    def set_id(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setId(value)
    def get_sid(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getSid()
    def set_sid(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setSid(value)
    def get_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getName()
    def set_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setName(value)
    def get_summary(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getSummary()
    def set_summary(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setSummary(value)
    def get_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDescription()
    def set_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDescription(value)
    def get_status(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getStatus()
        if value is None:
            return value
        else:
            return value.getName()
    def get_review(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getReview()
    def set_review(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setReview(value)
    def get_visible_in_documentation(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isVisibleInDoc()
    def set_visible_in_documentation(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setVisibleInDoc(value)
    def get_visible_for_traceability(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isVisibleInLM()
    def set_visible_for_traceability(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setVisibleInLM(value)
    def get_owned_constraints(self) -> List[Constraint]:
        """
        Returns: Constraint[*]
        """
        return create_e_list(self.get_java_object().getOwnedConstraints(), Constraint)
    def get_constraints(self) -> List[Constraint]:
        """
        Returns: Constraint[*]
        """
        return create_e_list(self.get_java_object().getConstraints(), Constraint)
    def get_owned_property_values(self) -> List[PropertyValue]:
        """
        Returns: PropertyValue[*]
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValues(), PropertyValue)
    def get_applied_property_values(self) -> List[PropertyValue]:
        """
        Returns: PropertyValue[*]
        """
        return create_e_list(self.get_java_object().getAppliedPropertyValues(), PropertyValue)
    def get_owned_property_value_groups(self) -> List[PropertyValueGroup]:
        """
        Returns: PropertyValueGroup[*]
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValueGroups(), PropertyValueGroup)
    def get_applied_property_value_groups(self) -> List[PropertyValueGroup]:
        """
        Returns: PropertyValueGroup[*]
        """
        return create_e_list(self.get_java_object().getAppliedPropertyValueGroups(), PropertyValueGroup)
    def get_owned_enumeration_property_types(self) -> List[EnumerationPropertyType]:
        """
        Returns: EnumerationPropertyType[*]
        """
        return create_e_list(self.get_java_object().getOwnedEnumerationPropertyTypes(), EnumerationPropertyType)

class Constraint(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacore.Constraint
    A generic constraint which can be defined on Capella elements
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "Constraint")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Constraint):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_specification(self) -> str:
        """
        Returns: String
        """
        value = self.get_java_object().getOwnedSpecification()
        if get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "OpaqueExpression").isInstance(value):
            for body in value.getBodies():
                return body
            return None
        else:
            return None
    def set_specification(self, value: str):
        """
        Parameters: value: String
        """
        spec = self.get_java_object().getOwnedSpecification()
        if spec is None:
            spec = create("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "OpaqueExpression")
        elif not get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "OpaqueExpression").isInstance(spec):
            raise AttributeError("can only edit OpaqueExpression")
        if not spec.getBodies().isEmpty():
            spec.getBodies().clear()
        spec.getBodies().add(value)
    def get_constrained_elements(self):
        """
        Returns: CapellaElement[*]
        """
        return capella_query_by_name(self, "Constrained Elements")

class PropertyValue(CapellaElement):
    """
    A generic property with a name and value&nbsp;which can be added to Capella elements
    """
    def __init__(self, java_object = None, kind = "StringPropertyValue"):
        """
        """
        if java_object is None:
            if kind in ["BooleanPropertyValue", "EnumerationPropertyValue", "FloatPropertyValue", "IntegerPropertyValue", "StringPropertyValue" ]:
                JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), kind))
            else:
                raise ValueError("kind must be either \"BooleanPropertyValue\", \"EnumerationPropertyValue\", \"FloatPropertyValue\", \"IntegerPropertyValue\", or \"StringPropertyValue\"")
        elif isinstance(java_object, PropertyValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "AbstractPropertyValue").isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        return self.java_object.eClass().getName()
    def get_value(self) -> Any:
        """
        Returns: String
        """
        if self.java_object.eClass().getName() == "BooleanPropertyValue":
            return self.get_java_object().isValue()
        else:
            return self.get_java_object().getValue()
    def set_value(self, value: Any):
        """
        Parameters: value: String
        """
        self.get_java_object().setValue(value)
    def get_valued_elements(self) -> List[CapellaElement]:
        """
        Returns: CapellaElement[*]
        """
        return create_e_list(self.get_java_object().getValuedElements(), CapellaElement)
    def get_type(self) -> EnumerationPropertyType:
        """
        Returns: EnumerationPropertyType[0..1]
        """
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class PropertyValueGroup(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacore.PropertyValueGroup
    A group which can contain several PropertyValue and be applied to CapellaElements
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValueGroup")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PropertyValueGroup):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_valued_elements(self):
        """
        Returns: CapellaElement[*]
        """
        return capella_query_by_name(self, "Valued Elements")

class EnumerationPropertyType(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacore.EnumerationPropertyType
    The definition of an Enumeration to type a PropertyValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumerationPropertyType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_literals(self) -> List[EnumerationPropertyLiteral]:
        """
        Returns: EnumerationPropertyLiteral[*]
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationPropertyLiteral)

class EnumerationPropertyLiteral(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacore.EnumerationPropertyLiteral
    A value defined in an EnumerationPropertyType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyLiteral")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumerationPropertyLiteral):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class PropertyValuePkgContainer(CapellaElement):
    """
    An abstract type to define all elements which can contain PropertyValuePkg
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PropertyValuePkgContainer):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_property_value_pkgs(self) -> List[PropertyValuePkg]:
        """
        Returns: PropertyValuePkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValuePkgs(), PropertyValuePkg)

class Diagram(JavaObject):
    """
    A generic Capella diagram
    """
    e_class = get_e_classifier("http://www.eclipse.org/sirius/1.1.0", "DRepresentationDescriptor")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Diagram):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_uid(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getUid()
    def set_uid(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setUid(value)
    def get_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getName()
    def set_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setName(value)
    def get_type(self) -> str:
        """
        Returns: String
        """
        if self.get_java_object().getDescription() is None:
            return None
        else:
            return self.get_java_object().getDescription().getName()
    def get_package(self) -> str:
        """
        Returns: String
        """
        return Sirius.get_package(self.get_java_object())
    def get_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDocumentation()
    def set_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDocumentation(value)
    def get_status(self) -> str:
        """
        Returns: String
        """
        value = Sirius.get_status(self.get_java_object())
        if value is None:
            return value
        else:
            return value.getName()
    def get_review(self) -> str:
        """
        Returns: String
        """
        return Sirius.get_review(self.get_java_object())
    def get_visible_in_documentation(self) -> bool:
        """
        Returns: Boolean
        """
        return Sirius.is_visible_in_documentation(self.get_java_object())
    def get_visible_for_traceability(self) -> bool:
        """
        Returns: Boolean
        """
        return Sirius.is_visible_for_traceability(self.get_java_object())
    def get_synchronized(self) -> bool:
        """
        Returns: Boolean
        """
        return Sirius.is_synchronized(self.get_java_object())
    def get_target(self) -> EObject:
        """
        Returns: EObject
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_represented_elements(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return Sirius.get_represented_elements(self.get_java_object())
    def get_contextual_elements(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToContextualElement", self)
    def get_elements_of_interest(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToElement", self)
    def export_as_image(self, file_path):
        """
        Parameters: filePath: String, format: String
        status: KO
        """
        Sirius.export_image(self.get_java_object(), file_path)

class AbstractReElement(EObject):
    """
    An abstract type to define the generic attributes of REC / RPL and packages&nbsp;elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractReElement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_id(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getId()
    def set_id(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setId(value)
    def get_name(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getName()
    def set_name(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setName(value)

class AbstractCatalogElement(AbstractReElement):
    """
    An abstract type to define the generic attributes and relations&nbsp;of REC / RPL elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractCatalogElement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_decription(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDecription()
    def set_decription(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDecription(value)
    def get_author(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getAuthor()
    def set_author(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setAuthor(value)
    def get_environment(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getEnvironment()
    def set_environment(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setEnvironment(value)
    def get_tags(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getTags()
    def set_tags(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setTags(value)

class REC(AbstractCatalogElement):
    """
    A Record element is the definition of a set of elements to be replicated together
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElement")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setKind(get_enum_literal("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementKind", "REC"))
        elif isinstance(java_object, RPL):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.getKind().getName() == "REC":
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed catalog element is not a REC.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_referenced_elements(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)
    def get_default_replica_compliancy(self) -> CompliancyDefinition:
        """
        Returns: CompliancyDefinition
        """
        value =  self.get_java_object().getDefaultReplicaCompliancy()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_replica_compliancy(self, value: CompliancyDefinition):
        """
        Parameters: value: CompliancyDefinition
        """
        return self.get_java_object().setDefaultReplicaCompliancy(value.get_java_object())
    def get_replicated_elements(self) -> List[RPL]:
        """
        Returns: RPL[*]
        """
        return create_e_list(self.get_java_object().getReplicatedElements(), RPL)

class RPL(AbstractCatalogElement):
    """
    A replay element is the instantiation of a record element
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElement")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setKind(get_enum_literal("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementKind", "RPL"))
        elif isinstance(java_object, RPL):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.getKind().getName() == "RPL":
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed catalog element is not a RPL.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_referenced_elements(self) -> List[EObject]:
        """
        Returns: EObject[*]
        """
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)
    def get_suffix(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getSuffix()
    def set_suffix(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setSuffix(value)
    def get_read_only(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isReadOnly()
    def set_read_only(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setReadOnly(value)
    def get_origin(self) -> REC:
        """
        Returns: REC
        """
        value =  self.get_java_object().getOrigin()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_origin(self, value: REC):
        """
        Parameters: value: REC
        """
        return self.get_java_object().setOrigin(value.get_java_object())
    def get_current_compliancy(self) -> CompliancyDefinition:
        """
        Returns: CompliancyDefinition
        """
        value =  self.get_java_object().getCurrentCompliancy()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_current_compliancy(self, value: CompliancyDefinition):
        """
        Parameters: value: CompliancyDefinition
        """
        return self.get_java_object().setCurrentCompliancy(value.get_java_object())

class CatalogElementPkg(AbstractReElement):
    """
    Java class: org.polarsys.capella.common.re.CatalogElementPkg
    A package to structure the definition of REC / RPL elements
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CatalogElementPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_element_pkgs(self) -> List[CatalogElementPkg]:
        """
        Returns: CatalogElementPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedElementPkgs(), CatalogElementPkg)
    def get_owned_recs(self) -> List[REC]:
        """
        Returns: REC[*]
        """
        return create_e_list(self.get_java_object().getOwnedRecs(), REC)
    def get_owned_rpls(self) -> List[RPL]:
        """
        Returns: RPL[*]
        """
        return create_e_list(self.get_java_object().getOwnedRpls(), RPL)

class RecCatalog(CatalogElementPkg):
    """
    Java class: org.polarsys.capella.common.re.RecCatalog
    The root package which contains the REC / RPL definitions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "RecCatalog")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, RecCatalog):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_compliancy_definition_pkg(self) -> CompliancyDefinitionPkg:
        """
        Returns: CompliancyDefinitionPkg
        """
        value =  self.get_java_object().getOwnedCompliancyDefinitionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class CompliancyDefinitionPkg(AbstractReElement):
    """
    Java class: org.polarsys.capella.common.re.CompliancyDefinitionPkg
    A package to contain CompliancyDefinitions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinitionPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CompliancyDefinitionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_definitions(self) -> List[CompliancyDefinition]:
        """
        Returns: CompliancyDefinition[*]
        """
        return create_e_list(self.get_java_object().getOwnedDefinitions(), CompliancyDefinition)

class CompliancyDefinition(AbstractReElement):
    """
    Java class: org.polarsys.capella.common.re.CompliancyDefinition
    The type of compliancy which have to be respected by the RPL regarding its REC definition. Default list of compliancies is:
    BLACK_BOX
    CONSTRAINT_REUSE
    INHERITANCY_REUSE
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinition")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CompliancyDefinition):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDescription()
    def set_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDescription(value)

class OperationalAnalysis(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalAnalysis
    The element containing all definitions from the Operational Analysis.
    The Operational Analysis aims at defining what the users of the system need to accomplish
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalAnalysis")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalAnalysis):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_operational_activity_pkg(self) -> OperationalActivityPkg:
        """
        Returns: OperationalActivityPkg
        """
        value =  self.get_java_object().getContainedOperationalActivityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_operational_capability_pkg(self) -> OperationalCapabilityPkg:
        """
        Returns: OperationalCapabilityPkg
        """
        value =  self.get_java_object().getContainedOperationalCapabilityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self) -> InterfacePkg:
        """
        Returns: InterfacePkg
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self) -> DataPkg:
        """
        Returns: DataPkg
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_entity_pkg(self) -> EntityPkg:
        """
        Returns: EntityPkg
        """
        value =  self.get_java_object().getOwnedEntityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class OperationalActivityPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalActivityPkg
    A package to contain OperationalActivity
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivityPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalActivityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_operational_activity_pkgs(self) -> List[OperationalActivityPkg]:
        """
        Returns: OperationalActivityPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_owned_operational_activities(self) -> List[OperationalActivity]:
        """
        Returns: OperationalActivity[*]
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivities(), OperationalActivity)

class OperationalProcess(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalProcess
    An operational process is used to describe a particular context for performing operational activities to contribute to one or more operational capabilities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalProcess")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalProcess):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_involved_operational_activities(self) -> List[OperationalActivity]:
        """
        Returns: OperationalActivity[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for involved_element in self.get_java_object().getInvolvedElements():
            specific_cls = e_object_class.get_class(involved_element)
            if specific_cls is not None and specific_cls.__name__ == "OperationalActivity":
                res.append(specific_cls(involved_element))
        return res
    def get_involved_interactions(self) -> List[Interaction]:
        """
        Returns: Interaction[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for involved_element in self.get_java_object().getInvolvedElements():
            specific_cls = e_object_class.get_class(involved_element)
            if specific_cls is not None and specific_cls.__name__ == "FunctionalExchange":
                res.append(Interaction(involved_element))
        return res
    def get_involved_operational_processes(self):
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Involved Operational Processes")
    def get_pre_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_available_in_states(self) -> List[State]:
        """
        Returns: State[*]
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involving_operational_capabilities(self) -> List[OperationalCapability]:
        """
        Returns: OperationalCapability[*]
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_realizing_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getRealizingFunctionalChains(), FunctionalChain)

class OperationalCapabilityPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalCapabilityPkg
    A package to contain OperationalCapabilities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapabilityPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalCapabilityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_operational_capability_pkgs(self) -> List[OperationalCapabilityPkg]:
        """
        Returns: OperationalCapabilityPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilityPkgs(), OperationalCapabilityPkg)
    def get_owned_operational_capabilities(self) -> List[OperationalCapability]:
        """
        Returns: OperationalCapability[*]
        """
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilities(), OperationalCapability)

class EntityPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.oa.EntityPkg
    A package to define Operational entities / actors
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "EntityPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EntityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_entity_pkgs(self) -> List[EntityPkg]:
        """
        Returns: EntityPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedEntityPkgs(), EntityPkg)
    def get_owned_entities(self) -> List[OperationalActor]:
        """
        Returns: OperationalActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalActor)

class OperationalActor(CapellaElement):
    """
    An Operational Actor is a kind of Operational Entity, usually human. It cannot be broken down
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "Entity")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, OperationalEntity):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed entity is not an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_incoming_communication_means(self) -> List[CommunicationMean]:
        """
        Returns: CommunicationMean[*]
        """
        return create_e_list(self.get_java_object().getIncomingCommunicationMeans(), CommunicationMean)
    def get_outgoing_communication_means(self) -> List[CommunicationMean]:
        """
        Returns: CommunicationMean[*]
        """
        return create_e_list(self.get_java_object().getOutgoingCommunicationMeans(), CommunicationMean)
    def get_allocated_operational_activities(self) -> List[OperationalActivity]:
        """
        Returns: OperationalActivity[*]
        """
        return create_e_list(self.get_java_object().getAllocatedOperationalActivities(), OperationalActivity)
    def get_involving_operational_capabilities(self) -> List[OperationalCapability]:
        """
        Returns: OperationalCapability[*]
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_owned_state_machines(self) -> List[StateMachine]:
        """
        Returns: StateMachine[*]
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_realizing_system_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        return create_e_list(self.get_java_object().getRealizingSystemActors(), SystemActor)

class CommunicationMean(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.oa.CommunicationMean
    Describes the media between the Operational Entities / Actors&nbsp;to support the Operational Interactions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "CommunicationMean")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CommunicationMean):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source_entity(self) -> OperationalActor:
        """
        Returns: OperationalActor
        """
        value =  self.get_java_object().getSourceEntity()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source_entity(self, value: OperationalActor):
        """
        Parameters: value: OperationalActor
        """
        return self.get_java_object().setSourceEntity(value.get_java_object())
    def get_target_entity(self) -> OperationalActor:
        """
        Returns: OperationalActor
        """
        value =  self.get_java_object().getTargetEntity()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target_entity(self, value: OperationalActor):
        """
        Parameters: value: OperationalActor
        """
        return self.get_java_object().setTargetEntity(value.get_java_object())
    def get_allocated_interactions(self):
        """
        Returns: Interaction[*]
        """
        return capella_query_by_name(self, "Allocated Interactions")
    def get_convoyed_informations(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_realizing_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getRealizingComponentExchanges(), ComponentExchange)

class SystemAnalysis(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.ctx.SystemAnalysis
    The element containing all definitions from the System Analysis.
    The System Analysis aims at defining what the system has to accomplish for the users
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemAnalysis")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SystemAnalysis):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_system_function_pkg(self) -> SystemFunctionPkg:
        """
        Returns: SystemFunctionPkg
        """
        value =  self.get_java_object().getContainedSystemFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_pkg(self) -> CapabilityPkg:
        """
        Returns: CapabilityPkg
        """
        value =  self.get_java_object().getContainedCapabilityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self) -> InterfacePkg:
        """
        Returns: InterfacePkg
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self) -> DataPkg:
        """
        Returns: DataPkg
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_system_component_pkg(self) -> SystemComponentPkg:
        """
        Returns: SystemComponentPkg
        """
        value =  self.get_java_object().getOwnedSystemComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_mission_pkg(self) -> MissionPkg:
        """
        Returns: MissionPkg
        """
        value =  self.get_java_object().getOwnedMissionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_system(self) -> System:
        """
        Returns: System
        """
        value =  self.get_java_object().getSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class SystemFunctionPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.ctx.SystemFunctionPkg
    A package to contain SystemFunctions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunctionPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SystemFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_system_function_pkgs(self) -> List[SystemFunctionPkg]:
        """
        Returns: SystemFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_owned_system_functions(self) -> List[SystemFunction]:
        """
        Returns: SystemFunction[*]
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctions(), SystemFunction)
    def get_owned_categories(self) -> List[ExchangeCategory]:
        """
        Returns: ExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class CapabilityPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.ctx.CapabilityPkg
    A package to contain Capabilities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "CapabilityPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapabilityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_capability_pkgs(self) -> List[CapabilityPkg]:
        """
        Returns: CapabilityPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityPkgs(), CapabilityPkg)
    def get_owned_capabilities(self) -> List[Capability]:
        """
        Returns: Capability[*]
        """
        return create_e_list(self.get_java_object().getOwnedCapabilities(), Capability)

class SystemComponentPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.ctx.SystemComponentPkg
    A package to contain the System and the Actors
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponentPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SystemComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_system_component_pkgs(self) -> List[SystemComponentPkg]:
        """
        Returns: SystemComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedSystemComponentPkgs(), SystemComponentPkg)
    def get_owned_system(self) -> System:
        """
        Returns: System
        """
        value =  self.get_java_object().getOwnedSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_owned_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)
    def get_owned_component_exchange_categories(self) -> List[ComponentExchangeCategory]:
        """
        Returns: ComponentExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self) -> List[PhysicalLinkCategory]:
        """
        Returns: PhysicalLinkCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class MissionPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.ctx.MissionPkg
    A package to contain Missions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "MissionPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, MissionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_mission_pkgs(self) -> List[MissionPkg]:
        """
        Returns: MissionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedMissionPkgs(), MissionPkg)
    def get_owned_missions(self) -> List[Mission]:
        """
        Returns: Mission[*]
        """
        return create_e_list(self.get_java_object().getOwnedMissions(), Mission)

class Mission(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.ctx.Mission
    High-level goal to which the System should contribute. To be fulfilled, a Mission should use a number of system Functions regrouped within one or more Capabilities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Mission")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Mission):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_exploited_capabilities(self):
        """
        Returns: Capability[*]
        """
        return capella_query_by_name(self, "Exploited Capabilities")
    def get_involved_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for system_comp in self.get_java_object().getInvolvedSystemComponents():
            if system_comp is not None:
                specific_cls = e_object_class.get_class(system_comp)
                if specific_cls is not None and specific_cls.__name__.endswith('Actor'):
                    res.append(specific_cls(system_comp))
        return res

class LogicalArchitecture(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.la.LogicalArchitecture
    The element containing all definitions from the Logical Architecture.
    The Logical Architecture (or conceptual solution)&nbsp;aims at defining how the system will work in order to fulfil expectations
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalArchitecture")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_logical_function_pkg(self) -> LogicalFunctionPkg:
        """
        Returns: LogicalFunctionPkg
        """
        value =  self.get_java_object().getContainedLogicalFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_realization_pkg(self) -> CapabilityRealizationPkg:
        """
        Returns: CapabilityRealizationPkg
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self) -> InterfacePkg:
        """
        Returns: InterfacePkg
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self) -> DataPkg:
        """
        Returns: DataPkg
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_logical_component_pkg(self) -> LogicalComponentPkg:
        """
        Returns: LogicalComponentPkg
        """
        value =  self.get_java_object().getOwnedLogicalComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_logical_system(self) -> LogicalSystem:
        """
        Returns: LogicalSystem
        """
        value =  self.get_java_object().getSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class LogicalFunctionPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.la.LogicalFunctionPkg
    A package to contain LogicalFunctions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunctionPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_logical_function_pkgs(self) -> List[LogicalFunctionPkg]:
        """
        Returns: LogicalFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_owned_logical_functions(self) -> List[LogicalFunction]:
        """
        Returns: LogicalFunction[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctions(), LogicalFunction)
    def get_owned_categories(self) -> List[ExchangeCategory]:
        """
        Returns: ExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class CapabilityRealizationPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.la.CapabilityRealizationPkg
    A package to contain CapabilityRealizations
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealizationPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapabilityRealizationPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_capability_realization_pkgs(self) -> List[CapabilityRealizationPkg]:
        """
        Returns: CapabilityRealizationPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizationPkgs(), CapabilityRealizationPkg)
    def get_owned_capability_realizations(self) -> List[CapabilityRealization]:
        """
        Returns: CapabilityRealization[*]
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizations(), CapabilityRealization)

class LogicalComponentPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.la.LogicalComponentPkg
    A package to contain the LogicalSystem, LogicalComponents and LogicalActors
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponentPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_logical_component_pkgs(self) -> List[LogicalComponentPkg]:
        """
        Returns: LogicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_owned_logical_system(self) -> LogicalSystem:
        """
        Returns: LogicalSystem
        """
        value =  self.get_java_object().getOwnedLogicalSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_owned_logical_actors(self) -> List[LogicalActor]:
        """
        Returns: LogicalActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_components(self) -> List[LogicalComponent]:
        """
        Returns: LogicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_component_exchange_categories(self) -> List[ComponentExchangeCategory]:
        """
        Returns: ComponentExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self) -> List[PhysicalLinkCategory]:
        """
        Returns: PhysicalLinkCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class PhysicalArchitecture(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.pa.PhysicalArchitecture
    The element containing all definitions from the Physical Architecture.
    The Physical Architecture (or finalized solution)&nbsp;aims at defining how the system will be developed and built
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalArchitecture")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_physical_function_pkg(self) -> PhysicalFunctionPkg:
        """
        Returns: PhysicalFunctionPkg
        """
        value =  self.get_java_object().getContainedPhysicalFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_realization_pkg(self) -> CapabilityRealizationPkg:
        """
        Returns: CapabilityRealizationPkg
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self) -> InterfacePkg:
        """
        Returns: InterfacePkg
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self) -> DataPkg:
        """
        Returns: DataPkg
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_physical_component_pkg(self) -> PhysicalComponentPkg:
        """
        Returns: PhysicalComponentPkg
        """
        value =  self.get_java_object().getOwnedPhysicalComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_physical_system(self) -> PhysicalSystem:
        """
        Returns: PhysicalSystem
        """
        return self.get_physical_component_pkg().get_owned_physical_system()

class PhysicalFunctionPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.pa.PhysicalFunctionPkg
    A package to contain PhysicalFunctions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunctionPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_physical_function_pkgs(self) -> List[PhysicalFunctionPkg]:
        """
        Returns: PhysicalFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_owned_physical_functions(self) -> List[PhysicalFunction]:
        """
        Returns: PhysicalFunction[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctions(), PhysicalFunction)
    def get_owned_categories(self) -> List[ExchangeCategory]:
        """
        Returns: ExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class PhysicalComponentPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.pa.PhysicalComponentPkg
    A package to contain the PhysicalSystem, PhysicalComponents and PhysicalActors
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_physical_component_pkgs(self) -> List[PhysicalComponentPkg]:
        """
        Returns: PhysicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_owned_physical_system(self) -> PhysicalSystem:
        """
        Returns: PhysicalSystem
        """
        for value in self.get_owned_physical_components():
            if isinstance(value, PhysicalSystem):
                return value
        return None
    def get_owned_physical_actors(self) -> List[PhysicalActor]:
        """
        Returns: PhysicalActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_components(self) -> List[PhysicalComponent]:
        """
        Returns: PhysicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_component_exchange_categories(self) -> List[ComponentExchangeCategory]:
        """
        Returns: ComponentExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self) -> List[PhysicalLinkCategory]:
        """
        Returns: PhysicalLinkCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class AbstractPhysicalArtifact(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.cs.AbstractPhysicalArtifact
    An abstract type to defined the relation between elements of the Physical Architecture and ConfigurationItems
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "AbstractPhysicalArtifact")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractPhysicalArtifact):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_allocator_configuration_items(self) -> List[ConfigurationItem]:
        """
        Returns: ConfigurationItem[*]
        """
        return create_e_list(self.get_java_object().getAllocatorConfigurationItems(), ConfigurationItem)

class PhysicalComponent(AbstractPhysicalArtifact):
    """
    Java class: org.polarsys.capella.core.data.pa.PhysicalComponent
    A generic Physical Component which can be either a BehaviorPC or a NodePC
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalComponent):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if not java_object.isActor():
                if java_object.getNature().getName() == "UNSET":
                    JavaObject.__init__(self, java_object)
                elif java_object.getNature().getName() == "BEHAVIOR":
                    raise AttributeError("Passed component is a behavior physical component.")
                elif java_object.getNature().getName() == "NODE":
                    raise AttributeError("Passed component is a node physical component.")
            else:
                raise AttributeError("Passed component is an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self):
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            return value.getName()
    def set_kind(self, value):
        """
        Parameters: value: String
        """
        self.get_java_object().setKind(get_enum_literal("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentKind", value))
    def get_owned_physical_components(self) -> List[PhysicalComponent]:
        """
        Returns: PhysicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self) -> List[PhysicalComponentPkg]:
        """
        Returns: PhysicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_is_human(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setHuman(value)
    def get_involving_capability_realizations(self) -> List[CapabilityRealization]:
        """
        Returns: CapabilityRealization[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)
    def get_deployed_physical_components(self):
        """
        Returns: PhysicalComponent[*]
        """
        return capella_query_by_name(self, "Deployed Physical Components")
    def get_allocated_physical_functions(self):
        """
        Returns: PhysicalFunction[*]
        """
        return capella_query_by_name(self, "Allocated Physical Functions")

class EPBSArchitecture(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.epbs.EPBSArchitecture
    The element containing all definitions from the End-Product Breakdown Structure.
    The End-Product Breakdown Structure aims at defining the construction strategy of the product, taking into account industrial and subcontracting constraints
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "EPBSArchitecture")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EPBSArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_capability_realization_pkg(self) -> CapabilityRealizationPkg:
        """
        Returns: CapabilityRealizationPkg
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_configuration_item_pkg(self) -> ConfigurationItemPkg:
        """
        Returns: ConfigurationItemPkg
        """
        value =  self.get_java_object().getOwnedConfigurationItemPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self) -> DataPkg:
        """
        Returns: DataPkg
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class ConfigurationItemPkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.epbs.ConfigurationItemPkg
    A package to contain ConfigurationItems
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItemPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ConfigurationItemPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_configuration_item_pkgs(self) -> List[ConfigurationItemPkg]:
        """
        Returns: ConfigurationItemPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_owned_configuration_items(self) -> List[ConfigurationItem]:
        """
        Returns: ConfigurationItem[*]
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)

class ConfigurationItem(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.epbs.ConfigurationItem
    System part to be acquired or produced, in as many copies as the physical architecture requires
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItem")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ConfigurationItem):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_item_identifier(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getItemIdentifier()
    def set_item_identifier(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setItemIdentifier(value)
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_owned_configuration_items(self) -> List[ConfigurationItem]:
        """
        Returns: ConfigurationItem[*]
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self) -> List[ConfigurationItemPkg]:
        """
        Returns: ConfigurationItemPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_allocated_physical_artifacts(self) -> List[AbstractPhysicalArtifact]:
        """
        Returns: AbstractPhysicalArtifact[*]
        """
        return create_e_list(self.get_java_object().getAllocatedPhysicalArtifacts(), AbstractPhysicalArtifact)

class StateMachine(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.StateMachine
    State Machine is a way to define some of&nbsp;the expected behavior of the System, a Component or an external Actor
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateMachine")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, StateMachine):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_regions(self) -> List[Region]:
        """
        Returns: Region[*]
        """
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)

class AbstractState(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.AbstractState
    An abstract type to define the generic relation of modes and states
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "AbstractState")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractState):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_incoming(self) -> List[StateTransition]:
        """
        Returns: StateTransition[*]
        """
        return create_e_list(self.get_java_object().getIncoming(), StateTransition)
    def get_outgoing(self) -> List[StateTransition]:
        """
        Returns: StateTransition[*]
        """
        return create_e_list(self.get_java_object().getOutgoing(), StateTransition)
    def get_realized_states(self) -> List[AbstractState]:
        """
        Returns: AbstractState[*]
        """
        return create_e_list(self.get_java_object().getRealizedAbstractStates(), AbstractState)
    def get_realizing_states(self) -> List[AbstractState]:
        """
        Returns: AbstractState[*]
        """
        return create_e_list(self.get_java_object().getRealizingAbstractStates(), AbstractState)

class State(AbstractState):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.State
    A State is a context undergone by the system, an actor or a component in specific circumstances (for example imposed by the environment)
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "State")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, State):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_regions(self) -> List[Region]:
        """
        Returns: Region[*]
        """
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)
    def get_available_activities_functions(self) -> List[AbstractActivityFunction]:
        """
        Returns: AbstractActivityFunction[*]
        """
        return create_e_list(self.get_java_object().getAvailableActivitiesFunctions(), AbstractActivityFunction)
    def get_entry(self) -> List[AbstractEvent]:
        """
        Returns: AbstractEvent[*]
        """
        return create_e_list(self.get_java_object().getEntry(), AbstractEvent)
    def get_do(self) -> List[AbstractEvent]:
        """
        Returns: AbstractEvent[*]
        """
        return create_e_list(self.get_java_object().getDoActivity(), AbstractEvent)
    def get_exit(self) -> List[AbstractEvent]:
        """
        Returns: AbstractEvent[*]
        """
        return create_e_list(self.get_java_object().getExit(), AbstractEvent)
    def get_available_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getAvailableFunctionalChains(), FunctionalChain)
    def get_available_operational_processes(self) -> List[OperationalProcess]:
        """
        Returns: OperationalProcess[*]
        """
        return create_e_list(self.get_java_object().getAvailableOperationalProcesses(), OperationalProcess)
    def get_available_capabilities(self) -> List[AbstractCapability]:
        """
        Returns: AbstractCapability[*]
        """
        return create_e_list(self.get_java_object().getAvailableAbstractCapabilities(), AbstractCapability)

class Mode(State):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.Mode
    A Mode is a behavior expected from the system,&nbsp;an Actor or a component&nbsp;in chosen conditions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "Mode")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Mode):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Pseudostate(AbstractState):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.Pseudostate
    A pseudo states are transitive states (meaning they don't remain active). They are used to define entry / exit point of a state machine, and to connect multiple transitions into more complex transition paths
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "Pseudostate")
    def __init__(self, java_object = None, kind = "InitialPseudoState"):
        """
        """
        if java_object is None:
            if kind in ["ChoicePseudoState", "DeepHistoryPseudoState", "EntryPointPseudoState", "ExitPointPseudoState", "ForkPseudoState", "InitialPseudoState", "JoinPseudoState", "ShallowHistoryPseudoState", "TerminatePseudoState"]:
                JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), kind))
            else:
                raise ValueError("kind must be either \"ChoicePseudoState\", \"DeepHistoryPseudoState\", \"EntryPointPseudoState\", \"ExitPointPseudoState\", \"ForkPseudoState\", \"InitialPseudoState\", \"JoinPseudoState\", \"ShallowHistoryPseudoState\", or \"TerminatePseudoState\"")
        elif isinstance(java_object, Pseudostate):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        return self.java_object.eClass().getName()

class Region(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.Region
    A region is an orthogonal part of either a composite state or a state machine.
    Inside of a region, only one more or state can be active at a time
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "Region")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Region):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_states(self) -> List[AbstractState]:
        """
        Returns: AbstractState[*]
        """
        return create_e_list(self.get_java_object().getOwnedStates(), AbstractState)

class StateTransition(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.StateTransition
    A possible transition between 2 modes or 2 states
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateTransition")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, StateTransition):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_trigger_description(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getTriggerDescription()
    def set_trigger_description(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setTriggerDescription(value)
    def get_source(self):
        """
        Returns: AbstractState
        """
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is None:
                return None
            else:
                return specific_cls(value)
    def get_target(self):
        """
        Returns: AbstractState
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is None:
                return None
            else:
                return specific_cls(value)
    def get_triggers(self) -> List[AbstractEvent]:
        """
        Returns: AbstractEvent[*]
        """
        return create_e_list(self.get_java_object().getTriggers(), AbstractEvent)
    def get_guard(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_guard(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setGuard(value.get_java_object())
    def get_effects(self) -> List[AbstractAction]:
        """
        Returns: AbstractAction[*]
        """
        return create_e_list(self.get_java_object().getEffect(), AbstractAction)
    def get_realized_state_transitions(self) -> List[StateTransition]:
        """
        Returns: StateTransition[*]
        """
        return create_e_list(self.get_java_object().getRealizedStateTransitions(), StateTransition)
    def get_realizing_state_transitions(self) -> List[StateTransition]:
        """
        Returns: StateTransition[*]
        """
        return create_e_list(self.get_java_object().getRealizingStateTransitions(), StateTransition)

class AbstractAction(JavaObject):
    """
    Java class: org.polarsys.capella.common.data.activity.AbstractAction
    A generic action which can be triggered by a Mode / State or a StateTransition
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/activity/" + capella_version(), "AbstractAction")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractAction):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class AbstractEvent(CapellaElement):
    """
    Java class: org.polarsys.capella.common.data.behavior.AbstractEvent
    An generic event which can trigger a transition
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/common/behavior/" + capella_version(), "AbstractEvent")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Scenario(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.Scenario
    A scenario of use of the system defined by a specific sequence
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "Scenario")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Scenario):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_pre_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_instance_roles(self) -> List[InstanceRole]:
        """
        Returns: InstanceRole[*]
        """
        return create_e_list(self.get_java_object().getOwnedInstanceRoles(), InstanceRole)
    def get_owned_messages(self) -> List[SequenceMessage]:
        """
        Returns: SequenceMessage[*]
        """
        return create_e_list(self.get_java_object().getOwnedMessages(), SequenceMessage)
    def get_owned_state_fragments(self) -> List[StateFragment]:
        """
        Returns: StateFragment[*]
        """
        return create_e_list(self.get_java_object().getOwnedStateFragments(), StateFragment)
    def get_owned_combined_fragments(self) -> List[CombinedFragment]:
        """
        Returns: CombinedFragment[*]
        """
        return create_e_list(self.get_java_object().getOwnedCombinedFragments(), CombinedFragment)
    def get_owned_constraint_durations(self) -> List[ConstraintDuration]:
        """
        Returns: ConstraintDuration[*]
        """
        return create_e_list(self.get_java_object().getOwnedConstraintDurations(), ConstraintDuration)
    def get_referenced_scenarios(self) -> List[Scenario]:
        """
        Returns: Scenario[*]
        """
        return create_e_list(self.get_java_object().getReferencedScenarios(), Scenario)
    def get_realized_scenarios(self):
        """
        Returns: Scenario[*]
        """
        return capella_query_by_name(self, "Realized Scenarios")
    def get_realizing_scenarios(self):
        """
        Returns: Scenario[*]
        """
        return capella_query_by_name(self, "Realizing Scenarios")

class InstanceRole(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.InstanceRole
    The involvement of an element (function, system, component or actor)&nbsp;in a scenario
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "InstanceRole")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, InstanceRole):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_represented_instance(self):
        """
        Returns: AbstractInstance
        """
        return capella_query_by_name(self, "Represented Instance")

class AbstractInstance(JavaObject):
    """
    Java class: org.polarsys.capella.core.data.information.AbstractInstance
    A generic element which can be involved in a scenario as an InstanceRole
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "AbstractInstance")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractInstance):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class SequenceMessage(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.SequenceMessage
    An exchange between InstanceRole performed in the frame of a scenario
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "SequenceMessage")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SequenceMessage):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_sending_instance_role(self) -> InstanceRole:
        """
        Returns: InstanceRole
        """
        part =  self.get_java_object().getSendingPart()
        if part is None:
            return part
        else:
            value = part.getType()
            if value is None:
                return value
            else:
                e_object_class = getattr(sys.modules["__main__"], "EObject")
                specific_cls = e_object_class.get_class(value)
                return specific_cls(value)
    def get_receiving_instance_role(self) -> InstanceRole:
        """
        Returns: InstanceRole
        """
        part =  self.get_java_object().getReceivingPart()
        if part is None:
            return part
        else:
            value = part.getType()
            if value is None:
                return value
            else:
                e_object_class = getattr(sys.modules["__main__"], "EObject")
                specific_cls = e_object_class.get_class(value)
                return specific_cls(value)
    def get_invoked_exchange(self) -> AbstractExchange:
        """
        Returns: AbstractExchange[0..1]
        """
        exchanges = capella_query_by_name(self, 'Invoked Interaction', AbstractExchange)
        if not exchanges:
            return None
        else:
            return exchanges[0]
    def get_exchanged_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_invoked_operation(self):
        """
        Returns: ExchangeItemAllocation[0..1]
        """
        return capella_query_by_name(self, "Invoked Operation")
    def get_exchange_context(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getExchangeContext()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class AbstractExchange(JavaObject):
    """
    A generic exchange which can be used in a scenario as a sequence message
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractExchange):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_invoking_sequence_messages(self) -> List[SequenceMessage]:
        """
        Returns: SequenceMessage[*]
        """
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class StateFragment(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.StateFragment
    The call of a function or mode / state&nbsp;by an InstanceRole in the context of a scenario
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "StateFragment")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, StateFragment):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_covered_instance_role(self) -> InstanceRole:
        """
        Returns: InstanceRole
        """
        value =  self.get_java_object().getCoveredInstanceRole()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_related_state(self):
        """
        Returns: State[0..1]
        """
        return capella_query_by_name(self, "Related State")
    def get_related_activity_function(self) -> AbstractActivityFunction:
        """
        Returns: AbstractActivityFunction[0..1]
        """
        value =  self.get_java_object().getRelatedAbstractFunction()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class CombinedFragment(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.CombinedFragment
    The identification of a specific operator (ALT, OPT, LOOP...)&nbsp;in the sequence of a scenario
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "CombinedFragment")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CombinedFragment):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_operator(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getOperator()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_operands(self) -> List[Operand]:
        """
        Returns: Operand[1..*]
        """
        return create_e_list(self.get_java_object().getOperands(), Operand)
    def get_covered_instance_roles(self) -> List[InstanceRole]:
        """
        Returns: InstanceRole[1..*]
        """
        return create_e_list(self.get_java_object().getCoveredInstanceRoles(), InstanceRole)

class Operand(CapellaElement):
    """
    A specific "region" in a Combined Fragment
    For example, an ALTERNATIVE contains one operand for each of the alternative conditions
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "InteractionOperand")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Operand):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_guard(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_guard(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setGuard(value.get_java_object())
    def get_referenced_messages(self) -> List[SequenceMessage]:
        """
        Returns: SequenceMessage[*]
        """
        return create_e_list(self.get_java_object().getReferencedMessages(), SequenceMessage)
    def get_referenced_fragments(self) -> List[StateFragment]:
        """
        Returns: StateFragment[*]
        """
        return create_e_list(self.get_java_object().getReferencedFragments(), StateFragment)

class ConstraintDuration(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.interaction.ConstraintDuration
    A constraint about the execution time of a scenario defined between 2 points
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "ConstraintDuration")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ConstraintDuration):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_duration(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getDuration()
    def set_duration(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setDuration(value)

class Node(AbstractInstance):
    """
    An abstract type defining the generic relation of a Node (implementation ressource)&nbsp;element
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Node):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_physical_ports(self) -> List[PhysicalPort]:
        """
        Returns: PhysicalPort[*]
        """
        return create_e_list(self.get_java_object().getContainedPhysicalPorts(), PhysicalPort)
    def get_physical_links(self) -> List[PhysicalLink]:
        """
        Returns: PhysicalLink[*]
        """
        return create_e_list(self.get_java_object().getInvolvedLinks(), PhysicalLink)
    def get_involving_physical_paths(self) -> List[PhysicalPath]:
        """
        Returns: PhysicalPath[*]
        """
        res = []
        involvements = self.get_java_object().getInvolvingInvolvements()
        physical_path_involvement_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPathInvolvement")
        physical_path_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPath")
        for involvement in involvements:
            if physical_path_involvement_e_class.isInstance(involvement) and physical_path_e_class.isInstance(involvement.getInvolver()):
                res.append(PhysicalPath(involvement.getInvolver()))
        return res
    def get_owned_physical_link_categories(self) -> List[PhysicalLinkCategory]:
        """
        Returns: PhysicalLinkCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)
    def get_owned_physical_paths(self) -> List[PhysicalPath]:
        """
        Returns: PhysicalPath[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalPaths(), PhysicalPath)

class PhysicalPort(AbstractPhysicalArtifact):
    """
    Java class: org.polarsys.capella.core.data.cs.PhysicalPort
    A port on a Node component defining a physical interaction point
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPort")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalPort):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_physical_links(self):
        """
        Returns: PhysicalLink[*]
        """
        return capella_query_by_name(self, "Physical Links")
    def get_allocated_component_ports(self):
        """
        Returns: ComponentPort[*]
        """
        return capella_query_by_name(self, "Allocated Component Ports")
    def get_realized_physical_ports(self) -> List[PhysicalPort]:
        """
        Returns: PhysicalPort[*]
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalPorts(), PhysicalPort)
    def get_realizing_physical_ports(self) -> List[PhysicalPort]:
        """
        Returns: PhysicalPort[*]
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalPorts(), PhysicalPort)

class PhysicalLink(AbstractPhysicalArtifact):
    """
    Java class: org.polarsys.capella.core.data.cs.PhysicalLink
    Means of communication, transport or routing between two Node components, used as a support for behavioral exchanges
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLink")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalLink):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_connected_physical_ports(self) -> List[PhysicalPort]:
        """
        Returns: PhysicalPort[2]
        """
        res = []
        if self.get_java_object().getSourcePhysicalPort() is not None:
            res.append(PhysicalPort(self.get_java_object().getSourcePhysicalPort()))
        if self.get_java_object().getTargetPhysicalPort() is not None:
            res.append(PhysicalPort(self.get_java_object().getTargetPhysicalPort()))
        return res
    def get_categories(self):
        """
        Returns: PhysicalLinkCategory[*]
        """
        return capella_query_by_name(self, "Categories")
    def get_involving_physical_paths(self) -> List[PhysicalPath]:
        """
        Returns: PhysicalPath[*]
        """
        res = []
        involvements = self.get_java_object().getInvolvingInvolvements()
        physical_path_involvement_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPathInvolvement")
        physical_path_e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPath")
        for involvement in involvements:
            if physical_path_involvement_e_class.isInstance(involvement) and physical_path_e_class.isInstance(involvement.getInvolver()):
                res.append(PhysicalPath(involvement.getInvolver()))
        return res
    def get_connected_components(self) -> Node:
        """
        Returns: Node[2]
        """
        return create_e_list(self.get_java_object().getConnectedComponents(), Node)
    def get_allocated_component_exchanges(self):
        """
        Returns: ComponentExchange[*]
        """
        return capella_query_by_name(self, "Allocated Component Exchanges")
    def get_realized_physical_links(self) -> List[PhysicalLink]:
        """
        Returns: PhysicalLink[*]
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalLinks(), PhysicalLink)
    def get_realizing_physical_links(self) -> List[PhysicalLink]:
        """
        Returns: PhysicalLink[*]
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalLinks(), PhysicalLink)

class PhysicalLinkCategory(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.cs.PhysicalLinkCategory
    A regroupement of PhysicalLinks for graphical simplification of diagrams
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLinkCategory")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalLinkCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_links(self) -> List[PhysicalLink]:
        """
        Returns: PhysicalLink[*]
        """
        return create_e_list(self.get_java_object().getLinks(), PhysicalLink)

class PhysicalPath(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.cs.PhysicalPath
    Set of Physical Links defining a continuous path likely to route one or more behavioral exchanges
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPath")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalPath):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_involved_physical_links(self):
        """
        Returns: PhysicalLink[*]
        """
        return capella_query_by_name(self, "Involved Physical Links")
    def get_involved_node_p_cs(self) -> List[Node]:
        """
        Returns: Node[*]
        """
        return create_e_list(self.get_java_object().getInvolvedNodePCs(), Node)
    def get_allocated_component_exchanges(self):
        """
        Returns: ComponentExchange[*]
        """
        return capella_query_by_name(self, "Allocated Component Exchanges")
    def get_realized_physical_paths(self) -> List[PhysicalPath]:
        """
        Returns: PhysicalPath[*]
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalPaths(), PhysicalPath)
    def get_realizing_physical_paths(self) -> List[PhysicalPath]:
        """
        Returns: PhysicalPath[*]
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalPaths(), PhysicalPath)

class InterfacePkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.cs.InterfacePkg
    A package to contain Interfaces
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "InterfacePkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, InterfacePkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_interface_pkgs(self) -> List[InterfacePkg]:
        """
        Returns: InterfacePkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedInterfacePkgs(), InterfacePkg)
    def get_owned_interfaces(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getOwnedInterfaces(), Interface)
    def get_owned_exchange_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getOwnedExchangeItems(), ExchangeItem)

class Interface(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.cs.Interface
    The definition of ExchangeItems which can be send / received by a ComponentPort
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Interface")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Interface):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_owned_exchange_item_allocations(self) -> List[ExchangeItemAllocation]:
        """
        Returns: ExchangeItemAllocation[*]
        """
        return create_e_list(self.get_java_object().getOwnedExchangeItemAllocations(), ExchangeItemAllocation)
    def get_exchange_items(self):
        """
        Returns: ExchangeItem[*]
        """
        return capella_query_by_name(self, "Exchange Items")
    def get_providing_component_ports(self) -> List[ComponentPort]:
        """
        Returns: ComponentPort[*]
        """
        return create_e_list(self.get_java_object().getProvidingComponentPorts(), ComponentPort)
    def get_requiring_component_ports(self) -> List[ComponentPort]:
        """
        Returns: ComponentPort[*]
        """
        return create_e_list(self.get_java_object().getRequiringComponentPorts(), ComponentPort)
    def get_user_components(self) -> List[BehavioralComponent]:
        """
        Returns: BehavioralComponent[*]
        """
        return create_e_list(self.get_java_object().getUserComponents(), BehavioralComponent)
    def get_implementor_components(self) -> List[BehavioralComponent]:
        """
        Returns: BehavioralComponent[*]
        """
        return create_e_list(self.get_java_object().getImplementorComponents(), BehavioralComponent)
    def get_super(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getSuper(), Interface)
    def get_sub(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getSub(), Interface)

class ExchangeItemAllocation(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.cs.ExchangeItemAllocation
    The involvement of an ExchangeItem by an Interface.
    Mainly used for the involvement of ExchangeItems in Interface Scenarios based on the definition of Interfaces between components
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/cs/" + capella_version(), "ExchangeItemAllocation")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ExchangeItemAllocation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_transmission_protocol(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getTransmissionProtocol()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_transmission_protocol(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setTransmissionProtocol(value.get_java_object())
    def get_acquisition_protocol(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getAcquisitionProtocol()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_acquisition_protocol(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setAcquisitionProtocol(value.get_java_object())
    def get_allocated_item(self) -> ExchangeItem:
        """
        Returns: ExchangeItem
        """
        value =  self.get_java_object().getAllocatedItem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocated_item(self, value: ExchangeItem):
        """
        Parameters: value: ExchangeItem
        """
        return self.get_java_object().setAllocatedItem(value.get_java_object())
    def get_invoking_sequence_messages(self) -> List[SequenceMessage]:
        """
        Returns: SequenceMessage[*]
        """
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class ExchangeItem(AbstractAction, AbstractEvent, AbstractInstance):
    """
    Java class: org.polarsys.capella.core.data.information.ExchangeItem
    Ordered set of references to elements carried together during an interaction or exchange between functions, components and actors. The elements are carried simultaneously, in the same conditions, with the same non-functional properties. The “elements” are called data
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItem")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ExchangeItem):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)
    def get_final(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isFinal()
    def set_final(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setFinal(value)
    def get_exchange_mechanism(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getExchangeMechanism()
        if value is None:
            return value
        else:
            return value.getName()
    def set_exchange_mechanism(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setExchangeMechanism(get_enum_literal("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeMechanism", value))
    def get_owned_elements(self) -> List[ExchangeItemElement]:
        """
        Returns: ExchangeItemElement[*]
        """
        return create_e_list(self.get_java_object().getOwnedElements(), ExchangeItemElement)
    def get_allocator_interfaces(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getAllocatorInterfaces(), Interface)
    def get_super(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getSuper(), ExchangeItem)
    def get_sub(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getSub(), ExchangeItem)
    def get_realized_exchange_items(self):
        """
        Returns: ExchangeItem[*]
        """
        return capella_query_by_name(self, "Realized Exchange Items")
    def get_realizing_exchange_items(self):
        """
        Returns: ExchangeItem[*]
        """
        return capella_query_by_name(self, "Realizing Exchange Items")
    def get_realizing_operations(self) -> List[Operation]:
        """
        Returns: Operation[*]
        """
        return create_e_list(self.get_java_object().getRealizingOperations(), Operation)

class ExchangeItemElement(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.ExchangeItemElement
    A part of the information contained by an ExchangeItem
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItemElement")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ExchangeItemElement):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_type(self):
        """
        Returns: DataType
        """
        return capella_query_by_name(self, "Type")

class FunctionPort(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.fa.FunctionPort
    An generic FunctionPort to define the allocation with ComponentPorts
    A Function Port specify what a Function is capable of producing or is requiring
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionPort")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, FunctionPort):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_allocator_component_port(self) -> ComponentPort:
        """
        Returns: ComponentPort[0..1]
        """
        value =  self.get_java_object().getRepresentedComponentPort()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocator_component_port(self, value: ComponentPort):
        """
        Parameters: value: ComponentPort[0..1]
        """
        return self.get_java_object().setRepresentedComponentPort(value.get_java_object())

class FunctionInputPort(FunctionPort):
    """
    Java class: org.polarsys.capella.core.data.fa.FunctionInputPort
    An FunctionInputPort defines what a Function is requiring
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionInputPort")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, FunctionInputPort):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_incoming_functional_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getIncomingFunctionalExchanges(), FunctionalExchange)
    def get_incoming_exchange_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getIncomingExchangeItems(), ExchangeItem)
    def get_realized_function_input_ports(self) -> List[FunctionInputPort]:
        """
        Returns: FunctionInputPort[*]
        """
        return create_e_list(self.get_java_object().getRealizedFunctionInputPorts(), FunctionInputPort)
    def get_realizing_function_input_ports(self) -> List[FunctionInputPort]:
        """
        Returns: FunctionInputPort[*]
        """
        return create_e_list(self.get_java_object().getRealizingFunctionInputPorts(), FunctionInputPort)

class FunctionOutputPort(FunctionPort):
    """
    Java class: org.polarsys.capella.core.data.fa.FunctionOutputPort
    A FunctionOutputPort defines what a Function is capable of producing
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionOutputPort")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, FunctionOutputPort):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_outgoing_functional_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getOutgoingFunctionalExchanges(), FunctionalExchange)
    def get_outgoing_exchange_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getOutgoingExchangeItems(), ExchangeItem)
    def get_realized_function_output_ports(self) -> List[FunctionOutputPort]:
        """
        Returns: FunctionOutputPort[*]
        """
        return create_e_list(self.get_java_object().getRealizedFunctionOutputPorts(), FunctionOutputPort)
    def get_realizing_function_output_ports(self) -> List[FunctionOutputPort]:
        """
        Returns: FunctionOutputPort[*]
        """
        return create_e_list(self.get_java_object().getRealizingFunctionOutputPorts(), FunctionOutputPort)

class FunctionalExchange(AbstractEvent, AbstractExchange):
    """
    Java class: org.polarsys.capella.core.data.fa.FunctionalExchange
    A functional exchange represents a dependency between a source function and a target one. Exchanges connect Function Ports, which specify what a Function is capable of producing or is requiring.
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalExchange")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, FunctionalExchange):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source_port(self) -> FunctionOutputPort:
        """
        Returns: FunctionOutputPort
        """
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source_port(self, value: FunctionOutputPort):
        """
        Parameters: value: FunctionOutputPort
        """
        return self.get_java_object().setSource(value.get_java_object())
    def get_target_port(self) -> FunctionInputPort:
        """
        Returns: FunctionInputPort
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target_port(self, value: FunctionInputPort):
        """
        Parameters: value: FunctionInputPort
        """
        return self.get_java_object().setTarget(value.get_java_object())
    def get_source_function(self) -> Function:
        """
        Returns: Function
        """
        port = self.get_java_object().getSourceFunctionOutputPort()
        if port is None:
            return port
        elif port.eContainer() is not None:
            value = port.eContainer()
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                return specific_cls(value)
            else:
                return None
        else:
            return None
    def get_target_function(self) -> Function:
        """
        Returns: Function
        """
        port =  self.get_java_object().getTargetFunctionInputPort()
        if port is None:
            return port
        elif port.eContainer() is not None:
            value = port.eContainer()
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                return specific_cls(value)
            else:
                return None
        else:
            return None
    def get_exchanged_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_involving_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_categories(self):
        """
        Returns: ExchangeCategory[*]
        """
        return capella_query_by_name(self, "Categories")
    def get_allocating_component_exchange(self):
        """
        Returns: ComponentExchange[0..1]
        """
        return capella_query_by_name(self, "Allocating Component Exchange")
    def get_realized_functional_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getRealizedFunctionalExchanges(), FunctionalExchange)
    def get_realizing_functional_exchanges(self):
        """
        Returns: FunctionalExchange[*]
        """
        return capella_query_by_name(self, "Realizing Functional Exchanges")
    def get_realized_interactions(self):
        """
        Returns: Interaction[*]
        """
        return capella_query_by_name(self, "Realized Interactions")

class ExchangeCategory(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.fa.ExchangeCategory
    A regroupement of FunctionalExchanges for graphical simplification of diagrams
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ExchangeCategory")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ExchangeCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getExchanges(), FunctionalExchange)

class FunctionalChain(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.fa.FunctionalChain
    Describe the system behaviour in a particular usage context with references towards Functions and Functional Exchanges
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChain")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, FunctionalChain):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_pre_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self) -> Constraint:
        """
        Returns: Constraint[0..1]
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value: Constraint):
        """
        Parameters: value: Constraint[0..1]
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_involved_functions(self) -> List[Function]:
        """
        Returns: Function[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for involvment in self.get_java_object().getOwnedFunctionalChainInvolvements():
            if involvment.eClass().getName() == 'FunctionalChainInvolvementFunction':
                involvedElement = involvment.getInvolvedElement()
                if involvedElement is not None:
                    specific_cls = e_object_class.get_class(involvedElement)
                    res.append(specific_cls(involvedElement))
        return res
    def get_involved_functional_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getInvolvedFunctionalExchanges(), FunctionalExchange)
    def get_involved_functional_chains(self):
        """
        Returns: FunctionalChain[*]
        """
        return capella_query_by_name(self, "Involved Functional Chains")
    def get_involving_capabilities(self):
        """
        Returns: AbstractSystemCapability[*]
        """
        return capella_query_by_name(self, "Involving Capabilities")
    def get_available_in_states(self) -> List[State]:
        """
        Returns: State[*]
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_realized_operational_processes(self):
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Realized Operational Processes")
    def get_realized_functional_chains(self):
        """
        Returns: FunctionalChain[*]
        """
        return capella_query_by_name(self, "Realized Functional Chains")
    def get_realizing_functional_chains(self):
        """
        Returns: FunctionalChain[*]
        """
        return capella_query_by_name(self, "Realizing Functional Chains")

class BehavioralComponent(CapellaElement, AbstractInstance):
    """
    An abstract type to define the generic relation of behavioral elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, BehavioralComponent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_component_ports(self) -> List[ComponentPort]:
        """
        Returns: ComponentPort[*]
        """
        return create_e_list(self.get_java_object().getContainedComponentPorts(), ComponentPort)
    def get_incoming_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getIncomingComponentExchanges(), ComponentExchange)
    def get_outgoing_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getOutgoingComponentExchanges(), ComponentExchange)
    def get_inout_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getInoutComponentExchanges(), ComponentExchange)
    def get_allocated_functions(self) -> List[Function]:
        """
        Returns: Function[*]
        """
        return create_e_list(self.get_java_object().getAllocatedFunctions(), Function)
    def get_used_interfaces(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getUsedInterfaces(), Interface)
    def get_implemented_interfaces(self) -> List[Interface]:
        """
        Returns: Interface[*]
        """
        return create_e_list(self.get_java_object().getImplementedInterfaces(), Interface)
    def get_owned_state_machines(self) -> List[StateMachine]:
        """
        Returns: StateMachine[*]
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_owned_component_exchange_categories(self) -> List[ComponentExchangeCategory]:
        """
        Returns: ComponentExchangeCategory[*]
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)

class ComponentPort(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.fa.ComponentPort
    A port on a BehavioralComponent defining a logical interaction point
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentPort")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ComponentPort):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_orientation(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getOrientation()
        if value is None:
            return value
        else:
            return value.getName()
    def get_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getComponentExchanges(), ComponentExchange)
    def get_allocated_function_ports(self):
        """
        Returns: FunctionPort[*]
        """
        return capella_query_by_name(self, "Allocated Function Ports")
    def get_provided_interfaces(self):
        """
        Returns: Interface[*]
        """
        return capella_query_by_name(self, "Provided Interfaces")
    def get_required_interfaces(self):
        """
        Returns: Interface[*]
        """
        return capella_query_by_name(self, "Required Interfaces")
    def get_allocating_physical_ports(self):
        """
        Returns: PhysicalPort[0..1]
        """
        return capella_query_by_name(self, "Allocating Physical Ports")
    def get_realized_component_ports(self):
        """
        Returns: ComponentPort[*]
        """
        return capella_query_by_name(self, "Realized Component Ports")
    def get_realizing_component_ports(self):
        """
        Returns: ComponentPort[*]
        """
        return capella_query_by_name(self, "Realizing Component Ports")

class ComponentExchange(CapellaElement, AbstractExchange):
    """
    Java class: org.polarsys.capella.core.data.fa.ComponentExchange
    Represent the interactions between Logical / Behavioral&nbsp;Components. Exchanges connects Component Ports.
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchange")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ComponentExchange):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_connected_component_ports(self) -> ComponentPort:
        """
        Returns: ComponentPort[2]
        """
        return create_e_list(self.get_java_object().getConnectedComponentPorts(), ComponentPort)
    def get_connected_components(self):
        """
        Returns: BehavioralComponent[2]
        """
        return capella_query_by_name(self, "Connected Components")
    def get_categories(self):
        """
        Returns: ComponentExchangeCategory[*]
        """
        return capella_query_by_name(self, "Categories")
    def get_allocated_functional_exchanges(self):
        """
        Returns: FunctionalExchange[*]
        """
        return capella_query_by_name(self, "Allocated Functional Exchanges")
    def get_convoyed_informations(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_allocating_physical_link(self):
        """
        Returns: PhysicalLink[0..1]
        """
        return capella_query_by_name(self, "Allocating Physical Link")
    def get_allocating_physical_path(self):
        """
        Returns: PhysicalPath[0..1]
        """
        return capella_query_by_name(self, "Allocating Physical Path")
    def get_realized_communication_means(self) -> List[CommunicationMean]:
        """
        Returns: CommunicationMean[*]
        """
        return create_e_list(self.get_java_object().getRealizedCommunicationMeans(), CommunicationMean)
    def get_realized_component_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getRealizedComponentExchanges(), ComponentExchange)
    def get_realizing_component_exchanges(self):
        """
        Returns: ComponentExchange[*]
        """
        return capella_query_by_name(self, "Realizing Component Exchanges")

class ComponentExchangeCategory(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.fa.ComponentExchangeCategory
    A regroupement of ComponentExchanges for graphical simplification of diagrams
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchangeCategory")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ComponentExchangeCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_exchanges(self) -> List[ComponentExchange]:
        """
        Returns: ComponentExchange[*]
        """
        return create_e_list(self.get_java_object().getExchanges(), ComponentExchange)

class AbstractCapability(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.interaction.AbstractCapability
    An abstract type to define the generic relations of all capabilities (operational and system)
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "AbstractCapability")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, AbstractCapability):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_pre_condition(self) -> Constraint:
        """
        Returns: Constraint
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value: Constraint):
        """
        Parameters: value: Constraint
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self) -> Constraint:
        """
        Returns: Constraint
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value: Constraint):
        """
        Parameters: value: Constraint
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_scenarios(self) -> List[Scenario]:
        """
        Returns: Scenario[*]
        """
        return create_e_list(self.get_java_object().getOwnedScenarios(), Scenario)
    def get_super(self) -> List[AbstractCapability]:
        """
        Returns: AbstractCapability[*]
        """
        return create_e_list(self.get_java_object().getSuper(), AbstractCapability)
    def get_sub(self) -> List[AbstractCapability]:
        """
        Returns: AbstractCapability[*]
        """
        return create_e_list(self.get_java_object().getSub(), AbstractCapability)
    def get_included_capabilities(self):
        """
        Returns: AbstractCapability[*]
        """
        return capella_query_by_name(self, "Included Capabilities")
    def get_including_capabilities(self):
        """
        Returns: AbstractCapability[*]
        """
        return capella_query_by_name(self, "Including Capabilities")
    def get_extended_capabilities(self):
        """
        Returns: AbstractCapability[*]
        """
        return capella_query_by_name(self, "Extended Capabilities")
    def get_extending_capabilities(self):
        """
        Returns: AbstractCapability[*]
        """
        return capella_query_by_name(self, "Extending Capabilities")
    def get_available_in_states(self) -> List[State]:
        """
        Returns: State[*]
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)

class AbstractSystemCapability(AbstractCapability):
    """
    An abstract type to define the generic relation of system capabilities (as defined in SA, LA and PA)
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractSystemCapability):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involved_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getInvolvedFunctionalChains(), FunctionalChain)
    def get_involved_functions(self) -> List[Function]:
        """
        Returns: Function[*]
        """
        return create_e_list(self.get_java_object().getInvolvedAbstractFunctions(), Function)

class DataValue(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.DataValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "DataValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, DataValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)

class LiteralBooleanValue(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.LiteralBooleanValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralBooleanValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LiteralBooleanValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class BooleanReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.BooleanReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BooleanReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, BooleanReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class EnumerationReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.EnumerationReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumerationReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class LiteralStringValue(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.LiteralStringValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralStringValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LiteralStringValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class StringReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.StringReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "StringReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, StringReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class LiteralNumericValue(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.LiteralNumericValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralNumericValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LiteralNumericValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class NumericReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.NumericReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "NumericReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, NumericReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class ComplexValue(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.ComplexValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ComplexValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class ComplexValueReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.ComplexValueReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValueReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ComplexValueReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class BinaryExpression(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.BinaryExpression
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BinaryExpression")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, BinaryExpression):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class UnaryExpression(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.UnaryExpression
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "UnaryExpression")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, UnaryExpression):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class CollectionValueReference(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.CollectionValueReference
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValueReference")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CollectionValueReference):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class CollectionValue(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.CollectionValue
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValue")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CollectionValue):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class DataPkg(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.DataPkg
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "DataPkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, DataPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_classes(self) -> List[Class]:
        """
        Returns: Class[*]
        """
        return create_e_list(self.get_java_object().getOwnedClasses(), Class)
    def get_owned_data_pkgs(self) -> List[DataPkg]:
        """
        Returns: DataPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedDataPkgs(), DataPkg)
    def get_owned_collections(self) -> List[Collection]:
        """
        Returns: Collection[*]
        """
        return create_e_list(self.get_java_object().getOwnedCollections(), Collection)
    def get_owned_data_types(self) -> List[DataType]:
        """
        Returns: DataType[*]
        """
        return create_e_list(self.get_java_object().getOwnedDataTypes(), DataType)
    def get_owned_exceptions(self) -> List[CapellaException]:
        """
        Returns: CapellaException[*]
        """
        return create_e_list(self.get_java_object().getOwnedExceptions(), CapellaException)
    def get_owned_units(self) -> List[Unit]:
        """
        Returns: Unit[*]
        """
        return create_e_list(self.get_java_object().getOwnedUnits(), Unit)

class DataType(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.DataType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "DataType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, DataType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Class(DataType):
    """
    Java class: org.polarsys.capella.core.data.information.Class
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Class")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Class):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)
    def get_final(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isFinal()
    def set_final(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setFinal(value)
    def get_primitive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setPrimitive(value)
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_properties(self) -> List[Property]:
        """
        Returns: Property[*]
        """
        return create_e_list(self.get_java_object().getContainedProperties(), Property)
    def get_contained_operations(self) -> List[Operation]:
        """
        Returns: Operation[*]
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Collection(DataType):
    """
    Java class: org.polarsys.capella.core.data.information.Collection
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Collection")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Collection):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_ordered(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isOrdered()
    def set_ordered(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setOrdered(value)
    def get_unique(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isUnique()
    def set_unique(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setUnique(value)
    def get_min_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMaxInclusive(value)
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)
    def get_final(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isFinal()
    def set_final(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setFinal(value)
    def get_primitive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setPrimitive(value)
    def get_collection_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getCollectionKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_collection_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setCollectionKind(value.get_java_object())
    def get_aggregation_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getAggregationKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_aggregation_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setAggregationKind(value.get_java_object())
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_operations(self) -> List[Operation]:
        """
        Returns: Operation[*]
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)
    def get_min_card(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMinCard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_card(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMaxCard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class Union(DataType):
    """
    Java class: org.polarsys.capella.core.data.information.Union
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Union")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Union):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_final(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isFinal()
    def set_final(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setFinal(value)
    def get_contained_union_properties(self) -> List[UnionProperty]:
        """
        Returns: UnionProperty[*]
        """
        return create_e_list(self.get_java_object().getContainedUnionProperties(), UnionProperty)
    def get_discriminant(self) -> UnionProperty:
        """
        Returns: UnionProperty[0..1]
        """
        value =  self.get_java_object().getDiscriminant()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_discriminant(self, value: UnionProperty):
        """
        Parameters: value: UnionProperty[0..1]
        """
        return self.get_java_object().setDiscriminant(value.get_java_object())
    def get_default_property(self) -> UnionProperty:
        """
        Returns: UnionProperty[0..1]
        """
        value =  self.get_java_object().getDefaultProperty()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_property(self, value: UnionProperty):
        """
        Parameters: value: UnionProperty[0..1]
        """
        return self.get_java_object().setDefaultProperty(value.get_java_object())
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_contained_operations(self) -> List[Operation]:
        """
        Returns: Operation[*]
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Association(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.Association
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Association")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Association):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Property(JavaObject):
    """
    Java class: org.polarsys.kitalpha.ad.viewpoint.coredomain.viewpoint.model.Property
    """
    """
    Java class: org.polarsys.capella.core.data.information.Property
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Property")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Property):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_type(self) -> DataType:
        """
        Returns: DataType
        """
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_type(self, value: DataType):
        """
        Parameters: value: DataType
        """
        return self.get_java_object().setType(value.get_java_object())

class UnionProperty(Property):
    """
    Java class: org.polarsys.capella.core.data.information.UnionProperty
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "UnionProperty")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, UnionProperty):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Operation(JavaObject):
    """
    Java class: org.polarsys.capella.core.data.information.Operation
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Service")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Operation):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_realized_exchange_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getRealizedExchangeItems(), ExchangeItem)
    def get_owned_parameters(self) -> List[Parameter]:
        """
        Returns: Parameter[*]
        """
        return create_e_list(self.get_java_object().getOwnedParameters(), Parameter)
    def get_thrown_exceptions(self) -> List[CapellaException]:
        """
        Returns: CapellaException[*]
        """
        return create_e_list(self.get_java_object().getThrownExceptions(), CapellaException)

class Parameter(JavaObject):
    """
    Java class: org.polarsys.capella.core.data.information.Parameter
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Parameter")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Parameter):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class CapellaException(JavaObject):
    """
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/communication/" + capella_version(), "Exception")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapellaException):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self) -> List[CapellaException]:
        """
        Returns: CapellaException[*]
        """
        return create_e_list(self.get_java_object().getSuper(), CapellaException)
    def get_sub(self) -> List[CapellaException]:
        """
        Returns: CapellaException[*]
        """
        return create_e_list(self.get_java_object().getSub(), CapellaException)

class PrimitiveDataType(PropertyValuePkgContainer, DataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PrimitiveDataType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_abstract(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setAbstract(value)
    def get_final(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isFinal()
    def set_final(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setFinal(value)
    def get_discrete(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isDiscrete()
    def set_discrete(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setDiscrete(value)
    def get_visibility(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self) -> List[PrimitiveDataType]:
        """
        Returns: PrimitiveDataType[*]
        """
        return create_e_list(self.get_java_object().getSuper(), PrimitiveDataType)
    def get_sub(self) -> List[PrimitiveDataType]:
        """
        Returns: PrimitiveDataType[*]
        """
        return create_e_list(self.get_java_object().getSub(), PrimitiveDataType)
    def get_realized_informations(self) -> List[PrimitiveDataType]:
        """
        Returns: PrimitiveDataType[*]
        """
        return create_e_list(self.get_java_object().getRealizedDataTypes(), PrimitiveDataType)
    def get_realizing_informations(self) -> List[PrimitiveDataType]:
        """
        Returns: PrimitiveDataType[*]
        """
        return create_e_list(self.get_java_object().getRealizingDataTypes(), PrimitiveDataType)

class Enumeration(PrimitiveDataType):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.Enumeration
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "Enumeration")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Enumeration):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_min_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setPattern(value)
    def get_owned_literals(self) -> List[EnumerationLiteral]:
        """
        Returns: EnumerationLiteral[*]
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationLiteral)
    def get_default_value(self) -> EnumerationLiteral:
        """
        Returns: EnumerationLiteral[0..1]
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_value(self, value: EnumerationLiteral):
        """
        Parameters: value: EnumerationLiteral[0..1]
        """
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_min_value(self) -> EnumerationLiteral:
        """
        Returns: EnumerationLiteral[0..1]
        """
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_min_value(self, value: EnumerationLiteral):
        """
        Parameters: value: EnumerationLiteral[0..1]
        """
        return self.get_java_object().setMinValue(value.get_java_object())
    def get_max_value(self) -> EnumerationLiteral:
        """
        Returns: EnumerationLiteral[0..1]
        """
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_max_value(self, value: EnumerationLiteral):
        """
        Parameters: value: EnumerationLiteral[0..1]
        """
        return self.get_java_object().setMaxValue(value.get_java_object())
    def get_null_value(self) -> EnumerationLiteral:
        """
        Returns: EnumerationLiteral[0..1]
        """
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_null_value(self, value: EnumerationLiteral):
        """
        Parameters: value: EnumerationLiteral[0..1]
        """
        return self.get_java_object().setNullValue(value.get_java_object())
    def get_domain_type(self) -> PrimitiveDataType:
        """
        Returns: PrimitiveDataType[0..1]
        """
        value =  self.get_java_object().getDomainType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_domain_type(self, value: PrimitiveDataType):
        """
        Parameters: value: PrimitiveDataType[0..1]
        """
        return self.get_java_object().setDomainType(value.get_java_object())

class EnumerationLiteral(DataValue):
    """
    Java class: org.polarsys.capella.core.data.information.datavalue.EnumerationLiteral
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationLiteral")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, EnumerationLiteral):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_domain_value(self):
        """
        Returns: DataValue[0..1]
        """
        return capella_query_by_name(self, "Domain Value")
    def get_enumeration_type(self) -> Enumeration:
        """
        Returns: Enumeration[0..1]
        """
        value =  self.get_java_object().getEnumerationType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_enumeration_type(self, value: Enumeration):
        """
        Parameters: value: Enumeration[0..1]
        """
        return self.get_java_object().setEnumerationType(value.get_java_object())

class BooleanType(PrimitiveDataType):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.BooleanType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "BooleanType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, BooleanType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_literals(self) -> LiteralBooleanValue:
        """
        Returns: LiteralBooleanValue[0..2]
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), LiteralBooleanValue)
    def get_default_value(self) -> LiteralBooleanValue:
        """
        Returns: LiteralBooleanValue[0..1]
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_value(self, value: LiteralBooleanValue):
        """
        Parameters: value: LiteralBooleanValue[0..1]
        """
        return self.get_java_object().setDefaultValue(value.get_java_object())

class StringType(PrimitiveDataType):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.StringType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "StringType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, StringType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_min_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setPattern(value)
    def get_min_length(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMinLength()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_length(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMaxLength()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_default_value(self) -> LiteralStringValue:
        """
        Returns: LiteralStringValue[0..1]
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_null_value(self) -> LiteralStringValue:
        """
        Returns: LiteralStringValue[0..1]
        """
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class NumericType(PrimitiveDataType):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.NumericType
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "NumericType")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, NumericType):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_min_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setPattern(value)
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_min_value(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_value(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_default_value(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_null_value(self) -> LiteralNumericValue:
        """
        Returns: LiteralNumericValue[0..1]
        """
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class PhysicalQuantity(NumericType):
    """
    Java class: org.polarsys.capella.core.data.information.datatype.PhysicalQuantity
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "PhysicalQuantity")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalQuantity):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_unit(self) -> Unit:
        """
        Returns: Unit[0..1]
        """
        value =  self.get_java_object().getUnit()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_unit(self, value: Unit):
        """
        Parameters: value: Unit[0..1]
        """
        return self.get_java_object().setUnit(value.get_java_object())

class Unit(CapellaElement):
    """
    Java class: org.polarsys.capella.core.data.information.Unit
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/information/" + capella_version(), "Unit")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Unit):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class SystemEngineering(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.capellamodeller.SystemEngineering
    The main element in the definition of a Capella model. Contains the perspectives of the Arcadia methodology
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SystemEngineering):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_rec_catalogs(self) -> List[RecCatalog]:
        """
        Returns: RecCatalog[*]
        """
        res = []
        for extension in self.get_java_object().getOwnedExtensions():
            if extension.eClass().getName() == "RecCatalog" and extension.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/common/re/" + capella_version():
                res.append(RecCatalog(extension))
        return res
    def get_operational_analysis(self) -> OperationalAnalysis:
        """
        Returns: OperationalAnalysis
        """
        for oa in self.get_java_object().getContainedOperationalAnalysis():
            return OperationalAnalysis(oa)
    def get_system_analysis(self) -> SystemAnalysis:
        """
        Returns: SystemAnalysis
        """
        for sa in self.get_java_object().getContainedSystemAnalysis():
            return SystemAnalysis(sa)
    def get_logical_architecture(self) -> LogicalArchitecture:
        """
        Returns: LogicalArchitecture
        """
        for la in self.get_java_object().getContainedLogicalArchitectures():
            return LogicalArchitecture(la)
    def get_physical_architecture(self) -> PhysicalArchitecture:
        """
        Returns: PhysicalArchitecture
        """
        for pa in self.get_java_object().getContainedPhysicalArchitectures():
            return PhysicalArchitecture(pa)
    def get_e_p_b_s_architecture(self) -> EPBSArchitecture:
        """
        Returns: EPBSArchitecture
        """
        for epbsa in self.get_java_object().getContainedEPBSArchitectures():
            return EPBSArchitecture(epbsa)

class PropertyValuePkg(PropertyValuePkgContainer):
    """
    Java class: org.polarsys.capella.core.data.capellacore.PropertyValuePkg
    A package to contain PropertyValues&nbsp;and/or&nbsp;PropertyValueGroups
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValuePkg")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PropertyValuePkg):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class Interaction(AbstractEvent):
    """
    Oriented dependency between Operational Activities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalExchange")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Interaction):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_source(self) -> OperationalActivity:
        """
        Returns: OperationalActivity
        """
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source(self, value: OperationalActivity):
        """
        Parameters: value: OperationalActivity
        """
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self) -> OperationalActivity:
        """
        Returns: OperationalActivity
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target(self, value: OperationalActivity):
        """
        Parameters: value: OperationalActivity
        """
        return self.get_java_object().setTarget(value.get_java_object())
    def get_allocating_communication_mean(self) -> CommunicationMean:
        """
        Returns: CommunicationMean[0..1]
        """
        value =  self.get_java_object().getAllocatingCommunicationMean()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocating_communication_mean(self, value: CommunicationMean):
        """
        Parameters: value: CommunicationMean[0..1]
        """
        return self.get_java_object().setAllocatingCommunicationMean(value.get_java_object())
    def get_involving_operational_processes(self) -> List[OperationalProcess]:
        """
        Returns: OperationalProcess[*]
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalProcesses(), OperationalProcess)
    def get_exchanged_items(self) -> List[ExchangeItem]:
        """
        Returns: ExchangeItem[*]
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_realizing_functional_exchanges(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getRealizingFunctionalExchanges(), FunctionalExchange)

class OperationalCapability(AbstractCapability):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalCapability
    An operational capability is an ability, expected of one or more operational entities / actors. An operational capability is characterized by a set of operational processes and scenarios
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapability")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalCapability):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_operational_processes(self):
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Owned Operational Processes")
    def get_involved_operational_processes(self):
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Involved Operational Processes")
    def get_involved_operational_activities(self) -> List[OperationalActivity]:
        """
        Returns: OperationalActivity[*]
        """
        return create_e_list(self.get_java_object().getInvolvedOperationalActivities(), OperationalActivity)
    def get_involved_entities(self):
        """
        Returns: OperationalActor[*]
        """
        return capella_query_by_name(self, "Involved Entities")
    def get_realizing_capabilities(self):
        """
        Returns: Capability[*]
        """
        return capella_query_by_name(self, "Realizing Capabilities")

class OperationalEntity(OperationalActor):
    """
    An Operational Entity is a real world entity (other system, device, group or organisation…) carrying Operational Activities to which the system is likely to contribute
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "Entity")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalEntity):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if not java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed entity is an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_entities(self) -> List[OperationalEntity]:
        """
        Returns: OperationalEntity[*]
        """
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalEntity)

class Capability(AbstractSystemCapability):
    """
    Java class: org.polarsys.capella.core.data.ctx.Capability
    The ability of the system to supply a service contributing to fulfilling one or more Missions. A Capability represents a system usage context. It is characterized by a set of Functional Chains and Scenarios it references.
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Capability")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, Capability):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_purpose_missions(self) -> List[Mission]:
        """
        Returns: Mission[*]
        """
        return create_e_list(self.get_java_object().getPurposeMissions(), Mission)
    def get_realized_operational_capabilities(self):
        """
        Returns: OperationalCapability[*]
        """
        return capella_query_by_name(self, "Realized Operational Capabilities")
    def get_realizing_capability_realizations(self):
        """
        Returns: CapabilityRealization[*]
        """
        return capella_query_by_name(self, "Realizing Capability Realizations")
    def get_involved_system_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        return create_e_list(self.get_java_object().getInvolvedSystemActors(), SystemActor)

class System(BehavioralComponent, Node):
    """
    Set of elements functioning as a whole, responding to customer and user demand and needs
    The System defined in the SystemAnalysis is seen as a black box
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, System):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))

class SystemActor(BehavioralComponent, Node):
    """
    Entity (human or not) that is external to the System (in term of responsibility), interacting with it, via its interfaces
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, SystemActor):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_is_human(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setHuman(value)
    def get_owned_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)
    def get_owned_system_component_pkgs(self) -> SystemComponentPkg:
        """
        Returns: SystemComponentPkg
        """
        value =  self.get_java_object().getOwnedSystemComponentPkgs()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_involving_missions(self) -> List[Mission]:
        """
        Returns: Mission[*]
        """
        return create_e_list(self.get_java_object().getInvolvingMissions(), Mission)
    def get_realized_operational_entities(self) -> List[OperationalActor]:
        """
        Returns: OperationalActor[*]
        """
        return create_e_list(self.get_java_object().getRealizedOperationalEntities(), OperationalActor)
    def get_involving_capabilities(self) -> List[Capability]:
        """
        Returns: Capability[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_realizing_logical_actors(self) -> List[LogicalActor]:
        """
        Returns: LogicalActor[*]
        """
        return create_e_list(self.get_java_object().getRealizingLogicalActors(), LogicalActor)

class CapabilityRealization(AbstractSystemCapability):
    """
    Java class: org.polarsys.capella.core.data.la.CapabilityRealization
    The implementation of the system Capabilities in Logical Architecture and Physical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealization")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, CapabilityRealization):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_realized_capabilities(self):
        """
        Returns: Capability[*]
        """
        return capella_query_by_name(self, "Realized Capabilities")
    def get_realized_capability_realizations(self):
        """
        Returns: CapabilityRealization[*]
        """
        return capella_query_by_name(self, "Realized Capability Realizations")
    def get_realizing_capability_realizations(self):
        """
        Returns: CapabilityRealization[*]
        """
        return capella_query_by_name(self, "Realizing Capability Realizations")
    def get_involved_logical_actors(self) -> List[LogicalActor]:
        """
        Returns: LogicalActor[*]
        """
        return create_e_list(self.get_java_object().getInvolvedLogicalActors(), LogicalActor)
    def get_involved_logical_components(self) -> List[LogicalComponent]:
        """
        Returns: LogicalComponent[*]
        """
        return create_e_list(self.get_java_object().getInvolvedLogicalComponents(), LogicalComponent)
    def get_involved_physical_components(self) -> List[PhysicalComponent]:
        """
        Returns: PhysicalComponent[*]
        """
        return create_e_list(self.get_java_object().getInvolvedPhysicalComponents(), PhysicalComponent)
    def get_involved_physical_actors(self) -> List[PhysicalActor]:
        """
        Returns: PhysicalActor[*]
        """
        return create_e_list(self.get_java_object().getInvolvedPhysicalActors(), PhysicalActor)

class LogicalSystem(BehavioralComponent, Node):
    """
    The definition of the system in Logical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalSystem):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_logical_components(self) -> List[LogicalComponent]:
        """
        Returns: LogicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self) -> List[LogicalComponentPkg]:
        """
        Returns: LogicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)

class LogicalComponent(BehavioralComponent):
    """
    Java class: org.polarsys.capella.core.data.la.LogicalComponent
    Logical Components are the artefacts enabling a notional decomposition of the system as a "white box", independently from any technological solutions, but dealing with major system decomposition constraints
    Logical components are identified according to logical abstractions (i.e. functional grouping, logical interfaces)
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalComponent):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if not java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_logical_components(self) -> List[LogicalComponent]:
        """
        Returns: LogicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self) -> List[LogicalComponentPkg]:
        """
        Returns: LogicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_is_human(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setHuman(value)
    def get_realizing_behavior_p_cs(self) -> List[BehaviorPC]:
        """
        Returns: BehaviorPC[*]
        """
        return create_e_list(self.get_java_object().getRealizingBehaviorPCs(), BehaviorPC)
    def get_involving_capability_realizations(self) -> List[CapabilityRealization]:
        """
        Returns: CapabilityRealization[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class LogicalActor(BehavioralComponent, Node):
    """
    An external Actor defined in the Logical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, LogicalActor):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_logical_actors(self) -> List[LogicalActor]:
        """
        Returns: LogicalActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_component_pkgs(self) -> List[LogicalComponentPkg]:
        """
        Returns: LogicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_realized_system_actors(self) -> List[SystemActor]:
        """
        Returns: SystemActor[*]
        """
        return create_e_list(self.get_java_object().getRealizedSystemActors(), SystemActor)
    def get_is_human(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setHuman(value)
    def get_realizing_physical_actors(self) -> List[PhysicalActor]:
        """
        Returns: PhysicalActor[*]
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalActors(), PhysicalActor)
    def get_involving_capability_realizations(self) -> List[CapabilityRealization]:
        """
        Returns: CapabilityRealization[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class PhysicalSystem(CapellaElement, Node):
    """
    The definition of the system in Physical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, PhysicalSystem):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_physical_components(self) -> List[PhysicalComponent]:
        """
        Returns: PhysicalComponent[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self) -> List[PhysicalComponentPkg]:
        """
        Returns: PhysicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)

class BehaviorPC(PhysicalComponent, BehavioralComponent):
    """
    System component in charge of implementing / realizing some of the functions devoted to the system
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setNature(get_enum_literal("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentNature", "BEHAVIOR"))
        elif isinstance(java_object, BehaviorPC):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if not java_object.isActor():
                if java_object.getNature().getName() == "UNSET":
                    raise AttributeError("Passed component is a physical component.")
                elif java_object.getNature().getName() == "BEHAVIOR":
                    JavaObject.__init__(self, java_object)
                elif java_object.getNature().getName() == "NODE":
                    raise AttributeError("Passed component is a node physical component.")
                else:
                    raise AttributeError("Passed component has unexpected nature.")
            else:
                raise AttributeError("Passed component is an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_deploying_node_p_cs(self) -> List[NodePC]:
        """
        Returns: NodePC[*]
        """
        return create_e_list(self.get_java_object().getDeployingPhysicalComponents(), NodePC)
    def get_realized_logical_components(self) -> List[LogicalComponent]:
        """
        Returns: LogicalComponent[*]
        """
        return create_e_list(self.get_java_object().getRealizedLogicalComponents(), LogicalComponent)

class NodePC(PhysicalComponent, Node):
    """
    Component hosting a number of behavioral components, providing them with the resource they require to function and to interact with their environment
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setNature(get_enum_literal("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentNature", "NODE"))
        elif isinstance(java_object, NodePC):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if not java_object.isActor():
                if java_object.getNature().getName() == "UNSET":
                    raise AttributeError("Passed component is a physical component.")
                elif java_object.getNature().getName() == "BEHAVIOR":
                    raise AttributeError("Passed component is a behavior physical component.")
                elif java_object.getNature().getName() == "NODE":
                    JavaObject.__init__(self, java_object)
                else:
                    raise AttributeError("Passed component has unexpected nature.")
            else:
                raise AttributeError("Passed component is an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_deployed_behavior_p_cs(self) -> List[BehaviorPC]:
        """
        Returns: BehaviorPC[*]
        """
        res = []
        e_object_class = getattr(sys.modules["__main__"], "EObject")
        for pc in self.java_object.getDeployedPhysicalComponents():
            specific_cls = e_object_class.get_class(pc)
            if specific_cls == BehaviorPC:
                res.append(specific_cls(pc))
        return res
    def get_owned_state_machines(self) -> List[StateMachine]:
        """
        Returns: StateMachine[*]
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class PhysicalActor(BehavioralComponent, Node):
    """
    An external Actor defined in the Physical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent")
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, PhysicalActor):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_owned_physical_actors(self) -> List[PhysicalActor]:
        """
        Returns: PhysicalActor[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_component_pkgs(self) -> List[PhysicalComponentPkg]:
        """
        Returns: PhysicalComponentPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_realized_logical_actors(self) -> List[LogicalActor]:
        """
        Returns: LogicalActor[*]
        """
        return create_e_list(self.get_java_object().getRealizedLogicalActors(), LogicalActor)
    def get_is_human(self) -> bool:
        """
        Returns: Boolean
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value: bool):
        """
        Returns: Boolean
        """
        self.get_java_object().setHuman(value)
    def get_involving_capability_realizations(self) -> List[CapabilityRealization]:
        """
        Returns: CapabilityRealization[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class ChangeEvent(AbstractEvent):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.ChangeEvent
    An event defined by WHEN something occurs
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "ChangeEvent")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, ChangeEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_expression(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getExpression()
    def set_expression(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setExpression(value)

class TimeEvent(AbstractEvent):
    """
    Java class: org.polarsys.capella.core.data.capellacommon.TimeEvent
    An event defined by AT a given time, or AFTER a certain time
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/common/" + capella_version(), "TimeEvent")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, TimeEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_expression(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getExpression()
    def set_expression(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setExpression(value)

class AbstractActivityFunction(AbstractAction, AbstractEvent, AbstractInstance):
    """
    An abstract type to define the link between mode / state and activity / function (available in states)
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractActivityFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_available_in_states(self) -> List[State]:
        """
        Returns: State[*]
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)

class Function(AbstractActivityFunction):
    """
    Action performed by the System, an Actor or a component, in order to realize a Capability
    """
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Function):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self) -> str:
        """
        Returns: String
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value: str):
        """
        Parameters: value: String
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_condition(self) -> str:
        """
        Returns: String
        """
        return self.get_java_object().getCondition()
    def set_condition(self, value: str):
        """
        Returns: String
        """
        self.get_java_object().setCondition(value)
    def get_inputs(self) -> List[FunctionInputPort]:
        """
        Returns: FunctionInputPort[*]
        """
        return create_e_list(self.get_java_object().getInputs(), FunctionInputPort)
    def get_outputs(self) -> List[FunctionOutputPort]:
        """
        Returns: FunctionOutputPort[*]
        """
        return create_e_list(self.get_java_object().getOutputs(), FunctionOutputPort)
    def get_incoming(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getIncoming(), FunctionalExchange)
    def get_outgoing(self) -> List[FunctionalExchange]:
        """
        Returns: FunctionalExchange[*]
        """
        return create_e_list(self.get_java_object().getOutgoing(), FunctionalExchange)
    def get_allocating_component(self) -> BehavioralComponent:
        """
        Returns: BehavioralComponent[0..1]
        """
        values = None
        if isinstance(self, LogicalFunction):
            values = self.get_java_object().getAllocatingLogicalComponents()
        elif isinstance(self, OperationalActivity):
            values = self.get_java_object().getAllocatingRoles()
        elif isinstance(self, PhysicalFunction):
            values = self.get_java_object().getAllocatingPhysicalComponents()
        elif isinstance(self, SystemFunction):
            values = self.get_java_object().getAllocatingSystemComponents()
        if not values:
            return None
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(values[0])
            return specific_cls(values[0])
    def get_owned_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involving_functional_chains(self) -> List[FunctionalChain]:
        """
        Returns: FunctionalChain[*]
        """
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_involving_capabilities(self) -> List[AbstractSystemCapability]:
        """
        Returns: AbstractSystemCapability[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), AbstractSystemCapability)
    def get_owned_functions(self) -> List[Function]:
        """
        Returns: Function[*]
        """
        return create_e_list(self.get_java_object().getOwnedFunctions(), Function)

class OperationalActivity(Function):
    """
    Java class: org.polarsys.capella.core.data.oa.OperationalActivity
    Process step or action/operation/service performed by an Operational entity / actor&nbsp;and likely to influence the system definition or usage. Implementing operational activities generally produces elements of interactions expected by other activities
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivity")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, OperationalActivity):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_contained_operational_activities(self) -> List[OperationalActivity]:
        """
        Returns: OperationalActivity[*]
        """
        return create_e_list(self.get_java_object().getContainedOperationalActivities(), OperationalActivity)
    def get_owned_operational_activity_pkgs(self) -> List[OperationalActivityPkg]:
        """
        Returns: OperationalActivityPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_incoming(self) -> List[Interaction]:
        """
        Returns: Interaction[*]
        """
        return create_e_list(self.get_java_object().getIncoming(), Interaction)
    def get_outgoing(self) -> List[Interaction]:
        """
        Returns: Interaction[*]
        """
        return create_e_list(self.get_java_object().getOutgoing(), Interaction)
    def get_allocating_entity(self):
        """
        Returns: OperationalActor[0..1]
        """
        return capella_query_by_name(self, "Allocating Entity")
    def get_owned_operational_processes(self):
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Owned Operational Processes")
    def get_involving_operational_processes(self) -> List[OperationalProcess]:
        """
        Returns: OperationalProcess[*]
        """
        return capella_query_by_name(self, "Operational Processes")
    def get_involving_operational_capabilities(self) -> List[OperationalCapability]:
        """
        Returns: OperationalCapability[*]
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), OperationalCapability)
    def get_realizing_system_functions(self):
        """
        Returns: SystemFunction[*]
        """
        return capella_query_by_name(self, "Realizing System Functions")

class SystemFunction(Function):
    """
    Java class: org.polarsys.capella.core.data.ctx.SystemFunction
    The definition of a Function in the System Analysis
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunction")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, SystemFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_contained_system_functions(self) -> List[SystemFunction]:
        """
        Returns: SystemFunction[*]
        """
        return create_e_list(self.get_java_object().getContainedSystemFunctions(), SystemFunction)
    def get_owned_system_function_pkgs(self) -> List[SystemFunctionPkg]:
        """
        Returns: SystemFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_realized_operational_activities(self):
        """
        Returns: OperationalActivity[*]
        """
        return capella_query_by_name(self, "Realized Operational Activities")
    def get_realizing_logical_functions(self):
        """
        Returns: LogicalFunction[*]
        """
        return capella_query_by_name(self, "Realizing Logical Functions")

class LogicalFunction(Function):
    """
    Java class: org.polarsys.capella.core.data.la.LogicalFunction
    The definition of a Function in the Logical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunction")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, LogicalFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_contained_logical_functions(self) -> List[LogicalFunction]:
        """
        Returns: LogicalFunction[*]
        """
        return create_e_list(self.get_java_object().getContainedLogicalFunctions(), LogicalFunction)
    def get_owned_logical_function_pkgs(self) -> List[LogicalFunctionPkg]:
        """
        Returns: LogicalFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_realized_system_functions(self):
        """
        Returns: SystemFunction[*]
        """
        return capella_query_by_name(self, "Realized System Functions")
    def get_realizing_physical_functions(self):
        """
        Returns: PhysicalFunction[*]
        """
        return capella_query_by_name(self, "Realizing Physical Functions")

class PhysicalFunction(Function):
    """
    Java class: org.polarsys.capella.core.data.pa.PhysicalFunction
    The definition of a Function in the Physical Architecture
    """
    e_class = get_e_classifier("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunction")
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object_from_e_classifier(self.e_class))
        elif isinstance(java_object, PhysicalFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        elif self.e_class.isInstance(java_object):
            JavaObject.__init__(self, java_object)
        else:
            raise AttributeError("Passed object is not compatible with " + self.__class__.__name__ + ": " + str(java_object))
    def get_contained_physical_functions(self) -> List[PhysicalFunction]:
        """
        Returns: PhysicalFunction[*]
        """
        return create_e_list(self.get_java_object().getContainedPhysicalFunctions(), PhysicalFunction)
    def get_owned_physical_function_pkgs(self) -> List[PhysicalFunctionPkg]:
        """
        Returns: PhysicalFunctionPkg[*]
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_realized_logical_functions(self):
        """
        Returns: LogicalFunction[*]
        """
        return capella_query_by_name(self, "Realized Logical Functions")

class Status(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyLiteral"))
        elif isinstance(java_object, Status):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

