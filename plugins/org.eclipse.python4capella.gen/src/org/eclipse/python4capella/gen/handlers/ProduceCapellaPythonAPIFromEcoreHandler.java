package org.eclipse.python4capella.gen.handlers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.lang.reflect.Field;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
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
import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EEnum;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EPackage.Descriptor;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.EcorePackage;
import org.polarsys.capella.common.helpers.query.IQuery;
import org.polarsys.capella.common.ui.toolkit.browser.category.CategoryRegistry;
import org.polarsys.capella.common.ui.toolkit.browser.category.ICategory;

public class ProduceCapellaPythonAPIFromEcoreHandler extends AbstractHandler {

	// self.eAllContents()->filter({information::Property |
	// information::Association})->collect(e | '"' + e.name + '"')->sep(',
	// ')->toString()
	private static final Set<String> TO_KEEP = new HashSet<>(Arrays.asList("Root Operational Activity",
			"Root System Function", "laAssociation1", "ctxAssociation1", "paAssociation1", "faAssociation13",
			"faAssociation14", "faAssociation20", "faAssociation20", "faAssociation21", "saAssociation9",
			"laAssociation1", "csAssociation18", "csAssociation17", "csAssociation19", "oaAssociation27",
			"diagramAssociation2", "diagramAssociation1", "Basic TypesAssociation1", "DataAssociation1",
			"faAssociation46", "saAssociation22", "laAssociation23", "oaAssociation30", "faAssociation12",
			"faAssociation45", "laAssociation25", "paAssociation22", "laAssociation26", "paAssociation21",
			"epbsAssociation6", "scenarioAssociation16", "classesAssociation8", "capellamodellerAssociation1",
			"project", "Capella Light MetamodelAssociation8", "systemEngineering",
			"Capella Light MetamodelAssociation11", "systemEngineering", "Capella Light MetamodelAssociation7",
			"systemEngineering", "Capella Light MetamodelAssociation10", "systemEngineering",
			"Capella Light MetamodelAssociation9", "systemEngineering", "capellamodellerAssociation7", "model",
			"Capella Light MetamodelAssociation7", "systemEngineering", "capellamodellerAssociation9", "capellaModel",
			"systemEngineering", "referencedLibraries", "allDiagrams", "recCatalogs", "operationalAnalysis",
			"systemAnalysis", "logicalArchitecture", "physicalArchitecture", "ePBSArchitecture",
			"capellacoreAssociation3", "enumerationPropertyType", "capellacoreAssociation3", "capellaElement",
			"capellacoreAssociation4", "capellaElement", "capellacoreAssociation5", "capellacoreAssociation6",
			"capellaElement", "capellacoreAssociation7", "capellaElement", "capellacoreAssociation8",
			"propertyValuePkgContainer", "Abstract TypesAssociation4", "Abstract TypesAssociation1",
			"capellacoreAssociation10", "propertyValue", "ownedDiagrams", "elementOfInterestForDiagrams",
			"contextualElementForDiagrams", "representingDiagrams", "id", "sid", "name", "summary", "description",
			"status", "review", "visibleInDocumentation", "visibleForTraceability", "ownedConstraints", "constraints",
			"ownedPropertyValues", "appliedPropertyValues", "ownedPropertyValueGroups", "appliedPropertyValueGroups",
			"ownedEnumerationPropertyTypes", "specification", "constrainedElements", "kind", "value", "valuedElements",
			"type", "valuedElements", "ownedLiterals", "ownedPropertyValuePkgs", "uid", "name", "type", "package",
			"description", "status", "review", "visibleInDocumentation", "visibleForTraceability", "synchronized",
			"target", "representedElements", "contextualElements", "elementsOfInterest", "reAssociation1",
			"catalogElementPkg", "reAssociation2", "reAssociation3", "compliancyDefinitionPkg", "reAssociation4",
			"recCatalog", "reAssociation5", "rEC", "reAssociation6", "rPL", "reAssociation7", "abstractCatalogElement",
			"reAssociation8", "catalogElementPkg", "reAssociation9", "catalogElementPkg", "id", "name", "decription",
			"author", "environment", "tags", "referencedElements", "defaultReplicaCompliancy", "replicatedElements",
			"suffix", "readOnly", "origin", "currentCompliancy", "ownedElementPkgs", "ownedRecs", "ownedRpls",
			"ownedCompliancyDefinitionPkg", "ownedDefinitions", "description", "oaAssociation1", "oaAssociation2",
			"oaAssociation3", "operationalActivityPkg", "oaAssociation4", "operationalActivityPkg", "oaAssociation5",
			"operationalActivity", "oaAssociation7", "oaAssociation8", "entity", "oaAssociation9", "oaAssociation10",
			"oaAssociation11", "oaAssociation12", "operationalActivity", "oaAssociation13", "entityPkg",
			"oaAssociation14", "entityPkg", "oaAssociation15", "interaction", "oaAssociation16", "oaAssociation17",
			"communicationMean", "oaAssociation17", "oaAssociation18", "operationalAnalysis", "oaAssociation19",
			"operationalAnalysis", "oaAssociation20", "operationalAnalysis", "oaAssociation21", "oaAssociation22",
			"operationalCapability", "oaAssociation23", "Capella Light MetamodelAssociation9", "operationalAnalysis",
			"Capella Light MetamodelAssociation10", "operationalAnalysis", "oaAssociation26", "oaAssociation28",
			"operationalProcess", "oaAssociation29", "operationalProcess", "oaAssociation31", "operationalProcess",
			"oaAssociation32", "operationalCapabilityPkg", "oaAssociation33", "operationalCapabilityPkg",
			"oaAssociation33", "operationalActivity", "Capella Light MetamodelAssociation19", "operationalActor",
			"operationalActivityPkg", "operationalCapabilityPkg", "interfacePkg", "dataPkg", "entityPkg",
			"ownedOperationalActivityPkgs", "ownedOperationalActivities", "containedOperationalActivities",
			"ownedOperationalActivityPkgs", "incoming", "outgoing", "allocatingEntity", "ownedOperationalProcesses",
			"involvingOperationalProcesses", "involvingOperationalCapabilities", "realizingSystemFunctions", "source",
			"target", "allocatingCommunicationMean", "involvingOperationalProcesses", "exchangedItems",
			"realizingFunctionalExchanges", "involvedOperationalActivities", "involvedInteractions",
			"involvedOperationalProcesses", "preCondition", "postCondition", "availableInStates",
			"involvingOperationalCapabilities", "realizingFunctionalChains", "ownedOperationalCapabilityPkgs",
			"ownedOperationalCapabilities", "ownedOperationalProcesses", "involvedOperationalProcesses",
			"involvedOperationalActivities", "involvedEntities", "realizingCapabilities", "ownedEntityPkgs",
			"ownedEntities", "ownedEntities", "incomingCommunicationMeans", "outgoingCommunicationMeans",
			"allocatedOperationalActivities", "involvingOperationalCapabilities", "ownedStateMachines",
			"realizingSystemActors", "sourceEntity", "targetEntity", "allocatedInteractions", "convoyedInformations",
			"realizingComponentExchanges", "saAssociation1", "saAssociation2", "missionPkg", "saAssociation3",
			"missionPkg", "saAssociation4", "capabilityPkg", "saAssociation5", "capabilityPkg", "saAssociation6",
			"actorPkg", "saAssociation7", "systemComponentPkg", "saAssociation8", "systemActor", "saAssociation9",
			"systemAnalysis", "saAssociation10", "systemAnalysis", "saAssociation11", "systemAnalysis",
			"saAssociation12", "systemAnalysis", "saAssociation13", "saAssociation14", "systemFunctionPkg",
			"saAssociation15", "systemFunctionPkg", "saAssociation16", "systemFunction", "saAssociation17",
			"systemFunction", "saAssociation18", "systemComponentPkg", "saAssociation19", "systemActor",
			"Capella Light MetamodelAssociation12", "systemAnalysis", "Capella Light MetamodelAssociation11",
			"systemAnalysis", "saAssociation22", "systemFunctionPkg", "capabilityPkg", "interfacePkg", "dataPkg",
			"systemComponentPkg", "missionPkg", "ownedSystemFunctionPkgs", "ownedSystemFunctions",
			"containedSystemFunctions", "ownedSystemFunctionPkgs", "realizedOperationalActivities",
			"realizingLogicalFunctions", "ownedCapabilityPkgs", "ownedCapabilities", "purposeMissions",
			"realizedOperationalCapabilities", "realizingCapabilityRealizations", "involvedSystemActors",
			"ownedSystemComponentPkgs", "ownedSystem", "ownedActors", "isHuman", "ownedActors",
			"ownedSystemComponentPkgs", "involvingMissions", "realizedOperationalEntities", "involvingCapabilities",
			"realizingLogicalActors", "ownedMissionPkgs", "ownedMissions", "exploitedCapabilities", "involvedActors",
			"laAssociation2", "laAssociation2", "logicalArchitecture", "laAssociation3", "logicalArchitecture",
			"laAssociation4", "logicalArchitecture", "laAssociation5", "logicalFunction", "laAssociation6",
			"logicalFunctionPkg", "laAssociation7", "logicalFunction", "laAssociation8", "logicalFunctionPkg",
			"laAssociation9", "capabilityRealizationPkg", "laAssociation10", "capabilityRealizationPkg",
			"Capella Light MetamodelAssociation14", "logicalArchitecture", "Capella Light MetamodelAssociation13",
			"logicalArchitecture", "laAssociation13", "logicalComponentPkg", "laAssociation14", "logicalComponentPkg",
			"laAssociation15", "logicalComponentPkg", "laAssociation16", "logicalComponentPkg", "laAssociation17",
			"logicalActor", "laAssociation18", "logicalSystem", "laAssociation19", "logicalComponent",
			"laAssociation20", "logicalActor", "laAssociation21", "logicalSystem", "laAssociation22",
			"logicalComponent", "laAssociation23", "laAssociation24", "logicalFunctionPkg", "capabilityRealizationPkg",
			"interfacePkg", "dataPkg", "logicalComponentPkg", "ownedLogicalFunctionPkgs", "ownedLogicalFunctions",
			"containedLogicalFunctions", "ownedLogicalFunctionPkgs", "realizedSystemFunctions",
			"realizingPhysicalFunctions", "ownedCapabilityRealizationPkgs", "ownedCapabilityRealizations",
			"realizedCapabilities", "realizedCapabilityRealizations", "realizingCapabilityRealizations",
			"involvedLogicalActors", "involvedLogicalComponents", "involvedPhysicalComponents",
			"involvedPhysicalActors", "ownedLogicalComponentPkgs", "ownedLogicalSystem", "ownedLogicalActors",
			"ownedLogicalComponents", "ownedLogicalComponents", "ownedLogicalComponentPkgs", "ownedLogicalComponents",
			"ownedLogicalComponentPkgs", "isHuman", "realizingBehaviorPCs", "involvingCapabilityRealizations",
			"ownedLogicalActors", "ownedLogicalComponentPkgs", "realizedSystemActors", "isHuman",
			"realizingPhysicalActors", "involvingCapabilityRealizations", "paAssociation1", "paAssociation2",
			"physicalArchitecture", "paAssociation3", "physicalArchitecture", "paAssociation4", "physicalFunctionPkg",
			"paAssociation5", "physicalFunction", "paAssociation6", "physicalFunctionPkg", "paAssociation7",
			"physicalFunction", "paAssociation8", "physicalComponentPkg", "paAssociation9", "physicalComponentPkg",
			"paAssociation10", "physicalComponent", "paAssociation11", "physicalComponent", "paAssociation12",
			"physicalActor", "paAssociation13", "physicalComponentPkg", "paAssociation14", "physicalActor",
			"paAssociation15", "physicalComponentPkg", "paAssociation16", "physicalSystem",
			"Capella Light MetamodelAssociation13", "physicalArchitecture", "Capella Light MetamodelAssociation11",
			"physicalArchitecture", "Capella Light MetamodelAssociation12", "physicalArchitecture", "paAssociation20",
			"physicalSystem", "physicalFunctionPkg", "capabilityRealizationPkg", "interfacePkg", "dataPkg",
			"physicalComponentPkg", "ownedPhysicalFunctionPkgs", "ownedPhysicalFunctions", "containedPhysicalFunctions",
			"ownedPhysicalFunctionPkgs", "realizedLogicalFunctions", "ownedPhysicalComponentPkgs",
			"ownedPhysicalSystem", "ownedPhysicalActors", "ownedPhysicalComponents", "ownedPhysicalComponents",
			"ownedPhysicalComponentPkgs", "allocatorConfigurationItems", "kind", "ownedPhysicalComponents",
			"ownedPhysicalComponentPkgs", "isHuman", "involvingCapabilityRealizations", "deployingNodePC",
			"realizedLogicalComponents", "deployedBehaviorPCs", "ownedPhysicalActors", "ownedPhysicalComponentPkgs",
			"realizedLogicalActors", "isHuman", "involvingCapabilityRealizations", "epbsAssociation1",
			"ePBSArchitecture", "epbsAssociation2", "configurationItem", "epbsAssociation3", "configurationItem",
			"epbsAssociation4", "configurationItemPkg", "epbsAssociation5", "configurationItemPkg",
			"Capella Light MetamodelAssociation15", "ePBSArchitecture", "Capella Light MetamodelAssociation14",
			"ePBSArchitecture", "capabilityRealizationPkg", "configurationItemPkg", "dataPkg",
			"ownedConfigurationItemPkgs", "ownedConfigurationItems", "itemIdentifier", "kind",
			"ownedConfigurationItems", "ownedConfigurationItemPkgs", "allocatedPhysicalArtifacts",
			"capellacommonAssociation1", "capellacommonAssociation2", "capellacommonAssociation3",
			"capellacommonAssociation4", "capellacommonAssociation5", "stateTransition", "capellacommonAssociation6",
			"state", "capellacommonAssociation7", "region", "capellacommonAssociation9", "stateMachine",
			"oaAssociation6", "statemachineAssociation11", "state", "statemachineAssociation12", "state",
			"statemachineAssociation13", "state", "statemachineAssociation13", "stateTransition",
			"statemachineAssociation14", "stateTransition", "ownedRegions", "incoming", "outgoing", "realizedStates",
			"realizingStates", "ownedRegions", "availableActivities/Functions", "entry", "do", "exit",
			"availableFunctionalChains", "availableOperationalProcesses", "availableCapabilities", "kind",
			"ownedStates", "triggerDescription", "source", "target", "triggers", "guard", "effects",
			"realizedStateTransitions", "realizingStateTransitions", "expression", "kind", "expression",
			"availableInStates", "interactionAssociation8", "scenario", "interactionAssociation4", "scenario",
			"interactionAssociation7", "scenario", "interactionAssociation1", "scenario", "interactionAssociation6",
			"scenario", "interactionAssociation2", "scenario", "interactionAssociation3", "scenario",
			"interactionAssociation5", "scenarioAssociation9", "instanceRole", "scenarioAssociation10",
			"sequenceMessage", "scenarioAssociation11", "sequenceMessage", "scenarioAssociation12", "sequenceMessage",
			"scenarioAssociation13", "scenarioAssociation14", "sequenceMessage", "scenarioAssociation15",
			"combinedFragment", "scenarioAssociation17", "stateFragment", "scenarioAssociation18", "stateFragment",
			"scenarioAssociation19", "stateFragment", "scenarioAssociation20", "scenario", "scenarioAssociation21",
			"combinedFragment", "scenarioAssociation22", "operand", "scenarioAssociation23", "operand",
			"scenarioAssociation24", "operand", "kind", "preCondition", "postCondition", "ownedInstanceRoles",
			"ownedMessages", "ownedStateFragments", "ownedCombinedFragments", "ownedConstraintDurations",
			"referencedScenarios", "realizedScenarios", "realizingScenarios", "representedInstance", "kind",
			"sendingInstanceRole", "receivingInstanceRole", "invokedExchange", "exchangedItems", "invokedOperation",
			"exchangeContext", "invokingSequenceMessages", "coveredInstanceRole", "relatedState",
			"relatedActivityFunction", "operator", "operands", "coveredInstanceRoles", "guard", "referencedMessages",
			"referencedFragments", "duration", "csAssociation2", "csAssociation3", "csAssociation4", "interfacePkg",
			"csAssociation5", "interfacePkg", "csAssociation6", "interfacePkg", "csAssociation7", "csAssociation8",
			"csAssociation9", "exchangeItem", "paAssociation5", "Capella Light MetamodelAssociation9", "nodePC",
			"paAssociation4", "paAssociation6", "csAssociation1", "csAssociation14", "csAssociation15",
			"csAssociation16", "Capella Light MetamodelAssociation21", "node", "csAssociation18", "csAssociation19",
			"interface", "csAssociation20", "exchangeItemAllocation", "csAssociation21", "exchangeItemElement",
			"containedPhysicalPorts", "physicalLinks", "involvingPhysicalPaths", "ownedStateMachines", "physicalLinks",
			"allocatedComponentPorts", "realizedPhysicalPorts", "realizingPhysicalPorts", "connectedPhysicalPorts",
			"categories", "involvingPhysicalPaths", "connectedComponents", "allocatedComponentExchanges",
			"realizedPhysicalLinks", "realizingPhysicalLinks", "links", "involvedPhysicalLinks", "involvedNodePCs",
			"allocatedComponentExchanges", "realizedPhysicalPaths", "realizingPhysicalPaths", "ownedInterfacePkgs",
			"ownedInterfaces", "ownedExchangeItems", "visibility", "ownedExchangeItemAllocations", "exchangeItems",
			"providingComponentPorts", "requiringComponentPorts", "userComponents", "implementorComponents", "super",
			"sub", "transmissionProtocol", "acquisitionProtocol", "allocatedItem", "invokingSequenceMessages",
			"abstract", "final", "exchangeMechanism", "ownedElements", "allocatorInterfaces", "super", "sub",
			"realizedExchangeItems", "realizingExchangeItems", "realizingOperations", "type", "faAssociation1",
			"faAssociation2", "faAssociation3", "faAssociation4", "faAssociation5", "faAssociation6", "functionalChain",
			"faAssociation7", "functionalChain", "faAssociation8", "faAssociation9", "faAssociation10",
			"functionalChain", "faAssociation15", "faAssociation16", "faAssociation18", "faAssociation19",
			"faAssociation6", "Capella Light MetamodelAssociation8", "behavioralComponent", "Association 19",
			"Property 1", "faAssociation20", "abstractFunction", "faAssociation21", "abstractFunction",
			"faAssociation22", "abstractFunction", "faAssociation23", "abstractFunction", "faAssociation23",
			"componentExchanges", "faAssociation24", "behavioralComponent", "faAssociation25", "behavioralComponent",
			"faAssociation26", "behavioralComponent", "faAssociation27", "faAssociation28", "faAssociation29",
			"faAssociation30", "faAssociation31", "functionalExchange", "faAssociation32", "componentExchange",
			"faAssociation33", "functionInputPort", "faAssociation34", "functionOutputPort", "faAssociation35",
			"abstractCapability", "faAssociation36", "abstractCapability", "faAssociation37", "abstractCapability",
			"faAssociation38", "faAssociation39", "faAssociation40", "faAssociation11", "faAssociation42",
			"faAssociation43", "abstractCapability", "Capella Light MetamodelAssociation10", "behavioralComponent",
			"kind", "condition", "inputs", "outputs", "incoming", "outgoing", "allocatingComponent",
			"ownedFunctionalChains", "involvingFunctionalChains", "involvingCapabilities", "allocatorComponentPort",
			"incomingFunctionalExchanges", "incomingExchangeItems", "realizedFunctionInputPorts",
			"realizingFunctionInputPorts", "outgoingFunctionalExchanges", "outgoingExchangeItems",
			"realizedFunctionOutputPorts", "realizingFunctionOutputPorts", "source", "target", "exchangedItems",
			"involvingFunctionalChains", "categories", "allocatingComponentExchange", "realizedFunctionalExchanges",
			"realizingFunctionalExchanges", "realizedInteractions", "exchanges", "preCondition", "postCondition",
			"involvedFunctions", "involvedFunctionalExchanges", "involvedFunctionalChains", "involvingCapabilities",
			"availableInStates", "realizedOperationalProcesses", "realizedFunctionalChains",
			"realizingFunctionalChains", "containedComponentPorts", "incomingComponentExchanges",
			"outgoingComponentExchanges", "inoutComponentExchanges", "allocatedFunctions", "usedInterfaces",
			"implementedInterfaces", "ownedStateMachines", "orientation", "componentExchanges",
			"allocatedFunctionPorts", "providedInterfaces", "requiredInterfaces", "allocatingPhysicalPorts",
			"realizedComponentPorts", "realizingComponentPorts", "connectedComponentPorts", "connectedComponents",
			"categories", "allocatedFunctionalExchanges", "convoyedInformations", "allocatingPhysicalLink",
			"allocatingPhysicalPath", "realizedCommunicationMeans", "realizedComponentExchanges",
			"realizingComponentExchanges", "kind", "exchanges", "preCondition", "postCondition", "ownedScenarios",
			"super", "sub", "includedCapabilities", "includingCapabilities", "extendedCapabilities",
			"extendingCapabilities", "availableInStates", "ownedFunctionalChains", "involvedFunctionalChains",
			"involvedFunctions", "classesAssociation1", "class", "classesAssociation2", "class", "classesAssociation3",
			"union", "classesAssociation4", "union", "classesAssociation5", "union", "classesAssociation6",
			"collection", "classesAssociation7", "union", "classesAssociation9", "operation", "classesAssociation10",
			"operation", "classesAssociation11", "Capella Light MetamodelAssociation41", "collection",
			"Capella Light MetamodelAssociation42", "collection", "classesAssociation13", "property", "abstract",
			"final", "primitive", "visibility", "containedProperties", "containedOperations", "ordered", "unique",
			"minInclusive", "maxInclusive", "abstract", "final", "primitive", "collectionKind", "aggregationKind",
			"visibility", "containedOperations", "minCard", "maxCard", "final", "containedUnionProperties",
			"discriminant", "defaultProperty", "kind", "containedOperations", "type", "visibility",
			"realizedExchangeItems", "ownedParameters", "thrownExceptions", "abstract", "visibility", "super", "sub",
			"datatypeAssociation1", "physicalQuantity", "datatypeAssociation2", "booleanType", "datatypeAssociation3",
			"enumeration", "datatypeAssociation4", "enumeration", "datatypeAssociation5", "enumeration",
			"datatypeAssociation6", "enumeration", "datatypeAssociation7", "enumeration", "datatypeAssociation8",
			"datatypeAssociation9", "Capella Light MetamodelAssociation35", "stringType",
			"Capella Light MetamodelAssociation33", "numericType", "Capella Light MetamodelAssociation39",
			"booleanType", "Capella Light MetamodelAssociation32", "numericType",
			"Capella Light MetamodelAssociation38", "stringType", "Capella Light MetamodelAssociation37", "stringType",
			"Capella Light MetamodelAssociation40", "enumeration", "Capella Light MetamodelAssociation31",
			"numericType", "Capella Light MetamodelAssociation34", "numericType",
			"Capella Light MetamodelAssociation36", "stringType", "abstract", "final", "discrete", "visibility",
			"super", "sub", "realizedInformations", "realizingInformations", "minInclusive", "maxInclusive", "pattern",
			"ownedLiterals", "defaultValue", "minValue", "maxValue", "nullValue", "domainType", "ownedLiterals",
			"defaultValue", "minInclusive", "maxInclusive", "pattern", "minLength", "maxLength", "defaultValue",
			"nullValue", "minInclusive", "maxInclusive", "pattern", "kind", "minValue", "maxValue", "defaultValue",
			"nullValue", "unit", "RequirementAssociation2", "folder", "RequirementAssociation3", "requirement",
			"RequirementAssociation3", "capellaModule", "ownedRequirements", "id", "longName", "name", "prefix", "id",
			"longName", "name", "chapterName", "prefix", "text", "ownedAttributes", "ownedRequirements", "name",
			"value", "kind", "System", "Root Logical Function", "Logical System", "Root Physical Function",
			"Physical System", "System"));

