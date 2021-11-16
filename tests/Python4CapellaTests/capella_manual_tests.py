include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

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
        lc_pkg = LogicalComponentPkg()
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
        pc_pkg = PhysicalComponentPkg()
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
            #: :type fc: Mission
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

    def test_OperationalProcess_involved_activities_getter(self):
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


