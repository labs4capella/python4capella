package org.eclipse.python4capella.gen.handlers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringJoiner;
import java.util.stream.Collectors;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.ui.handlers.HandlerUtil;
import org.polarsys.capella.core.data.capellacore.Feature;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.capellacore.TypedElement;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.DataPkg;
import org.polarsys.capella.core.data.information.Operation;
import org.polarsys.capella.core.data.information.Parameter;
import org.polarsys.capella.core.data.information.ParameterDirection;
import org.polarsys.capella.core.data.information.Property;
import org.polarsys.capella.core.data.information.datavalue.LiteralNumericValue;
import org.polarsys.capella.core.data.information.datavalue.NumericValue;

public class ProduceCapellaPythonTestsFromCapellaHandler extends AbstractHandler {

	/**
	 * The new line separator.
	 */
	private static final String NL = System.lineSeparator();

	private Map<Class, Class> concreteClass = new HashMap<Class, Class>();

	private final List<EPackage> ePackages = initEPackages();

	private Set<String> queries = initQueryNames();

	private Set<String> readOnlyTests = initReadOnlyTests();

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		DataPkg root = (DataPkg) ((IStructuredSelection) HandlerUtil.getCurrentSelection(event)).getFirstElement();

		for (DataPkg pkg : root.getOwnedDataPkgs()) {
			for (Class cls : pkg.getOwnedClasses()) {
				if (!cls.isAbstract()) {
					concreteClass.put(cls, cls);
					for (Class superCls : getAllSuperClasses(cls)) {
						if (superCls.isAbstract()) {
							concreteClass.put(superCls, cls);
						}
					}
				}
			}
		}

