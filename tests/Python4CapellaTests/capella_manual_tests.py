include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

include('workspace://Python4Capella/simplified_api/requirement.py')
if False:
    from simplified_api.requirement import *

include('workspace://Python4Capella/simplified_api/pvmt.py')
if False:
    from simplified_api.pvmt import *

import unittest

class capella_manual_tests(unittest.TestCase):

    def test_new_LogicalComponent(self):
        lc = LogicalComponent()
        self.assertEqual(False, lc.get_java_object().isActor())
        pass

    def test_new_LogicalComponent_invalid_java_object(self):
        la = LogicalActor()
        with self.assertRaises(AttributeError) as context:
            LogicalComponent(la.get_java_object())
        self.assertEqual("Passed component is an actor.", str(context.exception))
        pass

    def test_new_LogicalActor(self):
        la = LogicalActor()
        self.assertEqual(True, la.get_java_object().isActor())
        pass

    def test_LogicalComponent_get_class(self):
        lc = LogicalComponent()
        self.assertEqual(LogicalComponent, EObject.get_class(lc.get_java_object()))
        pass

    def test_LogicalSystem_get_class(self):
        la = LogicalArchitecture()
        lc_pkg = LogicalComponentPkg()
        la.get_java_object().setOwnedLogicalComponentPkg(lc_pkg.get_java_object())
        lc = LogicalComponent()
        lc_pkg.get_owned_logical_components().add(lc)
        self.assertEqual(LogicalSystem, EObject.get_class(lc.get_java_object()))
        pass

    def test_LogicalActor_get_class(self):
        la = LogicalActor()
        self.assertEqual(LogicalActor, EObject.get_class(la.get_java_object()))
        pass


    def test_new_LogicalActor_invalid_java_object(self):
        lc = LogicalComponent()
        with self.assertRaises(AttributeError) as context:
            LogicalActor(lc.get_java_object())
        self.assertEqual("Passed component is not an actor.", str(context.exception))
        pass


    def test_new_PhysicalComponent(self):
        pc = PhysicalComponent()
        self.assertEqual(False, pc.get_java_object().isActor())
        pass

    def test_new_PhysicalComponent_invalid_java_object_actor(self):
        pa = PhysicalActor()
        with self.assertRaises(AttributeError) as context:
            PhysicalComponent(pa.get_java_object())
        self.assertEqual("Passed component is an actor.", str(context.exception))
        pass

    def test_new_PhysicalComponent_invalid_java_object_behavior(self):
        bpc = BehaviorPC()
        with self.assertRaises(AttributeError) as context:
            PhysicalComponent(bpc.get_java_object())
        self.assertEqual("Passed component is a behavior physical component.", str(context.exception))
        pass

    def test_new_PhysicalComponent_invalid_java_object_node(self):
        npc = NodePC()
        with self.assertRaises(AttributeError) as context:
            PhysicalComponent(npc.get_java_object())
        self.assertEqual("Passed component is a node physical component.", str(context.exception))
        pass

    def test_new_PhysicalActor(self):
        pa = PhysicalActor()
        self.assertEqual(True, pa.get_java_object().isActor())
        pass

    def test_new_BehaviorPC(self):
        bpc = BehaviorPC()
        self.assertEqual("BEHAVIOR", bpc.get_java_object().getNature().getName())
        pass

    def test_new_NodePC(self):
        npc = NodePC()
        self.assertEqual("NODE", npc.get_java_object().getNature().getName())
        pass

    def test_PhysicalComponent_get_class(self):
        pc = PhysicalComponent()
        self.assertEqual(PhysicalComponent, EObject.get_class(pc.get_java_object()))
        pass

    def test_PhysicalActor_get_class(self):
        pa = PhysicalActor()
        self.assertEqual(PhysicalActor, EObject.get_class(pa.get_java_object()))
        pass

    def test_PhysicalSystem_get_class(self):
        pa = PhysicalArchitecture();
        pc_pkg = PhysicalComponentPkg()
        pa.get_java_object().setOwnedPhysicalComponentPkg(pc_pkg.get_java_object())
        pc = PhysicalComponent()
        pc_pkg.get_owned_physical_components().add(pc)
        self.assertEqual(PhysicalSystem, EObject.get_class(pc.get_java_object()))
        pass

    def test_BehaviorPC_get_class(self):
        bpc = BehaviorPC()
        self.assertEqual(BehaviorPC, EObject.get_class(bpc.get_java_object()))
        pass

    def test_NodePC_get_class(self):
        npc = NodePC()
        self.assertEqual(NodePC, EObject.get_class(npc.get_java_object()))
        pass

    def test_new_PhysicalActor_invalid_java_object(self):
        pc = PhysicalComponent()
        with self.assertRaises(AttributeError) as context:
            PhysicalActor(pc.get_java_object())
        self.assertEqual("Passed component is not an actor.", str(context.exception))
        pass

    def test_new_BehaviorPC_invalid_java_object(self):
        pc = PhysicalComponent()
        with self.assertRaises(AttributeError) as context:
            BehaviorPC(pc.get_java_object())
        self.assertEqual("Passed component is a physical component.", str(context.exception))
        pass

    def test_new_NodePC_invalid_java_object(self):
        pc = PhysicalComponent()
        with self.assertRaises(AttributeError) as context:
            NodePC(pc.get_java_object())
        self.assertEqual("Passed component is a physical component.", str(context.exception))
        pass

    def test_new_OperationalEntity(self):
        oe = OperationalEntity()
        self.assertEqual(False, oe.get_java_object().isActor())
        pass

    def test_new_OperationalEntity_invalid_java_object(self):
        oa = OperationalActor()
        with self.assertRaises(AttributeError) as context:
            OperationalEntity(oa.get_java_object())
        self.assertEqual("Passed entity is an actor.", str(context.exception))
        pass

    def test_new_OperationalActor(self):
        oa = OperationalActor()
        self.assertEqual(True, oa.get_java_object().isActor())
        pass

    def test_OperationalEntity_get_class(self):
        oe = OperationalEntity()
        self.assertEqual(OperationalEntity, EObject.get_class(oe.get_java_object()))
        pass

    def test_OperationalActor_get_class(self):
        oa = OperationalActor()
        self.assertEqual(OperationalActor, EObject.get_class(oa.get_java_object()))
        pass

    def test_new_OperationalActor_invalid_java_object(self):
        oe = OperationalEntity()
        with self.assertRaises(AttributeError) as context:
            OperationalActor(oe.get_java_object())
        self.assertEqual("Passed entity is not an actor.", str(context.exception))
        pass

    def test_Operand_get_class(self):
        o = Operand()
        self.assertEqual(Operand, EObject.get_class(o.get_java_object()))
        pass

    def test_new_Operand(self):
        oa = Operand()
        self.assertEqual("InteractionOperand", oa.get_java_object().eClass().getName())
        pass

    def test_new_REC(self):
        rec = REC()
        self.assertEqual("REC", rec.get_java_object().getKind().getName())
        pass

    def test_new_REC_invalid_java_object(self):
        rpl = RPL()
        with self.assertRaises(AttributeError) as context:
            REC(rpl.get_java_object())
        self.assertEqual("Passed catalog element is not a REC.", str(context.exception))
        pass

    def test_new_RPL(self):
        rpl = RPL()
        self.assertEqual("RPL", rpl.get_java_object().getKind().getName())
        pass

    def test_REC_get_class(self):
        rec = REC()
        self.assertEqual(REC, EObject.get_class(rec.get_java_object()))
        pass

    def test_RPL_get_class(self):
        rpl = RPL()
        self.assertEqual(RPL, EObject.get_class(rpl.get_java_object()))
        pass


    def test_new_RPL_invalid_java_object(self):
        rec = REC()
        with self.assertRaises(AttributeError) as context:
            RPL(rec.get_java_object())
        self.assertEqual("Passed catalog element is not a RPL.", str(context.exception))
        pass

    def test_Operation_get_class(self):
        o = Operation()
        self.assertEqual(Operation, EObject.get_class(o.get_java_object()))
        pass

    def test_set_in_capella(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        self.assertEqual("In-Flight Entertainment System", se.get_name())
        model.start_transaction()
        try:
            se.set_name("Some name")
            self.assertEqual("Some name", se.get_name())
        except:
            self.fail("transaction failed")
        else:
            model.commit_transaction()
            pass
        model.start_transaction()
        try:
            se.set_name("In-Flight Entertainment System")
            self.assertEqual("In-Flight Entertainment System", se.get_name())
        except:
            self.fail("transaction failed")
        else:
            model.commit_transaction()
            pass

    def test_FunctionalChain_involved_functions(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for fc in se.get_all_contents_by_type(FunctionalChain):
            #: :type fc: FunctionalChain
            if fc.get_name() == 'Broadcast Audio Announcement':
                tested = fc
                break
        involved_functions = tested.get_involved_functions()
        self.assertEqual(6, len(involved_functions))
        self.assertEqual("Perform Cabin Management Activities", involved_functions[0].get_name())
        self.assertEqual("Send Audio Announcement", involved_functions[1].get_name())
        self.assertEqual("Provide Aircraft Information, Commands and Means", involved_functions[2].get_name())
        self.assertEqual("Broadcast Audio Video Streams", involved_functions[3].get_name())
        self.assertEqual("Manage Passenger Service Interruptions", involved_functions[4].get_name())
        self.assertEqual("Listen to Audio Announcement", involved_functions[5].get_name())

    def test_Mission_involved_actors_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for mission in se.get_all_contents_by_type(Mission):
            #: :type mission: Mission
            if mission.get_name() == 'Provide Cabin Management Solutions':
                tested = mission
                break
        involved_actors = tested.get_involved_actors()
        self.assertEqual(3, len(involved_actors))
        self.assertEqual("Cabin Crew", involved_actors[0].get_name())
        self.assertEqual("Passenger", involved_actors[1].get_name())
        self.assertEqual("Aircraft", involved_actors[2].get_name())

    def test_OperationalProcess_involved_interactions_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for operational_process in se.get_all_contents_by_type(OperationalProcess):
            #: :type operational_process: OperationalProcess
            if operational_process.get_name() == 'Broadcast Safety Instructions Movie':
                tested = operational_process
                break
        involved_interactions = tested.get_involved_interactions()
        self.assertEqual(2, len(involved_interactions))
        self.assertEqual("Safety Instructions", involved_interactions[0].get_name())
        self.assertEqual("Imposed Movie", involved_interactions[1].get_name())

    def test_OperationalProcess_involved_operational_activities_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for operational_process in se.get_all_contents_by_type(OperationalProcess):
            #: :type operational_process: OperationalProcess
            if operational_process.get_name() == 'Broadcast Safety Instructions Movie':
                tested = operational_process
                break
        involved_activities = tested.get_involved_operational_activities()
        self.assertEqual(3, len(involved_activities))
        self.assertEqual("Broadcast Movies", involved_activities[0].get_name())
        self.assertEqual("Play Imposed Movie", involved_activities[1].get_name())
        self.assertEqual("Watch Movie", involved_activities[2].get_name())

    def test_CapabilityRealization_owned_functional_chains_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for cr in se.get_all_contents_by_type(CapabilityRealization):
            #: :type cr: CapabilityRealization
            if cr.get_name() == 'Provide Audio and Video Intercommunication Means':
                tested = cr
                break
        fc = tested.get_owned_functional_chains()
        self.assertEqual(5, fc.size())
        self.assertEqual("Watch Imposed Video on Cabin Screen", fc.get(0).get_name())
        self.assertEqual("Watch Imposed Video on Private Screen", fc.get(1).get_name())
        self.assertEqual("Broadcast Audio Announcement", fc.get(2).get_name())
        self.assertEqual("Stop Playing Imposed Video [NOT DONE]", fc.get(3).get_name())
        self.assertEqual("Pause Running Imposed Video [NOT DONE]", fc.get(4).get_name())

    def test_CapabilityRealization_owned_scenarios_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for cr in se.get_all_contents_by_type(CapabilityRealization):
            #: :type cr: CapabilityRealization
            if cr.get_name() == 'Provide Audio and Video Intercommunication Means':
                tested = cr
                break
        scenarii = tested.get_owned_scenarios()
        self.assertEqual(2, scenarii.size())
        self.assertEqual("[FS] Perform Audio Announcement", scenarii.get(0).get_name())
        self.assertEqual("[ES] Perform Audio Announcement", scenarii.get(1).get_name())

    def test_Capability_purpose_missions_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for capability in se.get_all_contents_by_type(Capability):
            #: :type capability: Capability
            if capability.get_name() == 'Provide Audio and Video Intercommunication Means':
                tested = capability
                break
        missions = tested.get_purpose_missions()
        self.assertEqual(1, missions.size())
        self.assertEqual("Provide Cabin Management Solutions", missions.get(0).get_name())

    def test_FunctionalChain_involving_capabilities_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for fc in se.get_all_contents_by_type(FunctionalChain):
            #: :type fc: FunctionalChain
            if fc.get_name() == 'Watch Imposed Video on Cabin Screen':
                tested = fc
                break
        capabilities = tested.get_involving_capabilities()
        self.assertEqual(1, len(capabilities))
        self.assertEqual("Provide Audio and Video Intercommunication Means", capabilities[0].get_name())

    def test_Mission_exploited_capabilities_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for mission in se.get_all_contents_by_type(Mission):
            #: :type mission: Mission
            if mission.get_name() == 'Provide Entertainement Solutions':
                tested = mission
                break
        capabilities = tested.get_exploited_capabilities()
        self.assertEqual(4, len(capabilities))
        self.assertEqual("Provide Moving-Map Services", capabilities[0].get_name())
        self.assertEqual("Provide Audio Entertainment Services", capabilities[1].get_name())
        self.assertEqual("Provide Video Entertainment Services", capabilities[2].get_name())
        self.assertEqual("Provide Video Gaming Services", capabilities[3].get_name())

    def test_Capability_involved_functional_chains_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for capability in se.get_all_contents_by_type(Capability):
            #: :type capability: Capability
            if capability.get_name() == 'Provide Audio and Video Intercommunication Means':
                tested = capability
                break
        functional_chains = tested.get_involved_functional_chains()
        self.assertEqual(5, functional_chains.size())
        self.assertEqual("Pause Running Imposed Video [NOT DONE]", functional_chains.get(0).get_name())
        self.assertEqual("Stop Playing Imposed Video [NOT DONE]", functional_chains.get(1).get_name())
        self.assertEqual("Watch Imposed Video on Cabin Screen", functional_chains.get(2).get_name())
        self.assertEqual("Broadcast Audio Announcement", functional_chains.get(3).get_name())
        self.assertEqual("Watch Imposed Video on Private Screen", functional_chains.get(4).get_name())

    def test_OperationalProcess_involving_operational_capabilities_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for operational_process in se.get_all_contents_by_type(OperationalProcess):
            #: :type operational_process: OperationalProcess
            if operational_process.get_name() == 'Broadcast Safety Instructions Movie':
                tested = operational_process
                break
        capabilities = tested.get_involving_operational_capabilities()
        self.assertEqual(0, capabilities.size())

    def test_OperationalProcess_realizing_functional_chains_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for operational_process in se.get_all_contents_by_type(OperationalProcess):
            #: :type operational_process: OperationalProcess
            if operational_process.get_name() == 'Broadcast Safety Instructions Movie':
                tested = operational_process
                break
        functional_chains = tested.get_realizing_functional_chains()
        self.assertEqual(0, functional_chains.size())

    def test_PhysicalPath_involved_physical_links_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for physical_path in se.get_all_contents_by_type(PhysicalPath):
            #: :type physical_path: PhysicalPath
            if physical_path.get_name() == 'Network Path':
                tested = physical_path
                break
        physical_links = tested.get_involved_physical_links()
        self.assertEqual(4, len(physical_links))
        self.assertEqual("Ethernet Connector", physical_links[0].get_name())
        self.assertEqual("Gigabit Ethernet", physical_links[1].get_name())
        self.assertEqual("Gigabit Ethernet", physical_links[2].get_name())
        self.assertEqual("Ethernet Connector", physical_links[3].get_name())

    def test_RequirementAddOn_get_incoming_requirements(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for oa in se.get_all_contents_by_type(OperationalActivity):
            #: :type oa: OperationalActivity
            if oa.get_name() == 'Broadcast Movies':
                tested = oa
                break
        requirements = RequirementAddOn.get_incoming_requirements(tested)
        self.assertEqual(1, len(requirements))
        self.assertEqual("Display of VOD Movies List", requirements[0].get_name())

    def test_RequirementAddOn_get_system_engineering(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        system = RequirementAddOn.get_system_engineering(se)
        self.assertEqual(se, system)
        ls = se.get_logical_architecture().get_logical_system()
        system1 = RequirementAddOn.get_system_engineering(ls)
        self.assertEqual(se, system1)

    def test_RequirementAddOn_get_outgoing_requirements(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for fa in se.get_all_contents_by_type(FunctionalExchange):
            #: :type fa: FunctionalExchange
            if fa.get_name() == 'Displayed Movies List':
                tested = fa
                break
        requirements = RequirementAddOn.get_outgoing_requirements(tested)
        self.assertEqual(1, len(requirements))
        self.assertEqual("Display of VOD Movies List", requirements[0].get_name())

    def test_Requirement_get_incoming_linked_elems(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for requirement in se.get_all_contents_by_type(Requirement):
            #: :type requirement: Requirement
            if requirement.get_name() == 'Display of VOD Movies List':
                tested = requirement
                break
        elements = tested.get_incoming_linked_elems()
        self.assertEqual(1, len(elements))
        self.assertEqual("Displayed Movies List", elements[0].get_name())
        self.assertEqual(FunctionalExchange, type(elements[0]))

    def test_Requirement_get_outgoing_linked_elems(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for requirement in se.get_all_contents_by_type(Requirement):
            #: :type requirement: Requirement
            if requirement.get_name() == 'Display of VOD Movies List':
                tested = requirement
                break
        elements = tested.get_outgoing_linked_elems()
        self.assertEqual(1, len(elements))
        self.assertEqual("Broadcast Movies", elements[0].get_name())
        self.assertEqual(OperationalActivity, type(elements[0]))

    def test_PVMT_get_p_v_names(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for sf in se.get_all_contents_by_type(SystemFunction):
            #: :type sf: SystemFunction
            if sf.get_name() == 'Retrieve VOD Movie Data':
                tested = sf
                break
        names = PVMT.get_p_v_names(tested)
        self.assertEqual(1, len(names))
        self.assertEqual("Version", names[0])

    def test_PVMT_get_p_v_group_names(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for sf in se.get_all_contents_by_type(SystemFunction):
            #: :type sf: SystemFunction
            if sf.get_name() == 'Retrieve VOD Movie Data':
                tested = sf
                break
        names = PVMT.get_p_v_group_names(tested)
        self.assertEqual(1, len(names))
        self.assertEqual("Version_Domain.Version_Extension", names[0])

    def test_PVMT_is_p_v_defined(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for sf in se.get_all_contents_by_type(SystemFunction):
            #: :type sf: SystemFunction
            if sf.get_name() == 'Retrieve VOD Movie Data':
                tested = sf
                break
        self.assertEqual(False, PVMT.is_p_v_defined(tested, 'not existing'))
        self.assertEqual(True, PVMT.is_p_v_defined(tested, 'Version'))

    def test_PVMT_get_p_v_value(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        tested = None
        for sf in se.get_all_contents_by_type(SystemFunction):
            #: :type sf: SystemFunction
            if sf.get_name() == 'Retrieve VOD Movie Data':
                tested = sf
                break
        self.assertEqual("1", PVMT.get_p_v_value(tested, 'Version'))

    def test_CapellaModel_progress_status_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        self.assertEqual("DRAFT", model.get_progress_status())

    def test_EObject_copy_e_object(self):
        lc = LogicalComponent()
        lc.set_name("LC1")
        lc_copy = EObject.copy_e_object(lc)
        self.assertEqual("LC1", lc_copy.get_name())
        
    def test_EObject_copy_all_e_objects(self):
        fe = FunctionalExchange()
        fp = FunctionOutputPort()
        fe.set_source_port(fp)
        to_copy = []
        to_copy.append(fe)
        to_copy.append(fp)
        copied = EObject.copy_all_e_objects(to_copy)
        self.assertEqual(copied[1], copied[0].get_source_port())
        
    def test_CapellaException_get_class(self):
        e = CapellaException()
        self.assertEqual(CapellaException, EObject.get_class(e.get_java_object()))

    def test_CapellaElement_get_applied_property_value_by_name(self):
        lc = LogicalComponent()
        self.assertEqual(None, lc.get_applied_property_value_by_name("name"))
        pv = PropertyValue()
        pv.set_name("name")
        lc.get_applied_property_values().add(pv)
        self.assertEqual(pv, lc.get_applied_property_value_by_name("name"))

    def test_CapellaElement_get_owned_property_value_by_name(self):
        lc = LogicalComponent()
        self.assertEqual(None, lc.get_owned_property_value_by_name("name"))
        pv = PropertyValue()
        pv.set_name("name")
        lc.get_owned_property_values().add(pv)
        self.assertEqual(pv, lc.get_owned_property_value_by_name("name"))

    def test_CapellaElement_get_applied_property_value_group_by_name(self):
        lc = LogicalComponent()
        self.assertEqual(None, lc.get_applied_property_value_group_by_name("name"))
        pvg = PropertyValueGroup()
        pvg.set_name("name")
        lc.get_applied_property_value_groups().add(pvg)
        self.assertEqual(pvg, lc.get_applied_property_value_group_by_name("name"))

    def test_CapellaElement_get_owned_property_value_group_by_name(self):
        lc = LogicalComponent()
        self.assertEqual(None, lc.get_owned_property_value_group_by_name("name"))
        pvg = PropertyValueGroup()
        pvg.set_name("name")
        lc.get_owned_property_value_groups().add(pvg)
        self.assertEqual(pvg, lc.get_owned_property_value_group_by_name("name"))

    def test_OperationalActivity_incoming_getter(self):
        """
        This test need the IFE project to be in the workspace to run
        """
        model = CapellaModel()
        model.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        se = model.get_system_engineering()
        oa = se.get_all_contents_by_type(OperationalActivity)[3]
        self.assertEqual(Interaction, type(oa.get_incoming()[0]))
        for elem in oa.get_incoming():
            self.assertEqual(Interaction, type(elem))