	private Map<String, String> classRenames = initClassRenames();

	private Map<String, String> featureRenames = initFeatureRenames();

	/**
	 * The new line separator.
	 */
	private static final String NL = System.lineSeparator();

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		final Set<EPackage> capellaPackages = new LinkedHashSet<>();
		final Set<EPackage> siriusPackages = new LinkedHashSet<>();
		final Map<String, List<ICategory>> queries = getQueryMapping();

		for (Object registered : new ArrayList<>(EPackage.Registry.INSTANCE.values())) {
			if (registered instanceof Descriptor) {
				boolean addEPackage = false;
				try {
					addEPackage = ((Descriptor) registered).getEPackage().getNsURI().contains("capella");
				} catch (Exception e) {
					// nothing to do here
				}
				if (addEPackage) {
					capellaPackages.addAll(getAllEpackages(((Descriptor) registered).getEPackage()));
				}
			} else if (registered instanceof EPackage) {
				if (((EPackage) registered).getNsURI().contains("capella")) {
					capellaPackages.addAll(getAllEpackages((EPackage) registered));
				} else if (((EPackage) registered).getNsURI().contains("sirius")) {
					siriusPackages.addAll(getAllEpackages((EPackage) registered));
				}
			}
		}

		createPythonAPI("capella", capellaPackages, queries);
		queries.clear();
		// createPythonAPI("sirius", siriusPackages, queries);

