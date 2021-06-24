include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

import unittest

class capella_tests(unittest.TestCase):

    def test_CapellaModel_system_engineering(self):
        tested = CapellaModel()
        value = SystemEngineering()
        tested.set_system_engineering(value)
        self.assertEqual(tested.get_system_engineering(), value)
        pass

    def test_CapellaModel_referenced_libraries(self):
        tested = CapellaModel()
        value = CapellaLibrary()
        tested.get_referenced_libraries().add(value)
        self.assertEqual(tested.get_referenced_libraries().get(0), value)
        pass

    def test_CapellaModel_all_diagrams(self):
        tested = CapellaModel()
        value = Diagram()
        tested.get_all_diagrams().add(value)
        self.assertEqual(tested.get_all_diagrams().get(0), value)
        pass

    def test_CapellaModel_getDiagrams(self):
        self.fail("TODO")

    def test_CapellaLibrary_system_engineering(self):
        tested = CapellaLibrary()
        value = SystemEngineering()
        tested.set_system_engineering(value)
        self.assertEqual(tested.get_system_engineering(), value)
        pass

    def test_CapellaLibrary_referenced_libraries(self):
        tested = CapellaLibrary()
        value = CapellaLibrary()
        tested.get_referenced_libraries().add(value)
        self.assertEqual(tested.get_referenced_libraries().get(0), value)
        pass

    def test_CapellaLibrary_all_diagrams(self):
        tested = CapellaLibrary()
        value = Diagram()
        tested.get_all_diagrams().add(value)
        self.assertEqual(tested.get_all_diagrams().get(0), value)
        pass

    def test_CapellaLibrary_getDiagrams(self):
        self.fail("TODO")

    def test_SystemEngineering_owned_property_value_pkgs(self):
        tested = SystemEngineering()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_SystemEngineering_id(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemEngineering_sid(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemEngineering_name(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemEngineering_summary(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemEngineering_description(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemEngineering_status(self):
        tested = SystemEngineering()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemEngineering_review(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemEngineering_visible_in_documentation(self):
        tested = SystemEngineering()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemEngineering_visible_for_traceability(self):
        tested = SystemEngineering()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemEngineering_owned_constraints(self):
        tested = SystemEngineering()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemEngineering_constraints(self):
        tested = SystemEngineering()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemEngineering_owned_property_values(self):
        tested = SystemEngineering()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemEngineering_applied_property_values(self):
        tested = SystemEngineering()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemEngineering_owned_property_value_groups(self):
        tested = SystemEngineering()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemEngineering_applied_property_value_groups(self):
        tested = SystemEngineering()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemEngineering_owned_enumeration_property_types(self):
        tested = SystemEngineering()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemEngineering_owned_diagrams(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemEngineering_element_of_interest_for_diagrams(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemEngineering_contextual_element_for_diagrams(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemEngineering_representing_diagrams(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemEngineering_rec_catalogs(self):
        tested = SystemEngineering()
        value = RecCatalog()
        tested.get_rec_catalogs().add(value)
        self.assertEqual(tested.get_rec_catalogs().get(0), value)
        pass

    def test_SystemEngineering_operational_analysis(self):
        tested = SystemEngineering()
        value = OperationalAnalysis()
        tested.set_operational_analysis(value)
        self.assertEqual(tested.get_operational_analysis(), value)
        pass

    def test_SystemEngineering_system_analysis(self):
        tested = SystemEngineering()
        value = SystemAnalysis()
        tested.set_system_analysis(value)
        self.assertEqual(tested.get_system_analysis(), value)
        pass

    def test_SystemEngineering_logical_architecture(self):
        tested = SystemEngineering()
        value = LogicalArchitecture()
        tested.set_logical_architecture(value)
        self.assertEqual(tested.get_logical_architecture(), value)
        pass

    def test_SystemEngineering_physical_architecture(self):
        tested = SystemEngineering()
        value = PhysicalArchitecture()
        tested.set_physical_architecture(value)
        self.assertEqual(tested.get_physical_architecture(), value)
        pass

    def test_SystemEngineering_e_p_b_s_architecture(self):
        tested = SystemEngineering()
        value = EPBSArchitecture()
        tested.set_e_p_b_s_architecture(value)
        self.assertEqual(tested.get_e_p_b_s_architecture(), value)
        pass

    def test_Constraint_id(self):
        tested = Constraint()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Constraint_sid(self):
        tested = Constraint()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Constraint_name(self):
        tested = Constraint()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Constraint_summary(self):
        tested = Constraint()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Constraint_description(self):
        tested = Constraint()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Constraint_status(self):
        tested = Constraint()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Constraint_review(self):
        tested = Constraint()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Constraint_visible_in_documentation(self):
        tested = Constraint()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Constraint_visible_for_traceability(self):
        tested = Constraint()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Constraint_owned_constraints(self):
        tested = Constraint()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Constraint_constraints(self):
        tested = Constraint()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Constraint_owned_property_values(self):
        tested = Constraint()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Constraint_applied_property_values(self):
        tested = Constraint()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Constraint_owned_property_value_groups(self):
        tested = Constraint()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Constraint_applied_property_value_groups(self):
        tested = Constraint()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Constraint_owned_enumeration_property_types(self):
        tested = Constraint()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Constraint_owned_diagrams(self):
        tested = Constraint()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Constraint_element_of_interest_for_diagrams(self):
        tested = Constraint()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Constraint_contextual_element_for_diagrams(self):
        tested = Constraint()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Constraint_representing_diagrams(self):
        tested = Constraint()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Constraint_specification(self):
        tested = Constraint()
        value = "value"
        tested.set_specification(value)
        self.assertEqual(tested.get_specification(), value)
        pass

    def test_Constraint_constrained_elements(self):
        tested = Constraint()
        value = ComponentExchangeCategory()
        tested.get_constrained_elements()
        pass

    def test_PropertyValue_id(self):
        tested = PropertyValue()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PropertyValue_sid(self):
        tested = PropertyValue()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PropertyValue_name(self):
        tested = PropertyValue()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PropertyValue_summary(self):
        tested = PropertyValue()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PropertyValue_description(self):
        tested = PropertyValue()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PropertyValue_status(self):
        tested = PropertyValue()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PropertyValue_review(self):
        tested = PropertyValue()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PropertyValue_visible_in_documentation(self):
        tested = PropertyValue()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PropertyValue_visible_for_traceability(self):
        tested = PropertyValue()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PropertyValue_owned_constraints(self):
        tested = PropertyValue()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PropertyValue_constraints(self):
        tested = PropertyValue()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_PropertyValue_owned_property_values(self):
        tested = PropertyValue()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PropertyValue_applied_property_values(self):
        tested = PropertyValue()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PropertyValue_owned_property_value_groups(self):
        tested = PropertyValue()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PropertyValue_applied_property_value_groups(self):
        tested = PropertyValue()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PropertyValue_owned_enumeration_property_types(self):
        tested = PropertyValue()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PropertyValue_owned_diagrams(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PropertyValue_element_of_interest_for_diagrams(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PropertyValue_contextual_element_for_diagrams(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PropertyValue_representing_diagrams(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PropertyValue_kind(self):
        tested = PropertyValue()
        value = PropertyValueKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_PropertyValue_value(self):
        tested = PropertyValue()
        value = "value"
        tested.set_value(value)
        self.assertEqual(tested.get_value(), value)
        pass

    def test_PropertyValue_valued_elements(self):
        tested = PropertyValue()
        value = ComponentExchangeCategory()
        tested.get_valued_elements().add(value)
        self.assertEqual(tested.get_valued_elements().get(0), value)
        pass

    def test_PropertyValue_type(self):
        tested = PropertyValue()
        value = EnumerationPropertyType()
        tested.set_type(value)
        self.assertEqual(tested.get_type(), value)
        pass

    def test_PropertyValueGroup_id(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PropertyValueGroup_sid(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PropertyValueGroup_name(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PropertyValueGroup_summary(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PropertyValueGroup_description(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PropertyValueGroup_status(self):
        tested = PropertyValueGroup()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PropertyValueGroup_review(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PropertyValueGroup_visible_in_documentation(self):
        tested = PropertyValueGroup()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PropertyValueGroup_visible_for_traceability(self):
        tested = PropertyValueGroup()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PropertyValueGroup_owned_constraints(self):
        tested = PropertyValueGroup()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PropertyValueGroup_constraints(self):
        tested = PropertyValueGroup()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PropertyValueGroup_owned_property_values(self):
        tested = PropertyValueGroup()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PropertyValueGroup_applied_property_values(self):
        tested = PropertyValueGroup()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PropertyValueGroup_owned_property_value_groups(self):
        tested = PropertyValueGroup()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PropertyValueGroup_applied_property_value_groups(self):
        tested = PropertyValueGroup()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PropertyValueGroup_owned_enumeration_property_types(self):
        tested = PropertyValueGroup()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PropertyValueGroup_owned_diagrams(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PropertyValueGroup_element_of_interest_for_diagrams(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PropertyValueGroup_contextual_element_for_diagrams(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PropertyValueGroup_representing_diagrams(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PropertyValueGroup_valued_elements(self):
        tested = PropertyValueGroup()
        value = ComponentExchangeCategory()
        tested.get_valued_elements()
        pass

    def test_PropertyValuePkg_owned_property_value_pkgs(self):
        tested = PropertyValuePkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_PropertyValuePkg_id(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PropertyValuePkg_sid(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PropertyValuePkg_name(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PropertyValuePkg_summary(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PropertyValuePkg_description(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PropertyValuePkg_status(self):
        tested = PropertyValuePkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PropertyValuePkg_review(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PropertyValuePkg_visible_in_documentation(self):
        tested = PropertyValuePkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PropertyValuePkg_visible_for_traceability(self):
        tested = PropertyValuePkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PropertyValuePkg_owned_constraints(self):
        tested = PropertyValuePkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PropertyValuePkg_constraints(self):
        tested = PropertyValuePkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PropertyValuePkg_owned_property_values(self):
        tested = PropertyValuePkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PropertyValuePkg_applied_property_values(self):
        tested = PropertyValuePkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PropertyValuePkg_owned_property_value_groups(self):
        tested = PropertyValuePkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PropertyValuePkg_applied_property_value_groups(self):
        tested = PropertyValuePkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PropertyValuePkg_owned_enumeration_property_types(self):
        tested = PropertyValuePkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PropertyValuePkg_owned_diagrams(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PropertyValuePkg_element_of_interest_for_diagrams(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PropertyValuePkg_contextual_element_for_diagrams(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PropertyValuePkg_representing_diagrams(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyType_id(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_EnumerationPropertyType_sid(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_EnumerationPropertyType_name(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_EnumerationPropertyType_summary(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_EnumerationPropertyType_description(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_EnumerationPropertyType_status(self):
        tested = EnumerationPropertyType()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_EnumerationPropertyType_review(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_EnumerationPropertyType_visible_in_documentation(self):
        tested = EnumerationPropertyType()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_EnumerationPropertyType_visible_for_traceability(self):
        tested = EnumerationPropertyType()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_EnumerationPropertyType_owned_constraints(self):
        tested = EnumerationPropertyType()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_EnumerationPropertyType_constraints(self):
        tested = EnumerationPropertyType()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_EnumerationPropertyType_owned_property_values(self):
        tested = EnumerationPropertyType()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_EnumerationPropertyType_applied_property_values(self):
        tested = EnumerationPropertyType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_EnumerationPropertyType_owned_property_value_groups(self):
        tested = EnumerationPropertyType()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_EnumerationPropertyType_applied_property_value_groups(self):
        tested = EnumerationPropertyType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_EnumerationPropertyType_owned_enumeration_property_types(self):
        tested = EnumerationPropertyType()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_EnumerationPropertyType_owned_diagrams(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyType_element_of_interest_for_diagrams(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyType_contextual_element_for_diagrams(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyType_representing_diagrams(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyType_owned_literals(self):
        tested = EnumerationPropertyType()
        value = EnumerationPropertyLiteral()
        tested.get_owned_literals().add(value)
        self.assertEqual(tested.get_owned_literals().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_id(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_EnumerationPropertyLiteral_sid(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_EnumerationPropertyLiteral_name(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_EnumerationPropertyLiteral_summary(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_EnumerationPropertyLiteral_description(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_EnumerationPropertyLiteral_status(self):
        tested = EnumerationPropertyLiteral()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_EnumerationPropertyLiteral_review(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_EnumerationPropertyLiteral_visible_in_documentation(self):
        tested = EnumerationPropertyLiteral()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_EnumerationPropertyLiteral_visible_for_traceability(self):
        tested = EnumerationPropertyLiteral()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_EnumerationPropertyLiteral_owned_constraints(self):
        tested = EnumerationPropertyLiteral()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_constraints(self):
        tested = EnumerationPropertyLiteral()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_EnumerationPropertyLiteral_owned_property_values(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_applied_property_values(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_owned_property_value_groups(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_applied_property_value_groups(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_owned_enumeration_property_types(self):
        tested = EnumerationPropertyLiteral()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_owned_diagrams(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_element_of_interest_for_diagrams(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_contextual_element_for_diagrams(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_EnumerationPropertyLiteral_representing_diagrams(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Diagram_uid(self):
        tested = Diagram()
        value = "value"
        tested.set_uid(value)
        self.assertEqual(tested.get_uid(), value)
        pass

    def test_Diagram_name(self):
        tested = Diagram()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Diagram_type(self):
        tested = Diagram()
        value = "value"
        tested.set_type(value)
        self.assertEqual(tested.get_type(), value)
        pass

    def test_Diagram_package(self):
        tested = Diagram()
        value = "value"
        tested.set_package(value)
        self.assertEqual(tested.get_package(), value)
        pass

    def test_Diagram_description(self):
        tested = Diagram()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Diagram_status(self):
        tested = Diagram()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Diagram_review(self):
        tested = Diagram()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Diagram_visible_in_documentation(self):
        tested = Diagram()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Diagram_visible_for_traceability(self):
        tested = Diagram()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Diagram_synchronized(self):
        tested = Diagram()
        value = True
        tested.set_synchronized(value)
        self.assertEqual(tested.get_synchronized(), value)
        pass

    def test_Diagram_target(self):
        tested = Diagram()
        value = Attribute()
        tested.set_target(value)
        self.assertEqual(tested.get_target(), value)
        pass

    def test_Diagram_represented_elements(self):
        tested = Diagram()
        value = Attribute()
        tested.get_represented_elements().add(value)
        self.assertEqual(tested.get_represented_elements().get(0), value)
        pass

    def test_Diagram_contextual_elements(self):
        tested = Diagram()
        value = Attribute()
        tested.get_contextual_elements().add(value)
        self.assertEqual(tested.get_contextual_elements().get(0), value)
        pass

    def test_Diagram_elements_of_interest(self):
        tested = Diagram()
        value = Attribute()
        tested.get_elements_of_interest().add(value)
        self.assertEqual(tested.get_elements_of_interest().get(0), value)
        pass

    def test_Diagram_exportAsImage(self):
        self.fail("TODO")

    def test_REC_decription(self):
        tested = REC()
        value = "value"
        tested.set_decription(value)
        self.assertEqual(tested.get_decription(), value)
        pass

    def test_REC_author(self):
        tested = REC()
        value = "value"
        tested.set_author(value)
        self.assertEqual(tested.get_author(), value)
        pass

    def test_REC_environment(self):
        tested = REC()
        value = "value"
        tested.set_environment(value)
        self.assertEqual(tested.get_environment(), value)
        pass

    def test_REC_tags(self):
        tested = REC()
        value = "value"
        tested.set_tags(value)
        self.assertEqual(tested.get_tags(), value)
        pass

    def test_REC_referenced_elements(self):
        tested = REC()
        value = Attribute()
        tested.get_referenced_elements().add(value)
        self.assertEqual(tested.get_referenced_elements().get(0), value)
        pass

    def test_REC_id(self):
        tested = REC()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_REC_name(self):
        tested = REC()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_REC_owned_diagrams(self):
        tested = REC()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_REC_element_of_interest_for_diagrams(self):
        tested = REC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_REC_contextual_element_for_diagrams(self):
        tested = REC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_REC_representing_diagrams(self):
        tested = REC()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_REC_default_replica_compliancy(self):
        tested = REC()
        value = CompliancyDefinition()
        tested.set_default_replica_compliancy(value)
        self.assertEqual(tested.get_default_replica_compliancy(), value)
        pass

    def test_REC_replicated_elements(self):
        tested = REC()
        value = RPL()
        tested.get_replicated_elements().add(value)
        self.assertEqual(tested.get_replicated_elements().get(0), value)
        pass

    def test_RPL_decription(self):
        tested = RPL()
        value = "value"
        tested.set_decription(value)
        self.assertEqual(tested.get_decription(), value)
        pass

    def test_RPL_author(self):
        tested = RPL()
        value = "value"
        tested.set_author(value)
        self.assertEqual(tested.get_author(), value)
        pass

    def test_RPL_environment(self):
        tested = RPL()
        value = "value"
        tested.set_environment(value)
        self.assertEqual(tested.get_environment(), value)
        pass

    def test_RPL_tags(self):
        tested = RPL()
        value = "value"
        tested.set_tags(value)
        self.assertEqual(tested.get_tags(), value)
        pass

    def test_RPL_referenced_elements(self):
        tested = RPL()
        value = Attribute()
        tested.get_referenced_elements().add(value)
        self.assertEqual(tested.get_referenced_elements().get(0), value)
        pass

    def test_RPL_id(self):
        tested = RPL()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_RPL_name(self):
        tested = RPL()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_RPL_owned_diagrams(self):
        tested = RPL()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_RPL_element_of_interest_for_diagrams(self):
        tested = RPL()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_RPL_contextual_element_for_diagrams(self):
        tested = RPL()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_RPL_representing_diagrams(self):
        tested = RPL()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_RPL_suffix(self):
        tested = RPL()
        value = "value"
        tested.set_suffix(value)
        self.assertEqual(tested.get_suffix(), value)
        pass

    def test_RPL_read_only(self):
        tested = RPL()
        value = True
        tested.set_read_only(value)
        self.assertEqual(tested.get_read_only(), value)
        pass

    def test_RPL_origin(self):
        tested = RPL()
        value = REC()
        tested.set_origin(value)
        self.assertEqual(tested.get_origin(), value)
        pass

    def test_RPL_current_compliancy(self):
        tested = RPL()
        value = CompliancyDefinition()
        tested.set_current_compliancy(value)
        self.assertEqual(tested.get_current_compliancy(), value)
        pass

    def test_CatalogElementPkg_id(self):
        tested = CatalogElementPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CatalogElementPkg_name(self):
        tested = CatalogElementPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CatalogElementPkg_owned_diagrams(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CatalogElementPkg_element_of_interest_for_diagrams(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CatalogElementPkg_contextual_element_for_diagrams(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CatalogElementPkg_representing_diagrams(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CatalogElementPkg_owned_element_pkgs(self):
        tested = CatalogElementPkg()
        value = CatalogElementPkg()
        tested.get_owned_element_pkgs().add(value)
        self.assertEqual(tested.get_owned_element_pkgs().get(0), value)
        pass

    def test_CatalogElementPkg_owned_recs(self):
        tested = CatalogElementPkg()
        value = REC()
        tested.get_owned_recs().add(value)
        self.assertEqual(tested.get_owned_recs().get(0), value)
        pass

    def test_CatalogElementPkg_owned_rpls(self):
        tested = CatalogElementPkg()
        value = RPL()
        tested.get_owned_rpls().add(value)
        self.assertEqual(tested.get_owned_rpls().get(0), value)
        pass

    def test_RecCatalog_owned_element_pkgs(self):
        tested = RecCatalog()
        value = CatalogElementPkg()
        tested.get_owned_element_pkgs().add(value)
        self.assertEqual(tested.get_owned_element_pkgs().get(0), value)
        pass

    def test_RecCatalog_owned_recs(self):
        tested = RecCatalog()
        value = REC()
        tested.get_owned_recs().add(value)
        self.assertEqual(tested.get_owned_recs().get(0), value)
        pass

    def test_RecCatalog_owned_rpls(self):
        tested = RecCatalog()
        value = RPL()
        tested.get_owned_rpls().add(value)
        self.assertEqual(tested.get_owned_rpls().get(0), value)
        pass

    def test_RecCatalog_id(self):
        tested = RecCatalog()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_RecCatalog_name(self):
        tested = RecCatalog()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_RecCatalog_owned_diagrams(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_RecCatalog_element_of_interest_for_diagrams(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_RecCatalog_contextual_element_for_diagrams(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_RecCatalog_representing_diagrams(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_RecCatalog_owned_compliancy_definition_pkg(self):
        tested = RecCatalog()
        value = CompliancyDefinitionPkg()
        tested.set_owned_compliancy_definition_pkg(value)
        self.assertEqual(tested.get_owned_compliancy_definition_pkg(), value)
        pass

    def test_CompliancyDefinitionPkg_id(self):
        tested = CompliancyDefinitionPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CompliancyDefinitionPkg_name(self):
        tested = CompliancyDefinitionPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CompliancyDefinitionPkg_owned_diagrams(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CompliancyDefinitionPkg_element_of_interest_for_diagrams(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CompliancyDefinitionPkg_contextual_element_for_diagrams(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CompliancyDefinitionPkg_representing_diagrams(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CompliancyDefinitionPkg_owned_definitions(self):
        tested = CompliancyDefinitionPkg()
        value = CompliancyDefinition()
        tested.get_owned_definitions().add(value)
        self.assertEqual(tested.get_owned_definitions().get(0), value)
        pass

    def test_CompliancyDefinition_id(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CompliancyDefinition_name(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CompliancyDefinition_owned_diagrams(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CompliancyDefinition_element_of_interest_for_diagrams(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CompliancyDefinition_contextual_element_for_diagrams(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CompliancyDefinition_representing_diagrams(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CompliancyDefinition_description(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalAnalysis_owned_property_value_pkgs(self):
        tested = OperationalAnalysis()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_OperationalAnalysis_id(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalAnalysis_sid(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalAnalysis_name(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalAnalysis_summary(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalAnalysis_description(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalAnalysis_status(self):
        tested = OperationalAnalysis()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalAnalysis_review(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalAnalysis_visible_in_documentation(self):
        tested = OperationalAnalysis()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalAnalysis_visible_for_traceability(self):
        tested = OperationalAnalysis()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalAnalysis_owned_constraints(self):
        tested = OperationalAnalysis()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalAnalysis_constraints(self):
        tested = OperationalAnalysis()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalAnalysis_owned_property_values(self):
        tested = OperationalAnalysis()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalAnalysis_applied_property_values(self):
        tested = OperationalAnalysis()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalAnalysis_owned_property_value_groups(self):
        tested = OperationalAnalysis()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalAnalysis_applied_property_value_groups(self):
        tested = OperationalAnalysis()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalAnalysis_owned_enumeration_property_types(self):
        tested = OperationalAnalysis()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalAnalysis_owned_diagrams(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalAnalysis_element_of_interest_for_diagrams(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalAnalysis_contextual_element_for_diagrams(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalAnalysis_representing_diagrams(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalAnalysis_operational_activity_pkg(self):
        tested = OperationalAnalysis()
        value = OperationalActivityPkg()
        tested.set_operational_activity_pkg(value)
        self.assertEqual(tested.get_operational_activity_pkg(), value)
        pass

    def test_OperationalAnalysis_operational_capability_pkg(self):
        tested = OperationalAnalysis()
        value = OperationalCapabilityPkg()
        tested.set_operational_capability_pkg(value)
        self.assertEqual(tested.get_operational_capability_pkg(), value)
        pass

    def test_OperationalAnalysis_interface_pkg(self):
        tested = OperationalAnalysis()
        value = InterfacePkg()
        tested.set_interface_pkg(value)
        self.assertEqual(tested.get_interface_pkg(), value)
        pass

    def test_OperationalAnalysis_data_pkg(self):
        tested = OperationalAnalysis()
        value = DataPkg()
        tested.set_data_pkg(value)
        self.assertEqual(tested.get_data_pkg(), value)
        pass

    def test_OperationalAnalysis_entity_pkg(self):
        tested = OperationalAnalysis()
        value = EntityPkg()
        tested.set_entity_pkg(value)
        self.assertEqual(tested.get_entity_pkg(), value)
        pass

    def test_OperationalActivityPkg_owned_property_value_pkgs(self):
        tested = OperationalActivityPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_OperationalActivityPkg_id(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalActivityPkg_sid(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalActivityPkg_name(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalActivityPkg_summary(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalActivityPkg_description(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalActivityPkg_status(self):
        tested = OperationalActivityPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalActivityPkg_review(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalActivityPkg_visible_in_documentation(self):
        tested = OperationalActivityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalActivityPkg_visible_for_traceability(self):
        tested = OperationalActivityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalActivityPkg_owned_constraints(self):
        tested = OperationalActivityPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalActivityPkg_constraints(self):
        tested = OperationalActivityPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalActivityPkg_owned_property_values(self):
        tested = OperationalActivityPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalActivityPkg_applied_property_values(self):
        tested = OperationalActivityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalActivityPkg_owned_property_value_groups(self):
        tested = OperationalActivityPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalActivityPkg_applied_property_value_groups(self):
        tested = OperationalActivityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalActivityPkg_owned_enumeration_property_types(self):
        tested = OperationalActivityPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalActivityPkg_owned_diagrams(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalActivityPkg_element_of_interest_for_diagrams(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalActivityPkg_contextual_element_for_diagrams(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalActivityPkg_representing_diagrams(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalActivityPkg_owned_operational_activity_pkgs(self):
        tested = OperationalActivityPkg()
        value = OperationalActivityPkg()
        tested.get_owned_operational_activity_pkgs().add(value)
        self.assertEqual(tested.get_owned_operational_activity_pkgs().get(0), value)
        pass

    def test_OperationalActivityPkg_owned_operational_activities(self):
        tested = OperationalActivityPkg()
        value = OperationalActivity()
        tested.get_owned_operational_activities().add(value)
        self.assertEqual(tested.get_owned_operational_activities().get(0), value)
        pass

    def test_OperationalActivity_available_in_states(self):
        tested = OperationalActivity()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_OperationalActivity_id(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalActivity_sid(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalActivity_name(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalActivity_summary(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalActivity_description(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalActivity_status(self):
        tested = OperationalActivity()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalActivity_review(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalActivity_visible_in_documentation(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalActivity_visible_for_traceability(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalActivity_owned_constraints(self):
        tested = OperationalActivity()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalActivity_constraints(self):
        tested = OperationalActivity()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalActivity_owned_property_values(self):
        tested = OperationalActivity()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalActivity_applied_property_values(self):
        tested = OperationalActivity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalActivity_owned_property_value_groups(self):
        tested = OperationalActivity()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalActivity_applied_property_value_groups(self):
        tested = OperationalActivity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalActivity_owned_enumeration_property_types(self):
        tested = OperationalActivity()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalActivity_owned_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalActivity_element_of_interest_for_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalActivity_contextual_element_for_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalActivity_representing_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalActivity_id(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalActivity_sid(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalActivity_name(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalActivity_summary(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalActivity_description(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalActivity_status(self):
        tested = OperationalActivity()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalActivity_review(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalActivity_visible_in_documentation(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalActivity_visible_for_traceability(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalActivity_owned_constraints(self):
        tested = OperationalActivity()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalActivity_constraints(self):
        tested = OperationalActivity()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalActivity_owned_property_values(self):
        tested = OperationalActivity()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalActivity_applied_property_values(self):
        tested = OperationalActivity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalActivity_owned_property_value_groups(self):
        tested = OperationalActivity()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalActivity_applied_property_value_groups(self):
        tested = OperationalActivity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalActivity_owned_enumeration_property_types(self):
        tested = OperationalActivity()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalActivity_owned_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalActivity_element_of_interest_for_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalActivity_contextual_element_for_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalActivity_representing_diagrams(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalActivity_contained_operational_activities(self):
        tested = OperationalActivity()
        value = OperationalActivity()
        tested.get_contained_operational_activities()
        pass

    def test_OperationalActivity_owned_operational_activity_pkgs(self):
        tested = OperationalActivity()
        value = OperationalActivityPkg()
        tested.get_owned_operational_activity_pkgs().add(value)
        self.assertEqual(tested.get_owned_operational_activity_pkgs().get(0), value)
        pass

    def test_OperationalActivity_incoming(self):
        tested = OperationalActivity()
        value = Interaction()
        tested.get_incoming().add(value)
        self.assertEqual(tested.get_incoming().get(0), value)
        pass

    def test_OperationalActivity_outgoing(self):
        tested = OperationalActivity()
        value = Interaction()
        tested.get_outgoing().add(value)
        self.assertEqual(tested.get_outgoing().get(0), value)
        pass

    def test_OperationalActivity_allocating_entity(self):
        tested = OperationalActivity()
        value = OperationalActor()
        tested.set_allocating_entity(value)
        self.assertEqual(tested.get_allocating_entity(), value)
        pass

    def test_OperationalActivity_owned_operational_processes(self):
        tested = OperationalActivity()
        value = OperationalProcess()
        tested.get_owned_operational_processes()
        pass

    def test_OperationalActivity_involving_operational_processes(self):
        tested = OperationalActivity()
        value = OperationalProcess()
        tested.get_involving_operational_processes().add(value)
        self.assertEqual(tested.get_involving_operational_processes().get(0), value)
        pass

    def test_OperationalActivity_involving_operational_capabilities(self):
        tested = OperationalActivity()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        self.assertEqual(tested.get_involving_operational_capabilities().get(0), value)
        pass

    def test_OperationalActivity_realizing_system_functions(self):
        tested = OperationalActivity()
        value = SystemFunction()
        tested.get_realizing_system_functions()
        pass

    def test_Interaction_id(self):
        tested = Interaction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Interaction_sid(self):
        tested = Interaction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Interaction_name(self):
        tested = Interaction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Interaction_summary(self):
        tested = Interaction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Interaction_description(self):
        tested = Interaction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Interaction_status(self):
        tested = Interaction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Interaction_review(self):
        tested = Interaction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Interaction_visible_in_documentation(self):
        tested = Interaction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Interaction_visible_for_traceability(self):
        tested = Interaction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Interaction_owned_constraints(self):
        tested = Interaction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Interaction_constraints(self):
        tested = Interaction()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_Interaction_owned_property_values(self):
        tested = Interaction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Interaction_applied_property_values(self):
        tested = Interaction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Interaction_owned_property_value_groups(self):
        tested = Interaction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Interaction_applied_property_value_groups(self):
        tested = Interaction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Interaction_owned_enumeration_property_types(self):
        tested = Interaction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Interaction_owned_diagrams(self):
        tested = Interaction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Interaction_element_of_interest_for_diagrams(self):
        tested = Interaction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Interaction_contextual_element_for_diagrams(self):
        tested = Interaction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Interaction_representing_diagrams(self):
        tested = Interaction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Interaction_source(self):
        tested = Interaction()
        value = OperationalActivity()
        tested.set_source(value)
        self.assertEqual(tested.get_source(), value)
        pass

    def test_Interaction_target(self):
        tested = Interaction()
        value = OperationalActivity()
        tested.set_target(value)
        self.assertEqual(tested.get_target(), value)
        pass

    def test_Interaction_allocating_communication_mean(self):
        tested = Interaction()
        value = CommunicationMean()
        tested.set_allocating_communication_mean(value)
        self.assertEqual(tested.get_allocating_communication_mean(), value)
        pass

    def test_Interaction_involving_operational_processes(self):
        tested = Interaction()
        value = OperationalProcess()
        tested.get_involving_operational_processes().add(value)
        self.assertEqual(tested.get_involving_operational_processes().get(0), value)
        pass

    def test_Interaction_exchanged_items(self):
        tested = Interaction()
        value = ExchangeItem()
        tested.get_exchanged_items().add(value)
        self.assertEqual(tested.get_exchanged_items().get(0), value)
        pass

    def test_Interaction_realizing_functional_exchanges(self):
        tested = Interaction()
        value = FunctionalExchange()
        tested.get_realizing_functional_exchanges().add(value)
        self.assertEqual(tested.get_realizing_functional_exchanges().get(0), value)
        pass

    def test_OperationalProcess_id(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalProcess_sid(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalProcess_name(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalProcess_summary(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalProcess_description(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalProcess_status(self):
        tested = OperationalProcess()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalProcess_review(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalProcess_visible_in_documentation(self):
        tested = OperationalProcess()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalProcess_visible_for_traceability(self):
        tested = OperationalProcess()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalProcess_owned_constraints(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalProcess_constraints(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalProcess_owned_property_values(self):
        tested = OperationalProcess()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalProcess_applied_property_values(self):
        tested = OperationalProcess()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalProcess_owned_property_value_groups(self):
        tested = OperationalProcess()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalProcess_applied_property_value_groups(self):
        tested = OperationalProcess()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalProcess_owned_enumeration_property_types(self):
        tested = OperationalProcess()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalProcess_owned_diagrams(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalProcess_element_of_interest_for_diagrams(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalProcess_contextual_element_for_diagrams(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalProcess_representing_diagrams(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalProcess_involved_operational_activities(self):
        tested = OperationalProcess()
        value = OperationalActivity()
        tested.get_involved_operational_activities()
        pass

    def test_OperationalProcess_involved_interactions(self):
        tested = OperationalProcess()
        value = Interaction()
        tested.get_involved_interactions().add(value)
        self.assertEqual(tested.get_involved_interactions().get(0), value)
        pass

    def test_OperationalProcess_involved_operational_processes(self):
        tested = OperationalProcess()
        value = OperationalProcess()
        tested.get_involved_operational_processes()
        pass

    def test_OperationalProcess_pre_condition(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_OperationalProcess_post_condition(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_OperationalProcess_available_in_states(self):
        tested = OperationalProcess()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_OperationalProcess_involving_operational_capabilities(self):
        tested = OperationalProcess()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities()
        pass

    def test_OperationalProcess_realizing_functional_chains(self):
        tested = OperationalProcess()
        value = FunctionalChain()
        tested.get_realizing_functional_chains()
        pass

    def test_OperationalCapabilityPkg_owned_property_value_pkgs(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_OperationalCapabilityPkg_id(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalCapabilityPkg_sid(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalCapabilityPkg_name(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalCapabilityPkg_summary(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalCapabilityPkg_description(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalCapabilityPkg_status(self):
        tested = OperationalCapabilityPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalCapabilityPkg_review(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalCapabilityPkg_visible_in_documentation(self):
        tested = OperationalCapabilityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalCapabilityPkg_visible_for_traceability(self):
        tested = OperationalCapabilityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalCapabilityPkg_owned_constraints(self):
        tested = OperationalCapabilityPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalCapabilityPkg_constraints(self):
        tested = OperationalCapabilityPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalCapabilityPkg_owned_property_values(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalCapabilityPkg_applied_property_values(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalCapabilityPkg_owned_property_value_groups(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalCapabilityPkg_applied_property_value_groups(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalCapabilityPkg_owned_enumeration_property_types(self):
        tested = OperationalCapabilityPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalCapabilityPkg_owned_diagrams(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalCapabilityPkg_element_of_interest_for_diagrams(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalCapabilityPkg_contextual_element_for_diagrams(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalCapabilityPkg_representing_diagrams(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalCapabilityPkg_owned_operational_capability_pkgs(self):
        tested = OperationalCapabilityPkg()
        value = OperationalCapabilityPkg()
        tested.get_owned_operational_capability_pkgs().add(value)
        self.assertEqual(tested.get_owned_operational_capability_pkgs().get(0), value)
        pass

    def test_OperationalCapabilityPkg_owned_operational_capabilities(self):
        tested = OperationalCapabilityPkg()
        value = OperationalCapability()
        tested.get_owned_operational_capabilities().add(value)
        self.assertEqual(tested.get_owned_operational_capabilities().get(0), value)
        pass

    def test_OperationalCapability_pre_condition(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_OperationalCapability_post_condition(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_OperationalCapability_owned_scenarios(self):
        tested = OperationalCapability()
        value = Scenario()
        tested.get_owned_scenarios().add(value)
        self.assertEqual(tested.get_owned_scenarios().get(0), value)
        pass

    def test_OperationalCapability_super(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_super()
        pass

    def test_OperationalCapability_sub(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_sub()
        pass

    def test_OperationalCapability_included_capabilities(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        self.assertEqual(tested.get_included_capabilities().get(0), value)
        pass

    def test_OperationalCapability_including_capabilities(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        self.assertEqual(tested.get_including_capabilities().get(0), value)
        pass

    def test_OperationalCapability_extended_capabilities(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        self.assertEqual(tested.get_extended_capabilities().get(0), value)
        pass

    def test_OperationalCapability_extending_capabilities(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        self.assertEqual(tested.get_extending_capabilities().get(0), value)
        pass

    def test_OperationalCapability_available_in_states(self):
        tested = OperationalCapability()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_OperationalCapability_owned_property_value_pkgs(self):
        tested = OperationalCapability()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_OperationalCapability_id(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalCapability_sid(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalCapability_name(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalCapability_summary(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalCapability_description(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalCapability_status(self):
        tested = OperationalCapability()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalCapability_review(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalCapability_visible_in_documentation(self):
        tested = OperationalCapability()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalCapability_visible_for_traceability(self):
        tested = OperationalCapability()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalCapability_owned_constraints(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalCapability_constraints(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_OperationalCapability_owned_property_values(self):
        tested = OperationalCapability()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalCapability_applied_property_values(self):
        tested = OperationalCapability()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalCapability_owned_property_value_groups(self):
        tested = OperationalCapability()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalCapability_applied_property_value_groups(self):
        tested = OperationalCapability()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalCapability_owned_enumeration_property_types(self):
        tested = OperationalCapability()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalCapability_owned_diagrams(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalCapability_element_of_interest_for_diagrams(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalCapability_contextual_element_for_diagrams(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalCapability_representing_diagrams(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalCapability_owned_operational_processes(self):
        tested = OperationalCapability()
        value = OperationalProcess()
        tested.get_owned_operational_processes()
        pass

    def test_OperationalCapability_involved_operational_processes(self):
        tested = OperationalCapability()
        value = OperationalProcess()
        tested.get_involved_operational_processes()
        pass

    def test_OperationalCapability_involved_operational_activities(self):
        tested = OperationalCapability()
        value = OperationalActivity()
        tested.get_involved_operational_activities().add(value)
        self.assertEqual(tested.get_involved_operational_activities().get(0), value)
        pass

    def test_OperationalCapability_involved_entities(self):
        tested = OperationalCapability()
        value = OperationalActor()
        tested.get_involved_entities()
        pass

    def test_OperationalCapability_realizing_capabilities(self):
        tested = OperationalCapability()
        value = Capability()
        tested.get_realizing_capabilities()
        pass

    def test_EntityPkg_owned_property_value_pkgs(self):
        tested = EntityPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_EntityPkg_id(self):
        tested = EntityPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_EntityPkg_sid(self):
        tested = EntityPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_EntityPkg_name(self):
        tested = EntityPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_EntityPkg_summary(self):
        tested = EntityPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_EntityPkg_description(self):
        tested = EntityPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_EntityPkg_status(self):
        tested = EntityPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_EntityPkg_review(self):
        tested = EntityPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_EntityPkg_visible_in_documentation(self):
        tested = EntityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_EntityPkg_visible_for_traceability(self):
        tested = EntityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_EntityPkg_owned_constraints(self):
        tested = EntityPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_EntityPkg_constraints(self):
        tested = EntityPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_EntityPkg_owned_property_values(self):
        tested = EntityPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_EntityPkg_applied_property_values(self):
        tested = EntityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_EntityPkg_owned_property_value_groups(self):
        tested = EntityPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_EntityPkg_applied_property_value_groups(self):
        tested = EntityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_EntityPkg_owned_enumeration_property_types(self):
        tested = EntityPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_EntityPkg_owned_diagrams(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_EntityPkg_element_of_interest_for_diagrams(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_EntityPkg_contextual_element_for_diagrams(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_EntityPkg_representing_diagrams(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_EntityPkg_owned_entity_pkgs(self):
        tested = EntityPkg()
        value = EntityPkg()
        tested.get_owned_entity_pkgs().add(value)
        self.assertEqual(tested.get_owned_entity_pkgs().get(0), value)
        pass

    def test_EntityPkg_owned_entities(self):
        tested = EntityPkg()
        value = OperationalActor()
        tested.get_owned_entities().add(value)
        self.assertEqual(tested.get_owned_entities().get(0), value)
        pass

    def test_OperationalEntity_incoming_communication_means(self):
        tested = OperationalEntity()
        value = CommunicationMean()
        tested.get_incoming_communication_means().add(value)
        self.assertEqual(tested.get_incoming_communication_means().get(0), value)
        pass

    def test_OperationalEntity_outgoing_communication_means(self):
        tested = OperationalEntity()
        value = CommunicationMean()
        tested.get_outgoing_communication_means().add(value)
        self.assertEqual(tested.get_outgoing_communication_means().get(0), value)
        pass

    def test_OperationalEntity_allocated_operational_activities(self):
        tested = OperationalEntity()
        value = OperationalActivity()
        tested.get_allocated_operational_activities().add(value)
        self.assertEqual(tested.get_allocated_operational_activities().get(0), value)
        pass

    def test_OperationalEntity_involving_operational_capabilities(self):
        tested = OperationalEntity()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        self.assertEqual(tested.get_involving_operational_capabilities().get(0), value)
        pass

    def test_OperationalEntity_owned_state_machines(self):
        tested = OperationalEntity()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_OperationalEntity_realizing_system_actors(self):
        tested = OperationalEntity()
        value = SystemActor()
        tested.get_realizing_system_actors().add(value)
        self.assertEqual(tested.get_realizing_system_actors().get(0), value)
        pass

    def test_OperationalEntity_id(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalEntity_sid(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalEntity_name(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalEntity_summary(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalEntity_description(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalEntity_status(self):
        tested = OperationalEntity()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalEntity_review(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalEntity_visible_in_documentation(self):
        tested = OperationalEntity()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalEntity_visible_for_traceability(self):
        tested = OperationalEntity()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalEntity_owned_constraints(self):
        tested = OperationalEntity()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalEntity_constraints(self):
        tested = OperationalEntity()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_OperationalEntity_owned_property_values(self):
        tested = OperationalEntity()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalEntity_applied_property_values(self):
        tested = OperationalEntity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalEntity_owned_property_value_groups(self):
        tested = OperationalEntity()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalEntity_applied_property_value_groups(self):
        tested = OperationalEntity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalEntity_owned_enumeration_property_types(self):
        tested = OperationalEntity()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalEntity_owned_diagrams(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalEntity_element_of_interest_for_diagrams(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalEntity_contextual_element_for_diagrams(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalEntity_representing_diagrams(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalEntity_owned_entities(self):
        tested = OperationalEntity()
        value = OperationalEntity()
        tested.get_owned_entities().add(value)
        self.assertEqual(tested.get_owned_entities().get(0), value)
        pass

    def test_OperationalActor_id(self):
        tested = OperationalActor()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_OperationalActor_sid(self):
        tested = OperationalActor()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_OperationalActor_name(self):
        tested = OperationalActor()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_OperationalActor_summary(self):
        tested = OperationalActor()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_OperationalActor_description(self):
        tested = OperationalActor()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_OperationalActor_status(self):
        tested = OperationalActor()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_OperationalActor_review(self):
        tested = OperationalActor()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_OperationalActor_visible_in_documentation(self):
        tested = OperationalActor()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_OperationalActor_visible_for_traceability(self):
        tested = OperationalActor()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_OperationalActor_owned_constraints(self):
        tested = OperationalActor()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_OperationalActor_constraints(self):
        tested = OperationalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_OperationalActor_owned_property_values(self):
        tested = OperationalActor()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_OperationalActor_applied_property_values(self):
        tested = OperationalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_OperationalActor_owned_property_value_groups(self):
        tested = OperationalActor()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_OperationalActor_applied_property_value_groups(self):
        tested = OperationalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_OperationalActor_owned_enumeration_property_types(self):
        tested = OperationalActor()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_OperationalActor_owned_diagrams(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_OperationalActor_element_of_interest_for_diagrams(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_OperationalActor_contextual_element_for_diagrams(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_OperationalActor_representing_diagrams(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_OperationalActor_incoming_communication_means(self):
        tested = OperationalActor()
        value = CommunicationMean()
        tested.get_incoming_communication_means().add(value)
        self.assertEqual(tested.get_incoming_communication_means().get(0), value)
        pass

    def test_OperationalActor_outgoing_communication_means(self):
        tested = OperationalActor()
        value = CommunicationMean()
        tested.get_outgoing_communication_means().add(value)
        self.assertEqual(tested.get_outgoing_communication_means().get(0), value)
        pass

    def test_OperationalActor_allocated_operational_activities(self):
        tested = OperationalActor()
        value = OperationalActivity()
        tested.get_allocated_operational_activities().add(value)
        self.assertEqual(tested.get_allocated_operational_activities().get(0), value)
        pass

    def test_OperationalActor_involving_operational_capabilities(self):
        tested = OperationalActor()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        self.assertEqual(tested.get_involving_operational_capabilities().get(0), value)
        pass

    def test_OperationalActor_owned_state_machines(self):
        tested = OperationalActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_OperationalActor_realizing_system_actors(self):
        tested = OperationalActor()
        value = SystemActor()
        tested.get_realizing_system_actors().add(value)
        self.assertEqual(tested.get_realizing_system_actors().get(0), value)
        pass

    def test_CommunicationMean_id(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CommunicationMean_sid(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_CommunicationMean_name(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CommunicationMean_summary(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_CommunicationMean_description(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_CommunicationMean_status(self):
        tested = CommunicationMean()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_CommunicationMean_review(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_CommunicationMean_visible_in_documentation(self):
        tested = CommunicationMean()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_CommunicationMean_visible_for_traceability(self):
        tested = CommunicationMean()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_CommunicationMean_owned_constraints(self):
        tested = CommunicationMean()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_CommunicationMean_constraints(self):
        tested = CommunicationMean()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_CommunicationMean_owned_property_values(self):
        tested = CommunicationMean()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_CommunicationMean_applied_property_values(self):
        tested = CommunicationMean()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_CommunicationMean_owned_property_value_groups(self):
        tested = CommunicationMean()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_CommunicationMean_applied_property_value_groups(self):
        tested = CommunicationMean()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_CommunicationMean_owned_enumeration_property_types(self):
        tested = CommunicationMean()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_CommunicationMean_owned_diagrams(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CommunicationMean_element_of_interest_for_diagrams(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CommunicationMean_contextual_element_for_diagrams(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CommunicationMean_representing_diagrams(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CommunicationMean_source_entity(self):
        tested = CommunicationMean()
        value = OperationalActor()
        tested.set_source_entity(value)
        self.assertEqual(tested.get_source_entity(), value)
        pass

    def test_CommunicationMean_target_entity(self):
        tested = CommunicationMean()
        value = OperationalActor()
        tested.set_target_entity(value)
        self.assertEqual(tested.get_target_entity(), value)
        pass

    def test_CommunicationMean_allocated_interactions(self):
        tested = CommunicationMean()
        value = Interaction()
        tested.get_allocated_interactions()
        pass

    def test_CommunicationMean_convoyed_informations(self):
        tested = CommunicationMean()
        value = ExchangeItem()
        tested.get_convoyed_informations().add(value)
        self.assertEqual(tested.get_convoyed_informations().get(0), value)
        pass

    def test_CommunicationMean_realizing_component_exchanges(self):
        tested = CommunicationMean()
        value = ComponentExchange()
        tested.get_realizing_component_exchanges()
        pass

    def test_SystemAnalysis_owned_property_value_pkgs(self):
        tested = SystemAnalysis()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_SystemAnalysis_id(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemAnalysis_sid(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemAnalysis_name(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemAnalysis_summary(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemAnalysis_description(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemAnalysis_status(self):
        tested = SystemAnalysis()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemAnalysis_review(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemAnalysis_visible_in_documentation(self):
        tested = SystemAnalysis()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemAnalysis_visible_for_traceability(self):
        tested = SystemAnalysis()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemAnalysis_owned_constraints(self):
        tested = SystemAnalysis()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemAnalysis_constraints(self):
        tested = SystemAnalysis()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemAnalysis_owned_property_values(self):
        tested = SystemAnalysis()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemAnalysis_applied_property_values(self):
        tested = SystemAnalysis()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemAnalysis_owned_property_value_groups(self):
        tested = SystemAnalysis()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemAnalysis_applied_property_value_groups(self):
        tested = SystemAnalysis()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemAnalysis_owned_enumeration_property_types(self):
        tested = SystemAnalysis()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemAnalysis_owned_diagrams(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemAnalysis_element_of_interest_for_diagrams(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemAnalysis_contextual_element_for_diagrams(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemAnalysis_representing_diagrams(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemAnalysis_system_function_pkg(self):
        tested = SystemAnalysis()
        value = SystemFunctionPkg()
        tested.set_system_function_pkg(value)
        self.assertEqual(tested.get_system_function_pkg(), value)
        pass

    def test_SystemAnalysis_capability_pkg(self):
        tested = SystemAnalysis()
        value = CapabilityPkg()
        tested.set_capability_pkg(value)
        self.assertEqual(tested.get_capability_pkg(), value)
        pass

    def test_SystemAnalysis_interface_pkg(self):
        tested = SystemAnalysis()
        value = InterfacePkg()
        tested.set_interface_pkg(value)
        self.assertEqual(tested.get_interface_pkg(), value)
        pass

    def test_SystemAnalysis_data_pkg(self):
        tested = SystemAnalysis()
        value = DataPkg()
        tested.set_data_pkg(value)
        self.assertEqual(tested.get_data_pkg(), value)
        pass

    def test_SystemAnalysis_system_component_pkg(self):
        tested = SystemAnalysis()
        value = SystemComponentPkg()
        tested.set_system_component_pkg(value)
        self.assertEqual(tested.get_system_component_pkg(), value)
        pass

    def test_SystemAnalysis_mission_pkg(self):
        tested = SystemAnalysis()
        value = MissionPkg()
        tested.set_mission_pkg(value)
        self.assertEqual(tested.get_mission_pkg(), value)
        pass

    def test_SystemFunctionPkg_owned_property_value_pkgs(self):
        tested = SystemFunctionPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_SystemFunctionPkg_id(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemFunctionPkg_sid(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemFunctionPkg_name(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemFunctionPkg_summary(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemFunctionPkg_description(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemFunctionPkg_status(self):
        tested = SystemFunctionPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemFunctionPkg_review(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemFunctionPkg_visible_in_documentation(self):
        tested = SystemFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemFunctionPkg_visible_for_traceability(self):
        tested = SystemFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemFunctionPkg_owned_constraints(self):
        tested = SystemFunctionPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemFunctionPkg_constraints(self):
        tested = SystemFunctionPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemFunctionPkg_owned_property_values(self):
        tested = SystemFunctionPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemFunctionPkg_applied_property_values(self):
        tested = SystemFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemFunctionPkg_owned_property_value_groups(self):
        tested = SystemFunctionPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemFunctionPkg_applied_property_value_groups(self):
        tested = SystemFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemFunctionPkg_owned_enumeration_property_types(self):
        tested = SystemFunctionPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemFunctionPkg_owned_diagrams(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemFunctionPkg_element_of_interest_for_diagrams(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemFunctionPkg_contextual_element_for_diagrams(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemFunctionPkg_representing_diagrams(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemFunctionPkg_owned_system_function_pkgs(self):
        tested = SystemFunctionPkg()
        value = SystemFunctionPkg()
        tested.get_owned_system_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_system_function_pkgs().get(0), value)
        pass

    def test_SystemFunctionPkg_owned_system_functions(self):
        tested = SystemFunctionPkg()
        value = SystemFunction()
        tested.get_owned_system_functions().add(value)
        self.assertEqual(tested.get_owned_system_functions().get(0), value)
        pass

    def test_SystemFunction_kind(self):
        tested = SystemFunction()
        value = FunctionKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_SystemFunction_condition(self):
        tested = SystemFunction()
        value = "value"
        tested.set_condition(value)
        self.assertEqual(tested.get_condition(), value)
        pass

    def test_SystemFunction_inputs(self):
        tested = SystemFunction()
        value = FunctionInputPort()
        tested.get_inputs().add(value)
        self.assertEqual(tested.get_inputs().get(0), value)
        pass

    def test_SystemFunction_outputs(self):
        tested = SystemFunction()
        value = FunctionOutputPort()
        tested.get_outputs().add(value)
        self.assertEqual(tested.get_outputs().get(0), value)
        pass

    def test_SystemFunction_incoming(self):
        tested = SystemFunction()
        value = FunctionalExchange()
        tested.get_incoming()
        pass

    def test_SystemFunction_outgoing(self):
        tested = SystemFunction()
        value = FunctionalExchange()
        tested.get_outgoing()
        pass

    def test_SystemFunction_allocating_component(self):
        tested = SystemFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        self.assertEqual(tested.get_allocating_component(), value)
        pass

    def test_SystemFunction_owned_functional_chains(self):
        tested = SystemFunction()
        value = FunctionalChain()
        tested.get_owned_functional_chains()
        pass

    def test_SystemFunction_involving_functional_chains(self):
        tested = SystemFunction()
        value = FunctionalChain()
        tested.get_involving_functional_chains()
        pass

    def test_SystemFunction_involving_capabilities(self):
        tested = SystemFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities()
        pass

    def test_SystemFunction_available_in_states(self):
        tested = SystemFunction()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_SystemFunction_id(self):
        tested = SystemFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemFunction_sid(self):
        tested = SystemFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemFunction_name(self):
        tested = SystemFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemFunction_summary(self):
        tested = SystemFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemFunction_description(self):
        tested = SystemFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemFunction_status(self):
        tested = SystemFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemFunction_review(self):
        tested = SystemFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemFunction_visible_in_documentation(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemFunction_visible_for_traceability(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemFunction_owned_constraints(self):
        tested = SystemFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemFunction_constraints(self):
        tested = SystemFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemFunction_owned_property_values(self):
        tested = SystemFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemFunction_applied_property_values(self):
        tested = SystemFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemFunction_owned_property_value_groups(self):
        tested = SystemFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemFunction_applied_property_value_groups(self):
        tested = SystemFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemFunction_owned_enumeration_property_types(self):
        tested = SystemFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemFunction_owned_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemFunction_element_of_interest_for_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemFunction_contextual_element_for_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemFunction_representing_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemFunction_id(self):
        tested = SystemFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemFunction_sid(self):
        tested = SystemFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemFunction_name(self):
        tested = SystemFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemFunction_summary(self):
        tested = SystemFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemFunction_description(self):
        tested = SystemFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemFunction_status(self):
        tested = SystemFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemFunction_review(self):
        tested = SystemFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemFunction_visible_in_documentation(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemFunction_visible_for_traceability(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemFunction_owned_constraints(self):
        tested = SystemFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemFunction_constraints(self):
        tested = SystemFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemFunction_owned_property_values(self):
        tested = SystemFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemFunction_applied_property_values(self):
        tested = SystemFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemFunction_owned_property_value_groups(self):
        tested = SystemFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemFunction_applied_property_value_groups(self):
        tested = SystemFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemFunction_owned_enumeration_property_types(self):
        tested = SystemFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemFunction_owned_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemFunction_element_of_interest_for_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemFunction_contextual_element_for_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemFunction_representing_diagrams(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemFunction_contained_system_functions(self):
        tested = SystemFunction()
        value = SystemFunction()
        tested.get_contained_system_functions()
        pass

    def test_SystemFunction_owned_system_function_pkgs(self):
        tested = SystemFunction()
        value = SystemFunctionPkg()
        tested.get_owned_system_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_system_function_pkgs().get(0), value)
        pass

    def test_SystemFunction_realized_operational_activities(self):
        tested = SystemFunction()
        value = OperationalActivity()
        tested.get_realized_operational_activities()
        pass

    def test_SystemFunction_realizing_logical_functions(self):
        tested = SystemFunction()
        value = LogicalFunction()
        tested.get_realizing_logical_functions()
        pass

    def test_CapabilityPkg_owned_property_value_pkgs(self):
        tested = CapabilityPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_CapabilityPkg_id(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CapabilityPkg_sid(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_CapabilityPkg_name(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CapabilityPkg_summary(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_CapabilityPkg_description(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_CapabilityPkg_status(self):
        tested = CapabilityPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_CapabilityPkg_review(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_CapabilityPkg_visible_in_documentation(self):
        tested = CapabilityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_CapabilityPkg_visible_for_traceability(self):
        tested = CapabilityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_CapabilityPkg_owned_constraints(self):
        tested = CapabilityPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_CapabilityPkg_constraints(self):
        tested = CapabilityPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_CapabilityPkg_owned_property_values(self):
        tested = CapabilityPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_CapabilityPkg_applied_property_values(self):
        tested = CapabilityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_CapabilityPkg_owned_property_value_groups(self):
        tested = CapabilityPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_CapabilityPkg_applied_property_value_groups(self):
        tested = CapabilityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_CapabilityPkg_owned_enumeration_property_types(self):
        tested = CapabilityPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_CapabilityPkg_owned_diagrams(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CapabilityPkg_element_of_interest_for_diagrams(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CapabilityPkg_contextual_element_for_diagrams(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CapabilityPkg_representing_diagrams(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CapabilityPkg_owned_capability_pkgs(self):
        tested = CapabilityPkg()
        value = CapabilityPkg()
        tested.get_owned_capability_pkgs().add(value)
        self.assertEqual(tested.get_owned_capability_pkgs().get(0), value)
        pass

    def test_CapabilityPkg_owned_capabilities(self):
        tested = CapabilityPkg()
        value = Capability()
        tested.get_owned_capabilities().add(value)
        self.assertEqual(tested.get_owned_capabilities().get(0), value)
        pass

    def test_Capability_owned_functional_chains(self):
        tested = Capability()
        value = FunctionalChain()
        tested.get_owned_functional_chains()
        pass

    def test_Capability_involved_functional_chains(self):
        tested = Capability()
        value = FunctionalChain()
        tested.get_involved_functional_chains()
        pass

    def test_Capability_involved_functions(self):
        tested = Capability()
        value = PhysicalFunction()
        tested.get_involved_functions().add(value)
        self.assertEqual(tested.get_involved_functions().get(0), value)
        pass

    def test_Capability_pre_condition(self):
        tested = Capability()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_Capability_post_condition(self):
        tested = Capability()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_Capability_owned_scenarios(self):
        tested = Capability()
        value = Scenario()
        tested.get_owned_scenarios().add(value)
        self.assertEqual(tested.get_owned_scenarios().get(0), value)
        pass

    def test_Capability_super(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_super()
        pass

    def test_Capability_sub(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_sub()
        pass

    def test_Capability_included_capabilities(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        self.assertEqual(tested.get_included_capabilities().get(0), value)
        pass

    def test_Capability_including_capabilities(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        self.assertEqual(tested.get_including_capabilities().get(0), value)
        pass

    def test_Capability_extended_capabilities(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        self.assertEqual(tested.get_extended_capabilities().get(0), value)
        pass

    def test_Capability_extending_capabilities(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        self.assertEqual(tested.get_extending_capabilities().get(0), value)
        pass

    def test_Capability_available_in_states(self):
        tested = Capability()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_Capability_owned_property_value_pkgs(self):
        tested = Capability()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_Capability_id(self):
        tested = Capability()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Capability_sid(self):
        tested = Capability()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Capability_name(self):
        tested = Capability()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Capability_summary(self):
        tested = Capability()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Capability_description(self):
        tested = Capability()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Capability_status(self):
        tested = Capability()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Capability_review(self):
        tested = Capability()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Capability_visible_in_documentation(self):
        tested = Capability()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Capability_visible_for_traceability(self):
        tested = Capability()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Capability_owned_constraints(self):
        tested = Capability()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Capability_constraints(self):
        tested = Capability()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Capability_owned_property_values(self):
        tested = Capability()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Capability_applied_property_values(self):
        tested = Capability()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Capability_owned_property_value_groups(self):
        tested = Capability()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Capability_applied_property_value_groups(self):
        tested = Capability()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Capability_owned_enumeration_property_types(self):
        tested = Capability()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Capability_owned_diagrams(self):
        tested = Capability()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Capability_element_of_interest_for_diagrams(self):
        tested = Capability()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Capability_contextual_element_for_diagrams(self):
        tested = Capability()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Capability_representing_diagrams(self):
        tested = Capability()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Capability_purpose_missions(self):
        tested = Capability()
        value = Mission()
        tested.get_purpose_missions()
        pass

    def test_Capability_realized_operational_capabilities(self):
        tested = Capability()
        value = OperationalCapability()
        tested.get_realized_operational_capabilities()
        pass

    def test_Capability_realizing_capability_realizations(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_realizing_capability_realizations()
        pass

    def test_Capability_involved_system_actors(self):
        tested = Capability()
        value = SystemActor()
        tested.get_involved_system_actors().add(value)
        self.assertEqual(tested.get_involved_system_actors().get(0), value)
        pass

    def test_SystemComponentPkg_owned_property_value_pkgs(self):
        tested = SystemComponentPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_SystemComponentPkg_id(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemComponentPkg_sid(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemComponentPkg_name(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemComponentPkg_summary(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemComponentPkg_description(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemComponentPkg_status(self):
        tested = SystemComponentPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemComponentPkg_review(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemComponentPkg_visible_in_documentation(self):
        tested = SystemComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemComponentPkg_visible_for_traceability(self):
        tested = SystemComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemComponentPkg_owned_constraints(self):
        tested = SystemComponentPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemComponentPkg_constraints(self):
        tested = SystemComponentPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SystemComponentPkg_owned_property_values(self):
        tested = SystemComponentPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemComponentPkg_applied_property_values(self):
        tested = SystemComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemComponentPkg_owned_property_value_groups(self):
        tested = SystemComponentPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemComponentPkg_applied_property_value_groups(self):
        tested = SystemComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemComponentPkg_owned_enumeration_property_types(self):
        tested = SystemComponentPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemComponentPkg_owned_diagrams(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemComponentPkg_element_of_interest_for_diagrams(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemComponentPkg_contextual_element_for_diagrams(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemComponentPkg_representing_diagrams(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemComponentPkg_owned_system_component_pkgs(self):
        tested = SystemComponentPkg()
        value = SystemComponentPkg()
        tested.get_owned_system_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_system_component_pkgs().get(0), value)
        pass

    def test_SystemComponentPkg_owned_system(self):
        tested = SystemComponentPkg()
        value = System()
        tested.set_owned_system(value)
        self.assertEqual(tested.get_owned_system(), value)
        pass

    def test_SystemComponentPkg_owned_actors(self):
        tested = SystemComponentPkg()
        value = SystemActor()
        tested.get_owned_actors().add(value)
        self.assertEqual(tested.get_owned_actors().get(0), value)
        pass

    def test_System_contained_component_ports(self):
        tested = System()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_System_incoming_component_exchanges(self):
        tested = System()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_System_outgoing_component_exchanges(self):
        tested = System()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_System_inout_component_exchanges(self):
        tested = System()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_System_allocated_functions(self):
        tested = System()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_System_used_interfaces(self):
        tested = System()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_System_implemented_interfaces(self):
        tested = System()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_System_owned_state_machines(self):
        tested = System()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_System_id(self):
        tested = System()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_System_sid(self):
        tested = System()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_System_name(self):
        tested = System()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_System_summary(self):
        tested = System()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_System_description(self):
        tested = System()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_System_status(self):
        tested = System()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_System_review(self):
        tested = System()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_System_visible_in_documentation(self):
        tested = System()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_System_visible_for_traceability(self):
        tested = System()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_System_owned_constraints(self):
        tested = System()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_System_constraints(self):
        tested = System()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_System_owned_property_values(self):
        tested = System()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_System_applied_property_values(self):
        tested = System()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_System_owned_property_value_groups(self):
        tested = System()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_System_applied_property_value_groups(self):
        tested = System()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_System_owned_enumeration_property_types(self):
        tested = System()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_System_owned_diagrams(self):
        tested = System()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_System_element_of_interest_for_diagrams(self):
        tested = System()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_System_contextual_element_for_diagrams(self):
        tested = System()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_System_representing_diagrams(self):
        tested = System()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_System_contained_physical_ports(self):
        tested = System()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_System_physical_links(self):
        tested = System()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_System_involving_physical_paths(self):
        tested = System()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_System_owned_state_machines(self):
        tested = System()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_SystemActor_contained_component_ports(self):
        tested = SystemActor()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_SystemActor_incoming_component_exchanges(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_SystemActor_outgoing_component_exchanges(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_SystemActor_inout_component_exchanges(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_SystemActor_allocated_functions(self):
        tested = SystemActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_SystemActor_used_interfaces(self):
        tested = SystemActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_SystemActor_implemented_interfaces(self):
        tested = SystemActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_SystemActor_owned_state_machines(self):
        tested = SystemActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_SystemActor_id(self):
        tested = SystemActor()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SystemActor_sid(self):
        tested = SystemActor()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SystemActor_name(self):
        tested = SystemActor()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SystemActor_summary(self):
        tested = SystemActor()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SystemActor_description(self):
        tested = SystemActor()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SystemActor_status(self):
        tested = SystemActor()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SystemActor_review(self):
        tested = SystemActor()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SystemActor_visible_in_documentation(self):
        tested = SystemActor()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SystemActor_visible_for_traceability(self):
        tested = SystemActor()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SystemActor_owned_constraints(self):
        tested = SystemActor()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SystemActor_constraints(self):
        tested = SystemActor()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_SystemActor_owned_property_values(self):
        tested = SystemActor()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SystemActor_applied_property_values(self):
        tested = SystemActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SystemActor_owned_property_value_groups(self):
        tested = SystemActor()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SystemActor_applied_property_value_groups(self):
        tested = SystemActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SystemActor_owned_enumeration_property_types(self):
        tested = SystemActor()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SystemActor_owned_diagrams(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SystemActor_element_of_interest_for_diagrams(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SystemActor_contextual_element_for_diagrams(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SystemActor_representing_diagrams(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SystemActor_contained_physical_ports(self):
        tested = SystemActor()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_SystemActor_physical_links(self):
        tested = SystemActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_SystemActor_involving_physical_paths(self):
        tested = SystemActor()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_SystemActor_owned_state_machines(self):
        tested = SystemActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_SystemActor_is_human(self):
        tested = SystemActor()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_SystemActor_owned_actors(self):
        tested = SystemActor()
        value = SystemActor()
        tested.get_owned_actors().add(value)
        self.assertEqual(tested.get_owned_actors().get(0), value)
        pass

    def test_SystemActor_owned_system_component_pkgs(self):
        tested = SystemActor()
        value = SystemComponentPkg()
        tested.set_owned_system_component_pkgs(value)
        self.assertEqual(tested.get_owned_system_component_pkgs(), value)
        pass

    def test_SystemActor_involving_missions(self):
        tested = SystemActor()
        value = Mission()
        tested.get_involving_missions().add(value)
        self.assertEqual(tested.get_involving_missions().get(0), value)
        pass

    def test_SystemActor_realized_operational_entities(self):
        tested = SystemActor()
        value = OperationalActor()
        tested.get_realized_operational_entities().add(value)
        self.assertEqual(tested.get_realized_operational_entities().get(0), value)
        pass

    def test_SystemActor_involving_capabilities(self):
        tested = SystemActor()
        value = Capability()
        tested.get_involving_capabilities().add(value)
        self.assertEqual(tested.get_involving_capabilities().get(0), value)
        pass

    def test_SystemActor_realizing_logical_actors(self):
        tested = SystemActor()
        value = LogicalActor()
        tested.get_realizing_logical_actors().add(value)
        self.assertEqual(tested.get_realizing_logical_actors().get(0), value)
        pass

    def test_MissionPkg_owned_property_value_pkgs(self):
        tested = MissionPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_MissionPkg_id(self):
        tested = MissionPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_MissionPkg_sid(self):
        tested = MissionPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_MissionPkg_name(self):
        tested = MissionPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_MissionPkg_summary(self):
        tested = MissionPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_MissionPkg_description(self):
        tested = MissionPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_MissionPkg_status(self):
        tested = MissionPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_MissionPkg_review(self):
        tested = MissionPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_MissionPkg_visible_in_documentation(self):
        tested = MissionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_MissionPkg_visible_for_traceability(self):
        tested = MissionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_MissionPkg_owned_constraints(self):
        tested = MissionPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_MissionPkg_constraints(self):
        tested = MissionPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_MissionPkg_owned_property_values(self):
        tested = MissionPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_MissionPkg_applied_property_values(self):
        tested = MissionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_MissionPkg_owned_property_value_groups(self):
        tested = MissionPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_MissionPkg_applied_property_value_groups(self):
        tested = MissionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_MissionPkg_owned_enumeration_property_types(self):
        tested = MissionPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_MissionPkg_owned_diagrams(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_MissionPkg_element_of_interest_for_diagrams(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_MissionPkg_contextual_element_for_diagrams(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_MissionPkg_representing_diagrams(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_MissionPkg_owned_mission_pkgs(self):
        tested = MissionPkg()
        value = MissionPkg()
        tested.get_owned_mission_pkgs().add(value)
        self.assertEqual(tested.get_owned_mission_pkgs().get(0), value)
        pass

    def test_MissionPkg_owned_missions(self):
        tested = MissionPkg()
        value = Mission()
        tested.get_owned_missions().add(value)
        self.assertEqual(tested.get_owned_missions().get(0), value)
        pass

    def test_Mission_id(self):
        tested = Mission()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Mission_sid(self):
        tested = Mission()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Mission_name(self):
        tested = Mission()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Mission_summary(self):
        tested = Mission()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Mission_description(self):
        tested = Mission()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Mission_status(self):
        tested = Mission()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Mission_review(self):
        tested = Mission()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Mission_visible_in_documentation(self):
        tested = Mission()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Mission_visible_for_traceability(self):
        tested = Mission()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Mission_owned_constraints(self):
        tested = Mission()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Mission_constraints(self):
        tested = Mission()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Mission_owned_property_values(self):
        tested = Mission()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Mission_applied_property_values(self):
        tested = Mission()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Mission_owned_property_value_groups(self):
        tested = Mission()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Mission_applied_property_value_groups(self):
        tested = Mission()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Mission_owned_enumeration_property_types(self):
        tested = Mission()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Mission_owned_diagrams(self):
        tested = Mission()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Mission_element_of_interest_for_diagrams(self):
        tested = Mission()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Mission_contextual_element_for_diagrams(self):
        tested = Mission()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Mission_representing_diagrams(self):
        tested = Mission()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Mission_exploited_capabilities(self):
        tested = Mission()
        value = Capability()
        tested.get_exploited_capabilities()
        pass

    def test_Mission_involved_actors(self):
        tested = Mission()
        value = SystemActor()
        tested.get_involved_actors().add(value)
        self.assertEqual(tested.get_involved_actors().get(0), value)
        pass

    def test_LogicalArchitecture_owned_property_value_pkgs(self):
        tested = LogicalArchitecture()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_LogicalArchitecture_id(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalArchitecture_sid(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalArchitecture_name(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalArchitecture_summary(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalArchitecture_description(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalArchitecture_status(self):
        tested = LogicalArchitecture()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalArchitecture_review(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalArchitecture_visible_in_documentation(self):
        tested = LogicalArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalArchitecture_visible_for_traceability(self):
        tested = LogicalArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalArchitecture_owned_constraints(self):
        tested = LogicalArchitecture()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalArchitecture_constraints(self):
        tested = LogicalArchitecture()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalArchitecture_owned_property_values(self):
        tested = LogicalArchitecture()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalArchitecture_applied_property_values(self):
        tested = LogicalArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalArchitecture_owned_property_value_groups(self):
        tested = LogicalArchitecture()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalArchitecture_applied_property_value_groups(self):
        tested = LogicalArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalArchitecture_owned_enumeration_property_types(self):
        tested = LogicalArchitecture()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalArchitecture_owned_diagrams(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalArchitecture_element_of_interest_for_diagrams(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalArchitecture_contextual_element_for_diagrams(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalArchitecture_representing_diagrams(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalArchitecture_logical_function_pkg(self):
        tested = LogicalArchitecture()
        value = LogicalFunctionPkg()
        tested.set_logical_function_pkg(value)
        self.assertEqual(tested.get_logical_function_pkg(), value)
        pass

    def test_LogicalArchitecture_capability_realization_pkg(self):
        tested = LogicalArchitecture()
        value = CapabilityRealizationPkg()
        tested.set_capability_realization_pkg(value)
        self.assertEqual(tested.get_capability_realization_pkg(), value)
        pass

    def test_LogicalArchitecture_interface_pkg(self):
        tested = LogicalArchitecture()
        value = InterfacePkg()
        tested.set_interface_pkg(value)
        self.assertEqual(tested.get_interface_pkg(), value)
        pass

    def test_LogicalArchitecture_data_pkg(self):
        tested = LogicalArchitecture()
        value = DataPkg()
        tested.set_data_pkg(value)
        self.assertEqual(tested.get_data_pkg(), value)
        pass

    def test_LogicalArchitecture_logical_component_pkg(self):
        tested = LogicalArchitecture()
        value = LogicalComponentPkg()
        tested.set_logical_component_pkg(value)
        self.assertEqual(tested.get_logical_component_pkg(), value)
        pass

    def test_LogicalFunctionPkg_owned_property_value_pkgs(self):
        tested = LogicalFunctionPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_LogicalFunctionPkg_id(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalFunctionPkg_sid(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalFunctionPkg_name(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalFunctionPkg_summary(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalFunctionPkg_description(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalFunctionPkg_status(self):
        tested = LogicalFunctionPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalFunctionPkg_review(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalFunctionPkg_visible_in_documentation(self):
        tested = LogicalFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalFunctionPkg_visible_for_traceability(self):
        tested = LogicalFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalFunctionPkg_owned_constraints(self):
        tested = LogicalFunctionPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalFunctionPkg_constraints(self):
        tested = LogicalFunctionPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalFunctionPkg_owned_property_values(self):
        tested = LogicalFunctionPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalFunctionPkg_applied_property_values(self):
        tested = LogicalFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalFunctionPkg_owned_property_value_groups(self):
        tested = LogicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalFunctionPkg_applied_property_value_groups(self):
        tested = LogicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalFunctionPkg_owned_enumeration_property_types(self):
        tested = LogicalFunctionPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalFunctionPkg_owned_diagrams(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalFunctionPkg_element_of_interest_for_diagrams(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalFunctionPkg_contextual_element_for_diagrams(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalFunctionPkg_representing_diagrams(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalFunctionPkg_owned_logical_function_pkgs(self):
        tested = LogicalFunctionPkg()
        value = LogicalFunctionPkg()
        tested.get_owned_logical_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_logical_function_pkgs().get(0), value)
        pass

    def test_LogicalFunctionPkg_owned_logical_functions(self):
        tested = LogicalFunctionPkg()
        value = LogicalFunction()
        tested.get_owned_logical_functions().add(value)
        self.assertEqual(tested.get_owned_logical_functions().get(0), value)
        pass

    def test_LogicalFunction_kind(self):
        tested = LogicalFunction()
        value = FunctionKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_LogicalFunction_condition(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_condition(value)
        self.assertEqual(tested.get_condition(), value)
        pass

    def test_LogicalFunction_inputs(self):
        tested = LogicalFunction()
        value = FunctionInputPort()
        tested.get_inputs().add(value)
        self.assertEqual(tested.get_inputs().get(0), value)
        pass

    def test_LogicalFunction_outputs(self):
        tested = LogicalFunction()
        value = FunctionOutputPort()
        tested.get_outputs().add(value)
        self.assertEqual(tested.get_outputs().get(0), value)
        pass

    def test_LogicalFunction_incoming(self):
        tested = LogicalFunction()
        value = FunctionalExchange()
        tested.get_incoming()
        pass

    def test_LogicalFunction_outgoing(self):
        tested = LogicalFunction()
        value = FunctionalExchange()
        tested.get_outgoing()
        pass

    def test_LogicalFunction_allocating_component(self):
        tested = LogicalFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        self.assertEqual(tested.get_allocating_component(), value)
        pass

    def test_LogicalFunction_owned_functional_chains(self):
        tested = LogicalFunction()
        value = FunctionalChain()
        tested.get_owned_functional_chains()
        pass

    def test_LogicalFunction_involving_functional_chains(self):
        tested = LogicalFunction()
        value = FunctionalChain()
        tested.get_involving_functional_chains()
        pass

    def test_LogicalFunction_involving_capabilities(self):
        tested = LogicalFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities()
        pass

    def test_LogicalFunction_available_in_states(self):
        tested = LogicalFunction()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_LogicalFunction_id(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalFunction_sid(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalFunction_name(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalFunction_summary(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalFunction_description(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalFunction_status(self):
        tested = LogicalFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalFunction_review(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalFunction_visible_in_documentation(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalFunction_visible_for_traceability(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalFunction_owned_constraints(self):
        tested = LogicalFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalFunction_constraints(self):
        tested = LogicalFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalFunction_owned_property_values(self):
        tested = LogicalFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalFunction_applied_property_values(self):
        tested = LogicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalFunction_owned_property_value_groups(self):
        tested = LogicalFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalFunction_applied_property_value_groups(self):
        tested = LogicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalFunction_owned_enumeration_property_types(self):
        tested = LogicalFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalFunction_owned_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalFunction_element_of_interest_for_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalFunction_contextual_element_for_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalFunction_representing_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalFunction_id(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalFunction_sid(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalFunction_name(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalFunction_summary(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalFunction_description(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalFunction_status(self):
        tested = LogicalFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalFunction_review(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalFunction_visible_in_documentation(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalFunction_visible_for_traceability(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalFunction_owned_constraints(self):
        tested = LogicalFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalFunction_constraints(self):
        tested = LogicalFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalFunction_owned_property_values(self):
        tested = LogicalFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalFunction_applied_property_values(self):
        tested = LogicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalFunction_owned_property_value_groups(self):
        tested = LogicalFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalFunction_applied_property_value_groups(self):
        tested = LogicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalFunction_owned_enumeration_property_types(self):
        tested = LogicalFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalFunction_owned_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalFunction_element_of_interest_for_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalFunction_contextual_element_for_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalFunction_representing_diagrams(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalFunction_contained_logical_functions(self):
        tested = LogicalFunction()
        value = LogicalFunction()
        tested.get_contained_logical_functions()
        pass

    def test_LogicalFunction_owned_logical_function_pkgs(self):
        tested = LogicalFunction()
        value = LogicalFunctionPkg()
        tested.get_owned_logical_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_logical_function_pkgs().get(0), value)
        pass

    def test_LogicalFunction_realized_system_functions(self):
        tested = LogicalFunction()
        value = SystemFunction()
        tested.get_realized_system_functions()
        pass

    def test_LogicalFunction_realizing_physical_functions(self):
        tested = LogicalFunction()
        value = PhysicalFunction()
        tested.get_realizing_physical_functions()
        pass

    def test_CapabilityRealizationPkg_owned_property_value_pkgs(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_CapabilityRealizationPkg_id(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CapabilityRealizationPkg_sid(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_CapabilityRealizationPkg_name(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CapabilityRealizationPkg_summary(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_CapabilityRealizationPkg_description(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_CapabilityRealizationPkg_status(self):
        tested = CapabilityRealizationPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_CapabilityRealizationPkg_review(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_CapabilityRealizationPkg_visible_in_documentation(self):
        tested = CapabilityRealizationPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_CapabilityRealizationPkg_visible_for_traceability(self):
        tested = CapabilityRealizationPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_CapabilityRealizationPkg_owned_constraints(self):
        tested = CapabilityRealizationPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_CapabilityRealizationPkg_constraints(self):
        tested = CapabilityRealizationPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_CapabilityRealizationPkg_owned_property_values(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_CapabilityRealizationPkg_applied_property_values(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_CapabilityRealizationPkg_owned_property_value_groups(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_CapabilityRealizationPkg_applied_property_value_groups(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_CapabilityRealizationPkg_owned_enumeration_property_types(self):
        tested = CapabilityRealizationPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_CapabilityRealizationPkg_owned_diagrams(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CapabilityRealizationPkg_element_of_interest_for_diagrams(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CapabilityRealizationPkg_contextual_element_for_diagrams(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CapabilityRealizationPkg_representing_diagrams(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CapabilityRealizationPkg_owned_capability_realization_pkgs(self):
        tested = CapabilityRealizationPkg()
        value = CapabilityRealizationPkg()
        tested.get_owned_capability_realization_pkgs().add(value)
        self.assertEqual(tested.get_owned_capability_realization_pkgs().get(0), value)
        pass

    def test_CapabilityRealizationPkg_owned_capability_realizations(self):
        tested = CapabilityRealizationPkg()
        value = CapabilityRealization()
        tested.get_owned_capability_realizations().add(value)
        self.assertEqual(tested.get_owned_capability_realizations().get(0), value)
        pass

    def test_CapabilityRealization_owned_functional_chains(self):
        tested = CapabilityRealization()
        value = FunctionalChain()
        tested.get_owned_functional_chains()
        pass

    def test_CapabilityRealization_involved_functional_chains(self):
        tested = CapabilityRealization()
        value = FunctionalChain()
        tested.get_involved_functional_chains()
        pass

    def test_CapabilityRealization_involved_functions(self):
        tested = CapabilityRealization()
        value = PhysicalFunction()
        tested.get_involved_functions().add(value)
        self.assertEqual(tested.get_involved_functions().get(0), value)
        pass

    def test_CapabilityRealization_pre_condition(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_CapabilityRealization_post_condition(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_CapabilityRealization_owned_scenarios(self):
        tested = CapabilityRealization()
        value = Scenario()
        tested.get_owned_scenarios().add(value)
        self.assertEqual(tested.get_owned_scenarios().get(0), value)
        pass

    def test_CapabilityRealization_super(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_super()
        pass

    def test_CapabilityRealization_sub(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_sub()
        pass

    def test_CapabilityRealization_included_capabilities(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        self.assertEqual(tested.get_included_capabilities().get(0), value)
        pass

    def test_CapabilityRealization_including_capabilities(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        self.assertEqual(tested.get_including_capabilities().get(0), value)
        pass

    def test_CapabilityRealization_extended_capabilities(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        self.assertEqual(tested.get_extended_capabilities().get(0), value)
        pass

    def test_CapabilityRealization_extending_capabilities(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        self.assertEqual(tested.get_extending_capabilities().get(0), value)
        pass

    def test_CapabilityRealization_available_in_states(self):
        tested = CapabilityRealization()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_CapabilityRealization_owned_property_value_pkgs(self):
        tested = CapabilityRealization()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_CapabilityRealization_id(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CapabilityRealization_sid(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_CapabilityRealization_name(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CapabilityRealization_summary(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_CapabilityRealization_description(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_CapabilityRealization_status(self):
        tested = CapabilityRealization()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_CapabilityRealization_review(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_CapabilityRealization_visible_in_documentation(self):
        tested = CapabilityRealization()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_CapabilityRealization_visible_for_traceability(self):
        tested = CapabilityRealization()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_CapabilityRealization_owned_constraints(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_CapabilityRealization_constraints(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_CapabilityRealization_owned_property_values(self):
        tested = CapabilityRealization()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_CapabilityRealization_applied_property_values(self):
        tested = CapabilityRealization()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_CapabilityRealization_owned_property_value_groups(self):
        tested = CapabilityRealization()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_CapabilityRealization_applied_property_value_groups(self):
        tested = CapabilityRealization()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_CapabilityRealization_owned_enumeration_property_types(self):
        tested = CapabilityRealization()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_CapabilityRealization_owned_diagrams(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CapabilityRealization_element_of_interest_for_diagrams(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CapabilityRealization_contextual_element_for_diagrams(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CapabilityRealization_representing_diagrams(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CapabilityRealization_realized_capabilities(self):
        tested = CapabilityRealization()
        value = Capability()
        tested.get_realized_capabilities()
        pass

    def test_CapabilityRealization_realized_capability_realizations(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_realized_capability_realizations()
        pass

    def test_CapabilityRealization_realizing_capability_realizations(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_realizing_capability_realizations()
        pass

    def test_CapabilityRealization_involved_logical_actors(self):
        tested = CapabilityRealization()
        value = LogicalActor()
        tested.get_involved_logical_actors().add(value)
        self.assertEqual(tested.get_involved_logical_actors().get(0), value)
        pass

    def test_CapabilityRealization_involved_logical_components(self):
        tested = CapabilityRealization()
        value = LogicalComponent()
        tested.get_involved_logical_components().add(value)
        self.assertEqual(tested.get_involved_logical_components().get(0), value)
        pass

    def test_CapabilityRealization_involved_physical_components(self):
        tested = CapabilityRealization()
        value = NodePC()
        tested.get_involved_physical_components().add(value)
        self.assertEqual(tested.get_involved_physical_components().get(0), value)
        pass

    def test_CapabilityRealization_involved_physical_actors(self):
        tested = CapabilityRealization()
        value = PhysicalActor()
        tested.get_involved_physical_actors().add(value)
        self.assertEqual(tested.get_involved_physical_actors().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_property_value_pkgs(self):
        tested = LogicalComponentPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_LogicalComponentPkg_id(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalComponentPkg_sid(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalComponentPkg_name(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalComponentPkg_summary(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalComponentPkg_description(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalComponentPkg_status(self):
        tested = LogicalComponentPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalComponentPkg_review(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalComponentPkg_visible_in_documentation(self):
        tested = LogicalComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalComponentPkg_visible_for_traceability(self):
        tested = LogicalComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalComponentPkg_owned_constraints(self):
        tested = LogicalComponentPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalComponentPkg_constraints(self):
        tested = LogicalComponentPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalComponentPkg_owned_property_values(self):
        tested = LogicalComponentPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalComponentPkg_applied_property_values(self):
        tested = LogicalComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_property_value_groups(self):
        tested = LogicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalComponentPkg_applied_property_value_groups(self):
        tested = LogicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_enumeration_property_types(self):
        tested = LogicalComponentPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_diagrams(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalComponentPkg_element_of_interest_for_diagrams(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalComponentPkg_contextual_element_for_diagrams(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalComponentPkg_representing_diagrams(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_logical_component_pkgs(self):
        tested = LogicalComponentPkg()
        value = LogicalComponentPkg()
        tested.set_owned_logical_component_pkgs(value)
        self.assertEqual(tested.get_owned_logical_component_pkgs(), value)
        pass

    def test_LogicalComponentPkg_owned_logical_system(self):
        tested = LogicalComponentPkg()
        value = LogicalSystem()
        tested.set_owned_logical_system(value)
        self.assertEqual(tested.get_owned_logical_system(), value)
        pass

    def test_LogicalComponentPkg_owned_logical_actors(self):
        tested = LogicalComponentPkg()
        value = LogicalActor()
        tested.get_owned_logical_actors().add(value)
        self.assertEqual(tested.get_owned_logical_actors().get(0), value)
        pass

    def test_LogicalComponentPkg_owned_logical_components(self):
        tested = LogicalComponentPkg()
        value = LogicalComponent()
        tested.get_owned_logical_components().add(value)
        self.assertEqual(tested.get_owned_logical_components().get(0), value)
        pass

    def test_LogicalSystem_contained_component_ports(self):
        tested = LogicalSystem()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_LogicalSystem_incoming_component_exchanges(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_LogicalSystem_outgoing_component_exchanges(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_LogicalSystem_inout_component_exchanges(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_LogicalSystem_allocated_functions(self):
        tested = LogicalSystem()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_LogicalSystem_used_interfaces(self):
        tested = LogicalSystem()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_LogicalSystem_implemented_interfaces(self):
        tested = LogicalSystem()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_LogicalSystem_owned_state_machines(self):
        tested = LogicalSystem()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_LogicalSystem_id(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalSystem_sid(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalSystem_name(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalSystem_summary(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalSystem_description(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalSystem_status(self):
        tested = LogicalSystem()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalSystem_review(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalSystem_visible_in_documentation(self):
        tested = LogicalSystem()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalSystem_visible_for_traceability(self):
        tested = LogicalSystem()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalSystem_owned_constraints(self):
        tested = LogicalSystem()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalSystem_constraints(self):
        tested = LogicalSystem()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_LogicalSystem_owned_property_values(self):
        tested = LogicalSystem()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalSystem_applied_property_values(self):
        tested = LogicalSystem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalSystem_owned_property_value_groups(self):
        tested = LogicalSystem()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalSystem_applied_property_value_groups(self):
        tested = LogicalSystem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalSystem_owned_enumeration_property_types(self):
        tested = LogicalSystem()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalSystem_owned_diagrams(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalSystem_element_of_interest_for_diagrams(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalSystem_contextual_element_for_diagrams(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalSystem_representing_diagrams(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalSystem_contained_physical_ports(self):
        tested = LogicalSystem()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_LogicalSystem_physical_links(self):
        tested = LogicalSystem()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_LogicalSystem_involving_physical_paths(self):
        tested = LogicalSystem()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_LogicalSystem_owned_state_machines(self):
        tested = LogicalSystem()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_LogicalSystem_owned_logical_components(self):
        tested = LogicalSystem()
        value = LogicalComponent()
        tested.get_owned_logical_components().add(value)
        self.assertEqual(tested.get_owned_logical_components().get(0), value)
        pass

    def test_LogicalSystem_owned_logical_component_pkgs(self):
        tested = LogicalSystem()
        value = LogicalComponentPkg()
        tested.get_owned_logical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_logical_component_pkgs().get(0), value)
        pass

    def test_LogicalComponent_contained_component_ports(self):
        tested = LogicalComponent()
        value = ComponentPort()
        tested.get_contained_component_ports()
        pass

    def test_LogicalComponent_incoming_component_exchanges(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_LogicalComponent_outgoing_component_exchanges(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_LogicalComponent_inout_component_exchanges(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_LogicalComponent_allocated_functions(self):
        tested = LogicalComponent()
        value = PhysicalFunction()
        tested.get_allocated_functions()
        pass

    def test_LogicalComponent_used_interfaces(self):
        tested = LogicalComponent()
        value = Interface()
        tested.get_used_interfaces()
        pass

    def test_LogicalComponent_implemented_interfaces(self):
        tested = LogicalComponent()
        value = Interface()
        tested.get_implemented_interfaces()
        pass

    def test_LogicalComponent_owned_state_machines(self):
        tested = LogicalComponent()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_LogicalComponent_id(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalComponent_sid(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalComponent_name(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalComponent_summary(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalComponent_description(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalComponent_status(self):
        tested = LogicalComponent()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalComponent_review(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalComponent_visible_in_documentation(self):
        tested = LogicalComponent()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalComponent_visible_for_traceability(self):
        tested = LogicalComponent()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalComponent_owned_constraints(self):
        tested = LogicalComponent()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalComponent_constraints(self):
        tested = LogicalComponent()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_LogicalComponent_owned_property_values(self):
        tested = LogicalComponent()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalComponent_applied_property_values(self):
        tested = LogicalComponent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalComponent_owned_property_value_groups(self):
        tested = LogicalComponent()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalComponent_applied_property_value_groups(self):
        tested = LogicalComponent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalComponent_owned_enumeration_property_types(self):
        tested = LogicalComponent()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalComponent_owned_diagrams(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalComponent_element_of_interest_for_diagrams(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalComponent_contextual_element_for_diagrams(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalComponent_representing_diagrams(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalComponent_owned_logical_components(self):
        tested = LogicalComponent()
        value = LogicalComponent()
        tested.get_owned_logical_components().add(value)
        self.assertEqual(tested.get_owned_logical_components().get(0), value)
        pass

    def test_LogicalComponent_owned_logical_component_pkgs(self):
        tested = LogicalComponent()
        value = LogicalComponentPkg()
        tested.get_owned_logical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_logical_component_pkgs().get(0), value)
        pass

    def test_LogicalComponent_is_human(self):
        tested = LogicalComponent()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_LogicalComponent_realizing_behavior_p_cs(self):
        tested = LogicalComponent()
        value = BehaviorPC()
        tested.get_realizing_behavior_p_cs().add(value)
        self.assertEqual(tested.get_realizing_behavior_p_cs().get(0), value)
        pass

    def test_LogicalComponent_involving_capability_realizations(self):
        tested = LogicalComponent()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        self.assertEqual(tested.get_involving_capability_realizations().get(0), value)
        pass

    def test_LogicalActor_contained_component_ports(self):
        tested = LogicalActor()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_LogicalActor_incoming_component_exchanges(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_LogicalActor_outgoing_component_exchanges(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_LogicalActor_inout_component_exchanges(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_LogicalActor_allocated_functions(self):
        tested = LogicalActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_LogicalActor_used_interfaces(self):
        tested = LogicalActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_LogicalActor_implemented_interfaces(self):
        tested = LogicalActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_LogicalActor_owned_state_machines(self):
        tested = LogicalActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_LogicalActor_id(self):
        tested = LogicalActor()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_LogicalActor_sid(self):
        tested = LogicalActor()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_LogicalActor_name(self):
        tested = LogicalActor()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_LogicalActor_summary(self):
        tested = LogicalActor()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_LogicalActor_description(self):
        tested = LogicalActor()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_LogicalActor_status(self):
        tested = LogicalActor()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_LogicalActor_review(self):
        tested = LogicalActor()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_LogicalActor_visible_in_documentation(self):
        tested = LogicalActor()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_LogicalActor_visible_for_traceability(self):
        tested = LogicalActor()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_LogicalActor_owned_constraints(self):
        tested = LogicalActor()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_LogicalActor_constraints(self):
        tested = LogicalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_LogicalActor_owned_property_values(self):
        tested = LogicalActor()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_LogicalActor_applied_property_values(self):
        tested = LogicalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_LogicalActor_owned_property_value_groups(self):
        tested = LogicalActor()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_LogicalActor_applied_property_value_groups(self):
        tested = LogicalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_LogicalActor_owned_enumeration_property_types(self):
        tested = LogicalActor()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_LogicalActor_owned_diagrams(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_LogicalActor_element_of_interest_for_diagrams(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_LogicalActor_contextual_element_for_diagrams(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_LogicalActor_representing_diagrams(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_LogicalActor_contained_physical_ports(self):
        tested = LogicalActor()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_LogicalActor_physical_links(self):
        tested = LogicalActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_LogicalActor_involving_physical_paths(self):
        tested = LogicalActor()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_LogicalActor_owned_state_machines(self):
        tested = LogicalActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_LogicalActor_owned_logical_actors(self):
        tested = LogicalActor()
        value = LogicalActor()
        tested.get_owned_logical_actors().add(value)
        self.assertEqual(tested.get_owned_logical_actors().get(0), value)
        pass

    def test_LogicalActor_owned_logical_component_pkgs(self):
        tested = LogicalActor()
        value = LogicalComponentPkg()
        tested.get_owned_logical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_logical_component_pkgs().get(0), value)
        pass

    def test_LogicalActor_realized_system_actors(self):
        tested = LogicalActor()
        value = SystemActor()
        tested.get_realized_system_actors().add(value)
        self.assertEqual(tested.get_realized_system_actors().get(0), value)
        pass

    def test_LogicalActor_is_human(self):
        tested = LogicalActor()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_LogicalActor_realizing_physical_actors(self):
        tested = LogicalActor()
        value = PhysicalActor()
        tested.get_realizing_physical_actors().add(value)
        self.assertEqual(tested.get_realizing_physical_actors().get(0), value)
        pass

    def test_LogicalActor_involving_capability_realizations(self):
        tested = LogicalActor()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        self.assertEqual(tested.get_involving_capability_realizations().get(0), value)
        pass

    def test_PhysicalArchitecture_owned_property_value_pkgs(self):
        tested = PhysicalArchitecture()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_PhysicalArchitecture_id(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalArchitecture_sid(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalArchitecture_name(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalArchitecture_summary(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalArchitecture_description(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalArchitecture_status(self):
        tested = PhysicalArchitecture()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalArchitecture_review(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalArchitecture_visible_in_documentation(self):
        tested = PhysicalArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalArchitecture_visible_for_traceability(self):
        tested = PhysicalArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalArchitecture_owned_constraints(self):
        tested = PhysicalArchitecture()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalArchitecture_constraints(self):
        tested = PhysicalArchitecture()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalArchitecture_owned_property_values(self):
        tested = PhysicalArchitecture()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalArchitecture_applied_property_values(self):
        tested = PhysicalArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalArchitecture_owned_property_value_groups(self):
        tested = PhysicalArchitecture()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalArchitecture_applied_property_value_groups(self):
        tested = PhysicalArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalArchitecture_owned_enumeration_property_types(self):
        tested = PhysicalArchitecture()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalArchitecture_owned_diagrams(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalArchitecture_element_of_interest_for_diagrams(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalArchitecture_contextual_element_for_diagrams(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalArchitecture_representing_diagrams(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalArchitecture_physical_function_pkg(self):
        tested = PhysicalArchitecture()
        value = PhysicalFunctionPkg()
        tested.set_physical_function_pkg(value)
        self.assertEqual(tested.get_physical_function_pkg(), value)
        pass

    def test_PhysicalArchitecture_capability_realization_pkg(self):
        tested = PhysicalArchitecture()
        value = CapabilityRealizationPkg()
        tested.set_capability_realization_pkg(value)
        self.assertEqual(tested.get_capability_realization_pkg(), value)
        pass

    def test_PhysicalArchitecture_interface_pkg(self):
        tested = PhysicalArchitecture()
        value = InterfacePkg()
        tested.set_interface_pkg(value)
        self.assertEqual(tested.get_interface_pkg(), value)
        pass

    def test_PhysicalArchitecture_data_pkg(self):
        tested = PhysicalArchitecture()
        value = DataPkg()
        tested.set_data_pkg(value)
        self.assertEqual(tested.get_data_pkg(), value)
        pass

    def test_PhysicalArchitecture_physical_component_pkg(self):
        tested = PhysicalArchitecture()
        value = PhysicalComponentPkg()
        tested.set_physical_component_pkg(value)
        self.assertEqual(tested.get_physical_component_pkg(), value)
        pass

    def test_PhysicalFunctionPkg_owned_property_value_pkgs(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_PhysicalFunctionPkg_id(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalFunctionPkg_sid(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalFunctionPkg_name(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalFunctionPkg_summary(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalFunctionPkg_description(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalFunctionPkg_status(self):
        tested = PhysicalFunctionPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalFunctionPkg_review(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalFunctionPkg_visible_in_documentation(self):
        tested = PhysicalFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalFunctionPkg_visible_for_traceability(self):
        tested = PhysicalFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalFunctionPkg_owned_constraints(self):
        tested = PhysicalFunctionPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalFunctionPkg_constraints(self):
        tested = PhysicalFunctionPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalFunctionPkg_owned_property_values(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalFunctionPkg_applied_property_values(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalFunctionPkg_owned_property_value_groups(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunctionPkg_applied_property_value_groups(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunctionPkg_owned_enumeration_property_types(self):
        tested = PhysicalFunctionPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalFunctionPkg_owned_diagrams(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalFunctionPkg_element_of_interest_for_diagrams(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunctionPkg_contextual_element_for_diagrams(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunctionPkg_representing_diagrams(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalFunctionPkg_owned_physical_function_pkgs(self):
        tested = PhysicalFunctionPkg()
        value = PhysicalFunctionPkg()
        tested.get_owned_physical_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_function_pkgs().get(0), value)
        pass

    def test_PhysicalFunctionPkg_owned_physical_functions(self):
        tested = PhysicalFunctionPkg()
        value = PhysicalFunction()
        tested.get_owned_physical_functions().add(value)
        self.assertEqual(tested.get_owned_physical_functions().get(0), value)
        pass

    def test_PhysicalFunction_kind(self):
        tested = PhysicalFunction()
        value = FunctionKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_PhysicalFunction_condition(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_condition(value)
        self.assertEqual(tested.get_condition(), value)
        pass

    def test_PhysicalFunction_inputs(self):
        tested = PhysicalFunction()
        value = FunctionInputPort()
        tested.get_inputs().add(value)
        self.assertEqual(tested.get_inputs().get(0), value)
        pass

    def test_PhysicalFunction_outputs(self):
        tested = PhysicalFunction()
        value = FunctionOutputPort()
        tested.get_outputs().add(value)
        self.assertEqual(tested.get_outputs().get(0), value)
        pass

    def test_PhysicalFunction_incoming(self):
        tested = PhysicalFunction()
        value = FunctionalExchange()
        tested.get_incoming()
        pass

    def test_PhysicalFunction_outgoing(self):
        tested = PhysicalFunction()
        value = FunctionalExchange()
        tested.get_outgoing()
        pass

    def test_PhysicalFunction_allocating_component(self):
        tested = PhysicalFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        self.assertEqual(tested.get_allocating_component(), value)
        pass

    def test_PhysicalFunction_owned_functional_chains(self):
        tested = PhysicalFunction()
        value = FunctionalChain()
        tested.get_owned_functional_chains()
        pass

    def test_PhysicalFunction_involving_functional_chains(self):
        tested = PhysicalFunction()
        value = FunctionalChain()
        tested.get_involving_functional_chains()
        pass

    def test_PhysicalFunction_involving_capabilities(self):
        tested = PhysicalFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities()
        pass

    def test_PhysicalFunction_available_in_states(self):
        tested = PhysicalFunction()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_PhysicalFunction_id(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalFunction_sid(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalFunction_name(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalFunction_summary(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalFunction_description(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalFunction_status(self):
        tested = PhysicalFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalFunction_review(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalFunction_visible_in_documentation(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalFunction_visible_for_traceability(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalFunction_owned_constraints(self):
        tested = PhysicalFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalFunction_constraints(self):
        tested = PhysicalFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalFunction_owned_property_values(self):
        tested = PhysicalFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalFunction_applied_property_values(self):
        tested = PhysicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalFunction_owned_property_value_groups(self):
        tested = PhysicalFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunction_applied_property_value_groups(self):
        tested = PhysicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunction_owned_enumeration_property_types(self):
        tested = PhysicalFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalFunction_owned_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_element_of_interest_for_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_contextual_element_for_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_representing_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_id(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalFunction_sid(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalFunction_name(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalFunction_summary(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalFunction_description(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalFunction_status(self):
        tested = PhysicalFunction()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalFunction_review(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalFunction_visible_in_documentation(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalFunction_visible_for_traceability(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalFunction_owned_constraints(self):
        tested = PhysicalFunction()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalFunction_constraints(self):
        tested = PhysicalFunction()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalFunction_owned_property_values(self):
        tested = PhysicalFunction()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalFunction_applied_property_values(self):
        tested = PhysicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalFunction_owned_property_value_groups(self):
        tested = PhysicalFunction()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunction_applied_property_value_groups(self):
        tested = PhysicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalFunction_owned_enumeration_property_types(self):
        tested = PhysicalFunction()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalFunction_owned_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_element_of_interest_for_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_contextual_element_for_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_representing_diagrams(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalFunction_contained_physical_functions(self):
        tested = PhysicalFunction()
        value = PhysicalFunction()
        tested.get_contained_physical_functions()
        pass

    def test_PhysicalFunction_owned_physical_function_pkgs(self):
        tested = PhysicalFunction()
        value = PhysicalFunctionPkg()
        tested.get_owned_physical_function_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_function_pkgs().get(0), value)
        pass

    def test_PhysicalFunction_realized_logical_functions(self):
        tested = PhysicalFunction()
        value = LogicalFunction()
        tested.get_realized_logical_functions()
        pass

    def test_PhysicalComponentPkg_owned_property_value_pkgs(self):
        tested = PhysicalComponentPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_PhysicalComponentPkg_id(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalComponentPkg_sid(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalComponentPkg_name(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalComponentPkg_summary(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalComponentPkg_description(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalComponentPkg_status(self):
        tested = PhysicalComponentPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalComponentPkg_review(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalComponentPkg_visible_in_documentation(self):
        tested = PhysicalComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalComponentPkg_visible_for_traceability(self):
        tested = PhysicalComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalComponentPkg_owned_constraints(self):
        tested = PhysicalComponentPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalComponentPkg_constraints(self):
        tested = PhysicalComponentPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalComponentPkg_owned_property_values(self):
        tested = PhysicalComponentPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalComponentPkg_applied_property_values(self):
        tested = PhysicalComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_property_value_groups(self):
        tested = PhysicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalComponentPkg_applied_property_value_groups(self):
        tested = PhysicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_enumeration_property_types(self):
        tested = PhysicalComponentPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_diagrams(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalComponentPkg_element_of_interest_for_diagrams(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalComponentPkg_contextual_element_for_diagrams(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalComponentPkg_representing_diagrams(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_physical_component_pkgs(self):
        tested = PhysicalComponentPkg()
        value = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_component_pkgs().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_physical_system(self):
        tested = PhysicalComponentPkg()
        value = PhysicalSystem()
        tested.set_owned_physical_system(value)
        self.assertEqual(tested.get_owned_physical_system(), value)
        pass

    def test_PhysicalComponentPkg_owned_physical_actors(self):
        tested = PhysicalComponentPkg()
        value = PhysicalActor()
        tested.get_owned_physical_actors().add(value)
        self.assertEqual(tested.get_owned_physical_actors().get(0), value)
        pass

    def test_PhysicalComponentPkg_owned_physical_components(self):
        tested = PhysicalComponentPkg()
        value = NodePC()
        tested.get_owned_physical_components().add(value)
        self.assertEqual(tested.get_owned_physical_components().get(0), value)
        pass

    def test_PhysicalSystem_id(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalSystem_sid(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalSystem_name(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalSystem_summary(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalSystem_description(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalSystem_status(self):
        tested = PhysicalSystem()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalSystem_review(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalSystem_visible_in_documentation(self):
        tested = PhysicalSystem()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalSystem_visible_for_traceability(self):
        tested = PhysicalSystem()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalSystem_owned_constraints(self):
        tested = PhysicalSystem()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalSystem_constraints(self):
        tested = PhysicalSystem()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_PhysicalSystem_owned_property_values(self):
        tested = PhysicalSystem()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalSystem_applied_property_values(self):
        tested = PhysicalSystem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalSystem_owned_property_value_groups(self):
        tested = PhysicalSystem()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalSystem_applied_property_value_groups(self):
        tested = PhysicalSystem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalSystem_owned_enumeration_property_types(self):
        tested = PhysicalSystem()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalSystem_owned_diagrams(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalSystem_element_of_interest_for_diagrams(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalSystem_contextual_element_for_diagrams(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalSystem_representing_diagrams(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalSystem_owned_physical_components(self):
        tested = PhysicalSystem()
        value = NodePC()
        tested.get_owned_physical_components().add(value)
        self.assertEqual(tested.get_owned_physical_components().get(0), value)
        pass

    def test_PhysicalSystem_owned_physical_component_pkgs(self):
        tested = PhysicalSystem()
        value = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_component_pkgs().get(0), value)
        pass

    def test_BehaviorPC_kind(self):
        tested = BehaviorPC()
        value = PhysicalComponentKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_BehaviorPC_owned_physical_components(self):
        tested = BehaviorPC()
        value = NodePC()
        tested.get_owned_physical_components().add(value)
        self.assertEqual(tested.get_owned_physical_components().get(0), value)
        pass

    def test_BehaviorPC_owned_physical_component_pkgs(self):
        tested = BehaviorPC()
        value = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_component_pkgs().get(0), value)
        pass

    def test_BehaviorPC_is_human(self):
        tested = BehaviorPC()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_BehaviorPC_involving_capability_realizations(self):
        tested = BehaviorPC()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        self.assertEqual(tested.get_involving_capability_realizations().get(0), value)
        pass

    def test_BehaviorPC_allocator_configuration_items(self):
        tested = BehaviorPC()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        self.assertEqual(tested.get_allocator_configuration_items().get(0), value)
        pass

    def test_BehaviorPC_id(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_BehaviorPC_sid(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_BehaviorPC_name(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_BehaviorPC_summary(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_BehaviorPC_description(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_BehaviorPC_status(self):
        tested = BehaviorPC()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_BehaviorPC_review(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_BehaviorPC_visible_in_documentation(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_BehaviorPC_visible_for_traceability(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_BehaviorPC_owned_constraints(self):
        tested = BehaviorPC()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_BehaviorPC_constraints(self):
        tested = BehaviorPC()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_BehaviorPC_owned_property_values(self):
        tested = BehaviorPC()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_BehaviorPC_applied_property_values(self):
        tested = BehaviorPC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_BehaviorPC_owned_property_value_groups(self):
        tested = BehaviorPC()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_BehaviorPC_applied_property_value_groups(self):
        tested = BehaviorPC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_BehaviorPC_owned_enumeration_property_types(self):
        tested = BehaviorPC()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_BehaviorPC_owned_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_BehaviorPC_element_of_interest_for_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_BehaviorPC_contextual_element_for_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_BehaviorPC_representing_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_BehaviorPC_contained_component_ports(self):
        tested = BehaviorPC()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_BehaviorPC_incoming_component_exchanges(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_BehaviorPC_outgoing_component_exchanges(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_BehaviorPC_inout_component_exchanges(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_BehaviorPC_allocated_functions(self):
        tested = BehaviorPC()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_BehaviorPC_used_interfaces(self):
        tested = BehaviorPC()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_BehaviorPC_implemented_interfaces(self):
        tested = BehaviorPC()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_BehaviorPC_owned_state_machines(self):
        tested = BehaviorPC()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_BehaviorPC_id(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_BehaviorPC_sid(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_BehaviorPC_name(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_BehaviorPC_summary(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_BehaviorPC_description(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_BehaviorPC_status(self):
        tested = BehaviorPC()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_BehaviorPC_review(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_BehaviorPC_visible_in_documentation(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_BehaviorPC_visible_for_traceability(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_BehaviorPC_owned_constraints(self):
        tested = BehaviorPC()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_BehaviorPC_constraints(self):
        tested = BehaviorPC()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_BehaviorPC_owned_property_values(self):
        tested = BehaviorPC()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_BehaviorPC_applied_property_values(self):
        tested = BehaviorPC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_BehaviorPC_owned_property_value_groups(self):
        tested = BehaviorPC()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_BehaviorPC_applied_property_value_groups(self):
        tested = BehaviorPC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_BehaviorPC_owned_enumeration_property_types(self):
        tested = BehaviorPC()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_BehaviorPC_owned_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_BehaviorPC_element_of_interest_for_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_BehaviorPC_contextual_element_for_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_BehaviorPC_representing_diagrams(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_BehaviorPC_deploying_node_p_c(self):
        tested = BehaviorPC()
        value = NodePC()
        tested.set_deploying_node_p_c(value)
        self.assertEqual(tested.get_deploying_node_p_c(), value)
        pass

    def test_BehaviorPC_realized_logical_components(self):
        tested = BehaviorPC()
        value = LogicalComponent()
        tested.get_realized_logical_components().add(value)
        self.assertEqual(tested.get_realized_logical_components().get(0), value)
        pass

    def test_NodePC_kind(self):
        tested = NodePC()
        value = PhysicalComponentKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_NodePC_owned_physical_components(self):
        tested = NodePC()
        value = NodePC()
        tested.get_owned_physical_components().add(value)
        self.assertEqual(tested.get_owned_physical_components().get(0), value)
        pass

    def test_NodePC_owned_physical_component_pkgs(self):
        tested = NodePC()
        value = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_component_pkgs().get(0), value)
        pass

    def test_NodePC_is_human(self):
        tested = NodePC()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_NodePC_involving_capability_realizations(self):
        tested = NodePC()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        self.assertEqual(tested.get_involving_capability_realizations().get(0), value)
        pass

    def test_NodePC_allocator_configuration_items(self):
        tested = NodePC()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        self.assertEqual(tested.get_allocator_configuration_items().get(0), value)
        pass

    def test_NodePC_id(self):
        tested = NodePC()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_NodePC_sid(self):
        tested = NodePC()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_NodePC_name(self):
        tested = NodePC()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_NodePC_summary(self):
        tested = NodePC()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_NodePC_description(self):
        tested = NodePC()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_NodePC_status(self):
        tested = NodePC()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_NodePC_review(self):
        tested = NodePC()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_NodePC_visible_in_documentation(self):
        tested = NodePC()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_NodePC_visible_for_traceability(self):
        tested = NodePC()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_NodePC_owned_constraints(self):
        tested = NodePC()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_NodePC_constraints(self):
        tested = NodePC()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_NodePC_owned_property_values(self):
        tested = NodePC()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_NodePC_applied_property_values(self):
        tested = NodePC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_NodePC_owned_property_value_groups(self):
        tested = NodePC()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_NodePC_applied_property_value_groups(self):
        tested = NodePC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_NodePC_owned_enumeration_property_types(self):
        tested = NodePC()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_NodePC_owned_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_NodePC_element_of_interest_for_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_NodePC_contextual_element_for_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_NodePC_representing_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_NodePC_id(self):
        tested = NodePC()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_NodePC_sid(self):
        tested = NodePC()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_NodePC_name(self):
        tested = NodePC()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_NodePC_summary(self):
        tested = NodePC()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_NodePC_description(self):
        tested = NodePC()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_NodePC_status(self):
        tested = NodePC()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_NodePC_review(self):
        tested = NodePC()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_NodePC_visible_in_documentation(self):
        tested = NodePC()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_NodePC_visible_for_traceability(self):
        tested = NodePC()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_NodePC_owned_constraints(self):
        tested = NodePC()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_NodePC_constraints(self):
        tested = NodePC()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_NodePC_owned_property_values(self):
        tested = NodePC()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_NodePC_applied_property_values(self):
        tested = NodePC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_NodePC_owned_property_value_groups(self):
        tested = NodePC()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_NodePC_applied_property_value_groups(self):
        tested = NodePC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_NodePC_owned_enumeration_property_types(self):
        tested = NodePC()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_NodePC_owned_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_NodePC_element_of_interest_for_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_NodePC_contextual_element_for_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_NodePC_representing_diagrams(self):
        tested = NodePC()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_NodePC_contained_physical_ports(self):
        tested = NodePC()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_NodePC_physical_links(self):
        tested = NodePC()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_NodePC_involving_physical_paths(self):
        tested = NodePC()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_NodePC_owned_state_machines(self):
        tested = NodePC()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_NodePC_deployed_behavior_p_cs(self):
        tested = NodePC()
        value = BehaviorPC()
        tested.get_deployed_behavior_p_cs().add(value)
        self.assertEqual(tested.get_deployed_behavior_p_cs().get(0), value)
        pass

    def test_PhysicalActor_contained_component_ports(self):
        tested = PhysicalActor()
        value = ComponentPort()
        tested.get_contained_component_ports().add(value)
        self.assertEqual(tested.get_contained_component_ports().get(0), value)
        pass

    def test_PhysicalActor_incoming_component_exchanges(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        self.assertEqual(tested.get_incoming_component_exchanges().get(0), value)
        pass

    def test_PhysicalActor_outgoing_component_exchanges(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        self.assertEqual(tested.get_outgoing_component_exchanges().get(0), value)
        pass

    def test_PhysicalActor_inout_component_exchanges(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        self.assertEqual(tested.get_inout_component_exchanges().get(0), value)
        pass

    def test_PhysicalActor_allocated_functions(self):
        tested = PhysicalActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        self.assertEqual(tested.get_allocated_functions().get(0), value)
        pass

    def test_PhysicalActor_used_interfaces(self):
        tested = PhysicalActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        self.assertEqual(tested.get_used_interfaces().get(0), value)
        pass

    def test_PhysicalActor_implemented_interfaces(self):
        tested = PhysicalActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        self.assertEqual(tested.get_implemented_interfaces().get(0), value)
        pass

    def test_PhysicalActor_owned_state_machines(self):
        tested = PhysicalActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_PhysicalActor_id(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalActor_sid(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalActor_name(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalActor_summary(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalActor_description(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalActor_status(self):
        tested = PhysicalActor()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalActor_review(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalActor_visible_in_documentation(self):
        tested = PhysicalActor()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalActor_visible_for_traceability(self):
        tested = PhysicalActor()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalActor_owned_constraints(self):
        tested = PhysicalActor()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalActor_constraints(self):
        tested = PhysicalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_PhysicalActor_owned_property_values(self):
        tested = PhysicalActor()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalActor_applied_property_values(self):
        tested = PhysicalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalActor_owned_property_value_groups(self):
        tested = PhysicalActor()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalActor_applied_property_value_groups(self):
        tested = PhysicalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalActor_owned_enumeration_property_types(self):
        tested = PhysicalActor()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalActor_owned_diagrams(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalActor_element_of_interest_for_diagrams(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalActor_contextual_element_for_diagrams(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalActor_representing_diagrams(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalActor_contained_physical_ports(self):
        tested = PhysicalActor()
        value = PhysicalPort()
        tested.get_contained_physical_ports().add(value)
        self.assertEqual(tested.get_contained_physical_ports().get(0), value)
        pass

    def test_PhysicalActor_physical_links(self):
        tested = PhysicalActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        self.assertEqual(tested.get_physical_links().get(0), value)
        pass

    def test_PhysicalActor_involving_physical_paths(self):
        tested = PhysicalActor()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_PhysicalActor_owned_state_machines(self):
        tested = PhysicalActor()
        value = StateMachine()
        tested.get_owned_state_machines().add(value)
        self.assertEqual(tested.get_owned_state_machines().get(0), value)
        pass

    def test_PhysicalActor_owned_physical_actors(self):
        tested = PhysicalActor()
        value = PhysicalActor()
        tested.get_owned_physical_actors().add(value)
        self.assertEqual(tested.get_owned_physical_actors().get(0), value)
        pass

    def test_PhysicalActor_owned_physical_component_pkgs(self):
        tested = PhysicalActor()
        value = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs().add(value)
        self.assertEqual(tested.get_owned_physical_component_pkgs().get(0), value)
        pass

    def test_PhysicalActor_realized_logical_actors(self):
        tested = PhysicalActor()
        value = LogicalActor()
        tested.get_realized_logical_actors().add(value)
        self.assertEqual(tested.get_realized_logical_actors().get(0), value)
        pass

    def test_PhysicalActor_is_human(self):
        tested = PhysicalActor()
        value = True
        tested.set_is_human(value)
        self.assertEqual(tested.get_is_human(), value)
        pass

    def test_PhysicalActor_involving_capability_realizations(self):
        tested = PhysicalActor()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        self.assertEqual(tested.get_involving_capability_realizations().get(0), value)
        pass

    def test_EPBSArchitecture_owned_property_value_pkgs(self):
        tested = EPBSArchitecture()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_EPBSArchitecture_id(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_EPBSArchitecture_sid(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_EPBSArchitecture_name(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_EPBSArchitecture_summary(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_EPBSArchitecture_description(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_EPBSArchitecture_status(self):
        tested = EPBSArchitecture()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_EPBSArchitecture_review(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_EPBSArchitecture_visible_in_documentation(self):
        tested = EPBSArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_EPBSArchitecture_visible_for_traceability(self):
        tested = EPBSArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_EPBSArchitecture_owned_constraints(self):
        tested = EPBSArchitecture()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_EPBSArchitecture_constraints(self):
        tested = EPBSArchitecture()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_EPBSArchitecture_owned_property_values(self):
        tested = EPBSArchitecture()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_EPBSArchitecture_applied_property_values(self):
        tested = EPBSArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_EPBSArchitecture_owned_property_value_groups(self):
        tested = EPBSArchitecture()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_EPBSArchitecture_applied_property_value_groups(self):
        tested = EPBSArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_EPBSArchitecture_owned_enumeration_property_types(self):
        tested = EPBSArchitecture()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_EPBSArchitecture_owned_diagrams(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_EPBSArchitecture_element_of_interest_for_diagrams(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_EPBSArchitecture_contextual_element_for_diagrams(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_EPBSArchitecture_representing_diagrams(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_EPBSArchitecture_capability_realization_pkg(self):
        tested = EPBSArchitecture()
        value = CapabilityRealizationPkg()
        tested.set_capability_realization_pkg(value)
        self.assertEqual(tested.get_capability_realization_pkg(), value)
        pass

    def test_EPBSArchitecture_configuration_item_pkg(self):
        tested = EPBSArchitecture()
        value = ConfigurationItemPkg()
        tested.set_configuration_item_pkg(value)
        self.assertEqual(tested.get_configuration_item_pkg(), value)
        pass

    def test_EPBSArchitecture_data_pkg(self):
        tested = EPBSArchitecture()
        value = DataPkg()
        tested.set_data_pkg(value)
        self.assertEqual(tested.get_data_pkg(), value)
        pass

    def test_ConfigurationItemPkg_owned_property_value_pkgs(self):
        tested = ConfigurationItemPkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_ConfigurationItemPkg_id(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ConfigurationItemPkg_sid(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ConfigurationItemPkg_name(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ConfigurationItemPkg_summary(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ConfigurationItemPkg_description(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ConfigurationItemPkg_status(self):
        tested = ConfigurationItemPkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ConfigurationItemPkg_review(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ConfigurationItemPkg_visible_in_documentation(self):
        tested = ConfigurationItemPkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ConfigurationItemPkg_visible_for_traceability(self):
        tested = ConfigurationItemPkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ConfigurationItemPkg_owned_constraints(self):
        tested = ConfigurationItemPkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ConfigurationItemPkg_constraints(self):
        tested = ConfigurationItemPkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ConfigurationItemPkg_owned_property_values(self):
        tested = ConfigurationItemPkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ConfigurationItemPkg_applied_property_values(self):
        tested = ConfigurationItemPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ConfigurationItemPkg_owned_property_value_groups(self):
        tested = ConfigurationItemPkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ConfigurationItemPkg_applied_property_value_groups(self):
        tested = ConfigurationItemPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ConfigurationItemPkg_owned_enumeration_property_types(self):
        tested = ConfigurationItemPkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ConfigurationItemPkg_owned_diagrams(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ConfigurationItemPkg_element_of_interest_for_diagrams(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ConfigurationItemPkg_contextual_element_for_diagrams(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ConfigurationItemPkg_representing_diagrams(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ConfigurationItemPkg_owned_configuration_item_pkgs(self):
        tested = ConfigurationItemPkg()
        value = ConfigurationItemPkg()
        tested.get_owned_configuration_item_pkgs().add(value)
        self.assertEqual(tested.get_owned_configuration_item_pkgs().get(0), value)
        pass

    def test_ConfigurationItemPkg_owned_configuration_items(self):
        tested = ConfigurationItemPkg()
        value = ConfigurationItem()
        tested.get_owned_configuration_items().add(value)
        self.assertEqual(tested.get_owned_configuration_items().get(0), value)
        pass

    def test_ConfigurationItem_id(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ConfigurationItem_sid(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ConfigurationItem_name(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ConfigurationItem_summary(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ConfigurationItem_description(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ConfigurationItem_status(self):
        tested = ConfigurationItem()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ConfigurationItem_review(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ConfigurationItem_visible_in_documentation(self):
        tested = ConfigurationItem()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ConfigurationItem_visible_for_traceability(self):
        tested = ConfigurationItem()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ConfigurationItem_owned_constraints(self):
        tested = ConfigurationItem()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ConfigurationItem_constraints(self):
        tested = ConfigurationItem()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ConfigurationItem_owned_property_values(self):
        tested = ConfigurationItem()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ConfigurationItem_applied_property_values(self):
        tested = ConfigurationItem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ConfigurationItem_owned_property_value_groups(self):
        tested = ConfigurationItem()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ConfigurationItem_applied_property_value_groups(self):
        tested = ConfigurationItem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ConfigurationItem_owned_enumeration_property_types(self):
        tested = ConfigurationItem()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ConfigurationItem_owned_diagrams(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ConfigurationItem_element_of_interest_for_diagrams(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ConfigurationItem_contextual_element_for_diagrams(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ConfigurationItem_representing_diagrams(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ConfigurationItem_item_identifier(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_item_identifier(value)
        self.assertEqual(tested.get_item_identifier(), value)
        pass

    def test_ConfigurationItem_kind(self):
        tested = ConfigurationItem()
        value = ConfigurationItemKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_ConfigurationItem_owned_configuration_items(self):
        tested = ConfigurationItem()
        value = ConfigurationItem()
        tested.get_owned_configuration_items().add(value)
        self.assertEqual(tested.get_owned_configuration_items().get(0), value)
        pass

    def test_ConfigurationItem_owned_configuration_item_pkgs(self):
        tested = ConfigurationItem()
        value = ConfigurationItemPkg()
        tested.get_owned_configuration_item_pkgs().add(value)
        self.assertEqual(tested.get_owned_configuration_item_pkgs().get(0), value)
        pass

    def test_ConfigurationItem_allocated_physical_artifacts(self):
        tested = ConfigurationItem()
        value = PhysicalLink()
        tested.get_allocated_physical_artifacts()
        pass

    def test_StateMachine_id(self):
        tested = StateMachine()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_StateMachine_sid(self):
        tested = StateMachine()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_StateMachine_name(self):
        tested = StateMachine()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_StateMachine_summary(self):
        tested = StateMachine()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_StateMachine_description(self):
        tested = StateMachine()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_StateMachine_status(self):
        tested = StateMachine()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_StateMachine_review(self):
        tested = StateMachine()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_StateMachine_visible_in_documentation(self):
        tested = StateMachine()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_StateMachine_visible_for_traceability(self):
        tested = StateMachine()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_StateMachine_owned_constraints(self):
        tested = StateMachine()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_StateMachine_constraints(self):
        tested = StateMachine()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_StateMachine_owned_property_values(self):
        tested = StateMachine()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_StateMachine_applied_property_values(self):
        tested = StateMachine()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_StateMachine_owned_property_value_groups(self):
        tested = StateMachine()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_StateMachine_applied_property_value_groups(self):
        tested = StateMachine()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_StateMachine_owned_enumeration_property_types(self):
        tested = StateMachine()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_StateMachine_owned_diagrams(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_StateMachine_element_of_interest_for_diagrams(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_StateMachine_contextual_element_for_diagrams(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_StateMachine_representing_diagrams(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_StateMachine_owned_regions(self):
        tested = StateMachine()
        value = Region()
        tested.get_owned_regions().add(value)
        self.assertEqual(tested.get_owned_regions().get(0), value)
        pass

    def test_State_incoming(self):
        tested = State()
        value = StateTransition()
        tested.get_incoming()
        pass

    def test_State_outgoing(self):
        tested = State()
        value = StateTransition()
        tested.get_outgoing()
        pass

    def test_State_realized_states(self):
        tested = State()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        self.assertEqual(tested.get_realized_states().get(0), value)
        pass

    def test_State_realizing_states(self):
        tested = State()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        self.assertEqual(tested.get_realizing_states().get(0), value)
        pass

    def test_State_id(self):
        tested = State()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_State_sid(self):
        tested = State()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_State_name(self):
        tested = State()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_State_summary(self):
        tested = State()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_State_description(self):
        tested = State()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_State_status(self):
        tested = State()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_State_review(self):
        tested = State()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_State_visible_in_documentation(self):
        tested = State()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_State_visible_for_traceability(self):
        tested = State()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_State_owned_constraints(self):
        tested = State()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_State_constraints(self):
        tested = State()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_State_owned_property_values(self):
        tested = State()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_State_applied_property_values(self):
        tested = State()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_State_owned_property_value_groups(self):
        tested = State()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_State_applied_property_value_groups(self):
        tested = State()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_State_owned_enumeration_property_types(self):
        tested = State()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_State_owned_diagrams(self):
        tested = State()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_State_element_of_interest_for_diagrams(self):
        tested = State()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_State_contextual_element_for_diagrams(self):
        tested = State()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_State_representing_diagrams(self):
        tested = State()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_State_owned_regions(self):
        tested = State()
        value = Region()
        tested.get_owned_regions().add(value)
        self.assertEqual(tested.get_owned_regions().get(0), value)
        pass

    def test_State_available_activities__functions(self):
        tested = State()
        value = PhysicalFunction()
        tested.get_available_activities__functions().add(value)
        self.assertEqual(tested.get_available_activities__functions().get(0), value)
        pass

    def test_State_entry(self):
        tested = State()
        value = ExchangeItem()
        tested.get_entry().add(value)
        self.assertEqual(tested.get_entry().get(0), value)
        pass

    def test_State_do(self):
        tested = State()
        value = ExchangeItem()
        tested.get_do().add(value)
        self.assertEqual(tested.get_do().get(0), value)
        pass

    def test_State_exit(self):
        tested = State()
        value = ExchangeItem()
        tested.get_exit().add(value)
        self.assertEqual(tested.get_exit().get(0), value)
        pass

    def test_State_available_functional_chains(self):
        tested = State()
        value = FunctionalChain()
        tested.get_available_functional_chains().add(value)
        self.assertEqual(tested.get_available_functional_chains().get(0), value)
        pass

    def test_State_available_operational_processes(self):
        tested = State()
        value = OperationalProcess()
        tested.get_available_operational_processes().add(value)
        self.assertEqual(tested.get_available_operational_processes().get(0), value)
        pass

    def test_State_available_capabilities(self):
        tested = State()
        value = CapabilityRealization()
        tested.get_available_capabilities().add(value)
        self.assertEqual(tested.get_available_capabilities().get(0), value)
        pass

    def test_Mode_owned_regions(self):
        tested = Mode()
        value = Region()
        tested.get_owned_regions().add(value)
        self.assertEqual(tested.get_owned_regions().get(0), value)
        pass

    def test_Mode_available_activities__functions(self):
        tested = Mode()
        value = PhysicalFunction()
        tested.get_available_activities__functions().add(value)
        self.assertEqual(tested.get_available_activities__functions().get(0), value)
        pass

    def test_Mode_entry(self):
        tested = Mode()
        value = ExchangeItem()
        tested.get_entry().add(value)
        self.assertEqual(tested.get_entry().get(0), value)
        pass

    def test_Mode_do(self):
        tested = Mode()
        value = ExchangeItem()
        tested.get_do().add(value)
        self.assertEqual(tested.get_do().get(0), value)
        pass

    def test_Mode_exit(self):
        tested = Mode()
        value = ExchangeItem()
        tested.get_exit().add(value)
        self.assertEqual(tested.get_exit().get(0), value)
        pass

    def test_Mode_available_functional_chains(self):
        tested = Mode()
        value = FunctionalChain()
        tested.get_available_functional_chains().add(value)
        self.assertEqual(tested.get_available_functional_chains().get(0), value)
        pass

    def test_Mode_available_operational_processes(self):
        tested = Mode()
        value = OperationalProcess()
        tested.get_available_operational_processes().add(value)
        self.assertEqual(tested.get_available_operational_processes().get(0), value)
        pass

    def test_Mode_available_capabilities(self):
        tested = Mode()
        value = CapabilityRealization()
        tested.get_available_capabilities().add(value)
        self.assertEqual(tested.get_available_capabilities().get(0), value)
        pass

    def test_Mode_incoming(self):
        tested = Mode()
        value = StateTransition()
        tested.get_incoming()
        pass

    def test_Mode_outgoing(self):
        tested = Mode()
        value = StateTransition()
        tested.get_outgoing()
        pass

    def test_Mode_realized_states(self):
        tested = Mode()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        self.assertEqual(tested.get_realized_states().get(0), value)
        pass

    def test_Mode_realizing_states(self):
        tested = Mode()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        self.assertEqual(tested.get_realizing_states().get(0), value)
        pass

    def test_Mode_id(self):
        tested = Mode()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Mode_sid(self):
        tested = Mode()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Mode_name(self):
        tested = Mode()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Mode_summary(self):
        tested = Mode()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Mode_description(self):
        tested = Mode()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Mode_status(self):
        tested = Mode()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Mode_review(self):
        tested = Mode()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Mode_visible_in_documentation(self):
        tested = Mode()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Mode_visible_for_traceability(self):
        tested = Mode()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Mode_owned_constraints(self):
        tested = Mode()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Mode_constraints(self):
        tested = Mode()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Mode_owned_property_values(self):
        tested = Mode()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Mode_applied_property_values(self):
        tested = Mode()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Mode_owned_property_value_groups(self):
        tested = Mode()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Mode_applied_property_value_groups(self):
        tested = Mode()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Mode_owned_enumeration_property_types(self):
        tested = Mode()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Mode_owned_diagrams(self):
        tested = Mode()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Mode_element_of_interest_for_diagrams(self):
        tested = Mode()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Mode_contextual_element_for_diagrams(self):
        tested = Mode()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Mode_representing_diagrams(self):
        tested = Mode()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Pseudostate_incoming(self):
        tested = Pseudostate()
        value = StateTransition()
        tested.get_incoming().add(value)
        self.assertEqual(tested.get_incoming().get(0), value)
        pass

    def test_Pseudostate_outgoing(self):
        tested = Pseudostate()
        value = StateTransition()
        tested.get_outgoing().add(value)
        self.assertEqual(tested.get_outgoing().get(0), value)
        pass

    def test_Pseudostate_realized_states(self):
        tested = Pseudostate()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        self.assertEqual(tested.get_realized_states().get(0), value)
        pass

    def test_Pseudostate_realizing_states(self):
        tested = Pseudostate()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        self.assertEqual(tested.get_realizing_states().get(0), value)
        pass

    def test_Pseudostate_id(self):
        tested = Pseudostate()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Pseudostate_sid(self):
        tested = Pseudostate()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Pseudostate_name(self):
        tested = Pseudostate()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Pseudostate_summary(self):
        tested = Pseudostate()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Pseudostate_description(self):
        tested = Pseudostate()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Pseudostate_status(self):
        tested = Pseudostate()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Pseudostate_review(self):
        tested = Pseudostate()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Pseudostate_visible_in_documentation(self):
        tested = Pseudostate()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Pseudostate_visible_for_traceability(self):
        tested = Pseudostate()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Pseudostate_owned_constraints(self):
        tested = Pseudostate()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Pseudostate_constraints(self):
        tested = Pseudostate()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_Pseudostate_owned_property_values(self):
        tested = Pseudostate()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Pseudostate_applied_property_values(self):
        tested = Pseudostate()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Pseudostate_owned_property_value_groups(self):
        tested = Pseudostate()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Pseudostate_applied_property_value_groups(self):
        tested = Pseudostate()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Pseudostate_owned_enumeration_property_types(self):
        tested = Pseudostate()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Pseudostate_owned_diagrams(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Pseudostate_element_of_interest_for_diagrams(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Pseudostate_contextual_element_for_diagrams(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Pseudostate_representing_diagrams(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Pseudostate_kind(self):
        tested = Pseudostate()
        value = PseudoStateKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_Region_id(self):
        tested = Region()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Region_sid(self):
        tested = Region()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Region_name(self):
        tested = Region()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Region_summary(self):
        tested = Region()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Region_description(self):
        tested = Region()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Region_status(self):
        tested = Region()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Region_review(self):
        tested = Region()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Region_visible_in_documentation(self):
        tested = Region()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Region_visible_for_traceability(self):
        tested = Region()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Region_owned_constraints(self):
        tested = Region()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Region_constraints(self):
        tested = Region()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Region_owned_property_values(self):
        tested = Region()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Region_applied_property_values(self):
        tested = Region()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Region_owned_property_value_groups(self):
        tested = Region()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Region_applied_property_value_groups(self):
        tested = Region()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Region_owned_enumeration_property_types(self):
        tested = Region()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Region_owned_diagrams(self):
        tested = Region()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Region_element_of_interest_for_diagrams(self):
        tested = Region()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Region_contextual_element_for_diagrams(self):
        tested = Region()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Region_representing_diagrams(self):
        tested = Region()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Region_owned_states(self):
        tested = Region()
        value = Pseudostate()
        tested.get_owned_states().add(value)
        self.assertEqual(tested.get_owned_states().get(0), value)
        pass

    def test_StateTransition_id(self):
        tested = StateTransition()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_StateTransition_sid(self):
        tested = StateTransition()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_StateTransition_name(self):
        tested = StateTransition()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_StateTransition_summary(self):
        tested = StateTransition()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_StateTransition_description(self):
        tested = StateTransition()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_StateTransition_status(self):
        tested = StateTransition()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_StateTransition_review(self):
        tested = StateTransition()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_StateTransition_visible_in_documentation(self):
        tested = StateTransition()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_StateTransition_visible_for_traceability(self):
        tested = StateTransition()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_StateTransition_owned_constraints(self):
        tested = StateTransition()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_StateTransition_constraints(self):
        tested = StateTransition()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_StateTransition_owned_property_values(self):
        tested = StateTransition()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_StateTransition_applied_property_values(self):
        tested = StateTransition()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_StateTransition_owned_property_value_groups(self):
        tested = StateTransition()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_StateTransition_applied_property_value_groups(self):
        tested = StateTransition()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_StateTransition_owned_enumeration_property_types(self):
        tested = StateTransition()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_StateTransition_owned_diagrams(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_StateTransition_element_of_interest_for_diagrams(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_StateTransition_contextual_element_for_diagrams(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_StateTransition_representing_diagrams(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_StateTransition_trigger_description(self):
        tested = StateTransition()
        value = "value"
        tested.set_trigger_description(value)
        self.assertEqual(tested.get_trigger_description(), value)
        pass

    def test_StateTransition_source(self):
        tested = StateTransition()
        value = Pseudostate()
        tested.set_source(value)
        self.assertEqual(tested.get_source(), value)
        pass

    def test_StateTransition_target(self):
        tested = StateTransition()
        value = Pseudostate()
        tested.set_target(value)
        self.assertEqual(tested.get_target(), value)
        pass

    def test_StateTransition_triggers(self):
        tested = StateTransition()
        value = FunctionalExchange()
        tested.get_triggers().add(value)
        self.assertEqual(tested.get_triggers().get(0), value)
        pass

    def test_StateTransition_guard(self):
        tested = StateTransition()
        value = Constraint()
        tested.set_guard(value)
        self.assertEqual(tested.get_guard(), value)
        pass

    def test_StateTransition_effects(self):
        tested = StateTransition()
        value = ExchangeItem()
        tested.get_effects().add(value)
        self.assertEqual(tested.get_effects().get(0), value)
        pass

    def test_StateTransition_realized_state_transitions(self):
        tested = StateTransition()
        value = StateTransition()
        tested.get_realized_state_transitions()
        pass

    def test_StateTransition_realizing_state_transitions(self):
        tested = StateTransition()
        value = StateTransition()
        tested.get_realizing_state_transitions()
        pass

    def test_ChangeEvent_id(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ChangeEvent_sid(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ChangeEvent_name(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ChangeEvent_summary(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ChangeEvent_description(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ChangeEvent_status(self):
        tested = ChangeEvent()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ChangeEvent_review(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ChangeEvent_visible_in_documentation(self):
        tested = ChangeEvent()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ChangeEvent_visible_for_traceability(self):
        tested = ChangeEvent()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ChangeEvent_owned_constraints(self):
        tested = ChangeEvent()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ChangeEvent_constraints(self):
        tested = ChangeEvent()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ChangeEvent_owned_property_values(self):
        tested = ChangeEvent()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ChangeEvent_applied_property_values(self):
        tested = ChangeEvent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ChangeEvent_owned_property_value_groups(self):
        tested = ChangeEvent()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ChangeEvent_applied_property_value_groups(self):
        tested = ChangeEvent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ChangeEvent_owned_enumeration_property_types(self):
        tested = ChangeEvent()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ChangeEvent_owned_diagrams(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ChangeEvent_element_of_interest_for_diagrams(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ChangeEvent_contextual_element_for_diagrams(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ChangeEvent_representing_diagrams(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ChangeEvent_expression(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_expression(value)
        self.assertEqual(tested.get_expression(), value)
        pass

    def test_TimeEvent_id(self):
        tested = TimeEvent()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_TimeEvent_sid(self):
        tested = TimeEvent()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_TimeEvent_name(self):
        tested = TimeEvent()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_TimeEvent_summary(self):
        tested = TimeEvent()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_TimeEvent_description(self):
        tested = TimeEvent()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_TimeEvent_status(self):
        tested = TimeEvent()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_TimeEvent_review(self):
        tested = TimeEvent()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_TimeEvent_visible_in_documentation(self):
        tested = TimeEvent()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_TimeEvent_visible_for_traceability(self):
        tested = TimeEvent()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_TimeEvent_owned_constraints(self):
        tested = TimeEvent()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_TimeEvent_constraints(self):
        tested = TimeEvent()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_TimeEvent_owned_property_values(self):
        tested = TimeEvent()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_TimeEvent_applied_property_values(self):
        tested = TimeEvent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_TimeEvent_owned_property_value_groups(self):
        tested = TimeEvent()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_TimeEvent_applied_property_value_groups(self):
        tested = TimeEvent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_TimeEvent_owned_enumeration_property_types(self):
        tested = TimeEvent()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_TimeEvent_owned_diagrams(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_TimeEvent_element_of_interest_for_diagrams(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_TimeEvent_contextual_element_for_diagrams(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_TimeEvent_representing_diagrams(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_TimeEvent_kind(self):
        tested = TimeEvent()
        value = TimeEventKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_TimeEvent_expression(self):
        tested = TimeEvent()
        value = "value"
        tested.set_expression(value)
        self.assertEqual(tested.get_expression(), value)
        pass

    def test_Scenario_id(self):
        tested = Scenario()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Scenario_sid(self):
        tested = Scenario()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Scenario_name(self):
        tested = Scenario()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Scenario_summary(self):
        tested = Scenario()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Scenario_description(self):
        tested = Scenario()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Scenario_status(self):
        tested = Scenario()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Scenario_review(self):
        tested = Scenario()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Scenario_visible_in_documentation(self):
        tested = Scenario()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Scenario_visible_for_traceability(self):
        tested = Scenario()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Scenario_owned_constraints(self):
        tested = Scenario()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Scenario_constraints(self):
        tested = Scenario()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Scenario_owned_property_values(self):
        tested = Scenario()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Scenario_applied_property_values(self):
        tested = Scenario()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Scenario_owned_property_value_groups(self):
        tested = Scenario()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Scenario_applied_property_value_groups(self):
        tested = Scenario()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Scenario_owned_enumeration_property_types(self):
        tested = Scenario()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Scenario_owned_diagrams(self):
        tested = Scenario()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Scenario_element_of_interest_for_diagrams(self):
        tested = Scenario()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Scenario_contextual_element_for_diagrams(self):
        tested = Scenario()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Scenario_representing_diagrams(self):
        tested = Scenario()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Scenario_kind(self):
        tested = Scenario()
        value = ScenarioKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_Scenario_pre_condition(self):
        tested = Scenario()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_Scenario_post_condition(self):
        tested = Scenario()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_Scenario_owned_instance_roles(self):
        tested = Scenario()
        value = InstanceRole()
        tested.get_owned_instance_roles().add(value)
        self.assertEqual(tested.get_owned_instance_roles().get(0), value)
        pass

    def test_Scenario_owned_messages(self):
        tested = Scenario()
        value = SequenceMessage()
        tested.get_owned_messages().add(value)
        self.assertEqual(tested.get_owned_messages().get(0), value)
        pass

    def test_Scenario_owned_state_fragments(self):
        tested = Scenario()
        value = StateFragment()
        tested.get_owned_state_fragments().add(value)
        self.assertEqual(tested.get_owned_state_fragments().get(0), value)
        pass

    def test_Scenario_owned_combined_fragments(self):
        tested = Scenario()
        value = CombinedFragment()
        tested.get_owned_combined_fragments().add(value)
        self.assertEqual(tested.get_owned_combined_fragments().get(0), value)
        pass

    def test_Scenario_owned_constraint_durations(self):
        tested = Scenario()
        value = ConstraintDuration()
        tested.get_owned_constraint_durations().add(value)
        self.assertEqual(tested.get_owned_constraint_durations().get(0), value)
        pass

    def test_Scenario_referenced_scenarios(self):
        tested = Scenario()
        value = Scenario()
        tested.get_referenced_scenarios()
        pass

    def test_Scenario_realized_scenarios(self):
        tested = Scenario()
        value = Scenario()
        tested.get_realized_scenarios()
        pass

    def test_Scenario_realizing_scenarios(self):
        tested = Scenario()
        value = Scenario()
        tested.get_realizing_scenarios()
        pass

    def test_InstanceRole_id(self):
        tested = InstanceRole()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_InstanceRole_sid(self):
        tested = InstanceRole()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_InstanceRole_name(self):
        tested = InstanceRole()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_InstanceRole_summary(self):
        tested = InstanceRole()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_InstanceRole_description(self):
        tested = InstanceRole()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_InstanceRole_status(self):
        tested = InstanceRole()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_InstanceRole_review(self):
        tested = InstanceRole()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_InstanceRole_visible_in_documentation(self):
        tested = InstanceRole()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_InstanceRole_visible_for_traceability(self):
        tested = InstanceRole()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_InstanceRole_owned_constraints(self):
        tested = InstanceRole()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_InstanceRole_constraints(self):
        tested = InstanceRole()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_InstanceRole_owned_property_values(self):
        tested = InstanceRole()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_InstanceRole_applied_property_values(self):
        tested = InstanceRole()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_InstanceRole_owned_property_value_groups(self):
        tested = InstanceRole()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_InstanceRole_applied_property_value_groups(self):
        tested = InstanceRole()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_InstanceRole_owned_enumeration_property_types(self):
        tested = InstanceRole()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_InstanceRole_owned_diagrams(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_InstanceRole_element_of_interest_for_diagrams(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_InstanceRole_contextual_element_for_diagrams(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_InstanceRole_representing_diagrams(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_InstanceRole_represented_instance(self):
        tested = InstanceRole()
        value = ExchangeItem()
        tested.set_represented_instance(value)
        self.assertEqual(tested.get_represented_instance(), value)
        pass

    def test_SequenceMessage_id(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_SequenceMessage_sid(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_SequenceMessage_name(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_SequenceMessage_summary(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_SequenceMessage_description(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_SequenceMessage_status(self):
        tested = SequenceMessage()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_SequenceMessage_review(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_SequenceMessage_visible_in_documentation(self):
        tested = SequenceMessage()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_SequenceMessage_visible_for_traceability(self):
        tested = SequenceMessage()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_SequenceMessage_owned_constraints(self):
        tested = SequenceMessage()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_SequenceMessage_constraints(self):
        tested = SequenceMessage()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_SequenceMessage_owned_property_values(self):
        tested = SequenceMessage()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_SequenceMessage_applied_property_values(self):
        tested = SequenceMessage()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_SequenceMessage_owned_property_value_groups(self):
        tested = SequenceMessage()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_SequenceMessage_applied_property_value_groups(self):
        tested = SequenceMessage()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_SequenceMessage_owned_enumeration_property_types(self):
        tested = SequenceMessage()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_SequenceMessage_owned_diagrams(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_SequenceMessage_element_of_interest_for_diagrams(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_SequenceMessage_contextual_element_for_diagrams(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_SequenceMessage_representing_diagrams(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_SequenceMessage_kind(self):
        tested = SequenceMessage()
        value = MessageKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_SequenceMessage_sending_instance_role(self):
        tested = SequenceMessage()
        value = InstanceRole()
        tested.set_sending_instance_role(value)
        self.assertEqual(tested.get_sending_instance_role(), value)
        pass

    def test_SequenceMessage_receiving_instance_role(self):
        tested = SequenceMessage()
        value = InstanceRole()
        tested.set_receiving_instance_role(value)
        self.assertEqual(tested.get_receiving_instance_role(), value)
        pass

    def test_SequenceMessage_invoked_exchange(self):
        tested = SequenceMessage()
        value = ComponentExchange()
        tested.set_invoked_exchange(value)
        self.assertEqual(tested.get_invoked_exchange(), value)
        pass

    def test_SequenceMessage_exchanged_items(self):
        tested = SequenceMessage()
        value = ExchangeItem()
        tested.get_exchanged_items().add(value)
        self.assertEqual(tested.get_exchanged_items().get(0), value)
        pass

    def test_SequenceMessage_invoked_operation(self):
        tested = SequenceMessage()
        value = ExchangeItemAllocation()
        tested.set_invoked_operation(value)
        self.assertEqual(tested.get_invoked_operation(), value)
        pass

    def test_SequenceMessage_exchange_context(self):
        tested = SequenceMessage()
        value = Constraint()
        tested.set_exchange_context(value)
        self.assertEqual(tested.get_exchange_context(), value)
        pass

    def test_StateFragment_id(self):
        tested = StateFragment()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_StateFragment_sid(self):
        tested = StateFragment()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_StateFragment_name(self):
        tested = StateFragment()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_StateFragment_summary(self):
        tested = StateFragment()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_StateFragment_description(self):
        tested = StateFragment()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_StateFragment_status(self):
        tested = StateFragment()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_StateFragment_review(self):
        tested = StateFragment()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_StateFragment_visible_in_documentation(self):
        tested = StateFragment()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_StateFragment_visible_for_traceability(self):
        tested = StateFragment()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_StateFragment_owned_constraints(self):
        tested = StateFragment()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_StateFragment_constraints(self):
        tested = StateFragment()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_StateFragment_owned_property_values(self):
        tested = StateFragment()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_StateFragment_applied_property_values(self):
        tested = StateFragment()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_StateFragment_owned_property_value_groups(self):
        tested = StateFragment()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_StateFragment_applied_property_value_groups(self):
        tested = StateFragment()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_StateFragment_owned_enumeration_property_types(self):
        tested = StateFragment()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_StateFragment_owned_diagrams(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_StateFragment_element_of_interest_for_diagrams(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_StateFragment_contextual_element_for_diagrams(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_StateFragment_representing_diagrams(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_StateFragment_covered_instance_role(self):
        tested = StateFragment()
        value = InstanceRole()
        tested.set_covered_instance_role(value)
        self.assertEqual(tested.get_covered_instance_role(), value)
        pass

    def test_StateFragment_related_state(self):
        tested = StateFragment()
        value = State()
        tested.set_related_state(value)
        self.assertEqual(tested.get_related_state(), value)
        pass

    def test_StateFragment_related_activity_function(self):
        tested = StateFragment()
        value = PhysicalFunction()
        tested.set_related_activity_function(value)
        self.assertEqual(tested.get_related_activity_function(), value)
        pass

    def test_CombinedFragment_id(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CombinedFragment_sid(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_CombinedFragment_name(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CombinedFragment_summary(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_CombinedFragment_description(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_CombinedFragment_status(self):
        tested = CombinedFragment()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_CombinedFragment_review(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_CombinedFragment_visible_in_documentation(self):
        tested = CombinedFragment()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_CombinedFragment_visible_for_traceability(self):
        tested = CombinedFragment()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_CombinedFragment_owned_constraints(self):
        tested = CombinedFragment()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_CombinedFragment_constraints(self):
        tested = CombinedFragment()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_CombinedFragment_owned_property_values(self):
        tested = CombinedFragment()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_CombinedFragment_applied_property_values(self):
        tested = CombinedFragment()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_CombinedFragment_owned_property_value_groups(self):
        tested = CombinedFragment()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_CombinedFragment_applied_property_value_groups(self):
        tested = CombinedFragment()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_CombinedFragment_owned_enumeration_property_types(self):
        tested = CombinedFragment()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_CombinedFragment_owned_diagrams(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CombinedFragment_element_of_interest_for_diagrams(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CombinedFragment_contextual_element_for_diagrams(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CombinedFragment_representing_diagrams(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CombinedFragment_operator(self):
        tested = CombinedFragment()
        value = InteractionOperatorKind()
        tested.set_operator(value)
        self.assertEqual(tested.get_operator(), value)
        pass

    def test_CombinedFragment_operands(self):
        tested = CombinedFragment()
        value = Operand()
        tested.get_operands().add(value)
        self.assertEqual(tested.get_operands().get(0), value)
        pass

    def test_CombinedFragment_covered_instance_roles(self):
        tested = CombinedFragment()
        value = InstanceRole()
        tested.get_covered_instance_roles().add(value)
        self.assertEqual(tested.get_covered_instance_roles().get(0), value)
        pass

    def test_Operand_id(self):
        tested = Operand()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Operand_sid(self):
        tested = Operand()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Operand_name(self):
        tested = Operand()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Operand_summary(self):
        tested = Operand()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Operand_description(self):
        tested = Operand()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Operand_status(self):
        tested = Operand()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Operand_review(self):
        tested = Operand()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Operand_visible_in_documentation(self):
        tested = Operand()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Operand_visible_for_traceability(self):
        tested = Operand()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Operand_owned_constraints(self):
        tested = Operand()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Operand_constraints(self):
        tested = Operand()
        value = Constraint()
        tested.get_constraints().add(value)
        self.assertEqual(tested.get_constraints().get(0), value)
        pass

    def test_Operand_owned_property_values(self):
        tested = Operand()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Operand_applied_property_values(self):
        tested = Operand()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Operand_owned_property_value_groups(self):
        tested = Operand()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Operand_applied_property_value_groups(self):
        tested = Operand()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Operand_owned_enumeration_property_types(self):
        tested = Operand()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Operand_owned_diagrams(self):
        tested = Operand()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Operand_element_of_interest_for_diagrams(self):
        tested = Operand()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Operand_contextual_element_for_diagrams(self):
        tested = Operand()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Operand_representing_diagrams(self):
        tested = Operand()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Operand_guard(self):
        tested = Operand()
        value = Constraint()
        tested.set_guard(value)
        self.assertEqual(tested.get_guard(), value)
        pass

    def test_Operand_referenced_messages(self):
        tested = Operand()
        value = SequenceMessage()
        tested.get_referenced_messages().add(value)
        self.assertEqual(tested.get_referenced_messages().get(0), value)
        pass

    def test_Operand_referenced_fragments(self):
        tested = Operand()
        value = StateFragment()
        tested.get_referenced_fragments().add(value)
        self.assertEqual(tested.get_referenced_fragments().get(0), value)
        pass

    def test_ConstraintDuration_id(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ConstraintDuration_sid(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ConstraintDuration_name(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ConstraintDuration_summary(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ConstraintDuration_description(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ConstraintDuration_status(self):
        tested = ConstraintDuration()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ConstraintDuration_review(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ConstraintDuration_visible_in_documentation(self):
        tested = ConstraintDuration()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ConstraintDuration_visible_for_traceability(self):
        tested = ConstraintDuration()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ConstraintDuration_owned_constraints(self):
        tested = ConstraintDuration()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ConstraintDuration_constraints(self):
        tested = ConstraintDuration()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ConstraintDuration_owned_property_values(self):
        tested = ConstraintDuration()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ConstraintDuration_applied_property_values(self):
        tested = ConstraintDuration()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ConstraintDuration_owned_property_value_groups(self):
        tested = ConstraintDuration()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ConstraintDuration_applied_property_value_groups(self):
        tested = ConstraintDuration()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ConstraintDuration_owned_enumeration_property_types(self):
        tested = ConstraintDuration()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ConstraintDuration_owned_diagrams(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ConstraintDuration_element_of_interest_for_diagrams(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ConstraintDuration_contextual_element_for_diagrams(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ConstraintDuration_representing_diagrams(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ConstraintDuration_duration(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_duration(value)
        self.assertEqual(tested.get_duration(), value)
        pass

    def test_PhysicalPort_allocator_configuration_items(self):
        tested = PhysicalPort()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        self.assertEqual(tested.get_allocator_configuration_items().get(0), value)
        pass

    def test_PhysicalPort_id(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalPort_sid(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalPort_name(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalPort_summary(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalPort_description(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalPort_status(self):
        tested = PhysicalPort()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalPort_review(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalPort_visible_in_documentation(self):
        tested = PhysicalPort()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalPort_visible_for_traceability(self):
        tested = PhysicalPort()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalPort_owned_constraints(self):
        tested = PhysicalPort()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalPort_constraints(self):
        tested = PhysicalPort()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalPort_owned_property_values(self):
        tested = PhysicalPort()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalPort_applied_property_values(self):
        tested = PhysicalPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalPort_owned_property_value_groups(self):
        tested = PhysicalPort()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalPort_applied_property_value_groups(self):
        tested = PhysicalPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalPort_owned_enumeration_property_types(self):
        tested = PhysicalPort()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalPort_owned_diagrams(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalPort_element_of_interest_for_diagrams(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalPort_contextual_element_for_diagrams(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalPort_representing_diagrams(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalPort_physical_links(self):
        tested = PhysicalPort()
        value = PhysicalLink()
        tested.get_physical_links()
        pass

    def test_PhysicalPort_allocated_component_ports(self):
        tested = PhysicalPort()
        value = ComponentPort()
        tested.get_allocated_component_ports()
        pass

    def test_PhysicalPort_realized_physical_ports(self):
        tested = PhysicalPort()
        value = PhysicalPort()
        tested.get_realized_physical_ports()
        pass

    def test_PhysicalPort_realizing_physical_ports(self):
        tested = PhysicalPort()
        value = PhysicalPort()
        tested.get_realizing_physical_ports()
        pass

    def test_PhysicalLink_allocator_configuration_items(self):
        tested = PhysicalLink()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        self.assertEqual(tested.get_allocator_configuration_items().get(0), value)
        pass

    def test_PhysicalLink_id(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalLink_sid(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalLink_name(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalLink_summary(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalLink_description(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalLink_status(self):
        tested = PhysicalLink()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalLink_review(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalLink_visible_in_documentation(self):
        tested = PhysicalLink()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalLink_visible_for_traceability(self):
        tested = PhysicalLink()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalLink_owned_constraints(self):
        tested = PhysicalLink()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalLink_constraints(self):
        tested = PhysicalLink()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalLink_owned_property_values(self):
        tested = PhysicalLink()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalLink_applied_property_values(self):
        tested = PhysicalLink()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalLink_owned_property_value_groups(self):
        tested = PhysicalLink()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalLink_applied_property_value_groups(self):
        tested = PhysicalLink()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalLink_owned_enumeration_property_types(self):
        tested = PhysicalLink()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalLink_owned_diagrams(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalLink_element_of_interest_for_diagrams(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalLink_contextual_element_for_diagrams(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalLink_representing_diagrams(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalLink_connected_physical_ports(self):
        tested = PhysicalLink()
        value = PhysicalPort()
        tested.get_connected_physical_ports().add(value)
        self.assertEqual(tested.get_connected_physical_ports().get(0), value)
        pass

    def test_PhysicalLink_categories(self):
        tested = PhysicalLink()
        value = PhysicalLinkCategory()
        tested.get_categories()
        pass

    def test_PhysicalLink_involving_physical_paths(self):
        tested = PhysicalLink()
        value = PhysicalPath()
        tested.get_involving_physical_paths().add(value)
        self.assertEqual(tested.get_involving_physical_paths().get(0), value)
        pass

    def test_PhysicalLink_connected_components(self):
        tested = PhysicalLink()
        value = PhysicalActor()
        tested.get_connected_components().add(value)
        self.assertEqual(tested.get_connected_components().get(0), value)
        pass

    def test_PhysicalLink_allocated_component_exchanges(self):
        tested = PhysicalLink()
        value = ComponentExchange()
        tested.get_allocated_component_exchanges()
        pass

    def test_PhysicalLink_realized_physical_links(self):
        tested = PhysicalLink()
        value = PhysicalLink()
        tested.get_realized_physical_links()
        pass

    def test_PhysicalLink_realizing_physical_links(self):
        tested = PhysicalLink()
        value = PhysicalLink()
        tested.get_realizing_physical_links()
        pass

    def test_PhysicalLinkCategory_id(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalLinkCategory_sid(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalLinkCategory_name(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalLinkCategory_summary(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalLinkCategory_description(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalLinkCategory_status(self):
        tested = PhysicalLinkCategory()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalLinkCategory_review(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalLinkCategory_visible_in_documentation(self):
        tested = PhysicalLinkCategory()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalLinkCategory_visible_for_traceability(self):
        tested = PhysicalLinkCategory()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalLinkCategory_owned_constraints(self):
        tested = PhysicalLinkCategory()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalLinkCategory_constraints(self):
        tested = PhysicalLinkCategory()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalLinkCategory_owned_property_values(self):
        tested = PhysicalLinkCategory()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalLinkCategory_applied_property_values(self):
        tested = PhysicalLinkCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalLinkCategory_owned_property_value_groups(self):
        tested = PhysicalLinkCategory()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalLinkCategory_applied_property_value_groups(self):
        tested = PhysicalLinkCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalLinkCategory_owned_enumeration_property_types(self):
        tested = PhysicalLinkCategory()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalLinkCategory_owned_diagrams(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalLinkCategory_element_of_interest_for_diagrams(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalLinkCategory_contextual_element_for_diagrams(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalLinkCategory_representing_diagrams(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalLinkCategory_links(self):
        tested = PhysicalLinkCategory()
        value = PhysicalLink()
        tested.get_links().add(value)
        self.assertEqual(tested.get_links().get(0), value)
        pass

    def test_PhysicalPath_id(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_PhysicalPath_sid(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_PhysicalPath_name(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_PhysicalPath_summary(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_PhysicalPath_description(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_PhysicalPath_status(self):
        tested = PhysicalPath()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_PhysicalPath_review(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_PhysicalPath_visible_in_documentation(self):
        tested = PhysicalPath()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_PhysicalPath_visible_for_traceability(self):
        tested = PhysicalPath()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_PhysicalPath_owned_constraints(self):
        tested = PhysicalPath()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_PhysicalPath_constraints(self):
        tested = PhysicalPath()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_PhysicalPath_owned_property_values(self):
        tested = PhysicalPath()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_PhysicalPath_applied_property_values(self):
        tested = PhysicalPath()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_PhysicalPath_owned_property_value_groups(self):
        tested = PhysicalPath()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_PhysicalPath_applied_property_value_groups(self):
        tested = PhysicalPath()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_PhysicalPath_owned_enumeration_property_types(self):
        tested = PhysicalPath()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_PhysicalPath_owned_diagrams(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_PhysicalPath_element_of_interest_for_diagrams(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_PhysicalPath_contextual_element_for_diagrams(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_PhysicalPath_representing_diagrams(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_PhysicalPath_involved_physical_links(self):
        tested = PhysicalPath()
        value = PhysicalLink()
        tested.get_involved_physical_links()
        pass

    def test_PhysicalPath_involved_node_p_cs(self):
        tested = PhysicalPath()
        value = PhysicalActor()
        tested.get_involved_node_p_cs().add(value)
        self.assertEqual(tested.get_involved_node_p_cs().get(0), value)
        pass

    def test_PhysicalPath_allocated_component_exchanges(self):
        tested = PhysicalPath()
        value = ComponentExchange()
        tested.get_allocated_component_exchanges()
        pass

    def test_PhysicalPath_realized_physical_paths(self):
        tested = PhysicalPath()
        value = PhysicalPath()
        tested.get_realized_physical_paths().add(value)
        self.assertEqual(tested.get_realized_physical_paths().get(0), value)
        pass

    def test_PhysicalPath_realizing_physical_paths(self):
        tested = PhysicalPath()
        value = PhysicalPath()
        tested.get_realizing_physical_paths().add(value)
        self.assertEqual(tested.get_realizing_physical_paths().get(0), value)
        pass

    def test_InterfacePkg_owned_property_value_pkgs(self):
        tested = InterfacePkg()
        value = PropertyValuePkg()
        tested.get_owned_property_value_pkgs().add(value)
        self.assertEqual(tested.get_owned_property_value_pkgs().get(0), value)
        pass

    def test_InterfacePkg_id(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_InterfacePkg_sid(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_InterfacePkg_name(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_InterfacePkg_summary(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_InterfacePkg_description(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_InterfacePkg_status(self):
        tested = InterfacePkg()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_InterfacePkg_review(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_InterfacePkg_visible_in_documentation(self):
        tested = InterfacePkg()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_InterfacePkg_visible_for_traceability(self):
        tested = InterfacePkg()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_InterfacePkg_owned_constraints(self):
        tested = InterfacePkg()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_InterfacePkg_constraints(self):
        tested = InterfacePkg()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_InterfacePkg_owned_property_values(self):
        tested = InterfacePkg()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_InterfacePkg_applied_property_values(self):
        tested = InterfacePkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_InterfacePkg_owned_property_value_groups(self):
        tested = InterfacePkg()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_InterfacePkg_applied_property_value_groups(self):
        tested = InterfacePkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_InterfacePkg_owned_enumeration_property_types(self):
        tested = InterfacePkg()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_InterfacePkg_owned_diagrams(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_InterfacePkg_element_of_interest_for_diagrams(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_InterfacePkg_contextual_element_for_diagrams(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_InterfacePkg_representing_diagrams(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_InterfacePkg_owned_interface_pkgs(self):
        tested = InterfacePkg()
        value = InterfacePkg()
        tested.get_owned_interface_pkgs().add(value)
        self.assertEqual(tested.get_owned_interface_pkgs().get(0), value)
        pass

    def test_InterfacePkg_owned_interfaces(self):
        tested = InterfacePkg()
        value = Interface()
        tested.get_owned_interfaces().add(value)
        self.assertEqual(tested.get_owned_interfaces().get(0), value)
        pass

    def test_InterfacePkg_owned_exchange_items(self):
        tested = InterfacePkg()
        value = ExchangeItem()
        tested.get_owned_exchange_items().add(value)
        self.assertEqual(tested.get_owned_exchange_items().get(0), value)
        pass

    def test_Interface_id(self):
        tested = Interface()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Interface_sid(self):
        tested = Interface()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_Interface_name(self):
        tested = Interface()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Interface_summary(self):
        tested = Interface()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_Interface_description(self):
        tested = Interface()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_Interface_status(self):
        tested = Interface()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_Interface_review(self):
        tested = Interface()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_Interface_visible_in_documentation(self):
        tested = Interface()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_Interface_visible_for_traceability(self):
        tested = Interface()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_Interface_owned_constraints(self):
        tested = Interface()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_Interface_constraints(self):
        tested = Interface()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_Interface_owned_property_values(self):
        tested = Interface()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_Interface_applied_property_values(self):
        tested = Interface()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_Interface_owned_property_value_groups(self):
        tested = Interface()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_Interface_applied_property_value_groups(self):
        tested = Interface()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_Interface_owned_enumeration_property_types(self):
        tested = Interface()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_Interface_owned_diagrams(self):
        tested = Interface()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Interface_element_of_interest_for_diagrams(self):
        tested = Interface()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Interface_contextual_element_for_diagrams(self):
        tested = Interface()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Interface_representing_diagrams(self):
        tested = Interface()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Interface_visibility(self):
        tested = Interface()
        value = VisibilityKind()
        tested.set_visibility(value)
        self.assertEqual(tested.get_visibility(), value)
        pass

    def test_Interface_owned_exchange_item_allocations(self):
        tested = Interface()
        value = ExchangeItemAllocation()
        tested.get_owned_exchange_item_allocations().add(value)
        self.assertEqual(tested.get_owned_exchange_item_allocations().get(0), value)
        pass

    def test_Interface_exchange_items(self):
        tested = Interface()
        value = ExchangeItem()
        tested.get_exchange_items()
        pass

    def test_Interface_providing_component_ports(self):
        tested = Interface()
        value = ComponentPort()
        tested.get_providing_component_ports()
        pass

    def test_Interface_requiring_component_ports(self):
        tested = Interface()
        value = ComponentPort()
        tested.get_requiring_component_ports()
        pass

    def test_Interface_user_components(self):
        tested = Interface()
        value = PhysicalActor()
        tested.get_user_components().add(value)
        self.assertEqual(tested.get_user_components().get(0), value)
        pass

    def test_Interface_implementor_components(self):
        tested = Interface()
        value = PhysicalActor()
        tested.get_implementor_components().add(value)
        self.assertEqual(tested.get_implementor_components().get(0), value)
        pass

    def test_Interface_super(self):
        tested = Interface()
        value = Interface()
        tested.get_super()
        pass

    def test_Interface_sub(self):
        tested = Interface()
        value = Interface()
        tested.get_sub()
        pass

    def test_ExchangeItemAllocation_id(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ExchangeItemAllocation_sid(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ExchangeItemAllocation_name(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ExchangeItemAllocation_summary(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ExchangeItemAllocation_description(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ExchangeItemAllocation_status(self):
        tested = ExchangeItemAllocation()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ExchangeItemAllocation_review(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ExchangeItemAllocation_visible_in_documentation(self):
        tested = ExchangeItemAllocation()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ExchangeItemAllocation_visible_for_traceability(self):
        tested = ExchangeItemAllocation()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ExchangeItemAllocation_owned_constraints(self):
        tested = ExchangeItemAllocation()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ExchangeItemAllocation_constraints(self):
        tested = ExchangeItemAllocation()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ExchangeItemAllocation_owned_property_values(self):
        tested = ExchangeItemAllocation()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ExchangeItemAllocation_applied_property_values(self):
        tested = ExchangeItemAllocation()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ExchangeItemAllocation_owned_property_value_groups(self):
        tested = ExchangeItemAllocation()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ExchangeItemAllocation_applied_property_value_groups(self):
        tested = ExchangeItemAllocation()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ExchangeItemAllocation_owned_enumeration_property_types(self):
        tested = ExchangeItemAllocation()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ExchangeItemAllocation_owned_diagrams(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ExchangeItemAllocation_element_of_interest_for_diagrams(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ExchangeItemAllocation_contextual_element_for_diagrams(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ExchangeItemAllocation_representing_diagrams(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ExchangeItemAllocation_transmission_protocol(self):
        tested = ExchangeItemAllocation()
        value = CommunicationLinkProtocol()
        tested.set_transmission_protocol(value)
        self.assertEqual(tested.get_transmission_protocol(), value)
        pass

    def test_ExchangeItemAllocation_acquisition_protocol(self):
        tested = ExchangeItemAllocation()
        value = CommunicationLinkProtocol()
        tested.set_acquisition_protocol(value)
        self.assertEqual(tested.get_acquisition_protocol(), value)
        pass

    def test_ExchangeItemAllocation_allocated_item(self):
        tested = ExchangeItemAllocation()
        value = ExchangeItem()
        tested.set_allocated_item(value)
        self.assertEqual(tested.get_allocated_item(), value)
        pass

    def test_ExchangeItemAllocation_invoking_sequence_messages(self):
        tested = ExchangeItemAllocation()
        value = SequenceMessage()
        tested.get_invoking_sequence_messages().add(value)
        self.assertEqual(tested.get_invoking_sequence_messages().get(0), value)
        pass

    def test_ExchangeItem_id(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ExchangeItem_sid(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ExchangeItem_name(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ExchangeItem_summary(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ExchangeItem_description(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ExchangeItem_status(self):
        tested = ExchangeItem()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ExchangeItem_review(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ExchangeItem_visible_in_documentation(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ExchangeItem_visible_for_traceability(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ExchangeItem_owned_constraints(self):
        tested = ExchangeItem()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ExchangeItem_constraints(self):
        tested = ExchangeItem()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ExchangeItem_owned_property_values(self):
        tested = ExchangeItem()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ExchangeItem_applied_property_values(self):
        tested = ExchangeItem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ExchangeItem_owned_property_value_groups(self):
        tested = ExchangeItem()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ExchangeItem_applied_property_value_groups(self):
        tested = ExchangeItem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ExchangeItem_owned_enumeration_property_types(self):
        tested = ExchangeItem()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ExchangeItem_owned_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ExchangeItem_element_of_interest_for_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ExchangeItem_contextual_element_for_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ExchangeItem_representing_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ExchangeItem_id(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ExchangeItem_sid(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ExchangeItem_name(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ExchangeItem_summary(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ExchangeItem_description(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ExchangeItem_status(self):
        tested = ExchangeItem()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ExchangeItem_review(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ExchangeItem_visible_in_documentation(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ExchangeItem_visible_for_traceability(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ExchangeItem_owned_constraints(self):
        tested = ExchangeItem()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ExchangeItem_constraints(self):
        tested = ExchangeItem()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ExchangeItem_owned_property_values(self):
        tested = ExchangeItem()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ExchangeItem_applied_property_values(self):
        tested = ExchangeItem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ExchangeItem_owned_property_value_groups(self):
        tested = ExchangeItem()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ExchangeItem_applied_property_value_groups(self):
        tested = ExchangeItem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ExchangeItem_owned_enumeration_property_types(self):
        tested = ExchangeItem()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ExchangeItem_owned_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ExchangeItem_element_of_interest_for_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ExchangeItem_contextual_element_for_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ExchangeItem_representing_diagrams(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ExchangeItem_abstract(self):
        tested = ExchangeItem()
        value = True
        tested.set_abstract(value)
        self.assertEqual(tested.get_abstract(), value)
        pass

    def test_ExchangeItem_final(self):
        tested = ExchangeItem()
        value = True
        tested.set_final(value)
        self.assertEqual(tested.get_final(), value)
        pass

    def test_ExchangeItem_exchange_mechanism(self):
        tested = ExchangeItem()
        value = ExchangeMechanism()
        tested.set_exchange_mechanism(value)
        self.assertEqual(tested.get_exchange_mechanism(), value)
        pass

    def test_ExchangeItem_owned_elements(self):
        tested = ExchangeItem()
        value = ExchangeItemElement()
        tested.get_owned_elements().add(value)
        self.assertEqual(tested.get_owned_elements().get(0), value)
        pass

    def test_ExchangeItem_allocator_interfaces(self):
        tested = ExchangeItem()
        value = Interface()
        tested.get_allocator_interfaces()
        pass

    def test_ExchangeItem_super(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_super()
        pass

    def test_ExchangeItem_sub(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_sub()
        pass

    def test_ExchangeItem_realized_exchange_items(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_realized_exchange_items()
        pass

    def test_ExchangeItem_realizing_exchange_items(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_realizing_exchange_items()
        pass

    def test_ExchangeItemElement_id(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ExchangeItemElement_sid(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ExchangeItemElement_name(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ExchangeItemElement_summary(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ExchangeItemElement_description(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ExchangeItemElement_status(self):
        tested = ExchangeItemElement()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ExchangeItemElement_review(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ExchangeItemElement_visible_in_documentation(self):
        tested = ExchangeItemElement()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ExchangeItemElement_visible_for_traceability(self):
        tested = ExchangeItemElement()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ExchangeItemElement_owned_constraints(self):
        tested = ExchangeItemElement()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ExchangeItemElement_constraints(self):
        tested = ExchangeItemElement()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ExchangeItemElement_owned_property_values(self):
        tested = ExchangeItemElement()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ExchangeItemElement_applied_property_values(self):
        tested = ExchangeItemElement()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ExchangeItemElement_owned_property_value_groups(self):
        tested = ExchangeItemElement()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ExchangeItemElement_applied_property_value_groups(self):
        tested = ExchangeItemElement()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ExchangeItemElement_owned_enumeration_property_types(self):
        tested = ExchangeItemElement()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ExchangeItemElement_owned_diagrams(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ExchangeItemElement_element_of_interest_for_diagrams(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ExchangeItemElement_contextual_element_for_diagrams(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ExchangeItemElement_representing_diagrams(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_FunctionInputPort_allocator_component_port(self):
        tested = FunctionInputPort()
        value = ComponentPort()
        tested.set_allocator_component_port(value)
        self.assertEqual(tested.get_allocator_component_port(), value)
        pass

    def test_FunctionInputPort_id(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_FunctionInputPort_sid(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_FunctionInputPort_name(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_FunctionInputPort_summary(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_FunctionInputPort_description(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_FunctionInputPort_status(self):
        tested = FunctionInputPort()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_FunctionInputPort_review(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_FunctionInputPort_visible_in_documentation(self):
        tested = FunctionInputPort()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_FunctionInputPort_visible_for_traceability(self):
        tested = FunctionInputPort()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_FunctionInputPort_owned_constraints(self):
        tested = FunctionInputPort()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_FunctionInputPort_constraints(self):
        tested = FunctionInputPort()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_FunctionInputPort_owned_property_values(self):
        tested = FunctionInputPort()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_FunctionInputPort_applied_property_values(self):
        tested = FunctionInputPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_FunctionInputPort_owned_property_value_groups(self):
        tested = FunctionInputPort()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_FunctionInputPort_applied_property_value_groups(self):
        tested = FunctionInputPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_FunctionInputPort_owned_enumeration_property_types(self):
        tested = FunctionInputPort()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_FunctionInputPort_owned_diagrams(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_FunctionInputPort_element_of_interest_for_diagrams(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_FunctionInputPort_contextual_element_for_diagrams(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_FunctionInputPort_representing_diagrams(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_FunctionInputPort_incoming_functional_exchanges(self):
        tested = FunctionInputPort()
        value = FunctionalExchange()
        tested.get_incoming_functional_exchanges()
        pass

    def test_FunctionInputPort_incoming_exchange_items(self):
        tested = FunctionInputPort()
        value = ExchangeItem()
        tested.get_incoming_exchange_items().add(value)
        self.assertEqual(tested.get_incoming_exchange_items().get(0), value)
        pass

    def test_FunctionInputPort_realized_function_input_ports(self):
        tested = FunctionInputPort()
        value = FunctionInputPort()
        tested.get_realized_function_input_ports().add(value)
        self.assertEqual(tested.get_realized_function_input_ports().get(0), value)
        pass

    def test_FunctionInputPort_realizing_function_input_ports(self):
        tested = FunctionInputPort()
        value = FunctionInputPort()
        tested.get_realizing_function_input_ports().add(value)
        self.assertEqual(tested.get_realizing_function_input_ports().get(0), value)
        pass

    def test_FunctionOutputPort_allocator_component_port(self):
        tested = FunctionOutputPort()
        value = ComponentPort()
        tested.set_allocator_component_port(value)
        self.assertEqual(tested.get_allocator_component_port(), value)
        pass

    def test_FunctionOutputPort_id(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_FunctionOutputPort_sid(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_FunctionOutputPort_name(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_FunctionOutputPort_summary(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_FunctionOutputPort_description(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_FunctionOutputPort_status(self):
        tested = FunctionOutputPort()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_FunctionOutputPort_review(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_FunctionOutputPort_visible_in_documentation(self):
        tested = FunctionOutputPort()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_FunctionOutputPort_visible_for_traceability(self):
        tested = FunctionOutputPort()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_FunctionOutputPort_owned_constraints(self):
        tested = FunctionOutputPort()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_FunctionOutputPort_constraints(self):
        tested = FunctionOutputPort()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_FunctionOutputPort_owned_property_values(self):
        tested = FunctionOutputPort()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_FunctionOutputPort_applied_property_values(self):
        tested = FunctionOutputPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_FunctionOutputPort_owned_property_value_groups(self):
        tested = FunctionOutputPort()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_FunctionOutputPort_applied_property_value_groups(self):
        tested = FunctionOutputPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_FunctionOutputPort_owned_enumeration_property_types(self):
        tested = FunctionOutputPort()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_FunctionOutputPort_owned_diagrams(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_FunctionOutputPort_element_of_interest_for_diagrams(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_FunctionOutputPort_contextual_element_for_diagrams(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_FunctionOutputPort_representing_diagrams(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_FunctionOutputPort_outgoing_functional_exchanges(self):
        tested = FunctionOutputPort()
        value = FunctionalExchange()
        tested.get_outgoing_functional_exchanges()
        pass

    def test_FunctionOutputPort_outgoing_exchange_items(self):
        tested = FunctionOutputPort()
        value = ExchangeItem()
        tested.get_outgoing_exchange_items().add(value)
        self.assertEqual(tested.get_outgoing_exchange_items().get(0), value)
        pass

    def test_FunctionOutputPort_realized_function_output_ports(self):
        tested = FunctionOutputPort()
        value = FunctionOutputPort()
        tested.get_realized_function_output_ports().add(value)
        self.assertEqual(tested.get_realized_function_output_ports().get(0), value)
        pass

    def test_FunctionOutputPort_realizing_function_output_ports(self):
        tested = FunctionOutputPort()
        value = FunctionOutputPort()
        tested.get_realizing_function_output_ports().add(value)
        self.assertEqual(tested.get_realizing_function_output_ports().get(0), value)
        pass

    def test_FunctionalExchange_id(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_FunctionalExchange_sid(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_FunctionalExchange_name(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_FunctionalExchange_summary(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_FunctionalExchange_description(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_FunctionalExchange_status(self):
        tested = FunctionalExchange()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_FunctionalExchange_review(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_FunctionalExchange_visible_in_documentation(self):
        tested = FunctionalExchange()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_FunctionalExchange_visible_for_traceability(self):
        tested = FunctionalExchange()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_FunctionalExchange_owned_constraints(self):
        tested = FunctionalExchange()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_FunctionalExchange_constraints(self):
        tested = FunctionalExchange()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_FunctionalExchange_owned_property_values(self):
        tested = FunctionalExchange()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_FunctionalExchange_applied_property_values(self):
        tested = FunctionalExchange()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_FunctionalExchange_owned_property_value_groups(self):
        tested = FunctionalExchange()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_FunctionalExchange_applied_property_value_groups(self):
        tested = FunctionalExchange()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_FunctionalExchange_owned_enumeration_property_types(self):
        tested = FunctionalExchange()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_FunctionalExchange_owned_diagrams(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_FunctionalExchange_element_of_interest_for_diagrams(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_FunctionalExchange_contextual_element_for_diagrams(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_FunctionalExchange_representing_diagrams(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_FunctionalExchange_invoking_sequence_messages(self):
        tested = FunctionalExchange()
        value = SequenceMessage()
        tested.get_invoking_sequence_messages().add(value)
        self.assertEqual(tested.get_invoking_sequence_messages().get(0), value)
        pass

    def test_FunctionalExchange_source(self):
        tested = FunctionalExchange()
        value = FunctionOutputPort()
        tested.set_source(value)
        self.assertEqual(tested.get_source(), value)
        pass

    def test_FunctionalExchange_target(self):
        tested = FunctionalExchange()
        value = FunctionInputPort()
        tested.set_target(value)
        self.assertEqual(tested.get_target(), value)
        pass

    def test_FunctionalExchange_exchanged_items(self):
        tested = FunctionalExchange()
        value = ExchangeItem()
        tested.get_exchanged_items().add(value)
        self.assertEqual(tested.get_exchanged_items().get(0), value)
        pass

    def test_FunctionalExchange_involving_functional_chains(self):
        tested = FunctionalExchange()
        value = FunctionalChain()
        tested.get_involving_functional_chains()
        pass

    def test_FunctionalExchange_categories(self):
        tested = FunctionalExchange()
        value = ExchangeCategory()
        tested.get_categories()
        pass

    def test_FunctionalExchange_allocating_component_exchange(self):
        tested = FunctionalExchange()
        value = ComponentExchange()
        tested.set_allocating_component_exchange(value)
        self.assertEqual(tested.get_allocating_component_exchange(), value)
        pass

    def test_FunctionalExchange_realized_functional_exchanges(self):
        tested = FunctionalExchange()
        value = FunctionalExchange()
        tested.get_realized_functional_exchanges()
        pass

    def test_FunctionalExchange_realizing_functional_exchanges(self):
        tested = FunctionalExchange()
        value = FunctionalExchange()
        tested.get_realizing_functional_exchanges()
        pass

    def test_FunctionalExchange_realized_interactions(self):
        tested = FunctionalExchange()
        value = Interaction()
        tested.get_realized_interactions()
        pass

    def test_ExchangeCategory_id(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ExchangeCategory_sid(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ExchangeCategory_name(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ExchangeCategory_summary(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ExchangeCategory_description(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ExchangeCategory_status(self):
        tested = ExchangeCategory()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ExchangeCategory_review(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ExchangeCategory_visible_in_documentation(self):
        tested = ExchangeCategory()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ExchangeCategory_visible_for_traceability(self):
        tested = ExchangeCategory()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ExchangeCategory_owned_constraints(self):
        tested = ExchangeCategory()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ExchangeCategory_constraints(self):
        tested = ExchangeCategory()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ExchangeCategory_owned_property_values(self):
        tested = ExchangeCategory()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ExchangeCategory_applied_property_values(self):
        tested = ExchangeCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ExchangeCategory_owned_property_value_groups(self):
        tested = ExchangeCategory()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ExchangeCategory_applied_property_value_groups(self):
        tested = ExchangeCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ExchangeCategory_owned_enumeration_property_types(self):
        tested = ExchangeCategory()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ExchangeCategory_owned_diagrams(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ExchangeCategory_element_of_interest_for_diagrams(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ExchangeCategory_contextual_element_for_diagrams(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ExchangeCategory_representing_diagrams(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ExchangeCategory_exchanges(self):
        tested = ExchangeCategory()
        value = FunctionalExchange()
        tested.get_exchanges().add(value)
        self.assertEqual(tested.get_exchanges().get(0), value)
        pass

    def test_FunctionalChain_id(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_FunctionalChain_sid(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_FunctionalChain_name(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_FunctionalChain_summary(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_FunctionalChain_description(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_FunctionalChain_status(self):
        tested = FunctionalChain()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_FunctionalChain_review(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_FunctionalChain_visible_in_documentation(self):
        tested = FunctionalChain()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_FunctionalChain_visible_for_traceability(self):
        tested = FunctionalChain()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_FunctionalChain_owned_constraints(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_FunctionalChain_constraints(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_FunctionalChain_owned_property_values(self):
        tested = FunctionalChain()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_FunctionalChain_applied_property_values(self):
        tested = FunctionalChain()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_FunctionalChain_owned_property_value_groups(self):
        tested = FunctionalChain()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_FunctionalChain_applied_property_value_groups(self):
        tested = FunctionalChain()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_FunctionalChain_owned_enumeration_property_types(self):
        tested = FunctionalChain()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_FunctionalChain_owned_diagrams(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_FunctionalChain_element_of_interest_for_diagrams(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_FunctionalChain_contextual_element_for_diagrams(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_FunctionalChain_representing_diagrams(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_FunctionalChain_pre_condition(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.set_pre_condition(value)
        self.assertEqual(tested.get_pre_condition(), value)
        pass

    def test_FunctionalChain_post_condition(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.set_post_condition(value)
        self.assertEqual(tested.get_post_condition(), value)
        pass

    def test_FunctionalChain_involved_functions(self):
        tested = FunctionalChain()
        value = PhysicalFunction()
        tested.get_involved_functions()
        pass

    def test_FunctionalChain_involved_functional_exchanges(self):
        tested = FunctionalChain()
        value = FunctionalExchange()
        tested.get_involved_functional_exchanges()
        pass

    def test_FunctionalChain_involved_functional_chains(self):
        tested = FunctionalChain()
        value = FunctionalChain()
        tested.get_involved_functional_chains()
        pass

    def test_FunctionalChain_involving_capabilities(self):
        tested = FunctionalChain()
        value = CapabilityRealization()
        tested.get_involving_capabilities()
        pass

    def test_FunctionalChain_available_in_states(self):
        tested = FunctionalChain()
        value = State()
        tested.get_available_in_states().add(value)
        self.assertEqual(tested.get_available_in_states().get(0), value)
        pass

    def test_FunctionalChain_realized_operational_processes(self):
        tested = FunctionalChain()
        value = OperationalProcess()
        tested.get_realized_operational_processes()
        pass

    def test_FunctionalChain_realized_functional_chains(self):
        tested = FunctionalChain()
        value = FunctionalChain()
        tested.get_realized_functional_chains()
        pass

    def test_FunctionalChain_realizing_functional_chains(self):
        tested = FunctionalChain()
        value = FunctionalChain()
        tested.get_realizing_functional_chains()
        pass

    def test_ComponentPort_id(self):
        tested = ComponentPort()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ComponentPort_sid(self):
        tested = ComponentPort()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ComponentPort_name(self):
        tested = ComponentPort()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ComponentPort_summary(self):
        tested = ComponentPort()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ComponentPort_description(self):
        tested = ComponentPort()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ComponentPort_status(self):
        tested = ComponentPort()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ComponentPort_review(self):
        tested = ComponentPort()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ComponentPort_visible_in_documentation(self):
        tested = ComponentPort()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ComponentPort_visible_for_traceability(self):
        tested = ComponentPort()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ComponentPort_owned_constraints(self):
        tested = ComponentPort()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ComponentPort_constraints(self):
        tested = ComponentPort()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ComponentPort_owned_property_values(self):
        tested = ComponentPort()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ComponentPort_applied_property_values(self):
        tested = ComponentPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ComponentPort_owned_property_value_groups(self):
        tested = ComponentPort()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ComponentPort_applied_property_value_groups(self):
        tested = ComponentPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ComponentPort_owned_enumeration_property_types(self):
        tested = ComponentPort()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ComponentPort_owned_diagrams(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ComponentPort_element_of_interest_for_diagrams(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ComponentPort_contextual_element_for_diagrams(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ComponentPort_representing_diagrams(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ComponentPort_orientation(self):
        tested = ComponentPort()
        value = OrientationPortKind()
        tested.set_orientation(value)
        self.assertEqual(tested.get_orientation(), value)
        pass

    def test_ComponentPort_component_exchanges(self):
        tested = ComponentPort()
        value = ComponentExchange()
        tested.get_component_exchanges()
        pass

    def test_ComponentPort_allocated_function_ports(self):
        tested = ComponentPort()
        value = FunctionOutputPort()
        tested.get_allocated_function_ports()
        pass

    def test_ComponentPort_provided_interfaces(self):
        tested = ComponentPort()
        value = Interface()
        tested.get_provided_interfaces()
        pass

    def test_ComponentPort_required_interfaces(self):
        tested = ComponentPort()
        value = Interface()
        tested.get_required_interfaces()
        pass

    def test_ComponentPort_allocating_physical_ports(self):
        tested = ComponentPort()
        value = PhysicalPort()
        tested.set_allocating_physical_ports(value)
        self.assertEqual(tested.get_allocating_physical_ports(), value)
        pass

    def test_ComponentPort_realized_component_ports(self):
        tested = ComponentPort()
        value = ComponentPort()
        tested.get_realized_component_ports()
        pass

    def test_ComponentPort_realizing_component_ports(self):
        tested = ComponentPort()
        value = ComponentPort()
        tested.get_realizing_component_ports()
        pass

    def test_ComponentExchange_id(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ComponentExchange_sid(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ComponentExchange_name(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ComponentExchange_summary(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ComponentExchange_description(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ComponentExchange_status(self):
        tested = ComponentExchange()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ComponentExchange_review(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ComponentExchange_visible_in_documentation(self):
        tested = ComponentExchange()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ComponentExchange_visible_for_traceability(self):
        tested = ComponentExchange()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ComponentExchange_owned_constraints(self):
        tested = ComponentExchange()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ComponentExchange_constraints(self):
        tested = ComponentExchange()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ComponentExchange_owned_property_values(self):
        tested = ComponentExchange()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ComponentExchange_applied_property_values(self):
        tested = ComponentExchange()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ComponentExchange_owned_property_value_groups(self):
        tested = ComponentExchange()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ComponentExchange_applied_property_value_groups(self):
        tested = ComponentExchange()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ComponentExchange_owned_enumeration_property_types(self):
        tested = ComponentExchange()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ComponentExchange_owned_diagrams(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ComponentExchange_element_of_interest_for_diagrams(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ComponentExchange_contextual_element_for_diagrams(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ComponentExchange_representing_diagrams(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ComponentExchange_invoking_sequence_messages(self):
        tested = ComponentExchange()
        value = SequenceMessage()
        tested.get_invoking_sequence_messages().add(value)
        self.assertEqual(tested.get_invoking_sequence_messages().get(0), value)
        pass

    def test_ComponentExchange_connected_component_ports(self):
        tested = ComponentExchange()
        value = ComponentPort()
        tested.get_connected_component_ports().add(value)
        self.assertEqual(tested.get_connected_component_ports().get(0), value)
        pass

    def test_ComponentExchange_connected_components(self):
        tested = ComponentExchange()
        value = PhysicalActor()
        tested.get_connected_components()
        pass

    def test_ComponentExchange_categories(self):
        tested = ComponentExchange()
        value = ComponentExchangeCategory()
        tested.get_categories()
        pass

    def test_ComponentExchange_allocated_functional_exchanges(self):
        tested = ComponentExchange()
        value = FunctionalExchange()
        tested.get_allocated_functional_exchanges()
        pass

    def test_ComponentExchange_convoyed_informations(self):
        tested = ComponentExchange()
        value = ExchangeItem()
        tested.get_convoyed_informations().add(value)
        self.assertEqual(tested.get_convoyed_informations().get(0), value)
        pass

    def test_ComponentExchange_allocating_physical_link(self):
        tested = ComponentExchange()
        value = PhysicalLink()
        tested.set_allocating_physical_link(value)
        self.assertEqual(tested.get_allocating_physical_link(), value)
        pass

    def test_ComponentExchange_allocating_physical_path(self):
        tested = ComponentExchange()
        value = PhysicalPath()
        tested.set_allocating_physical_path(value)
        self.assertEqual(tested.get_allocating_physical_path(), value)
        pass

    def test_ComponentExchange_realized_communication_means(self):
        tested = ComponentExchange()
        value = CommunicationMean()
        tested.get_realized_communication_means().add(value)
        self.assertEqual(tested.get_realized_communication_means().get(0), value)
        pass

    def test_ComponentExchange_realized_component_exchanges(self):
        tested = ComponentExchange()
        value = ComponentExchange()
        tested.get_realized_component_exchanges()
        pass

    def test_ComponentExchange_realizing_component_exchanges(self):
        tested = ComponentExchange()
        value = ComponentExchange()
        tested.get_realizing_component_exchanges()
        pass

    def test_ComponentExchange_kind(self):
        tested = ComponentExchange()
        value = ComponentExchangeKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass

    def test_ComponentExchangeCategory_id(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_ComponentExchangeCategory_sid(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_sid(value)
        self.assertEqual(tested.get_sid(), value)
        pass

    def test_ComponentExchangeCategory_name(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_ComponentExchangeCategory_summary(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_summary(value)
        self.assertEqual(tested.get_summary(), value)
        pass

    def test_ComponentExchangeCategory_description(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_description(value)
        self.assertEqual(tested.get_description(), value)
        pass

    def test_ComponentExchangeCategory_status(self):
        tested = ComponentExchangeCategory()
        value = Status()
        tested.set_status(value)
        self.assertEqual(tested.get_status(), value)
        pass

    def test_ComponentExchangeCategory_review(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_review(value)
        self.assertEqual(tested.get_review(), value)
        pass

    def test_ComponentExchangeCategory_visible_in_documentation(self):
        tested = ComponentExchangeCategory()
        value = True
        tested.set_visible_in_documentation(value)
        self.assertEqual(tested.get_visible_in_documentation(), value)
        pass

    def test_ComponentExchangeCategory_visible_for_traceability(self):
        tested = ComponentExchangeCategory()
        value = True
        tested.set_visible_for_traceability(value)
        self.assertEqual(tested.get_visible_for_traceability(), value)
        pass

    def test_ComponentExchangeCategory_owned_constraints(self):
        tested = ComponentExchangeCategory()
        value = Constraint()
        tested.get_owned_constraints().add(value)
        self.assertEqual(tested.get_owned_constraints().get(0), value)
        pass

    def test_ComponentExchangeCategory_constraints(self):
        tested = ComponentExchangeCategory()
        value = Constraint()
        tested.get_constraints()
        pass

    def test_ComponentExchangeCategory_owned_property_values(self):
        tested = ComponentExchangeCategory()
        value = PropertyValue()
        tested.get_owned_property_values().add(value)
        self.assertEqual(tested.get_owned_property_values().get(0), value)
        pass

    def test_ComponentExchangeCategory_applied_property_values(self):
        tested = ComponentExchangeCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        self.assertEqual(tested.get_applied_property_values().get(0), value)
        pass

    def test_ComponentExchangeCategory_owned_property_value_groups(self):
        tested = ComponentExchangeCategory()
        value = PropertyValueGroup()
        tested.get_owned_property_value_groups().add(value)
        self.assertEqual(tested.get_owned_property_value_groups().get(0), value)
        pass

    def test_ComponentExchangeCategory_applied_property_value_groups(self):
        tested = ComponentExchangeCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        self.assertEqual(tested.get_applied_property_value_groups().get(0), value)
        pass

    def test_ComponentExchangeCategory_owned_enumeration_property_types(self):
        tested = ComponentExchangeCategory()
        value = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types().add(value)
        self.assertEqual(tested.get_owned_enumeration_property_types().get(0), value)
        pass

    def test_ComponentExchangeCategory_owned_diagrams(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_ComponentExchangeCategory_element_of_interest_for_diagrams(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_ComponentExchangeCategory_contextual_element_for_diagrams(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_ComponentExchangeCategory_representing_diagrams(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_ComponentExchangeCategory_exchanges(self):
        tested = ComponentExchangeCategory()
        value = ComponentExchange()
        tested.get_exchanges().add(value)
        self.assertEqual(tested.get_exchanges().get(0), value)
        pass

    def test_PVMT_getPVNames(self):
        self.fail("TODO")

    def test_PVMT_isPVDefined(self):
        self.fail("TODO")

    def test_PVMT_getPVValue(self):
        self.fail("TODO")

    def test_RequirementAddOn_getRequirementModules(self):
        self.fail("TODO")

    def test_RequirementAddOn_getIncomingRequirements(self):
        self.fail("TODO")

    def test_RequirementAddOn_getOutgoingRequirements(self):
        self.fail("TODO")

    def test_RequirementAddOn_getRelationType(self):
        self.fail("TODO")

    def test_CapellaModule_owned_diagrams(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_CapellaModule_element_of_interest_for_diagrams(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_CapellaModule_contextual_element_for_diagrams(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_CapellaModule_representing_diagrams(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_CapellaModule_owned_requirements(self):
        tested = CapellaModule()
        value = Requirement()
        tested.get_owned_requirements().add(value)
        self.assertEqual(tested.get_owned_requirements().get(0), value)
        pass

    def test_CapellaModule_id(self):
        tested = CapellaModule()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_CapellaModule_long_name(self):
        tested = CapellaModule()
        value = "value"
        tested.set_long_name(value)
        self.assertEqual(tested.get_long_name(), value)
        pass

    def test_CapellaModule_name(self):
        tested = CapellaModule()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_CapellaModule_prefix(self):
        tested = CapellaModule()
        value = "value"
        tested.set_prefix(value)
        self.assertEqual(tested.get_prefix(), value)
        pass

    def test_Requirement_owned_diagrams(self):
        tested = Requirement()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Requirement_element_of_interest_for_diagrams(self):
        tested = Requirement()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Requirement_contextual_element_for_diagrams(self):
        tested = Requirement()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Requirement_representing_diagrams(self):
        tested = Requirement()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Requirement_id(self):
        tested = Requirement()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Requirement_long_name(self):
        tested = Requirement()
        value = "value"
        tested.set_long_name(value)
        self.assertEqual(tested.get_long_name(), value)
        pass

    def test_Requirement_name(self):
        tested = Requirement()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Requirement_chapter_name(self):
        tested = Requirement()
        value = "value"
        tested.set_chapter_name(value)
        self.assertEqual(tested.get_chapter_name(), value)
        pass

    def test_Requirement_prefix(self):
        tested = Requirement()
        value = "value"
        tested.set_prefix(value)
        self.assertEqual(tested.get_prefix(), value)
        pass

    def test_Requirement_text(self):
        tested = Requirement()
        value = "value"
        tested.set_text(value)
        self.assertEqual(tested.get_text(), value)
        pass

    def test_Requirement_owned_attributes(self):
        tested = Requirement()
        value = Attribute()
        tested.get_owned_attributes().add(value)
        self.assertEqual(tested.get_owned_attributes().get(0), value)
        pass

    def test_Requirement_getIncomingLinkedElems(self):
        self.fail("TODO")

    def test_Requirement_getOutgoingLinkedElems(self):
        self.fail("TODO")

    def test_Folder_id(self):
        tested = Folder()
        value = "value"
        tested.set_id(value)
        self.assertEqual(tested.get_id(), value)
        pass

    def test_Folder_long_name(self):
        tested = Folder()
        value = "value"
        tested.set_long_name(value)
        self.assertEqual(tested.get_long_name(), value)
        pass

    def test_Folder_name(self):
        tested = Folder()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Folder_chapter_name(self):
        tested = Folder()
        value = "value"
        tested.set_chapter_name(value)
        self.assertEqual(tested.get_chapter_name(), value)
        pass

    def test_Folder_prefix(self):
        tested = Folder()
        value = "value"
        tested.set_prefix(value)
        self.assertEqual(tested.get_prefix(), value)
        pass

    def test_Folder_text(self):
        tested = Folder()
        value = "value"
        tested.set_text(value)
        self.assertEqual(tested.get_text(), value)
        pass

    def test_Folder_owned_attributes(self):
        tested = Folder()
        value = Attribute()
        tested.get_owned_attributes().add(value)
        self.assertEqual(tested.get_owned_attributes().get(0), value)
        pass

    def test_Folder_getIncomingLinkedElems(self):
        self.fail("TODO")

    def test_Folder_getOutgoingLinkedElems(self):
        self.fail("TODO")

    def test_Folder_owned_diagrams(self):
        tested = Folder()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Folder_element_of_interest_for_diagrams(self):
        tested = Folder()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Folder_contextual_element_for_diagrams(self):
        tested = Folder()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Folder_representing_diagrams(self):
        tested = Folder()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Folder_owned_requirements(self):
        tested = Folder()
        value = Requirement()
        tested.get_owned_requirements().add(value)
        self.assertEqual(tested.get_owned_requirements().get(0), value)
        pass

    def test_Attribute_owned_diagrams(self):
        tested = Attribute()
        value = Diagram()
        tested.get_owned_diagrams().add(value)
        self.assertEqual(tested.get_owned_diagrams().get(0), value)
        pass

    def test_Attribute_element_of_interest_for_diagrams(self):
        tested = Attribute()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        self.assertEqual(tested.get_element_of_interest_for_diagrams().get(0), value)
        pass

    def test_Attribute_contextual_element_for_diagrams(self):
        tested = Attribute()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        self.assertEqual(tested.get_contextual_element_for_diagrams().get(0), value)
        pass

    def test_Attribute_representing_diagrams(self):
        tested = Attribute()
        value = Diagram()
        tested.get_representing_diagrams().add(value)
        self.assertEqual(tested.get_representing_diagrams().get(0), value)
        pass

    def test_Attribute_name(self):
        tested = Attribute()
        value = "value"
        tested.set_name(value)
        self.assertEqual(tested.get_name(), value)
        pass

    def test_Attribute_value(self):
        tested = Attribute()
        value = "value"
        tested.set_value(value)
        self.assertEqual(tested.get_value(), value)
        pass

    def test_Attribute_kind(self):
        tested = Attribute()
        value = AttributeKind()
        tested.set_kind(value)
        self.assertEqual(tested.get_kind(), value)
        pass
