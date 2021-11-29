include('workspace://Python4Capella/java_api/EMF_API.py')
if False:
    from java_api.EMF_API import *
include('workspace://Python4Capella/java_api/Capella_API.py')
if False:
    from java_api.Capella_API import *
include('workspace://Python4Capella/java_api/Sirius_API.py')
if False:
    from java_api.Sirius_API import *
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *


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
    def get_system_engineering(self):
        """
        """
        if self.session is None:
            return None
        else:
            return SystemEngineering(Sirius.get_system_engineering(self.session))
    def get_progress_status(self):
        """
        """
        value =  self.get_system_engineering().get_java_object().getStatus()
        if value is None:
            return value
        else:
            return value.getName()
    def get_referenced_libraries(self):
        """
        """
        return get_libraries(self.get_system_engineering())
    def get_all_diagrams(self):
        """
        """
        res = []
        descriptors = Sirius.get_all_diagrams(self.session)
        for descriptor in descriptors:
            res.append(Diagram(descriptor))
        return res
    def get_diagrams(self, diagram_type):
        """
        status: OK
        """
        res = []
        descriptors = Sirius.get_diagrams(self.session, diagram_type)
        for descriptor in descriptors:
            res.append(Diagram(descriptor))
        return res
    def open(self, obj):
        """
        status: KO
        """
        # obj can be a path to the .aird file or an EObject
        if isinstance(obj, str) or isinstance(obj, unicode):
            if CapellaPlatform.getWorkspaceFile(obj) is None:
                raise AttributeError("the .aird file doesn't exist: " + obj)
            self.session = Sirius.load_session(obj)
        elif isinstance(obj, EObject):
            self.session = Sirius.get_session(obj)
        else:
            raise AttributeError("You can pass a path to the .aird file or an EObject.")
    def create(self, path):
        """
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
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering"))
        elif isinstance(java_object, CapellaLibrary):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class EObject(JavaObject):
    """
    A generic object. Defines generic relations which are available for all elements
    """
    @staticmethod
    def get_class(e_object):
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
        if res == None and e_object.eClass().getName() in ["ChoicePseudoState", "DeepHistoryPseudoState", "EntryPointPseudoState", "ExitPointPseudoState", "ForkPseudoState", "InitialPseudoState", "JoinPseudoState", "ShallowHistoryPseudoState", "TerminatePseudoState", "FinalState"]:
            res = Pseudostate
        return res
    def get_owned_diagrams(self):
        """
        """
        res = []
        for element in Sirius.get_representation_descriptors(self.get_java_object()):
            res.append(Diagram(element))
        return res
    def get_element_of_interest_for_diagrams(self):
        """
        """
        return capella_query_by_name(self, "Element of Interest for Diagram", Diagram)
    def get_contextual_element_for_diagrams(self):
        """
        """
        res = []
        for element in Sirius.get_contextual_element_for_diagrams(self.get_java_object()):
            res.append(Diagram(element))
        return res
    def get_representing_diagrams(self):
        """
        """
        res = []
        for element in Sirius.get_representing_diagrams(self.get_java_object()):
            res.append(Diagram(element))
        return res
    def get__r_e_cs(self):
        """
        """
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicableElements", self)
    def get__r_p_ls(self):
        """
        """
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicas", self)
    def get_label(self):
        """
        """
        return get_label(self)
    def get_element_type(self):
        """
        """
        raise AttributeError("TODO")
    def get_container(self):
        """
        """
        value = self.get_java_object().eContainer()
        if value is not None:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                return specific_cls(value)
        return None
    def get_contents(self):
        """
        """
        res = []
        for value in self.get_java_object().eContents():
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                res.append(specific_cls(value))
        return res
    def get_all_contents(self):
        """
        """
        res = []
        for value in e_all_contents(self.get_java_object()):
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            if specific_cls is not None:
                res.append(specific_cls(value))
        return res
    def get_all_contents_by_type(self, cls):
        """
        """
        res = []
        for value in self.get_all_contents():
            if isinstance(value, cls):
                res.append(value)
        return res
    def get_available_s_b_queries(self):
        """
        """
        return available_query_names(self)
    def get_query_result(self, name):
        """
        """
        return capella_query_by_name(self, name)

class CapellaElement(EObject):
    """
    A generic Capella model Element. Used to define generic attributes and relations inherited by most Capella elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "CapellaElement"))
        elif isinstance(java_object, CapellaElement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_id(self):
        """
        """
        return self.get_java_object().getId()
    def set_id(self, value):
        """
        """
        self.get_java_object().setId(value)
    def get_sid(self):
        """
        """
        return self.get_java_object().getSid()
    def set_sid(self, value):
        """
        """
        self.get_java_object().setSid(value)
    def get_name(self):
        """
        """
        return self.get_java_object().getName()
    def set_name(self, value):
        """
        """
        self.get_java_object().setName(value)
    def get_summary(self):
        """
        """
        return self.get_java_object().getSummary()
    def set_summary(self, value):
        """
        """
        self.get_java_object().setSummary(value)
    def get_description(self):
        """
        """
        return self.get_java_object().getDescription()
    def set_description(self, value):
        """
        """
        self.get_java_object().setDescription(value)
    def get_status(self):
        """
        """
        value =  self.get_java_object().getStatus()
        if value is None:
            return value
        else:
            return value.getName()
    def get_review(self):
        """
        """
        return self.get_java_object().getReview()
    def set_review(self, value):
        """
        """
        self.get_java_object().setReview(value)
    def get_visible_in_documentation(self):
        """
        """
        return self.get_java_object().isVisibleInDoc()
    def set_visible_in_documentation(self, value):
        """
        """
        self.get_java_object().setVisibleInDoc(value)
    def get_visible_for_traceability(self):
        """
        """
        return self.get_java_object().isVisibleInLM()
    def set_visible_for_traceability(self, value):
        """
        """
        self.get_java_object().setVisibleInLM(value)
    def get_owned_constraints(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConstraints(), Constraint)
    def get_constraints(self):
        """
        """
        return create_e_list(self.get_java_object().getConstraints(), Constraint)
    def get_owned_property_values(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValues(), PropertyValue)
    def get_applied_property_values(self):
        """
        """
        return create_e_list(self.get_java_object().getAppliedPropertyValues(), PropertyValue)
    def get_owned_property_value_groups(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValueGroups(), PropertyValueGroup)
    def get_applied_property_value_groups(self):
        """
        """
        return create_e_list(self.get_java_object().getAppliedPropertyValueGroups(), PropertyValueGroup)
    def get_owned_enumeration_property_types(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedEnumerationPropertyTypes(), EnumerationPropertyType)

class Constraint(CapellaElement):
    """
    A generic constraint which can be defined on Capella elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "Constraint"))
        elif isinstance(java_object, Constraint):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_specification(self):
        """
        """
        return self.get_java_object().getSpecification()
    def set_specification(self, value):
        """
        """
        self.get_java_object().setSpecification(value)
    def get_constrained_elements(self):
        """
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
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        return self.java_object.eClass().getName()
    def get_value(self):
        """
        """
        return self.get_java_object().getValue()
    def set_value(self, value):
        """
        """
        self.get_java_object().setValue(value)
    def get_valued_elements(self):
        """
        """
        return create_e_list(self.get_java_object().getValuedElements(), CapellaElement)
    def get_type(self):
        """
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
    A group which can contain several PropertyValue and be applied to CapellaElements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValueGroup"))
        elif isinstance(java_object, PropertyValueGroup):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_valued_elements(self):
        """
        """
        return capella_query_by_name(self, "Valued Elements")

class EnumerationPropertyType(CapellaElement):
    """
    The definition of an Enumeration to type a PropertyValue
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyType"))
        elif isinstance(java_object, EnumerationPropertyType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_literals(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationPropertyLiteral)

class EnumerationPropertyLiteral(CapellaElement):
    """
    A value defined in an EnumerationPropertyType
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyLiteral"))
        elif isinstance(java_object, EnumerationPropertyLiteral):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

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
    def get_owned_property_value_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPropertyValuePkgs(), PropertyValuePkg)

class Diagram(JavaObject):
    """
    A generic Capella diagram
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.eclipse.org/sirius/1.1.0", "DRepresentationDescriptor"))
        elif isinstance(java_object, Diagram):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_uid(self):
        """
        """
        return self.get_java_object().getUid()
    def set_uid(self, value):
        """
        """
        self.get_java_object().setUid(value)
    def get_name(self):
        """
        """
        return self.get_java_object().getName()
    def set_name(self, value):
        """
        """
        self.get_java_object().setName(value)
    def get_type(self):
        """
        """
        if self.get_java_object().getDescription() is None:
            return None
        else:
            return self.get_java_object().getDescription().getName()
    def get_package(self):
        """
        """
        if self.get_java_object().getTarget() is None:
            return None
        else:
            return self.get_java_object().getTarget().eClass().getEPackage().getName()
    def get_description(self):
        """
        """
        return self.get_java_object().getDocumentation()
    def set_description(self, value):
        """
        """
        self.get_java_object().setDocumentation(value)
    def get_status(self):
        """
        """
        value = Sirius.get_status(self.get_java_object())
        if value is None:
            return value
        else:
            return value.getName()
    def get_review(self):
        """
        """
        return Sirius.get_review(self.get_java_object())
    def get_visible_in_documentation(self):
        """
        """
        return Sirius.is_visible_in_documentation(self.get_java_object())
    def get_visible_for_traceability(self):
        """
        """
        return Sirius.is_visible_for_traceability(self.get_java_object())
    def get_synchronized(self):
        """
        """
        return Sirius.is_synchronized(self.get_java_object())
    def get_target(self):
        """
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_represented_elements(self):
        """
        """
        res = []
        for element in Sirius.get_represented_elements(self.get_java_object()):
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(element)
            if specific_cls is not None:
                res.append(specific_cls(element))
        return res
    def get_contextual_elements(self):
        """
        """
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToContextualElement", self)
    def get_elements_of_interest(self):
        """
        """
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToElement", self)
    def export_as_image(self, file_path):
        """
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
    def get_id(self):
        """
        """
        return self.get_java_object().getId()
    def set_id(self, value):
        """
        """
        self.get_java_object().setId(value)
    def get_name(self):
        """
        """
        return self.get_java_object().getName()
    def set_name(self, value):
        """
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
    def get_decription(self):
        """
        """
        return self.get_java_object().getDecription()
    def set_decription(self, value):
        """
        """
        self.get_java_object().setDecription(value)
    def get_author(self):
        """
        """
        return self.get_java_object().getAuthor()
    def set_author(self, value):
        """
        """
        self.get_java_object().setAuthor(value)
    def get_environment(self):
        """
        """
        return self.get_java_object().getEnvironment()
    def set_environment(self, value):
        """
        """
        self.get_java_object().setEnvironment(value)
    def get_tags(self):
        """
        """
        return self.get_java_object().getTags()
    def set_tags(self, value):
        """
        """
        self.get_java_object().setTags(value)

class REC(AbstractCatalogElement):
    """
    A Record element is the definition of a set of elements to be replicated together
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElement"))
            self.get_java_object().setKind(get_enum_literal("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementKind", "REC"))
        elif isinstance(java_object, RPL):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.getKind().getName() == "REC":
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed catalog element is not a REC.")
    def get_referenced_elements(self):
        """
        """
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)
    def get_default_replica_compliancy(self):
        """
        """
        value =  self.get_java_object().getDefaultReplicaCompliancy()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_replica_compliancy(self, value):
        """
        """
        return self.get_java_object().setDefaultReplicaCompliancy(value.get_java_object())
    def get_replicated_elements(self):
        """
        """
        return create_e_list(self.get_java_object().getReplicatedElements(), RPL)

class RPL(AbstractCatalogElement):
    """
    A replay element is the instantiation of a record element
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElement"))
            self.get_java_object().setKind(get_enum_literal("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementKind", "RPL"))
        elif isinstance(java_object, RPL):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.getKind().getName() == "RPL":
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed catalog element is not a RPL.")
    def get_referenced_elements(self):
        """
        """
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)
    def get_suffix(self):
        """
        """
        return self.get_java_object().getSuffix()
    def set_suffix(self, value):
        """
        """
        self.get_java_object().setSuffix(value)
    def get_read_only(self):
        """
        """
        return self.get_java_object().isReadOnly()
    def set_read_only(self, value):
        """
        """
        self.get_java_object().setReadOnly(value)
    def get_origin(self):
        """
        """
        value =  self.get_java_object().getOrigin()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_origin(self, value):
        """
        """
        return self.get_java_object().setOrigin(value.get_java_object())
    def get_current_compliancy(self):
        """
        """
        value =  self.get_java_object().getCurrentCompliancy()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_current_compliancy(self, value):
        """
        """
        return self.get_java_object().setCurrentCompliancy(value.get_java_object())

class CatalogElementPkg(AbstractReElement):
    """
    A package to structure the definition of REC / RPL elements
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementPkg"))
        elif isinstance(java_object, CatalogElementPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_element_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedElementPkgs(), CatalogElementPkg)
    def get_owned_recs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRecs(), REC)
    def get_owned_rpls(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRpls(), RPL)

