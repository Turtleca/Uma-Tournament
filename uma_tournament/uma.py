from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .race_result import RaceResult
from .skill import Skill
from .succession_chara_info import SuccessionCharaInfo
from .support_card import SupportCard


@dataclass
class Uma:
    """An individual trained Uma."""

    trained_chara_id: int = 0
    owner_trained_chara_id: int = 0
    single_mode_chara_id: int = 0
    chara_seed: int = 0
    card_id: int = 0
    speed: int = 0
    stamina: int = 0
    power: int = 0
    wiz: int = 0
    guts: int = 0
    fans: int = 0
    rank_score: int = 0
    rank: int = 0
    wins: int = 0
    motivation: int = 0
    talent_level: int = 0
    running_style: int = 0
    scenario_id: int = 0
    route_id: int = 0
    arrive_route_race_id: int = 0
    chara_grade: int = 0
    rarity: int = 0
    nickname_id: int = 0
    race_cloth_id: int = 0
    max_speed: int = 0
    max_stamina: int = 0
    max_power: int = 0
    max_wiz: int = 0
    max_guts: int = 0
    proper_ground_turf: int = 0
    proper_ground_dirt: int = 0
    proper_running_style_nige: int = 0
    proper_running_style_senko: int = 0
    proper_running_style_sashi: int = 0
    proper_running_style_oikomi: int = 0
    proper_distance_short: int = 0
    proper_distance_mile: int = 0
    proper_distance_middle: int = 0
    proper_distance_long: int = 0
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
