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

    def test_new_PhysicalComponent_invalid_java_object(self):
        pa = PhysicalActor()
        with self.assertRaises(AttributeError) as context:
            PhysicalComponent(pa.get_java_object())
        self.assertEqual("Passed component is an actor.", str(context.exception))
        pass

    def test_new_PhysicalActor(self):
        pa = PhysicalActor()
        self.assertEqual(True, pa.get_java_object().isActor())
        pass

    def test_PhysicalComponent_get_class(self):
        pc = PhysicalComponent()
        self.assertEqual(PhysicalComponent, EObject.get_class(pc.get_java_object()))
        pass

    def test_PhysicalActor_get_class(self):
        pa = PhysicalActor()
        self.assertEqual(PhysicalActor, EObject.get_class(pa.get_java_object()))
        pass


    def test_new_PhysicalActor_invalid_java_object(self):
        pc = PhysicalComponent()
        with self.assertRaises(AttributeError) as context:
            PhysicalActor(pc.get_java_object())
        self.assertEqual("Passed component is not an actor.", str(context.exception))
        pass
