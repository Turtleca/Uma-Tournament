from dataclasses import dataclass


@dataclass(frozen=True)
class SupportCard:
    """An equipped support card."""

    position: int
    support_card_id: int
    exp: int
    limit_break_count: int
