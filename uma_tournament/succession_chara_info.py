from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class SuccessionCharaInfo:
    """Information about a succession character."""

    position_id: int
    card_id: int
    rank: int
    rarity: int
    talent_level: int
    factor_id_array: List[int] = field(default_factory=list)
    factor_info_array: List[Dict[str, int]] = field(default_factory=list)
    win_saddle_id_array: List[int] = field(default_factory=list)
    owner_viewer_id: int = 0