		return null;
	}

	private String getClassAdditions(String clsName) {
		String res = "";

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/additions/classes/" + clsName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));

		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private String getPackageAdditions(String pkgName) {
		String res = "";

		try (InputStream is = getClass().getClassLoader()
				.getResourceAsStream("resources/additions/packages/" + pkgName + ".txt");) {
			res = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8)).lines()
					.collect(Collectors.joining(NL));

		} catch (Exception e) {
			// nothing to do here
		}

		return res;
	}

	private Map<String, String> initFeatureRenames() {
		final Map<String, String> res = new HashMap<>();

		res.put("Capability.extendedAbstractCapabilities", "extendedCapabilities");
		res.put("Capability.extendingAbstractCapabilities", "extendingCapabilities");
		res.put("Capability.includedAbstractCapabilities", "includedCapabilities");
		res.put("Capability.includingAbstractCapabilities", "includingCapabilities");
		res.put("CapabilityRealization.extendedAbstractCapabilities", "extendedCapabilities");
		res.put("CapabilityRealization.extendingAbstractCapabilities", "extendingCapabilities");
		res.put("CapabilityRealization.includedAbstractCapabilities", "includedCapabilities");
		res.put("CapabilityRealization.includingAbstractCapabilities", "includingCapabilities");
		res.put("EPBSArchitecture.containedCapabilityRealizationPkg", "capabilityRealizationPkg");
		res.put("EPBSArchitecture.ownedConfigurationItemPkg", "configurationItemPkg");
		res.put("EPBSArchitecture.ownedDataPkg", "dataPkg");
		res.put("FunctionalChain.realizedFunctionalChains", "involvedFunctionalChains");
		res.put("FunctionInputPort.representedComponentPort", "allocatorComponentPort");
		res.put("FunctionOutputPort.representedComponentPort", "allocatorComponentPort");
		res.put("LogicalArchitecture.containedCapabilityRealizationPkg", "capabilityRealizationPkg");
		res.put("LogicalArchitecture.containedLogicalFunctionPkg", "logicalFunctionPkg");
		res.put("LogicalArchitecture.ownedDataPkg", "dataPkg");
		res.put("LogicalArchitecture.ownedInterfacePkg", "interfacePkg");
		res.put("LogicalArchitecture.ownedLogicalComponentPkg", "logicalComponentPkg");
		// TODO
		// res.put("LogicalComponent.ownedComponentExchanges","incomingComponentExchanges");
		// TODO
		// res.put("LogicalComponent.ownedComponentExchanges","inoutComponentExchanges");
		// TODO
		// res.put("LogicalComponent.ownedComponentExchanges","outgoingComponentExchanges");
		res.put("Mode.availableAbstractCapabilities", "availableCapabilities");
		res.put("Mode.realizedAbstractStates", "realizedStates");
		res.put("Mode.realizingAbstractStates", "realizingStates");
		// TODO
		// res.put("OperationalActivity.ownedProcess","involvingOperationalProcesses");
		// TODO
		// res.put("OperationalActivity.ownedProcess","ownedOperationalProcesses");
		res.put("OperationalAnalysis.containedOperationalActivityPkg", "operationalActivityPkg");
		res.put("OperationalAnalysis.containedOperationalCapabilityPkg", "operationalCapabilityPkg");
		res.put("OperationalAnalysis.ownedDataPkg", "dataPkg");
		res.put("OperationalAnalysis.ownedEntityPkg", "entityPkg");
		res.put("OperationalAnalysis.ownedInterfacePkg", "interfacePkg");
		res.put("OperationalCapability.extendedAbstractCapabilities", "extendedCapabilities");
		res.put("OperationalCapability.extendingAbstractCapabilities", "extendingCapabilities");
		res.put("OperationalCapability.includedAbstractCapabilities", "includedCapabilities");
		res.put("OperationalCapability.includingAbstractCapabilities", "includingCapabilities");
		res.put("PhysicalArchitecture.containedCapabilityRealizationPkg", "capabilityRealizationPkg");
		res.put("PhysicalArchitecture.containedPhysicalFunctionPkg", "physicalFunctionPkg");
		res.put("PhysicalArchitecture.ownedDataPkg", "dataPkg");
		res.put("PhysicalArchitecture.ownedInterfacePkg", "interfacePkg");
		res.put("PhysicalArchitecture.ownedPhysicalComponentPkg", "physicalComponentPkg");
		res.put("PhysicalPort.involvedLinks", "physicalLinks");
		res.put("Pseudostate.realizedAbstractStates", "realizedStates");
		res.put("Pseudostate.realizingAbstractStates", "realizingStates");
		res.put("State.availableAbstractCapabilities", "availableCapabilities");
		res.put("State.realizedAbstractStates", "realizedStates");
		res.put("State.realizingAbstractStates", "realizingStates");
		res.put("SystemAnalysis.containedCapabilityPkg", "capabilityPkg");
		res.put("SystemAnalysis.containedSystemFunctionPkg", "systemFunctionPkg");
		res.put("SystemAnalysis.ownedDataPkg", "dataPkg");
		res.put("SystemAnalysis.ownedInterfacePkg", "interfacePkg");
		res.put("SystemAnalysis.ownedMissionPkg", "missionPkg");
		res.put("SystemAnalysis.ownedSystemComponentPkg", "systemComponentPkg");
		res.put("PublishableElement.visibleInDoc", "visibleInDocumentation");
		res.put("PublishableElement.visibleInLM", "visibleForTraceability");

		return res;
	}

	private Map<String, String> initClassRenames() {
		final Map<String, String> res = new HashMap<>();

		return res;
	}

	private void createPythonAPI(String apiName, Set<EPackage> ePackages, Map<String, List<ICategory>> queries) {
		final File file = new File("/tmp/" + apiName + "/" + apiName + ".py");

		final List<EClass> orderedEClasses = new ArrayList<>();
		final Set<EClass> remainingEClasses = new LinkedHashSet<>();
		final Set<EClass> knwonEClasses = new HashSet<>();
		for (EPackage ePkg : ePackages) {
			for (EClassifier eClassifier : ePkg.getEClassifiers()) {
				if (eClassifier instanceof EClass) {
					final EClass eCls = (EClass) eClassifier;
					remainingEClasses.addAll(eCls.getEAllSuperTypes());
					remainingEClasses.add(eCls);
				}
			}
		}

		while (!remainingEClasses.isEmpty()) {
			final List<EClass> toRemove = new ArrayList<>();
			for (EClass eCls : remainingEClasses) {
				if (knwonEClasses.containsAll(eCls.getESuperTypes())) {
					orderedEClasses.add(eCls);
					knwonEClasses.add(eCls);
					toRemove.add(eCls);
				}
			}
			remainingEClasses.removeAll(toRemove);
		}

		try {
			if (!file.exists()) {
				file.getParentFile().mkdirs();
				file.createNewFile();
			}
			try (OutputStream os = new FileOutputStream(file)) {
				final Set<EPackage> toImport = new LinkedHashSet<>();
				final StringBuilder pythonClassesStringBuilder = new StringBuilder();
				for (EClass eCls : orderedEClasses) {
					pythonClassesStringBuilder.append(getPythonEClass((EClass) eCls, queries, toImport));
				}
				os.write(getPythonHeader(apiName, toImport).getBytes());
				os.write(pythonClassesStringBuilder.toString().getBytes());
				os.write(getPackageAdditions(apiName).getBytes());
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private String getPythonHeader(String apiName, Set<EPackage> toImport) {
		final StringBuilder res = new StringBuilder();

		res.append("include('workspace://Python4Capella/java_api/EMF_API.py')" + NL);
		res.append("if False:" + NL);
		res.append("    from java_api.EMF_API import *" + NL);
		res.append("include('workspace://Python4Capella/java_api/Capella_API.py')" + NL);
		res.append("if False:" + NL);
		res.append("    from java_api.Capella_API import *" + NL);
		res.append("include('workspace://Python4Capella/simplified_api/sirius.py')" + NL);
		res.append("if False:" + NL);
		res.append("    from simplified_api.sirius import *" + NL);
		res.append(NL);
		res.append(NL);

		return res.toString();
	}

	private String getPythonEClass(EClass eCls, Map<String, List<ICategory>> queries, Set<EPackage> toImport) {
		final StringBuilder res = new StringBuilder();

		final String superClassNames;
		if (eCls.getESuperTypes().isEmpty()) {
			superClassNames = "EObject";
		} else {
			final StringJoiner joiner = new StringJoiner(", ");
			for (EClass eSuperCls : eCls.getESuperTypes()) {
				joiner.add(getPythonClassName(eSuperCls));
				if (eSuperCls.getEPackage() != eCls.getEPackage()) {
					toImport.add(eSuperCls.getEPackage());
				}
			}
			superClassNames = joiner.toString();
		}
		res.append("class " + getPythonClassName(eCls) + "(" + superClassNames + "):" + NL);
		res.append("    def __init__(self, java_object = None):" + NL);
		res.append("        if java_object is None:" + NL);
		final String nsURIString;
		if (eCls.getEPackage().getNsURI().contains("capella")) {
			nsURIString = "\""
					+ eCls.getEPackage().getNsURI().substring(0, eCls.getEPackage().getNsURI().lastIndexOf("/") + 1)
					+ "\"" + " + capella_version()";
		} else {
			nsURIString = "\"" + eCls.getEPackage().getNsURI() + "\"";
		}

		res.append("            JavaObject.__init__(self, create_e_object(" + nsURIString + ", \""
				+ getPythonClassName(eCls) + "\"))" + NL);
		res.append("        elif isinstance(java_object, " + getPythonClassName(eCls) + "):" + NL);
		res.append("            JavaObject.__init__(self, java_object.get_java_object())" + NL);
		res.append("        else:" + NL);
		res.append("            JavaObject.__init__(self, java_object)" + NL);

		final Set<String> pythonClassMembers = new HashSet<>();
		for (EStructuralFeature feature : eCls.getEStructuralFeatures()) {
			if (feature.getEType().getEPackage() != eCls.getEPackage()) {
				toImport.add(feature.getEType().getEPackage());
			}

			final String featureName = featureRenames.getOrDefault(eCls.getName() + "." + feature.getName(),
					feature.getName());
			if (TO_KEEP.contains(featureName)) {
				if (feature instanceof EAttribute) {
					res.append(getPythonAttribute((EAttribute) feature, featureName, pythonClassMembers));
				} else if (feature instanceof EReference) {
					res.append(getPythonReference((EReference) feature, featureName, pythonClassMembers));
				} else {
					throw new IllegalStateException();
				}
			} else {
//				System.out.println(
//						"Rejected feature: " + feature.getEContainingClass().getName() + "." + feature.getName());
			}
		}
		// TODO eOperations
		final Set<String> knownQueries = new HashSet<>();
		final List<ICategory> categories = queries.get(eCls.getInstanceClass().getCanonicalName());
		if (categories != null) {
			for (ICategory category : categories) {
				final IQuery query = getQuery(category);
				if (knownQueries.add(query.getClass().getCanonicalName())) {
					final String getterName = "get_" + getCategoryPythonName(category.getName());
					System.out.println(
							"res.add(\"" + eCls.getName() + "." + getCategoryPythonName(category.getName()) + "\");");
					if (pythonClassMembers.add(getterName)) {
						res.append("    def " + getterName + "(self):" + NL);
						res.append("        return capella_query(\"" + query.getClass().getCanonicalName() + "\", self)"
								+ NL);
					}
//					System.out.println("public List<Object> get" + getCategoryJavaName(category.getName()) + "("
//							+ eCls.getName() + " value) { return castList(new " + query.getClass().getCanonicalName()
//							+ "().compute(value));}");
				}
			}
		}
		res.append(getClassAdditions(eCls.getName()));
		res.append(NL);
		return res.toString();
	}

	private IQuery getQuery(ICategory category) {
		for (Field field : category.getClass().getDeclaredFields()) {
			if ("categoryQuery".equals(field.getName())) {
				field.setAccessible(true);
				try {
					return (IQuery) field.get(category);
				} catch (IllegalArgumentException | IllegalAccessException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		throw new IllegalStateException();
	}

	private String getCategoryPythonName(String name) {
		final StringBuilder res = new StringBuilder();

		res.append(Character.toLowerCase(name.charAt(0)));
		for (int i = 1; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isLetterOrDigit(c)) {
				res.append(c);
			} else if (c == ' ') {
				// skip
			} else {
				break;
			}
		}

		if (res.charAt(res.length() - 1) == '_') {
			return getPythonName(res.substring(0, res.length() - 1).trim());
		} else {
			return getPythonName(res.toString().trim());
		}
	}

	private String getCategoryJavaName(String name) {
		final StringBuilder res = new StringBuilder();

		boolean toUpper = true;
		for (int i = 0; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isLetterOrDigit(c)) {
				if (toUpper) {
					res.append(Character.toUpperCase(c));
				} else {
					res.append(c);
				}
				toUpper = false;
			} else {
				toUpper = true;
			}
		}

		if (res.charAt(res.length() - 1) == '_') {
			return res.substring(0, res.length() - 1).trim();
		} else {
			return res.toString().trim();
		}
	}

	private Object getPythonAttribute(EAttribute attr, String featureName, Set<String> pythonClassMembers) {
		final StringBuilder res = new StringBuilder();

		// TODO isMany
		final String attributeName = getPythonName(featureName);
		final String getterName = "get_" + attributeName;
		pythonClassMembers.add(getterName);
		final String setterName = "set_" + attributeName;
		pythonClassMembers.add(setterName);
		res.append("    def " + getterName + "(self):" + NL);
		if (attr.getEType() instanceof EEnum) {
			res.append("        return self.get_java_object()." + getJavaGetterName(attr) + "().getName()" + NL);
		} else {
			res.append("        return self.get_java_object()." + getJavaGetterName(attr) + "()" + NL);
		}
		if (attr.isChangeable() && !attr.isDerived()) {
			res.append("    def " + setterName + "(self, value):" + NL);
			res.append("        self.get_java_object()." + getJavaSetterName(attr) + "(value)" + NL);
		}

		return res;
	}

	private String getJavaGetterName(EStructuralFeature feature) {
		if (feature.getEType() == EcorePackage.eINSTANCE.getEBoolean()) {
			return "is" + Character.toUpperCase(feature.getName().charAt(0)) + feature.getName().substring(1);
		} else {
			return "get" + Character.toUpperCase(feature.getName().charAt(0)) + feature.getName().substring(1);
		}
	}

	private String getJavaSetterName(EStructuralFeature feature) {
		return "set" + Character.toUpperCase(feature.getName().charAt(0)) + feature.getName().substring(1);
	}

	private Object getPythonReference(EReference ref, String featureName, Set<String> pythonClassMembers) {
		final StringBuilder res = new StringBuilder();

		final String getterName = "get_" + getPythonName(featureName);
		pythonClassMembers.add(getterName);
		res.append("    def " + getterName + "(self):" + NL);
		if (ref.isMany()) {
			res.append("        return create_e_list(self.get_java_object()." + getJavaGetterName(ref) + "(), "
					+ getPythonClassName(ref.getEType()) + ")" + NL);
		} else {
			res.append("        value =  self.get_java_object()." + getJavaGetterName(ref) + "()" + NL);
			res.append("        if value is None:" + NL);
			res.append("            return value" + NL);
			res.append("        else:" + NL);
			res.append("            specific_cls = getattr(sys.modules[\"__main__\"], value.eClass().getName())" + NL);
			res.append("            return specific_cls(value)" + NL);
			if (ref.isChangeable() && !ref.isDerived()) {
				res.append("    def set_" + getPythonName(featureName) + "(self, value):" + NL);
				res.append("        return self.get_java_object()." + getJavaSetterName(ref)
						+ "(value.get_java_object())" + NL);
			}
		}

		return res;
	}

	public static String getPythonName(String name) {
		final StringBuilder res = new StringBuilder();

		for (int i = 0; i < name.length(); i++) {
			final char c = name.charAt(i);
			if (Character.isUpperCase(c)) {
				res.append("_");
				res.append(Character.toLowerCase(c));
			} else {
				res.append(c);
			}
		}

		return res.toString();
	}

	private List<EPackage> getAllEpackages(EPackage ePackage) {
		final List<EPackage> res = new ArrayList<>();

		res.add(ePackage);
		for (EPackage child : ePackage.getESubpackages()) {
			res.addAll(getAllEpackages(child));
		}

		return res;
	}

	private Map<String, List<ICategory>> getQueryMapping() {
		final Map<String, List<ICategory>> res = new HashMap<>();

		final CategoryRegistry registry = CategoryRegistry.getInstance();
		final Set<String> fields = new HashSet<>();
		fields.add("currentElementRegistry");
		fields.add("diagramElementRegistry");
		fields.add("referencedElementRegistry");
		fields.add("referencingElementRegistry");
		fields.add("relatedElementsRegistry");
		for (Field field : registry.getClass().getDeclaredFields()) {
			if (fields.contains(field.getName())) {
				field.setAccessible(true);
				try {
					HashMap<String, ICategory> map = (HashMap<String, ICategory>) field.get(registry);
					for (ICategory category : map.values()) {
						res.computeIfAbsent(category.getTypeFullyQualifiedName(), t -> new ArrayList<>()).add(category);
					}
				} catch (IllegalArgumentException | IllegalAccessException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}

		return res;
	}

	private String getPythonClassName(EClassifier eClassifier) {
		final String res;

		if ("Exception".equals(eClassifier.getName())) {
			res = "ExceptionCapella";
		} else {
			res = eClassifier.getName();
		}

		return res;
	}

}
