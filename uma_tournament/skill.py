from dataclasses import dataclass


@dataclass(frozen=True)
class Skill:
    """A skill learned by an Uma."""

    skill_id: int
    level: int
