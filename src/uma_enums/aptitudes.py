from enum import Enum
from typing import Any, Optional


class UmaStyle(Enum):
    # Primary canonical values are the Japanese romanized names required for output
    NIGE = "Nige"
    SENJOUR = "Senjour"
    SASI = "Sasi"
    OIKOMI = "Oikomi"

    # Aliases for English/alternate names (these will be enum aliases)
    FRONT = NIGE
    NIGE_ALT = NIGE  # additional alias if needed
    PACE = SENJOUR
    SENKOU = SENJOUR
    LATE = SASI
    SASHI = SASI
    END = OIKOMI

    @classmethod
    def from_name(cls, name: Optional[Any]) -> Optional["UmaStyle"]:

        if not name:
            return None
        key = str(name).strip().lower()

        # Direct matches on canonical values
        for member in (cls.NIGE, cls.SENJOUR, cls.SASI, cls.OIKOMI):
            if key == member.value.lower():
                return member

        # Normalize common synonyms and romanizations
        mapping = {
            # Front runner synonyms -> NIGE
            "nige": cls.NIGE,
            "front": cls.NIGE,
            # Pace runner synonyms -> SENJOUR
            "pace": cls.SENJOUR,
            "senjou": cls.SENJOUR,
            "senkou": cls.SENJOUR,
            "senkō": cls.SENJOUR,
            # Late runner synonyms -> SASI
            "sasi": cls.SASI,
            "sashi": cls.SASI,
            "late": cls.SASI,
            # Oikomi / End -> OIKOMI
            "oikomi": cls.OIKOMI,
            "end": cls.OIKOMI,
        }

        # Some inputs may use first-letter english words; handle those
        first_char_map = {
            "f": cls.NIGE,  # front
            "p": cls.SENJOUR,  # pace
            "l": cls.SASI,  # late
            "e": cls.OIKOMI,  # end
        }

        if key in mapping:
            return mapping[key]
        if key and key[0] in first_char_map:
            return first_char_map[key[0]]
        return None


class UmaTrack(Enum):
    TURF = 0
    DIRT = 1


class UmaDistance(Enum):
    SPRINT = 0
    MILE = 1
    MEDIUM = 2
    LONG = 3


class UmaStats(Enum):
    SPEED = "speed"
    STAMINA = "stamina"
    POWER = "power"
    GUTS = "guts"
    WIT = "wisdom"