class RecCatalog(CatalogElementPkg):
    """
    The root package which contains the REC / RPL definitions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "RecCatalog"))
        elif isinstance(java_object, RecCatalog):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_compliancy_definition_pkg(self):
        """
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
    A package to contain CompliancyDefinitions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinitionPkg"))
        elif isinstance(java_object, CompliancyDefinitionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_definitions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedDefinitions(), CompliancyDefinition)

class CompliancyDefinition(AbstractReElement):
    """
    The type of compliancy which have to be respected by the RPL regarding its REC definition. Default list of compliancies is:
    BLACK_BOX
    CONSTRAINT_REUSE
    INHERITANCY_REUSE
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinition"))
        elif isinstance(java_object, CompliancyDefinition):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_description(self):
        """
        """
        return self.get_java_object().getDescription()
    def set_description(self, value):
        """
        """
        self.get_java_object().setDescription(value)

class OperationalAnalysis(PropertyValuePkgContainer):
    """
    The element containing all definitions from the Operational Analysis.
    The Operational Analysis aims at defining what the users of the system need to accomplish
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalAnalysis"))
        elif isinstance(java_object, OperationalAnalysis):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_operational_activity_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedOperationalActivityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_operational_capability_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedOperationalCapabilityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_entity_pkg(self):
        """
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
    A package to contain OperationalActivity
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivityPkg"))
        elif isinstance(java_object, OperationalActivityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_operational_activity_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_owned_operational_activities(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivities(), OperationalActivity)

class OperationalProcess(CapellaElement):
    """
    An operational process is used to describe a particular context for performing operational activities to contribute to one or more operational capabilities
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalProcess"))
        elif isinstance(java_object, OperationalProcess):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_involved_operational_activities(self):
        """
        """
        res = []
        for involved_element in self.get_java_object().getInvolvedElements():
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(involved_element)
            if specific_cls is not None and specific_cls.__name__ == "OperationalActivity":
                res.append(specific_cls(involved_element))
        return res
    def get_involved_interactions(self):
        """
        """
        res = []
        for involved_element in self.get_java_object().getInvolvedElements():
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(involved_element)
            if specific_cls is not None and specific_cls.__name__ == "FunctionalExchange":
                res.append(Interaction(involved_element))
        return res
    def get_involved_operational_processes(self):
        """
        """
        return capella_query_by_name(self, "Involved Operational Processes")
    def get_pre_condition(self):
        """
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value):
        """
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        """
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value):
        """
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_available_in_states(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involving_operational_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_realizing_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingFunctionalChains(), FunctionalChain)

class OperationalCapabilityPkg(PropertyValuePkgContainer):
    """
    A package to contain OperationalCapabilities
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapabilityPkg"))
        elif isinstance(java_object, OperationalCapabilityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_operational_capability_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilityPkgs(), OperationalCapabilityPkg)
    def get_owned_operational_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilities(), OperationalCapability)

class EntityPkg(PropertyValuePkgContainer):
    """
    A package to define Operational entities / actors
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "EntityPkg"))
        elif isinstance(java_object, EntityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_entity_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedEntityPkgs(), EntityPkg)
    def get_owned_entities(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalActor)

class OperationalActor(CapellaElement):
    """
    An Operational Actor is a kind of Operational Entity, usually human. It cannot be broken down
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "Entity"))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, OperationalEntity):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed entity is not an actor.")
    def get_incoming_communication_means(self):
        """
        """
        return create_e_list(self.get_java_object().getIncomingCommunicationMeans(), CommunicationMean)
    def get_outgoing_communication_means(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoingCommunicationMeans(), CommunicationMean)
    def get_allocated_operational_activities(self):
        """
        """
        return create_e_list(self.get_java_object().getAllocatedOperationalActivities(), OperationalActivity)
    def get_involving_operational_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_owned_state_machines(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_realizing_system_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingSystemActors(), SystemActor)

class CommunicationMean(CapellaElement):
    """
    Describes the media between the Operational Entities / Actors&nbsp;to support the Operational Interactions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "CommunicationMean"))
        elif isinstance(java_object, CommunicationMean):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_source_entity(self):
        """
        """
        value =  self.get_java_object().getSourceEntity()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source_entity(self, value):
        """
        """
        return self.get_java_object().setSourceEntity(value.get_java_object())
    def get_target_entity(self):
        """
        """
        value =  self.get_java_object().getTargetEntity()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target_entity(self, value):
        """
        """
        return self.get_java_object().setTargetEntity(value.get_java_object())
    def get_allocated_interactions(self):
        """
        """
        return capella_query_by_name(self, "Allocated Interactions")
    def get_convoyed_informations(self):
        """
        """
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_realizing_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingComponentExchanges(), ComponentExchange)

