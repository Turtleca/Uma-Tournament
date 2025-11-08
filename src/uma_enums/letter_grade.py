from enum import Enum
from typing import Any


class LetterGrade(Enum):
    """Umamusume Letter Grade Enum."""

    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

    @classmethod
    def from_str(cls, value: Any) -> "LetterGrade":
        if isinstance(value, cls):
            return value
        if value is None:
            return cls.G
        v = str(value).strip().upper()
        if not v:
            return cls.G
        # accept first-letter matches and full-value matches
        if v[0] in cls.__members__:
            return cls[v[0]]
        for m in cls:
            if v == m.value:
                return m
        return cls.G
