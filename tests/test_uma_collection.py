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
    def test_veterans_json_loads_snake_case_schema(self) -> None:
        veterans = [{
            "trained_chara_id": 78,
            "card_id": 106101,
            "speed": 1200,
            "stamina": 800,
            "power": 900,
            "wiz": 1000,
            "guts": 700,
            "running_style": 3,
            "skill_array": [{"skill_id": 200331, "level": 1}],
            "support_card_list": [{
                "position": 1,
                "support_card_id": 20023,
                "exp": 10740,
                "limit_break_count": 0,
            }],
            "race_result_list": [{
                "turn": 1,
                "program_id": 100,
                "weather": 1,
                "ground_condition": 1,
                "running_style": 3,
                "result_rank": 1,
            }],
        }]

        with tempfile.NamedTemporaryFile(
            "w",
            suffix=".json",
            encoding="utf-8",
        ) as file:
            json.dump(veterans, file)
            file.flush()
            collection = UmaCollection(file.name)

        uma = collection.get_all()[0]
        self.assertEqual(uma.trained_chara_id, 78)
        self.assertEqual(uma.running_style, 3)
        self.assertIsInstance(uma.skills[0], Skill)
        self.assertIsInstance(uma.support_card_list[0], SupportCard)
        self.assertIsInstance(uma.race_result_list[0], RaceResult)

    def test_normalized_horseact_aliases_load(self) -> None:
        veterans = [{
            "id": 78,
            "cardId": 106101,
            "speed": 1200,
            "stamina": 800,
            "power": 900,
            "wiz": 1000,
            "guts": 700,
            "raceRunningStyle": 3,
            "acquiredSkillArray": [{"skillId": 200331, "level": 1}],
            "supportCardArray": [{
                "position": 1,
                "supportCardId": 20023,
                "exp": 10740,
                "limitBreakCount": 0,
            }],
            "singleModeRaceResultArray": [{
                "turn": 1,
                "programId": 100,
                "weather": 1,
                "groundCondition": 1,
                "runningStyle": 3,
                "resultRank": 1,
            }],
            "successionCharaList": [{
                "positionId": 1,
                "cardId": 10010,
                "rank": 10,
                "rarity": 3,
                "talentLevel": 5,
                "factorDataArray": [
                    {"factorId": 2001},
                ],
            }],
        }]

        with tempfile.NamedTemporaryFile(
            "w",
            suffix=".json",
            encoding="utf-8",
        ) as file:
            json.dump(veterans, file)
            file.flush()
            collection = UmaCollection(file.name)

        uma = collection.get_all()[0]
        self.assertEqual(uma.trained_chara_id, 78)
        self.assertEqual(uma.running_style, 3)
        self.assertEqual(uma.skills[0].skill_id, 200331)
        self.assertEqual(uma.support_card_list[0].support_card_id, 20023)
        self.assertEqual(uma.succession_chara_array[0].card_id, 10010)

    def test_veterans_file_must_be_an_array(self) -> None:
        with tempfile.NamedTemporaryFile(
            "w",
            suffix=".json",
            encoding="utf-8",
        ) as file:
            json.dump({"single_mode_load_common": {}}, file)
            file.flush()
            with self.assertRaises(ValueError):
                UmaCollection(file.name)

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