class SystemAnalysis(PropertyValuePkgContainer):
    """
    The element containing all definitions from the System Analysis.
    The System Analysis aims at defining what the system has to accomplish for the users
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemAnalysis"))
        elif isinstance(java_object, SystemAnalysis):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_system_function_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedSystemFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedCapabilityPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_system_component_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedSystemComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_mission_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedMissionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_system(self):
        """
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
    A package to contain SystemFunctions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunctionPkg"))
        elif isinstance(java_object, SystemFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_system_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_owned_system_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctions(), SystemFunction)
    def get_owned_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class CapabilityPkg(PropertyValuePkgContainer):
    """
    A package to contain Capabilities
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "CapabilityPkg"))
        elif isinstance(java_object, CapabilityPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_capability_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityPkgs(), CapabilityPkg)
    def get_owned_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCapabilities(), Capability)

class SystemComponentPkg(PropertyValuePkgContainer):
    """
    A package to contain the System and the Actors
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponentPkg"))
        elif isinstance(java_object, SystemComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_system_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedSystemComponentPkgs(), SystemComponentPkg)
    def get_owned_system(self):
        """
        """
        value =  self.get_java_object().getOwnedSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_owned_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)
    def get_owned_component_exchange_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class MissionPkg(PropertyValuePkgContainer):
    """
    A package to contain Missions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "MissionPkg"))
        elif isinstance(java_object, MissionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_mission_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedMissionPkgs(), MissionPkg)
    def get_owned_missions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedMissions(), Mission)

class Mission(CapellaElement):
    """
    High-level goal to which the System should contribute. To be fulfilled, a Mission should use a number of system Functions regrouped within one or more Capabilities
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Mission"))
        elif isinstance(java_object, Mission):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_exploited_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Exploited Capabilities")
    def get_involved_actors(self):
        """
        """
        res = []
        for system_comp in self.get_java_object().getInvolvedSystemComponents():
            if system_comp is not None:
                e_object_class = getattr(sys.modules["__main__"], "EObject")
                specific_cls = e_object_class.get_class(system_comp)
                if specific_cls is not None and specific_cls.__name__.endswith('Actor'):
                    res.append(specific_cls(system_comp))
        return res

class LogicalArchitecture(PropertyValuePkgContainer):
    """
    The element containing all definitions from the Logical Architecture.
    The Logical Architecture (or conceptual solution)&nbsp;aims at defining how the system will work in order to fulfil expectations
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalArchitecture"))
        elif isinstance(java_object, LogicalArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_logical_function_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedLogicalFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_realization_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_logical_component_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedLogicalComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_logical_system(self):
        """
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
    A package to contain LogicalFunctions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunctionPkg"))
        elif isinstance(java_object, LogicalFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_logical_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_owned_logical_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctions(), LogicalFunction)
    def get_owned_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class CapabilityRealizationPkg(PropertyValuePkgContainer):
    """
    A package to contain CapabilityRealizations
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealizationPkg"))
        elif isinstance(java_object, CapabilityRealizationPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_capability_realization_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizationPkgs(), CapabilityRealizationPkg)
    def get_owned_capability_realizations(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizations(), CapabilityRealization)

class LogicalComponentPkg(PropertyValuePkgContainer):
    """
    A package to contain the LogicalSystem, LogicalComponents and LogicalActors
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponentPkg"))
        elif isinstance(java_object, LogicalComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_logical_component_pkgs(self):
        """
        """
        value =  self.get_java_object().getOwnedLogicalComponentPkgs()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_owned_logical_system(self):
        """
        """
        value =  self.get_java_object().getOwnedLogicalSystem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_owned_logical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_component_exchange_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class PhysicalArchitecture(PropertyValuePkgContainer):
    """
    The element containing all definitions from the Physical Architecture.
    The Physical Architecture (or finalized solution)&nbsp;aims at defining how the system will be developed and built
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalArchitecture"))
        elif isinstance(java_object, PhysicalArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_physical_function_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedPhysicalFunctionPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_capability_realization_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_interface_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_physical_component_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedPhysicalComponentPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_physical_system(self):
        """
        """
        return self.get_physical_component_pkg().get_owned_physical_system()

class PhysicalFunctionPkg(PropertyValuePkgContainer):
    """
    A package to contain PhysicalFunctions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunctionPkg"))
        elif isinstance(java_object, PhysicalFunctionPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_physical_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_owned_physical_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctions(), PhysicalFunction)
    def get_owned_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCategories(), ExchangeCategory)

class PhysicalComponentPkg(PropertyValuePkgContainer):
    """
    A package to contain the PhysicalSystem, PhysicalComponents and PhysicalActors
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentPkg"))
        elif isinstance(java_object, PhysicalComponentPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_physical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_owned_physical_system(self):
        """
        """
        for value in self.get_owned_physical_components():
            if isinstance(value, PhysicalSystem):
                return value
        return None
    def get_owned_physical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_component_exchange_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)
    def get_owned_physical_link_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)

class AbstractPhysicalArtifact(CapellaElement):
    """
    An abstract type to defined the relation between elements of the Physical Architecture and ConfigurationItems
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "AbstractPhysicalArtifact"))
        elif isinstance(java_object, AbstractPhysicalArtifact):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_allocator_configuration_items(self):
        """
        """
        return create_e_list(self.get_java_object().getAllocatorConfigurationItems(), ConfigurationItem)

class PhysicalComponent(AbstractPhysicalArtifact):
    """
    A generic Physical Component which can be either a BehaviorPC or a NodePC
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
        elif isinstance(java_object, PhysicalComponent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if not java_object.isActor():
                if java_object.getNature().getName() == "UNSET":
                    JavaObject.__init__(self, java_object)
                elif java_object.getNature().getName() == "BEHAVIOR":
                    raise AttributeError("Passed component is a behavior physical component.")
                elif java_object.getNature().getName() == "NODE":
                    raise AttributeError("Passed component is a node physical component.")
            else:
                raise AttributeError("Passed component is an actor.")
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_owned_physical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_is_human(self):
        """
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value):
        """
        """
        self.get_java_object().setHuman(value)
    def get_involving_capability_realizations(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class EPBSArchitecture(PropertyValuePkgContainer):
    """
    The element containing all definitions from the End-Product Breakdown Structure.
    The End-Product Breakdown Structure aims at defining the construction strategy of the product, taking into account industrial and subcontracting constraints
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "EPBSArchitecture"))
        elif isinstance(java_object, EPBSArchitecture):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_capability_realization_pkg(self):
        """
        """
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_configuration_item_pkg(self):
        """
        """
        value =  self.get_java_object().getOwnedConfigurationItemPkg()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_data_pkg(self):
        """
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
    A package to contain ConfigurationItems
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItemPkg"))
        elif isinstance(java_object, ConfigurationItemPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_configuration_item_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_owned_configuration_items(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)

class ConfigurationItem(CapellaElement):
    """
    System part to be acquired or produced, in as many copies as the physical architecture requires
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItem"))
        elif isinstance(java_object, ConfigurationItem):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_item_identifier(self):
        """
        """
        return self.get_java_object().getItemIdentifier()
    def set_item_identifier(self, value):
        """
        """
        self.get_java_object().setItemIdentifier(value)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_owned_configuration_items(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_allocated_physical_artifacts(self):
        """
        """
        return create_e_list(self.get_java_object().getAllocatedPhysicalArtifacts(), AbstractPhysicalArtifact)

class StateMachine(CapellaElement):
    """
    State Machine is a way to define some of&nbsp;the expected behavior of the System, a Component or an external Actor
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateMachine"))
        elif isinstance(java_object, StateMachine):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_regions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)

class AbstractState(CapellaElement):
    """
    An abstract type to define the generic relation of modes and states
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "AbstractState"))
        elif isinstance(java_object, AbstractState):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_incoming(self):
        """
        """
        return create_e_list(self.get_java_object().getIncoming(), StateTransition)
    def get_outgoing(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoing(), StateTransition)
    def get_realized_states(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedAbstractStates(), AbstractState)
    def get_realizing_states(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingAbstractStates(), AbstractState)

class State(AbstractState):
    """
    A State is a context undergone by the system, an actor or a component in specific circumstances (for example imposed by the environment)
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "State"))
        elif isinstance(java_object, State):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_regions(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)
    def get_available_activities_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableActivitiesFunctions(), AbstractActivityFunction)
    def get_entry(self):
        """
        """
        return create_e_list(self.get_java_object().getEntry(), AbstractAction)
    def get_do(self):
        """
        """
        return create_e_list(self.get_java_object().getDo(), AbstractAction)
    def get_exit(self):
        """
        """
        return create_e_list(self.get_java_object().getExit(), AbstractAction)
    def get_available_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableFunctionalChains(), FunctionalChain)
    def get_available_operational_processes(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableOperationalProcesses(), OperationalProcess)
    def get_available_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableAbstractCapabilities(), AbstractCapability)

