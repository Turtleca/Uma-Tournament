from typing import Any, Dict, Iterable, List, Optional

from .race_result import RaceResult
from .skill import Skill
from .succession_chara_info import SuccessionCharaInfo
from .support_card import SupportCard
from .uma import Uma


def normalized_key(key: str) -> str:
    return "".join(character.lower() for character in key if character.isalnum())


def get_value(data: Dict[str, Any], *names: str, default: Any = 0) -> Any:
    normalized_names = {normalized_key(name) for name in names}
    for key, value in data.items():
        if normalized_key(key) in normalized_names:
            return value
    return default


class UmaFactory:
    """Converts one horseACT veterans.json entry into an Uma."""

    def create(self, data: Dict[str, Any]) -> Uma:
        return Uma(
            trained_chara_id=get_value(
                data,
                "trained_chara_id",
                "trainedCharaId",
                "id",
            ),
            owner_trained_chara_id=get_value(
                data,
                "owner_trained_chara_id",
                "ownerTrainedCharaId",
            ),
            single_mode_chara_id=get_value(
                data,
                "single_mode_chara_id",
                "singleModeCharaId",
            ),
            chara_seed=get_value(data, "chara_seed", "charaSeed"),
            card_id=get_value(data, "card_id", "cardId"),
            speed=get_value(data, "speed"),
            stamina=get_value(data, "stamina"),
            power=get_value(data, "power"),
            wiz=get_value(data, "wiz", "wisdom"),
            guts=get_value(data, "guts"),
            fans=get_value(data, "fans", "fanCount"),
            rank_score=get_value(data, "rank_score", "rankScore"),
            rank=get_value(data, "rank"),
            wins=get_value(
                data,
                "wins",
                "single_win_num",
                "singleWinNum",
            ),
            motivation=get_value(data, "motivation"),
            talent_level=get_value(data, "talent_level", "talentLevel"),
            running_style=get_value(
                data,
                "running_style",
                "race_running_style",
                "raceRunningStyle",
            ),
            scenario_id=get_value(data, "scenario_id", "scenarioId"),
            route_id=get_value(data, "route_id", "routeId"),
            arrive_route_race_id=get_value(
                data,
                "arrive_route_race_id",
                "arriveRouteRaceId",
            ),
            chara_grade=get_value(data, "chara_grade", "charaGrade"),
            rarity=get_value(data, "rarity"),
            nickname_id=get_value(data, "nickname_id", "nick_name_id", "nickNameId"),
            race_cloth_id=get_value(data, "race_cloth_id", "raceClothId"),
            max_speed=get_value(data, "max_speed", "maxSpeed"),
            max_stamina=get_value(data, "max_stamina", "maxStamina"),
            max_power=get_value(data, "max_power", "maxPower"),
            max_wiz=get_value(data, "max_wiz", "maxWiz"),
            max_guts=get_value(data, "max_guts", "maxGuts"),
            proper_ground_turf=get_value(
                data,
                "proper_ground_turf",
                "properGroundTurf",
            ),
            proper_ground_dirt=get_value(
                data,
                "proper_ground_dirt",
                "properGroundDirt",
            ),
            proper_running_style_nige=get_value(
                data,
                "proper_running_style_nige",
                "properRunningStyleNige",
            ),
            proper_running_style_senko=get_value(
                data,
                "proper_running_style_senko",
                "properRunningStyleSenko",
            ),
            proper_running_style_sashi=get_value(
                data,
                "proper_running_style_sashi",
                "properRunningStyleSashi",
            ),
            proper_running_style_oikomi=get_value(
                data,
                "proper_running_style_oikomi",
                "properRunningStyleOikomi",
            ),
            proper_distance_short=get_value(
                data,
                "proper_distance_short",
                "properDistanceShort",
            ),
            proper_distance_mile=get_value(
                data,
                "proper_distance_mile",
                "properDistanceMile",
            ),
            proper_distance_middle=get_value(
                data,
                "proper_distance_middle",
                "properDistanceMiddle",
            ),
            proper_distance_long=get_value(
                data,
                "proper_distance_long",
                "properDistanceLong",
            ),
            skills=self._create_skills(data),
            support_card_list=self._create_support_cards(data),
            race_result_list=self._create_race_results(data),
            win_saddle_id_array=self._get_int_list(
                data,
                "win_saddle_id_array",
                "winSaddleIdArray",
            ),
            nickname_id_array=self._get_int_list(
                data,
                "nickname_id_array",
                "nick_name_id_array",
                "nickNameIdArray",
            ),
            factor_id_array=self._get_int_list(
                data,
                "factor_id_array",
                "factorIdArray",
                "factorDataArray",
            ),
            factor_info_array=get_value(
                data,
                "factor_info_array",
                "factorInfoArray",
                "factorDataArray",
                default=[],
            ),
            succession_chara_array=self._create_succession_charas(data),
            succession_history_array=get_value(
                data,
                "succession_history_array",
                "successionHistoryArray",
                default=[],
            ),
            succession_trained_chara_id_1=get_value(
                data,
                "succession_trained_chara_id_1",
                "successionTrainedCharaId1",
            ),
            succession_trained_chara_id_2=get_value(
                data,
                "succession_trained_chara_id_2",
                "successionTrainedCharaId2",
            ),
            succession_num=get_value(
                data,
                "succession_num",
                "successionCount",
                "successionNum",
            ),
            use_type=get_value(data, "use_type", "useType"),
            is_saved=get_value(data, "is_saved", "isSaved"),
            is_locked=get_value(data, "is_locked", "isLock", "isLocked"),
            register_time=get_value(
                data,
                "register_time",
                "registerTime",
                default="",
            ),
            create_time=get_value(data, "create_time", "createTime", default=""),
        )

    @staticmethod
    def _get_int_list(
        data: Dict[str, Any],
        *names: str,
    ) -> List[int]:
        value = get_value(data, *names, default=[])
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, int)]

    @staticmethod
    def _get_array(
        data: Dict[str, Any],
        *names: str,
    ) -> List[Dict[str, Any]]:
        value = get_value(data, *names, default=[])
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, dict)]

    def _create_skills(self, data: Dict[str, Any]) -> List[Skill]:
        return [
            Skill(
                skill_id=get_value(skill, "skill_id", "skillId"),
                level=get_value(skill, "level"),
            )
            for skill in self._get_array(
                data,
                "skill_array",
                "acquired_skill_array",
                "acquiredSkillArray",
            )
        ]

    def _create_support_cards(
        self,
        data: Dict[str, Any],
    ) -> List[SupportCard]:
        return [
            SupportCard(
                position=get_value(card, "position"),
                support_card_id=get_value(
                    card,
                    "support_card_id",
                    "supportCardId",
                ),
                exp=get_value(card, "exp"),
                limit_break_count=get_value(
                    card,
                    "limit_break_count",
                    "limitBreakCount",
                ),
            )
            for card in self._get_array(
                data,
                "support_card_list",
                "supportCardArray",
                "support_card_array",
            )
        ]

    def _create_race_results(
        self,
        data: Dict[str, Any],
    ) -> List[RaceResult]:
        return [
            RaceResult(
                turn=get_value(result, "turn"),
                program_id=get_value(result, "program_id", "programId"),
                weather=get_value(result, "weather"),
                ground_condition=get_value(
                    result,
                    "ground_condition",
                    "groundCondition",
                ),
                running_style=get_value(result, "running_style", "runningStyle"),
                popularity=get_value(result, "popularity"),
                result_rank=get_value(
                    result,
                    "result_rank",
                    "resultRank",
                    "frame_order",
                    "frameOrder",
                ),
                result_time=get_value(
                    result,
                    "result_time",
                    "resultTime",
                ),
                prize_money=get_value(
                    result,
                    "prize_money",
                    "prizeMoney",
                ),
            )
            for result in self._get_array(
                data,
                "race_result_list",
                "singleModeRaceResultArray",
                "raceHistory",
            )
        ]

    def _create_succession_charas(
        self,
        data: Dict[str, Any],
    ) -> List[SuccessionCharaInfo]:
        return [
            SuccessionCharaInfo(
                position_id=get_value(
                    char,
                    "position_id",
                    "positionId",
                ),
                card_id=get_value(char, "card_id", "cardId"),
                rank=get_value(char, "rank"),
                rarity=get_value(char, "rarity"),
                talent_level=get_value(
                    char,
                    "talent_level",
                    "talentLevel",
                ),
                factor_id_array=self._get_int_list(
                    char,
                    "factor_id_array",
                    "factorIdArray",
                    "factorDataArray",
                ),
                factor_info_array=get_value(
                    char,
                    "factor_info_array",
                    "factorInfoArray",
                    "factorDataArray",
                    default=[],
                ),
                win_saddle_id_array=self._get_int_list(
                    char,
                    "win_saddle_id_array",
                    "winSaddleIdArray",
                ),
                owner_viewer_id=get_value(
                    char,
                    "owner_viewer_id",
                    "ownerViewerId",
                ),
            )
            for char in self._get_array(
                data,
                "succession_chara_array",
                "successionCharaList",
                "succession_chara_list",
            )
        ]
