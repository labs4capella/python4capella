include('workspace://Python4Capella/api/EMF_API.py')
if False:
    from api.EMF_API import *
include('workspace://Python4Capella/api/Capella_API.py')
if False:
    from api.Capella_API import *
include('workspace://Python4Capella/advanced/sirius.py')
if False:
    from advanced.sirius import *


class Element(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/emde/1.0.0", "Element"))
        elif isinstance(java_object, Element):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/emde/1.0.0", "Element")
    def get_r_e_c_source_element(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicableElementLinks", self)
    def get_r_e_c(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.CatalogElementOrigin", self)
    def get_r_p_l(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.ReferencingReplicas", self)
    def get_elementof_interestfor_diagram(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.ElementToRepresentation", self)

class ExtensibleElement(Element):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/emde/1.0.0", "ExtensibleElement"))
        elif isinstance(java_object, ExtensibleElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/emde/1.0.0", "ExtensibleElement")
    def get_owned_extensions(self):
        return create_e_list(self.e_get("ownedExtensions"), ElementExtension)

class ModelElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "ModelElement"))
        elif isinstance(java_object, ModelElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "ModelElement")
    def get_id(self):
        return self.e_get("id")
    def set_id(self, value):
        self.e_set("id", value)
    def get_sid(self):
        return self.e_get("sid")
    def set_sid(self, value):
        self.e_set("sid", value)
    def get_constraints(self):
        return create_e_list(self.e_get("constraints"), AbstractConstraint)
    def get_owned_constraints(self):
        return create_e_list(self.e_get("ownedConstraints"), AbstractConstraint)
    def get_owned_migrated_elements(self):
        return create_e_list(self.e_get("ownedMigratedElements"), ModelElement)
    def get_expression(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OwnedSpecification", self)
    def get_all_related_tables(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.diagram.ModelElementRelatedTablesQuery", self)
    def get_all_related_diagrams(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.diagram.ModelElementRelatedDiagramsQuery", self)
    def get_all_related_pattern_instances(self):
        return capella_query("org.eclipse.emf.diffmerge.patterns.capella.ext.ModelElementPatternInstancesQuery", self)
    def get_guard(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ModelElementGuard", self)
    def get_post(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ModelElementPostCondition", self)
    def get_exchange_context(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ModelElementExchangeContext", self)
    def get_pre(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ModelElementPreCondition", self)
    def get_constraining_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ModelElementConstraints", self)

class AbstractNamedElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractNamedElement"))
        elif isinstance(java_object, AbstractNamedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractNamedElement")
    def get_name(self):
        return self.e_get("name")
    def set_name(self, value):
        self.e_set("name", value)

class TraceableElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "TraceableElement"))
        elif isinstance(java_object, TraceableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "TraceableElement")
    def get_incoming_traces(self):
        return create_e_list(self.e_get("incomingTraces"), AbstractTrace)
    def get_outgoing_traces(self):
        return create_e_list(self.e_get("outgoingTraces"), AbstractTrace)
    def get_outgoing_generic_traces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.TraceableElementOutgoingTrace", self)
    def get_incoming_generic_traces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.TraceableElementIncomingTrace", self)

class PublishableElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "PublishableElement"))
        elif isinstance(java_object, PublishableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "PublishableElement")
    def get_visible_in_doc(self):
        return self.e_get("visibleInDoc")
    def set_visible_in_doc(self, value):
        self.e_set("visibleInDoc", value)
    def get_visible_in_l_m(self):
        return self.e_get("visibleInLM")
    def set_visible_in_l_m(self, value):
        self.e_set("visibleInLM", value)

class CapellaElement(TraceableElement, PublishableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "CapellaElement"))
        elif isinstance(java_object, CapellaElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "CapellaElement")
    def get_summary(self):
        return self.e_get("summary")
    def set_summary(self, value):
        self.e_set("summary", value)
    def get_description(self):
        return self.e_get("description")
    def set_description(self, value):
        self.e_set("description", value)
    def get_review(self):
        return self.e_get("review")
    def set_review(self, value):
        self.e_set("review", value)
    def get_owned_property_values(self):
        return create_e_list(self.e_get("ownedPropertyValues"), AbstractPropertyValue)
    def get_owned_enumeration_property_types(self):
        return create_e_list(self.e_get("ownedEnumerationPropertyTypes"), EnumerationPropertyType)
    def get_applied_property_values(self):
        return create_e_list(self.e_get("appliedPropertyValues"), AbstractPropertyValue)
    def get_owned_property_value_groups(self):
        return create_e_list(self.e_get("ownedPropertyValueGroups"), PropertyValueGroup)
    def get_applied_property_value_groups(self):
        return create_e_list(self.e_get("appliedPropertyValueGroups"), PropertyValueGroup)
    def get_status(self):
        value =  self.e_get("status")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_status(self, value):
        return self.e_set("status", value.get_java_object())
    def get_features(self):
        return create_e_list(self.e_get("features"), EnumerationPropertyLiteral)
    def get_applied_requirements(self):
        return create_e_list(self.e_get("appliedRequirements"), Requirement)
    def get_allocated_requirements(self):
        return capella_query("org.polarsys.capella.vp.requirements.semantic.browser.queries.CapellaElementOutgoingRelatedRequirementsQuery", self)
    def get_requirements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElement_requirement", self)
    def get_allocating_requirements(self):
        return capella_query("org.polarsys.capella.vp.requirements.semantic.browser.queries.CapellaElementIncomingRelatedRequirementsQuery", self)

class NamedElement(AbstractNamedElement, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamedElement"))
        elif isinstance(java_object, NamedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "NamedElement")

class Namespace(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Namespace"))
        elif isinstance(java_object, Namespace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Namespace")
    def get_owned_traces(self):
        return create_e_list(self.e_get("ownedTraces"), Trace)
    def get_contained_generic_traces(self):
        return create_e_list(self.e_get("containedGenericTraces"), GenericTrace)
    def get_contained_requirements_traces(self):
        return create_e_list(self.e_get("containedRequirementsTraces"), RequirementsTrace)
    def get_naming_rules(self):
        return create_e_list(self.e_get("namingRules"), NamingRule)

class Structure(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Structure"))
        elif isinstance(java_object, Structure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Structure")
    def get_owned_property_value_pkgs(self):
        return create_e_list(self.e_get("ownedPropertyValuePkgs"), PropertyValuePkg)

class ModellingArchitecture(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecture"))
        elif isinstance(java_object, ModellingArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecture")

class AbstractFunctionalArchitecture(ModellingArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalArchitecture"))
        elif isinstance(java_object, AbstractFunctionalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalArchitecture")
    def get_owned_function_pkg(self):
        value =  self.e_get("ownedFunctionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_function_pkg(self, value):
        return self.e_set("ownedFunctionPkg", value.get_java_object())
    def get_owned_component_exchanges(self):
        return create_e_list(self.e_get("ownedComponentExchanges"), ComponentExchange)
    def get_owned_component_exchange_categories(self):
        return create_e_list(self.e_get("ownedComponentExchangeCategories"), ComponentExchangeCategory)
    def get_owned_functional_links(self):
        return create_e_list(self.e_get("ownedFunctionalLinks"), ExchangeLink)
    def get_owned_functional_allocations(self):
        return create_e_list(self.e_get("ownedFunctionalAllocations"), ComponentFunctionalAllocation)
    def get_owned_component_exchange_realizations(self):
        return create_e_list(self.e_get("ownedComponentExchangeRealizations"), ComponentExchangeRealization)

class BlockArchitecture(AbstractFunctionalArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecture"))
        elif isinstance(java_object, BlockArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecture")
    def get_owned_requirement_pkgs(self):
        return create_e_list(self.e_get("ownedRequirementPkgs"), RequirementsPkg)
    def get_owned_abstract_capability_pkg(self):
        value =  self.e_get("ownedAbstractCapabilityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_abstract_capability_pkg(self, value):
        return self.e_set("ownedAbstractCapabilityPkg", value.get_java_object())
    def get_owned_interface_pkg(self):
        value =  self.e_get("ownedInterfacePkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_interface_pkg(self, value):
        return self.e_set("ownedInterfacePkg", value.get_java_object())
    def get_owned_data_pkg(self):
        value =  self.e_get("ownedDataPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_data_pkg(self, value):
        return self.e_set("ownedDataPkg", value.get_java_object())
    def get_provisioned_architecture_allocations(self):
        return create_e_list(self.e_get("provisionedArchitectureAllocations"), ArchitectureAllocation)
    def get_provisioning_architecture_allocations(self):
        return create_e_list(self.e_get("provisioningArchitectureAllocations"), ArchitectureAllocation)
    def get_allocated_architectures(self):
        return create_e_list(self.e_get("allocatedArchitectures"), BlockArchitecture)
    def get_allocating_architectures(self):
        return create_e_list(self.e_get("allocatingArchitectures"), BlockArchitecture)
    def get_system(self):
        value =  self.e_get("system")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComponentArchitecture(BlockArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentArchitecture"))
        elif isinstance(java_object, ComponentArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentArchitecture")

class SystemAnalysis(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemAnalysis"))
        elif isinstance(java_object, SystemAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemAnalysis")
    def get_owned_system_component_pkg(self):
        value =  self.e_get("ownedSystemComponentPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_system_component_pkg(self, value):
        return self.e_set("ownedSystemComponentPkg", value.get_java_object())
    def get_owned_mission_pkg(self):
        value =  self.e_get("ownedMissionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_mission_pkg(self, value):
        return self.e_set("ownedMissionPkg", value.get_java_object())
    def get_contained_capability_pkg(self):
        value =  self.e_get("containedCapabilityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_contained_system_function_pkg(self):
        value =  self.e_get("containedSystemFunctionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_operational_analysis_realizations(self):
        return create_e_list(self.e_get("ownedOperationalAnalysisRealizations"), OperationalAnalysisRealization)
    def get_allocated_operational_analysis_realizations(self):
        return create_e_list(self.e_get("allocatedOperationalAnalysisRealizations"), OperationalAnalysisRealization)
    def get_allocated_operational_analyses(self):
        return create_e_list(self.e_get("allocatedOperationalAnalyses"), OperationalAnalysis)
    def get_allocating_logical_architectures(self):
        return create_e_list(self.e_get("allocatingLogicalArchitectures"), LogicalArchitecture)

class InvolvedElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "InvolvedElement"))
        elif isinstance(java_object, InvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "InvolvedElement")
    def get_involving_involvements(self):
        return create_e_list(self.e_get("involvingInvolvements"), Involvement)

class Feature(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Feature"))
        elif isinstance(java_object, Feature):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Feature")
    def get_is_abstract(self):
        return self.e_get("isAbstract")
    def set_is_abstract(self, value):
        self.e_set("isAbstract", value)
    def get_is_static(self):
        return self.e_get("isStatic")
    def set_is_static(self, value):
        self.e_set("isStatic", value)
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)

class AbstractTypedElement(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTypedElement"))
        elif isinstance(java_object, AbstractTypedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTypedElement")
    def get_abstract_type(self):
        value =  self.e_get("abstractType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_abstract_type(self, value):
        return self.e_set("abstractType", value.get_java_object())

class TypedElement(AbstractTypedElement, NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "TypedElement"))
        elif isinstance(java_object, TypedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "TypedElement")
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class MultiplicityElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "MultiplicityElement"))
        elif isinstance(java_object, MultiplicityElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "MultiplicityElement")
    def get_ordered(self):
        return self.e_get("ordered")
    def set_ordered(self, value):
        self.e_set("ordered", value)
    def get_unique(self):
        return self.e_get("unique")
    def set_unique(self, value):
        self.e_set("unique", value)
    def get_min_inclusive(self):
        return self.e_get("minInclusive")
    def set_min_inclusive(self, value):
        self.e_set("minInclusive", value)
    def get_max_inclusive(self):
        return self.e_get("maxInclusive")
    def set_max_inclusive(self, value):
        self.e_set("maxInclusive", value)
    def get_owned_default_value(self):
        value =  self.e_get("ownedDefaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_value(self, value):
        return self.e_set("ownedDefaultValue", value.get_java_object())
    def get_owned_min_value(self):
        value =  self.e_get("ownedMinValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_value(self, value):
        return self.e_set("ownedMinValue", value.get_java_object())
    def get_owned_max_value(self):
        value =  self.e_get("ownedMaxValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_value(self, value):
        return self.e_set("ownedMaxValue", value.get_java_object())
    def get_owned_null_value(self):
        value =  self.e_get("ownedNullValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_null_value(self, value):
        return self.e_set("ownedNullValue", value.get_java_object())
    def get_owned_min_card(self):
        value =  self.e_get("ownedMinCard")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_card(self, value):
        return self.e_set("ownedMinCard", value.get_java_object())
    def get_owned_min_length(self):
        value =  self.e_get("ownedMinLength")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_length(self, value):
        return self.e_set("ownedMinLength", value.get_java_object())
    def get_owned_max_card(self):
        value =  self.e_get("ownedMaxCard")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_card(self, value):
        return self.e_set("ownedMaxCard", value.get_java_object())
    def get_owned_max_length(self):
        value =  self.e_get("ownedMaxLength")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_length(self, value):
        return self.e_set("ownedMaxLength", value.get_java_object())

class FinalizableElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "FinalizableElement"))
        elif isinstance(java_object, FinalizableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "FinalizableElement")
    def get_final(self):
        return self.e_get("final")
    def set_final(self, value):
        self.e_set("final", value)

class Property(Feature, TypedElement, MultiplicityElement, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Property"))
        elif isinstance(java_object, Property):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Property")
    def get_aggregation_kind(self):
        return self.e_get("aggregationKind").getName()
    def set_aggregation_kind(self, value):
        self.e_set("aggregationKind", value)
    def get_is_derived(self):
        return self.e_get("isDerived")
    def set_is_derived(self, value):
        self.e_set("isDerived", value)
    def get_is_read_only(self):
        return self.e_get("isReadOnly")
    def set_is_read_only(self, value):
        self.e_set("isReadOnly", value)
    def get_is_part_of_key(self):
        return self.e_get("isPartOfKey")
    def set_is_part_of_key(self, value):
        self.e_set("isPartOfKey", value)
    def get_association(self):
        value =  self.e_get("association")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_parent(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyOwner", self)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyType", self)

class AbstractInstance(Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractInstance"))
        elif isinstance(java_object, AbstractInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractInstance")
    def get_representing_instance_roles(self):
        return create_e_list(self.e_get("representingInstanceRoles"), InstanceRole)

class AbstractFunctionalChainContainer(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalChainContainer"))
        elif isinstance(java_object, AbstractFunctionalChainContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalChainContainer")
    def get_owned_functional_chains(self):
        return create_e_list(self.e_get("ownedFunctionalChains"), FunctionalChain)

class ActivityNode(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityNode"))
        elif isinstance(java_object, ActivityNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityNode")
    def get_in_activity_partition(self):
        value =  self.e_get("inActivityPartition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_in_interruptible_region(self):
        value =  self.e_get("inInterruptibleRegion")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_in_structured_node(self):
        value =  self.e_get("inStructuredNode")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_outgoing(self):
        return create_e_list(self.e_get("outgoing"), ActivityEdge)
    def get_incoming(self):
        return create_e_list(self.e_get("incoming"), ActivityEdge)

class ExecutableNode(ActivityNode):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ExecutableNode"))
        elif isinstance(java_object, ExecutableNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ExecutableNode")
    def get_owned_handlers(self):
        return create_e_list(self.e_get("ownedHandlers"), ExceptionHandler)

class AbstractAction(ExecutableNode, AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractAction"))
        elif isinstance(java_object, AbstractAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractAction")
    def get_local_precondition(self):
        value =  self.e_get("localPrecondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_local_precondition(self, value):
        return self.e_set("localPrecondition", value.get_java_object())
    def get_local_postcondition(self):
        value =  self.e_get("localPostcondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_local_postcondition(self, value):
        return self.e_set("localPostcondition", value.get_java_object())
    def get_context(self):
        value =  self.e_get("context")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_context(self, value):
        return self.e_set("context", value.get_java_object())
    def get_inputs(self):
        return create_e_list(self.e_get("inputs"), InputPin)
    def get_outputs(self):
        return create_e_list(self.e_get("outputs"), OutputPin)

class InvocationAction(AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "InvocationAction"))
        elif isinstance(java_object, InvocationAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "InvocationAction")
    def get_arguments(self):
        return create_e_list(self.e_get("arguments"), InputPin)

class CallAction(InvocationAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "CallAction"))
        elif isinstance(java_object, CallAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "CallAction")
    def get_results(self):
        return create_e_list(self.e_get("results"), OutputPin)

class CallBehaviorAction(CallAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "CallBehaviorAction"))
        elif isinstance(java_object, CallBehaviorAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "CallBehaviorAction")
    def get_behavior(self):
        value =  self.e_get("behavior")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_behavior(self, value):
        return self.e_set("behavior", value.get_java_object())

class AbstractType(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractType"))
        elif isinstance(java_object, AbstractType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractType")
    def get_abstract_typed_elements(self):
        return create_e_list(self.e_get("abstractTypedElements"), AbstractTypedElement)
    def get_inheritedof_typing_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractTypeAbstractTypedElement", self)

class AbstractEvent(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractEvent"))
        elif isinstance(java_object, AbstractEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractEvent")

class AbstractFunction(Namespace, InvolvedElement, AbstractInstance, AbstractFunctionalChainContainer, CallBehaviorAction, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunction"))
        elif isinstance(java_object, AbstractFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunction")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_condition(self):
        return self.e_get("condition")
    def set_condition(self, value):
        self.e_set("condition", value)
    def get_owned_functions(self):
        return create_e_list(self.e_get("ownedFunctions"), AbstractFunction)
    def get_owned_function_realizations(self):
        return create_e_list(self.e_get("ownedFunctionRealizations"), FunctionRealization)
    def get_owned_functional_exchanges(self):
        return create_e_list(self.e_get("ownedFunctionalExchanges"), FunctionalExchange)
    def get_sub_functions(self):
        return create_e_list(self.e_get("subFunctions"), AbstractFunction)
    def get_out_function_realizations(self):
        return create_e_list(self.e_get("outFunctionRealizations"), FunctionRealization)
    def get_in_function_realizations(self):
        return create_e_list(self.e_get("inFunctionRealizations"), FunctionRealization)
    def get_component_functional_allocations(self):
        return create_e_list(self.e_get("componentFunctionalAllocations"), ComponentFunctionalAllocation)
    def get_allocation_blocks(self):
        return create_e_list(self.e_get("allocationBlocks"), AbstractFunctionalBlock)
    def get_available_in_states(self):
        return create_e_list(self.e_get("availableInStates"), State)
    def get_involving_capabilities(self):
        return create_e_list(self.e_get("involvingCapabilities"), Capability)
    def get_involving_capability_realizations(self):
        return create_e_list(self.e_get("involvingCapabilityRealizations"), CapabilityRealization)
    def get_involving_functional_chains(self):
        return create_e_list(self.e_get("involvingFunctionalChains"), FunctionalChain)
    def get_linked_state_machine(self):
        value =  self.e_get("linkedStateMachine")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_linked_function_specification(self):
        value =  self.e_get("linkedFunctionSpecification")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_parent(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_parentFunction", self)
    def get_breakdown(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_functionBreakdown", self)
    def get_active_in_modes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_activeInModes", self)
    def get_active_in_states(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_activeInStates", self)
    def get_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionFunctionalChain", self)
    def get_allocating_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_mother_function_allocation", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class SystemFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunction"))
        elif isinstance(java_object, SystemFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunction")
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.e_get("ownedSystemFunctionPkgs"), SystemFunctionPkg)
    def get_allocating_system_components(self):
        return create_e_list(self.e_get("allocatingSystemComponents"), SystemComponent)
    def get_realized_operational_activities(self):
        return create_e_list(self.e_get("realizedOperationalActivities"), OperationalActivity)
    def get_realizing_logical_functions(self):
        return create_e_list(self.e_get("realizingLogicalFunctions"), LogicalFunction)
    def get_contained_system_functions(self):
        return create_e_list(self.e_get("containedSystemFunctions"), SystemFunction)
    def get_children_system_functions(self):
        return create_e_list(self.e_get("childrenSystemFunctions"), SystemFunction)
    def get_owned_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_ownedFunctionalChains", self)
    def get_internal_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalOutGoingDataflows", self)
    def get_out_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_outFlowPorts", self)
    def get_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_outgoingInteraction", self)
    def get_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_incomingInteraction", self)
    def get_internal_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalInComingDataflows", self)
    def get_allocating_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingActor", self)
    def get_in_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_inFlowPorts", self)
    def get_involving_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SystemFunctionInvolvingCapabilities", self)
    def get_allocating_system(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingComponent", self)

class FunctionPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionPkg"))
        elif isinstance(java_object, FunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionPkg")
    def get_owned_functional_links(self):
        return create_e_list(self.e_get("ownedFunctionalLinks"), ExchangeLink)
    def get_owned_exchanges(self):
        return create_e_list(self.e_get("ownedExchanges"), FunctionalExchangeSpecification)
    def get_owned_exchange_specification_realizations(self):
        return create_e_list(self.e_get("ownedExchangeSpecificationRealizations"), ExchangeSpecificationRealization)
    def get_owned_categories(self):
        return create_e_list(self.e_get("ownedCategories"), ExchangeCategory)
    def get_owned_function_specifications(self):
        return create_e_list(self.e_get("ownedFunctionSpecifications"), FunctionSpecification)

class SystemFunctionPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunctionPkg"))
        elif isinstance(java_object, SystemFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunctionPkg")
    def get_owned_system_functions(self):
        return create_e_list(self.e_get("ownedSystemFunctions"), SystemFunction)
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.e_get("ownedSystemFunctionPkgs"), SystemFunctionPkg)

class SystemCommunicationHook(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunicationHook"))
        elif isinstance(java_object, SystemCommunicationHook):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunicationHook")
    def get_communication(self):
        value =  self.e_get("communication")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_communication(self, value):
        return self.e_set("communication", value.get_java_object())
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())

class AbstractRelationship(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractRelationship"))
        elif isinstance(java_object, AbstractRelationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractRelationship")
    def get_realized_flow(self):
        value =  self.e_get("realizedFlow")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_realized_flow(self, value):
        return self.e_set("realizedFlow", value.get_java_object())

class Relationship(AbstractRelationship, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Relationship"))
        elif isinstance(java_object, Relationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Relationship")

class SystemCommunication(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunication"))
        elif isinstance(java_object, SystemCommunication):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunication")
    def get_ends(self):
        return create_e_list(self.e_get("ends"), SystemCommunicationHook)

class Involvement(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Involvement"))
        elif isinstance(java_object, Involvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Involvement")
    def get_involver(self):
        value =  self.e_get("involver")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_involved(self):
        value =  self.e_get("involved")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_involved(self, value):
        return self.e_set("involved", value.get_java_object())
    def get_involved_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInvolvementTarget", self)
    def get_involving_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInvolvementSource", self)

class CapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityInvolvement"))
        elif isinstance(java_object, CapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityInvolvement")
    def get_system_component(self):
        value =  self.e_get("systemComponent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_capability(self):
        value =  self.e_get("capability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class MissionInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionInvolvement"))
        elif isinstance(java_object, MissionInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionInvolvement")
    def get_system_component(self):
        value =  self.e_get("systemComponent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_mission(self):
        value =  self.e_get("mission")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class InvolverElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "InvolverElement"))
        elif isinstance(java_object, InvolverElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "InvolverElement")
    def get_involved_involvements(self):
        return create_e_list(self.e_get("involvedInvolvements"), Involvement)

class Mission(NamedElement, InvolverElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "Mission"))
        elif isinstance(java_object, Mission):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "Mission")
    def get_owned_mission_involvements(self):
        return create_e_list(self.e_get("ownedMissionInvolvements"), MissionInvolvement)
    def get_involved_system_components(self):
        return create_e_list(self.e_get("involvedSystemComponents"), SystemComponent)
    def get_owned_capability_exploitations(self):
        return create_e_list(self.e_get("ownedCapabilityExploitations"), CapabilityExploitation)
    def get_exploited_capabilities(self):
        return create_e_list(self.e_get("exploitedCapabilities"), Capability)

class MissionPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionPkg"))
        elif isinstance(java_object, MissionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionPkg")
    def get_owned_mission_pkgs(self):
        return create_e_list(self.e_get("ownedMissionPkgs"), MissionPkg)
    def get_owned_missions(self):
        return create_e_list(self.e_get("ownedMissions"), Mission)

class AbstractCapability(Structure, InvolverElement, AbstractFunctionalChainContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapability"))
        elif isinstance(java_object, AbstractCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapability")
    def get_pre_condition(self):
        value =  self.e_get("preCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.e_set("preCondition", value.get_java_object())
    def get_post_condition(self):
        value =  self.e_get("postCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.e_set("postCondition", value.get_java_object())
    def get_owned_scenarios(self):
        return create_e_list(self.e_get("ownedScenarios"), Scenario)
    def get_incoming_capability_allocation(self):
        return create_e_list(self.e_get("incomingCapabilityAllocation"), AbstractCapabilityRealization)
    def get_outgoing_capability_allocation(self):
        return create_e_list(self.e_get("outgoingCapabilityAllocation"), AbstractCapabilityRealization)
    def get_extends(self):
        return create_e_list(self.e_get("extends"), AbstractCapabilityExtend)
    def get_extending(self):
        return create_e_list(self.e_get("extending"), AbstractCapabilityExtend)
    def get_abstract_capability_extension_points(self):
        return create_e_list(self.e_get("abstractCapabilityExtensionPoints"), AbstractCapabilityExtensionPoint)
    def get_super_generalizations(self):
        return create_e_list(self.e_get("superGeneralizations"), AbstractCapabilityGeneralization)
    def get_sub_generalizations(self):
        return create_e_list(self.e_get("subGeneralizations"), AbstractCapabilityGeneralization)
    def get_includes(self):
        return create_e_list(self.e_get("includes"), AbstractCapabilityInclude)
    def get_including(self):
        return create_e_list(self.e_get("including"), AbstractCapabilityInclude)
    def get_super(self):
        return create_e_list(self.e_get("super"), AbstractCapability)
    def get_sub(self):
        return create_e_list(self.e_get("sub"), AbstractCapability)
    def get_included_abstract_capabilities(self):
        return create_e_list(self.e_get("includedAbstractCapabilities"), AbstractCapability)
    def get_including_abstract_capabilities(self):
        return create_e_list(self.e_get("includingAbstractCapabilities"), AbstractCapability)
    def get_extended_abstract_capabilities(self):
        return create_e_list(self.e_get("extendedAbstractCapabilities"), AbstractCapability)
    def get_extending_abstract_capabilities(self):
        return create_e_list(self.e_get("extendingAbstractCapabilities"), AbstractCapability)
    def get_owned_functional_chain_abstract_capability_involvements(self):
        return create_e_list(self.e_get("ownedFunctionalChainAbstractCapabilityInvolvements"), FunctionalChainAbstractCapabilityInvolvement)
    def get_owned_abstract_function_abstract_capability_involvements(self):
        return create_e_list(self.e_get("ownedAbstractFunctionAbstractCapabilityInvolvements"), AbstractFunctionAbstractCapabilityInvolvement)
    def get_available_in_states(self):
        return create_e_list(self.e_get("availableInStates"), State)
    def get_owned_abstract_capability_realizations(self):
        return create_e_list(self.e_get("ownedAbstractCapabilityRealizations"), AbstractCapabilityRealization)
    def get_involved_abstract_functions(self):
        return create_e_list(self.e_get("involvedAbstractFunctions"), AbstractFunction)
    def get_involved_functional_chains(self):
        return create_e_list(self.e_get("involvedFunctionalChains"), FunctionalChain)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_scenarios", self)
    def get_generalized_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilitySuper", self)
    def get_active_in_modes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityAvailableInMode", self)
    def get_involved_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_InvolvedComponents", self)
    def get_extended_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_extendedCapabilities", self)
    def get_refined_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapability_refinedAbstractCapabilities", self)
    def get_active_in_states(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityAvailableInState", self)
    def get_included_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_includedCapabilities", self)
    def get_generalizing_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilitySub", self)
    def get_refining_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapability_refiningAbstractCapabilities", self)
    def get_including_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_includingCapabilities", self)
    def get_extending_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_extendingCapabilities", self)

class Capability(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "Capability"))
        elif isinstance(java_object, Capability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "Capability")
    def get_owned_capability_involvements(self):
        return create_e_list(self.e_get("ownedCapabilityInvolvements"), CapabilityInvolvement)
    def get_involved_system_components(self):
        return create_e_list(self.e_get("involvedSystemComponents"), SystemComponent)
    def get_purposes(self):
        return create_e_list(self.e_get("purposes"), CapabilityExploitation)
    def get_purpose_missions(self):
        return create_e_list(self.e_get("purposeMissions"), Mission)
    def get_realized_operational_capabilities(self):
        return create_e_list(self.e_get("realizedOperationalCapabilities"), OperationalCapability)
    def get_realizing_capability_realizations(self):
        return create_e_list(self.e_get("realizingCapabilityRealizations"), CapabilityRealization)
    def get_owned_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityOwnedFunctionalChains", self)
    def get_involved_system_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityInvolvedFunctions", self)
    def get_involved_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityInvolvedFunctionalChains", self)
    def get_exploiting_missions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_purposeMissions", self)

class CapabilityExploitation(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityExploitation"))
        elif isinstance(java_object, CapabilityExploitation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityExploitation")
    def get_mission(self):
        value =  self.e_get("mission")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_capability(self):
        value =  self.e_get("capability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_capability(self, value):
        return self.e_set("capability", value.get_java_object())
    def get_involved_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsCapabilityExploitationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsCapabilityExploitationSource", self)

class AbstractCapabilityPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractCapabilityPkg"))
        elif isinstance(java_object, AbstractCapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractCapabilityPkg")

class CapabilityPkg(AbstractCapabilityPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityPkg"))
        elif isinstance(java_object, CapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityPkg")
    def get_owned_capabilities(self):
        return create_e_list(self.e_get("ownedCapabilities"), Capability)
    def get_owned_capability_pkgs(self):
        return create_e_list(self.e_get("ownedCapabilityPkgs"), CapabilityPkg)

class AbstractTrace(TraceableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTrace"))
        elif isinstance(java_object, AbstractTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTrace")
    def get_target_element(self):
        value =  self.e_get("targetElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target_element(self, value):
        return self.e_set("targetElement", value.get_java_object())
    def get_source_element(self):
        value =  self.e_get("sourceElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source_element(self, value):
        return self.e_set("sourceElement", value.get_java_object())

class Allocation(Relationship, AbstractTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Allocation"))
        elif isinstance(java_object, Allocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Allocation")
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAllocationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAllocationSource", self)

class ArchitectureAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ArchitectureAllocation"))
        elif isinstance(java_object, ArchitectureAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ArchitectureAllocation")
    def get_allocated_architecture(self):
        value =  self.e_get("allocatedArchitecture")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_architecture(self):
        value =  self.e_get("allocatingArchitecture")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class OperationalAnalysisRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "OperationalAnalysisRealization"))
        elif isinstance(java_object, OperationalAnalysisRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "OperationalAnalysisRealization")

class ComponentPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentPkg"))
        elif isinstance(java_object, ComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentPkg")
    def get_owned_parts(self):
        return create_e_list(self.e_get("ownedParts"), Part)
    def get_owned_component_exchanges(self):
        return create_e_list(self.e_get("ownedComponentExchanges"), ComponentExchange)
    def get_owned_component_exchange_categories(self):
        return create_e_list(self.e_get("ownedComponentExchangeCategories"), ComponentExchangeCategory)
    def get_owned_functional_links(self):
        return create_e_list(self.e_get("ownedFunctionalLinks"), ExchangeLink)
    def get_owned_functional_allocations(self):
        return create_e_list(self.e_get("ownedFunctionalAllocations"), ComponentFunctionalAllocation)
    def get_owned_component_exchange_realizations(self):
        return create_e_list(self.e_get("ownedComponentExchangeRealizations"), ComponentExchangeRealization)
    def get_owned_physical_links(self):
        return create_e_list(self.e_get("ownedPhysicalLinks"), PhysicalLink)
    def get_owned_physical_link_categories(self):
        return create_e_list(self.e_get("ownedPhysicalLinkCategories"), PhysicalLinkCategory)
    def get_owned_state_machines(self):
        return create_e_list(self.e_get("ownedStateMachines"), StateMachine)

class SystemComponentPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponentPkg"))
        elif isinstance(java_object, SystemComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponentPkg")
    def get_owned_system_components(self):
        return create_e_list(self.e_get("ownedSystemComponents"), SystemComponent)
    def get_owned_system_component_pkgs(self):
        return create_e_list(self.e_get("ownedSystemComponentPkgs"), SystemComponentPkg)

class Type(AbstractType, Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Type"))
        elif isinstance(java_object, Type):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Type")
    def get_typed_elements(self):
        return create_e_list(self.e_get("typedElements"), TypedElement)
    def get_exchange_item_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractTypeExchangeItemElements", self)
    def get_typing_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractTypeTypedElements", self)

class ModellingBlock(Type):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingBlock"))
        elif isinstance(java_object, ModellingBlock):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingBlock")

class AbstractFunctionalBlock(ModellingBlock):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalBlock"))
        elif isinstance(java_object, AbstractFunctionalBlock):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalBlock")
    def get_owned_functional_allocation(self):
        return create_e_list(self.e_get("ownedFunctionalAllocation"), ComponentFunctionalAllocation)
    def get_owned_component_exchanges(self):
        return create_e_list(self.e_get("ownedComponentExchanges"), ComponentExchange)
    def get_owned_component_exchange_categories(self):
        return create_e_list(self.e_get("ownedComponentExchangeCategories"), ComponentExchangeCategory)
    def get_functional_allocations(self):
        return create_e_list(self.e_get("functionalAllocations"), ComponentFunctionalAllocation)
    def get_allocated_functions(self):
        return create_e_list(self.e_get("allocatedFunctions"), AbstractFunction)
    def get_in_exchange_links(self):
        return create_e_list(self.e_get("inExchangeLinks"), ExchangeLink)
    def get_out_exchange_links(self):
        return create_e_list(self.e_get("outExchangeLinks"), ExchangeLink)

class Block(ModellingBlock, AbstractFunctionalBlock):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Block"))
        elif isinstance(java_object, Block):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "Block")
    def get_owned_abstract_capability_pkg(self):
        value =  self.e_get("ownedAbstractCapabilityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_abstract_capability_pkg(self, value):
        return self.e_set("ownedAbstractCapabilityPkg", value.get_java_object())
    def get_owned_interface_pkg(self):
        value =  self.e_get("ownedInterfacePkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_interface_pkg(self, value):
        return self.e_set("ownedInterfacePkg", value.get_java_object())
    def get_owned_data_pkg(self):
        value =  self.e_get("ownedDataPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_data_pkg(self, value):
        return self.e_set("ownedDataPkg", value.get_java_object())
    def get_owned_state_machines(self):
        return create_e_list(self.e_get("ownedStateMachines"), StateMachine)

class GeneralizableElement(Type):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralizableElement"))
        elif isinstance(java_object, GeneralizableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralizableElement")
    def get_abstract(self):
        return self.e_get("abstract")
    def set_abstract(self, value):
        self.e_set("abstract", value)
    def get_owned_generalizations(self):
        return create_e_list(self.e_get("ownedGeneralizations"), Generalization)
    def get_super_generalizations(self):
        return create_e_list(self.e_get("superGeneralizations"), Generalization)
    def get_sub_generalizations(self):
        return create_e_list(self.e_get("subGeneralizations"), Generalization)
    def get_super(self):
        return create_e_list(self.e_get("super"), GeneralizableElement)
    def get_sub(self):
        return create_e_list(self.e_get("sub"), GeneralizableElement)
    def get_generalized_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.GeneralizableElementAllSuperGE", self)
    def get_generalizing_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.GeneralizableElementAllSubGE", self)

class Classifier(GeneralizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Classifier"))
        elif isinstance(java_object, Classifier):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Classifier")
    def get_owned_features(self):
        return create_e_list(self.e_get("ownedFeatures"), Feature)
    def get_contained_properties(self):
        return create_e_list(self.e_get("containedProperties"), Property)

class InterfaceAllocator(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocator"))
        elif isinstance(java_object, InterfaceAllocator):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocator")
    def get_owned_interface_allocations(self):
        return create_e_list(self.e_get("ownedInterfaceAllocations"), InterfaceAllocation)
    def get_provisioned_interface_allocations(self):
        return create_e_list(self.e_get("provisionedInterfaceAllocations"), InterfaceAllocation)
    def get_allocated_interfaces(self):
        return create_e_list(self.e_get("allocatedInterfaces"), Interface)

class CommunicationLinkExchanger(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLinkExchanger"))
        elif isinstance(java_object, CommunicationLinkExchanger):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLinkExchanger")
    def get_owned_communication_links(self):
        return create_e_list(self.e_get("ownedCommunicationLinks"), CommunicationLink)
    def get_produce(self):
        return create_e_list(self.e_get("produce"), CommunicationLink)
    def get_consume(self):
        return create_e_list(self.e_get("consume"), CommunicationLink)
    def get_send(self):
        return create_e_list(self.e_get("send"), CommunicationLink)
    def get_receive(self):
        return create_e_list(self.e_get("receive"), CommunicationLink)
    def get_call(self):
        return create_e_list(self.e_get("call"), CommunicationLink)
    def get_execute(self):
        return create_e_list(self.e_get("execute"), CommunicationLink)
    def get_write(self):
        return create_e_list(self.e_get("write"), CommunicationLink)
    def get_access(self):
        return create_e_list(self.e_get("access"), CommunicationLink)
    def get_acquire(self):
        return create_e_list(self.e_get("acquire"), CommunicationLink)
    def get_transmit(self):
        return create_e_list(self.e_get("transmit"), CommunicationLink)

class Component(Block, Classifier, InterfaceAllocator, CommunicationLinkExchanger):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Component"))
        elif isinstance(java_object, Component):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "Component")
    def get_actor(self):
        return self.e_get("actor")
    def set_actor(self, value):
        self.e_set("actor", value)
    def get_human(self):
        return self.e_get("human")
    def set_human(self, value):
        self.e_set("human", value)
    def get_owned_interface_uses(self):
        return create_e_list(self.e_get("ownedInterfaceUses"), InterfaceUse)
    def get_used_interface_links(self):
        return create_e_list(self.e_get("usedInterfaceLinks"), InterfaceUse)
    def get_used_interfaces(self):
        return create_e_list(self.e_get("usedInterfaces"), Interface)
    def get_owned_interface_implementations(self):
        return create_e_list(self.e_get("ownedInterfaceImplementations"), InterfaceImplementation)
    def get_implemented_interface_links(self):
        return create_e_list(self.e_get("implementedInterfaceLinks"), InterfaceImplementation)
    def get_implemented_interfaces(self):
        return create_e_list(self.e_get("implementedInterfaces"), Interface)
    def get_owned_component_realizations(self):
        return create_e_list(self.e_get("ownedComponentRealizations"), ComponentRealization)
    def get_realized_components(self):
        return create_e_list(self.e_get("realizedComponents"), Component)
    def get_realizing_components(self):
        return create_e_list(self.e_get("realizingComponents"), Component)
    def get_provided_interfaces(self):
        return create_e_list(self.e_get("providedInterfaces"), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.e_get("requiredInterfaces"), Interface)
    def get_contained_component_ports(self):
        return create_e_list(self.e_get("containedComponentPorts"), ComponentPort)
    def get_contained_parts(self):
        return create_e_list(self.e_get("containedParts"), Part)
    def get_contained_physical_ports(self):
        return create_e_list(self.e_get("containedPhysicalPorts"), PhysicalPort)
    def get_owned_physical_path(self):
        return create_e_list(self.e_get("ownedPhysicalPath"), PhysicalPath)
    def get_owned_physical_links(self):
        return create_e_list(self.e_get("ownedPhysicalLinks"), PhysicalLink)
    def get_owned_physical_link_categories(self):
        return create_e_list(self.e_get("ownedPhysicalLinkCategories"), PhysicalLinkCategory)
    def get_representing_parts(self):
        return create_e_list(self.e_get("representingParts"), Part)
    def get_component_breakdown(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_componentBreakdown", self)
    def get_parent(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_parentComponent", self)
    def get_owned_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_SubDefinedComponents", self)
    def get_generalized_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.GeneralizableElementAllSuperGC", self)
    def get_internal_outgoing_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentInternalOutgoingComponentExchanges", self)
    def get_outgoing_delegations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentOutgoingDelegation", self)
    def get_communication_link(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentCommunicationLink", self)
    def get_outgoing_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentOutgoingComponentExchange", self)
    def get_incoming_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentIncomingComponentExchange", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)
    def get_component_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_componentPorts", self)
    def get_incoming_delegations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentIncomingDelegation", self)
    def get_generalizing_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.GeneralizableElementAllSubGC", self)
    def get_referencing_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_referencingComponent", self)
    def get_internal_incoming_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentInternalIncomingComponentExchanges", self)

class SystemComponent(Component, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponent"))
        elif isinstance(java_object, SystemComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponent")
    def get_owned_system_components(self):
        return create_e_list(self.e_get("ownedSystemComponents"), SystemComponent)
    def get_owned_system_component_pkgs(self):
        return create_e_list(self.e_get("ownedSystemComponentPkgs"), SystemComponentPkg)
    def get_data_component(self):
        return self.e_get("dataComponent")
    def set_data_component(self, value):
        self.e_set("dataComponent", value)
    def get_data_type(self):
        return create_e_list(self.e_get("dataType"), Classifier)
    def get_involving_capabilities(self):
        return create_e_list(self.e_get("involvingCapabilities"), Capability)
    def get_capability_involvements(self):
        return create_e_list(self.e_get("capabilityInvolvements"), CapabilityInvolvement)
    def get_involving_missions(self):
        return create_e_list(self.e_get("involvingMissions"), Mission)
    def get_mission_involvements(self):
        return create_e_list(self.e_get("missionInvolvements"), MissionInvolvement)
    def get_realized_entities(self):
        return create_e_list(self.e_get("realizedEntities"), Entity)
    def get_realizing_logical_components(self):
        return create_e_list(self.e_get("realizingLogicalComponents"), LogicalComponent)
    def get_allocated_system_functions(self):
        return create_e_list(self.e_get("allocatedSystemFunctions"), SystemFunction)
    def get_realized_operational_entities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizedComponents", self)

class IdentifiableElement(Element):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "IdentifiableElement"))
        elif isinstance(java_object, IdentifiableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "IdentifiableElement")
    def get_id(self):
        return self.e_get("id")
    def set_id(self, value):
        self.e_set("id", value)

class ReqIFElement(IdentifiableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "ReqIFElement"))
        elif isinstance(java_object, ReqIFElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "ReqIFElement")
    def get__req_i_f_identifier(self):
        return self.e_get("ReqIFIdentifier")
    def set__req_i_f_identifier(self, value):
        self.e_set("ReqIFIdentifier", value)
    def get__req_i_f_description(self):
        return self.e_get("ReqIFDescription")
    def set__req_i_f_description(self, value):
        self.e_set("ReqIFDescription", value)
    def get__req_i_f_long_name(self):
        return self.e_get("ReqIFLongName")
    def set__req_i_f_long_name(self, value):
        self.e_set("ReqIFLongName", value)

class TypesFolder(ReqIFElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "TypesFolder"))
        elif isinstance(java_object, TypesFolder):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "TypesFolder")
    #def get_owned_definition_types(self):
    #    return create_e_list(self.e_get("ownedDefinitionTypes"), DataTypeDefinition)
    def get_owned_types(self):
        return create_e_list(self.e_get("ownedTypes"), AbstractType)

class ElementExtension(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/emde/1.0.0", "ElementExtension"))
        elif isinstance(java_object, ElementExtension):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/emde/1.0.0", "ElementExtension")

class CapellaTypesFolder(TypesFolder, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaTypesFolder"))
        elif isinstance(java_object, CapellaTypesFolder):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaTypesFolder")

class AttributeOwner(ReqIFElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "AttributeOwner"))
        elif isinstance(java_object, AttributeOwner):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AttributeOwner")
    #def get_owned_attributes(self):
    #    return create_e_list(self.e_get("ownedAttributes"), Attribute)

class SharedDirectAttributes(Element):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "SharedDirectAttributes"))
        elif isinstance(java_object, SharedDirectAttributes):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "SharedDirectAttributes")
    def get__req_i_f_name(self):
        return self.e_get("ReqIFName")
    def set__req_i_f_name(self, value):
        self.e_set("ReqIFName", value)
    def get__req_i_f_prefix(self):
        return self.e_get("ReqIFPrefix")
    def set__req_i_f_prefix(self, value):
        self.e_set("ReqIFPrefix", value)

class Module(AttributeOwner, SharedDirectAttributes):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Module"))
        elif isinstance(java_object, Module):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "Module")
    def get_module_type(self):
        value =  self.e_get("moduleType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_module_type(self, value):
        return self.e_set("moduleType", value.get_java_object())
    def get_owned_requirements(self):
        return create_e_list(self.e_get("ownedRequirements"), Requirement)

class CapellaModule(Module, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaModule"))
        elif isinstance(java_object, CapellaModule):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaModule")

class AbstractRelation(ReqIFElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "AbstractRelation"))
        elif isinstance(java_object, AbstractRelation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/kitalpha/requirements", "AbstractRelation")
    def get_relation_type(self):
        value =  self.e_get("relationType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_relation_type(self, value):
        return self.e_set("relationType", value.get_java_object())
    def get_relation_type_proxy(self):
        return self.e_get("relationTypeProxy")
    def set_relation_type_proxy(self, value):
        self.e_set("relationTypeProxy", value)

class CapellaRelation(AbstractRelation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaRelation"))
        elif isinstance(java_object, CapellaRelation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaRelation")

class CapellaIncomingRelation(CapellaRelation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaIncomingRelation"))
        elif isinstance(java_object, CapellaIncomingRelation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaIncomingRelation")
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())

class CapellaOutgoingRelation(CapellaRelation, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation"))
        elif isinstance(java_object, CapellaOutgoingRelation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/requirements", "CapellaOutgoingRelation")
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())

class NamedRelationship(Relationship, NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamedRelationship"))
        elif isinstance(java_object, NamedRelationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "NamedRelationship")
    def get_naming_rules(self):
        return create_e_list(self.e_get("namingRules"), NamingRule)

class ReuserStructure(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuserStructure"))
        elif isinstance(java_object, ReuserStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ReuserStructure")
    def get_reuse_links(self):
        return create_e_list(self.e_get("reuseLinks"), ReuseLink)
    def get_owned_reuse_links(self):
        return create_e_list(self.e_get("ownedReuseLinks"), ReuseLink)

class AbstractModellingStructure(ReuserStructure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractModellingStructure"))
        elif isinstance(java_object, AbstractModellingStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractModellingStructure")
    def get_owned_architectures(self):
        return create_e_list(self.e_get("ownedArchitectures"), ModellingArchitecture)
    def get_owned_architecture_pkgs(self):
        return create_e_list(self.e_get("ownedArchitecturePkgs"), ModellingArchitecturePkg)

class ModellingArchitecturePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecturePkg"))
        elif isinstance(java_object, ModellingArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecturePkg")

class Trace(Relationship, AbstractTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Trace"))
        elif isinstance(java_object, Trace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Trace")
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsTraceTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsTraceSource", self)

class AbstractAnnotation(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractAnnotation"))
        elif isinstance(java_object, AbstractAnnotation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractAnnotation")
    def get_content(self):
        return self.e_get("content")
    def set_content(self, value):
        self.e_set("content", value)

class NamingRule(AbstractAnnotation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamingRule"))
        elif isinstance(java_object, NamingRule):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "NamingRule")
    def get_target_type(self):
        return self.e_get("targetType")
    def set_target_type(self, value):
        self.e_set("targetType", value)

class AbstractConstraint(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractConstraint"))
        elif isinstance(java_object, AbstractConstraint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractConstraint")
    def get_constrained_elements(self):
        return create_e_list(self.e_get("constrainedElements"), ModelElement)
    def get_owned_specification(self):
        value =  self.e_get("ownedSpecification")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_specification(self, value):
        return self.e_set("ownedSpecification", value.get_java_object())
    def get_context(self):
        value =  self.e_get("context")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class Constraint(NamedElement, AbstractConstraint):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Constraint"))
        elif isinstance(java_object, Constraint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Constraint")
    def get_constrained_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ConstraintModelElements", self)

class KeyValue(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "KeyValue"))
        elif isinstance(java_object, KeyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "KeyValue")
    def get_key(self):
        return self.e_get("key")
    def set_key(self, value):
        self.e_set("key", value)
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class ReuseLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseLink"))
        elif isinstance(java_object, ReuseLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseLink")
    def get_reused(self):
        value =  self.e_get("reused")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_reused(self, value):
        return self.e_set("reused", value.get_java_object())
    def get_reuser(self):
        value =  self.e_get("reuser")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_reuser(self, value):
        return self.e_set("reuser", value.get_java_object())

class ReuseableStructure(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseableStructure"))
        elif isinstance(java_object, ReuseableStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseableStructure")
    def get_reuse_links(self):
        return create_e_list(self.e_get("reuseLinks"), ReuseLink)

class GeneralClass(Classifier, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralClass"))
        elif isinstance(java_object, GeneralClass):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralClass")
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)
    def get_contained_operations(self):
        return create_e_list(self.e_get("containedOperations"), Operation)
    def get_nested_general_classes(self):
        return create_e_list(self.e_get("nestedGeneralClasses"), GeneralClass)

class Generalization(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Generalization"))
        elif isinstance(java_object, Generalization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "Generalization")
    def get_super(self):
        value =  self.e_get("super")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_super(self, value):
        return self.e_set("super", value.get_java_object())
    def get_sub(self):
        value =  self.e_get("sub")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_sub(self, value):
        return self.e_set("sub", value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsGeneralizationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsGeneralizationSource", self)

class AbstractExchangeItemPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractExchangeItemPkg"))
        elif isinstance(java_object, AbstractExchangeItemPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractExchangeItemPkg")
    def get_owned_exchange_items(self):
        return create_e_list(self.e_get("ownedExchangeItems"), ExchangeItem)

class AbstractPropertyValue(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractPropertyValue"))
        elif isinstance(java_object, AbstractPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractPropertyValue")
    def get_involved_elements(self):
        return create_e_list(self.e_get("involvedElements"), CapellaElement)
    def get_valued_elements(self):
        return create_e_list(self.e_get("valuedElements"), CapellaElement)
    def get_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyValue_applying_valued_element_Primitive", self)

class StringPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "StringPropertyValue"))
        elif isinstance(java_object, StringPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "StringPropertyValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class IntegerPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "IntegerPropertyValue"))
        elif isinstance(java_object, IntegerPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "IntegerPropertyValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class BooleanPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "BooleanPropertyValue"))
        elif isinstance(java_object, BooleanPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "BooleanPropertyValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class FloatPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "FloatPropertyValue"))
        elif isinstance(java_object, FloatPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "FloatPropertyValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class EnumerationPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyValue"))
        elif isinstance(java_object, EnumerationPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyValue")
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())
    def get_value(self):
        value =  self.e_get("value")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.e_set("value", value.get_java_object())

class EnumerationPropertyType(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyType"))
        elif isinstance(java_object, EnumerationPropertyType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyType")
    def get_owned_literals(self):
        return create_e_list(self.e_get("ownedLiterals"), EnumerationPropertyLiteral)

class EnumerationPropertyLiteral(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyLiteral"))
        elif isinstance(java_object, EnumerationPropertyLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyLiteral")

class PropertyValueGroup(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValueGroup"))
        elif isinstance(java_object, PropertyValueGroup):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValueGroup")
    def get_valued_elements(self):
        return create_e_list(self.e_get("valuedElements"), CapellaElement)

class PropertyValuePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValuePkg"))
        elif isinstance(java_object, PropertyValuePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValuePkg")

class AbstractDependenciesPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractDependenciesPkg"))
        elif isinstance(java_object, AbstractDependenciesPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractDependenciesPkg")
    def get_dependencies(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractDependenciesPkg_dependencies", self)
    def get_inverse_dependencies(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractDependenciesPkg_inverse_dependencies", self)

class Project(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Project"))
        elif isinstance(java_object, Project):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "Project")
    def get_key_value_pairs(self):
        return create_e_list(self.e_get("keyValuePairs"), KeyValue)
    def get_owned_folders(self):
        return create_e_list(self.e_get("ownedFolders"), Folder)
    def get_owned_model_roots(self):
        return create_e_list(self.e_get("ownedModelRoots"), ModelRoot)

class Folder(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Folder"))
        elif isinstance(java_object, Folder):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "Folder")
    def get_owned_folders(self):
        return create_e_list(self.e_get("ownedFolders"), Folder)
    def get_owned_model_roots(self):
        return create_e_list(self.e_get("ownedModelRoots"), ModelRoot)

class ModelRoot(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "ModelRoot"))
        elif isinstance(java_object, ModelRoot):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "ModelRoot")

class SystemEngineering(AbstractModellingStructure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineering"))
        elif isinstance(java_object, SystemEngineering):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineering")
    def get_contained_operational_analysis(self):
        return create_e_list(self.e_get("containedOperationalAnalysis"), OperationalAnalysis)
    def get_contained_system_analysis(self):
        return create_e_list(self.e_get("containedSystemAnalysis"), SystemAnalysis)
    def get_contained_logical_architectures(self):
        return create_e_list(self.e_get("containedLogicalArchitectures"), LogicalArchitecture)
    def get_contained_physical_architectures(self):
        return create_e_list(self.e_get("containedPhysicalArchitectures"), PhysicalArchitecture)
    def get_contained_e_p_b_s_architectures(self):
        return create_e_list(self.e_get("containedEPBSArchitectures"), EPBSArchitecture)
    def get_contained_shared_pkgs(self):
        return create_e_list(self.e_get("containedSharedPkgs"), SharedPkg)

class SystemEngineeringPkg(Structure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineeringPkg"))
        elif isinstance(java_object, SystemEngineeringPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineeringPkg")
    def get_owned_system_engineerings(self):
        return create_e_list(self.e_get("ownedSystemEngineerings"), SystemEngineering)

class Library(Project):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Library"))
        elif isinstance(java_object, Library):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/modeller/1.4.0", "Library")

class AssociationPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AssociationPkg"))
        elif isinstance(java_object, AssociationPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "AssociationPkg")
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)
    def get_owned_associations(self):
        return create_e_list(self.e_get("ownedAssociations"), Association)

class Association(NamedRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Association"))
        elif isinstance(java_object, Association):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Association")
    def get_owned_members(self):
        return create_e_list(self.e_get("ownedMembers"), Property)
    def get_navigable_members(self):
        return create_e_list(self.e_get("navigableMembers"), Property)
    def get_roles(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAssociationRoles", self)

class Class(GeneralClass):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Class"))
        elif isinstance(java_object, Class):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Class")
    def get_is_primitive(self):
        return self.e_get("isPrimitive")
    def set_is_primitive(self, value):
        self.e_set("isPrimitive", value)
    def get_key_parts(self):
        return create_e_list(self.e_get("keyParts"), KeyPart)
    def get_owned_state_machines(self):
        return create_e_list(self.e_get("ownedStateMachines"), StateMachine)
    def get_owned_data_values(self):
        return create_e_list(self.e_get("ownedDataValues"), DataValue)
    def get_owned_information_realizations(self):
        return create_e_list(self.e_get("ownedInformationRealizations"), InformationRealization)
    def get_realized_classes(self):
        return create_e_list(self.e_get("realizedClasses"), Class)
    def get_realizing_classes(self):
        return create_e_list(self.e_get("realizingClasses"), Class)

class DataValueContainer(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValueContainer"))
        elif isinstance(java_object, DataValueContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValueContainer")
    def get_owned_data_values(self):
        return create_e_list(self.e_get("ownedDataValues"), DataValue)

class Collection(Classifier, MultiplicityElement, DataValueContainer, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Collection"))
        elif isinstance(java_object, Collection):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Collection")
    def get_is_primitive(self):
        return self.e_get("isPrimitive")
    def set_is_primitive(self, value):
        self.e_set("isPrimitive", value)
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_aggregation_kind(self):
        return self.e_get("aggregationKind").getName()
    def set_aggregation_kind(self, value):
        self.e_set("aggregationKind", value)
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())
    def get_index(self):
        return create_e_list(self.e_get("index"), DataType)
    def get_contained_operations(self):
        return create_e_list(self.e_get("containedOperations"), Operation)

class ValueSpecification(AbstractTypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "ValueSpecification"))
        elif isinstance(java_object, ValueSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "ValueSpecification")

class DataValue(NamedElement, ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValue"))
        elif isinstance(java_object, DataValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValue")
    def get_abstract(self):
        return self.e_get("abstract")
    def set_abstract(self, value):
        self.e_set("abstract", value)
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyValue_applying_valued_element_DataValue", self)
    def get_referenced_property(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueRefReferencedProperty", self)
    def get_referenced_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueRefReferencedValue", self)
    def get_referencing_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueReferencingReferencedValue", self)

class AbstractCollectionValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractCollectionValue"))
        elif isinstance(java_object, AbstractCollectionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractCollectionValue")

class CollectionValue(AbstractCollectionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValue"))
        elif isinstance(java_object, CollectionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValue")
    def get_owned_elements(self):
        return create_e_list(self.e_get("ownedElements"), DataValue)
    def get_owned_default_element(self):
        value =  self.e_get("ownedDefaultElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_element(self, value):
        return self.e_set("ownedDefaultElement", value.get_java_object())

class CollectionValueReference(AbstractCollectionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValueReference"))
        elif isinstance(java_object, CollectionValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValueReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class MessageReferencePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReferencePkg"))
        elif isinstance(java_object, MessageReferencePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReferencePkg")
    def get_owned_message_references(self):
        return create_e_list(self.e_get("ownedMessageReferences"), MessageReference)

class DataPkg(AbstractDependenciesPkg, AbstractExchangeItemPkg, AssociationPkg, DataValueContainer, MessageReferencePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "DataPkg"))
        elif isinstance(java_object, DataPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "DataPkg")
    def get_owned_data_pkgs(self):
        return create_e_list(self.e_get("ownedDataPkgs"), DataPkg)
    def get_owned_classes(self):
        return create_e_list(self.e_get("ownedClasses"), Class)
    def get_owned_key_parts(self):
        return create_e_list(self.e_get("ownedKeyParts"), KeyPart)
    def get_owned_collections(self):
        return create_e_list(self.e_get("ownedCollections"), Collection)
    def get_owned_units(self):
        return create_e_list(self.e_get("ownedUnits"), Unit)
    def get_owned_data_types(self):
        return create_e_list(self.e_get("ownedDataTypes"), DataType)
    def get_owned_signals(self):
        return create_e_list(self.e_get("ownedSignals"), Signal)
    def get_owned_messages(self):
        return create_e_list(self.e_get("ownedMessages"), Message)
    def get_owned_exceptions(self):
        return create_e_list(self.e_get("ownedExceptions"), ExceptionCapella)
    def get_owned_state_events(self):
        return create_e_list(self.e_get("ownedStateEvents"), StateEvent)

class DomainElement(Class):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "DomainElement"))
        elif isinstance(java_object, DomainElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "DomainElement")

class KeyPart(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "KeyPart"))
        elif isinstance(java_object, KeyPart):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "KeyPart")
    def get_property(self):
        value =  self.e_get("property")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_property(self, value):
        return self.e_set("property", value.get_java_object())

class AbstractEventOperation(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractEventOperation"))
        elif isinstance(java_object, AbstractEventOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractEventOperation")
    def get_invoking_sequence_messages(self):
        return create_e_list(self.e_get("invokingSequenceMessages"), SequenceMessage)

class Operation(Feature, AbstractEvent, AbstractEventOperation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Operation"))
        elif isinstance(java_object, Operation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Operation")
    def get_owned_parameters(self):
        return create_e_list(self.e_get("ownedParameters"), Parameter)
    def get_allocating_operations(self):
        return create_e_list(self.e_get("allocatingOperations"), Operation)
    def get_allocated_operations(self):
        return create_e_list(self.e_get("allocatedOperations"), Operation)
    def get_owned_operation_allocation(self):
        return create_e_list(self.e_get("ownedOperationAllocation"), OperationAllocation)
    def get_owned_exchange_item_realizations(self):
        return create_e_list(self.e_get("ownedExchangeItemRealizations"), ExchangeItemRealization)
    def get_realized_exchange_items(self):
        return create_e_list(self.e_get("realizedExchangeItems"), ExchangeItem)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class OperationAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "OperationAllocation"))
        elif isinstance(java_object, OperationAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "OperationAllocation")
    def get_allocated_operation(self):
        value =  self.e_get("allocatedOperation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_operation(self):
        value =  self.e_get("allocatingOperation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class AbstractParameter(AbstractTypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameter"))
        elif isinstance(java_object, AbstractParameter):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameter")
    def get_is_exception(self):
        return self.e_get("isException")
    def set_is_exception(self, value):
        self.e_set("isException", value)
    def get_is_stream(self):
        return self.e_get("isStream")
    def set_is_stream(self, value):
        self.e_set("isStream", value)
    def get_is_optional(self):
        return self.e_get("isOptional")
    def set_is_optional(self, value):
        self.e_set("isOptional", value)
    def get_kind_of_rate(self):
        return self.e_get("kindOfRate").getName()
    def set_kind_of_rate(self, value):
        self.e_set("kindOfRate", value)
    def get_effect(self):
        return self.e_get("effect").getName()
    def set_effect(self, value):
        self.e_set("effect", value)
    def get_rate(self):
        value =  self.e_get("rate")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_rate(self, value):
        return self.e_set("rate", value.get_java_object())
    def get_probability(self):
        value =  self.e_get("probability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_probability(self, value):
        return self.e_set("probability", value.get_java_object())
    def get_parameter_set(self):
        return create_e_list(self.e_get("parameterSet"), AbstractParameterSet)

class Parameter(TypedElement, MultiplicityElement, AbstractParameter):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Parameter"))
        elif isinstance(java_object, Parameter):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Parameter")
    def get_direction(self):
        return self.e_get("direction").getName()
    def set_direction(self, value):
        self.e_set("direction", value)
    def get_passing_mode(self):
        return self.e_get("passingMode").getName()
    def set_passing_mode(self, value):
        self.e_set("passingMode", value)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Parameter_Type", self)

class Service(Operation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Service"))
        elif isinstance(java_object, Service):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Service")
    def get_synchronism_kind(self):
        return self.e_get("synchronismKind").getName()
    def set_synchronism_kind(self, value):
        self.e_set("synchronismKind", value)
    def get_thrown_exceptions(self):
        return create_e_list(self.e_get("thrownExceptions"), ExceptionCapella)
    def get_messages(self):
        return create_e_list(self.e_get("messages"), Message)
    def get_message_references(self):
        return create_e_list(self.e_get("messageReferences"), MessageReference)

class Union(Class):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Union"))
        elif isinstance(java_object, Union):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Union")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_discriminant(self):
        value =  self.e_get("discriminant")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_discriminant(self, value):
        return self.e_set("discriminant", value.get_java_object())
    def get_default_property(self):
        value =  self.e_get("defaultProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_default_property(self, value):
        return self.e_set("defaultProperty", value.get_java_object())
    def get_contained_union_properties(self):
        return create_e_list(self.e_get("containedUnionProperties"), UnionProperty)

class UnionProperty(Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "UnionProperty"))
        elif isinstance(java_object, UnionProperty):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "UnionProperty")
    def get_qualifier(self):
        return create_e_list(self.e_get("qualifier"), DataValue)

class Unit(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Unit"))
        elif isinstance(java_object, Unit):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Unit")

class Port(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Port"))
        elif isinstance(java_object, Port):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "Port")
    def get_incoming_port_realizations(self):
        return create_e_list(self.e_get("incomingPortRealizations"), PortRealization)
    def get_outgoing_port_realizations(self):
        return create_e_list(self.e_get("outgoingPortRealizations"), PortRealization)
    def get_owned_protocols(self):
        return create_e_list(self.e_get("ownedProtocols"), StateMachine)
    def get_incoming_port_allocations(self):
        return create_e_list(self.e_get("incomingPortAllocations"), PortAllocation)
    def get_outgoing_port_allocations(self):
        return create_e_list(self.e_get("outgoingPortAllocations"), PortAllocation)
    def get_provided_interfaces(self):
        return create_e_list(self.e_get("providedInterfaces"), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.e_get("requiredInterfaces"), Interface)
    def get_owned_port_realizations(self):
        return create_e_list(self.e_get("ownedPortRealizations"), PortRealization)
    def get_owned_port_allocations(self):
        return create_e_list(self.e_get("ownedPortAllocations"), PortAllocation)

class PortRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "PortRealization"))
        elif isinstance(java_object, PortRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "PortRealization")
    def get_realized_port(self):
        value =  self.e_get("realizedPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_port(self):
        value =  self.e_get("realizingPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class PortAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "PortAllocation"))
        elif isinstance(java_object, PortAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "PortAllocation")
    def get_allocated_port(self):
        value =  self.e_get("allocatedPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_port(self):
        value =  self.e_get("allocatingPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class AbstractExchangeItem(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractExchangeItem"))
        elif isinstance(java_object, AbstractExchangeItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractExchangeItem")

class AbstractSignal(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignal"))
        elif isinstance(java_object, AbstractSignal):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignal")

class ExchangeItem(AbstractExchangeItem, AbstractEvent, AbstractSignal, FinalizableElement, GeneralizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItem"))
        elif isinstance(java_object, ExchangeItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItem")
    def get_exchange_mechanism(self):
        return self.e_get("exchangeMechanism").getName()
    def set_exchange_mechanism(self, value):
        self.e_set("exchangeMechanism", value)
    def get_owned_elements(self):
        return create_e_list(self.e_get("ownedElements"), ExchangeItemElement)
    def get_owned_information_realizations(self):
        return create_e_list(self.e_get("ownedInformationRealizations"), InformationRealization)
    def get_owned_exchange_item_instances(self):
        return create_e_list(self.e_get("ownedExchangeItemInstances"), ExchangeItemInstance)
    def get_allocator_interfaces(self):
        return create_e_list(self.e_get("allocatorInterfaces"), Interface)
    def get_realized_exchange_items(self):
        return create_e_list(self.e_get("realizedExchangeItems"), ExchangeItem)
    def get_realizing_exchange_items(self):
        return create_e_list(self.e_get("realizingExchangeItems"), ExchangeItem)
    def get_realizing_operations(self):
        return create_e_list(self.e_get("realizingOperations"), Operation)
    def get_exchange_item_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangesItemExchangeItemElements", self)
    def get_allocating_function_output_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemAllocatingOutPutFunctionPorts", self)
    def get_allocating_function_input_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemAllocatingInputFunctionPorts", self)
    def get_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangesItemExchangeItemAllocations", self)
    def get_communication_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangesItemCommLink", self)
    def get_allocating_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.EIActiveInConnectionsAndExchanges", self)

class ExchangeItemElement(NamedElement, MultiplicityElement, TypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemElement"))
        elif isinstance(java_object, ExchangeItemElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemElement")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_direction(self):
        return self.e_get("direction").getName()
    def set_direction(self, value):
        self.e_set("direction", value)
    def get_composite(self):
        return self.e_get("composite")
    def set_composite(self, value):
        self.e_set("composite", value)
    def get_referenced_properties(self):
        return create_e_list(self.e_get("referencedProperties"), Property)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemElementType", self)

class ExchangeItemInstance(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemInstance"))
        elif isinstance(java_object, ExchangeItemInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemInstance")
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class InformationRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "InformationRealization"))
        elif isinstance(java_object, InformationRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "InformationRealization")

class ExchangeItemRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemRealization"))
        elif isinstance(java_object, ExchangeItemRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemRealization")
    def get_realized_item(self):
        value =  self.e_get("realizedItem")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_operation(self):
        value =  self.e_get("realizingOperation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class CommunicationItem(Classifier, DataValueContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationItem"))
        elif isinstance(java_object, CommunicationItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationItem")
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)
    def get_owned_state_machines(self):
        return create_e_list(self.e_get("ownedStateMachines"), StateMachine)
    def get_properties(self):
        return create_e_list(self.e_get("properties"), Property)

class ExceptionCapella(CommunicationItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "ExceptionCapella"))
        elif isinstance(java_object, ExceptionCapella):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "ExceptionCapella")

class Message(CommunicationItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Message"))
        elif isinstance(java_object, Message):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Message")

class MessageReference(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReference"))
        elif isinstance(java_object, MessageReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReference")
    def get_message(self):
        value =  self.e_get("message")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_message(self, value):
        return self.e_set("message", value.get_java_object())

class Signal(CommunicationItem, AbstractSignal):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Signal"))
        elif isinstance(java_object, Signal):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Signal")
    def get_signal_instances(self):
        return create_e_list(self.e_get("signalInstances"), SignalInstance)

class SignalInstance(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "SignalInstance"))
        elif isinstance(java_object, SignalInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "SignalInstance")

class CommunicationLink(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLink"))
        elif isinstance(java_object, CommunicationLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLink")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_protocol(self):
        return self.e_get("protocol").getName()
    def set_protocol(self, value):
        self.e_set("protocol", value)
    def get_exchange_item(self):
        value =  self.e_get("exchangeItem")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_item(self, value):
        return self.e_set("exchangeItem", value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationLinkExchangeItem", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationLinkComponent", self)

class DataType(GeneralizableElement, DataValueContainer, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "DataType"))
        elif isinstance(java_object, DataType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "DataType")
    def get_discrete(self):
        return self.e_get("discrete")
    def set_discrete(self, value):
        self.e_set("discrete", value)
    def get_min_inclusive(self):
        return self.e_get("minInclusive")
    def set_min_inclusive(self, value):
        self.e_set("minInclusive", value)
    def get_max_inclusive(self):
        return self.e_get("maxInclusive")
    def set_max_inclusive(self, value):
        self.e_set("maxInclusive", value)
    def get_pattern(self):
        return self.e_get("pattern")
    def set_pattern(self, value):
        self.e_set("pattern", value)
    def get_visibility(self):
        return self.e_get("visibility").getName()
    def set_visibility(self, value):
        self.e_set("visibility", value)
    def get_default_value(self):
        value =  self.e_get("defaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_null_value(self):
        value =  self.e_get("nullValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_information_realizations(self):
        return create_e_list(self.e_get("ownedInformationRealizations"), InformationRealization)
    def get_realized_data_types(self):
        return create_e_list(self.e_get("realizedDataTypes"), DataType)
    def get_realizing_data_types(self):
        return create_e_list(self.e_get("realizingDataTypes"), DataType)

class BooleanType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "BooleanType"))
        elif isinstance(java_object, BooleanType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "BooleanType")
    def get_owned_literals(self):
        return create_e_list(self.e_get("ownedLiterals"), LiteralBooleanValue)
    def get_owned_default_value(self):
        value =  self.e_get("ownedDefaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_value(self, value):
        return self.e_set("ownedDefaultValue", value.get_java_object())

class Enumeration(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "Enumeration"))
        elif isinstance(java_object, Enumeration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "Enumeration")
    def get_owned_literals(self):
        return create_e_list(self.e_get("ownedLiterals"), EnumerationLiteral)
    def get_owned_default_value(self):
        value =  self.e_get("ownedDefaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_value(self, value):
        return self.e_set("ownedDefaultValue", value.get_java_object())
    def get_owned_null_value(self):
        value =  self.e_get("ownedNullValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_null_value(self, value):
        return self.e_set("ownedNullValue", value.get_java_object())
    def get_owned_min_value(self):
        value =  self.e_get("ownedMinValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_value(self, value):
        return self.e_set("ownedMinValue", value.get_java_object())
    def get_owned_max_value(self):
        value =  self.e_get("ownedMaxValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_value(self, value):
        return self.e_set("ownedMaxValue", value.get_java_object())
    def get_domain_type(self):
        value =  self.e_get("domainType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_domain_type(self, value):
        return self.e_set("domainType", value.get_java_object())

class StringType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "StringType"))
        elif isinstance(java_object, StringType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "StringType")
    def get_owned_default_value(self):
        value =  self.e_get("ownedDefaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_value(self, value):
        return self.e_set("ownedDefaultValue", value.get_java_object())
    def get_owned_null_value(self):
        value =  self.e_get("ownedNullValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_null_value(self, value):
        return self.e_set("ownedNullValue", value.get_java_object())
    def get_owned_min_length(self):
        value =  self.e_get("ownedMinLength")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_length(self, value):
        return self.e_set("ownedMinLength", value.get_java_object())
    def get_owned_max_length(self):
        value =  self.e_get("ownedMaxLength")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_length(self, value):
        return self.e_set("ownedMaxLength", value.get_java_object())

class NumericType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "NumericType"))
        elif isinstance(java_object, NumericType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "NumericType")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_owned_default_value(self):
        value =  self.e_get("ownedDefaultValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_default_value(self, value):
        return self.e_set("ownedDefaultValue", value.get_java_object())
    def get_owned_null_value(self):
        value =  self.e_get("ownedNullValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_null_value(self, value):
        return self.e_set("ownedNullValue", value.get_java_object())
    def get_owned_min_value(self):
        value =  self.e_get("ownedMinValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_min_value(self, value):
        return self.e_set("ownedMinValue", value.get_java_object())
    def get_owned_max_value(self):
        value =  self.e_get("ownedMaxValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_max_value(self, value):
        return self.e_set("ownedMaxValue", value.get_java_object())

class PhysicalQuantity(NumericType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "PhysicalQuantity"))
        elif isinstance(java_object, PhysicalQuantity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "PhysicalQuantity")
    def get_unit(self):
        value =  self.e_get("unit")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_unit(self, value):
        return self.e_set("unit", value.get_java_object())

class AbstractBooleanValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractBooleanValue"))
        elif isinstance(java_object, AbstractBooleanValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractBooleanValue")
    def get_boolean_type(self):
        value =  self.e_get("booleanType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class LiteralBooleanValue(AbstractBooleanValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralBooleanValue"))
        elif isinstance(java_object, LiteralBooleanValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralBooleanValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class BooleanReference(AbstractBooleanValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BooleanReference"))
        elif isinstance(java_object, BooleanReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BooleanReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class AbstractEnumerationValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractEnumerationValue"))
        elif isinstance(java_object, AbstractEnumerationValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractEnumerationValue")
    def get_enumeration_type(self):
        value =  self.e_get("enumerationType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class EnumerationLiteral(AbstractEnumerationValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationLiteral"))
        elif isinstance(java_object, EnumerationLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationLiteral")
    def get_domain_value(self):
        value =  self.e_get("domainValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_domain_value(self, value):
        return self.e_set("domainValue", value.get_java_object())

class EnumerationReference(AbstractEnumerationValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationReference"))
        elif isinstance(java_object, EnumerationReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class AbstractStringValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractStringValue"))
        elif isinstance(java_object, AbstractStringValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractStringValue")
    def get_string_type(self):
        value =  self.e_get("stringType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class LiteralStringValue(AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralStringValue"))
        elif isinstance(java_object, LiteralStringValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralStringValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class StringReference(AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "StringReference"))
        elif isinstance(java_object, StringReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "StringReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class NumericValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericValue"))
        elif isinstance(java_object, NumericValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericValue")
    def get_unit(self):
        value =  self.e_get("unit")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_unit(self, value):
        return self.e_set("unit", value.get_java_object())
    def get_numeric_type(self):
        value =  self.e_get("numericType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class LiteralNumericValue(NumericValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralNumericValue"))
        elif isinstance(java_object, LiteralNumericValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralNumericValue")
    def get_value(self):
        return self.e_get("value")
    def set_value(self, value):
        self.e_set("value", value)

class NumericReference(NumericValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericReference"))
        elif isinstance(java_object, NumericReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class AbstractComplexValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractComplexValue"))
        elif isinstance(java_object, AbstractComplexValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractComplexValue")
    def get_complex_type(self):
        value =  self.e_get("complexType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComplexValue(AbstractComplexValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValue"))
        elif isinstance(java_object, ComplexValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValue")
    def get_owned_parts(self):
        return create_e_list(self.e_get("ownedParts"), ValuePart)

class ComplexValueReference(AbstractComplexValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValueReference"))
        elif isinstance(java_object, ComplexValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValueReference")
    def get_referenced_value(self):
        value =  self.e_get("referencedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_value(self, value):
        return self.e_set("referencedValue", value.get_java_object())
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())

class ValuePart(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ValuePart"))
        elif isinstance(java_object, ValuePart):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ValuePart")
    def get_referenced_property(self):
        value =  self.e_get("referencedProperty")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_property(self, value):
        return self.e_set("referencedProperty", value.get_java_object())
    def get_owned_value(self):
        value =  self.e_get("ownedValue")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_value(self, value):
        return self.e_set("ownedValue", value.get_java_object())

class AbstractExpressionValue(AbstractBooleanValue, AbstractComplexValue, AbstractEnumerationValue, NumericValue, AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractExpressionValue"))
        elif isinstance(java_object, AbstractExpressionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractExpressionValue")
    def get_expression(self):
        return self.e_get("expression")
    def get_unparsed_expression(self):
        return self.e_get("unparsedExpression")
    def set_unparsed_expression(self, value):
        self.e_set("unparsedExpression", value)
    def get_expression_type(self):
        value =  self.e_get("expressionType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class BinaryExpression(AbstractExpressionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BinaryExpression"))
        elif isinstance(java_object, BinaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BinaryExpression")
    def get_operator(self):
        return self.e_get("operator").getName()
    def set_operator(self, value):
        self.e_set("operator", value)
    def get_owned_left_operand(self):
        value =  self.e_get("ownedLeftOperand")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_left_operand(self, value):
        return self.e_set("ownedLeftOperand", value.get_java_object())
    def get_owned_right_operand(self):
        value =  self.e_get("ownedRightOperand")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_right_operand(self, value):
        return self.e_set("ownedRightOperand", value.get_java_object())

class UnaryExpression(AbstractExpressionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "UnaryExpression"))
        elif isinstance(java_object, UnaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "UnaryExpression")
    def get_operator(self):
        return self.e_get("operator").getName()
    def set_operator(self, value):
        self.e_set("operator", value)
    def get_owned_operand(self):
        value =  self.e_get("ownedOperand")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_operand(self, value):
        return self.e_set("ownedOperand", value.get_java_object())

class OpaqueExpression(CapellaElement, ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "OpaqueExpression"))
        elif isinstance(java_object, OpaqueExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "OpaqueExpression")
    def get_bodies(self):
        return self.e_get("bodies")
    def set_bodies(self, value):
        self.e_set("bodies", value)
    def get_languages(self):
        return self.e_get("languages")
    def set_languages(self, value):
        self.e_set("languages", value)

class AbstractBehavior(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractBehavior"))
        elif isinstance(java_object, AbstractBehavior):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractBehavior")
    def get_is_control_operator(self):
        return self.e_get("isControlOperator")
    def set_is_control_operator(self, value):
        self.e_set("isControlOperator", value)
    def get_owned_parameter_set(self):
        return create_e_list(self.e_get("ownedParameterSet"), AbstractParameterSet)
    def get_owned_parameter(self):
        return create_e_list(self.e_get("ownedParameter"), AbstractParameter)

class AbstractTimeEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractTimeEvent"))
        elif isinstance(java_object, AbstractTimeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractTimeEvent")
    def get_is_relative(self):
        return self.e_get("isRelative")
    def set_is_relative(self, value):
        self.e_set("isRelative", value)
    def get_when(self):
        value =  self.e_get("when")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_when(self, value):
        return self.e_set("when", value.get_java_object())

class AbstractMessageEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractMessageEvent"))
        elif isinstance(java_object, AbstractMessageEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractMessageEvent")

class AbstractSignalEvent(AbstractMessageEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignalEvent"))
        elif isinstance(java_object, AbstractSignalEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignalEvent")
    def get_signal(self):
        value =  self.e_get("signal")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_signal(self, value):
        return self.e_set("signal", value.get_java_object())

class TimeExpression(ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "TimeExpression"))
        elif isinstance(java_object, TimeExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/behavior/1.4.0", "TimeExpression")
    def get_observations(self):
        value =  self.e_get("observations")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_observations(self, value):
        return self.e_set("observations", value.get_java_object())
    def get_expression(self):
        value =  self.e_get("expression")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_expression(self, value):
        return self.e_set("expression", value.get_java_object())

class AbstractActivity(AbstractBehavior, TraceableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractActivity"))
        elif isinstance(java_object, AbstractActivity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractActivity")
    def get_is_read_only(self):
        return self.e_get("isReadOnly")
    def set_is_read_only(self, value):
        self.e_set("isReadOnly", value)
    def get_is_single_execution(self):
        return self.e_get("isSingleExecution")
    def set_is_single_execution(self, value):
        self.e_set("isSingleExecution", value)
    def get_owned_nodes(self):
        return create_e_list(self.e_get("ownedNodes"), ActivityNode)
    def get_owned_edges(self):
        return create_e_list(self.e_get("ownedEdges"), ActivityEdge)
    def get_owned_groups(self):
        return create_e_list(self.e_get("ownedGroups"), ActivityGroup)
    def get_owned_structured_nodes(self):
        return create_e_list(self.e_get("ownedStructuredNodes"), StructuredActivityNode)

class FunctionSpecification(Namespace, AbstractActivity):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionSpecification"))
        elif isinstance(java_object, FunctionSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionSpecification")
    def get_in_exchange_links(self):
        return create_e_list(self.e_get("inExchangeLinks"), ExchangeLink)
    def get_out_exchange_links(self):
        return create_e_list(self.e_get("outExchangeLinks"), ExchangeLink)
    def get_owned_function_ports(self):
        return create_e_list(self.e_get("ownedFunctionPorts"), FunctionPort)
    def get_sub_function_specifications(self):
        return create_e_list(self.e_get("subFunctionSpecifications"), FunctionSpecification)

class ExchangeCategory(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeCategory"))
        elif isinstance(java_object, ExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeCategory")
    def get_exchanges(self):
        return create_e_list(self.e_get("exchanges"), FunctionalExchange)
    def get_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CategoryFunctionalExchange", self)

class ExchangeLink(NamedRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeLink"))
        elif isinstance(java_object, ExchangeLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeLink")
    def get_exchanges(self):
        return create_e_list(self.e_get("exchanges"), ExchangeSpecification)
    def get_exchange_containment_links(self):
        return create_e_list(self.e_get("exchangeContainmentLinks"), ExchangeContainment)
    def get_owned_exchange_containments(self):
        return create_e_list(self.e_get("ownedExchangeContainments"), ExchangeContainment)
    def get_sources(self):
        return create_e_list(self.e_get("sources"), FunctionSpecification)
    def get_destinations(self):
        return create_e_list(self.e_get("destinations"), FunctionSpecification)

class ExchangeContainment(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeContainment"))
        elif isinstance(java_object, ExchangeContainment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeContainment")
    def get_exchange(self):
        value =  self.e_get("exchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exchange(self, value):
        return self.e_set("exchange", value.get_java_object())
    def get_link(self):
        value =  self.e_get("link")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_link(self, value):
        return self.e_set("link", value.get_java_object())

class AbstractInformationFlow(AbstractNamedElement, AbstractRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractInformationFlow"))
        elif isinstance(java_object, AbstractInformationFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractInformationFlow")
    def get_realizations(self):
        return create_e_list(self.e_get("realizations"), AbstractRelationship)
    def get_convoyed_informations(self):
        return create_e_list(self.e_get("convoyedInformations"), AbstractExchangeItem)
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())

class ActivityExchange(AbstractInformationFlow):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityExchange"))
        elif isinstance(java_object, ActivityExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityExchange")
    def get_realizing_activity_flows(self):
        return create_e_list(self.e_get("realizingActivityFlows"), ActivityEdge)

class ExchangeSpecification(NamedElement, ActivityExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecification"))
        elif isinstance(java_object, ExchangeSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecification")
    def get_containing_link(self):
        value =  self.e_get("containingLink")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_link(self):
        value =  self.e_get("link")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_link(self, value):
        return self.e_set("link", value.get_java_object())
    def get_outgoing_exchange_specification_realizations(self):
        return create_e_list(self.e_get("outgoingExchangeSpecificationRealizations"), ExchangeSpecificationRealization)
    def get_incoming_exchange_specification_realizations(self):
        return create_e_list(self.e_get("incomingExchangeSpecificationRealizations"), ExchangeSpecificationRealization)
    def get_realized_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_realizedDataflow", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_dataflowTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_dataflowSource", self)

class FunctionalExchangeSpecification(ExchangeSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeSpecification"))
        elif isinstance(java_object, FunctionalExchangeSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeSpecification")
    def get_functional_exchanges(self):
        return create_e_list(self.e_get("functionalExchanges"), FunctionalExchange)

class FunctionalChain(NamedElement, InvolverElement, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChain"))
        elif isinstance(java_object, FunctionalChain):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChain")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_owned_functional_chain_involvements(self):
        return create_e_list(self.e_get("ownedFunctionalChainInvolvements"), FunctionalChainInvolvement)
    def get_owned_functional_chain_realizations(self):
        return create_e_list(self.e_get("ownedFunctionalChainRealizations"), FunctionalChainRealization)
    def get_involved_functional_chain_involvements(self):
        return create_e_list(self.e_get("involvedFunctionalChainInvolvements"), FunctionalChainInvolvement)
    def get_involved_functions(self):
        return create_e_list(self.e_get("involvedFunctions"), AbstractFunction)
    def get_involved_functional_exchanges(self):
        return create_e_list(self.e_get("involvedFunctionalExchanges"), FunctionalExchange)
    def get_involved_elements(self):
        return create_e_list(self.e_get("involvedElements"), InvolvedElement)
    def get_enacted_functions(self):
        return create_e_list(self.e_get("enactedFunctions"), AbstractFunction)
    def get_enacted_functional_blocks(self):
        return create_e_list(self.e_get("enactedFunctionalBlocks"), AbstractFunctionalBlock)
    def get_available_in_states(self):
        return create_e_list(self.e_get("availableInStates"), State)
    def get_first_functional_chain_involvements(self):
        return create_e_list(self.e_get("firstFunctionalChainInvolvements"), FunctionalChainInvolvement)
    def get_involving_capabilities(self):
        return create_e_list(self.e_get("involvingCapabilities"), Capability)
    def get_involving_capability_realizations(self):
        return create_e_list(self.e_get("involvingCapabilityRealizations"), CapabilityRealization)
    def get_realized_functional_chains(self):
        return create_e_list(self.e_get("realizedFunctionalChains"), FunctionalChain)
    def get_realizing_functional_chains(self):
        return create_e_list(self.e_get("realizingFunctionalChains"), FunctionalChain)
    def get_pre_condition(self):
        value =  self.e_get("preCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.e_set("preCondition", value.get_java_object())
    def get_post_condition(self):
        value =  self.e_get("postCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.e_set("postCondition", value.get_java_object())
    def get_owned_sequence_nodes(self):
        return create_e_list(self.e_get("ownedSequenceNodes"), ControlNode)
    def get_owned_sequence_links(self):
        return create_e_list(self.e_get("ownedSequenceLinks"), SequenceLink)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChain_owningFunction", self)
    def get_realized_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizedOperationalProcess", self)
    def get_involved_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainChildren", self)
    def get_active_in_states(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainAvailableInState", self)
    def get_involvement_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementLinks", self)
    def get_involved_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChain_enactedComponents", self)
    def get_active_in_modes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainAvailableInMode", self)
    def get_parent_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainParent", self)

class FunctionalChainInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvement"))
        elif isinstance(java_object, FunctionalChainInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvement")
    def get_next_functional_chain_involvements(self):
        return create_e_list(self.e_get("nextFunctionalChainInvolvements"), FunctionalChainInvolvement)
    def get_previous_functional_chain_involvements(self):
        return create_e_list(self.e_get("previousFunctionalChainInvolvements"), FunctionalChainInvolvement)
    def get_involved_element(self):
        value =  self.e_get("involvedElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class FunctionalChainReference(FunctionalChainInvolvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainReference"))
        elif isinstance(java_object, FunctionalChainReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainReference")
    def get_referenced_functional_chain(self):
        value =  self.e_get("referencedFunctionalChain")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_involved_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementFunctions", self)
    def get_involved_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainChildren", self)
    def get_involvement_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementLinks", self)
    def get_parent_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainParent", self)

class FunctionPort(Port, TypedElement, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionPort"))
        elif isinstance(java_object, FunctionPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionPort")
    def get_represented_component_port(self):
        value =  self.e_get("representedComponentPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_represented_component_port(self, value):
        return self.e_set("representedComponentPort", value.get_java_object())
    def get_allocator_component_ports(self):
        return create_e_list(self.e_get("allocatorComponentPorts"), ComponentPort)
    def get_realized_function_ports(self):
        return create_e_list(self.e_get("realizedFunctionPorts"), FunctionPort)
    def get_realizing_function_ports(self):
        return create_e_list(self.e_get("realizingFunctionPorts"), FunctionPort)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionPortAllocatedExchangeItems", self)
    def get_allocating_component_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionPortAllocatingCompoentPort", self)

class ObjectNode(ActivityNode, AbstractTypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ObjectNode"))
        elif isinstance(java_object, ObjectNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ObjectNode")
    def get_is_control_type(self):
        return self.e_get("isControlType")
    def set_is_control_type(self, value):
        self.e_set("isControlType", value)
    def get_kind_of_node(self):
        return self.e_get("kindOfNode").getName()
    def set_kind_of_node(self, value):
        self.e_set("kindOfNode", value)
    def get_ordering(self):
        return self.e_get("ordering").getName()
    def set_ordering(self, value):
        self.e_set("ordering", value)
    def get_upper_bound(self):
        value =  self.e_get("upperBound")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_upper_bound(self, value):
        return self.e_set("upperBound", value.get_java_object())
    def get_in_state(self):
        return create_e_list(self.e_get("inState"), IState)
    def get_selection(self):
        value =  self.e_get("selection")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_selection(self, value):
        return self.e_set("selection", value.get_java_object())

class Pin(ObjectNode):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "Pin"))
        elif isinstance(java_object, Pin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "Pin")
    def get_is_control(self):
        return self.e_get("isControl")
    def set_is_control(self, value):
        self.e_set("isControl", value)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_type", self)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_owner", self)
    def get_realized_pin(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_realizedFlowPort", self)
    def get_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_outgoingDataflows", self)
    def get_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_incomingDataflows", self)
    def get_realizing_pin(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Pin_realizingFlowPort", self)

class InputPin(Pin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "InputPin"))
        elif isinstance(java_object, InputPin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "InputPin")
    def get_input_evaluation_action(self):
        value =  self.e_get("inputEvaluationAction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_input_evaluation_action(self, value):
        return self.e_set("inputEvaluationAction", value.get_java_object())

class FunctionInputPort(FunctionPort, InputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionInputPort"))
        elif isinstance(java_object, FunctionInputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionInputPort")
    def get_incoming_exchange_items(self):
        return create_e_list(self.e_get("incomingExchangeItems"), ExchangeItem)
    def get_incoming_functional_exchanges(self):
        return create_e_list(self.e_get("incomingFunctionalExchanges"), FunctionalExchange)

class OutputPin(Pin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "OutputPin"))
        elif isinstance(java_object, OutputPin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "OutputPin")

class FunctionOutputPort(FunctionPort, OutputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionOutputPort"))
        elif isinstance(java_object, FunctionOutputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionOutputPort")
    def get_outgoing_exchange_items(self):
        return create_e_list(self.e_get("outgoingExchangeItems"), ExchangeItem)
    def get_outgoing_functional_exchanges(self):
        return create_e_list(self.e_get("outgoingFunctionalExchanges"), FunctionalExchange)

class AbstractFunctionAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionAllocation"))
        elif isinstance(java_object, AbstractFunctionAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionAllocation")

class ComponentFunctionalAllocation(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentFunctionalAllocation"))
        elif isinstance(java_object, ComponentFunctionalAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentFunctionalAllocation")
    def get_function(self):
        value =  self.e_get("function")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_block(self):
        value =  self.e_get("block")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class FunctionalChainRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainRealization"))
        elif isinstance(java_object, FunctionalChainRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainRealization")

class ExchangeSpecificationRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecificationRealization"))
        elif isinstance(java_object, ExchangeSpecificationRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecificationRealization")
    def get_realized_exchange_specification(self):
        value =  self.e_get("realizedExchangeSpecification")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_exchange_specification(self):
        value =  self.e_get("realizingExchangeSpecification")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class FunctionalExchangeRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeRealization"))
        elif isinstance(java_object, FunctionalExchangeRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeRealization")
    def get_realized_functional_exchange(self):
        value =  self.e_get("realizedFunctionalExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_functional_exchange(self):
        value =  self.e_get("realizingFunctionalExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class FunctionRealization(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionRealization"))
        elif isinstance(java_object, FunctionRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionRealization")
    def get_allocated_function(self):
        value =  self.e_get("allocatedFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_function(self):
        value =  self.e_get("allocatingFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ActivityEdge(AbstractRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityEdge"))
        elif isinstance(java_object, ActivityEdge):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityEdge")
    def get_kind_of_rate(self):
        return self.e_get("kindOfRate").getName()
    def set_kind_of_rate(self, value):
        self.e_set("kindOfRate", value)
    def get_in_activity_partition(self):
        value =  self.e_get("inActivityPartition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_in_interruptible_region(self):
        value =  self.e_get("inInterruptibleRegion")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_in_structured_node(self):
        value =  self.e_get("inStructuredNode")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_rate(self):
        value =  self.e_get("rate")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_rate(self, value):
        return self.e_set("rate", value.get_java_object())
    def get_probability(self):
        value =  self.e_get("probability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_probability(self, value):
        return self.e_set("probability", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_guard(self):
        value =  self.e_get("guard")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.e_set("guard", value.get_java_object())
    def get_weight(self):
        value =  self.e_get("weight")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_weight(self, value):
        return self.e_set("weight", value.get_java_object())
    def get_interrupts(self):
        value =  self.e_get("interrupts")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_interrupts(self, value):
        return self.e_set("interrupts", value.get_java_object())

class ObjectFlow(ActivityEdge):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ObjectFlow"))
        elif isinstance(java_object, ObjectFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ObjectFlow")
    def get_is_multicast(self):
        return self.e_get("isMulticast")
    def set_is_multicast(self, value):
        self.e_set("isMulticast", value)
    def get_is_multireceive(self):
        return self.e_get("isMultireceive")
    def set_is_multireceive(self, value):
        self.e_set("isMultireceive", value)
    def get_transformation(self):
        value =  self.e_get("transformation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_transformation(self, value):
        return self.e_set("transformation", value.get_java_object())
    def get_selection(self):
        value =  self.e_get("selection")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_selection(self, value):
        return self.e_set("selection", value.get_java_object())

class FunctionalExchange(NamedElement, Relationship, InvolvedElement, ObjectFlow, AbstractEvent, AbstractEventOperation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchange"))
        elif isinstance(java_object, FunctionalExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchange")
    def get_exchange_specifications(self):
        return create_e_list(self.e_get("exchangeSpecifications"), FunctionalExchangeSpecification)
    def get_involving_functional_chains(self):
        return create_e_list(self.e_get("involvingFunctionalChains"), FunctionalChain)
    def get_exchanged_items(self):
        return create_e_list(self.e_get("exchangedItems"), ExchangeItem)
    def get_allocating_component_exchanges(self):
        return create_e_list(self.e_get("allocatingComponentExchanges"), ComponentExchange)
    def get_incoming_component_exchange_functional_exchange_realizations(self):
        return create_e_list(self.e_get("incomingComponentExchangeFunctionalExchangeRealizations"), ComponentExchangeFunctionalExchangeAllocation)
    def get_incoming_functional_exchange_realizations(self):
        return create_e_list(self.e_get("incomingFunctionalExchangeRealizations"), FunctionalExchangeRealization)
    def get_outgoing_functional_exchange_realizations(self):
        return create_e_list(self.e_get("outgoingFunctionalExchangeRealizations"), FunctionalExchangeRealization)
    def get_categories(self):
        return create_e_list(self.e_get("categories"), ExchangeCategory)
    def get_owned_functional_exchange_realizations(self):
        return create_e_list(self.e_get("ownedFunctionalExchangeRealizations"), FunctionalExchangeRealization)
    def get_source_function_output_port(self):
        value =  self.e_get("sourceFunctionOutputPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target_function_input_port(self):
        value =  self.e_get("targetFunctionInputPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realized_functional_exchanges(self):
        return create_e_list(self.e_get("realizedFunctionalExchanges"), FunctionalExchange)
    def get_realizing_functional_exchanges(self):
        return create_e_list(self.e_get("realizingFunctionalExchanges"), FunctionalExchange)
    def get_related_data(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_relatedData", self)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_owner", self)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeExchangesItems", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_dataflowTarget", self)
    def get_realized_functional_exchange(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeRealizedFunctionalExchanges", self)
    def get_realized_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeRealizedInteractions", self)
    def get_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeFunctionalChain", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_dataflowSource", self)
    def get_allocating_communicationmean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeAllocatingCommunicationMean", self)
    def get_allocating_component_exchange(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeAllocatingComponentExchange", self)
    def get_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeOperationalProcess", self)

class ComponentExchange(AbstractEvent, AbstractEventOperation, NamedElement, ExchangeSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchange"))
        elif isinstance(java_object, ComponentExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchange")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_oriented(self):
        return self.e_get("oriented")
    def set_oriented(self, value):
        self.e_set("oriented", value)
    def get_allocated_functional_exchanges(self):
        return create_e_list(self.e_get("allocatedFunctionalExchanges"), FunctionalExchange)
    def get_incoming_component_exchange_realizations(self):
        return create_e_list(self.e_get("incomingComponentExchangeRealizations"), ComponentExchangeRealization)
    def get_outgoing_component_exchange_realizations(self):
        return create_e_list(self.e_get("outgoingComponentExchangeRealizations"), ComponentExchangeRealization)
    def get_outgoing_component_exchange_functional_exchange_allocations(self):
        return create_e_list(self.e_get("outgoingComponentExchangeFunctionalExchangeAllocations"), ComponentExchangeFunctionalExchangeAllocation)
    def get_owned_component_exchange_functional_exchange_allocations(self):
        return create_e_list(self.e_get("ownedComponentExchangeFunctionalExchangeAllocations"), ComponentExchangeFunctionalExchangeAllocation)
    def get_owned_component_exchange_realizations(self):
        return create_e_list(self.e_get("ownedComponentExchangeRealizations"), ComponentExchangeRealization)
    def get_owned_component_exchange_ends(self):
        return create_e_list(self.e_get("ownedComponentExchangeEnds"), ComponentExchangeEnd)
    def get_source_port(self):
        value =  self.e_get("sourcePort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_source_part(self):
        value =  self.e_get("sourcePart")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target_port(self):
        value =  self.e_get("targetPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target_part(self):
        value =  self.e_get("targetPart")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_categories(self):
        return create_e_list(self.e_get("categories"), ComponentExchangeCategory)
    def get_allocator_physical_links(self):
        return create_e_list(self.e_get("allocatorPhysicalLinks"), PhysicalLink)
    def get_realized_component_exchanges(self):
        return create_e_list(self.e_get("realizedComponentExchanges"), ComponentExchange)
    def get_realizing_component_exchanges(self):
        return create_e_list(self.e_get("realizingComponentExchanges"), ComponentExchange)
    def get_related_data(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_relatedData", self)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_owner", self)
    def get_inherited_categories(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeCategoriesForDelegations", self)
    def get_connected_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Connection_connectedComponents", self)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ConnectionConvoyedInformation", self)
    def get_realized_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponenExchangeRealizedCommunicationMean", self)
    def get_connectedparts(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Connection_connectedParts", self)
    def get_allocating_physical_path(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeAllocatingPhysicalPath", self)
    def get_allocating_physical_link(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeAllocatingPhysicalLink", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class ComponentExchangeAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocation"))
        elif isinstance(java_object, ComponentExchangeAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocation")
    def get_component_exchange_allocated(self):
        value =  self.e_get("componentExchangeAllocated")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_component_exchange_allocator(self):
        value =  self.e_get("componentExchangeAllocator")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComponentExchangeAllocator(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocator"))
        elif isinstance(java_object, ComponentExchangeAllocator):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocator")
    def get_owned_component_exchange_allocations(self):
        return create_e_list(self.e_get("ownedComponentExchangeAllocations"), ComponentExchangeAllocation)
    def get_allocated_component_exchanges(self):
        return create_e_list(self.e_get("allocatedComponentExchanges"), ComponentExchange)

class ComponentExchangeCategory(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeCategory"))
        elif isinstance(java_object, ComponentExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeCategory")
    def get_exchanges(self):
        return create_e_list(self.e_get("exchanges"), ComponentExchange)
    def get_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CategoryComponentExchange", self)

class InformationsExchanger(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "InformationsExchanger"))
        elif isinstance(java_object, InformationsExchanger):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "InformationsExchanger")
    def get_incoming_information_flows(self):
        return create_e_list(self.e_get("incomingInformationFlows"), AbstractInformationFlow)
    def get_outgoing_information_flows(self):
        return create_e_list(self.e_get("outgoingInformationFlows"), AbstractInformationFlow)
    def get_information_flows(self):
        return create_e_list(self.e_get("informationFlows"), AbstractInformationFlow)

class ComponentExchangeEnd(InformationsExchanger, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeEnd"))
        elif isinstance(java_object, ComponentExchangeEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeEnd")
    def get_port(self):
        value =  self.e_get("port")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_port(self, value):
        return self.e_set("port", value.get_java_object())
    def get_part(self):
        value =  self.e_get("part")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_part(self, value):
        return self.e_set("part", value.get_java_object())

class ComponentExchangeFunctionalExchangeAllocation(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeFunctionalExchangeAllocation"))
        elif isinstance(java_object, ComponentExchangeFunctionalExchangeAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeFunctionalExchangeAllocation")
    def get_allocated_functional_exchange(self):
        value =  self.e_get("allocatedFunctionalExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_component_exchange(self):
        value =  self.e_get("allocatingComponentExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComponentExchangeRealization(ExchangeSpecificationRealization):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeRealization"))
        elif isinstance(java_object, ComponentExchangeRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeRealization")
    def get_allocated_component_exchange(self):
        value =  self.e_get("allocatedComponentExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_component_exchange(self):
        value =  self.e_get("allocatingComponentExchange")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComponentPort(Port, InformationsExchanger, Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPort"))
        elif isinstance(java_object, ComponentPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPort")
    def get_orientation(self):
        return self.e_get("orientation").getName()
    def set_orientation(self, value):
        self.e_set("orientation", value)
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_component_exchanges(self):
        return create_e_list(self.e_get("componentExchanges"), ComponentExchange)
    def get_allocated_function_ports(self):
        return create_e_list(self.e_get("allocatedFunctionPorts"), FunctionPort)
    def get_delegated_component_ports(self):
        return create_e_list(self.e_get("delegatedComponentPorts"), ComponentPort)
    def get_delegating_component_ports(self):
        return create_e_list(self.e_get("delegatingComponentPorts"), ComponentPort)
    def get_allocating_physical_ports(self):
        return create_e_list(self.e_get("allocatingPhysicalPorts"), PhysicalPort)
    def get_realized_component_ports(self):
        return create_e_list(self.e_get("realizedComponentPorts"), ComponentPort)
    def get_realizing_component_ports(self):
        return create_e_list(self.e_get("realizingComponentPorts"), ComponentPort)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_type", self)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_owner", self)
    def get_provided_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_providedInterfaces", self)
    def get_required_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_requiredInterfaces", self)
    def get_outgoing_delegations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPortOutgoingDeletations", self)
    def get_outgoing_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPortOutgoingComponentExchanges", self)
    def get_incoming_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPortIncomingComponentExchanges", self)
    def get_incoming_delegations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPortIncomingDeletations", self)

class ComponentPortAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPortAllocation"))
        elif isinstance(java_object, ComponentPortAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPortAllocation")
    def get_owned_component_port_allocation_ends(self):
        return create_e_list(self.e_get("ownedComponentPortAllocationEnds"), ComponentPortAllocationEnd)
    def get_allocated_port(self):
        value =  self.e_get("allocatedPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_port(self):
        value =  self.e_get("allocatingPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ComponentPortAllocationEnd(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPortAllocationEnd"))
        elif isinstance(java_object, ComponentPortAllocationEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPortAllocationEnd")
    def get_port(self):
        value =  self.e_get("port")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_port(self, value):
        return self.e_set("port", value.get_java_object())
    def get_part(self):
        value =  self.e_get("part")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_part(self, value):
        return self.e_set("part", value.get_java_object())
    def get_owning_component_port_allocation(self):
        value =  self.e_get("owningComponentPortAllocation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ReferenceHierarchyContext(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ReferenceHierarchyContext"))
        elif isinstance(java_object, ReferenceHierarchyContext):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ReferenceHierarchyContext")
    def get_source_reference_hierarchy(self):
        return create_e_list(self.e_get("sourceReferenceHierarchy"), FunctionalChainReference)
    def get_target_reference_hierarchy(self):
        return create_e_list(self.e_get("targetReferenceHierarchy"), FunctionalChainReference)
    def get_source_reference_hierachy(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ReferenceHierarchyContextSource", self)
    def get_target_reference_hierachy(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ReferenceHierarchyContextTarget", self)

class FunctionalChainInvolvementLink(FunctionalChainInvolvement, ReferenceHierarchyContext):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvementLink"))
        elif isinstance(java_object, FunctionalChainInvolvementLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvementLink")
    def get_exchange_context(self):
        value =  self.e_get("exchangeContext")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_context(self, value):
        return self.e_set("exchangeContext", value.get_java_object())
    def get_exchanged_items(self):
        return create_e_list(self.e_get("exchangedItems"), ExchangeItem)
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())

class SequenceLink(CapellaElement, ReferenceHierarchyContext):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "SequenceLink"))
        elif isinstance(java_object, SequenceLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "SequenceLink")
    def get_condition(self):
        value =  self.e_get("condition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_condition(self, value):
        return self.e_set("condition", value.get_java_object())
    def get_links(self):
        return create_e_list(self.e_get("links"), FunctionalChainInvolvementLink)
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementOwner", self)
    def get_target_control_node(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkTargetControlNode", self)
    def get_target_involvement_function(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkTargetInvolvementFunction", self)
    def get_source_involvement_function(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkSourceInvolvementFunction", self)
    def get_source_control_node(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkSourceControlNode", self)

class SequenceLinkEnd(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "SequenceLinkEnd"))
        elif isinstance(java_object, SequenceLinkEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "SequenceLinkEnd")
    def get_target_sequence_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkEndTargetSequenceLinks", self)
    def get_source_sequence_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkEndSourceSequenceLinks", self)

class FunctionalChainInvolvementFunction(FunctionalChainInvolvement, SequenceLinkEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvementFunction"))
        elif isinstance(java_object, FunctionalChainInvolvementFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvementFunction")
    def get_outgoing_involvement_links(self):
        return create_e_list(self.e_get("outgoingInvolvementLinks"), FunctionalChainInvolvementLink)
    def get_incoming_involvement_links(self):
        return create_e_list(self.e_get("incomingInvolvementLinks"), FunctionalChainInvolvementLink)
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementOwner", self)

class ControlNode(SequenceLinkEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ControlNode"))
        elif isinstance(java_object, ControlNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/fa/1.4.0", "ControlNode")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)

class RequirementsPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsPkg"))
        elif isinstance(java_object, RequirementsPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsPkg")
    def get_additional_information(self):
        return self.e_get("additionalInformation")
    def set_additional_information(self, value):
        self.e_set("additionalInformation", value)
    def get_level(self):
        return self.e_get("level")
    def set_level(self, value):
        self.e_set("level", value)
    def get_owned_requirements(self):
        return create_e_list(self.e_get("ownedRequirements"), Requirement)
    def get_owned_requirement_pkgs(self):
        return create_e_list(self.e_get("ownedRequirementPkgs"), RequirementsPkg)

class RequirementsTrace(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsTrace"))
        elif isinstance(java_object, RequirementsTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsTrace")
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class Requirement(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "Requirement"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "Requirement")
    def get_is_obsolete(self):
        return self.e_get("isObsolete")
    def set_is_obsolete(self, value):
        self.e_set("isObsolete", value)
    def get_requirement_id(self):
        return self.e_get("requirementId")
    def set_requirement_id(self, value):
        self.e_set("requirementId", value)
    def get_additional_information(self):
        return self.e_get("additionalInformation")
    def set_additional_information(self, value):
        self.e_set("additionalInformation", value)
    def get_verification_method(self):
        return self.e_get("verificationMethod")
    def set_verification_method(self, value):
        self.e_set("verificationMethod", value)
    def get_verification_phase(self):
        return self.e_get("verificationPhase")
    def set_verification_phase(self, value):
        self.e_set("verificationPhase", value)
    def get_implementation_version(self):
        return self.e_get("implementationVersion")
    def set_implementation_version(self, value):
        self.e_set("implementationVersion", value)
    def get_feature(self):
        return self.e_get("feature")
    def set_feature(self, value):
        self.e_set("feature", value)
    def get_related_capella_elements(self):
        return create_e_list(self.e_get("relatedCapellaElements"), CapellaElement)
    def get_traced_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.RequirementTracedElements", self)

class SystemFunctionalInterfaceRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemFunctionalInterfaceRequirement"))
        elif isinstance(java_object, SystemFunctionalInterfaceRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemFunctionalInterfaceRequirement")

class SystemFunctionalRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemFunctionalRequirement"))
        elif isinstance(java_object, SystemFunctionalRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemFunctionalRequirement")

class SystemNonFunctionalInterfaceRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalInterfaceRequirement"))
        elif isinstance(java_object, SystemNonFunctionalInterfaceRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalInterfaceRequirement")

class SystemNonFunctionalRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalRequirement"))
        elif isinstance(java_object, SystemNonFunctionalRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalRequirement")

class SystemUserRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemUserRequirement"))
        elif isinstance(java_object, SystemUserRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemUserRequirement")

class OperationalAnalysis(BlockArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalAnalysis"))
        elif isinstance(java_object, OperationalAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalAnalysis")
    def get_owned_role_pkg(self):
        value =  self.e_get("ownedRolePkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_role_pkg(self, value):
        return self.e_set("ownedRolePkg", value.get_java_object())
    def get_owned_entity_pkg(self):
        value =  self.e_get("ownedEntityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_entity_pkg(self, value):
        return self.e_set("ownedEntityPkg", value.get_java_object())
    def get_owned_concept_pkg(self):
        value =  self.e_get("ownedConceptPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_concept_pkg(self, value):
        return self.e_set("ownedConceptPkg", value.get_java_object())
    def get_contained_operational_capability_pkg(self):
        value =  self.e_get("containedOperationalCapabilityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_contained_operational_activity_pkg(self):
        value =  self.e_get("containedOperationalActivityPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_system_analyses(self):
        return create_e_list(self.e_get("allocatingSystemAnalyses"), SystemAnalysis)

class OperationalScenario(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalScenario"))
        elif isinstance(java_object, OperationalScenario):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalScenario")
    def get_context(self):
        return self.e_get("context")
    def set_context(self, value):
        self.e_set("context", value)
    def get_objective(self):
        return self.e_get("objective")
    def set_objective(self, value):
        self.e_set("objective", value)

class OperationalActivityPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivityPkg"))
        elif isinstance(java_object, OperationalActivityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivityPkg")
    def get_owned_operational_activities(self):
        return create_e_list(self.e_get("ownedOperationalActivities"), OperationalActivity)
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.e_get("ownedOperationalActivityPkgs"), OperationalActivityPkg)

class OperationalActivity(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivity"))
        elif isinstance(java_object, OperationalActivity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivity")
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.e_get("ownedOperationalActivityPkgs"), OperationalActivityPkg)
    def get_activity_allocations(self):
        return create_e_list(self.e_get("activityAllocations"), ActivityAllocation)
    def get_owned_swimlanes(self):
        return create_e_list(self.e_get("ownedSwimlanes"), Swimlane)
    def get_owned_process(self):
        return create_e_list(self.e_get("ownedProcess"), OperationalProcess)
    def get_allocator_entities(self):
        return create_e_list(self.e_get("allocatorEntities"), Entity)
    def get_realizing_system_functions(self):
        return create_e_list(self.e_get("realizingSystemFunctions"), SystemFunction)
    def get_allocating_roles(self):
        return create_e_list(self.e_get("allocatingRoles"), Role)
    def get_contained_operational_activities(self):
        return create_e_list(self.e_get("containedOperationalActivities"), OperationalActivity)
    def get_children_operational_activities(self):
        return create_e_list(self.e_get("childrenOperationalActivities"), OperationalActivity)
    def get_owned_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_ownedFunctionalChains", self)
    def get_internal_outgoing_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalOutGoingDataflows", self)
    def get_outgoing_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_outgoingInteraction", self)
    def get_internal_incoming_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalInComingDataflows", self)
    def get_allocating_entity(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingComponent", self)
    def get_allocating_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_mother_activity_allocation", self)
    def get_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalActivityOperationalProcess", self)
    def get_allocating_role(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationActivityAllocatingRole", self)
    def get_incoming_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_incomingInteraction", self)
    def get_allocating_operational_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingActor", self)

class OperationalProcess(FunctionalChain):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalProcess"))
        elif isinstance(java_object, OperationalProcess):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalProcess")
    def get_involving_operational_capabilities(self):
        return create_e_list(self.e_get("involvingOperationalCapabilities"), OperationalCapability)
    def get_involved_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalProcessChildren", self)
    def get_involved_operational_activities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalProcessInvolvedOperationalActivities", self)
    def get_parent_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalProcessParent", self)

class ActivityGroup(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityGroup"))
        elif isinstance(java_object, ActivityGroup):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityGroup")
    def get_super_group(self):
        value =  self.e_get("superGroup")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_super_group(self, value):
        return self.e_set("superGroup", value.get_java_object())
    def get_sub_groups(self):
        return create_e_list(self.e_get("subGroups"), ActivityGroup)
    def get_owned_nodes(self):
        return create_e_list(self.e_get("ownedNodes"), ActivityNode)
    def get_owned_edges(self):
        return create_e_list(self.e_get("ownedEdges"), ActivityEdge)

class ActivityPartition(ActivityGroup, AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityPartition"))
        elif isinstance(java_object, ActivityPartition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityPartition")
    def get_is_dimension(self):
        return self.e_get("isDimension")
    def set_is_dimension(self, value):
        self.e_set("isDimension", value)
    def get_is_external(self):
        return self.e_get("isExternal")
    def set_is_external(self, value):
        self.e_set("isExternal", value)
    def get_represented_element(self):
        value =  self.e_get("representedElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_represented_element(self, value):
        return self.e_set("representedElement", value.get_java_object())
    def get_super_partition(self):
        value =  self.e_get("superPartition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_sub_partitions(self):
        return create_e_list(self.e_get("subPartitions"), ActivityPartition)

class Swimlane(NamedElement, ActivityPartition):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Swimlane"))
        elif isinstance(java_object, Swimlane):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "Swimlane")
    def get_represented_entity(self):
        value =  self.e_get("representedEntity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class OperationalCapabilityPkg(AbstractCapabilityPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapabilityPkg"))
        elif isinstance(java_object, OperationalCapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapabilityPkg")
    def get_owned_operational_capabilities(self):
        return create_e_list(self.e_get("ownedOperationalCapabilities"), OperationalCapability)
    def get_owned_operational_capability_pkgs(self):
        return create_e_list(self.e_get("ownedOperationalCapabilityPkgs"), OperationalCapabilityPkg)
    def get_owned_capability_configurations(self):
        return create_e_list(self.e_get("ownedCapabilityConfigurations"), CapabilityConfiguration)
    def get_owned_concept_compliances(self):
        return create_e_list(self.e_get("ownedConceptCompliances"), ConceptCompliance)

class OperationalCapability(AbstractCapability, Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapability"))
        elif isinstance(java_object, OperationalCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapability")
    def get_compliances(self):
        return create_e_list(self.e_get("compliances"), ConceptCompliance)
    def get_configurations(self):
        return create_e_list(self.e_get("configurations"), CapabilityConfiguration)
    def get_owned_entity_operational_capability_involvements(self):
        return create_e_list(self.e_get("ownedEntityOperationalCapabilityInvolvements"), EntityOperationalCapabilityInvolvement)
    def get_realizing_capabilities(self):
        return create_e_list(self.e_get("realizingCapabilities"), Capability)
    def get_involved_entities(self):
        return create_e_list(self.e_get("involvedEntities"), Entity)
    def get_owned_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityOwnedFunctionalChains", self)
    def get_involved_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityInvolvedFunctionalChains", self)

class ActivityAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ActivityAllocation"))
        elif isinstance(java_object, ActivityAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "ActivityAllocation")
    def get_role(self):
        value =  self.e_get("role")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_activity(self):
        value =  self.e_get("activity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class RolePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "RolePkg"))
        elif isinstance(java_object, RolePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "RolePkg")
    def get_owned_role_pkgs(self):
        return create_e_list(self.e_get("ownedRolePkgs"), RolePkg)
    def get_owned_roles(self):
        return create_e_list(self.e_get("ownedRoles"), Role)

class Role(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Role"))
        elif isinstance(java_object, Role):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "Role")
    def get_owned_role_assembly_usages(self):
        return create_e_list(self.e_get("ownedRoleAssemblyUsages"), RoleAssemblyUsage)
    def get_owned_activity_allocations(self):
        return create_e_list(self.e_get("ownedActivityAllocations"), ActivityAllocation)
    def get_role_allocations(self):
        return create_e_list(self.e_get("roleAllocations"), RoleAllocation)
    def get_activity_allocations(self):
        return create_e_list(self.e_get("activityAllocations"), ActivityAllocation)
    def get_allocating_entities(self):
        return create_e_list(self.e_get("allocatingEntities"), Entity)
    def get_allocated_operational_activities(self):
        return create_e_list(self.e_get("allocatedOperationalActivities"), OperationalActivity)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class RoleAssemblyUsage(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "RoleAssemblyUsage"))
        elif isinstance(java_object, RoleAssemblyUsage):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "RoleAssemblyUsage")
    def get_child(self):
        value =  self.e_get("child")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_child(self, value):
        return self.e_set("child", value.get_java_object())

class RoleAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "RoleAllocation"))
        elif isinstance(java_object, RoleAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "RoleAllocation")
    def get_role(self):
        value =  self.e_get("role")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_entity(self):
        value =  self.e_get("entity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class EntityPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "EntityPkg"))
        elif isinstance(java_object, EntityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "EntityPkg")
    def get_owned_entities(self):
        return create_e_list(self.e_get("ownedEntities"), Entity)
    def get_owned_entity_pkgs(self):
        return create_e_list(self.e_get("ownedEntityPkgs"), EntityPkg)
    def get_owned_locations(self):
        return create_e_list(self.e_get("ownedLocations"), Location)
    def get_owned_communication_means(self):
        return create_e_list(self.e_get("ownedCommunicationMeans"), CommunicationMean)

class AbstractConceptItem(Component):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "AbstractConceptItem"))
        elif isinstance(java_object, AbstractConceptItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "AbstractConceptItem")
    def get_composing_links(self):
        return create_e_list(self.e_get("composingLinks"), ItemInConcept)

class Entity(AbstractConceptItem, InformationsExchanger, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Entity"))
        elif isinstance(java_object, Entity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "Entity")
    def get_role_allocations(self):
        return create_e_list(self.e_get("roleAllocations"), RoleAllocation)
    def get_organisational_unit_memberships(self):
        return create_e_list(self.e_get("organisationalUnitMemberships"), OrganisationalUnitComposition)
    def get_actual_location(self):
        value =  self.e_get("actualLocation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_actual_location(self, value):
        return self.e_set("actualLocation", value.get_java_object())
    def get_sub_entities(self):
        return create_e_list(self.e_get("subEntities"), Entity)
    def get_owned_entities(self):
        return create_e_list(self.e_get("ownedEntities"), Entity)
    def get_owned_communication_means(self):
        return create_e_list(self.e_get("ownedCommunicationMeans"), CommunicationMean)
    def get_owned_role_allocations(self):
        return create_e_list(self.e_get("ownedRoleAllocations"), RoleAllocation)
    def get_allocated_operational_activities(self):
        return create_e_list(self.e_get("allocatedOperationalActivities"), OperationalActivity)
    def get_allocated_roles(self):
        return create_e_list(self.e_get("allocatedRoles"), Role)
    def get_involving_operational_capabilities(self):
        return create_e_list(self.e_get("involvingOperationalCapabilities"), OperationalCapability)
    def get_realizing_system_components(self):
        return create_e_list(self.e_get("realizingSystemComponents"), SystemComponent)
    def get_breakdown(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_Breakdown", self)
    def get_outgoing_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_OutgoingCommunicationMean", self)
    def get_incoming_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_IncomingCommunicationMean", self)

class ConceptPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptPkg"))
        elif isinstance(java_object, ConceptPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptPkg")
    def get_owned_concept_pkgs(self):
        return create_e_list(self.e_get("ownedConceptPkgs"), ConceptPkg)
    def get_owned_concepts(self):
        return create_e_list(self.e_get("ownedConcepts"), Concept)

class Concept(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Concept"))
        elif isinstance(java_object, Concept):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "Concept")
    def get_compliances(self):
        return create_e_list(self.e_get("compliances"), ConceptCompliance)
    def get_composite_links(self):
        return create_e_list(self.e_get("compositeLinks"), ItemInConcept)

class ConceptCompliance(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptCompliance"))
        elif isinstance(java_object, ConceptCompliance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptCompliance")
    def get_comply_with_concept(self):
        value =  self.e_get("complyWithConcept")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_comply_with_concept(self, value):
        return self.e_set("complyWithConcept", value.get_java_object())
    def get_compliant_capability(self):
        value =  self.e_get("compliantCapability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_compliant_capability(self, value):
        return self.e_set("compliantCapability", value.get_java_object())

class ItemInConcept(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ItemInConcept"))
        elif isinstance(java_object, ItemInConcept):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "ItemInConcept")
    def get_concept(self):
        value =  self.e_get("concept")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_concept(self, value):
        return self.e_set("concept", value.get_java_object())
    def get_item(self):
        value =  self.e_get("item")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_item(self, value):
        return self.e_set("item", value.get_java_object())

class CommunityOfInterest(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterest"))
        elif isinstance(java_object, CommunityOfInterest):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterest")
    def get_community_of_interest_compositions(self):
        return create_e_list(self.e_get("communityOfInterestCompositions"), CommunityOfInterestComposition)

class CommunityOfInterestComposition(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterestComposition"))
        elif isinstance(java_object, CommunityOfInterestComposition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterestComposition")
    def get_community_of_interest(self):
        value =  self.e_get("communityOfInterest")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_community_of_interest(self, value):
        return self.e_set("communityOfInterest", value.get_java_object())
    def get_interested_organisation_unit(self):
        value =  self.e_get("interestedOrganisationUnit")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_interested_organisation_unit(self, value):
        return self.e_set("interestedOrganisationUnit", value.get_java_object())

class OrganisationalUnit(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnit"))
        elif isinstance(java_object, OrganisationalUnit):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnit")
    def get_organisational_unit_compositions(self):
        return create_e_list(self.e_get("organisationalUnitCompositions"), OrganisationalUnitComposition)
    def get_community_of_interest_memberships(self):
        return create_e_list(self.e_get("communityOfInterestMemberships"), CommunityOfInterestComposition)

class OrganisationalUnitComposition(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnitComposition"))
        elif isinstance(java_object, OrganisationalUnitComposition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnitComposition")
    def get_organisational_unit(self):
        value =  self.e_get("organisationalUnit")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_organisational_unit(self, value):
        return self.e_set("organisationalUnit", value.get_java_object())
    def get_participating_entity(self):
        value =  self.e_get("participatingEntity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_participating_entity(self, value):
        return self.e_set("participatingEntity", value.get_java_object())

class Location(AbstractConceptItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Location"))
        elif isinstance(java_object, Location):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "Location")
    def get_location_description(self):
        return self.e_get("locationDescription")
    def set_location_description(self, value):
        self.e_set("locationDescription", value)
    def get_located_entities(self):
        return create_e_list(self.e_get("locatedEntities"), Entity)

class CapabilityConfiguration(AbstractConceptItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CapabilityConfiguration"))
        elif isinstance(java_object, CapabilityConfiguration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "CapabilityConfiguration")
    def get_configured_capability(self):
        value =  self.e_get("configuredCapability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_configured_capability(self, value):
        return self.e_set("configuredCapability", value.get_java_object())

class CommunicationMean(NamedRelationship, ComponentExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunicationMean"))
        elif isinstance(java_object, CommunicationMean):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunicationMean")
    def get_source_entity(self):
        value =  self.e_get("sourceEntity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target_entity(self):
        value =  self.e_get("targetEntity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocated_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationMean_AllocatedExchanges", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationMean_Target", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationMean_Source", self)

class EntityOperationalCapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "EntityOperationalCapabilityInvolvement"))
        elif isinstance(java_object, EntityOperationalCapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/oa/1.4.0", "EntityOperationalCapabilityInvolvement")
    def get_entity(self):
        value =  self.e_get("entity")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_capability(self):
        value =  self.e_get("capability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class BlockArchitecturePkg(ModellingArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecturePkg"))
        elif isinstance(java_object, BlockArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecturePkg")

class EPBSArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecturePkg"))
        elif isinstance(java_object, EPBSArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecturePkg")
    def get_owned_e_p_b_s_architectures(self):
        return create_e_list(self.e_get("ownedEPBSArchitectures"), EPBSArchitecture)

class EPBSArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecture"))
        elif isinstance(java_object, EPBSArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecture")
    def get_owned_configuration_item_pkg(self):
        value =  self.e_get("ownedConfigurationItemPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_configuration_item_pkg(self, value):
        return self.e_set("ownedConfigurationItemPkg", value.get_java_object())
    def get_contained_capability_realization_pkg(self):
        value =  self.e_get("containedCapabilityRealizationPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_physical_architecture_realizations(self):
        return create_e_list(self.e_get("ownedPhysicalArchitectureRealizations"), PhysicalArchitectureRealization)
    def get_allocated_physical_architecture_realizations(self):
        return create_e_list(self.e_get("allocatedPhysicalArchitectureRealizations"), PhysicalArchitectureRealization)
    def get_allocated_physical_architectures(self):
        return create_e_list(self.e_get("allocatedPhysicalArchitectures"), PhysicalArchitecture)

class ConfigurationItemPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItemPkg"))
        elif isinstance(java_object, ConfigurationItemPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItemPkg")
    def get_owned_configuration_items(self):
        return create_e_list(self.e_get("ownedConfigurationItems"), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.e_get("ownedConfigurationItemPkgs"), ConfigurationItemPkg)

class CapabilityRealizationInvolvedElement(InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvedElement"))
        elif isinstance(java_object, CapabilityRealizationInvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvedElement")
    def get_capability_realization_involvements(self):
        return create_e_list(self.e_get("capabilityRealizationInvolvements"), CapabilityRealizationInvolvement)
    def get_involving_capability_realizations(self):
        return create_e_list(self.e_get("involvingCapabilityRealizations"), CapabilityRealization)

class ConfigurationItem(CapabilityRealizationInvolvedElement, Component):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItem"))
        elif isinstance(java_object, ConfigurationItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItem")
    def get_item_identifier(self):
        return self.e_get("itemIdentifier")
    def set_item_identifier(self, value):
        self.e_set("itemIdentifier", value)
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_owned_configuration_items(self):
        return create_e_list(self.e_get("ownedConfigurationItems"), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.e_get("ownedConfigurationItemPkgs"), ConfigurationItemPkg)
    def get_owned_physical_artifact_realizations(self):
        return create_e_list(self.e_get("ownedPhysicalArtifactRealizations"), PhysicalArtifactRealization)
    def get_allocated_physical_artifacts(self):
        return create_e_list(self.e_get("allocatedPhysicalArtifacts"), AbstractPhysicalArtifact)
    def get_realized_physical_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CIRealizedPhysicalComponents", self)
    def get_realized_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CIRealizedPhysicalLinks", self)
    def get_realized_physical_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CIRealizedPhysicalPorts", self)

class PhysicalArchitectureRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "PhysicalArchitectureRealization"))
        elif isinstance(java_object, PhysicalArchitectureRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "PhysicalArchitectureRealization")

class PhysicalArtifactRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "PhysicalArtifactRealization"))
        elif isinstance(java_object, PhysicalArtifactRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/epbs/1.4.0", "PhysicalArtifactRealization")
    def get_realized_physical_artifact(self):
        value =  self.e_get("realizedPhysicalArtifact")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_configuration_item(self):
        value =  self.e_get("realizingConfigurationItem")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ExceptionHandler(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ExceptionHandler"))
        elif isinstance(java_object, ExceptionHandler):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ExceptionHandler")
    def get_protected_node(self):
        value =  self.e_get("protectedNode")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_protected_node(self, value):
        return self.e_set("protectedNode", value.get_java_object())
    def get_handler_body(self):
        value =  self.e_get("handlerBody")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_handler_body(self, value):
        return self.e_set("handlerBody", value.get_java_object())
    def get_exception_input(self):
        value =  self.e_get("exceptionInput")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exception_input(self, value):
        return self.e_set("exceptionInput", value.get_java_object())
    def get_exception_types(self):
        return create_e_list(self.e_get("exceptionTypes"), AbstractType)

class InterruptibleActivityRegion(ActivityGroup):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "InterruptibleActivityRegion"))
        elif isinstance(java_object, InterruptibleActivityRegion):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "InterruptibleActivityRegion")
    def get_interrupting_edges(self):
        return create_e_list(self.e_get("interruptingEdges"), ActivityEdge)

class ControlFlow(ActivityEdge):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ControlFlow"))
        elif isinstance(java_object, ControlFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ControlFlow")

class StructuredActivityNode(ActivityGroup, AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "StructuredActivityNode"))
        elif isinstance(java_object, StructuredActivityNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "StructuredActivityNode")

class AcceptEventAction(AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AcceptEventAction"))
        elif isinstance(java_object, AcceptEventAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "AcceptEventAction")
    def get_is_unmarshall(self):
        return self.e_get("isUnmarshall")
    def set_is_unmarshall(self, value):
        self.e_set("isUnmarshall", value)
    def get_result(self):
        return create_e_list(self.e_get("result"), OutputPin)

class SendSignalAction(InvocationAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "SendSignalAction"))
        elif isinstance(java_object, SendSignalAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "SendSignalAction")
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())
    def get_signal(self):
        value =  self.e_get("signal")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_signal(self, value):
        return self.e_set("signal", value.get_java_object())

class ValuePin(InputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ValuePin"))
        elif isinstance(java_object, ValuePin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/activity/1.4.0", "ValuePin")
    def get_value(self):
        value =  self.e_get("value")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.e_set("value", value.get_java_object())

class ReAbstractElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReAbstractElement"))
        elif isinstance(java_object, ReAbstractElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "ReAbstractElement")
    def get_id(self):
        return self.e_get("id")
    def set_id(self, value):
        self.e_set("id", value)

class ReNamedElement(ReAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReNamedElement"))
        elif isinstance(java_object, ReNamedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "ReNamedElement")
    def get_name(self):
        return self.e_get("name")
    def set_name(self, value):
        self.e_set("name", value)

class ReDescriptionElement(ReNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReDescriptionElement"))
        elif isinstance(java_object, ReDescriptionElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "ReDescriptionElement")
    def get_description(self):
        return self.e_get("description")
    def set_description(self, value):
        self.e_set("description", value)

class ReElementContainer(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReElementContainer"))
        elif isinstance(java_object, ReElementContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "ReElementContainer")
    def get_owned_elements(self):
        return create_e_list(self.e_get("ownedElements"), CatalogElement)

class CatalogElementPkg(ReNamedElement, ReElementContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementPkg"))
        elif isinstance(java_object, CatalogElementPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementPkg")
    def get_owned_element_pkgs(self):
        return create_e_list(self.e_get("ownedElementPkgs"), CatalogElementPkg)

class RecCatalog(CatalogElementPkg, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "RecCatalog"))
        elif isinstance(java_object, RecCatalog):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "RecCatalog")
    def get_owned_compliancy_definition_pkg(self):
        value =  self.e_get("ownedCompliancyDefinitionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_compliancy_definition_pkg(self, value):
        return self.e_set("ownedCompliancyDefinitionPkg", value.get_java_object())

class GroupingElementPkg(CatalogElementPkg, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "GroupingElementPkg"))
        elif isinstance(java_object, GroupingElementPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "GroupingElementPkg")

class CatalogElementLink(ReAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementLink"))
        elif isinstance(java_object, CatalogElementLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementLink")
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())
    def get_origin(self):
        value =  self.e_get("origin")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_origin(self, value):
        return self.e_set("origin", value.get_java_object())
    def get_unsynchronized_features(self):
        return self.e_get("unsynchronizedFeatures")
    def set_unsynchronized_features(self, value):
        self.e_set("unsynchronizedFeatures", value)
    def get_suffixed(self):
        return self.e_get("suffixed")
    def set_suffixed(self, value):
        self.e_set("suffixed", value)
    def get_referenced_element(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.CatalogElementLinkReferencedElement", self)

class CatalogElement(ReDescriptionElement, ReElementContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElement"))
        elif isinstance(java_object, CatalogElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElement")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_author(self):
        return self.e_get("author")
    def set_author(self, value):
        self.e_set("author", value)
    def get_environment(self):
        return self.e_get("environment")
    def set_environment(self, value):
        self.e_set("environment", value)
    def get_suffix(self):
        return self.e_get("suffix")
    def set_suffix(self, value):
        self.e_set("suffix", value)
    def get_purpose(self):
        return self.e_get("purpose")
    def set_purpose(self, value):
        self.e_set("purpose", value)
    def get_read_only(self):
        return self.e_get("readOnly")
    def set_read_only(self, value):
        self.e_set("readOnly", value)
    def get_version(self):
        return self.e_get("version")
    def set_version(self, value):
        self.e_set("version", value)
    def get_tags(self):
        return self.e_get("tags")
    def set_tags(self, value):
        self.e_set("tags", value)
    def get_origin(self):
        value =  self.e_get("origin")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_origin(self, value):
        return self.e_set("origin", value.get_java_object())
    def get_current_compliancy(self):
        value =  self.e_get("currentCompliancy")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_current_compliancy(self, value):
        return self.e_set("currentCompliancy", value.get_java_object())
    def get_default_replica_compliancy(self):
        value =  self.e_get("defaultReplicaCompliancy")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_default_replica_compliancy(self, value):
        return self.e_set("defaultReplicaCompliancy", value.get_java_object())
    def get_owned_links(self):
        return create_e_list(self.e_get("ownedLinks"), CatalogElementLink)
    def get_referenced_elements(self):
        return create_e_list(self.e_get("referencedElements"), EObject)
    def get_replicated_elements(self):
        return create_e_list(self.e_get("replicatedElements"), CatalogElement)
    def get_related_elements(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.CatalogElementRelatedSemanticElements", self)
    def get_related_replicable_elements(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.CatalogElementRelatedReplicas", self)
    def get_r_p_l(self):
        return capella_query("org.polarsys.capella.common.re.ui.queries.CatalogElementReverseOrigin", self)

class CompliancyDefinitionPkg(ReNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CompliancyDefinitionPkg"))
        elif isinstance(java_object, CompliancyDefinitionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "CompliancyDefinitionPkg")
    def get_owned_definitions(self):
        return create_e_list(self.e_get("ownedDefinitions"), CompliancyDefinition)

class CompliancyDefinition(ReDescriptionElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CompliancyDefinition"))
        elif isinstance(java_object, CompliancyDefinition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/re/1.4.0", "CompliancyDefinition")

class SequenceMessage(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessage"))
        elif isinstance(java_object, SequenceMessage):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessage")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_exchange_context(self):
        value =  self.e_get("exchangeContext")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_context(self, value):
        return self.e_set("exchangeContext", value.get_java_object())
    def get_sending_end(self):
        value =  self.e_get("sendingEnd")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_sending_end(self, value):
        return self.e_set("sendingEnd", value.get_java_object())
    def get_receiving_end(self):
        value =  self.e_get("receivingEnd")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_receiving_end(self, value):
        return self.e_set("receivingEnd", value.get_java_object())
    def get_invoked_operation(self):
        value =  self.e_get("invokedOperation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_exchanged_items(self):
        return create_e_list(self.e_get("exchangedItems"), ExchangeItem)
    def get_sending_part(self):
        value =  self.e_get("sendingPart")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_receiving_part(self):
        value =  self.e_get("receivingPart")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_sending_function(self):
        value =  self.e_get("sendingFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_receiving_function(self):
        value =  self.e_get("receivingFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_sequence_message_valuations(self):
        return create_e_list(self.e_get("ownedSequenceMessageValuations"), SequenceMessageValuation)
    def get_parent_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_parentScenario", self)
    def get_invoked_exchange_item_allocation(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageInvokedExchangeItemAllocation", self)
    def get_refined_sequence_message(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_refiningSequenceMessage", self)
    def get_invoked_component_exchange(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageInvokedComponentExchange", self)
    def get_invoked_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageInvokedCommunicationMean", self)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageExchangeItems", self)
    def get_invoked_interaction(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageInvokedInteraction", self)
    def get_invoked_functional_exchange(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_AllocatedFunctionalExchange", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessageFunctionTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessagePartSource", self)
    def get_refining_sequence_message(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_refinedSequenceMessage", self)

class Scenario(Namespace, AbstractBehavior):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Scenario"))
        elif isinstance(java_object, Scenario):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "Scenario")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_merged(self):
        return self.e_get("merged")
    def set_merged(self, value):
        self.e_set("merged", value)
    def get_pre_condition(self):
        value =  self.e_get("preCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.e_set("preCondition", value.get_java_object())
    def get_post_condition(self):
        value =  self.e_get("postCondition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.e_set("postCondition", value.get_java_object())
    def get_owned_instance_roles(self):
        return create_e_list(self.e_get("ownedInstanceRoles"), InstanceRole)
    def get_owned_messages(self):
        return create_e_list(self.e_get("ownedMessages"), SequenceMessage)
    def get_owned_interaction_fragments(self):
        return create_e_list(self.e_get("ownedInteractionFragments"), InteractionFragment)
    def get_owned_time_lapses(self):
        return create_e_list(self.e_get("ownedTimeLapses"), TimeLapse)
    def get_owned_events(self):
        return create_e_list(self.e_get("ownedEvents"), Event)
    def get_owned_formal_gates(self):
        return create_e_list(self.e_get("ownedFormalGates"), Gate)
    def get_owned_scenario_realization(self):
        return create_e_list(self.e_get("ownedScenarioRealization"), ScenarioRealization)
    def get_owned_constraint_durations(self):
        return create_e_list(self.e_get("ownedConstraintDurations"), ConstraintDuration)
    def get_contained_functions(self):
        return create_e_list(self.e_get("containedFunctions"), AbstractFunction)
    def get_contained_parts(self):
        return create_e_list(self.e_get("containedParts"), Part)
    def get_referenced_scenarios(self):
        return create_e_list(self.e_get("referencedScenarios"), Scenario)
    def get_realized_scenarios(self):
        return create_e_list(self.e_get("realizedScenarios"), Scenario)
    def get_realizing_scenarios(self):
        return create_e_list(self.e_get("realizingScenarios"), Scenario)
    def get_parent(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ItemQuery_Scenario_getAbstractCapabilityContainer", self)
    def get_referenced_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ItemQuery_Scenario_getReferencedScenarios", self)
    def get_refined_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Scenario_refiningScenarios", self)
    def get_refining_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Scenario_refinedScenarios", self)

class InteractionFragment(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionFragment"))
        elif isinstance(java_object, InteractionFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionFragment")
    def get_covered_instance_roles(self):
        return create_e_list(self.e_get("coveredInstanceRoles"), InstanceRole)

class AbstractEnd(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractEnd"))
        elif isinstance(java_object, AbstractEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractEnd")
    def get_event(self):
        value =  self.e_get("event")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_event(self, value):
        return self.e_set("event", value.get_java_object())
    def get_covered(self):
        value =  self.e_get("covered")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class MessageEnd(AbstractEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "MessageEnd"))
        elif isinstance(java_object, MessageEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "MessageEnd")
    def get_message(self):
        value =  self.e_get("message")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class TimeLapse(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "TimeLapse"))
        elif isinstance(java_object, TimeLapse):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "TimeLapse")
    def get_start(self):
        value =  self.e_get("start")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_start(self, value):
        return self.e_set("start", value.get_java_object())
    def get_finish(self):
        value =  self.e_get("finish")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_finish(self, value):
        return self.e_set("finish", value.get_java_object())

class Execution(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Execution"))
        elif isinstance(java_object, Execution):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "Execution")
    def get_covered(self):
        value =  self.e_get("covered")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ExecutionEnd(AbstractEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEnd"))
        elif isinstance(java_object, ExecutionEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEnd")
    def get_execution(self):
        value =  self.e_get("execution")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class Event(NamedElement, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Event"))
        elif isinstance(java_object, Event):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "Event")

class CreationEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "CreationEvent"))
        elif isinstance(java_object, CreationEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "CreationEvent")

class DestructionEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "DestructionEvent"))
        elif isinstance(java_object, DestructionEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "DestructionEvent")

class ExecutionEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEvent"))
        elif isinstance(java_object, ExecutionEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEvent")

class InstanceRole(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InstanceRole"))
        elif isinstance(java_object, InstanceRole):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "InstanceRole")
    def get_abstract_ends(self):
        return create_e_list(self.e_get("abstractEnds"), AbstractEnd)
    def get_represented_instance(self):
        value =  self.e_get("representedInstance")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_represented_instance(self, value):
        return self.e_set("representedInstance", value.get_java_object())
    def get_parent_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InstanceRole_parentScenario", self)

class EventReceiptOperation(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventReceiptOperation"))
        elif isinstance(java_object, EventReceiptOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventReceiptOperation")
    def get_operation(self):
        value =  self.e_get("operation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_operation(self, value):
        return self.e_set("operation", value.get_java_object())

class EventSentOperation(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventSentOperation"))
        elif isinstance(java_object, EventSentOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventSentOperation")
    def get_operation(self):
        value =  self.e_get("operation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_operation(self, value):
        return self.e_set("operation", value.get_java_object())

class MergeLink(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "MergeLink"))
        elif isinstance(java_object, MergeLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "MergeLink")

class RefinementLink(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "RefinementLink"))
        elif isinstance(java_object, RefinementLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "RefinementLink")

class AbstractCapabilityRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityRealization"))
        elif isinstance(java_object, AbstractCapabilityRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityRealization")
    def get_realized_capability(self):
        value =  self.e_get("realizedCapability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_capability(self):
        value =  self.e_get("realizingCapability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class AbstractCapabilityExtend(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityExtend"))
        elif isinstance(java_object, AbstractCapabilityExtend):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityExtend")
    def get_extended(self):
        value =  self.e_get("extended")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_extended(self, value):
        return self.e_set("extended", value.get_java_object())
    def get_extension(self):
        value =  self.e_get("extension")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_extension_location(self):
        value =  self.e_get("extensionLocation")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_extension_location(self, value):
        return self.e_set("extensionLocation", value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityExtendTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityExtendSource", self)

class AbstractCapabilityExtensionPoint(NamedRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityExtensionPoint"))
        elif isinstance(java_object, AbstractCapabilityExtensionPoint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityExtensionPoint")
    def get_abstract_capability(self):
        value =  self.e_get("abstractCapability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_extend_links(self):
        return create_e_list(self.e_get("extendLinks"), AbstractCapabilityExtend)

class AbstractCapabilityGeneralization(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityGeneralization"))
        elif isinstance(java_object, AbstractCapabilityGeneralization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityGeneralization")
    def get_super(self):
        value =  self.e_get("super")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_super(self, value):
        return self.e_set("super", value.get_java_object())
    def get_sub(self):
        value =  self.e_get("sub")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityGeneralizationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityGeneralizationSource", self)

class AbstractCapabilityInclude(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityInclude"))
        elif isinstance(java_object, AbstractCapabilityInclude):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityInclude")
    def get_included(self):
        value =  self.e_get("included")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_included(self, value):
        return self.e_set("included", value.get_java_object())
    def get_inclusion(self):
        value =  self.e_get("inclusion")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityIncludeTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsAbstractCapabilityIncludeSource", self)

class InteractionState(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionState"))
        elif isinstance(java_object, InteractionState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionState")
    def get_related_abstract_state(self):
        value =  self.e_get("relatedAbstractState")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_related_abstract_state(self, value):
        return self.e_set("relatedAbstractState", value.get_java_object())
    def get_related_abstract_function(self):
        value =  self.e_get("relatedAbstractFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_related_abstract_function(self, value):
        return self.e_set("relatedAbstractFunction", value.get_java_object())
    def get_covered(self):
        value =  self.e_get("covered")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class AbstractFragment(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFragment"))
        elif isinstance(java_object, AbstractFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFragment")
    def get_owned_gates(self):
        return create_e_list(self.e_get("ownedGates"), Gate)

class InteractionUse(AbstractFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionUse"))
        elif isinstance(java_object, InteractionUse):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionUse")
    def get_referenced_scenario(self):
        value =  self.e_get("referencedScenario")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_referenced_scenario(self, value):
        return self.e_set("referencedScenario", value.get_java_object())
    def get_actual_gates(self):
        return create_e_list(self.e_get("actualGates"), Gate)
    def get_referencing_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ItemQuery_Scenario_getReferencingScenarios", self)

class CombinedFragment(AbstractFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "CombinedFragment"))
        elif isinstance(java_object, CombinedFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "CombinedFragment")
    def get_operator(self):
        return self.e_get("operator").getName()
    def set_operator(self, value):
        self.e_set("operator", value)
    def get_referenced_operands(self):
        return create_e_list(self.e_get("referencedOperands"), InteractionOperand)
    def get_expression_gates(self):
        return create_e_list(self.e_get("expressionGates"), Gate)

class Gate(MessageEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Gate"))
        elif isinstance(java_object, Gate):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "Gate")

class InteractionOperand(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionOperand"))
        elif isinstance(java_object, InteractionOperand):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionOperand")
    def get_referenced_interaction_fragments(self):
        return create_e_list(self.e_get("referencedInteractionFragments"), InteractionFragment)
    def get_guard(self):
        value =  self.e_get("guard")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.e_set("guard", value.get_java_object())

class FragmentEnd(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "FragmentEnd"))
        elif isinstance(java_object, FragmentEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "FragmentEnd")
    def get_abstract_fragment(self):
        value =  self.e_get("abstractFragment")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class FunctionalChainAbstractCapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "FunctionalChainAbstractCapabilityInvolvement"))
        elif isinstance(java_object, FunctionalChainAbstractCapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "FunctionalChainAbstractCapabilityInvolvement")
    def get_capability(self):
        value =  self.e_get("capability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_functional_chain(self):
        value =  self.e_get("functionalChain")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class AbstractFunctionAbstractCapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFunctionAbstractCapabilityInvolvement"))
        elif isinstance(java_object, AbstractFunctionAbstractCapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFunctionAbstractCapabilityInvolvement")
    def get_capability(self):
        value =  self.e_get("capability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_function(self):
        value =  self.e_get("function")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ScenarioRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ScenarioRealization"))
        elif isinstance(java_object, ScenarioRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "ScenarioRealization")
    def get_realized_scenario(self):
        value =  self.e_get("realizedScenario")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_scenario(self):
        value =  self.e_get("realizingScenario")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class StateFragment(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "StateFragment"))
        elif isinstance(java_object, StateFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "StateFragment")
    def get_related_abstract_state(self):
        value =  self.e_get("relatedAbstractState")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_related_abstract_state(self, value):
        return self.e_set("relatedAbstractState", value.get_java_object())
    def get_related_abstract_function(self):
        value =  self.e_get("relatedAbstractFunction")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_related_abstract_function(self, value):
        return self.e_set("relatedAbstractFunction", value.get_java_object())
    def get_related_function(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateFragmentRelatedFunctions", self)
    def get_related_state(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateFragmentRelatedStates", self)

class ArmTimerEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ArmTimerEvent"))
        elif isinstance(java_object, ArmTimerEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "ArmTimerEvent")

class CancelTimerEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "CancelTimerEvent"))
        elif isinstance(java_object, CancelTimerEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "CancelTimerEvent")

class ConstraintDuration(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ConstraintDuration"))
        elif isinstance(java_object, ConstraintDuration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "ConstraintDuration")
    def get_duration(self):
        return self.e_get("duration")
    def set_duration(self, value):
        self.e_set("duration", value)
    def get_start(self):
        value =  self.e_get("start")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_start(self, value):
        return self.e_set("start", value.get_java_object())
    def get_finish(self):
        value =  self.e_get("finish")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_finish(self, value):
        return self.e_set("finish", value.get_java_object())

class SequenceMessageValuation(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessageValuation"))
        elif isinstance(java_object, SequenceMessageValuation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessageValuation")
    def get_exchange_item_element(self):
        value =  self.e_get("exchangeItemElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_item_element(self, value):
        return self.e_set("exchangeItemElement", value.get_java_object())
    def get_value(self):
        value =  self.e_get("value")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.e_set("value", value.get_java_object())

class LibraryAbstractElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryAbstractElement"))
        elif isinstance(java_object, LibraryAbstractElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryAbstractElement")
    def get_id(self):
        return self.e_get("id")
    def set_id(self, value):
        self.e_set("id", value)

class ModelInformation(LibraryAbstractElement, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelInformation"))
        elif isinstance(java_object, ModelInformation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelInformation")
    def get_owned_references(self):
        return create_e_list(self.e_get("ownedReferences"), LibraryReference)
    def get_version(self):
        value =  self.e_get("version")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_version(self, value):
        return self.e_set("version", value.get_java_object())

class LibraryReference(LibraryAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryReference"))
        elif isinstance(java_object, LibraryReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryReference")
    def get_library(self):
        value =  self.e_get("library")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_library(self, value):
        return self.e_set("library", value.get_java_object())
    def get_access_policy(self):
        return self.e_get("accessPolicy").getName()
    def set_access_policy(self, value):
        self.e_set("accessPolicy", value)
    def get_version(self):
        value =  self.e_get("version")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_version(self, value):
        return self.e_set("version", value.get_java_object())

class ModelVersion(LibraryAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelVersion"))
        elif isinstance(java_object, ModelVersion):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelVersion")
    def get_major_version_number(self):
        return self.e_get("majorVersionNumber")
    def set_major_version_number(self, value):
        self.e_set("majorVersionNumber", value)
    def get_minor_version_number(self):
        return self.e_get("minorVersionNumber")
    def set_minor_version_number(self, value):
        self.e_set("minorVersionNumber", value)
    def get_last_modified_file_stamp(self):
        return self.e_get("lastModifiedFileStamp")
    def set_last_modified_file_stamp(self, value):
        self.e_set("lastModifiedFileStamp", value)

class LogicalArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecturePkg"))
        elif isinstance(java_object, LogicalArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecturePkg")
    def get_owned_logical_architectures(self):
        return create_e_list(self.e_get("ownedLogicalArchitectures"), LogicalArchitecture)

class LogicalArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecture"))
        elif isinstance(java_object, LogicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecture")
    def get_owned_logical_component_pkg(self):
        value =  self.e_get("ownedLogicalComponentPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_logical_component_pkg(self, value):
        return self.e_set("ownedLogicalComponentPkg", value.get_java_object())
    def get_contained_capability_realization_pkg(self):
        value =  self.e_get("containedCapabilityRealizationPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_contained_logical_function_pkg(self):
        value =  self.e_get("containedLogicalFunctionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_system_analysis_realizations(self):
        return create_e_list(self.e_get("ownedSystemAnalysisRealizations"), SystemAnalysisRealization)
    def get_allocated_system_analysis_realizations(self):
        return create_e_list(self.e_get("allocatedSystemAnalysisRealizations"), SystemAnalysisRealization)
    def get_allocated_system_analyses(self):
        return create_e_list(self.e_get("allocatedSystemAnalyses"), SystemAnalysis)
    def get_allocating_physical_architectures(self):
        return create_e_list(self.e_get("allocatingPhysicalArchitectures"), PhysicalArchitecture)

class LogicalFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalFunction"))
        elif isinstance(java_object, LogicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalFunction")
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.e_get("ownedLogicalFunctionPkgs"), LogicalFunctionPkg)
    def get_allocating_logical_components(self):
        return create_e_list(self.e_get("allocatingLogicalComponents"), LogicalComponent)
    def get_realized_system_functions(self):
        return create_e_list(self.e_get("realizedSystemFunctions"), SystemFunction)
    def get_realizing_physical_functions(self):
        return create_e_list(self.e_get("realizingPhysicalFunctions"), PhysicalFunction)
    def get_contained_logical_functions(self):
        return create_e_list(self.e_get("containedLogicalFunctions"), LogicalFunction)
    def get_children_logical_functions(self):
        return create_e_list(self.e_get("childrenLogicalFunctions"), LogicalFunction)
    def get_owned_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_ownedFunctionalChains", self)
    def get_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_outgoingInteraction", self)
    def get_out_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_outFlowPorts", self)
    def get_internal_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalOutGoingDataflows", self)
    def get_allocating_logical_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingActor", self)
    def get_internal_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalInComingDataflows", self)
    def get_in_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_inFlowPorts", self)
    def get_allocating_logical_component(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingComponent", self)
    def get_involving_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.LogicalAndPhysicalFunctionInvolvingCapabilityRealization", self)
    def get_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_incomingInteraction", self)

class LogicalFunctionPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalFunctionPkg"))
        elif isinstance(java_object, LogicalFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalFunctionPkg")
    def get_owned_logical_functions(self):
        return create_e_list(self.e_get("ownedLogicalFunctions"), LogicalFunction)
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.e_get("ownedLogicalFunctionPkgs"), LogicalFunctionPkg)

class LogicalComponent(Component, CapabilityRealizationInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponent"))
        elif isinstance(java_object, LogicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponent")
    def get_owned_logical_components(self):
        return create_e_list(self.e_get("ownedLogicalComponents"), LogicalComponent)
    def get_owned_logical_architectures(self):
        return create_e_list(self.e_get("ownedLogicalArchitectures"), LogicalArchitecture)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.e_get("ownedLogicalComponentPkgs"), LogicalComponentPkg)
    def get_sub_logical_components(self):
        return create_e_list(self.e_get("subLogicalComponents"), LogicalComponent)
    def get_allocated_logical_functions(self):
        return create_e_list(self.e_get("allocatedLogicalFunctions"), LogicalFunction)
    def get_realized_system_components(self):
        return create_e_list(self.e_get("realizedSystemComponents"), SystemComponent)
    def get_realizing_physical_components(self):
        return create_e_list(self.e_get("realizingPhysicalComponents"), PhysicalComponent)

class LogicalComponentPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponentPkg"))
        elif isinstance(java_object, LogicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponentPkg")
    def get_owned_logical_components(self):
        return create_e_list(self.e_get("ownedLogicalComponents"), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.e_get("ownedLogicalComponentPkgs"), LogicalComponentPkg)

class CapabilityRealization(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "CapabilityRealization"))
        elif isinstance(java_object, CapabilityRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "CapabilityRealization")
    def get_owned_capability_realization_involvements(self):
        return create_e_list(self.e_get("ownedCapabilityRealizationInvolvements"), CapabilityRealizationInvolvement)
    def get_involved_components(self):
        return create_e_list(self.e_get("involvedComponents"), CapabilityRealizationInvolvedElement)
    def get_realized_capabilities(self):
        return create_e_list(self.e_get("realizedCapabilities"), Capability)
    def get_realized_capability_realizations(self):
        return create_e_list(self.e_get("realizedCapabilityRealizations"), CapabilityRealization)
    def get_realizing_capability_realizations(self):
        return create_e_list(self.e_get("realizingCapabilityRealizations"), CapabilityRealization)
    def get_owned_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityOwnedFunctionalChains", self)
    def get_involved_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityInvolvedFunctionalChains", self)
    def get_involved_logical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.LAAbstractCapabilityInvolvedFunctions", self)
    def get_involved_physical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PAAbstractCapabilityInvolvedFunctions", self)

class CapabilityRealizationPkg(AbstractCapabilityPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "CapabilityRealizationPkg"))
        elif isinstance(java_object, CapabilityRealizationPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "CapabilityRealizationPkg")
    def get_owned_capability_realizations(self):
        return create_e_list(self.e_get("ownedCapabilityRealizations"), CapabilityRealization)
    def get_owned_capability_realization_pkgs(self):
        return create_e_list(self.e_get("ownedCapabilityRealizationPkgs"), CapabilityRealizationPkg)

class SystemAnalysisRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "SystemAnalysisRealization"))
        elif isinstance(java_object, SystemAnalysisRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "SystemAnalysisRealization")

class InterfaceAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocation"))
        elif isinstance(java_object, InterfaceAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocation")
    def get_allocated_interface(self):
        value =  self.e_get("allocatedInterface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_allocating_interface_allocator(self):
        value =  self.e_get("allocatingInterfaceAllocator")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ContextInterfaceRealization(InterfaceAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "ContextInterfaceRealization"))
        elif isinstance(java_object, ContextInterfaceRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/la/1.4.0", "ContextInterfaceRealization")

class PhysicalArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecturePkg"))
        elif isinstance(java_object, PhysicalArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecturePkg")
    def get_owned_physical_architecture_pkgs(self):
        return create_e_list(self.e_get("ownedPhysicalArchitecturePkgs"), PhysicalArchitecturePkg)
    def get_owned_physical_architectures(self):
        return create_e_list(self.e_get("ownedPhysicalArchitectures"), PhysicalArchitecture)

class PhysicalArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecture"))
        elif isinstance(java_object, PhysicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecture")
    def get_owned_physical_component_pkg(self):
        value =  self.e_get("ownedPhysicalComponentPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_physical_component_pkg(self, value):
        return self.e_set("ownedPhysicalComponentPkg", value.get_java_object())
    def get_contained_capability_realization_pkg(self):
        value =  self.e_get("containedCapabilityRealizationPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_contained_physical_function_pkg(self):
        value =  self.e_get("containedPhysicalFunctionPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_owned_deployments(self):
        return create_e_list(self.e_get("ownedDeployments"), AbstractDeploymentLink)
    def get_owned_logical_architecture_realizations(self):
        return create_e_list(self.e_get("ownedLogicalArchitectureRealizations"), LogicalArchitectureRealization)
    def get_allocated_logical_architecture_realizations(self):
        return create_e_list(self.e_get("allocatedLogicalArchitectureRealizations"), LogicalArchitectureRealization)
    def get_allocated_logical_architectures(self):
        return create_e_list(self.e_get("allocatedLogicalArchitectures"), LogicalArchitecture)
    def get_allocating_epbs_architectures(self):
        return create_e_list(self.e_get("allocatingEpbsArchitectures"), EPBSArchitecture)

class PhysicalFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalFunction"))
        elif isinstance(java_object, PhysicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalFunction")
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.e_get("ownedPhysicalFunctionPkgs"), PhysicalFunctionPkg)
    def get_allocating_physical_components(self):
        return create_e_list(self.e_get("allocatingPhysicalComponents"), PhysicalComponent)
    def get_realized_logical_functions(self):
        return create_e_list(self.e_get("realizedLogicalFunctions"), LogicalFunction)
    def get_contained_physical_functions(self):
        return create_e_list(self.e_get("containedPhysicalFunctions"), PhysicalFunction)
    def get_children_physical_functions(self):
        return create_e_list(self.e_get("childrenPhysicalFunctions"), PhysicalFunction)
    def get_owned_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_ownedFunctionalChains", self)
    def get_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_outgoingInteraction", self)
    def get_out_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_outFlowPorts", self)
    def get_internal_outgoing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalOutGoingDataflows", self)
    def get_involving_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.LogicalAndPhysicalFunctionInvolvingCapabilityRealization", self)
    def get_allocating_physical_component(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingComponent", self)
    def get_internal_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionInternalInComingDataflows", self)
    def get_incoming_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_incomingInteraction", self)
    def get_allocating_physical_actor(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingActor", self)
    def get_in_flow_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_inFlowPorts", self)

class PhysicalFunctionPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalFunctionPkg"))
        elif isinstance(java_object, PhysicalFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalFunctionPkg")
    def get_owned_physical_functions(self):
        return create_e_list(self.e_get("ownedPhysicalFunctions"), PhysicalFunction)
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.e_get("ownedPhysicalFunctionPkgs"), PhysicalFunctionPkg)

class AbstractPhysicalArtifact(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalArtifact"))
        elif isinstance(java_object, AbstractPhysicalArtifact):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalArtifact")
    def get_allocator_configuration_items(self):
        return create_e_list(self.e_get("allocatorConfigurationItems"), ConfigurationItem)

class DeployableElement(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "DeployableElement"))
        elif isinstance(java_object, DeployableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "DeployableElement")
    def get_deploying_links(self):
        return create_e_list(self.e_get("deployingLinks"), AbstractDeploymentLink)

class DeploymentTarget(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "DeploymentTarget"))
        elif isinstance(java_object, DeploymentTarget):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "DeploymentTarget")
    def get_deployment_links(self):
        return create_e_list(self.e_get("deploymentLinks"), AbstractDeploymentLink)

class PhysicalComponent(AbstractPhysicalArtifact, Component, CapabilityRealizationInvolvedElement, DeployableElement, DeploymentTarget):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponent"))
        elif isinstance(java_object, PhysicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponent")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_nature(self):
        return self.e_get("nature").getName()
    def set_nature(self, value):
        self.e_set("nature", value)
    def get_owned_deployment_links(self):
        return create_e_list(self.e_get("ownedDeploymentLinks"), AbstractDeploymentLink)
    def get_owned_physical_components(self):
        return create_e_list(self.e_get("ownedPhysicalComponents"), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.e_get("ownedPhysicalComponentPkgs"), PhysicalComponentPkg)
    def get_logical_interface_realizations(self):
        return create_e_list(self.e_get("logicalInterfaceRealizations"), LogicalInterfaceRealization)
    def get_sub_physical_components(self):
        return create_e_list(self.e_get("subPhysicalComponents"), PhysicalComponent)
    def get_realized_logical_components(self):
        return create_e_list(self.e_get("realizedLogicalComponents"), LogicalComponent)
    def get_allocated_physical_functions(self):
        return create_e_list(self.e_get("allocatedPhysicalFunctions"), PhysicalFunction)
    def get_deployed_physical_components(self):
        return create_e_list(self.e_get("deployedPhysicalComponents"), PhysicalComponent)
    def get_deploying_physical_components(self):
        return create_e_list(self.e_get("deployingPhysicalComponents"), PhysicalComponent)
    def get_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_IncomingPhysicalLinks", self)
    def get_internal_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_InternalPhysicalLinks", self)
    def get_realized_logical_component(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizedComponents", self)
    def get_realizing_configuration_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizingComponents", self)

class PhysicalComponentPkg(ComponentPkg, AssociationPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponentPkg"))
        elif isinstance(java_object, PhysicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponentPkg")
    def get_owned_physical_components(self):
        return create_e_list(self.e_get("ownedPhysicalComponents"), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.e_get("ownedPhysicalComponentPkgs"), PhysicalComponentPkg)
    def get_owned_key_parts(self):
        return create_e_list(self.e_get("ownedKeyParts"), KeyPart)
    def get_owned_deployments(self):
        return create_e_list(self.e_get("ownedDeployments"), AbstractDeploymentLink)

class PhysicalNode(PhysicalComponent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalNode"))
        elif isinstance(java_object, PhysicalNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalNode")
    def get_sub_physical_nodes(self):
        return create_e_list(self.e_get("subPhysicalNodes"), PhysicalNode)

class LogicalArchitectureRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalArchitectureRealization"))
        elif isinstance(java_object, LogicalArchitectureRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalArchitectureRealization")

class LogicalInterfaceRealization(InterfaceAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalInterfaceRealization"))
        elif isinstance(java_object, LogicalInterfaceRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalInterfaceRealization")

class AbstractPhysicalInstance(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "AbstractPhysicalInstance"))
        elif isinstance(java_object, AbstractPhysicalInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "AbstractPhysicalInstance")

class ComponentInstance(AbstractPhysicalInstance, DeployableElement, DeploymentTarget):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ComponentInstance"))
        elif isinstance(java_object, ComponentInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ComponentInstance")
    def get_port_instances(self):
        return create_e_list(self.e_get("portInstances"), PortInstance)
    def get_owned_abstract_physical_instances(self):
        return create_e_list(self.e_get("ownedAbstractPhysicalInstances"), AbstractPhysicalInstance)
    def get_owned_instance_deployment_links(self):
        return create_e_list(self.e_get("ownedInstanceDeploymentLinks"), InstanceDeploymentLink)
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())

class ConnectionInstance(AbstractPhysicalInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ConnectionInstance"))
        elif isinstance(java_object, ConnectionInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ConnectionInstance")
    def get_connection_ends(self):
        return create_e_list(self.e_get("connectionEnds"), PortInstance)
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())

class DeploymentAspect(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentAspect"))
        elif isinstance(java_object, DeploymentAspect):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentAspect")
    def get_owned_configurations(self):
        return create_e_list(self.e_get("ownedConfigurations"), DeploymentConfiguration)
    def get_owned_deployment_aspects(self):
        return create_e_list(self.e_get("ownedDeploymentAspects"), DeploymentAspect)

class DeploymentConfiguration(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentConfiguration"))
        elif isinstance(java_object, DeploymentConfiguration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentConfiguration")
    def get_owned_deployment_links(self):
        return create_e_list(self.e_get("ownedDeploymentLinks"), AbstractDeploymentLink)
    def get_owned_physical_instances(self):
        return create_e_list(self.e_get("ownedPhysicalInstances"), AbstractPhysicalInstance)

class AbstractDeploymentLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractDeploymentLink"))
        elif isinstance(java_object, AbstractDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractDeploymentLink")
    def get_deployed_element(self):
        value =  self.e_get("deployedElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_deployed_element(self, value):
        return self.e_set("deployedElement", value.get_java_object())
    def get_location(self):
        value =  self.e_get("location")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_location(self, value):
        return self.e_set("location", value.get_java_object())

class InstanceDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "InstanceDeploymentLink"))
        elif isinstance(java_object, InstanceDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "InstanceDeploymentLink")

class PartDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PartDeploymentLink"))
        elif isinstance(java_object, PartDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PartDeploymentLink")

class PortInstance(AbstractPhysicalInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PortInstance"))
        elif isinstance(java_object, PortInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PortInstance")
    def get_connections(self):
        return create_e_list(self.e_get("connections"), ConnectionInstance)
    def get_component(self):
        value =  self.e_get("component")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_type(self):
        value =  self.e_get("type")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.e_set("type", value.get_java_object())

class TypeDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "TypeDeploymentLink"))
        elif isinstance(java_object, TypeDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "TypeDeploymentLink")

class AbstractPathInvolvedElement(InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPathInvolvedElement"))
        elif isinstance(java_object, AbstractPathInvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPathInvolvedElement")

class Part(AbstractInstance, InformationsExchanger, DeployableElement, DeploymentTarget, AbstractPathInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Part"))
        elif isinstance(java_object, Part):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "Part")
    def get_provided_interfaces(self):
        return create_e_list(self.e_get("providedInterfaces"), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.e_get("requiredInterfaces"), Interface)
    def get_owned_deployment_links(self):
        return create_e_list(self.e_get("ownedDeploymentLinks"), AbstractDeploymentLink)
    def get_deployed_parts(self):
        return create_e_list(self.e_get("deployedParts"), Part)
    def get_deploying_parts(self):
        return create_e_list(self.e_get("deployingParts"), Part)
    def get_owned_abstract_type(self):
        value =  self.e_get("ownedAbstractType")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_abstract_type(self, value):
        return self.e_set("ownedAbstractType", value.get_java_object())
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Part_type", self)

class ComponentRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentRealization"))
        elif isinstance(java_object, ComponentRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentRealization")
    def get_realized_component(self):
        value =  self.e_get("realizedComponent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_component(self):
        value =  self.e_get("realizingComponent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class InterfacePkg(MessageReferencePkg, AbstractDependenciesPkg, AbstractExchangeItemPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfacePkg"))
        elif isinstance(java_object, InterfacePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfacePkg")
    def get_owned_interfaces(self):
        return create_e_list(self.e_get("ownedInterfaces"), Interface)
    def get_owned_interface_pkgs(self):
        return create_e_list(self.e_get("ownedInterfacePkgs"), InterfacePkg)

class Interface(GeneralClass, InterfaceAllocator):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Interface"))
        elif isinstance(java_object, Interface):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "Interface")
    def get_mechanism(self):
        return self.e_get("mechanism")
    def set_mechanism(self, value):
        self.e_set("mechanism", value)
    def get_structural(self):
        return self.e_get("structural")
    def set_structural(self, value):
        self.e_set("structural", value)
    def get_implementor_components(self):
        return create_e_list(self.e_get("implementorComponents"), Component)
    def get_user_components(self):
        return create_e_list(self.e_get("userComponents"), Component)
    def get_interface_implementations(self):
        return create_e_list(self.e_get("interfaceImplementations"), InterfaceImplementation)
    def get_interface_uses(self):
        return create_e_list(self.e_get("interfaceUses"), InterfaceUse)
    def get_provisioning_interface_allocations(self):
        return create_e_list(self.e_get("provisioningInterfaceAllocations"), InterfaceAllocation)
    def get_allocating_interfaces(self):
        return create_e_list(self.e_get("allocatingInterfaces"), Interface)
    def get_allocating_components(self):
        return create_e_list(self.e_get("allocatingComponents"), Component)
    def get_exchange_items(self):
        return create_e_list(self.e_get("exchangeItems"), ExchangeItem)
    def get_owned_exchange_item_allocations(self):
        return create_e_list(self.e_get("ownedExchangeItemAllocations"), ExchangeItemAllocation)
    def get_requiring_components(self):
        return create_e_list(self.e_get("requiringComponents"), Component)
    def get_requiring_component_ports(self):
        return create_e_list(self.e_get("requiringComponentPorts"), ComponentPort)
    def get_providing_components(self):
        return create_e_list(self.e_get("providingComponents"), Component)
    def get_providing_component_ports(self):
        return create_e_list(self.e_get("providingComponentPorts"), ComponentPort)
    def get_realizing_logical_interfaces(self):
        return create_e_list(self.e_get("realizingLogicalInterfaces"), Interface)
    def get_realized_context_interfaces(self):
        return create_e_list(self.e_get("realizedContextInterfaces"), Interface)
    def get_realizing_physical_interfaces(self):
        return create_e_list(self.e_get("realizingPhysicalInterfaces"), Interface)
    def get_realized_logical_interfaces(self):
        return create_e_list(self.e_get("realizedLogicalInterfaces"), Interface)
    def get_refined_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Interface_provisionedInterfaces", self)
    def get_inherited_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceInheritedExchangesItems", self)
    def get_users(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceUsers", self)
    def get_refining_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Interface_provisioningInterfaces", self)
    def get_involving_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Interface_involvingScenarios", self)
    def get_providers(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceProviders", self)
    def get_requirers(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceRequires", self)
    def get_implementors(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceImplementors", self)

class InterfaceImplementation(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceImplementation"))
        elif isinstance(java_object, InterfaceImplementation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceImplementation")
    def get_interface_implementor(self):
        value =  self.e_get("interfaceImplementor")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_implemented_interface(self):
        value =  self.e_get("implementedInterface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_implemented_interface(self, value):
        return self.e_set("implementedInterface", value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInterfaceImplementationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInterfaceImplementationSource", self)

class InterfaceUse(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceUse"))
        elif isinstance(java_object, InterfaceUse):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceUse")
    def get_interface_user(self):
        value =  self.e_get("interfaceUser")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_used_interface(self):
        value =  self.e_get("usedInterface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_used_interface(self, value):
        return self.e_set("usedInterface", value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInterfaceUseTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInterfaceUseSource", self)

class ProvidedInterfaceLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ProvidedInterfaceLink"))
        elif isinstance(java_object, ProvidedInterfaceLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ProvidedInterfaceLink")
    def get_interface(self):
        value =  self.e_get("interface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_interface(self, value):
        return self.e_set("interface", value.get_java_object())

class RequiredInterfaceLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "RequiredInterfaceLink"))
        elif isinstance(java_object, RequiredInterfaceLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "RequiredInterfaceLink")
    def get_interface(self):
        value =  self.e_get("interface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_interface(self, value):
        return self.e_set("interface", value.get_java_object())

class ExchangeItemAllocation(Relationship, AbstractEventOperation, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ExchangeItemAllocation"))
        elif isinstance(java_object, ExchangeItemAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "ExchangeItemAllocation")
    def get_send_protocol(self):
        return self.e_get("sendProtocol").getName()
    def set_send_protocol(self, value):
        self.e_set("sendProtocol", value)
    def get_receive_protocol(self):
        return self.e_get("receiveProtocol").getName()
    def set_receive_protocol(self, value):
        self.e_set("receiveProtocol", value)
    def get_allocated_item(self):
        value =  self.e_get("allocatedItem")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_allocated_item(self, value):
        return self.e_set("allocatedItem", value.get_java_object())
    def get_allocating_interface(self):
        value =  self.e_get("allocatingInterface")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_exchange_item(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemAllocationExchangeItem", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class AbstractPhysicalLinkEnd(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalLinkEnd"))
        elif isinstance(java_object, AbstractPhysicalLinkEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalLinkEnd")
    def get_involved_links(self):
        return create_e_list(self.e_get("involvedLinks"), PhysicalLink)

class AbstractPhysicalPathLink(ComponentExchangeAllocator):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalPathLink"))
        elif isinstance(java_object, AbstractPhysicalPathLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalPathLink")

class PhysicalLink(AbstractPhysicalPathLink, AbstractPhysicalArtifact, AbstractPathInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLink"))
        elif isinstance(java_object, PhysicalLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLink")
    def get_link_ends(self):
        return create_e_list(self.e_get("linkEnds"), AbstractPhysicalLinkEnd)
    def get_owned_component_exchange_functional_exchange_allocations(self):
        return create_e_list(self.e_get("ownedComponentExchangeFunctionalExchangeAllocations"), ComponentExchangeFunctionalExchangeAllocation)
    def get_owned_physical_link_ends(self):
        return create_e_list(self.e_get("ownedPhysicalLinkEnds"), PhysicalLinkEnd)
    def get_owned_physical_link_realizations(self):
        return create_e_list(self.e_get("ownedPhysicalLinkRealizations"), PhysicalLinkRealization)
    def get_categories(self):
        return create_e_list(self.e_get("categories"), PhysicalLinkCategory)
    def get_source_physical_port(self):
        value =  self.e_get("sourcePhysicalPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target_physical_port(self):
        value =  self.e_get("targetPhysicalPort")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realized_physical_links(self):
        return create_e_list(self.e_get("realizedPhysicalLinks"), PhysicalLink)
    def get_realizing_physical_links(self):
        return create_e_list(self.e_get("realizingPhysicalLinks"), PhysicalLink)
    def get_inherited_categories(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinkCategoriesForDelegations", self)
    def get_allocated_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinksRealizedConnection", self)
    def get_physical_link_ends(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinkSourceAndTarget", self)
    def get_realizing_configuration_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalArtifactsRealizingCI", self)
    def get_physical_paths(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinksInvolvedInPhysicalPaths", self)

class PhysicalLinkCategory(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkCategory"))
        elif isinstance(java_object, PhysicalLinkCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkCategory")
    def get_links(self):
        return create_e_list(self.e_get("links"), PhysicalLink)
    def get_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CategoryPhysicalLink", self)

class PhysicalLinkEnd(AbstractPhysicalLinkEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkEnd"))
        elif isinstance(java_object, PhysicalLinkEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkEnd")
    def get_port(self):
        value =  self.e_get("port")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_port(self, value):
        return self.e_set("port", value.get_java_object())
    def get_part(self):
        value =  self.e_get("part")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_part(self, value):
        return self.e_set("part", value.get_java_object())

class PhysicalLinkRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkRealization"))
        elif isinstance(java_object, PhysicalLinkRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkRealization")

class PhysicalPath(NamedElement, ComponentExchangeAllocator, AbstractPathInvolvedElement, InvolverElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPath"))
        elif isinstance(java_object, PhysicalPath):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPath")
    def get_involved_links(self):
        return create_e_list(self.e_get("involvedLinks"), AbstractPhysicalPathLink)
    def get_owned_physical_path_involvements(self):
        return create_e_list(self.e_get("ownedPhysicalPathInvolvements"), PhysicalPathInvolvement)
    def get_first_physical_path_involvements(self):
        return create_e_list(self.e_get("firstPhysicalPathInvolvements"), PhysicalPathInvolvement)
    def get_owned_physical_path_realizations(self):
        return create_e_list(self.e_get("ownedPhysicalPathRealizations"), PhysicalPathRealization)
    def get_realized_physical_paths(self):
        return create_e_list(self.e_get("realizedPhysicalPaths"), PhysicalPath)
    def get_realizing_physical_paths(self):
        return create_e_list(self.e_get("realizingPhysicalPaths"), PhysicalPath)
    def get_involved_physical_paths(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvedPhysicalPath", self)
    def get_involved_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_PhysicalLinks", self)
    def get_allocated_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_RealisedConnection", self)
    def get_physical_paths(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvingPhysicalPath", self)

class PhysicalPathInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathInvolvement"))
        elif isinstance(java_object, PhysicalPathInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathInvolvement")
    def get_next_involvements(self):
        return create_e_list(self.e_get("nextInvolvements"), PhysicalPathInvolvement)
    def get_previous_involvements(self):
        return create_e_list(self.e_get("previousInvolvements"), PhysicalPathInvolvement)
    def get_involved_element(self):
        value =  self.e_get("involvedElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_involved_component(self):
        value =  self.e_get("involvedComponent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_involved_physical_path(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvmentInvolvedPhysicalPath", self)
    def get_involved_physical_component(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvmentPhysicalComp", self)
    def get_involved_physical_link(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvmentPhysicalLink", self)

class PhysicalPathReference(PhysicalPathInvolvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathReference"))
        elif isinstance(java_object, PhysicalPathReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathReference")
    def get_referenced_physical_path(self):
        value =  self.e_get("referencedPhysicalPath")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class PhysicalPathRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathRealization"))
        elif isinstance(java_object, PhysicalPathRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathRealization")

class PhysicalPort(Port, AbstractPhysicalArtifact, InformationsExchanger, AbstractPhysicalLinkEnd, Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPort"))
        elif isinstance(java_object, PhysicalPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPort")
    def get_owned_component_port_allocations(self):
        return create_e_list(self.e_get("ownedComponentPortAllocations"), ComponentPortAllocation)
    def get_owned_physical_port_realizations(self):
        return create_e_list(self.e_get("ownedPhysicalPortRealizations"), PhysicalPortRealization)
    def get_allocated_component_ports(self):
        return create_e_list(self.e_get("allocatedComponentPorts"), ComponentPort)
    def get_realized_physical_ports(self):
        return create_e_list(self.e_get("realizedPhysicalPorts"), PhysicalPort)
    def get_realizing_physical_ports(self):
        return create_e_list(self.e_get("realizingPhysicalPorts"), PhysicalPort)
    def get_allocated_function_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPortOutgoingFunctionPorts", self)
    def get_outgoing_delegations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPortOutgoingDelgations", self)
    def get_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPortIncomingPhysicalLinks", self)
    def get_realizing_configuration_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalArtifactsRealizingCI", self)

class PhysicalPortRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPortRealization"))
        elif isinstance(java_object, PhysicalPortRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPortRealization")

class AbstractParameterSet(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameterSet"))
        elif isinstance(java_object, AbstractParameterSet):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameterSet")
    def get_owned_conditions(self):
        return create_e_list(self.e_get("ownedConditions"), AbstractConstraint)
    def get_probability(self):
        value =  self.e_get("probability")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_probability(self, value):
        return self.e_set("probability", value.get_java_object())
    def get_parameters(self):
        return create_e_list(self.e_get("parameters"), AbstractParameter)

class IState(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "IState"))
        elif isinstance(java_object, IState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/common/core/1.4.0", "IState")
    def get_referenced_states(self):
        return create_e_list(self.e_get("referencedStates"), IState)
    def get_exploited_states(self):
        return create_e_list(self.e_get("exploitedStates"), IState)
    def get_parent_stateand_mode(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.State_ParentState", self)
    def get_involved_statesand_modes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.State_InvolvedStates", self)
    def get_owned_stateand_mode(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.State_OwnedStates", self)
    def get_outgoing_transition(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateAndModeOutGoingTransition", self)
    def get_incoming_transition(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateAndModeInComingTransition", self)
    def get_involving_statesandmodes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.State_InvolvingStates", self)

class SharedPkg(ReuseableStructure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "SharedPkg"))
        elif isinstance(java_object, SharedPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "SharedPkg")
    def get_owned_data_pkg(self):
        value =  self.e_get("ownedDataPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_data_pkg(self, value):
        return self.e_set("ownedDataPkg", value.get_java_object())
    def get_owned_generic_pkg(self):
        value =  self.e_get("ownedGenericPkg")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_owned_generic_pkg(self, value):
        return self.e_set("ownedGenericPkg", value.get_java_object())

class GenericPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "GenericPkg"))
        elif isinstance(java_object, GenericPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "GenericPkg")
    def get_sub_generic_pkgs(self):
        return create_e_list(self.e_get("subGenericPkgs"), GenericPkg)
    def get_capella_elements(self):
        return create_e_list(self.e_get("capellaElements"), CapellaElement)

class GenericTrace(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "GenericTrace"))
        elif isinstance(java_object, GenericTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "GenericTrace")
    def get_key_value_pairs(self):
        return create_e_list(self.e_get("keyValuePairs"), KeyValue)
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class TransfoLink(GenericTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TransfoLink"))
        elif isinstance(java_object, TransfoLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "TransfoLink")

class JustificationLink(GenericTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "JustificationLink"))
        elif isinstance(java_object, JustificationLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "JustificationLink")

class CapabilityRealizationInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvement"))
        elif isinstance(java_object, CapabilityRealizationInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvement")
    def get_involved_capability_realization_involved_element(self):
        value =  self.e_get("involvedCapabilityRealizationInvolvedElement")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class StateMachine(CapellaElement, AbstractBehavior):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateMachine"))
        elif isinstance(java_object, StateMachine):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "StateMachine")
    def get_owned_regions(self):
        return create_e_list(self.e_get("ownedRegions"), Region)
    def get_owned_connection_points(self):
        return create_e_list(self.e_get("ownedConnectionPoints"), Pseudostate)

class Region(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "Region"))
        elif isinstance(java_object, Region):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "Region")
    def get_owned_states(self):
        return create_e_list(self.e_get("ownedStates"), AbstractState)
    def get_owned_transitions(self):
        return create_e_list(self.e_get("ownedTransitions"), StateTransition)
    def get_involved_states(self):
        return create_e_list(self.e_get("involvedStates"), AbstractState)
    def get_owned_entry(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.State_OwnedEntryExitPoints", self)

class AbstractState(NamedElement, IState):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractState"))
        elif isinstance(java_object, AbstractState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractState")
    def get_owned_abstract_state_realizations(self):
        return create_e_list(self.e_get("ownedAbstractStateRealizations"), AbstractStateRealization)
    def get_realized_abstract_states(self):
        return create_e_list(self.e_get("realizedAbstractStates"), AbstractState)
    def get_realizing_abstract_states(self):
        return create_e_list(self.e_get("realizingAbstractStates"), AbstractState)
    def get_outgoing(self):
        return create_e_list(self.e_get("outgoing"), StateTransition)
    def get_incoming(self):
        return create_e_list(self.e_get("incoming"), StateTransition)
    def get_involver_regions(self):
        return create_e_list(self.e_get("involverRegions"), Region)
    def get_realized_mode(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateRealizedMode", self)
    def get_realized_state(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateRealizedState", self)
    def get_realizing_state(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateRealizingState", self)
    def get_realizing_mode(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateRealizingMode", self)

class State(AbstractState):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "State"))
        elif isinstance(java_object, State):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "State")
    def get_owned_regions(self):
        return create_e_list(self.e_get("ownedRegions"), Region)
    def get_owned_connection_points(self):
        return create_e_list(self.e_get("ownedConnectionPoints"), Pseudostate)
    def get_available_abstract_functions(self):
        return create_e_list(self.e_get("availableAbstractFunctions"), AbstractFunction)
    def get_available_functional_chains(self):
        return create_e_list(self.e_get("availableFunctionalChains"), FunctionalChain)
    def get_available_abstract_capabilities(self):
        return create_e_list(self.e_get("availableAbstractCapabilities"), AbstractCapability)
    def get_entry(self):
        return create_e_list(self.e_get("entry"), AbstractEvent)
    def get_do_activity(self):
        return create_e_list(self.e_get("doActivity"), AbstractEvent)
    def get_exit(self):
        return create_e_list(self.e_get("exit"), AbstractEvent)
    def get_state_invariant(self):
        value =  self.e_get("stateInvariant")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_state_invariant(self, value):
        return self.e_set("stateInvariant", value.get_java_object())
    def get_active_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateAvailableElements", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class Mode(State):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "Mode"))
        elif isinstance(java_object, Mode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "Mode")

class FinalState(State):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "FinalState"))
        elif isinstance(java_object, FinalState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "FinalState")

class StateTransition(NamedElement, Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransition"))
        elif isinstance(java_object, StateTransition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransition")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
    def get_trigger_description(self):
        return self.e_get("triggerDescription")
    def set_trigger_description(self, value):
        self.e_set("triggerDescription", value)
    def get_guard(self):
        value =  self.e_get("guard")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.e_set("guard", value.get_java_object())
    def get_source(self):
        value =  self.e_get("source")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.e_set("source", value.get_java_object())
    def get_target(self):
        value =  self.e_get("target")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.e_set("target", value.get_java_object())
    def get_effect(self):
        return create_e_list(self.e_get("effect"), AbstractEvent)
    def get_triggers(self):
        return create_e_list(self.e_get("triggers"), AbstractEvent)
    def get_owned_state_transition_realizations(self):
        return create_e_list(self.e_get("ownedStateTransitionRealizations"), StateTransitionRealization)
    def get_realized_state_transitions(self):
        return create_e_list(self.e_get("realizedStateTransitions"), StateTransition)
    def get_realizing_state_transitions(self):
        return create_e_list(self.e_get("realizingStateTransitions"), StateTransition)
    def get_trigger(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateTransitionTrigger", self)

class Pseudostate(AbstractState):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "Pseudostate"))
        elif isinstance(java_object, Pseudostate):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "Pseudostate")
    def get_parent_region(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.EntryExitPoint_ParentRegion", self)

class InitialPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "InitialPseudoState"))
        elif isinstance(java_object, InitialPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "InitialPseudoState")

class JoinPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "JoinPseudoState"))
        elif isinstance(java_object, JoinPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "JoinPseudoState")

class ForkPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ForkPseudoState"))
        elif isinstance(java_object, ForkPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "ForkPseudoState")

class ChoicePseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ChoicePseudoState"))
        elif isinstance(java_object, ChoicePseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "ChoicePseudoState")

class TerminatePseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TerminatePseudoState"))
        elif isinstance(java_object, TerminatePseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "TerminatePseudoState")

class AbstractStateRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractStateRealization"))
        elif isinstance(java_object, AbstractStateRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractStateRealization")
    def get_realized_abstract_state(self):
        value =  self.e_get("realizedAbstractState")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_abstract_state(self):
        value =  self.e_get("realizingAbstractState")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class StateTransitionRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransitionRealization"))
        elif isinstance(java_object, StateTransitionRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransitionRealization")
    def get_realized_state_transition(self):
        value =  self.e_get("realizedStateTransition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_state_transition(self):
        value =  self.e_get("realizingStateTransition")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class ShallowHistoryPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ShallowHistoryPseudoState"))
        elif isinstance(java_object, ShallowHistoryPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "ShallowHistoryPseudoState")

class DeepHistoryPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "DeepHistoryPseudoState"))
        elif isinstance(java_object, DeepHistoryPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "DeepHistoryPseudoState")

class EntryPointPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "EntryPointPseudoState"))
        elif isinstance(java_object, EntryPointPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "EntryPointPseudoState")

class ExitPointPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ExitPointPseudoState"))
        elif isinstance(java_object, ExitPointPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "ExitPointPseudoState")

class StateEventRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateEventRealization"))
        elif isinstance(java_object, StateEventRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "StateEventRealization")
    def get_realized_event(self):
        value =  self.e_get("realizedEvent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def get_realizing_event(self):
        value =  self.e_get("realizingEvent")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)

class StateEvent(NamedElement, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateEvent"))
        elif isinstance(java_object, StateEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "StateEvent")
    def get_expression(self):
        value =  self.e_get("expression")
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules[self.__module__], value.eClass().getName())
            return specific_cls(value)
    def set_expression(self, value):
        return self.e_set("expression", value.get_java_object())
    def get_owned_state_event_realizations(self):
        return create_e_list(self.e_get("ownedStateEventRealizations"), StateEventRealization)

class ChangeEvent(StateEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ChangeEvent"))
        elif isinstance(java_object, ChangeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "ChangeEvent")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)

class TimeEvent(StateEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TimeEvent"))
        elif isinstance(java_object, TimeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_e_class():
        return get_e_classifier("http://www.polarsys.org/capella/core/common/1.4.0", "TimeEvent")
    def get_kind(self):
        return self.e_get("kind").getName()
    def set_kind(self, value):
        self.e_set("kind", value)