class Mode(State):
    """
    A Mode is a behavior expected from the system,&nbsp;an Actor or a component&nbsp;in chosen conditions
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "Mode"))
        elif isinstance(java_object, Mode):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Pseudostate(AbstractState):
    """
    A pseudo states are transitive states (meaning they don't remain active). They are used to define entry / exit point of a state machine, and to connect multiple transitions into more complex transition paths
    """
    def __init__(self, java_object = None, kind = "InitialPseudoState"):
        """
        """
        if java_object is None:
            if kind in ["ChoicePseudoState", "DeepHistoryPseudoState", "EntryPointPseudoState", "ExitPointPseudoState", "ForkPseudoState", "InitialPseudoState", "JoinPseudoState", "ShallowHistoryPseudoState", "TerminatePseudoState", "FinalState"]:
                JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), kind))
            else:
                raise ValueError("kind must be either \"ChoicePseudoState\", \"DeepHistoryPseudoState\", \"EntryPointPseudoState\", \"ExitPointPseudoState\", \"ForkPseudoState\", \"InitialPseudoState\", \"JoinPseudoState\", \"ShallowHistoryPseudoState\", \"TerminatePseudoState\", or \"FinalState\"")
        elif isinstance(java_object, Pseudostate):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        return self.java_object.eClass().getName()

class Region(CapellaElement):
    """
    A region is an orthogonal part of either a composite state or a state machine.
    Inside of a region, only one more or state can be active at a time
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "Region"))
        elif isinstance(java_object, Region):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_states(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedStates(), AbstractState)

class StateTransition(CapellaElement):
    """
    A possible transition between 2 modes or 2 states
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateTransition"))
        elif isinstance(java_object, StateTransition):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_trigger_description(self):
        """
        """
        return self.get_java_object().getTriggerDescription()
    def set_trigger_description(self, value):
        """
        """
        self.get_java_object().setTriggerDescription(value)
    def get_source(self):
        """
        """
        return capella_query_by_name(self, "Source")
    def get_target(self):
        """
        """
        return capella_query_by_name(self, "Target")
    def get_triggers(self):
        """
        """
        return create_e_list(self.get_java_object().getTriggers(), AbstractEvent)
    def get_guard(self):
        """
        """
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_guard(self, value):
        """
        """
        return self.get_java_object().setGuard(value.get_java_object())
    def get_effects(self):
        """
        """
        return create_e_list(self.get_java_object().getEffects(), AbstractAction)
    def get_realized_state_transitions(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedStateTransitions(), StateTransition)
    def get_realizing_state_transitions(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingStateTransitions(), StateTransition)

class AbstractAction(JavaObject):
    """
    A generic action which can be triggered by a Mode / State or a StateTransition
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/" + capella_version(), "AbstractAction"))
        elif isinstance(java_object, AbstractAction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class AbstractEvent(CapellaElement):
    """
    An generic event which can trigger a transition
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/" + capella_version(), "AbstractEvent"))
        elif isinstance(java_object, AbstractEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Scenario(CapellaElement):
    """
    A scenario of use of the system defined by a specific sequence
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "Scenario"))
        elif isinstance(java_object, Scenario):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_pre_condition(self):
        """
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value):
        """
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        """
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value):
        """
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_instance_roles(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedInstanceRoles(), InstanceRole)
    def get_owned_messages(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedMessages(), SequenceMessage)
    def get_owned_state_fragments(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedStateFragments(), StateFragment)
    def get_owned_combined_fragments(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedCombinedFragments(), CombinedFragment)
    def get_owned_constraint_durations(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedConstraintDurations(), ConstraintDuration)
    def get_referenced_scenarios(self):
        """
        """
        return create_e_list(self.get_java_object().getReferencedScenarios(), Scenario)
    def get_realized_scenarios(self):
        """
        """
        return capella_query_by_name(self, "Realized Scenarios")
    def get_realizing_scenarios(self):
        """
        """
        return capella_query_by_name(self, "Realizing Scenarios")

class InstanceRole(CapellaElement):
    """
    The involvement of an element (function, system, component or actor)&nbsp;in a scenario
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "InstanceRole"))
        elif isinstance(java_object, InstanceRole):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_represented_instance(self):
        """
        """
        return capella_query_by_name(self, "Represented Instance")

class AbstractInstance(JavaObject):
    """
    A generic element which can be involved in a scenario as an InstanceRole
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "AbstractInstance"))
        elif isinstance(java_object, AbstractInstance):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class SequenceMessage(CapellaElement):
    """
    An exchange between InstanceRole performed in the frame of a scenario
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "SequenceMessage"))
        elif isinstance(java_object, SequenceMessage):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_sending_instance_role(self):
        """
        """
        value =  self.get_java_object().getSendingInstanceRole()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_receiving_instance_role(self):
        """
        """
        value =  self.get_java_object().getReceivingInstanceRole()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_invoked_exchange(self):
        """
        """
        value =  self.get_java_object().getInvokedExchange()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_exchanged_items(self):
        """
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_invoked_operation(self):
        """
        """
        return capella_query_by_name(self, "Invoked Operation")
    def get_exchange_context(self):
        """
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
    def get_invoking_sequence_messages(self):
        """
        """
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class StateFragment(CapellaElement):
    """
    The call of a function or mode / state&nbsp;by an InstanceRole in the context of a scenario
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "StateFragment"))
        elif isinstance(java_object, StateFragment):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_covered_instance_role(self):
        """
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
        """
        return capella_query_by_name(self, "Related State")
    def get_related_activity_function(self):
        """
        """
        value =  self.get_java_object().getRelatedActivityFunction()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)

class CombinedFragment(CapellaElement):
    """
    The identification of a specific operator (ALT, OPT, LOOP...)&nbsp;in the sequence of a scenario
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "CombinedFragment"))
        elif isinstance(java_object, CombinedFragment):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_operator(self):
        """
        """
        value =  self.get_java_object().getOperator()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_operands(self):
        """
        """
        return create_e_list(self.get_java_object().getOperands(), Operand)
    def get_covered_instance_roles(self):
        """
        """
        return create_e_list(self.get_java_object().getCoveredInstanceRoles(), InstanceRole)

class Operand(CapellaElement):
    """
    A specific "region" in a Combined Fragment
    For example, an ALTERNATIVE contains one operand for each of the alternative conditions
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "InteractionOperand"))
        elif isinstance(java_object, Operand):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_guard(self):
        """
        """
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_guard(self, value):
        """
        """
        return self.get_java_object().setGuard(value.get_java_object())
    def get_referenced_messages(self):
        """
        """
        return create_e_list(self.get_java_object().getReferencedMessages(), SequenceMessage)
    def get_referenced_fragments(self):
        """
        """
        return create_e_list(self.get_java_object().getReferencedFragments(), StateFragment)

class ConstraintDuration(CapellaElement):
    """
    A constraint about the execution time of a scenario defined between 2 points
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "ConstraintDuration"))
        elif isinstance(java_object, ConstraintDuration):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_duration(self):
        """
        """
        return self.get_java_object().getDuration()
    def set_duration(self, value):
        """
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
    def get_contained_physical_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedPhysicalPorts(), PhysicalPort)
    def get_physical_links(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedLinks(), PhysicalLink)
    def get_involving_physical_paths(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingPhysicalPaths(), PhysicalPath)
    def get_owned_physical_link_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalLinkCategories(), PhysicalLinkCategory)
    def get_owned_physical_paths(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalPaths(), PhysicalPath)

class PhysicalPort(AbstractPhysicalArtifact):
    """
    A port on a Node component defining a physical interaction point
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPort"))
        elif isinstance(java_object, PhysicalPort):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_physical_links(self):
        """
        """
        return capella_query_by_name(self, "Physical Links")
    def get_allocated_component_ports(self):
        """
        """
        return capella_query_by_name(self, "Allocated Component Ports")
    def get_realized_physical_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalPorts(), PhysicalPort)
    def get_realizing_physical_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalPorts(), PhysicalPort)

class PhysicalLink(AbstractPhysicalArtifact):
    """
    Means of communication, transport or routing between two Node components, used as a support for behavioral exchanges
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLink"))
        elif isinstance(java_object, PhysicalLink):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_connected_physical_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getConnectedPhysicalPorts(), PhysicalPort)
    def get_categories(self):
        """
        """
        return capella_query_by_name(self, "Categories")
    def get_involving_physical_paths(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingPhysicalPaths(), PhysicalPath)
    def get_connected_components(self):
        """
        """
        return create_e_list(self.get_java_object().getConnectedComponents(), Node)
    def get_allocated_component_exchanges(self):
        """
        """
        return capella_query_by_name(self, "Allocated Component Exchanges")
    def get_realized_physical_links(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalLinks(), PhysicalLink)
    def get_realizing_physical_links(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalLinks(), PhysicalLink)

