import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from step_solid_inventory import inventory_step_solids


class StepSolidInventoryTests(unittest.TestCase):
    def test_counts_distinct_supported_solid_definitions(self):
        step = """ISO-10303-21;HEADER;ENDSEC;DATA;
#1=MANIFOLD_SOLID_BREP('',#10);
#2=BREP_WITH_VOIDS('',#11,(#12));
#3=FACETED_BREP('',#13);
#4=CLOSED_SHELL('',());
#5=ORIENTED_CLOSED_SHELL('',#4,.T.);
ENDSEC;END-ISO-10303-21;"""
        result = inventory_step_solids(step)
        self.assertEqual(result["supported_solid_entity_counts"], {
            "MANIFOLD_SOLID_BREP": 1, "BREP_WITH_VOIDS": 1, "FACETED_BREP": 1,
        })
        self.assertEqual(result["supported_solid_definition_count"], 3)
        self.assertEqual(result["simple_non_solid_definition_count"], 2)

    def test_ignores_types_mentioned_in_comments_and_strings(self):
        step = """DATA;
/* #1=MANIFOLD_SOLID_BREP('',#2); */
#3=PRODUCT('MANIFOLD_SOLID_BREP(', '', '', ());
#4=MANIFOLD_SOLID_BREP('',#5);
ENDSEC;"""
        self.assertEqual(inventory_step_solids(step)["supported_solid_definition_count"], 1)

    def test_reports_complex_entities_separately(self):
        step = """DATA;
#12=(REPRESENTATION_ITEM('') MANIFOLD_SOLID_BREP('',#20));
#13=(PRODUCT('x','','',()) PRODUCT_DEFINITION_FORMATION('','',#14));
ENDSEC;"""
        result = inventory_step_solids(step)
        self.assertEqual(result["supported_solid_definition_count"], 0)
        self.assertEqual(result["complex_solid_related_entities"], [{
            "entity_id": 12,
            "component_types": ["MANIFOLD_SOLID_BREP", "REPRESENTATION_ITEM"],
            "solid_related": True,
        }])
        self.assertEqual([row["entity_id"] for row in result["complex_entities"]], [12, 13])

    def test_duplicate_entity_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate STEP entity"):
            inventory_step_solids("DATA;#1=MANIFOLD_SOLID_BREP('',#2);#1=FACETED_BREP('',#3);ENDSEC;")

    def test_missing_data_section_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "DATA section"):
            inventory_step_solids("ISO-10303-21;HEADER;ENDSEC;END-ISO-10303-21;")


if __name__ == "__main__":
    unittest.main()
