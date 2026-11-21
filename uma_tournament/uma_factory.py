from typing import Any, Dict, List

from .race_result import RaceResult
from .skill import Skill
from .succession_chara_info import SuccessionCharaInfo
from .support_card import SupportCard
from .uma import Uma


class UmaFactory:
    """Converts normalized JSON dictionaries into Uma domain objects."""

    REQUIRED_FIELDS = (
        "trained_chara_id",
        "speed",
        "stamina",
        "power",
        "wiz",
        "guts",
        "rank",
        "rank_score",
        "running_style",
        "card_id",
    )

    def create(self, uma_data: Dict[str, Any]) -> Uma:
        normalized = dict(uma_data)
        normalized.setdefault(
            "trained_chara_id",
            normalized.get("single_mode_chara_id", 0),
        )
        normalized.setdefault(
            "running_style",
            normalized.get("race_running_style"),
        )
        normalized.setdefault("rank", normalized.get("chara_grade", 0))
        normalized.setdefault("rank_score", 0)

        missing = [field for field in self.REQUIRED_FIELDS if field not in normalized]
        if missing:
            raise ValueError(f"Missing required fields in Uma data: {missing}")

        return Uma(
            trained_chara_id=normalized["trained_chara_id"],
            owner_trained_chara_id=normalized.get("owner_trained_chara_id", 0),
            single_mode_chara_id=normalized.get("single_mode_chara_id", 0),
            chara_seed=normalized.get("chara_seed", 0),
            card_id=normalized["card_id"],
            speed=normalized["speed"],
            stamina=normalized["stamina"],
            power=normalized["power"],
            wiz=normalized["wiz"],
            guts=normalized["guts"],
            fans=normalized.get("fans", 0),
            rank_score=normalized["rank_score"],
            rank=normalized["rank"],
            wins=normalized.get("wins", 0),
            scenario_id=normalized.get("scenario_id", 1),
            route_id=normalized.get("route_id", 0),
            arrive_route_race_id=normalized.get("arrive_route_race_id", 0),
            running_style=normalized["running_style"],
            talent_level=normalized.get("talent_level", 0),
            proper_ground_turf=normalized.get("proper_ground_turf", 0),
            proper_ground_dirt=normalized.get("proper_ground_dirt", 0),
            proper_running_style_nige=normalized.get("proper_running_style_nige", 0),
            proper_running_style_senko=normalized.get("proper_running_style_senko", 0),
            proper_running_style_sashi=normalized.get("proper_running_style_sashi", 0),
            proper_running_style_oikomi=normalized.get("proper_running_style_oikomi", 0),
            proper_distance_short=normalized.get("proper_distance_short", 0),
            proper_distance_mile=normalized.get("proper_distance_mile", 0),
            proper_distance_middle=normalized.get("proper_distance_middle", 0),
            proper_distance_long=normalized.get("proper_distance_long", 0),
            chara_grade=normalized.get("chara_grade", 0),
            rarity=normalized.get("rarity", 0),
            nickname_id=normalized.get("nickname_id", 0),
            skills=self._create_skills(normalized),
            support_card_list=self._create_support_cards(normalized),
            race_result_list=self._create_race_results(normalized),
            win_saddle_id_array=normalized.get("win_saddle_id_array", []),
            nickname_id_array=normalized.get("nickname_id_array", []),
            factor_id_array=normalized.get("factor_id_array", []),
            factor_info_array=normalized.get("factor_info_array", []),
            succession_chara_array=self._create_succession_charas(normalized),
            succession_history_array=normalized.get("succession_history_array", []),
            succession_trained_chara_id_1=normalized.get(
                "succession_trained_chara_id_1"
            ),
            succession_trained_chara_id_2=normalized.get(
                "succession_trained_chara_id_2"
            ),
            succession_num=normalized.get("succession_num", 0),
            use_type=normalized.get("use_type", 0),
            is_saved=normalized.get("is_saved", 1),
            is_locked=normalized.get("is_locked", 1),
            race_cloth_id=normalized.get("race_cloth_id", 101),
            register_time=normalized.get("register_time", ""),
            create_time=normalized.get("create_time", ""),
        )

    @staticmethod
    def _create_skills(data: Dict[str, Any]) -> List[Skill]:
        return [
            Skill(skill_id=skill["skill_id"], level=skill["level"])
            for skill in data.get("skill_array", [])
        ]

    @staticmethod
    def _create_support_cards(data: Dict[str, Any]) -> List[SupportCard]:
        cards = data.get("support_card_list")
        if cards is None:
            cards = data.get("support_card_array", [])
        return [
            SupportCard(
                position=card["position"],
                support_card_id=card["support_card_id"],
                exp=card["exp"],
                limit_break_count=card["limit_break_count"],
            )
            for card in cards
        ]

    @staticmethod
    def _create_race_results(data: Dict[str, Any]) -> List[RaceResult]:
        results = data.get("race_result_list")
        if results is None:
            results = data.get("race_history", [])
        return [
            RaceResult(
                turn=result["turn"],
                program_id=result["program_id"],
                weather=result["weather"],
                ground_condition=result["ground_condition"],
                running_style=result.get(
                    "running_style",
                    data.get("running_style", data.get("race_running_style", 0)),
                ),
                popularity=result.get("popularity", 0),
                result_rank=result.get(
                    "result_rank",
                    result.get("frame_order", 0),
                ),
                result_time=result.get("result_time", 0),
                prize_money=result.get("prize_money", 0),
            )
            for result in results
        ]

    @staticmethod
    def _create_succession_charas(
        data: Dict[str, Any],
    ) -> List[SuccessionCharaInfo]:
        return [
            SuccessionCharaInfo(
                position_id=char.get("position_id", 0),
                card_id=char["card_id"],
                rank=char["rank"],
                rarity=char["rarity"],
                talent_level=char["talent_level"],
                factor_id_array=char.get("factor_id_array", []),
                factor_info_array=char.get("factor_info_array", []),
                win_saddle_id_array=char.get("win_saddle_id_array", []),
                owner_viewer_id=char.get("owner_viewer_id", 0),
            )
            for char in data.get("succession_chara_array", [])
        ]