class PhysicalLinkCategory(CapellaElement):
    """
    A regroupement of PhysicalLinks for graphical simplification of diagrams
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLinkCategory"))
        elif isinstance(java_object, PhysicalLinkCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_links(self):
        """
        """
        return create_e_list(self.get_java_object().getLinks(), PhysicalLink)

class PhysicalPath(CapellaElement):
    """
    Set of Physical Links defining a continuous path likely to route one or more behavioral exchanges
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPath"))
        elif isinstance(java_object, PhysicalPath):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_involved_physical_links(self):
        """
        """
        return capella_query_by_name(self, "Involved Physical Links")
    def get_involved_node_p_cs(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedNodePCs(), Node)
    def get_allocated_component_exchanges(self):
        """
        """
        return capella_query_by_name(self, "Allocated Component Exchanges")
    def get_realized_physical_paths(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedPhysicalPaths(), PhysicalPath)
    def get_realizing_physical_paths(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalPaths(), PhysicalPath)

class InterfacePkg(PropertyValuePkgContainer):
    """
    A package to contain Interfaces
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "InterfacePkg"))
        elif isinstance(java_object, InterfacePkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_interface_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedInterfacePkgs(), InterfacePkg)
    def get_owned_interfaces(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedInterfaces(), Interface)
    def get_owned_exchange_items(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedExchangeItems(), ExchangeItem)

class Interface(CapellaElement):
    """
    The definition of ExchangeItems which can be send / received by a ComponentPort
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Interface"))
        elif isinstance(java_object, Interface):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_owned_exchange_item_allocations(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedExchangeItemAllocations(), ExchangeItemAllocation)
    def get_exchange_items(self):
        """
        """
        return capella_query_by_name(self, "Exchange Items")
    def get_providing_component_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getProvidingComponentPorts(), ComponentPort)
    def get_requiring_component_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRequiringComponentPorts(), ComponentPort)
    def get_user_components(self):
        """
        """
        return create_e_list(self.get_java_object().getUserComponents(), BehavioralComponent)
    def get_implementor_components(self):
        """
        """
        return create_e_list(self.get_java_object().getImplementorComponents(), BehavioralComponent)
    def get_super(self):
        """
        """
        return create_e_list(self.get_java_object().getSuper(), Interface)
    def get_sub(self):
        """
        """
        return create_e_list(self.get_java_object().getSub(), Interface)

class ExchangeItemAllocation(CapellaElement):
    """
    The involvement of an ExchangeItem by an Interface.
    Mainly used for the involvement of ExchangeItems in Interface Scenarios based on the definition of Interfaces between components
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "ExchangeItemAllocation"))
        elif isinstance(java_object, ExchangeItemAllocation):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_transmission_protocol(self):
        """
        """
        value =  self.get_java_object().getTransmissionProtocol()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_transmission_protocol(self, value):
        """
        """
        return self.get_java_object().setTransmissionProtocol(value.get_java_object())
    def get_acquisition_protocol(self):
        """
        """
        value =  self.get_java_object().getAcquisitionProtocol()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_acquisition_protocol(self, value):
        """
        """
        return self.get_java_object().setAcquisitionProtocol(value.get_java_object())
    def get_allocated_item(self):
        """
        """
        value =  self.get_java_object().getAllocatedItem()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocated_item(self, value):
        """
        """
        return self.get_java_object().setAllocatedItem(value.get_java_object())
    def get_invoking_sequence_messages(self):
        """
        """
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class ExchangeItem(AbstractAction, AbstractEvent, AbstractInstance):
    """
    Ordered set of references to elements carried together during an interaction or exchange between functions, components and actors. The elements are carried simultaneously, in the same conditions, with the same non-functional properties. The “elements” are called data
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItem"))
        elif isinstance(java_object, ExchangeItem):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_abstract(self):
        """
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        """
        """
        self.get_java_object().setAbstract(value)
    def get_final(self):
        """
        """
        return self.get_java_object().isFinal()
    def set_final(self, value):
        """
        """
        self.get_java_object().setFinal(value)
    def get_exchange_mechanism(self):
        """
        """
        value =  self.get_java_object().getExchangeMechanism()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_exchange_mechanism(self, value):
        """
        """
        return self.get_java_object().setExchangeMechanism(value.get_java_object())
    def get_owned_elements(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedElements(), ExchangeItemElement)
    def get_allocator_interfaces(self):
        """
        """
        return create_e_list(self.get_java_object().getAllocatorInterfaces(), Interface)
    def get_super(self):
        """
        """
        return create_e_list(self.get_java_object().getSuper(), ExchangeItem)
    def get_sub(self):
        """
        """
        return create_e_list(self.get_java_object().getSub(), ExchangeItem)
    def get_realized_exchange_items(self):
        """
        """
        return capella_query_by_name(self, "Realized Exchange Items")
    def get_realizing_exchange_items(self):
        """
        """
        return capella_query_by_name(self, "Realizing Exchange Items")
    def get_realizing_operations(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingOperations(), Operation)

class ExchangeItemElement(CapellaElement):
    """
    A part of the information contained by an ExchangeItem
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItemElement"))
        elif isinstance(java_object, ExchangeItemElement):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_type(self):
        """
        """
        return capella_query_by_name(self, "Type")

class FunctionPort(CapellaElement):
    """
    An generic FunctionPort to define the allocation with ComponentPorts
    A Function Port specify what a Function is capable of producing or is requiring
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionPort"))
        elif isinstance(java_object, FunctionPort):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_allocator_component_port(self):
        """
        """
        value =  self.get_java_object().getRepresentedComponentPort()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocator_component_port(self, value):
        """
        """
        return self.get_java_object().setRepresentedComponentPort(value.get_java_object())

class FunctionInputPort(FunctionPort):
    """
    An FunctionInputPort defines what a Function is requiring
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionInputPort"))
        elif isinstance(java_object, FunctionInputPort):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_incoming_functional_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getIncomingFunctionalExchanges(), FunctionalExchange)
    def get_incoming_exchange_items(self):
        """
        """
        return create_e_list(self.get_java_object().getIncomingExchangeItems(), ExchangeItem)
    def get_realized_function_input_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedFunctionInputPorts(), FunctionInputPort)
    def get_realizing_function_input_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingFunctionInputPorts(), FunctionInputPort)

class FunctionOutputPort(FunctionPort):
    """
    A FunctionOutputPort defines what a Function is capable of producing
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionOutputPort"))
        elif isinstance(java_object, FunctionOutputPort):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_outgoing_functional_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoingFunctionalExchanges(), FunctionalExchange)
    def get_outgoing_exchange_items(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoingExchangeItems(), ExchangeItem)
    def get_realized_function_output_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedFunctionOutputPorts(), FunctionOutputPort)
    def get_realizing_function_output_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingFunctionOutputPorts(), FunctionOutputPort)

class FunctionalExchange(AbstractEvent, AbstractExchange):
    """
    A functional exchange represents a dependency between a source function and a target one. Exchanges connect Function Ports, which specify what a Function is capable of producing or is requiring.
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalExchange"))
        elif isinstance(java_object, FunctionalExchange):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_source_port(self):
        """
        """
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source_port(self, value):
        """
        """
        return self.get_java_object().setSource(value.get_java_object())
    def get_target_port(self):
        """
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target_port(self, value):
        """
        """
        return self.get_java_object().setTarget(value.get_java_object())
    def get_source_function(self):
        """
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
    def get_target_function(self):
        """
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
    def get_exchanged_items(self):
        """
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_involving_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_categories(self):
        """
        """
        return capella_query_by_name(self, "Categories")
    def get_allocating_component_exchange(self):
        """
        """
        return capella_query_by_name(self, "Allocating Component Exchange")
    def get_realized_functional_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedFunctionalExchanges(), FunctionalExchange)
    def get_realizing_functional_exchanges(self):
        """
        """
        return capella_query_by_name(self, "Realizing Functional Exchanges")
    def get_realized_interactions(self):
        """
        """
        return capella_query_by_name(self, "Realized Interactions")

