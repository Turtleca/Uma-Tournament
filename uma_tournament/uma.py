from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .race_result import RaceResult
from .skill import Skill
from .succession_chara_info import SuccessionCharaInfo
from .support_card import SupportCard


@dataclass
class Uma:
    """An individual trained Uma."""

    trained_chara_id: int
    owner_trained_chara_id: int
    single_mode_chara_id: int
    chara_seed: int
    card_id: int
    speed: int
    stamina: int
    power: int
    wiz: int
    guts: int
    fans: int
    rank_score: int
    rank: int
    wins: int
    scenario_id: int
    route_id: int
    arrive_route_race_id: int
    running_style: int
    talent_level: int
    proper_ground_turf: int
    proper_ground_dirt: int
    proper_running_style_nige: int
    proper_running_style_senko: int
    proper_running_style_sashi: int
    proper_running_style_oikomi: int
    proper_distance_short: int
    proper_distance_mile: int
    proper_distance_middle: int
    proper_distance_long: int
    chara_grade: int
    rarity: int
    nickname_id: int
    skills: List[Skill] = field(default_factory=list)
    support_card_list: List[SupportCard] = field(default_factory=list)
    race_result_list: List[RaceResult] = field(default_factory=list)
    win_saddle_id_array: List[int] = field(default_factory=list)
    nickname_id_array: List[int] = field(default_factory=list)
    factor_id_array: List[int] = field(default_factory=list)
    factor_info_array: List[Dict[str, int]] = field(default_factory=list)
    succession_chara_array: List[SuccessionCharaInfo] = field(default_factory=list)
    succession_history_array: List[Dict[str, Any]] = field(default_factory=list)
    succession_trained_chara_id_1: Optional[int] = None
    succession_trained_chara_id_2: Optional[int] = None
    succession_num: int = 0
    use_type: int = 0
    is_saved: int = 1
    is_locked: int = 1
    race_cloth_id: int = 101
    register_time: str = ""
    create_time: str = ""

    def get_total_stats(self) -> int:
        return self.speed + self.stamina + self.power + self.wiz + self.guts

    def get_aptitude_dict(self) -> Dict[str, int]:
        return {
            "turf": self.proper_ground_turf,
            "dirt": self.proper_ground_dirt,
            "nige": self.proper_running_style_nige,
            "senko": self.proper_running_style_senko,
            "sashi": self.proper_running_style_sashi,
            "oikomi": self.proper_running_style_oikomi,
            "short": self.proper_distance_short,
            "mile": self.proper_distance_mile,
            "middle": self.proper_distance_middle,
            "long": self.proper_distance_long,
        }

    def __repr__(self) -> str:
        return (
            f"Uma(id={self.trained_chara_id}, card={self.card_id}, "
            f"stats={self.get_total_stats()}, rank={self.rank})"
        )
