from pathlib import Path
from typing import Dict, List, Optional, Union

from .uma import Uma
from .uma_factory import UmaFactory
from .json_loader import UmaJsonLoader


class UmaCollection:
    """A collection of Uma domain objects."""

    def __init__(
        self,
        filepath: Optional[Union[str, Path]] = None,
        loader: Optional[UmaJsonLoader] = None,
        factory: Optional[UmaFactory] = None,
    ) -> None:
        self.umas: List[Uma] = []
        self.filepath = filepath
        self.loader = loader or UmaJsonLoader()
        self.factory = factory or UmaFactory()
        if filepath is not None:
            self.load_from_file(filepath)

    def load_from_file(self, filepath: Union[str, Path]) -> None:
        self.filepath = filepath
        uma_data = self.loader.load(filepath)
        self.umas = [self.factory.create(item) for item in uma_data]

    def add_uma(self, uma: Uma) -> None:
        self.umas.append(uma)

    def remove_uma(self, trained_chara_id: int) -> bool:
        original_count = len(self.umas)
        self.umas = [
            uma
            for uma in self.umas
            if uma.trained_chara_id != trained_chara_id
        ]
        return len(self.umas) < original_count

    def get_all(self) -> List[Uma]:
        return self.umas.copy()

    def get_by_id(self, trained_chara_id: int) -> Optional[Uma]:
        return next(
            (
                uma
                for uma in self.umas
                if uma.trained_chara_id == trained_chara_id
            ),
            None,
        )

    def get_by_card_id(self, card_id: int) -> List[Uma]:
        return [uma for uma in self.umas if uma.card_id == card_id]

    def get_count(self) -> int:
        return len(self.umas)

    def filter_by_rank(
        self,
        min_rank: Optional[int] = None,
        max_rank: Optional[int] = None,
    ) -> List[Uma]:
        result = self.umas
        if min_rank is not None:
            result = [uma for uma in result if uma.rank >= min_rank]
        if max_rank is not None:
            result = [uma for uma in result if uma.rank <= max_rank]
        return result

    def filter_by_rarity(self, rarity: int) -> List[Uma]:
        return [uma for uma in self.umas if uma.rarity == rarity]

    def filter_by_running_style(self, running_style: int) -> List[Uma]:
        return [
            uma
            for uma in self.umas
            if uma.running_style == running_style
        ]

    def filter_by_min_total_stats(self, min_stats: int) -> List[Uma]:
        return [
            uma
            for uma in self.umas
            if uma.get_total_stats() >= min_stats
        ]

    def filter_locked(self, locked: bool = True) -> List[Uma]:
        return [
            uma
            for uma in self.umas
            if (uma.is_locked == 1) == locked
        ]

    def get_average_stats(self) -> Dict[str, float]:
        if not self.umas:
            return {}
        count = len(self.umas)
        return {
            "avg_speed": sum(uma.speed for uma in self.umas) / count,
            "avg_stamina": sum(uma.stamina for uma in self.umas) / count,
            "avg_power": sum(uma.power for uma in self.umas) / count,
            "avg_wisdom": sum(uma.wiz for uma in self.umas) / count,
            "avg_guts": sum(uma.guts for uma in self.umas) / count,
            "avg_total": sum(
                uma.get_total_stats() for uma in self.umas
            ) / count,
        }

    def get_top_umas(
        self,
        n: int = 10,
        sort_by: str = "rank_score",
    ) -> List[Uma]:
        if sort_by == "total_stats":
            sorted_umas = sorted(
                self.umas,
                key=lambda uma: uma.get_total_stats(),
                reverse=True,
            )
        elif sort_by == "rank":
            sorted_umas = sorted(
                self.umas,
                key=lambda uma: uma.rank,
                reverse=True,
            )
        elif sort_by == "fans":
            sorted_umas = sorted(
                self.umas,
                key=lambda uma: uma.fans,
                reverse=True,
            )
        else:
            sorted_umas = sorted(
                self.umas,
                key=lambda uma: uma.rank_score,
                reverse=True,
            )
        return sorted_umas[:n]