class ExchangeCategory(CapellaElement):
    """
    A regroupement of FunctionalExchanges for graphical simplification of diagrams
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ExchangeCategory"))
        elif isinstance(java_object, ExchangeCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getExchanges(), FunctionalExchange)

class FunctionalChain(CapellaElement):
    """
    Describe the system behaviour in a particular usage context with references towards Functions and Functional Exchanges
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChain"))
        elif isinstance(java_object, FunctionalChain):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_pre_condition(self):
        """
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value):
        """
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        """
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value):
        """
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_involved_functions(self):
        """
        """
        res = []
        for involvment in self.get_java_object().getOwnedFunctionalChainInvolvements():
            if involvment.eClass().getName() == 'FunctionalChainInvolvementFunction':
                involvedElement = involvment.getInvolvedElement()
                if involvedElement is not None:
                    e_object_class = getattr(sys.modules["__main__"], "EObject")
                    specific_cls = e_object_class.get_class(involvedElement)
                    res.append(specific_cls(involvedElement))
        return res
    def get_involved_functional_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedFunctionalExchanges(), FunctionalExchange)
    def get_involved_functional_chains(self):
        """
        """
        return capella_query_by_name(self, "Involved Functional Chains")
    def get_involving_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Involving Capabilities")
    def get_available_in_states(self):
        """
        """
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_realized_operational_processes(self):
        """
        """
        return capella_query_by_name(self, "Realized Operational Processes")
    def get_realized_functional_chains(self):
        """
        """
        return capella_query_by_name(self, "Realized Functional Chains")
    def get_realizing_functional_chains(self):
        """
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
    def get_contained_component_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedComponentPorts(), ComponentPort)
    def get_incoming_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getIncomingComponentExchanges(), ComponentExchange)
    def get_outgoing_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoingComponentExchanges(), ComponentExchange)
    def get_inout_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getInoutComponentExchanges(), ComponentExchange)
    def get_allocated_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getAllocatedFunctions(), Function)
    def get_used_interfaces(self):
        """
        """
        return create_e_list(self.get_java_object().getUsedInterfaces(), Interface)
    def get_implemented_interfaces(self):
        """
        """
        return create_e_list(self.get_java_object().getImplementedInterfaces(), Interface)
    def get_owned_state_machines(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_owned_component_exchange_categories(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedComponentExchangeCategories(), ComponentExchangeCategory)

class ComponentPort(CapellaElement):
    """
    A port on a BehavioralComponent defining a logical interaction point
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentPort"))
        elif isinstance(java_object, ComponentPort):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_orientation(self):
        """
        """
        value =  self.get_java_object().getOrientation()
        if value is None:
            return value
        else:
            return value.getName()
    def get_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getComponentExchanges(), ComponentExchange)
    def get_allocated_function_ports(self):
        """
        """
        return capella_query_by_name(self, "Allocated Function Ports")
    def get_provided_interfaces(self):
        """
        """
        return capella_query_by_name(self, "Provided Interfaces")
    def get_required_interfaces(self):
        """
        """
        return capella_query_by_name(self, "Required Interfaces")
    def get_allocating_physical_ports(self):
        """
        """
        return capella_query_by_name(self, "Allocating Physical Ports")
    def get_realized_component_ports(self):
        """
        """
        return capella_query_by_name(self, "Realized Component Ports")
    def get_realizing_component_ports(self):
        """
        """
        return capella_query_by_name(self, "Realizing Component Ports")

class ComponentExchange(CapellaElement, AbstractExchange):
    """
    Represent the interactions between Logical / Behavioral&nbsp;Components. Exchanges connects Component Ports.
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchange"))
        elif isinstance(java_object, ComponentExchange):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_connected_component_ports(self):
        """
        """
        return create_e_list(self.get_java_object().getConnectedComponentPorts(), ComponentPort)
    def get_connected_components(self):
        """
        """
        return capella_query_by_name(self, "Connected Components")
    def get_categories(self):
        """
        """
        return capella_query_by_name(self, "Categories")
    def get_allocated_functional_exchanges(self):
        """
        """
        return capella_query_by_name(self, "Allocated Functional Exchanges")
    def get_convoyed_informations(self):
        """
        """
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_allocating_physical_link(self):
        """
        """
        return capella_query_by_name(self, "Allocating Physical Link")
    def get_allocating_physical_path(self):
        """
        """
        return capella_query_by_name(self, "Allocating Physical Path")
    def get_realized_communication_means(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedCommunicationMeans(), CommunicationMean)
    def get_realized_component_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedComponentExchanges(), ComponentExchange)
    def get_realizing_component_exchanges(self):
        """
        """
        return capella_query_by_name(self, "Realizing Component Exchanges")

class ComponentExchangeCategory(CapellaElement):
    """
    A regroupement of ComponentExchanges for graphical simplification of diagrams
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchangeCategory"))
        elif isinstance(java_object, ComponentExchangeCategory):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getExchanges(), ComponentExchange)

class AbstractCapability(PropertyValuePkgContainer):
    """
    An abstract type to define the generic relations of all capabilities (operational and system)
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "AbstractCapability"))
        elif isinstance(java_object, AbstractCapability):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_pre_condition(self):
        """
        """
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_pre_condition(self, value):
        """
        """
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        """
        """
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_post_condition(self, value):
        """
        """
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_scenarios(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedScenarios(), Scenario)
    def get_super(self):
        """
        """
        return create_e_list(self.get_java_object().getSuper(), AbstractCapability)
    def get_sub(self):
        """
        """
        return create_e_list(self.get_java_object().getSub(), AbstractCapability)
    def get_included_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Included Capabilities")
    def get_including_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Including Capabilities")
    def get_extended_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Extended Capabilities")
    def get_extending_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Extending Capabilities")
    def get_available_in_states(self):
        """
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
    def get_owned_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involved_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedFunctionalChains(), FunctionalChain)
    def get_involved_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedAbstractFunctions(), Function)