		final File file = new File("/tmp/capella/" + "capella" + "_tests.py");
		try {
			if (!file.exists()) {
				file.getParentFile().mkdirs();
				file.createNewFile();
			}
			try (OutputStream os = new FileOutputStream(file)) {
				os.write(getHeader(root, "capella").getBytes());
				for (DataPkg pkg : root.getOwnedDataPkgs()) {
					for (Class cls : pkg.getOwnedClasses()) {
						if (!cls.isAbstract()) {
							final Set<Feature> allFeatures = getAllFeatures(cls);
							for (Feature feature : allFeatures) {
								os.write(getTest(cls, feature).getBytes());
							}
						}
					}
				}
				os.write(getTestAdditions("capella").getBytes());
				os.write(NL.getBytes());
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return null;
	}

	private String getTestAdditions(String pkgName) {
		String res = "";

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/additions/tests/" + pkgName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));

		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private Set<String> initReadOnlyTests() {
		final Set<String> res = new HashSet<>();

		res.add("test_CapabilityPkg_constraints");
		res.add("test_CapabilityRealizationPkg_constraints");
		res.add("test_CapabilityRealization_constraints");
		res.add("test_CapabilityRealization_sub");
		res.add("test_CapabilityRealization_super");
		res.add("test_Capability_constraints");
		res.add("test_Capability_purpose_missions");
		res.add("test_Capability_sub");
		res.add("test_Capability_super");
		res.add("test_CommunicationMean_constraints");
		res.add("test_CommunicationMean_realizing_component_exchanges");
		res.add("test_ComponentExchangeCategory_constraints");
		res.add("test_ComponentExchange_constraints");
		res.add("test_ComponentExchange_realized_component_exchanges");
		res.add("test_ComponentPort_component_exchanges");
		res.add("test_ComponentPort_constraints");
		res.add("test_ConfigurationItemPkg_constraints");
		res.add("test_ConfigurationItem_allocated_physical_artifacts");
		res.add("test_ConfigurationItem_constraints");
		res.add("test_Constraint_constraints");
		res.add("test_EPBSArchitecture_constraints");
		res.add("test_EntityPkg_constraints");
		res.add("test_EnumerationPropertyLiteral_constraints");
		res.add("test_EnumerationPropertyType_constraints");
		res.add("test_ExchangeCategory_constraints");
		res.add("test_ExchangeItemElement_constraints");
		res.add("test_ExchangeItem_allocator_interfaces");
		res.add("test_ExchangeItem_constraints");
		res.add("test_ExchangeItem_sub");
		res.add("test_ExchangeItem_super");
		res.add("test_FunctionInputPort_constraints");
		res.add("test_FunctionInputPort_incoming_functional_exchanges");
		res.add("test_FunctionOutputPort_constraints");
		res.add("test_FunctionOutputPort_outgoing_functional_exchanges");
		res.add("test_FunctionalChain_constraints");
		res.add("test_FunctionalChain_involved_functional_exchanges");
		res.add("test_FunctionalExchange_constraints");
		res.add("test_FunctionalExchange_involving_functional_chains");
		res.add("test_FunctionalExchange_realized_functional_exchanges");
		res.add("test_InterfacePkg_constraints");
		res.add("test_Interface_constraints");
		res.add("test_Interface_providing_component_ports");
		res.add("test_Interface_requiring_component_ports");
		res.add("test_Interface_sub");
		res.add("test_Interface_super");
		res.add("test_LogicalArchitecture_constraints");
		res.add("test_LogicalComponentPkg_constraints");
		res.add("test_LogicalComponent_allocated_functions");
		res.add("test_LogicalComponent_constraints");
		res.add("test_LogicalComponent_contained_component_ports");
		res.add("test_LogicalComponent_implemented_interfaces");
		res.add("test_LogicalComponent_used_interfaces");
		res.add("test_LogicalFunctionPkg_constraints");
		res.add("test_LogicalFunction_constraints");
		res.add("test_LogicalFunction_contained_logical_functions");
		res.add("test_LogicalFunction_incoming");
		res.add("test_LogicalFunction_involving_capabilities");
		res.add("test_LogicalFunction_involving_functional_chains");
		res.add("test_LogicalFunction_outgoing");
		res.add("test_MissionPkg_constraints");
		res.add("test_Mission_constraints");
		res.add("test_Mode_constraints");
		res.add("test_Mode_incoming");
		res.add("test_Mode_outgoing");
		res.add("test_OperationalActivityPkg_constraints");
		res.add("test_OperationalActivity_constraints");
		res.add("test_OperationalActivity_contained_operational_activities");
		res.add("test_OperationalAnalysis_constraints");
		res.add("test_OperationalCapabilityPkg_constraints");
		res.add("test_OperationalCapability_constraints");
		res.add("test_OperationalCapability_sub");
		res.add("test_OperationalCapability_super");
		res.add("test_OperationalProcess_constraints");
		res.add("test_OperationalProcess_realizing_functional_chains");
		res.add("test_PhysicalArchitecture_constraints");
		res.add("test_PhysicalComponentPkg_constraints");
		res.add("test_PhysicalFunctionPkg_constraints");
		res.add("test_PhysicalFunction_constraints");
		res.add("test_PhysicalFunction_contained_physical_functions");
		res.add("test_PhysicalFunction_incoming");
		res.add("test_PhysicalFunction_involving_capabilities");
		res.add("test_PhysicalFunction_involving_functional_chains");
		res.add("test_PhysicalFunction_outgoing");
		res.add("test_PhysicalLinkCategory_constraints");
		res.add("test_PhysicalLink_constraints");
		res.add("test_PhysicalLink_realized_physical_links");
		res.add("test_PhysicalLink_realizing_physical_links");
		res.add("test_PhysicalPath_constraints");
		res.add("test_PhysicalPort_constraints");
		res.add("test_PhysicalPort_realized_physical_ports");
		res.add("test_PhysicalPort_realizing_physical_ports");
		res.add("test_PropertyValueGroup_constraints");
		res.add("test_PropertyValuePkg_constraints");
		res.add("test_Region_constraints");
		res.add("test_Scenario_constraints");
		res.add("test_Scenario_referenced_scenarios");
		res.add("test_StateMachine_constraints");
		res.add("test_StateTransition_constraints");
		res.add("test_StateTransition_realized_state_transitions");
		res.add("test_StateTransition_realizing_state_transitions");
		res.add("test_State_constraints");
		res.add("test_State_incoming");
		res.add("test_State_outgoing");
		res.add("test_SystemAnalysis_constraints");
		res.add("test_SystemComponentPkg_constraints");
		res.add("test_SystemEngineering_constraints");
		res.add("test_SystemFunctionPkg_constraints");
		res.add("test_SystemFunction_constraints");
		res.add("test_SystemFunction_contained_system_functions");
		res.add("test_SystemFunction_incoming");
		res.add("test_SystemFunction_involving_functional_chains");
		res.add("test_SystemFunction_outgoing");
		res.add("test_ChangeEvent_constraints");
		res.add("test_CombinedFragment_constraints");
		res.add("test_ConstraintDuration_constraints");
		res.add("test_ExchangeItemAllocation_constraints");
		res.add("test_InstanceRole_constraints");
		res.add("test_SequenceMessage_constraints");
		res.add("test_StateFragment_constraints");
		res.add("test_TimeEvent_constraints");
		res.add("test_ComponentExchange_invoking_sequence_messages");
		res.add("test_ExchangeItemAllocation_invoking_sequence_messages");
		res.add("test_FunctionalExchange_invoking_sequence_messages");
		res.add("test_LogicalComponent_involving_capability_realizations");
		res.add("test_Mode_available_capabilities");
		res.add("test_Mode_available_functional_chains");
		res.add("test_PhysicalLink_allocator_configuration_items");
		res.add("test_PhysicalPath_realized_physical_paths");
		res.add("test_PhysicalPath_realizing_physical_paths");
		res.add("test_PhysicalPort_allocator_configuration_items");
		res.add("test_State_available_capabilities");
		res.add("test_State_available_functional_chains");
		res.add("test_CapabilityRealization_extended_capabilities");
		res.add("test_CapabilityRealization_extending_capabilities");
		res.add("test_CapabilityRealization_included_capabilities");
		res.add("test_CapabilityRealization_including_capabilities");
		res.add("test_Capability_extended_capabilities");
		res.add("test_Capability_extending_capabilities");
		res.add("test_Capability_included_capabilities");
		res.add("test_Capability_including_capabilities");
		res.add("test_LogicalComponent_incoming_component_exchanges");
		res.add("test_LogicalComponent_outgoing_component_exchanges");
		res.add("test_OperationalCapability_extended_capabilities");
		res.add("test_OperationalCapability_extending_capabilities");
		res.add("test_OperationalCapability_included_capabilities");
		res.add("test_OperationalCapability_including_capabilities");
		res.add("test_BooleanType_constraints");
		res.add("test_BooleanType_sub");
		res.add("test_BooleanType_super");
		res.add("test_Class_contained_properties");
		res.add("test_Enumeration_constraints");
		res.add("test_Enumeration_sub");
		res.add("test_Enumeration_super");
		res.add("test_NumericType_constraints");
		res.add("test_NumericType_sub");
		res.add("test_NumericType_super");
		res.add("test_PhysicalQuantity_constraints");
		res.add("test_PhysicalQuantity_sub");
		res.add("test_PhysicalQuantity_super");
		res.add("test_StringType_constraints");
		res.add("test_StringType_sub");
		res.add("test_StringType_super");
		res.add("test_Union_contained_union_properties");
		res.add("test_Unit_constraints");
		res.add("test_Diagram_type");
		res.add("test_Diagram_package");
		res.add("test_Attribute_owned_diagrams");
		res.add("test_BehaviorPC_owned_diagrams");
		res.add("test_BooleanType_owned_diagrams");
		res.add("test_CapabilityPkg_owned_diagrams");
		res.add("test_CapabilityRealizationPkg_owned_diagrams");
		res.add("test_CapabilityRealization_owned_diagrams");
		res.add("test_Capability_owned_diagrams");
		res.add("test_CapellaModule_owned_diagrams");
		res.add("test_CatalogElementPkg_owned_diagrams");
		res.add("test_ChangeEvent_owned_diagrams");
		res.add("test_CombinedFragment_owned_diagrams");
		res.add("test_CommunicationMean_owned_diagrams");
		res.add("test_CompliancyDefinitionPkg_owned_diagrams");
		res.add("test_CompliancyDefinition_owned_diagrams");
		res.add("test_ComponentExchangeCategory_owned_diagrams");
		res.add("test_ComponentExchange_owned_diagrams");
		res.add("test_ComponentPort_owned_diagrams");
		res.add("test_ConfigurationItemPkg_owned_diagrams");
		res.add("test_ConfigurationItem_owned_diagrams");
		res.add("test_ConstraintDuration_owned_diagrams");
		res.add("test_Constraint_owned_diagrams");
		res.add("test_EPBSArchitecture_owned_diagrams");
		res.add("test_EntityPkg_owned_diagrams");
		res.add("test_EnumerationPropertyLiteral_owned_diagrams");
		res.add("test_EnumerationPropertyType_owned_diagrams");
		res.add("test_Enumeration_owned_diagrams");
		res.add("test_ExchangeCategory_owned_diagrams");
		res.add("test_ExchangeItemAllocation_owned_diagrams");
		res.add("test_ExchangeItemElement_owned_diagrams");
		res.add("test_ExchangeItem_owned_diagrams");
		res.add("test_Folder_owned_diagrams");
		res.add("test_FunctionInputPort_owned_diagrams");
		res.add("test_FunctionOutputPort_owned_diagrams");
		res.add("test_FunctionalChain_owned_diagrams");
		res.add("test_FunctionalExchange_owned_diagrams");
		res.add("test_InstanceRole_owned_diagrams");
		res.add("test_Interaction_owned_diagrams");
		res.add("test_InterfacePkg_owned_diagrams");
		res.add("test_Interface_owned_diagrams");
		res.add("test_LogicalActor_owned_diagrams");
		res.add("test_LogicalArchitecture_owned_diagrams");
		res.add("test_LogicalComponentPkg_owned_diagrams");
		res.add("test_LogicalComponent_owned_diagrams");
		res.add("test_LogicalFunctionPkg_owned_diagrams");
		res.add("test_LogicalFunction_owned_diagrams");
		res.add("test_LogicalSystem_owned_diagrams");
		res.add("test_MissionPkg_owned_diagrams");
		res.add("test_Mission_owned_diagrams");
		res.add("test_Mode_owned_diagrams");
		res.add("test_NodePC_owned_diagrams");
		res.add("test_NumericType_owned_diagrams");
		res.add("test_Operand_owned_diagrams");
		res.add("test_OperationalActivityPkg_owned_diagrams");
		res.add("test_OperationalActivity_owned_diagrams");
		res.add("test_OperationalActor_owned_diagrams");
		res.add("test_OperationalAnalysis_owned_diagrams");
		res.add("test_OperationalCapabilityPkg_owned_diagrams");
		res.add("test_OperationalCapability_owned_diagrams");
		res.add("test_OperationalEntity_owned_diagrams");
		res.add("test_OperationalProcess_owned_diagrams");
		res.add("test_PhysicalActor_owned_diagrams");
		res.add("test_PhysicalArchitecture_owned_diagrams");
		res.add("test_PhysicalComponentPkg_owned_diagrams");
		res.add("test_PhysicalFunctionPkg_owned_diagrams");
		res.add("test_PhysicalFunction_owned_diagrams");
		res.add("test_PhysicalLinkCategory_owned_diagrams");
		res.add("test_PhysicalLink_owned_diagrams");
		res.add("test_PhysicalPath_owned_diagrams");
		res.add("test_PhysicalPort_owned_diagrams");
		res.add("test_PhysicalQuantity_owned_diagrams");
		res.add("test_PhysicalSystem_owned_diagrams");
		res.add("test_PropertyValueGroup_owned_diagrams");
		res.add("test_PropertyValuePkg_owned_diagrams");
		res.add("test_PropertyValue_owned_diagrams");
		res.add("test_Pseudostate_owned_diagrams");
		res.add("test_REC_owned_diagrams");
		res.add("test_RPL_owned_diagrams");
		res.add("test_RecCatalog_owned_diagrams");
		res.add("test_Region_owned_diagrams");
		res.add("test_Requirement_owned_diagrams");
		res.add("test_Scenario_owned_diagrams");
		res.add("test_SequenceMessage_owned_diagrams");
		res.add("test_StateFragment_owned_diagrams");
		res.add("test_StateMachine_owned_diagrams");
		res.add("test_StateTransition_owned_diagrams");
		res.add("test_State_owned_diagrams");
		res.add("test_StringType_owned_diagrams");
		res.add("test_SystemActor_owned_diagrams");
		res.add("test_SystemAnalysis_owned_diagrams");
		res.add("test_SystemComponentPkg_owned_diagrams");
		res.add("test_SystemEngineering_owned_diagrams");
		res.add("test_SystemFunctionPkg_owned_diagrams");
		res.add("test_SystemFunction_owned_diagrams");
		res.add("test_System_owned_diagrams");
		res.add("test_TimeEvent_owned_diagrams");
		res.add("test_Unit_owned_diagrams");
		res.add("test_Diagram_represented_elements");

		res.add("test_SystemEngineering_rec_catalogs");
		res.add("test_SystemEngineering_operational_analysis");
		res.add("test_SystemEngineering_system_analysis");
		res.add("test_SystemEngineering_logical_architecture");
		res.add("test_SystemEngineering_physical_architecture");
		res.add("test_SystemEngineering_e_p_b_s_architecture");

		res.add("test_BooleanType_contextual_element_for_diagrams");
		res.add("test_CapabilityPkg_contextual_element_for_diagrams");
		res.add("test_CapabilityRealizationPkg_contextual_element_for_diagrams");
		res.add("test_CapabilityRealization_contextual_element_for_diagrams");
		res.add("test_Capability_contextual_element_for_diagrams");
		res.add("test_CapellaModule_contextual_element_for_diagrams");
		res.add("test_CatalogElementPkg_contextual_element_for_diagrams");
		res.add("test_ChangeEvent_contextual_element_for_diagrams");
		res.add("test_CombinedFragment_contextual_element_for_diagrams");
		res.add("test_CommunicationMean_contextual_element_for_diagrams");
		res.add("test_CompliancyDefinitionPkg_contextual_element_for_diagrams");
		res.add("test_CompliancyDefinition_contextual_element_for_diagrams");
		res.add("test_ComponentExchangeCategory_contextual_element_for_diagrams");
		res.add("test_ComponentExchange_contextual_element_for_diagrams");
		res.add("test_ComponentPort_contextual_element_for_diagrams");
		res.add("test_ConfigurationItemPkg_contextual_element_for_diagrams");
		res.add("test_ConfigurationItem_contextual_element_for_diagrams");
		res.add("test_ConstraintDuration_contextual_element_for_diagrams");
		res.add("test_Constraint_contextual_element_for_diagrams");
		res.add("test_EPBSArchitecture_contextual_element_for_diagrams");
		res.add("test_EntityPkg_contextual_element_for_diagrams");
		res.add("test_EnumerationPropertyLiteral_contextual_element_for_diagrams");
		res.add("test_EnumerationPropertyType_contextual_element_for_diagrams");
		res.add("test_Enumeration_contextual_element_for_diagrams");
		res.add("test_ExchangeCategory_contextual_element_for_diagrams");
		res.add("test_ExchangeItemAllocation_contextual_element_for_diagrams");
		res.add("test_ExchangeItemElement_contextual_element_for_diagrams");
		res.add("test_ExchangeItem_contextual_element_for_diagrams");
		res.add("test_Folder_contextual_element_for_diagrams");
		res.add("test_FunctionInputPort_contextual_element_for_diagrams");
		res.add("test_FunctionOutputPort_contextual_element_for_diagrams");
		res.add("test_FunctionalChain_contextual_element_for_diagrams");
		res.add("test_FunctionalExchange_contextual_element_for_diagrams");
		res.add("test_InstanceRole_contextual_element_for_diagrams");
		res.add("test_InterfacePkg_contextual_element_for_diagrams");
		res.add("test_Interface_contextual_element_for_diagrams");
		res.add("test_LogicalArchitecture_contextual_element_for_diagrams");
		res.add("test_LogicalComponentPkg_contextual_element_for_diagrams");
		res.add("test_LogicalComponent_contextual_element_for_diagrams");
		res.add("test_LogicalFunctionPkg_contextual_element_for_diagrams");
		res.add("test_LogicalFunction_contextual_element_for_diagrams");
		res.add("test_MissionPkg_contextual_element_for_diagrams");
		res.add("test_Mission_contextual_element_for_diagrams");
		res.add("test_Mode_contextual_element_for_diagrams");
		res.add("test_NumericType_contextual_element_for_diagrams");
		res.add("test_OperationalActivityPkg_contextual_element_for_diagrams");
		res.add("test_OperationalActivity_contextual_element_for_diagrams");
		res.add("test_OperationalAnalysis_contextual_element_for_diagrams");
		res.add("test_OperationalCapabilityPkg_contextual_element_for_diagrams");
		res.add("test_OperationalCapability_contextual_element_for_diagrams");
		res.add("test_OperationalProcess_contextual_element_for_diagrams");
		res.add("test_PhysicalArchitecture_contextual_element_for_diagrams");
		res.add("test_PhysicalComponentPkg_contextual_element_for_diagrams");
		res.add("test_PhysicalFunctionPkg_contextual_element_for_diagrams");
		res.add("test_PhysicalFunction_contextual_element_for_diagrams");
		res.add("test_PhysicalLinkCategory_contextual_element_for_diagrams");
		res.add("test_PhysicalLink_contextual_element_for_diagrams");
		res.add("test_PhysicalPath_contextual_element_for_diagrams");
		res.add("test_PhysicalPort_contextual_element_for_diagrams");
		res.add("test_PhysicalQuantity_contextual_element_for_diagrams");
		res.add("test_PropertyValueGroup_contextual_element_for_diagrams");
		res.add("test_PropertyValuePkg_contextual_element_for_diagrams");
		res.add("test_RecCatalog_contextual_element_for_diagrams");
		res.add("test_Region_contextual_element_for_diagrams");
		res.add("test_Requirement_contextual_element_for_diagrams");
		res.add("test_Scenario_contextual_element_for_diagrams");
		res.add("test_SequenceMessage_contextual_element_for_diagrams");
		res.add("test_StateFragment_contextual_element_for_diagrams");
		res.add("test_StateMachine_contextual_element_for_diagrams");
		res.add("test_StateTransition_contextual_element_for_diagrams");
		res.add("test_State_contextual_element_for_diagrams");
		res.add("test_StringType_contextual_element_for_diagrams");
		res.add("test_SystemAnalysis_contextual_element_for_diagrams");
		res.add("test_SystemComponentPkg_contextual_element_for_diagrams");
		res.add("test_SystemEngineering_contextual_element_for_diagrams");
		res.add("test_SystemFunctionPkg_contextual_element_for_diagrams");
		res.add("test_SystemFunction_contextual_element_for_diagrams");
		res.add("test_TimeEvent_contextual_element_for_diagrams");
		res.add("test_Unit_contextual_element_for_diagrams");

		res.add("test_BooleanType_representing_diagrams");
		res.add("test_CapabilityPkg_representing_diagrams");
		res.add("test_CapabilityRealizationPkg_representing_diagrams");
		res.add("test_CapabilityRealization_representing_diagrams");
		res.add("test_Capability_representing_diagrams");
		res.add("test_CapellaModule_representing_diagrams");
		res.add("test_CatalogElementPkg_representing_diagrams");
		res.add("test_ChangeEvent_representing_diagrams");
		res.add("test_CombinedFragment_representing_diagrams");
		res.add("test_CommunicationMean_representing_diagrams");
		res.add("test_CompliancyDefinitionPkg_representing_diagrams");
		res.add("test_CompliancyDefinition_representing_diagrams");
		res.add("test_ComponentExchangeCategory_representing_diagrams");
		res.add("test_ComponentExchange_representing_diagrams");
		res.add("test_ComponentPort_representing_diagrams");
		res.add("test_ConfigurationItemPkg_representing_diagrams");
		res.add("test_ConfigurationItem_representing_diagrams");
		res.add("test_ConstraintDuration_representing_diagrams");
		res.add("test_Constraint_representing_diagrams");
		res.add("test_EPBSArchitecture_representing_diagrams");
		res.add("test_EntityPkg_representing_diagrams");
		res.add("test_EnumerationPropertyLiteral_representing_diagrams");
		res.add("test_EnumerationPropertyType_representing_diagrams");
		res.add("test_Enumeration_representing_diagrams");
		res.add("test_ExchangeCategory_representing_diagrams");
		res.add("test_ExchangeItemAllocation_representing_diagrams");
		res.add("test_ExchangeItemElement_representing_diagrams");
		res.add("test_ExchangeItem_representing_diagrams");
		res.add("test_Folder_representing_diagrams");
		res.add("test_FunctionInputPort_representing_diagrams");
		res.add("test_FunctionOutputPort_representing_diagrams");
		res.add("test_FunctionalChain_representing_diagrams");
		res.add("test_FunctionalExchange_representing_diagrams");
		res.add("test_InstanceRole_representing_diagrams");
		res.add("test_InterfacePkg_representing_diagrams");
		res.add("test_Interface_representing_diagrams");
		res.add("test_LogicalArchitecture_representing_diagrams");
		res.add("test_LogicalComponentPkg_representing_diagrams");
		res.add("test_LogicalComponent_representing_diagrams");
		res.add("test_LogicalFunctionPkg_representing_diagrams");
		res.add("test_LogicalFunction_representing_diagrams");
		res.add("test_MissionPkg_representing_diagrams");
		res.add("test_Mission_representing_diagrams");
		res.add("test_Mode_representing_diagrams");
		res.add("test_NumericType_representing_diagrams");
		res.add("test_OperationalActivityPkg_representing_diagrams");
		res.add("test_OperationalActivity_representing_diagrams");
		res.add("test_OperationalAnalysis_representing_diagrams");
		res.add("test_OperationalCapabilityPkg_representing_diagrams");
		res.add("test_OperationalCapability_representing_diagrams");
		res.add("test_OperationalProcess_representing_diagrams");
		res.add("test_PhysicalArchitecture_representing_diagrams");
		res.add("test_PhysicalComponentPkg_representing_diagrams");
		res.add("test_PhysicalFunctionPkg_representing_diagrams");
		res.add("test_PhysicalFunction_representing_diagrams");
		res.add("test_PhysicalLinkCategory_representing_diagrams");
		res.add("test_PhysicalLink_representing_diagrams");
		res.add("test_PhysicalPath_representing_diagrams");
		res.add("test_PhysicalPort_representing_diagrams");
		res.add("test_PhysicalQuantity_representing_diagrams");
		res.add("test_PropertyValueGroup_representing_diagrams");
		res.add("test_PropertyValuePkg_representing_diagrams");
		res.add("test_RecCatalog_representing_diagrams");
		res.add("test_Region_representing_diagrams");
		res.add("test_Requirement_representing_diagrams");
		res.add("test_Scenario_representing_diagrams");
		res.add("test_SequenceMessage_representing_diagrams");
		res.add("test_StateFragment_representing_diagrams");
		res.add("test_StateMachine_representing_diagrams");
		res.add("test_StateTransition_representing_diagrams");
		res.add("test_State_representing_diagrams");
		res.add("test_StringType_representing_diagrams");
		res.add("test_SystemAnalysis_representing_diagrams");
		res.add("test_SystemComponentPkg_representing_diagrams");
		res.add("test_SystemEngineering_representing_diagrams");
		res.add("test_SystemFunctionPkg_representing_diagrams");
		res.add("test_SystemFunction_representing_diagrams");
		res.add("test_TimeEvent_representing_diagrams");
		res.add("test_Unit_representing_diagrams");

		res.add("test_BooleanType_element_of_interest_for_diagrams");
		res.add("test_CapabilityPkg_element_of_interest_for_diagrams");
		res.add("test_CapabilityRealizationPkg_element_of_interest_for_diagrams");
		res.add("test_CapabilityRealization_element_of_interest_for_diagrams");
		res.add("test_Capability_element_of_interest_for_diagrams");
		res.add("test_CapellaModule_element_of_interest_for_diagrams");
		res.add("test_CatalogElementPkg_element_of_interest_for_diagrams");
		res.add("test_ChangeEvent_element_of_interest_for_diagrams");
		res.add("test_CombinedFragment_element_of_interest_for_diagrams");
		res.add("test_CommunicationMean_element_of_interest_for_diagrams");
		res.add("test_CompliancyDefinitionPkg_element_of_interest_for_diagrams");
		res.add("test_CompliancyDefinition_element_of_interest_for_diagrams");
		res.add("test_ComponentExchangeCategory_element_of_interest_for_diagrams");
		res.add("test_ComponentExchange_element_of_interest_for_diagrams");
		res.add("test_ComponentPort_element_of_interest_for_diagrams");
		res.add("test_ConfigurationItemPkg_element_of_interest_for_diagrams");
		res.add("test_ConfigurationItem_element_of_interest_for_diagrams");
		res.add("test_ConstraintDuration_element_of_interest_for_diagrams");
		res.add("test_Constraint_element_of_interest_for_diagrams");
		res.add("test_EPBSArchitecture_element_of_interest_for_diagrams");
		res.add("test_EntityPkg_element_of_interest_for_diagrams");
		res.add("test_EnumerationPropertyLiteral_element_of_interest_for_diagrams");
		res.add("test_EnumerationPropertyType_element_of_interest_for_diagrams");
		res.add("test_Enumeration_element_of_interest_for_diagrams");
		res.add("test_ExchangeCategory_element_of_interest_for_diagrams");
		res.add("test_ExchangeItemAllocation_element_of_interest_for_diagrams");
		res.add("test_ExchangeItemElement_element_of_interest_for_diagrams");
		res.add("test_ExchangeItem_element_of_interest_for_diagrams");
		res.add("test_Folder_element_of_interest_for_diagrams");
		res.add("test_FunctionInputPort_element_of_interest_for_diagrams");
		res.add("test_FunctionOutputPort_element_of_interest_for_diagrams");
		res.add("test_FunctionalChain_element_of_interest_for_diagrams");
		res.add("test_FunctionalExchange_element_of_interest_for_diagrams");
		res.add("test_InstanceRole_element_of_interest_for_diagrams");
		res.add("test_InterfacePkg_element_of_interest_for_diagrams");
		res.add("test_Interface_element_of_interest_for_diagrams");
		res.add("test_LogicalArchitecture_element_of_interest_for_diagrams");
		res.add("test_LogicalComponentPkg_element_of_interest_for_diagrams");
		res.add("test_LogicalComponent_element_of_interest_for_diagrams");
		res.add("test_LogicalFunctionPkg_element_of_interest_for_diagrams");
		res.add("test_LogicalFunction_element_of_interest_for_diagrams");
		res.add("test_MissionPkg_element_of_interest_for_diagrams");
		res.add("test_Mission_element_of_interest_for_diagrams");
		res.add("test_Mode_element_of_interest_for_diagrams");
		res.add("test_NumericType_element_of_interest_for_diagrams");
		res.add("test_OperationalActivityPkg_element_of_interest_for_diagrams");
		res.add("test_OperationalActivity_element_of_interest_for_diagrams");
		res.add("test_OperationalAnalysis_element_of_interest_for_diagrams");
		res.add("test_OperationalCapabilityPkg_element_of_interest_for_diagrams");
		res.add("test_OperationalCapability_element_of_interest_for_diagrams");
		res.add("test_OperationalProcess_element_of_interest_for_diagrams");
		res.add("test_PhysicalArchitecture_element_of_interest_for_diagrams");
		res.add("test_PhysicalComponentPkg_element_of_interest_for_diagrams");
		res.add("test_PhysicalFunctionPkg_element_of_interest_for_diagrams");
		res.add("test_PhysicalFunction_element_of_interest_for_diagrams");
		res.add("test_PhysicalLinkCategory_element_of_interest_for_diagrams");
		res.add("test_PhysicalLink_element_of_interest_for_diagrams");
		res.add("test_PhysicalPath_element_of_interest_for_diagrams");
		res.add("test_PhysicalPort_element_of_interest_for_diagrams");
		res.add("test_PhysicalQuantity_element_of_interest_for_diagrams");
		res.add("test_PropertyValueGroup_element_of_interest_for_diagrams");
		res.add("test_PropertyValuePkg_element_of_interest_for_diagrams");
		res.add("test_RecCatalog_element_of_interest_for_diagrams");
		res.add("test_Region_element_of_interest_for_diagrams");
		res.add("test_Requirement_element_of_interest_for_diagrams");
		res.add("test_Scenario_element_of_interest_for_diagrams");
		res.add("test_SequenceMessage_element_of_interest_for_diagrams");
		res.add("test_StateFragment_element_of_interest_for_diagrams");
		res.add("test_StateMachine_element_of_interest_for_diagrams");
		res.add("test_StateTransition_element_of_interest_for_diagrams");
		res.add("test_State_element_of_interest_for_diagrams");
		res.add("test_StringType_element_of_interest_for_diagrams");
		res.add("test_SystemAnalysis_element_of_interest_for_diagrams");
		res.add("test_SystemComponentPkg_element_of_interest_for_diagrams");
		res.add("test_SystemEngineering_element_of_interest_for_diagrams");
		res.add("test_SystemFunctionPkg_element_of_interest_for_diagrams");
		res.add("test_SystemFunction_element_of_interest_for_diagrams");
		res.add("test_TimeEvent_element_of_interest_for_diagrams");
		res.add("test_Unit_element_of_interest_for_diagrams");

		res.add("test_Diagram_review");
		res.add("test_Diagram_status");
		res.add("test_Diagram_synchronized");
		res.add("test_Diagram_visible_for_traceability");
		res.add("test_Diagram_visible_in_documentation");

		res.add("test_BooleanType_realized_informations");
		res.add("test_BooleanType_realizing_informations");
		res.add("test_Enumeration_realized_informations");
		res.add("test_Enumeration_realizing_informations");
		res.add("test_NumericType_realized_informations");
		res.add("test_NumericType_realizing_informations");
		res.add("test_PhysicalQuantity_realized_informations");
		res.add("test_PhysicalQuantity_realizing_informations");
		res.add("test_StringType_realized_informations");
		res.add("test_StringType_realizing_informations");

		res.add("test_BooleanType_status");
		res.add("test_CapabilityPkg_status");
		res.add("test_CapabilityRealizationPkg_status");
		res.add("test_CapabilityRealization_status");
		res.add("test_Capability_status");
		res.add("test_ChangeEvent_status");
		res.add("test_CombinedFragment_status");
		res.add("test_CommunicationMean_status");
		res.add("test_ComponentExchangeCategory_status");
		res.add("test_ComponentExchange_status");
		res.add("test_ComponentPort_status");
		res.add("test_ConfigurationItemPkg_status");
		res.add("test_ConfigurationItem_status");
		res.add("test_ConstraintDuration_status");
		res.add("test_Constraint_status");
		res.add("test_EPBSArchitecture_status");
		res.add("test_EntityPkg_status");
		res.add("test_EnumerationPropertyLiteral_status");
		res.add("test_EnumerationPropertyType_status");
		res.add("test_Enumeration_status");
		res.add("test_ExchangeCategory_status");
		res.add("test_ExchangeItemAllocation_status");
		res.add("test_ExchangeItemElement_status");
		res.add("test_ExchangeItem_status");
		res.add("test_FunctionInputPort_status");
		res.add("test_FunctionOutputPort_status");
		res.add("test_FunctionalChain_status");
		res.add("test_FunctionalExchange_status");
		res.add("test_InstanceRole_status");
		res.add("test_InterfacePkg_status");
		res.add("test_Interface_status");
		res.add("test_LogicalArchitecture_status");
		res.add("test_LogicalComponentPkg_status");
		res.add("test_LogicalComponent_status");
		res.add("test_LogicalFunctionPkg_status");
		res.add("test_LogicalFunction_status");
		res.add("test_MissionPkg_status");
		res.add("test_Mission_status");
		res.add("test_Mode_status");
		res.add("test_NumericType_status");
		res.add("test_OperationalActivityPkg_status");
		res.add("test_OperationalActivity_status");
		res.add("test_OperationalAnalysis_status");
		res.add("test_OperationalCapabilityPkg_status");
		res.add("test_OperationalCapability_status");
		res.add("test_OperationalProcess_status");
		res.add("test_PhysicalArchitecture_status");
		res.add("test_PhysicalComponentPkg_status");
		res.add("test_PhysicalFunctionPkg_status");
		res.add("test_PhysicalFunction_status");
		res.add("test_PhysicalLinkCategory_status");
		res.add("test_PhysicalLink_status");
		res.add("test_PhysicalPath_status");
		res.add("test_PhysicalPort_status");
		res.add("test_PhysicalQuantity_status");
		res.add("test_PropertyValueGroup_status");
		res.add("test_PropertyValuePkg_status");
		res.add("test_Region_status");
		res.add("test_Scenario_status");
		res.add("test_SequenceMessage_status");
		res.add("test_StateFragment_status");
		res.add("test_StateMachine_status");
		res.add("test_StateTransition_status");
		res.add("test_State_status");
		res.add("test_StringType_status");
		res.add("test_SystemAnalysis_status");
		res.add("test_SystemComponentPkg_status");
		res.add("test_SystemEngineering_status");
		res.add("test_SystemFunctionPkg_status");
		res.add("test_SystemFunction_status");
		res.add("test_TimeEvent_status");
		res.add("test_Unit_status");

		res.add("test_CapabilityRealization_involved_functions");
		res.add("test_Capability_involved_functions");
		res.add("test_Interface_implementor_components");
		res.add("test_Interface_user_components");
		res.add("test_LogicalActor_allocated_functions");
		res.add("test_LogicalActor_constraints");
		res.add("test_LogicalActor_contained_component_ports");
		res.add("test_LogicalActor_contained_physical_ports");
		res.add("test_LogicalActor_implemented_interfaces");
		res.add("test_LogicalActor_involving_capability_realizations");
		res.add("test_LogicalActor_used_interfaces");
		res.add("test_PhysicalActor_allocated_functions");
		res.add("test_PhysicalActor_constraints");
		res.add("test_PhysicalActor_contained_component_ports");
		res.add("test_PhysicalActor_contained_physical_ports");
		res.add("test_PhysicalActor_implemented_interfaces");
		res.add("test_PhysicalActor_involving_capability_realizations");
		res.add("test_PhysicalActor_used_interfaces");

		res.add("test_BehaviorPC_allocated_functions");
		res.add("test_BehaviorPC_allocator_configuration_items");
		res.add("test_BehaviorPC_constraints");
		res.add("test_BehaviorPC_contained_component_ports");
		res.add("test_BehaviorPC_implemented_interfaces");
		res.add("test_BehaviorPC_involving_capability_realizations");
		res.add("test_BehaviorPC_realized_logical_components");
		res.add("test_BehaviorPC_used_interfaces");
		res.add("test_Exception_sub");
		res.add("test_Exception_super");
		res.add("test_Interaction_constraints");
		res.add("test_Interaction_realizing_functional_exchanges");
		res.add("test_NodePC_allocator_configuration_items");
		res.add("test_NodePC_constraints");
		res.add("test_NodePC_contained_physical_ports");
		res.add("test_NodePC_involving_capability_realizations");
		res.add("test_Operand_constraints");
		res.add("test_OperationalActivity_incoming");
		res.add("test_OperationalActivity_outgoing");
		res.add("test_OperationalActor_allocated_operational_activities");
		res.add("test_OperationalActor_constraints");
		res.add("test_OperationalActor_involving_operational_capabilities");
		res.add("test_OperationalEntity_allocated_operational_activities");
		res.add("test_OperationalEntity_constraints");
		res.add("test_OperationalEntity_involving_operational_capabilities");

		res.add("test_REC_replicated_elements");

		res.add("test_BehaviorPC_contextual_element_for_diagrams");
		res.add("test_BehaviorPC_element_of_interest_for_diagrams");
		res.add("test_BehaviorPC_status");
		res.add("test_Interaction_contextual_element_for_diagrams");
		res.add("test_Interaction_element_of_interest_for_diagrams");
		res.add("test_Interaction_status");
		res.add("test_LogicalActor_contextual_element_for_diagrams");
		res.add("test_LogicalActor_element_of_interest_for_diagrams");
		res.add("test_LogicalActor_status");
		res.add("test_NodePC_contextual_element_for_diagrams");
		res.add("test_NodePC_element_of_interest_for_diagrams");
		res.add("test_NodePC_status");
		res.add("test_Operand_contextual_element_for_diagrams");
		res.add("test_Operand_element_of_interest_for_diagrams");
		res.add("test_Operand_status");
		res.add("test_OperationalActor_contextual_element_for_diagrams");
		res.add("test_OperationalActor_element_of_interest_for_diagrams");
		res.add("test_OperationalActor_status");
		res.add("test_OperationalEntity_contextual_element_for_diagrams");
		res.add("test_OperationalEntity_element_of_interest_for_diagrams");
		res.add("test_OperationalEntity_status");
		res.add("test_PhysicalActor_contextual_element_for_diagrams");
		res.add("test_PhysicalActor_element_of_interest_for_diagrams");
		res.add("test_PhysicalActor_status");
		res.add("test_REC_contextual_element_for_diagrams");
		res.add("test_REC_element_of_interest_for_diagrams");
		res.add("test_RPL_contextual_element_for_diagrams");
		res.add("test_RPL_element_of_interest_for_diagrams");

		res.add("test_BehaviorPC_deploying_node_p_c");
		res.add("test_BooleanType_default_value");
		res.add("test_ChangeEvent_expression");
		res.add("test_Class_primitive");
		res.add("test_Collection_max_card");
		res.add("test_Collection_min_card");
		res.add("test_Collection_primitive");
		res.add("test_CommunicationMean_source_entity");
		res.add("test_CommunicationMean_target_entity");
		res.add("test_Constraint_specification");
		res.add("test_Enumeration_default_value");
		res.add("test_Enumeration_max_value");
		res.add("test_Enumeration_min_value");
		res.add("test_Enumeration_null_value");
		res.add("test_FunctionalExchange_source_function");
		res.add("test_FunctionalExchange_source_port");
		res.add("test_FunctionalExchange_target_function");
		res.add("test_FunctionalExchange_target_port");
		res.add("test_Interaction_allocating_communication_mean");
		res.add("test_LogicalComponentPkg_owned_logical_component_pkgs");
		res.add("test_LogicalFunction_allocating_component");
		res.add("test_NumericType_default_value");
		res.add("test_NumericType_max_value");
		res.add("test_NumericType_min_value");
		res.add("test_NumericType_null_value");
		res.add("test_PhysicalFunction_allocating_component");
		res.add("test_PhysicalQuantity_default_value");
		res.add("test_PhysicalQuantity_max_value");
		res.add("test_PhysicalQuantity_min_value");
		res.add("test_PhysicalQuantity_null_value");
		res.add("test_REC_decription");
		res.add("test_REC_tags");
		res.add("test_RPL_decription");
		res.add("test_RPL_tags");
		res.add("test_StringType_default_value");
		res.add("test_StringType_max_length");
		res.add("test_StringType_min_length");
		res.add("test_StringType_null_value");
		res.add("test_SystemFunction_allocating_component");
		res.add("test_TimeEvent_expression");

		res.add("test_Class_contained_operations");
		res.add("test_Collection_contained_operations");
		res.add("test_ExchangeItem_realizing_operations");
		res.add("test_Operation_realized_exchange_items");
		res.add("test_Union_contained_operations");

		return res;
	}

	private Set<String> initQueryNames() {
		final Set<String> res = new HashSet<>();

		res.add("Element.r_e_c_source_element");
		res.add("Element.r_e_c");
		res.add("Element.r_p_l");
		res.add("Element.elementof_interestfor_diagram");
		res.add("ModelElement.expression");
		res.add("ModelElement.all_related_tables");
		res.add("ModelElement.all_related_diagrams");
		res.add("ModelElement.guard");
		res.add("ModelElement.post");
		res.add("ModelElement.exchange_context");
		res.add("ModelElement.pre");
		res.add("ModelElement.constraining_elements");
		res.add("AbstractType.inheritedof_typing_elements");
		res.add("TraceableElement.outgoing_generic_traces");
		res.add("TraceableElement.incoming_generic_traces");
		res.add("CapellaElement.applied_property_value_groups");
		res.add("CapellaElement.requirements");
		res.add("CapellaElement.applied_property_values");
		res.add("Type.exchange_item_elements");
		res.add("Type.typing_elements");
		res.add("GeneralizableElement.generalized_elements");
		res.add("GeneralizableElement.generalizing_elements");
		res.add("Component.component_breakdown");
		res.add("Component.parent");
		res.add("Component.owned_components");
		res.add("Component.generalized_components");
		res.add("Component.internal_outgoing_component_exchanges");
		res.add("Component.outgoing_delegations");
		res.add("Component.provided_interfaces");
		res.add("Component.communication_link");
		res.add("Component.used_interfaces");
		res.add("Component.required_interfaces");
		res.add("Component.outgoing_component_exchanges");
		res.add("Component.representing_parts");
		res.add("Component.implemented_interfaces");
		res.add("Component.incoming_component_exchanges");
		res.add("Component.scenarios");
		res.add("Component.component_ports");
		res.add("Component.incoming_delegations");
		res.add("Component.generalizing_components");
		res.add("Component.referencing_components");
		res.add("Component.internal_incoming_component_exchanges");
		res.add("Property.parent");
		res.add("Property.association");
		res.add("Property.type");
		res.add("Part.type");
		res.add("Allocation.target");
		res.add("Allocation.source");
		res.add("AbstractDependenciesPkg.dependencies");
		res.add("AbstractDependenciesPkg.inverse_dependencies");
		res.add("Interface.exchange_items");
		res.add("Interface.refined_interfaces");
		res.add("Interface.inherited_exchange_items");
		res.add("Interface.users");
		res.add("Interface.refining_interfaces");
		res.add("Interface.involving_scenarios");
		res.add("Interface.providers");
		res.add("Interface.requirers");
		res.add("Interface.implementors");
		res.add("InterfaceImplementation.target");
		res.add("InterfaceImplementation.source");
		res.add("InterfaceUse.target");
		res.add("InterfaceUse.source");
		res.add("ExchangeItemAllocation.exchange_item");
		res.add("ExchangeItemAllocation.scenarios");
		res.add("PhysicalLink.inherited_categories");
		res.add("PhysicalLink.allocated_component_exchanges");
		res.add("PhysicalLink.categories");
		res.add("PhysicalLink.physical_link_ends");
		res.add("PhysicalLink.realizing_configuration_items");
		res.add("PhysicalLink.physical_paths");
		res.add("PhysicalLinkCategory.physical_links");
		res.add("PhysicalPath.involved_physical_paths");
		res.add("PhysicalPath.involved_physical_links");
		res.add("PhysicalPath.allocated_component_exchanges");
		res.add("PhysicalPath.physical_paths");
		res.add("Involvement.involved_element");
		res.add("Involvement.involving_element");
		res.add("PhysicalPathInvolvement.involved_physical_path");
		res.add("PhysicalPathInvolvement.involved_physical_component");
		res.add("PhysicalPathInvolvement.involved_physical_link");
		res.add("PhysicalPort.allocated_function_ports");
		res.add("PhysicalPort.allocated_component_ports");
		res.add("PhysicalPort.outgoing_delegations");
		res.add("PhysicalPort.physical_links");
		res.add("PhysicalPort.realizing_configuration_items");
		res.add("DataValue.value");
		res.add("DataValue.referenced_property");
		res.add("DataValue.referenced_value");
		res.add("DataValue.referencing_value");
		res.add("Trace.target");
		res.add("Trace.source");
		res.add("Requirement.traced_elements");
		res.add("Constraint.constrained_elements");
		res.add("Generalization.target");
		res.add("Generalization.source");
		res.add("AbstractPropertyValue.value");
		res.add("AbstractPropertyValue.valued_elements");
		res.add("PropertyValueGroup.valued_elements");
		res.add("CatalogElementLink.referenced_element");
		res.add("CatalogElement.related_elements");
		res.add("CatalogElement.related_replicable_elements");
		res.add("CatalogElement.r_p_l");
		res.add("CapabilityRealizationInvolvedElement.involving_capability_realizations");
		res.add("ConfigurationItem.realized_physical_components");
		res.add("ConfigurationItem.realized_physical_links");
		res.add("ConfigurationItem.realized_physical_ports");
		res.add("CommunicationLink.target");
		res.add("CommunicationLink.source");
		res.add("SequenceMessage.parent_scenario");
		res.add("SequenceMessage.invoked_exchange_item_allocation");
		res.add("SequenceMessage.refined_sequence_message");
		res.add("SequenceMessage.invoked_component_exchange");
		res.add("SequenceMessage.invoked_communication_mean");
		res.add("SequenceMessage.exchange_items");
		res.add("SequenceMessage.invoked_interaction");
		res.add("SequenceMessage.invoked_functional_exchange");
		res.add("SequenceMessage.target");
		res.add("SequenceMessage.target");
		res.add("SequenceMessage.invoked_operation");
		res.add("SequenceMessage.source");
		res.add("SequenceMessage.refining_sequence_message");
		res.add("SequenceMessage.source");
		res.add("Scenario.parent");
		res.add("Scenario.referenced_scenario");
		res.add("Scenario.realized_scenarios");
		res.add("Scenario.refined_scenarios");
		res.add("Scenario.refining_scenarios");
		res.add("Scenario.realizing_scenarios");
		res.add("InstanceRole.parent_scenario");
		res.add("InstanceRole.represented_instance");
		res.add("AbstractCapability.scenarios");
		res.add("AbstractCapability.generalized_elements");
		res.add("AbstractCapability.active_in_modes");
		res.add("AbstractCapability.involved_components");
		res.add("AbstractCapability.extended_capabilities");
		res.add("AbstractCapability.refined_capabilities");
		res.add("AbstractCapability.active_in_states");
		res.add("AbstractCapability.included_capabilities");
		res.add("AbstractCapability.generalizing_elements");
		res.add("AbstractCapability.refining_scenarios");
		res.add("AbstractCapability.including_capabilities");
		res.add("AbstractCapability.extending_capabilities");
		res.add("AbstractCapabilityExtend.target");
		res.add("AbstractCapabilityExtend.source");
		res.add("AbstractCapabilityGeneralization.target");
		res.add("AbstractCapabilityGeneralization.source");
		res.add("AbstractCapabilityInclude.target");
		res.add("AbstractCapabilityInclude.source");
		res.add("InteractionUse.referenced_scenario");
		res.add("InteractionUse.referencing_scenario");
		res.add("StateFragment.related_function");
		res.add("StateFragment.related_state");
		res.add("Association.roles");
		res.add("Class.realized_classes");
		res.add("Class.realizing_classes");
		res.add("Collection.type");
		res.add("Operation.scenarios");
		res.add("Parameter.type");
		res.add("ExchangeItem.realized_exchange_items");
		res.add("ExchangeItem.exchange_item_elements");
		res.add("ExchangeItem.realizing_exchange_items");
		res.add("ExchangeItem.allocating_function_output_ports");
		res.add("ExchangeItem.allocating_function_input_ports");
		res.add("ExchangeItem.interfaces");
		res.add("ExchangeItem.communication_links");
		res.add("ExchangeItem.allocating_exchanges");
		res.add("ExchangeItemElement.type");
		res.add("ExchangeItemInstance.scenarios");
		res.add("AbstractFunction.parent");
		res.add("AbstractFunction.breakdown");
		res.add("AbstractFunction.active_in_modes");
		res.add("AbstractFunction.active_in_states");
		res.add("AbstractFunction.functional_chains");
		res.add("AbstractFunction.allocating_actor");
		res.add("AbstractFunction.scenarios");
		res.add("OperationalActivity.owned_operational_processes");
		res.add("OperationalActivity.internal_outgoing_interactions");
		res.add("OperationalActivity.outgoing_interactions");
		res.add("OperationalActivity.realizing_system_functions");
		res.add("OperationalActivity.internal_incoming_interactions");
		res.add("OperationalActivity.allocating_entity");
		res.add("OperationalActivity.allocating_actor");
		res.add("OperationalActivity.operational_processes");
		res.add("OperationalActivity.allocating_role");
		res.add("OperationalActivity.incoming_interactions");
		res.add("OperationalActivity.allocating_operational_actor");
		res.add("FunctionalChain.owner");
		res.add("FunctionalChain.involved_functions");
		res.add("FunctionalChain.realized_operational_processes");
		res.add("FunctionalChain.involved_functional_chains");
		res.add("FunctionalChain.realized_functional_chains");
		res.add("FunctionalChain.active_in_states");
		res.add("FunctionalChain.involvement_links");
		res.add("FunctionalChain.involved_components");
		res.add("FunctionalChain.active_in_modes");
		res.add("FunctionalChain.involving_capability_realizations");
		res.add("FunctionalChain.involving_capabilities");
		res.add("FunctionalChain.realizing_functional_chains");
		res.add("FunctionalChain.parent_functional_chains");
		res.add("OperationalProcess.involved_operational_processes");
		res.add("OperationalProcess.involved_operational_activities");
		res.add("OperationalProcess.involving_operational_capabilities");
		res.add("OperationalProcess.parent_operational_processes");
		res.add("OperationalCapability.owned_operational_processes");
		res.add("OperationalCapability.involved_entities");
		res.add("OperationalCapability.involved_operational_processes");
		res.add("OperationalCapability.realizing_capabilities");
		res.add("Role.allocated_operational_activities");
		res.add("Role.allocating_entities");
		res.add("Role.scenarios");
		res.add("Entity.breakdown");
		res.add("Entity.allocated_roles");
		res.add("Entity.allocated_operational_activities");
		res.add("Entity.outgoing_communication_mean");
		res.add("Entity.incoming_communication_mean");
		res.add("Entity.involving_operational_capabilities");
		res.add("Entity.realizing_system_components");
		res.add("ExchangeSpecification.realized_component_exchanges");
		res.add("ExchangeSpecification.target");
		res.add("ExchangeSpecification.source");
		res.add("ComponentExchange.related_data");
		res.add("ComponentExchange.owner");
		res.add("ComponentExchange.inherited_categories");
		res.add("ComponentExchange.allocated_functional_exchanges");
		res.add("ComponentExchange.categories");
		res.add("ComponentExchange.connected_components");
		res.add("ComponentExchange.exchange_items");
		res.add("ComponentExchange.realized_communication_mean");
		res.add("ComponentExchange.connectedparts");
		res.add("ComponentExchange.realizing_component_exchanges");
		res.add("ComponentExchange.allocating_physical_path");
		res.add("ComponentExchange.allocating_physical_link");
		res.add("ComponentExchange.scenarios");
		res.add("CommunicationMean.allocated_interactions");
		res.add("CommunicationMean.target");
		res.add("CommunicationMean.source");
		res.add("PhysicalFunction.owned_functional_chains");
		res.add("PhysicalFunction.outgoing_functional_exchanges");
		res.add("PhysicalFunction.out_flow_ports");
		res.add("PhysicalFunction.realized_logical_functions");
		res.add("PhysicalFunction.internal_outgoing_functional_exchanges");
		res.add("PhysicalFunction.involving_capability_realizations");
		res.add("PhysicalFunction.allocating_physical_component");
		res.add("PhysicalFunction.internal_incoming_functional_exchanges");
		res.add("PhysicalFunction.incoming_functional_exchanges");
		res.add("PhysicalFunction.allocating_physical_actor");
		res.add("PhysicalFunction.in_flow_ports");
		res.add("PhysicalComponent.deployed_physical_components");
		res.add("PhysicalComponent.physical_links");
		res.add("PhysicalComponent.allocated_physical_functions");
		res.add("PhysicalComponent.internal_physical_links");
		res.add("PhysicalComponent.realized_logical_component");
		res.add("PhysicalComponent.realizing_configuration_items");
		res.add("PhysicalComponent.physical_links");
		res.add("PhysicalComponent.deploying_physical_components");
		res.add("PhysicalComponent.realizing_configuration_items");
		res.add("LogicalFunction.owned_functional_chains");
		res.add("LogicalFunction.outgoing_functional_exchanges");
		res.add("LogicalFunction.out_flow_ports");
		res.add("LogicalFunction.internal_outgoing_functional_exchanges");
		res.add("LogicalFunction.realized_system_functions");
		res.add("LogicalFunction.realizing_physical_functions");
		res.add("LogicalFunction.allocating_logical_actor");
		res.add("LogicalFunction.internal_incoming_functional_exchanges");
		res.add("LogicalFunction.in_flow_ports");
		res.add("LogicalFunction.allocating_logical_component");
		res.add("LogicalFunction.involving_capability_realizations");
		res.add("LogicalFunction.incoming_functional_exchanges");
		res.add("LogicalComponent.realized_system_components");
		res.add("LogicalComponent.allocated_logical_functions");
		res.add("LogicalComponent.realizing_physical_components");
		res.add("CapabilityRealization.owned_functional_chains");
		res.add("CapabilityRealization.involved_functional_chains");
		res.add("CapabilityRealization.realized_capabilities");
		res.add("CapabilityRealization.realized_capability_realizations");
		res.add("CapabilityRealization.involved_logical_functions");
		res.add("CapabilityRealization.involved_physical_functions");
		res.add("CapabilityRealization.realizing_capability_realizations");
		res.add("ExchangeCategory.functional_exchanges");
		res.add("FunctionalChainReference.involved_functions");
		res.add("FunctionalChainReference.involved_functional_chains");
		res.add("FunctionalChainReference.involvement_links");
		res.add("FunctionalChainReference.parent_functional_chains");
		res.add("FunctionPort.realized_function_ports");
		res.add("FunctionPort.exchange_items");
		res.add("FunctionPort.realizing_function_ports");
		res.add("FunctionPort.allocating_component_ports");
		res.add("Pin.type");
		res.add("Pin.owner");
		res.add("Pin.realized_pin");
		res.add("Pin.outgoing_functional_exchanges");
		res.add("Pin.incoming_functional_exchanges");
		res.add("Pin.realizing_pin");
		res.add("FunctionalExchange.related_data");
		res.add("FunctionalExchange.owner");
		res.add("FunctionalExchange.exchange_items");
		res.add("FunctionalExchange.target");
		res.add("FunctionalExchange.realized_functional_exchange");
		res.add("FunctionalExchange.realized_interactions");
		res.add("FunctionalExchange.categories");
		res.add("FunctionalExchange.realizing_functional_exchanges");
		res.add("FunctionalExchange.functional_chains");
		res.add("FunctionalExchange.scenarios");
		res.add("FunctionalExchange.source");
		res.add("FunctionalExchange.allocating_communicationmean");
		res.add("FunctionalExchange.allocating_component_exchange");
		res.add("FunctionalExchange.operational_processes");
		res.add("ComponentExchangeCategory.component_exchanges");
		res.add("ComponentPort.type");
		res.add("ComponentPort.owner");
		res.add("ComponentPort.provided_interfaces");
		res.add("ComponentPort.required_interfaces");
		res.add("ComponentPort.realized_component_ports");
		res.add("ComponentPort.allocated_function_ports");
		res.add("ComponentPort.outgoing_delegations");
		res.add("ComponentPort.outgoing_component_exchanges");
		res.add("ComponentPort.allocating_physical_ports");
		res.add("ComponentPort.incoming_component_exchanges");
		res.add("ComponentPort.realizing_component_ports");
		res.add("ComponentPort.incoming_delegations");
		res.add("ReferenceHierarchyContext.source_reference_hierachy");
		res.add("ReferenceHierarchyContext.target_reference_hierachy");
		res.add("FunctionalChainInvolvementLink.exchange_context");
		res.add("FunctionalChainInvolvementLink.target");
		res.add("FunctionalChainInvolvementLink.source");
		res.add("SequenceLink.condition");
		res.add("SequenceLink.owner");
		res.add("SequenceLink.links");
		res.add("SequenceLink.target_control_node");
		res.add("SequenceLink.target_involvement_function");
		res.add("SequenceLink.source_involvement_function");
		res.add("SequenceLink.source_control_node");
		res.add("SequenceLinkEnd.target_sequence_links");
		res.add("SequenceLinkEnd.source_sequence_links");
		res.add("FunctionalChainInvolvementFunction.owner");
		res.add("FunctionalChainInvolvementFunction.outgoing_involvement_links");
		res.add("FunctionalChainInvolvementFunction.incoming_involvement_links");
		res.add("IState.parent_stateand_mode");
		res.add("IState.involved_statesand_modes");
		res.add("IState.owned_stateand_mode");
		res.add("IState.outgoing_transition");
		res.add("IState.incoming_transition");
		res.add("IState.involving_statesandmodes");
		res.add("Region.owned_entry");
		res.add("AbstractState.realized_mode");
		res.add("AbstractState.realized_state");
		res.add("AbstractState.realizing_state");
		res.add("AbstractState.realizing_mode");
		res.add("State.do_activity");
		res.add("State.active_elements");
		res.add("State.scenarios");
		res.add("State.active_elements");
		res.add("StateTransition.effect");
		res.add("StateTransition.target");
		res.add("StateTransition.trigger");
		res.add("StateTransition.source");
		res.add("Pseudostate.parent_region");
		res.add("SystemFunction.owned_functional_chains");
		res.add("SystemFunction.realized_operational_activities");
		res.add("SystemFunction.internal_outgoing_functional_exchanges");
		res.add("SystemFunction.out_flow_ports");
		res.add("SystemFunction.outgoing_functional_exchanges");
		res.add("SystemFunction.incoming_functional_exchanges");
		res.add("SystemFunction.internal_incoming_functional_exchanges");
		res.add("SystemFunction.realizing_logical_functions");
		res.add("SystemFunction.allocating_actor");
		res.add("SystemFunction.in_flow_ports");
		res.add("SystemFunction.involving_capabilities");
		res.add("SystemFunction.allocating_system");
		res.add("Mission.exploited_capabilities");
		res.add("Mission.involved_system_components");
		res.add("Capability.owned_functional_chains");
		res.add("Capability.realized_operational_capabilities");
		res.add("Capability.involved_system_functions");
		res.add("Capability.involved_functional_chains");
		res.add("Capability.exploiting_missions");
		res.add("Capability.realizing_capability_realizations");
		res.add("CapabilityExploitation.involved_element");
		res.add("CapabilityExploitation.source");
		res.add("SystemComponent.allocated_system_functions");
		res.add("SystemComponent.realized_operational_entities");
		res.add("SystemComponent.realizing_logical_components");
		res.add("SystemComponent.involving_capabilities");
		res.add("SystemComponent.involving_missions");

		return res;
	}

	private EStructuralFeature findMatchingFeature(EClass eCls, Property property) {
		EStructuralFeature res = null;

		final List<EStructuralFeature> candidates = new ArrayList<>();
		for (EStructuralFeature candidate : eCls.getEAllStructuralFeatures()) {
			if (candidate.getEType().getName().equals(property.getType().getLabel())
					&& (isScalar(property) && !candidate.isMany() || !isScalar(property) && candidate.isMany())) {
				candidates.add(candidate);
			}
		}

		if (candidates.size() == 1) {
			res = candidates.get(0);
		} else if (candidates.size() > 0) {
			EStructuralFeature bestMatch = null;
			int bestDistance = Integer.MAX_VALUE;

			for (EStructuralFeature candidate : candidates) {
				final int distance = levenshteinDistance(property.getLabel(), candidate.getName());
				if (distance < bestDistance) {
					bestDistance = distance;
					bestMatch = candidate;
				}
			}

			res = bestMatch;
		}

		return res;
	}

	private EClass findCorrespondingEClass(Class cls) {
		EClassifier res = null;

		for (EPackage ePkg : ePackages) {
			res = ePkg.getEClassifier(cls.getLabel());
			if (res instanceof EClass) {
				break;
			}
		}

		return (EClass) res;
	}

	private List<EPackage> initEPackages() {
		final List<EPackage> res = new ArrayList<>();

		for (Object obj : new ArrayList(EPackage.Registry.INSTANCE.values())) {
			if (obj instanceof EPackage.Descriptor && isEPackageOfInterest(((EPackage.Descriptor) obj).getEPackage())) {
				res.add(((EPackage.Descriptor) obj).getEPackage());
			} else if (obj instanceof EPackage && isEPackageOfInterest((EPackage) obj)) {
				res.add((EPackage) obj);
			}
		}

		return res;
	}

	private boolean isEPackageOfInterest(EPackage ePackage) {
		return ePackage != null && ePackage.getNsURI() != null && (ePackage.getNsURI().contains("capella")
				|| ePackage.getNsURI().contains("kitalpha") || ePackage.getNsURI().contains("sirius"));
	}

	public static List<Class> getAllSuperClasses(Class cls) {
		final List<Class> res = new ArrayList<>();

		for (GeneralizableElement superType : cls.getSuper()) {
			if (superType instanceof Class) {
				res.add((Class) superType);
				res.addAll(getAllSuperClasses((Class) superType));
			}
		}

		return res;
	}

	private Set<Feature> getAllFeatures(Class cls) {
		final Set<Feature> res = new LinkedHashSet<>();

		for (Class superType : getAllSuperClasses(cls)) {
			res.addAll(superType.getOwnedFeatures());
		}
		res.addAll(cls.getOwnedFeatures());

		return res;
	}

	private String getHeader(DataPkg root, String clsLabel) {
		final StringBuilder res = new StringBuilder();

//		for (DataPkg pkg : root.getOwnedDataPkgs()) {
		res.append("include('workspace://Python4Capella/simplified_api/" + "capella" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "capella" + " import *" + NL);
		res.append("include('workspace://Python4Capella/simplified_api/" + "pvmt" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "pvmt" + " import *" + NL);
		res.append("include('workspace://Python4Capella/simplified_api/" + "requirement" + ".py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api." + "requirement" + " import *" + NL);
//		}
		res.append(NL);
		res.append("import unittest" + NL);
		res.append(NL);
		res.append("class " + clsLabel + "_tests(unittest.TestCase):" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTest(Class cls, Feature feature) {
		final StringBuilder res = new StringBuilder();

		if (feature instanceof Operation) {
			res.append(getTest(cls, (Operation) feature));
		} else if (feature instanceof Property) {
			res.append(getTest(cls, (Property) feature));
		}

		return res.toString();
	}

	private String getTest(Class cls, Operation operation) {
		final StringBuilder res = new StringBuilder();

		final String pythonName = ProduceCapellaPythonAPIFromEcoreHandler.getPythonName(operation.getName());
		res.append("    def test_" + cls.getName() + "_" + pythonName + "(self):" + NL);
		res.append("        tested = " + cls.getName() + "()" + NL);
		if ("CapellaModel".equals(cls.getName())) {
			res.append("        tested.open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")" + NL);
		}

		int index = 1;
		final StringJoiner joiner = new StringJoiner(", ");
		for (Parameter parameter : operation.getOwnedParameters()) {
			if (parameter.getDirection() != ParameterDirection.RETURN) {
				final String paramName = "param" + index++;
				res.append("        " + paramName + " = " + getTestValue(cls, parameter) + NL);
				if ("CapellaModel".equals(parameter.getType().getLabel())) {
					res.append("        " + paramName + ".open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")" + NL);
				}
				joiner.add(paramName);
			}
		}

		res.append("        tested." + pythonName + "(" + joiner.toString() + ")" + NL);
		res.append("        pass" + NL);
		res.append(NL);

		return res.toString();
	}

	private String getTest(Class cls, Property property) {
		final StringBuilder res = new StringBuilder();

		final String pythonName = ProduceCapellaPythonAPIFromEcoreHandler.getPythonName(property.getName());
		final String testName = "test_" + cls.getName() + "_" + pythonName;
		res.append("    def " + testName + "(self):" + NL);
		res.append("        tested = " + cls.getName() + "()" + NL);
		if ("CapellaModel".equals(cls.getName())) {
			res.append("        tested.open(\"/In-Flight Entertainment System/In-Flight Entertainment System.aird\")" + NL);
		}
		if (isScalar(property)) {
			if (property.isIsReadOnly() || isQuery(cls, pythonName) || readOnlyTests.contains(testName)) {
				res.append("        tested.get_" + pythonName + "()" + NL);
			} else {
				res.append("        value = " + getTestValue(cls, property) + NL);
				res.append("        tested.set_" + pythonName + "(value)" + NL);
				res.append("        self.assertEqual(tested.get_" + pythonName + "(), value)" + NL);
			}
		} else {
			// collection
			if (property.isIsReadOnly() || isQuery(cls, pythonName) || readOnlyTests.contains(testName)) {
				res.append("        tested.get_" + pythonName + "()" + NL);
			} else {
				res.append("        value = " + getTestValue(cls, property) + NL);
				res.append("        tested.get_" + pythonName + "().add(value)" + NL);
				res.append("        self.assertEqual(tested.get_" + pythonName + "().get(0), value)" + NL);
			}
		}
		res.append("        pass" + NL);
		res.append(NL);

		return res.toString();
	}

	private boolean isQuery(Class cls, final String pythonName) {
		boolean res = queries.contains(cls.getLabel() + "." + pythonName);

		if (!res) {
			for (Class superCls : getAllSuperClasses(cls)) {
				if (queries.contains(superCls.getLabel() + "." + pythonName)) {
					res = true;
					break;
				}
			}
		}

		return res;
	}

	private String getTestValue(Class cls, TypedElement typedElement) {
		final String res;

		if ("Boolean".equals(typedElement.getType().getLabel())) {
			res = "True";
		} else if ("Float".equals(typedElement.getType().getLabel())) {
			res = "3.14";
		} else if ("Integer".equals(typedElement.getType().getLabel())) {
			res = "42";
		} else if ("String".equals(typedElement.getType().getLabel())) {
			res = "\"value\"";
		} else {
			if (typedElement.getType() instanceof Class && ((Class) typedElement.getType()).isAbstract()) {
				res = concreteClass.get(typedElement.getType()).getLabel() + "()";
			} else {
				res = typedElement.getType().getLabel() + "()";
			}
		}

		return res;
	}

	private boolean isScalar(Property property) {
		final NumericValue ownedMaxCard = property.getOwnedMaxCard();
		return ownedMaxCard instanceof LiteralNumericValue
				&& "1".equals(((LiteralNumericValue) ownedMaxCard).getValue());
	}

	private static int levenshteinDistance(CharSequence lhs, CharSequence rhs) {
		int len0 = lhs.length() + 1;
		int len1 = rhs.length() + 1;

		// the array of distances
		int[] cost = new int[len0];
		int[] newcost = new int[len0];

		// initial cost of skipping prefix in String s0
		for (int i = 0; i < len0; i++)
			cost[i] = i;

		// dynamically computing the array of distances

		// transformation cost for each letter in s1
		for (int j = 1; j < len1; j++) {
			// initial cost of skipping prefix in String s1
			newcost[0] = j;

			// transformation cost for each letter in s0
			for (int i = 1; i < len0; i++) {
				// matching current letters in both strings
				int match = (lhs.charAt(i - 1) == rhs.charAt(j - 1)) ? 0 : 1;

				// computing cost for each transformation
				int cost_replace = cost[i - 1] + match;
				int cost_insert = cost[i] + 1;
				int cost_delete = newcost[i - 1] + 1;

				// keep minimum cost
				newcost[i] = Math.min(Math.min(cost_insert, cost_delete), cost_replace);
			}

			// swap cost/newcost arrays
			int[] swap = cost;
			cost = newcost;
			newcost = swap;
		}

		// the distance is the cost for transforming all letters in both strings
		return cost[len0 - 1];
	}

}
