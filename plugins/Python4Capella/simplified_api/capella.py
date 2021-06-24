include('workspace://Python4Capella/java_api/EMF_API.py')
if False:
    from java_api.EMF_API import *
include('workspace://Python4Capella/java_api/Capella_API.py')
if False:
    from java_api.Capella_API import *
include('workspace://Python4Capella/simplified_api/sirius.py')
if False:
    from simplified_api.sirius import *


class Element(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/emde/1.0.0", "Element"))
        elif isinstance(java_object, Element):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class ModelElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "ModelElement"))
        elif isinstance(java_object, ModelElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getId()
    def set_id(self, value):
        self.get_java_object().setId(value)
    def get_sid(self):
        return self.get_java_object().getSid()
    def set_sid(self, value):
        self.get_java_object().setSid(value)
    def get_constraints(self):
        return create_e_list(self.get_java_object().getConstraints(), AbstractConstraint)
    def get_owned_constraints(self):
        return create_e_list(self.get_java_object().getOwnedConstraints(), AbstractConstraint)
    def get_expression(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OwnedSpecification", self)
    def get_all_related_tables(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.diagram.ModelElementRelatedTablesQuery", self)
    def get_all_related_diagrams(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.diagram.ModelElementRelatedDiagramsQuery", self)
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
    def get_name(self):
        return self.get_java_object().getName()
    def set_name(self, value):
        self.get_java_object().setName(value)

class AbstractBehavior(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractBehavior"))
        elif isinstance(java_object, AbstractBehavior):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractType(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractType"))
        elif isinstance(java_object, AbstractType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_inheritedof_typing_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractTypeAbstractTypedElement", self)

class AbstractSignal(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignal"))
        elif isinstance(java_object, AbstractSignal):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractEvent(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractEvent"))
        elif isinstance(java_object, AbstractEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractTimeEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractTimeEvent"))
        elif isinstance(java_object, AbstractTimeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractMessageEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractMessageEvent"))
        elif isinstance(java_object, AbstractMessageEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractSignalEvent(AbstractMessageEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "AbstractSignalEvent"))
        elif isinstance(java_object, AbstractSignalEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractTypedElement(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTypedElement"))
        elif isinstance(java_object, AbstractTypedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ValueSpecification(AbstractTypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "ValueSpecification"))
        elif isinstance(java_object, ValueSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class TimeExpression(ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/1.4.0", "TimeExpression"))
        elif isinstance(java_object, TimeExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class TraceableElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "TraceableElement"))
        elif isinstance(java_object, TraceableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class CapellaElement(TraceableElement, PublishableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "CapellaElement"))
        elif isinstance(java_object, CapellaElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_summary(self):
        return self.get_java_object().getSummary()
    def set_summary(self, value):
        self.get_java_object().setSummary(value)
    def get_description(self):
        return self.get_java_object().getDescription()
    def set_description(self, value):
        self.get_java_object().setDescription(value)
    def get_review(self):
        return self.get_java_object().getReview()
    def set_review(self, value):
        self.get_java_object().setReview(value)
    def get_owned_property_values(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValues(), AbstractPropertyValue)
    def get_owned_enumeration_property_types(self):
        return create_e_list(self.get_java_object().getOwnedEnumerationPropertyTypes(), EnumerationPropertyType)
    def get_applied_property_values(self):
        return create_e_list(self.get_java_object().getAppliedPropertyValues(), AbstractPropertyValue)
    def get_owned_property_value_groups(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValueGroups(), PropertyValueGroup)
    def get_applied_property_value_groups(self):
        return create_e_list(self.get_java_object().getAppliedPropertyValueGroups(), PropertyValueGroup)
    def get_status(self):
        value =  self.get_java_object().getStatus()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_status(self, value):
        return self.get_java_object().setStatus(value.get_java_object())
    def get_requirements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElement_requirement", self)

class NamedElement(AbstractNamedElement, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamedElement"))
        elif isinstance(java_object, NamedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Namespace(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Namespace"))
        elif isinstance(java_object, Namespace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Structure(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Structure"))
        elif isinstance(java_object, Structure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_property_value_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValuePkgs(), PropertyValuePkg)

class ModellingArchitecturePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecturePkg"))
        elif isinstance(java_object, ModellingArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BlockArchitecturePkg(ModellingArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecturePkg"))
        elif isinstance(java_object, BlockArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ModellingArchitecture(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ModellingArchitecture"))
        elif isinstance(java_object, ModellingArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractFunctionalArchitecture(ModellingArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalArchitecture"))
        elif isinstance(java_object, AbstractFunctionalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BlockArchitecture(AbstractFunctionalArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "BlockArchitecture"))
        elif isinstance(java_object, BlockArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Type(AbstractType, Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Type"))
        elif isinstance(java_object, Type):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class AbstractFunctionalBlock(ModellingBlock):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalBlock"))
        elif isinstance(java_object, AbstractFunctionalBlock):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocated_functions(self):
        return create_e_list(self.get_java_object().getAllocatedFunctions(), AbstractFunction)

class Block(ModellingBlock, AbstractFunctionalBlock):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Block"))
        elif isinstance(java_object, Block):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class ComponentArchitecture(BlockArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentArchitecture"))
        elif isinstance(java_object, ComponentArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class GeneralizableElement(Type):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralizableElement"))
        elif isinstance(java_object, GeneralizableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().getAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), GeneralizableElement)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), GeneralizableElement)
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

class InterfaceAllocator(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocator"))
        elif isinstance(java_object, InterfaceAllocator):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CommunicationLinkExchanger(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLinkExchanger"))
        elif isinstance(java_object, CommunicationLinkExchanger):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Component(Block, Classifier, InterfaceAllocator, CommunicationLinkExchanger):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Component"))
        elif isinstance(java_object, Component):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_used_interfaces(self):
        return create_e_list(self.get_java_object().getUsedInterfaces(), Interface)
    def get_implemented_interfaces(self):
        return create_e_list(self.get_java_object().getImplementedInterfaces(), Interface)
    def get_provided_interfaces(self):
        return create_e_list(self.get_java_object().getProvidedInterfaces(), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.get_java_object().getRequiredInterfaces(), Interface)
    def get_contained_component_ports(self):
        return create_e_list(self.get_java_object().getContainedComponentPorts(), ComponentPort)
    def get_contained_physical_ports(self):
        return create_e_list(self.get_java_object().getContainedPhysicalPorts(), PhysicalPort)
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
    def get_representing_parts(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_representingParts", self)
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

class Feature(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Feature"))
        elif isinstance(java_object, Feature):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)

class TypedElement(AbstractTypedElement, NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "TypedElement"))
        elif isinstance(java_object, TypedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class MultiplicityElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "MultiplicityElement"))
        elif isinstance(java_object, MultiplicityElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FinalizableElement(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "FinalizableElement"))
        elif isinstance(java_object, FinalizableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_final(self):
        return self.get_java_object().getFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)

class Property(Feature, TypedElement, MultiplicityElement, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Property"))
        elif isinstance(java_object, Property):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_parent(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyOwner", self)
    def get_association(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyAssociation", self)
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

class InformationsExchanger(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "InformationsExchanger"))
        elif isinstance(java_object, InformationsExchanger):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DeployableElement(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "DeployableElement"))
        elif isinstance(java_object, DeployableElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DeploymentTarget(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "DeploymentTarget"))
        elif isinstance(java_object, DeploymentTarget):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InvolvedElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "InvolvedElement"))
        elif isinstance(java_object, InvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractPathInvolvedElement(InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPathInvolvedElement"))
        elif isinstance(java_object, AbstractPathInvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Part(AbstractInstance, InformationsExchanger, DeployableElement, DeploymentTarget, AbstractPathInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Part"))
        elif isinstance(java_object, Part):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_provided_interfaces(self):
        return create_e_list(self.get_java_object().getProvidedInterfaces(), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.get_java_object().getRequiredInterfaces(), Interface)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Part_type", self)

class AbstractRelationship(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractRelationship"))
        elif isinstance(java_object, AbstractRelationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Relationship(AbstractRelationship, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Relationship"))
        elif isinstance(java_object, Relationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractTrace(TraceableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractTrace"))
        elif isinstance(java_object, AbstractTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Allocation(Relationship, AbstractTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Allocation"))
        elif isinstance(java_object, Allocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class ComponentRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentRealization"))
        elif isinstance(java_object, ComponentRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class MessageReferencePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReferencePkg"))
        elif isinstance(java_object, MessageReferencePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractDependenciesPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractDependenciesPkg"))
        elif isinstance(java_object, AbstractDependenciesPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_dependencies(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractDependenciesPkg_dependencies", self)
    def get_inverse_dependencies(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractDependenciesPkg_inverse_dependencies", self)

class AbstractExchangeItemPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractExchangeItemPkg"))
        elif isinstance(java_object, AbstractExchangeItemPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_exchange_items(self):
        return create_e_list(self.get_java_object().getOwnedExchangeItems(), ExchangeItem)

class InterfacePkg(MessageReferencePkg, AbstractDependenciesPkg, AbstractExchangeItemPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfacePkg"))
        elif isinstance(java_object, InterfacePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_interfaces(self):
        return create_e_list(self.get_java_object().getOwnedInterfaces(), Interface)
    def get_owned_interface_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedInterfacePkgs(), InterfacePkg)

class GeneralClass(Classifier, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "GeneralClass"))
        elif isinstance(java_object, GeneralClass):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)

class Interface(GeneralClass, InterfaceAllocator):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "Interface"))
        elif isinstance(java_object, Interface):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_implementor_components(self):
        return create_e_list(self.get_java_object().getImplementorComponents(), Component)
    def get_user_components(self):
        return create_e_list(self.get_java_object().getUserComponents(), Component)
    def get_exchange_items(self):
        return create_e_list(self.get_java_object().getExchangeItems(), ExchangeItem)
    def get_requiring_component_ports(self):
        return create_e_list(self.get_java_object().getRequiringComponentPorts(), ComponentPort)
    def get_providing_component_ports(self):
        return create_e_list(self.get_java_object().getProvidingComponentPorts(), ComponentPort)
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

class RequiredInterfaceLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "RequiredInterfaceLink"))
        elif isinstance(java_object, RequiredInterfaceLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InterfaceAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "InterfaceAllocation"))
        elif isinstance(java_object, InterfaceAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractEventOperation(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractEventOperation"))
        elif isinstance(java_object, AbstractEventOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExchangeItemAllocation(Relationship, AbstractEventOperation, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ExchangeItemAllocation"))
        elif isinstance(java_object, ExchangeItemAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchange_item(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemAllocationExchangeItem", self)
    def get_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementReferencingScenario", self)

class AbstractDeploymentLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractDeploymentLink"))
        elif isinstance(java_object, AbstractDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractPhysicalArtifact(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalArtifact"))
        elif isinstance(java_object, AbstractPhysicalArtifact):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractPhysicalLinkEnd(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalLinkEnd"))
        elif isinstance(java_object, AbstractPhysicalLinkEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComponentExchangeAllocator(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocator"))
        elif isinstance(java_object, ComponentExchangeAllocator):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocated_component_exchanges(self):
        return create_e_list(self.get_java_object().getAllocatedComponentExchanges(), ComponentExchange)

class AbstractPhysicalPathLink(ComponentExchangeAllocator):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "AbstractPhysicalPathLink"))
        elif isinstance(java_object, AbstractPhysicalPathLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PhysicalLink(AbstractPhysicalPathLink, AbstractPhysicalArtifact, AbstractPathInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLink"))
        elif isinstance(java_object, PhysicalLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_categories(self):
        return create_e_list(self.get_java_object().getCategories(), PhysicalLinkCategory)
    def get_realized_physical_links(self):
        return create_e_list(self.get_java_object().getRealizedPhysicalLinks(), PhysicalLink)
    def get_realizing_physical_links(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalLinks(), PhysicalLink)
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
    def get_links(self):
        return create_e_list(self.get_java_object().getLinks(), PhysicalLink)
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

class PhysicalLinkRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalLinkRealization"))
        elif isinstance(java_object, PhysicalLinkRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InvolverElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "InvolverElement"))
        elif isinstance(java_object, InvolverElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PhysicalPath(NamedElement, ComponentExchangeAllocator, AbstractPathInvolvedElement, InvolverElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPath"))
        elif isinstance(java_object, PhysicalPath):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involved_physical_paths(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvedPhysicalPath", self)
    def get_involved_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_PhysicalLinks", self)
    def get_allocated_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_RealisedConnection", self)
    def get_physical_paths(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPathInvolvingPhysicalPath", self)

class Involvement(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Involvement"))
        elif isinstance(java_object, Involvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involved_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInvolvementTarget", self)
    def get_involving_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsInvolvementSource", self)

class PhysicalPathInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathInvolvement"))
        elif isinstance(java_object, PhysicalPathInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class PhysicalPathRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPathRealization"))
        elif isinstance(java_object, PhysicalPathRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Port(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Port"))
        elif isinstance(java_object, Port):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_provided_interfaces(self):
        return create_e_list(self.get_java_object().getProvidedInterfaces(), Interface)
    def get_required_interfaces(self):
        return create_e_list(self.get_java_object().getRequiredInterfaces(), Interface)

class PhysicalPort(Port, AbstractPhysicalArtifact, InformationsExchanger, AbstractPhysicalLinkEnd, Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "PhysicalPort"))
        elif isinstance(java_object, PhysicalPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocated_component_ports(self):
        return create_e_list(self.get_java_object().getAllocatedComponentPorts(), ComponentPort)
    def get_realized_physical_ports(self):
        return create_e_list(self.get_java_object().getRealizedPhysicalPorts(), PhysicalPort)
    def get_realizing_physical_ports(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalPorts(), PhysicalPort)
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

class ComponentPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/1.4.0", "ComponentPkg"))
        elif isinstance(java_object, ComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class DataValue(NamedElement, ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValue"))
        elif isinstance(java_object, DataValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().getAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyValue_applying_valued_element_DataValue", self)
    def get_referenced_property(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueRefReferencedProperty", self)
    def get_referenced_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueRefReferencedValue", self)
    def get_referencing_value(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.DataValueReferencingReferencedValue", self)

class DataValueContainer(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "DataValueContainer"))
        elif isinstance(java_object, DataValueContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractBooleanValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractBooleanValue"))
        elif isinstance(java_object, AbstractBooleanValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralBooleanValue(AbstractBooleanValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralBooleanValue"))
        elif isinstance(java_object, LiteralBooleanValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class BooleanReference(AbstractBooleanValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BooleanReference"))
        elif isinstance(java_object, BooleanReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractEnumerationValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractEnumerationValue"))
        elif isinstance(java_object, AbstractEnumerationValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EnumerationLiteral(AbstractEnumerationValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationLiteral"))
        elif isinstance(java_object, EnumerationLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EnumerationReference(AbstractEnumerationValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "EnumerationReference"))
        elif isinstance(java_object, EnumerationReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractStringValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractStringValue"))
        elif isinstance(java_object, AbstractStringValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralStringValue(AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralStringValue"))
        elif isinstance(java_object, LiteralStringValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class StringReference(AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "StringReference"))
        elif isinstance(java_object, StringReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class NumericValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericValue"))
        elif isinstance(java_object, NumericValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralNumericValue(NumericValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "LiteralNumericValue"))
        elif isinstance(java_object, LiteralNumericValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class NumericReference(NumericValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "NumericReference"))
        elif isinstance(java_object, NumericReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractComplexValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractComplexValue"))
        elif isinstance(java_object, AbstractComplexValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComplexValue(AbstractComplexValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValue"))
        elif isinstance(java_object, ComplexValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComplexValueReference(AbstractComplexValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ComplexValueReference"))
        elif isinstance(java_object, ComplexValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ValuePart(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "ValuePart"))
        elif isinstance(java_object, ValuePart):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractExpressionValue(AbstractBooleanValue, AbstractComplexValue, AbstractEnumerationValue, NumericValue, AbstractStringValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "AbstractExpressionValue"))
        elif isinstance(java_object, AbstractExpressionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BinaryExpression(AbstractExpressionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "BinaryExpression"))
        elif isinstance(java_object, BinaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class UnaryExpression(AbstractExpressionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "UnaryExpression"))
        elif isinstance(java_object, UnaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OpaqueExpression(CapellaElement, ValueSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/1.4.0", "OpaqueExpression"))
        elif isinstance(java_object, OpaqueExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class RequirementsPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsPkg"))
        elif isinstance(java_object, RequirementsPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Trace(Relationship, AbstractTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Trace"))
        elif isinstance(java_object, Trace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsTraceTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsTraceSource", self)

class RequirementsTrace(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "RequirementsTrace"))
        elif isinstance(java_object, RequirementsTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class Requirement(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "Requirement"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class SystemFunctionalRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemFunctionalRequirement"))
        elif isinstance(java_object, SystemFunctionalRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemNonFunctionalInterfaceRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalInterfaceRequirement"))
        elif isinstance(java_object, SystemNonFunctionalInterfaceRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemNonFunctionalRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemNonFunctionalRequirement"))
        elif isinstance(java_object, SystemNonFunctionalRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemUserRequirement(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/requirement/1.4.0", "SystemUserRequirement"))
        elif isinstance(java_object, SystemUserRequirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class NamedRelationship(Relationship, NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamedRelationship"))
        elif isinstance(java_object, NamedRelationship):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ReuserStructure(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuserStructure"))
        elif isinstance(java_object, ReuserStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractModellingStructure(ReuserStructure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractModellingStructure"))
        elif isinstance(java_object, AbstractModellingStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractAnnotation(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractAnnotation"))
        elif isinstance(java_object, AbstractAnnotation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class NamingRule(AbstractAnnotation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "NamingRule"))
        elif isinstance(java_object, NamingRule):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractConstraint(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractConstraint"))
        elif isinstance(java_object, AbstractConstraint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_constrained_elements(self):
        return create_e_list(self.get_java_object().getConstrainedElements(), ModelElement)

class Constraint(NamedElement, AbstractConstraint):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Constraint"))
        elif isinstance(java_object, Constraint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class ReuseLink(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseLink"))
        elif isinstance(java_object, ReuseLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ReuseableStructure(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "ReuseableStructure"))
        elif isinstance(java_object, ReuseableStructure):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Generalization(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "Generalization"))
        elif isinstance(java_object, Generalization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_super(self):
        value =  self.get_java_object().getSuper()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_super(self, value):
        return self.get_java_object().setSuper(value.get_java_object())
    def get_sub(self):
        value =  self.get_java_object().getSub()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_sub(self, value):
        return self.get_java_object().setSub(value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsGeneralizationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsGeneralizationSource", self)

class AbstractPropertyValue(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "AbstractPropertyValue"))
        elif isinstance(java_object, AbstractPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_valued_elements(self):
        return create_e_list(self.get_java_object().getValuedElements(), CapellaElement)
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
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class IntegerPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "IntegerPropertyValue"))
        elif isinstance(java_object, IntegerPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class BooleanPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "BooleanPropertyValue"))
        elif isinstance(java_object, BooleanPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class FloatPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "FloatPropertyValue"))
        elif isinstance(java_object, FloatPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)

class EnumerationPropertyValue(AbstractPropertyValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyValue"))
        elif isinstance(java_object, EnumerationPropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())
    def get_value(self):
        value =  self.get_java_object().getValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.get_java_object().setValue(value.get_java_object())

class EnumerationPropertyType(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyType"))
        elif isinstance(java_object, EnumerationPropertyType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationPropertyLiteral)

class EnumerationPropertyLiteral(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "EnumerationPropertyLiteral"))
        elif isinstance(java_object, EnumerationPropertyLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PropertyValueGroup(Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValueGroup"))
        elif isinstance(java_object, PropertyValueGroup):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_valued_elements(self):
        return create_e_list(self.get_java_object().getValuedElements(), CapellaElement)

class PropertyValuePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/1.4.0", "PropertyValuePkg"))
        elif isinstance(java_object, PropertyValuePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ReAbstractElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReAbstractElement"))
        elif isinstance(java_object, ReAbstractElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getId()
    def set_id(self, value):
        self.get_java_object().setId(value)

class ReNamedElement(ReAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReNamedElement"))
        elif isinstance(java_object, ReNamedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_name(self):
        return self.get_java_object().getName()
    def set_name(self, value):
        self.get_java_object().setName(value)

class ReDescriptionElement(ReNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReDescriptionElement"))
        elif isinstance(java_object, ReDescriptionElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_description(self):
        return self.get_java_object().getDescription()
    def set_description(self, value):
        self.get_java_object().setDescription(value)

class ReElementContainer(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "ReElementContainer"))
        elif isinstance(java_object, ReElementContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_elements(self):
        return create_e_list(self.get_java_object().getOwnedElements(), CatalogElement)

class CatalogElementPkg(ReNamedElement, ReElementContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementPkg"))
        elif isinstance(java_object, CatalogElementPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_element_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedElementPkgs(), CatalogElementPkg)

class ElementExtension(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/emde/1.0.0", "ElementExtension"))
        elif isinstance(java_object, ElementExtension):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class RecCatalog(CatalogElementPkg, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "RecCatalog"))
        elif isinstance(java_object, RecCatalog):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_compliancy_definition_pkg(self):
        value =  self.get_java_object().getOwnedCompliancyDefinitionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_compliancy_definition_pkg(self, value):
        return self.get_java_object().setOwnedCompliancyDefinitionPkg(value.get_java_object())

class GroupingElementPkg(CatalogElementPkg, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "GroupingElementPkg"))
        elif isinstance(java_object, GroupingElementPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CatalogElementLink(ReAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CatalogElementLink"))
        elif isinstance(java_object, CatalogElementLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_origin(self):
        value =  self.get_java_object().getOrigin()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_origin(self, value):
        return self.get_java_object().setOrigin(value.get_java_object())
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
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_author(self):
        return self.get_java_object().getAuthor()
    def set_author(self, value):
        self.get_java_object().setAuthor(value)
    def get_environment(self):
        return self.get_java_object().getEnvironment()
    def set_environment(self, value):
        self.get_java_object().setEnvironment(value)
    def get_suffix(self):
        return self.get_java_object().getSuffix()
    def set_suffix(self, value):
        self.get_java_object().setSuffix(value)
    def get_read_only(self):
        return self.get_java_object().getReadOnly()
    def set_read_only(self, value):
        self.get_java_object().setReadOnly(value)
    def get_tags(self):
        return self.get_java_object().getTags()
    def set_tags(self, value):
        self.get_java_object().setTags(value)
    def get_origin(self):
        value =  self.get_java_object().getOrigin()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_origin(self, value):
        return self.get_java_object().setOrigin(value.get_java_object())
    def get_current_compliancy(self):
        value =  self.get_java_object().getCurrentCompliancy()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_current_compliancy(self, value):
        return self.get_java_object().setCurrentCompliancy(value.get_java_object())
    def get_default_replica_compliancy(self):
        value =  self.get_java_object().getDefaultReplicaCompliancy()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_replica_compliancy(self, value):
        return self.get_java_object().setDefaultReplicaCompliancy(value.get_java_object())
    def get_referenced_elements(self):
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)
    def get_replicated_elements(self):
        return create_e_list(self.get_java_object().getReplicatedElements(), CatalogElement)
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
    def get_owned_definitions(self):
        return create_e_list(self.get_java_object().getOwnedDefinitions(), CompliancyDefinition)

class CompliancyDefinition(ReDescriptionElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/1.4.0", "CompliancyDefinition"))
        elif isinstance(java_object, CompliancyDefinition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EPBSArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecturePkg"))
        elif isinstance(java_object, EPBSArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EPBSArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "EPBSArchitecture"))
        elif isinstance(java_object, EPBSArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_configuration_item_pkg(self):
        value =  self.get_java_object().getOwnedConfigurationItemPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_configuration_item_pkg(self, value):
        return self.get_java_object().setOwnedConfigurationItemPkg(value.get_java_object())
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class ConfigurationItemPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItemPkg"))
        elif isinstance(java_object, ConfigurationItemPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_configuration_items(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)

class CapabilityRealizationInvolvedElement(InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvedElement"))
        elif isinstance(java_object, CapabilityRealizationInvolvedElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involving_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealizationInvolvedElement_InvolvingCapabilityRealizations", self)

class ConfigurationItem(CapabilityRealizationInvolvedElement, Component):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "ConfigurationItem"))
        elif isinstance(java_object, ConfigurationItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_item_identifier(self):
        return self.get_java_object().getItemIdentifier()
    def set_item_identifier(self, value):
        self.get_java_object().setItemIdentifier(value)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_owned_configuration_items(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_allocated_physical_artifacts(self):
        return create_e_list(self.get_java_object().getAllocatedPhysicalArtifacts(), AbstractPhysicalArtifact)
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

class PhysicalArtifactRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/1.4.0", "PhysicalArtifactRealization"))
        elif isinstance(java_object, PhysicalArtifactRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CommunicationItem(Classifier, DataValueContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationItem"))
        elif isinstance(java_object, CommunicationItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class ExceptionCapella(CommunicationItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "ExceptionCapella"))
        elif isinstance(java_object, ExceptionCapella):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Message(CommunicationItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Message"))
        elif isinstance(java_object, Message):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class MessageReference(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "MessageReference"))
        elif isinstance(java_object, MessageReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Signal(CommunicationItem, AbstractSignal):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "Signal"))
        elif isinstance(java_object, Signal):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SignalInstance(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "SignalInstance"))
        elif isinstance(java_object, SignalInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CommunicationLink(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/1.4.0", "CommunicationLink"))
        elif isinstance(java_object, CommunicationLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_exchange_item(self):
        value =  self.get_java_object().getExchangeItem()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_item(self, value):
        return self.get_java_object().setExchangeItem(value.get_java_object())
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationLinkExchangeItem", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationLinkComponent", self)

class SequenceMessage(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessage"))
        elif isinstance(java_object, SequenceMessage):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
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
    def get_invoked_operation(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_invokedOperation", self)
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
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_instance_roles(self):
        return create_e_list(self.get_java_object().getOwnedInstanceRoles(), InstanceRole)
    def get_owned_messages(self):
        return create_e_list(self.get_java_object().getOwnedMessages(), SequenceMessage)
    def get_owned_constraint_durations(self):
        return create_e_list(self.get_java_object().getOwnedConstraintDurations(), ConstraintDuration)
    def get_referenced_scenarios(self):
        return create_e_list(self.get_java_object().getReferencedScenarios(), Scenario)
    def get_realized_scenarios(self):
        return create_e_list(self.get_java_object().getRealizedScenarios(), Scenario)
    def get_realizing_scenarios(self):
        return create_e_list(self.get_java_object().getRealizingScenarios(), Scenario)
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

class AbstractEnd(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractEnd"))
        elif isinstance(java_object, AbstractEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class MessageEnd(AbstractEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "MessageEnd"))
        elif isinstance(java_object, MessageEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class TimeLapse(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "TimeLapse"))
        elif isinstance(java_object, TimeLapse):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Execution(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Execution"))
        elif isinstance(java_object, Execution):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExecutionEnd(AbstractEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEnd"))
        elif isinstance(java_object, ExecutionEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Event(NamedElement, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Event"))
        elif isinstance(java_object, Event):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CreationEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "CreationEvent"))
        elif isinstance(java_object, CreationEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DestructionEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "DestructionEvent"))
        elif isinstance(java_object, DestructionEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExecutionEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ExecutionEvent"))
        elif isinstance(java_object, ExecutionEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InstanceRole(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InstanceRole"))
        elif isinstance(java_object, InstanceRole):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_parent_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InstanceRole_parentScenario", self)
    def get_represented_instance(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InstanceRole_representedInstance", self)

class EventReceiptOperation(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventReceiptOperation"))
        elif isinstance(java_object, EventReceiptOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EventSentOperation(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "EventSentOperation"))
        elif isinstance(java_object, EventSentOperation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class MergeLink(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "MergeLink"))
        elif isinstance(java_object, MergeLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class RefinementLink(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "RefinementLink"))
        elif isinstance(java_object, RefinementLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractCapabilityRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityRealization"))
        elif isinstance(java_object, AbstractCapabilityRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractFunctionalChainContainer(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionalChainContainer"))
        elif isinstance(java_object, AbstractFunctionalChainContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_functional_chains(self):
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)

class AbstractCapability(Structure, InvolverElement, AbstractFunctionalChainContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapability"))
        elif isinstance(java_object, AbstractCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_scenarios(self):
        return create_e_list(self.get_java_object().getOwnedScenarios(), Scenario)
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), AbstractCapability)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), AbstractCapability)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involved_functional_chains(self):
        return create_e_list(self.get_java_object().getInvolvedFunctionalChains(), FunctionalChain)
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

class AbstractCapabilityExtend(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityExtend"))
        elif isinstance(java_object, AbstractCapabilityExtend):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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
    def get_abstract_capability(self):
        value =  self.get_java_object().getAbstractCapability()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class AbstractCapabilityGeneralization(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractCapabilityGeneralization"))
        elif isinstance(java_object, AbstractCapabilityGeneralization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_super(self):
        value =  self.get_java_object().getSuper()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_super(self, value):
        return self.get_java_object().setSuper(value.get_java_object())
    def get_sub(self):
        value =  self.get_java_object().getSub()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
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

class AbstractFragment(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFragment"))
        elif isinstance(java_object, AbstractFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InteractionUse(AbstractFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionUse"))
        elif isinstance(java_object, InteractionUse):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_referenced_scenario(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InteractionUseReferencedScenario", self)
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

class Gate(MessageEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "Gate"))
        elif isinstance(java_object, Gate):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InteractionOperand(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "InteractionOperand"))
        elif isinstance(java_object, InteractionOperand):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_guard(self):
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.get_java_object().setGuard(value.get_java_object())

class FragmentEnd(InteractionFragment):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "FragmentEnd"))
        elif isinstance(java_object, FragmentEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalChainAbstractCapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "FunctionalChainAbstractCapabilityInvolvement"))
        elif isinstance(java_object, FunctionalChainAbstractCapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_functional_chain(self):
        value =  self.get_java_object().getFunctionalChain()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class AbstractFunctionAbstractCapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "AbstractFunctionAbstractCapabilityInvolvement"))
        elif isinstance(java_object, AbstractFunctionAbstractCapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ScenarioRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ScenarioRealization"))
        elif isinstance(java_object, ScenarioRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateFragment(TimeLapse):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "StateFragment"))
        elif isinstance(java_object, StateFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class CancelTimerEvent(Event):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "CancelTimerEvent"))
        elif isinstance(java_object, CancelTimerEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ConstraintDuration(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "ConstraintDuration"))
        elif isinstance(java_object, ConstraintDuration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SequenceMessageValuation(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/1.4.0", "SequenceMessageValuation"))
        elif isinstance(java_object, SequenceMessageValuation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        value =  self.get_java_object().getValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.get_java_object().setValue(value.get_java_object())

class AssociationPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AssociationPkg"))
        elif isinstance(java_object, AssociationPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)

class Association(NamedRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Association"))
        elif isinstance(java_object, Association):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_realized_classes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ClassRealizedClass", self)
    def get_realizing_classes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ClassRealizingClass", self)

class Collection(Classifier, MultiplicityElement, DataValueContainer, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Collection"))
        elif isinstance(java_object, Collection):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class AbstractCollectionValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "AbstractCollectionValue"))
        elif isinstance(java_object, AbstractCollectionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CollectionValue(AbstractCollectionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValue"))
        elif isinstance(java_object, CollectionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_elements(self):
        return create_e_list(self.get_java_object().getOwnedElements(), DataValue)

class CollectionValueReference(AbstractCollectionValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "CollectionValueReference"))
        elif isinstance(java_object, CollectionValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DataPkg(AbstractDependenciesPkg, AbstractExchangeItemPkg, AssociationPkg, DataValueContainer, MessageReferencePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "DataPkg"))
        elif isinstance(java_object, DataPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_messages(self):
        return create_e_list(self.get_java_object().getOwnedMessages(), Message)

class DomainElement(Class):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "DomainElement"))
        elif isinstance(java_object, DomainElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class KeyPart(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "KeyPart"))
        elif isinstance(java_object, KeyPart):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Operation(Feature, AbstractEvent, AbstractEventOperation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Operation"))
        elif isinstance(java_object, Operation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_realized_exchange_items(self):
        return create_e_list(self.get_java_object().getRealizedExchangeItems(), ExchangeItem)
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

class AbstractParameter(AbstractTypedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameter"))
        elif isinstance(java_object, AbstractParameter):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Parameter(TypedElement, MultiplicityElement, AbstractParameter):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Parameter"))
        elif isinstance(java_object, Parameter):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class Union(Class):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Union"))
        elif isinstance(java_object, Union):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)

class UnionProperty(Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "UnionProperty"))
        elif isinstance(java_object, UnionProperty):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Unit(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "Unit"))
        elif isinstance(java_object, Unit):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PortRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "PortRealization"))
        elif isinstance(java_object, PortRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PortAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "PortAllocation"))
        elif isinstance(java_object, PortAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractExchangeItem(AbstractType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractExchangeItem"))
        elif isinstance(java_object, AbstractExchangeItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExchangeItem(AbstractExchangeItem, AbstractEvent, AbstractSignal, FinalizableElement, GeneralizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItem"))
        elif isinstance(java_object, ExchangeItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchange_mechanism(self):
        return self.get_java_object().getExchangeMechanism().getName()
    def set_exchange_mechanism(self, value):
        self.get_java_object().setExchangeMechanism(value)
    def get_owned_elements(self):
        return create_e_list(self.get_java_object().getOwnedElements(), ExchangeItemElement)
    def get_allocator_interfaces(self):
        return create_e_list(self.get_java_object().getAllocatorInterfaces(), Interface)
    def get_realized_exchange_items(self):
        return create_e_list(self.get_java_object().getRealizedExchangeItems(), ExchangeItem)
    def get_realizing_exchange_items(self):
        return create_e_list(self.get_java_object().getRealizingExchangeItems(), ExchangeItem)
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
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
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

class ExchangeItemRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/1.4.0", "ExchangeItemRealization"))
        elif isinstance(java_object, ExchangeItemRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DataType(GeneralizableElement, DataValueContainer, FinalizableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "DataType"))
        elif isinstance(java_object, DataType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        return self.get_java_object().getVisibility().getName()
    def set_visibility(self, value):
        self.get_java_object().setVisibility(value)

class BooleanType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "BooleanType"))
        elif isinstance(java_object, BooleanType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), LiteralBooleanValue)

class Enumeration(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "Enumeration"))
        elif isinstance(java_object, Enumeration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationLiteral)

class StringType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "StringType"))
        elif isinstance(java_object, StringType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class NumericType(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "NumericType"))
        elif isinstance(java_object, NumericType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)

class PhysicalQuantity(NumericType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/1.4.0", "PhysicalQuantity"))
        elif isinstance(java_object, PhysicalQuantity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Project(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Project"))
        elif isinstance(java_object, Project):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Folder(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Folder"))
        elif isinstance(java_object, Folder):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ModelRoot(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "ModelRoot"))
        elif isinstance(java_object, ModelRoot):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemEngineering(AbstractModellingStructure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineering"))
        elif isinstance(java_object, SystemEngineering):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemEngineeringPkg(Structure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "SystemEngineeringPkg"))
        elif isinstance(java_object, SystemEngineeringPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Library(Project):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/1.4.0", "Library"))
        elif isinstance(java_object, Library):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OperationalAnalysis(BlockArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalAnalysis"))
        elif isinstance(java_object, OperationalAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_entity_pkg(self):
        value =  self.get_java_object().getOwnedEntityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_entity_pkg(self, value):
        return self.get_java_object().setOwnedEntityPkg(value.get_java_object())
    def get_operational_capability_pkg(self):
        value =  self.get_java_object().getContainedOperationalCapabilityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_operational_activity_pkg(self):
        value =  self.get_java_object().getContainedOperationalActivityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class OperationalScenario(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalScenario"))
        elif isinstance(java_object, OperationalScenario):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionPkg"))
        elif isinstance(java_object, FunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OperationalActivityPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivityPkg"))
        elif isinstance(java_object, OperationalActivityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_activities(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivities(), OperationalActivity)
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)

class ActivityNode(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityNode"))
        elif isinstance(java_object, ActivityNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_outgoing(self):
        return create_e_list(self.get_java_object().getOutgoing(), ActivityEdge)
    def get_incoming(self):
        return create_e_list(self.get_java_object().getIncoming(), ActivityEdge)

class ExecutableNode(ActivityNode):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ExecutableNode"))
        elif isinstance(java_object, ExecutableNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractAction(ExecutableNode, AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractAction"))
        elif isinstance(java_object, AbstractAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_inputs(self):
        return create_e_list(self.get_java_object().getInputs(), InputPin)
    def get_outputs(self):
        return create_e_list(self.get_java_object().getOutputs(), OutputPin)

class InvocationAction(AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "InvocationAction"))
        elif isinstance(java_object, InvocationAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CallAction(InvocationAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "CallAction"))
        elif isinstance(java_object, CallAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CallBehaviorAction(CallAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "CallBehaviorAction"))
        elif isinstance(java_object, CallBehaviorAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractFunction(Namespace, InvolvedElement, AbstractInstance, AbstractFunctionalChainContainer, CallBehaviorAction, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunction"))
        elif isinstance(java_object, AbstractFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involving_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_involving_functional_chains(self):
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
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

class OperationalActivity(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalActivity"))
        elif isinstance(java_object, OperationalActivity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_realizing_system_functions(self):
        return create_e_list(self.get_java_object().getRealizingSystemFunctions(), SystemFunction)
    def get_contained_operational_activities(self):
        return create_e_list(self.get_java_object().getContainedOperationalActivities(), OperationalActivity)
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

class FunctionalChain(NamedElement, InvolverElement, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChain"))
        elif isinstance(java_object, FunctionalChain):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_involved_functions(self):
        return create_e_list(self.get_java_object().getInvolvedFunctions(), AbstractFunction)
    def get_involved_functional_exchanges(self):
        return create_e_list(self.get_java_object().getInvolvedFunctionalExchanges(), FunctionalExchange)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involving_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_involved_functional_chains(self):
        return create_e_list(self.get_java_object().getRealizedFunctionalChains(), FunctionalChain)
    def get_realizing_functional_chains(self):
        return create_e_list(self.get_java_object().getRealizingFunctionalChains(), FunctionalChain)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChain_owningFunction", self)
    def get_realized_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizedOperationalProcess", self)
    def get_realized_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizedFunctionalChains", self)
    def get_active_in_states(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainAvailableInState", self)
    def get_involvement_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementLinks", self)
    def get_involved_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChain_enactedComponents", self)
    def get_active_in_modes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainAvailableInMode", self)
    def get_involving_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.LAAndPAFunctionalChainInvolvingCapabilityRealization", self)
    def get_parent_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainParent", self)

class OperationalProcess(FunctionalChain):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalProcess"))
        elif isinstance(java_object, OperationalProcess):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involving_operational_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
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

class ActivityPartition(ActivityGroup, AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityPartition"))
        elif isinstance(java_object, ActivityPartition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Swimlane(NamedElement, ActivityPartition):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Swimlane"))
        elif isinstance(java_object, Swimlane):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractCapabilityPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractCapabilityPkg"))
        elif isinstance(java_object, AbstractCapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OperationalCapabilityPkg(AbstractCapabilityPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapabilityPkg"))
        elif isinstance(java_object, OperationalCapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_capabilities(self):
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilities(), OperationalCapability)
    def get_owned_operational_capability_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilityPkgs(), OperationalCapabilityPkg)

class OperationalCapability(AbstractCapability, Namespace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OperationalCapability"))
        elif isinstance(java_object, OperationalCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_realizing_capabilities(self):
        return create_e_list(self.get_java_object().getRealizingCapabilities(), Capability)
    def get_involved_entities(self):
        return create_e_list(self.get_java_object().getInvolvedEntities(), Entity)
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

class RolePkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "RolePkg"))
        elif isinstance(java_object, RolePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Role(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Role"))
        elif isinstance(java_object, Role):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocated_operational_activities(self):
        return create_e_list(self.get_java_object().getAllocatedOperationalActivities(), OperationalActivity)
    def get_allocating_entities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Role_AllocatingEntity", self)
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

class RoleAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "RoleAllocation"))
        elif isinstance(java_object, RoleAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_entity(self):
        value =  self.get_java_object().getEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class EntityPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "EntityPkg"))
        elif isinstance(java_object, EntityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_entities(self):
        return create_e_list(self.get_java_object().getOwnedEntities(), Entity)
    def get_owned_entity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedEntityPkgs(), EntityPkg)

class AbstractConceptItem(Component):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "AbstractConceptItem"))
        elif isinstance(java_object, AbstractConceptItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Entity(AbstractConceptItem, InformationsExchanger, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Entity"))
        elif isinstance(java_object, Entity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_entities(self):
        return create_e_list(self.get_java_object().getOwnedEntities(), Entity)
    def get_allocated_operational_activities(self):
        return create_e_list(self.get_java_object().getAllocatedOperationalActivities(), OperationalActivity)
    def get_involving_operational_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_breakdown(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_Breakdown", self)
    def get_allocated_roles(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntityAllocatedRoles", self)
    def get_outgoing_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_OutgoingCommunicationMean", self)
    def get_incoming_communication_mean(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalEntity_IncomingCommunicationMean", self)
    def get_realizing_system_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizingComponents", self)

class ConceptPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptPkg"))
        elif isinstance(java_object, ConceptPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Concept(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Concept"))
        elif isinstance(java_object, Concept):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ConceptCompliance(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ConceptCompliance"))
        elif isinstance(java_object, ConceptCompliance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ItemInConcept(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "ItemInConcept"))
        elif isinstance(java_object, ItemInConcept):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CommunityOfInterest(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterest"))
        elif isinstance(java_object, CommunityOfInterest):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CommunityOfInterestComposition(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunityOfInterestComposition"))
        elif isinstance(java_object, CommunityOfInterestComposition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OrganisationalUnit(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnit"))
        elif isinstance(java_object, OrganisationalUnit):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class OrganisationalUnitComposition(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "OrganisationalUnitComposition"))
        elif isinstance(java_object, OrganisationalUnitComposition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Location(AbstractConceptItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "Location"))
        elif isinstance(java_object, Location):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CapabilityConfiguration(AbstractConceptItem):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CapabilityConfiguration"))
        elif isinstance(java_object, CapabilityConfiguration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractInformationFlow(AbstractNamedElement, AbstractRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractInformationFlow"))
        elif isinstance(java_object, AbstractInformationFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_convoyed_informations(self):
        return create_e_list(self.get_java_object().getConvoyedInformations(), AbstractExchangeItem)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())

class ActivityExchange(AbstractInformationFlow):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityExchange"))
        elif isinstance(java_object, ActivityExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExchangeSpecification(NamedElement, ActivityExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecification"))
        elif isinstance(java_object, ExchangeSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_realized_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_realizedDataflow", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_dataflowTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_dataflowSource", self)

class ComponentExchange(AbstractEvent, AbstractEventOperation, NamedElement, ExchangeSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchange"))
        elif isinstance(java_object, ComponentExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_allocated_functional_exchanges(self):
        return create_e_list(self.get_java_object().getAllocatedFunctionalExchanges(), FunctionalExchange)
    def get_categories(self):
        return create_e_list(self.get_java_object().getCategories(), ComponentExchangeCategory)
    def get_realized_component_exchanges(self):
        return create_e_list(self.get_java_object().getRealizedComponentExchanges(), ComponentExchange)
    def get_realizing_component_exchanges(self):
        return create_e_list(self.get_java_object().getRealizingComponentExchanges(), ComponentExchange)
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

class CommunicationMean(NamedRelationship, ComponentExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/1.4.0", "CommunicationMean"))
        elif isinstance(java_object, CommunicationMean):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source_entity(self):
        value =  self.get_java_object().getSourceEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_target_entity(self):
        value =  self.get_java_object().getTargetEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
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
    def get_entity(self):
        value =  self.get_java_object().getEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class PhysicalArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecturePkg"))
        elif isinstance(java_object, PhysicalArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PhysicalArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalArchitecture"))
        elif isinstance(java_object, PhysicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_physical_component_pkg(self):
        value =  self.get_java_object().getOwnedPhysicalComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_physical_component_pkg(self, value):
        return self.get_java_object().setOwnedPhysicalComponentPkg(value.get_java_object())
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_physical_function_pkg(self):
        value =  self.get_java_object().getContainedPhysicalFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class PhysicalFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalFunction"))
        elif isinstance(java_object, PhysicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_realized_logical_functions(self):
        return create_e_list(self.get_java_object().getRealizedLogicalFunctions(), LogicalFunction)
    def get_contained_physical_functions(self):
        return create_e_list(self.get_java_object().getContainedPhysicalFunctions(), PhysicalFunction)
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
    def get_owned_physical_functions(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctions(), PhysicalFunction)
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)

class PhysicalComponent(AbstractPhysicalArtifact, Component, CapabilityRealizationInvolvedElement, DeployableElement, DeploymentTarget):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponent"))
        elif isinstance(java_object, PhysicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_owned_physical_components(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_deployed_physical_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_deployedPhysicalComponents", self)
    def get_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_IncomingPhysicalLinks", self)
    def get_allocated_physical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_AllocatedFunctions", self)
    def get_internal_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_InternalPhysicalLinks", self)
    def get_realized_logical_component(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizedComponents", self)
    def get_realizing_configuration_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizingComponents", self)
    def get_deploying_physical_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalComponent_deployingPhysicalComponents", self)

class PhysicalComponentPkg(ComponentPkg, AssociationPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalComponentPkg"))
        elif isinstance(java_object, PhysicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_components(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)

class PhysicalNode(PhysicalComponent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "PhysicalNode"))
        elif isinstance(java_object, PhysicalNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LogicalArchitectureRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalArchitectureRealization"))
        elif isinstance(java_object, LogicalArchitectureRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LogicalInterfaceRealization(InterfaceAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/1.4.0", "LogicalInterfaceRealization"))
        elif isinstance(java_object, LogicalInterfaceRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractPhysicalInstance(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "AbstractPhysicalInstance"))
        elif isinstance(java_object, AbstractPhysicalInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComponentInstance(AbstractPhysicalInstance, DeployableElement, DeploymentTarget):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ComponentInstance"))
        elif isinstance(java_object, ComponentInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class ConnectionInstance(AbstractPhysicalInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "ConnectionInstance"))
        elif isinstance(java_object, ConnectionInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class DeploymentAspect(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentAspect"))
        elif isinstance(java_object, DeploymentAspect):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DeploymentConfiguration(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "DeploymentConfiguration"))
        elif isinstance(java_object, DeploymentConfiguration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InstanceDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "InstanceDeploymentLink"))
        elif isinstance(java_object, InstanceDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PartDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PartDeploymentLink"))
        elif isinstance(java_object, PartDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PortInstance(AbstractPhysicalInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "PortInstance"))
        elif isinstance(java_object, PortInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class TypeDeploymentLink(AbstractDeploymentLink):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/deployment/1.4.0", "TypeDeploymentLink"))
        elif isinstance(java_object, TypeDeploymentLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LogicalArchitecturePkg(BlockArchitecturePkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecturePkg"))
        elif isinstance(java_object, LogicalArchitecturePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LogicalArchitecture(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalArchitecture"))
        elif isinstance(java_object, LogicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_logical_component_pkg(self):
        value =  self.get_java_object().getOwnedLogicalComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_logical_component_pkg(self, value):
        return self.get_java_object().setOwnedLogicalComponentPkg(value.get_java_object())
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_logical_function_pkg(self):
        value =  self.get_java_object().getContainedLogicalFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class LogicalFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalFunction"))
        elif isinstance(java_object, LogicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_realized_system_functions(self):
        return create_e_list(self.get_java_object().getRealizedSystemFunctions(), SystemFunction)
    def get_realizing_physical_functions(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalFunctions(), PhysicalFunction)
    def get_contained_logical_functions(self):
        return create_e_list(self.get_java_object().getContainedLogicalFunctions(), LogicalFunction)
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
    def get_owned_logical_functions(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctions(), LogicalFunction)
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)

class LogicalComponent(Component, CapabilityRealizationInvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponent"))
        elif isinstance(java_object, LogicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_components(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_realized_system_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizedComponents", self)
    def get_allocated_logical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_AllocatedFunctions", self)
    def get_realizing_physical_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizingComponents", self)

class LogicalComponentPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "LogicalComponentPkg"))
        elif isinstance(java_object, LogicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_components(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)

class CapabilityRealization(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "CapabilityRealization"))
        elif isinstance(java_object, CapabilityRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_realized_capabilities(self):
        return create_e_list(self.get_java_object().getRealizedCapabilities(), Capability)
    def get_realized_capability_realizations(self):
        return create_e_list(self.get_java_object().getRealizedCapabilityRealizations(), CapabilityRealization)
    def get_realizing_capability_realizations(self):
        return create_e_list(self.get_java_object().getRealizingCapabilityRealizations(), CapabilityRealization)
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
    def get_owned_capability_realizations(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizations(), CapabilityRealization)
    def get_owned_capability_realization_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizationPkgs(), CapabilityRealizationPkg)

class SystemAnalysisRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "SystemAnalysisRealization"))
        elif isinstance(java_object, SystemAnalysisRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ContextInterfaceRealization(InterfaceAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/1.4.0", "ContextInterfaceRealization"))
        elif isinstance(java_object, ContextInterfaceRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SharedPkg(ReuseableStructure, ModelRoot):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "SharedPkg"))
        elif isinstance(java_object, SharedPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class GenericPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/sharedmodel/1.4.0", "GenericPkg"))
        elif isinstance(java_object, GenericPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractActivity(AbstractBehavior, TraceableElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AbstractActivity"))
        elif isinstance(java_object, AbstractActivity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionSpecification(Namespace, AbstractActivity):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionSpecification"))
        elif isinstance(java_object, FunctionSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExchangeCategory(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeCategory"))
        elif isinstance(java_object, ExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchanges(self):
        return create_e_list(self.get_java_object().getExchanges(), FunctionalExchange)
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
    def get_exchanges(self):
        return create_e_list(self.get_java_object().getExchanges(), ExchangeSpecification)

class ExchangeContainment(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeContainment"))
        elif isinstance(java_object, ExchangeContainment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalExchangeSpecification(ExchangeSpecification):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeSpecification"))
        elif isinstance(java_object, FunctionalExchangeSpecification):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalChainInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainInvolvement"))
        elif isinstance(java_object, FunctionalChainInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalChainReference(FunctionalChainInvolvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainReference"))
        elif isinstance(java_object, FunctionalChainReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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
    def get_realized_function_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionPortRealizedFunctionPort", self)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionPortAllocatedExchangeItems", self)
    def get_realizing_function_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionPortRealizingFunctionPort", self)
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

class Pin(ObjectNode):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "Pin"))
        elif isinstance(java_object, Pin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class FunctionInputPort(FunctionPort, InputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionInputPort"))
        elif isinstance(java_object, FunctionInputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_incoming_exchange_items(self):
        return create_e_list(self.get_java_object().getIncomingExchangeItems(), ExchangeItem)
    def get_incoming_functional_exchanges(self):
        return create_e_list(self.get_java_object().getIncomingFunctionalExchanges(), FunctionalExchange)

class OutputPin(Pin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "OutputPin"))
        elif isinstance(java_object, OutputPin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionOutputPort(FunctionPort, OutputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionOutputPort"))
        elif isinstance(java_object, FunctionOutputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_outgoing_exchange_items(self):
        return create_e_list(self.get_java_object().getOutgoingExchangeItems(), ExchangeItem)
    def get_outgoing_functional_exchanges(self):
        return create_e_list(self.get_java_object().getOutgoingFunctionalExchanges(), FunctionalExchange)

class AbstractFunctionAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "AbstractFunctionAllocation"))
        elif isinstance(java_object, AbstractFunctionAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComponentFunctionalAllocation(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentFunctionalAllocation"))
        elif isinstance(java_object, ComponentFunctionalAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalChainRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalChainRealization"))
        elif isinstance(java_object, FunctionalChainRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExchangeSpecificationRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ExchangeSpecificationRealization"))
        elif isinstance(java_object, ExchangeSpecificationRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalExchangeRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchangeRealization"))
        elif isinstance(java_object, FunctionalExchangeRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionRealization(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionRealization"))
        elif isinstance(java_object, FunctionRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ActivityEdge(AbstractRelationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ActivityEdge"))
        elif isinstance(java_object, ActivityEdge):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_guard(self):
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.get_java_object().setGuard(value.get_java_object())

class ObjectFlow(ActivityEdge):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ObjectFlow"))
        elif isinstance(java_object, ObjectFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class FunctionalExchange(NamedElement, Relationship, InvolvedElement, ObjectFlow, AbstractEvent, AbstractEventOperation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "FunctionalExchange"))
        elif isinstance(java_object, FunctionalExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involving_functional_chains(self):
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_categories(self):
        return create_e_list(self.get_java_object().getCategories(), ExchangeCategory)
    def get_realized_functional_exchanges(self):
        return create_e_list(self.get_java_object().getRealizedFunctionalExchanges(), FunctionalExchange)
    def get_realizing_functional_exchanges(self):
        return create_e_list(self.get_java_object().getRealizingFunctionalExchanges(), FunctionalExchange)
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

class ComponentExchangeAllocation(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeAllocation"))
        elif isinstance(java_object, ComponentExchangeAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComponentExchangeCategory(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeCategory"))
        elif isinstance(java_object, ComponentExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchanges(self):
        return create_e_list(self.get_java_object().getExchanges(), ComponentExchange)
    def get_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CategoryComponentExchange", self)

class ComponentExchangeEnd(InformationsExchanger, CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeEnd"))
        elif isinstance(java_object, ComponentExchangeEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComponentExchangeFunctionalExchangeAllocation(AbstractFunctionAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeFunctionalExchangeAllocation"))
        elif isinstance(java_object, ComponentExchangeFunctionalExchangeAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocating_component_exchange(self):
        value =  self.get_java_object().getAllocatingComponentExchange()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class ComponentExchangeRealization(ExchangeSpecificationRealization):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentExchangeRealization"))
        elif isinstance(java_object, ComponentExchangeRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocating_component_exchange(self):
        value =  self.get_java_object().getAllocatingComponentExchange()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class ComponentPort(Port, InformationsExchanger, Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPort"))
        elif isinstance(java_object, ComponentPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_orientation(self):
        return self.get_java_object().getOrientation().getName()
    def set_orientation(self, value):
        self.get_java_object().setOrientation(value)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_component_exchanges(self):
        return create_e_list(self.get_java_object().getComponentExchanges(), ComponentExchange)
    def get_allocated_function_ports(self):
        return create_e_list(self.get_java_object().getAllocatedFunctionPorts(), FunctionPort)
    def get_allocating_physical_ports(self):
        return create_e_list(self.get_java_object().getAllocatingPhysicalPorts(), PhysicalPort)
    def get_realized_component_ports(self):
        return create_e_list(self.get_java_object().getRealizedComponentPorts(), ComponentPort)
    def get_realizing_component_ports(self):
        return create_e_list(self.get_java_object().getRealizingComponentPorts(), ComponentPort)
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

class ComponentPortAllocationEnd(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ComponentPortAllocationEnd"))
        elif isinstance(java_object, ComponentPortAllocationEnd):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ReferenceHierarchyContext(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ReferenceHierarchyContext"))
        elif isinstance(java_object, ReferenceHierarchyContext):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_exchange_context(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvmentLinkExchangeContext", self)

class SequenceLink(CapellaElement, ReferenceHierarchyContext):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "SequenceLink"))
        elif isinstance(java_object, SequenceLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_links(self):
        return create_e_list(self.get_java_object().getLinks(), FunctionalChainInvolvementLink)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_condition(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceLinkCondition", self)
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
    def get_owner(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElementOwner", self)
    def get_outgoing_involvement_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementFunctionOutgoingInvolvementLinks", self)
    def get_incoming_involvement_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementFunctionIncomingInvolvementLinks", self)

class ControlNode(SequenceLinkEnd):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/1.4.0", "ControlNode"))
        elif isinstance(java_object, ControlNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)

class AbstractParameterSet(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "AbstractParameterSet"))
        elif isinstance(java_object, AbstractParameterSet):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class IState(AbstractNamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/core/1.4.0", "IState"))
        elif isinstance(java_object, IState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
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

class GenericTrace(Trace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "GenericTrace"))
        elif isinstance(java_object, GenericTrace):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class TransfoLink(GenericTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TransfoLink"))
        elif isinstance(java_object, TransfoLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class JustificationLink(GenericTrace):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "JustificationLink"))
        elif isinstance(java_object, JustificationLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CapabilityRealizationInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "CapabilityRealizationInvolvement"))
        elif isinstance(java_object, CapabilityRealizationInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateMachine(CapellaElement, AbstractBehavior):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateMachine"))
        elif isinstance(java_object, StateMachine):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_regions(self):
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)

class Region(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "Region"))
        elif isinstance(java_object, Region):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_states(self):
        return create_e_list(self.get_java_object().getOwnedStates(), AbstractState)
    def get_owned_transitions(self):
        return create_e_list(self.get_java_object().getOwnedTransitions(), StateTransition)
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
    def get_outgoing(self):
        return create_e_list(self.get_java_object().getOutgoing(), StateTransition)
    def get_incoming(self):
        return create_e_list(self.get_java_object().getIncoming(), StateTransition)
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
    def get_owned_regions(self):
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)
    def get_entry(self):
        return create_e_list(self.get_java_object().getEntry(), AbstractEvent)
    def get_exit(self):
        return create_e_list(self.get_java_object().getExit(), AbstractEvent)
    def get_do_activity(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractStateModeDoActivity", self)
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

class FinalState(State):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "FinalState"))
        elif isinstance(java_object, FinalState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateTransition(NamedElement, Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransition"))
        elif isinstance(java_object, StateTransition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)
    def get_trigger_description(self):
        return self.get_java_object().getTriggerDescription()
    def set_trigger_description(self, value):
        self.get_java_object().setTriggerDescription(value)
    def get_guard(self):
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.get_java_object().setGuard(value.get_java_object())
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_realized_state_transitions(self):
        return create_e_list(self.get_java_object().getRealizedStateTransitions(), StateTransition)
    def get_realizing_state_transitions(self):
        return create_e_list(self.get_java_object().getRealizingStateTransitions(), StateTransition)
    def get_effect(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateTransitionEffect", self)
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

class JoinPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "JoinPseudoState"))
        elif isinstance(java_object, JoinPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ForkPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ForkPseudoState"))
        elif isinstance(java_object, ForkPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ChoicePseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ChoicePseudoState"))
        elif isinstance(java_object, ChoicePseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class TerminatePseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TerminatePseudoState"))
        elif isinstance(java_object, TerminatePseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractStateRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "AbstractStateRealization"))
        elif isinstance(java_object, AbstractStateRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateTransitionRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateTransitionRealization"))
        elif isinstance(java_object, StateTransitionRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ShallowHistoryPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ShallowHistoryPseudoState"))
        elif isinstance(java_object, ShallowHistoryPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DeepHistoryPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "DeepHistoryPseudoState"))
        elif isinstance(java_object, DeepHistoryPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EntryPointPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "EntryPointPseudoState"))
        elif isinstance(java_object, EntryPointPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ExitPointPseudoState(Pseudostate):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ExitPointPseudoState"))
        elif isinstance(java_object, ExitPointPseudoState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateEventRealization(Allocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateEventRealization"))
        elif isinstance(java_object, StateEventRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StateEvent(NamedElement, AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "StateEvent"))
        elif isinstance(java_object, StateEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ChangeEvent(StateEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "ChangeEvent"))
        elif isinstance(java_object, ChangeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)

class TimeEvent(StateEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/1.4.0", "TimeEvent"))
        elif isinstance(java_object, TimeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        return self.get_java_object().getKind().getName()
    def set_kind(self, value):
        self.get_java_object().setKind(value)

class ExceptionHandler(ModelElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ExceptionHandler"))
        elif isinstance(java_object, ExceptionHandler):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class InterruptibleActivityRegion(ActivityGroup):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "InterruptibleActivityRegion"))
        elif isinstance(java_object, InterruptibleActivityRegion):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ControlFlow(ActivityEdge):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ControlFlow"))
        elif isinstance(java_object, ControlFlow):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StructuredActivityNode(ActivityGroup, AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "StructuredActivityNode"))
        elif isinstance(java_object, StructuredActivityNode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AcceptEventAction(AbstractAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "AcceptEventAction"))
        elif isinstance(java_object, AcceptEventAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SendSignalAction(InvocationAction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "SendSignalAction"))
        elif isinstance(java_object, SendSignalAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())

class ValuePin(InputPin):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/1.4.0", "ValuePin"))
        elif isinstance(java_object, ValuePin):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_value(self):
        value =  self.get_java_object().getValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_value(self, value):
        return self.get_java_object().setValue(value.get_java_object())

class SystemAnalysis(ComponentArchitecture):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemAnalysis"))
        elif isinstance(java_object, SystemAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_system_component_pkg(self):
        value =  self.get_java_object().getOwnedSystemComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_system_component_pkg(self, value):
        return self.get_java_object().setOwnedSystemComponentPkg(value.get_java_object())
    def get_mission_pkg(self):
        value =  self.get_java_object().getOwnedMissionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_mission_pkg(self, value):
        return self.get_java_object().setOwnedMissionPkg(value.get_java_object())
    def get_capability_pkg(self):
        value =  self.get_java_object().getContainedCapabilityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def get_system_function_pkg(self):
        value =  self.get_java_object().getContainedSystemFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)

class SystemFunction(AbstractFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunction"))
        elif isinstance(java_object, SystemFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_realized_operational_activities(self):
        return create_e_list(self.get_java_object().getRealizedOperationalActivities(), OperationalActivity)
    def get_realizing_logical_functions(self):
        return create_e_list(self.get_java_object().getRealizingLogicalFunctions(), LogicalFunction)
    def get_contained_system_functions(self):
        return create_e_list(self.get_java_object().getContainedSystemFunctions(), SystemFunction)
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

class SystemFunctionPkg(FunctionPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemFunctionPkg"))
        elif isinstance(java_object, SystemFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_functions(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctions(), SystemFunction)
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)

class SystemCommunicationHook(NamedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunicationHook"))
        elif isinstance(java_object, SystemCommunicationHook):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class SystemCommunication(Relationship):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemCommunication"))
        elif isinstance(java_object, SystemCommunication):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CapabilityInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityInvolvement"))
        elif isinstance(java_object, CapabilityInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class MissionInvolvement(Involvement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionInvolvement"))
        elif isinstance(java_object, MissionInvolvement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Mission(NamedElement, InvolverElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "Mission"))
        elif isinstance(java_object, Mission):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exploited_capabilities(self):
        return create_e_list(self.get_java_object().getExploitedCapabilities(), Capability)
    def get_involved_system_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Mission_InvolvedSystemComponents", self)

class MissionPkg(Structure):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "MissionPkg"))
        elif isinstance(java_object, MissionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_mission_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedMissionPkgs(), MissionPkg)
    def get_owned_missions(self):
        return create_e_list(self.get_java_object().getOwnedMissions(), Mission)

class Capability(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "Capability"))
        elif isinstance(java_object, Capability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_purpose_missions(self):
        return create_e_list(self.get_java_object().getPurposeMissions(), Mission)
    def get_realized_operational_capabilities(self):
        return create_e_list(self.get_java_object().getRealizedOperationalCapabilities(), OperationalCapability)
    def get_realizing_capability_realizations(self):
        return create_e_list(self.get_java_object().getRealizingCapabilityRealizations(), CapabilityRealization)
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
    def get_involved_element(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsCapabilityExploitationTarget", self)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaRelationshipsCapabilityExploitationSource", self)

class CapabilityPkg(AbstractCapabilityPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "CapabilityPkg"))
        elif isinstance(java_object, CapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_capabilities(self):
        return create_e_list(self.get_java_object().getOwnedCapabilities(), Capability)
    def get_owned_capability_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityPkgs(), CapabilityPkg)

class OperationalAnalysisRealization(ArchitectureAllocation):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "OperationalAnalysisRealization"))
        elif isinstance(java_object, OperationalAnalysisRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemComponentPkg(ComponentPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponentPkg"))
        elif isinstance(java_object, SystemComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemComponentPkgs(), SystemComponentPkg)

class SystemComponent(Component, InvolvedElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/1.4.0", "SystemComponent"))
        elif isinstance(java_object, SystemComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemComponentPkgs(), SystemComponentPkg)
    def get_involving_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_involving_missions(self):
        return create_e_list(self.get_java_object().getInvolvingMissions(), Mission)
    def get_allocated_system_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_AllocatedFunctions", self)
    def get_realized_operational_entities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizedComponents", self)
    def get_realizing_logical_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Component_RealizingComponents", self)

class LibraryAbstractElement(ExtensibleElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryAbstractElement"))
        elif isinstance(java_object, LibraryAbstractElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getId()
    def set_id(self, value):
        self.get_java_object().setId(value)

class ModelInformation(LibraryAbstractElement, ElementExtension):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelInformation"))
        elif isinstance(java_object, ModelInformation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LibraryReference(LibraryAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "LibraryReference"))
        elif isinstance(java_object, LibraryReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ModelVersion(LibraryAbstractElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/libraries/1.4.0", "ModelVersion"))
        elif isinstance(java_object, ModelVersion):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
