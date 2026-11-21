import json
import tempfile
import unittest

from uma_collection import UmaCollection
from uma_tournament import (
    RaceResult,
    Skill,
    SuccessionCharaInfo,
    SupportCard,
    Uma,
)


class UmaCollectionTest(unittest.TestCase):
    def test_legacy_data_json_loads(self) -> None:
        collection = UmaCollection("umas/data.json")

        self.assertGreater(collection.get_count(), 0)
        self.assertIsInstance(collection.get_all()[0], Uma)

    def test_career_export_json_loads(self) -> None:
        career = {
            "single_mode_load_common": {
                "chara_info": {
                    "single_mode_chara_id": 78,
                    "card_id": 106101,
                    "speed": 1200,
                    "stamina": 800,
                    "power": 900,
                    "guts": 700,
                    "wiz": 1000,
                    "chara_grade": 9,
                    "race_running_style": 3,
                    "skill_array": [{"skill_id": 200331, "level": 1}],
                    "support_card_array": [
                        {
                            "position": 1,
                            "support_card_id": 20023,
                            "exp": 10740,
                            "limit_break_count": 0,
                        }
                    ],
                    "race_history": [
                        {
                            "turn": 1,
                            "program_id": 100,
                            "weather": 1,
                            "ground_condition": 1,
                            "running_style": 3,
                            "result_rank": 1,
                        }
                    ],
                }
            }
        }

        with tempfile.NamedTemporaryFile(
            "w",
            suffix=".json",
            encoding="utf-8",
        ) as file:
            json.dump(career, file)
            file.flush()
            collection = UmaCollection(file.name)

        uma = collection.get_all()[0]
        self.assertEqual(uma.trained_chara_id, 78)
        self.assertEqual(uma.running_style, 3)
        self.assertIsInstance(uma.skills[0], Skill)
        self.assertIsInstance(uma.support_card_list[0], SupportCard)
        self.assertIsInstance(uma.race_result_list[0], RaceResult)

    def test_domain_classes_are_separate_exports(self) -> None:
        self.assertTrue(
            all(
                model is not None
                for model in (
                    Uma,
                    Skill,
                    SupportCard,
                    RaceResult,
                    SuccessionCharaInfo,
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
