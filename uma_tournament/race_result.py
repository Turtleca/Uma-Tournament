from dataclasses import dataclass


@dataclass(frozen=True)
class RaceResult:
    """A single race result."""

    turn: int
    program_id: int
    weather: int
    ground_condition: int
    running_style: int
    popularity: int
    result_rank: int
    result_time: int
    prize_money: int