class DataValue(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "DataValue"))
        elif isinstance(java_object, DataValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class LiteralBooleanValue(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralBooleanValue"))
        elif isinstance(java_object, LiteralBooleanValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class BooleanReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BooleanReference"))
        elif isinstance(java_object, BooleanReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class EnumerationReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationReference"))
        elif isinstance(java_object, EnumerationReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class LiteralStringValue(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralStringValue"))
        elif isinstance(java_object, LiteralStringValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class StringReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "StringReference"))
        elif isinstance(java_object, StringReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class LiteralNumericValue(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralNumericValue"))
        elif isinstance(java_object, LiteralNumericValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class NumericReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "NumericReference"))
        elif isinstance(java_object, NumericReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class ComplexValue(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValue"))
        elif isinstance(java_object, ComplexValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class ComplexValueReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValueReference"))
        elif isinstance(java_object, ComplexValueReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class BinaryExpression(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BinaryExpression"))
        elif isinstance(java_object, BinaryExpression):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class UnaryExpression(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "UnaryExpression"))
        elif isinstance(java_object, UnaryExpression):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class CollectionValueReference(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValueReference"))
        elif isinstance(java_object, CollectionValueReference):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class CollectionValue(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValue"))
        elif isinstance(java_object, CollectionValue):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class DataPkg(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "DataPkg"))
        elif isinstance(java_object, DataPkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class DataType(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "DataType"))
        elif isinstance(java_object, DataType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Class(DataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Class"))
        elif isinstance(java_object, Class):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_abstract(self):
        """
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        """
        """
        self.get_java_object().setAbstract(value)
    def get_final(self):
        """
        """
        return self.get_java_object().isFinal()
    def set_final(self, value):
        """
        """
        self.get_java_object().setFinal(value)
    def get_primitive(self):
        """
        """
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value):
        """
        """
        self.get_java_object().setPrimitive(value)
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_properties(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedProperties(), Property)
    def get_contained_operations(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Collection(DataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Collection"))
        elif isinstance(java_object, Collection):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_ordered(self):
        """
        """
        return self.get_java_object().isOrdered()
    def set_ordered(self, value):
        """
        """
        self.get_java_object().setOrdered(value)
    def get_unique(self):
        """
        """
        return self.get_java_object().isUnique()
    def set_unique(self, value):
        """
        """
        self.get_java_object().setUnique(value)
    def get_min_inclusive(self):
        """
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        """
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        """
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        """
        """
        self.get_java_object().setMaxInclusive(value)
    def get_abstract(self):
        """
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        """
        """
        self.get_java_object().setAbstract(value)
    def get_final(self):
        """
        """
        return self.get_java_object().isFinal()
    def set_final(self, value):
        """
        """
        self.get_java_object().setFinal(value)
    def get_primitive(self):
        """
        """
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value):
        """
        """
        self.get_java_object().setPrimitive(value)
    def get_collection_kind(self):
        """
        """
        value =  self.get_java_object().getCollectionKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_collection_kind(self, value):
        """
        """
        return self.get_java_object().setCollectionKind(value.get_java_object())
    def get_aggregation_kind(self):
        """
        """
        value =  self.get_java_object().getAggregationKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_aggregation_kind(self, value):
        """
        """
        return self.get_java_object().setAggregationKind(value.get_java_object())
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_operations(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)
    def get_min_card(self):
        """
        """
        value =  self.get_java_object().getMinCard()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_card(self):
        """
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
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Union"))
        elif isinstance(java_object, Union):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_final(self):
        """
        """
        return self.get_java_object().isFinal()
    def set_final(self, value):
        """
        """
        self.get_java_object().setFinal(value)
    def get_contained_union_properties(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedUnionProperties(), UnionProperty)
    def get_discriminant(self):
        """
        """
        value =  self.get_java_object().getDiscriminant()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_discriminant(self, value):
        """
        """
        return self.get_java_object().setDiscriminant(value.get_java_object())
    def get_default_property(self):
        """
        """
        value =  self.get_java_object().getDefaultProperty()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_property(self, value):
        """
        """
        return self.get_java_object().setDefaultProperty(value.get_java_object())
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_contained_operations(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Association(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Association"))
        elif isinstance(java_object, Association):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Property(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Property"))
        elif isinstance(java_object, Property):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_type(self):
        """
        """
        return capella_query_by_name(self, "Type")

class UnionProperty(Property):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "UnionProperty"))
        elif isinstance(java_object, UnionProperty):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Operation(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Service"))
        elif isinstance(java_object, Operation):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_realized_exchange_items(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedExchangeItems(), ExchangeItem)
    def get_owned_parameters(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedParameters(), Parameter)
    def get_thrown_exceptions(self):
        """
        """
        return create_e_list(self.get_java_object().getThrownExceptions(), Exception)

class Parameter(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Parameter"))
        elif isinstance(java_object, Parameter):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Exception(JavaObject):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/" + capella_version(), "Exception"))
        elif isinstance(java_object, Exception):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_abstract(self):
        """
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        """
        """
        self.get_java_object().setAbstract(value)
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self):
        """
        """
        return create_e_list(self.get_java_object().getSuper(), Exception)
    def get_sub(self):
        """
        """
        return create_e_list(self.get_java_object().getSub(), Exception)

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
    def get_abstract(self):
        """
        """
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        """
        """
        self.get_java_object().setAbstract(value)
    def get_final(self):
        """
        """
        return self.get_java_object().isFinal()
    def set_final(self, value):
        """
        """
        self.get_java_object().setFinal(value)
    def get_discrete(self):
        """
        """
        return self.get_java_object().isDiscrete()
    def set_discrete(self, value):
        """
        """
        self.get_java_object().setDiscrete(value)
    def get_visibility(self):
        """
        """
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_visibility(self, value):
        """
        """
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self):
        """
        """
        return create_e_list(self.get_java_object().getSuper(), PrimitiveDataType)
    def get_sub(self):
        """
        """
        return create_e_list(self.get_java_object().getSub(), PrimitiveDataType)
    def get_realized_informations(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedDataTypes(), PrimitiveDataType)
    def get_realizing_informations(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingDataTypes(), PrimitiveDataType)

class Enumeration(PrimitiveDataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "Enumeration"))
        elif isinstance(java_object, Enumeration):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_min_inclusive(self):
        """
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        """
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        """
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        """
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        """
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        """
        """
        self.get_java_object().setPattern(value)
    def get_owned_literals(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationLiteral)
    def get_default_value(self):
        """
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_value(self, value):
        """
        """
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_min_value(self):
        """
        """
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_min_value(self, value):
        """
        """
        return self.get_java_object().setMinValue(value.get_java_object())
    def get_max_value(self):
        """
        """
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_max_value(self, value):
        """
        """
        return self.get_java_object().setMaxValue(value.get_java_object())
    def get_null_value(self):
        """
        """
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_null_value(self, value):
        """
        """
        return self.get_java_object().setNullValue(value.get_java_object())
    def get_domain_type(self):
        """
        """
        value =  self.get_java_object().getDomainType()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_domain_type(self, value):
        """
        """
        return self.get_java_object().setDomainType(value.get_java_object())

class EnumerationLiteral(DataValue):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationLiteral"))
        elif isinstance(java_object, EnumerationLiteral):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class BooleanType(PrimitiveDataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "BooleanType"))
        elif isinstance(java_object, BooleanType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_literals(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLiterals(), LiteralBooleanValue)
    def get_default_value(self):
        """
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_default_value(self, value):
        """
        """
        return self.get_java_object().setDefaultValue(value.get_java_object())

class StringType(PrimitiveDataType):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "StringType"))
        elif isinstance(java_object, StringType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_min_inclusive(self):
        """
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        """
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        """
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        """
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        """
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        """
        """
        self.get_java_object().setPattern(value)
    def get_min_length(self):
        """
        """
        value =  self.get_java_object().getMinLength()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_length(self):
        """
        """
        value =  self.get_java_object().getMaxLength()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_default_value(self):
        """
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_null_value(self):
        """
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
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "NumericType"))
        elif isinstance(java_object, NumericType):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_min_inclusive(self):
        """
        """
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        """
        """
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        """
        """
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        """
        """
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        """
        """
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        """
        """
        self.get_java_object().setPattern(value)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_min_value(self):
        """
        """
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_max_value(self):
        """
        """
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_default_value(self):
        """
        """
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_null_value(self):
        """
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
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "PhysicalQuantity"))
        elif isinstance(java_object, PhysicalQuantity):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_unit(self):
        """
        """
        value =  self.get_java_object().getUnit()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_unit(self, value):
        """
        """
        return self.get_java_object().setUnit(value.get_java_object())

class Unit(CapellaElement):
    """
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Unit"))
        elif isinstance(java_object, Unit):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class SystemEngineering(PropertyValuePkgContainer):
    """
    The main element in the definition of a Capella model. Contains the perspectives of the Arcadia methodology
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering"))
        elif isinstance(java_object, SystemEngineering):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_rec_catalogs(self):
        """
        """
        res = []
        for extension in self.get_java_object().getOwnedExtensions():
            if extension.eClass().getName() == "RecCatalog" and extension.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/common/re/" + capella_version():
                res.append(RecCatalog(extension))
        return res
    def get_operational_analysis(self):
        """
        """
        for oa in self.get_java_object().getContainedOperationalAnalysis():
            return OperationalAnalysis(oa)
    def get_system_analysis(self):
        """
        """
        for sa in self.get_java_object().getContainedSystemAnalysis():
            return SystemAnalysis(sa)
    def get_logical_architecture(self):
        """
        """
        for la in self.get_java_object().getContainedLogicalArchitectures():
            return LogicalArchitecture(la)
    def get_physical_architecture(self):
        """
        """
        for pa in self.get_java_object().getContainedPhysicalArchitectures():
            return PhysicalArchitecture(pa)
    def get_e_p_b_s_architecture(self):
        """
        """
        for epbsa in self.get_java_object().getContainedEPBSArchitectures():
            return EPBSArchitecture(epbsa)

class PropertyValuePkg(PropertyValuePkgContainer):
    """
    A package to contain PropertyValues&nbsp;and/or&nbsp;PropertyValueGroups
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValuePkg"))
        elif isinstance(java_object, PropertyValuePkg):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)

class Interaction(AbstractEvent):
    """
    Oriented dependency between Operational Activities
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalExchange"))
        elif isinstance(java_object, Interaction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_source(self):
        """
        """
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_source(self, value):
        """
        """
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        """
        """
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_target(self, value):
        """
        """
        return self.get_java_object().setTarget(value.get_java_object())
    def get_allocating_communication_mean(self):
        """
        """
        value =  self.get_java_object().getAllocatingCommunicationMean()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_allocating_communication_mean(self, value):
        """
        """
        return self.get_java_object().setAllocatingCommunicationMean(value.get_java_object())
    def get_involving_operational_processes(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalProcesses(), OperationalProcess)
    def get_exchanged_items(self):
        """
        """
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_realizing_functional_exchanges(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingFunctionalExchanges(), FunctionalExchange)

class OperationalCapability(AbstractCapability):
    """
    An operational capability is an ability, expected of one or more operational entities / actors. An operational capability is characterized by a set of operational processes and scenarios
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapability"))
        elif isinstance(java_object, OperationalCapability):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_owned_operational_processes(self):
        """
        """
        return capella_query_by_name(self, "Owned Operational Processes")
    def get_involved_operational_processes(self):
        """
        """
        return capella_query_by_name(self, "Involved Operational Processes")
    def get_involved_operational_activities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedOperationalActivities(), OperationalActivity)
    def get_involved_entities(self):
        """
        """
        return capella_query_by_name(self, "Involved Entities")
    def get_realizing_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Realizing Capabilities")

class OperationalEntity(OperationalActor):
    """
    An Operational Entity is a real world entity (other system, device, group or organisation…) carrying Operational Activities to which the system is likely to contribute
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "Entity"))
        elif isinstance(java_object, OperationalEntity):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if not java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed entity is an actor.")
    def get_owned_entities(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalEntity)

class Capability(AbstractSystemCapability):
    """
    The ability of the system to supply a service contributing to fulfilling one or more Missions. A Capability represents a system usage context. It is characterized by a set of Functional Chains and Scenarios it references.
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Capability"))
        elif isinstance(java_object, Capability):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_purpose_missions(self):
        """
        """
        return create_e_list(self.get_java_object().getPurposeMissions(), Mission)
    def get_realized_operational_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Realized Operational Capabilities")
    def get_realizing_capability_realizations(self):
        """
        """
        return capella_query_by_name(self, "Realizing Capability Realizations")
    def get_involved_system_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedSystemActors(), SystemActor)

class System(BehavioralComponent, Node):
    """
    Set of elements functioning as a whole, responding to customer and user demand and needs
    The System defined in the SystemAnalysis is seen as a black box
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponent"))
        elif isinstance(java_object, System):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")

class SystemActor(BehavioralComponent, Node):
    """
    Entity (human or not) that is external to the System (in term of responsibility), interacting with it, via its interfaces
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponent"))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, SystemActor):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
    def get_is_human(self):
        """
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value):
        """
        """
        self.get_java_object().setHuman(value)
    def get_owned_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)
    def get_owned_system_component_pkgs(self):
        """
        """
        value =  self.get_java_object().getOwnedSystemComponentPkgs()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def get_involving_missions(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingMissions(), Mission)
    def get_realized_operational_entities(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedOperationalEntities(), OperationalActor)
    def get_involving_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_realizing_logical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingLogicalActors(), LogicalActor)

class CapabilityRealization(AbstractSystemCapability):
    """
    The implementation of the system Capabilities in Logical Architecture and Physical Architecture
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealization"))
        elif isinstance(java_object, CapabilityRealization):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_realized_capabilities(self):
        """
        """
        return capella_query_by_name(self, "Realized Capabilities")
    def get_realized_capability_realizations(self):
        """
        """
        return capella_query_by_name(self, "Realized Capability Realizations")
    def get_realizing_capability_realizations(self):
        """
        """
        return capella_query_by_name(self, "Realizing Capability Realizations")
    def get_involved_logical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedLogicalActors(), LogicalActor)
    def get_involved_logical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedLogicalComponents(), LogicalComponent)
    def get_involved_physical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedPhysicalComponents(), PhysicalComponent)
    def get_involved_physical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvedPhysicalActors(), PhysicalActor)

class LogicalSystem(BehavioralComponent, Node):
    """
    The definition of the system in Logical Architecture
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent"))
        elif isinstance(java_object, LogicalSystem):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")
    def get_owned_logical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)

class LogicalComponent(BehavioralComponent):
    """
    Logical Components are the artefacts enabling a notional decomposition of the system as a "white box", independently from any technological solutions, but dealing with major system decomposition constraints
    Logical components are identified according to logical abstractions (i.e. functional grouping, logical interfaces)
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent"))
        elif isinstance(java_object, LogicalComponent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if not java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is an actor.")
    def get_owned_logical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_is_human(self):
        """
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value):
        """
        """
        self.get_java_object().setHuman(value)
    def get_realizing_behavior_p_cs(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingBehaviorPCs(), BehaviorPC)
    def get_involving_capability_realizations(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class LogicalActor(BehavioralComponent, Node):
    """
    An external Actor defined in the Logical Architecture
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent"))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, LogicalActor):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
    def get_owned_logical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_realized_system_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedSystemActors(), SystemActor)
    def get_is_human(self):
        """
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value):
        """
        """
        self.get_java_object().setHuman(value)
    def get_realizing_physical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizingPhysicalActors(), PhysicalActor)
    def get_involving_capability_realizations(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class PhysicalSystem(CapellaElement, Node):
    """
    The definition of the system in Physical Architecture
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, PhysicalSystem):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if is_system(java_object):
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not a system.")
    def get_owned_physical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)

class BehaviorPC(PhysicalComponent, BehavioralComponent):
    """
    System component in charge of implementing / realizing some of the functions devoted to the system
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
            self.get_java_object().setNature(get_enum_literal("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentNature", "BEHAVIOR"))
        elif isinstance(java_object, BehaviorPC):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
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
    def get_deploying_node_p_c(self):
        """
        """
        value =  self.get_java_object().getDeployingNodePC()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_deploying_node_p_c(self, value):
        """
        """
        return self.get_java_object().setDeployingNodePC(value.get_java_object())
    def get_realized_logical_components(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedLogicalComponents(), LogicalComponent)

class NodePC(PhysicalComponent, Node):
    """
    Component hosting a number of behavioral components, providing them with the resource they require to function and to interact with their environment
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
            self.get_java_object().setNature(get_enum_literal("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentNature", "NODE"))
        elif isinstance(java_object, NodePC):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
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
    def get_deployed_behavior_p_cs(self):
        """
        """
        res = []
        for pc in self.java_object.getDeployedPhysicalComponents():
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(pc)
            if specific_cls == BehaviorPC:
                res.append(specific_cls(pc))
        return res
    def get_owned_state_machines(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class PhysicalActor(BehavioralComponent, Node):
    """
    An external Actor defined in the Physical Architecture
    """
    def __init__(self, java_object = None):
        """
        """
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
            self.get_java_object().setActor(True)
        elif isinstance(java_object, PhysicalActor):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            if java_object.isActor():
                JavaObject.__init__(self, java_object)
            else:
                raise AttributeError("Passed component is not an actor.")
    def get_owned_physical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_component_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_realized_logical_actors(self):
        """
        """
        return create_e_list(self.get_java_object().getRealizedLogicalActors(), LogicalActor)
    def get_is_human(self):
        """
        """
        return self.get_java_object().isHuman()
    def set_is_human(self, value):
        """
        """
        self.get_java_object().setHuman(value)
    def get_involving_capability_realizations(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class ChangeEvent(AbstractEvent):
    """
    An event defined by WHEN something occurs
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "ChangeEvent"))
        elif isinstance(java_object, ChangeEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_expression(self):
        """
        """
        return self.get_java_object().getExpression()
    def set_expression(self, value):
        """
        """
        self.get_java_object().setExpression(value)

class TimeEvent(AbstractEvent):
    """
    An event defined by AT a given time, or AFTER a certain time
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "TimeEvent"))
        elif isinstance(java_object, TimeEvent):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_expression(self):
        """
        """
        return self.get_java_object().getExpression()
    def set_expression(self, value):
        """
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
    def get_available_in_states(self):
        """
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
    def get_kind(self):
        """
        """
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            e_object_class = getattr(sys.modules["__main__"], "EObject")
            specific_cls = e_object_class.get_class(value)
            return specific_cls(value)
    def set_kind(self, value):
        """
        """
        return self.get_java_object().setKind(value.get_java_object())
    def get_condition(self):
        """
        """
        return self.get_java_object().getCondition()
    def set_condition(self, value):
        """
        """
        self.get_java_object().setCondition(value)
    def get_inputs(self):
        """
        """
        return create_e_list(self.get_java_object().getInputs(), FunctionInputPort)
    def get_outputs(self):
        """
        """
        return create_e_list(self.get_java_object().getOutputs(), FunctionOutputPort)
    def get_incoming(self):
        """
        """
        return create_e_list(self.get_java_object().getIncoming(), FunctionalExchange)
    def get_outgoing(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoing(), FunctionalExchange)
    def get_allocating_component(self):
        """
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
    def get_owned_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involving_functional_chains(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_involving_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), AbstractSystemCapability)

class OperationalActivity(AbstractActivityFunction):
    """
    Process step or action/operation/service performed by an Operational entity / actor&nbsp;and likely to influence the system definition or usage. Implementing operational activities generally produces elements of interactions expected by other activities
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivity"))
        elif isinstance(java_object, OperationalActivity):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_operational_activities(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedOperationalActivities(), OperationalActivity)
    def get_owned_operational_activity_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_incoming(self):
        """
        """
        return create_e_list(self.get_java_object().getIncoming(), Interaction)
    def get_outgoing(self):
        """
        """
        return create_e_list(self.get_java_object().getOutgoing(), Interaction)
    def get_allocating_entity(self):
        """
        """
        return capella_query_by_name(self, "Allocating Entity")
    def get_owned_operational_processes(self):
        """
        """
        return capella_query_by_name(self, "Owned Operational Processes")
    def get_involving_operational_processes(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalProcesses(), OperationalProcess)
    def get_involving_operational_capabilities(self):
        """
        """
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_realizing_system_functions(self):
        """
        """
        return capella_query_by_name(self, "Realizing System Functions")

class SystemFunction(Function):
    """
    The definition of a Function in the System Analysis
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunction"))
        elif isinstance(java_object, SystemFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_system_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedSystemFunctions(), SystemFunction)
    def get_owned_system_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_realized_operational_activities(self):
        """
        """
        return capella_query_by_name(self, "Realized Operational Activities")
    def get_realizing_logical_functions(self):
        """
        """
        return capella_query_by_name(self, "Realizing Logical Functions")

class LogicalFunction(Function):
    """
    The definition of a Function in the Logical Architecture
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunction"))
        elif isinstance(java_object, LogicalFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_logical_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedLogicalFunctions(), LogicalFunction)
    def get_owned_logical_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_realized_system_functions(self):
        """
        """
        return capella_query_by_name(self, "Realized System Functions")
    def get_realizing_physical_functions(self):
        """
        """
        return capella_query_by_name(self, "Realizing Physical Functions")

class PhysicalFunction(Function):
    """
    The definition of a Function in the Physical Architecture
    """
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunction"))
        elif isinstance(java_object, PhysicalFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            JavaObject.__init__(self, java_object)
    def get_contained_physical_functions(self):
        """
        """
        return create_e_list(self.get_java_object().getContainedPhysicalFunctions(), PhysicalFunction)
    def get_owned_physical_function_pkgs(self):
        """
        """
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_realized_logical_functions(self):
        """
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

