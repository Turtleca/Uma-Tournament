"""
Uma Class file
"""

from enum import Enum
from typing import Dict, List


class LetterGrade(Enum):
    """
    Umamusume Letter Grade Enum

    Attributes
    ----------
    S :
    A :
    B :
    C :
    D :
    E :
    F :
    G :

    """

    S = "s"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


class Uma:

    # Identifiers
    name: str  # Name in Plain Text
    outfit_id: str  # Outfit tagline
    score: int

    # Stats
    stats: Dict[str, int] = {
        "speed": 1,
        "stamina": 1,
        "power": 1,
        "guts": 1,
        "wisdom": 1,
    }

    # Prefered Strategy
    strategy: str

    # Aptitudes
    aptitudes: Dict[str, Dict[str, LetterGrade]] = {
        "distance_aptitudes": {
            "Sprint": LetterGrade("G"),
            "Mile": LetterGrade("G"),
            "Medium": LetterGrade("G"),
            "Long": LetterGrade("G"),
        },
        "surface_aptitudes": {
            "Turf": LetterGrade("G"),
            "Dirt": LetterGrade("G"),
        },
        "strategy_aptitudes": {
            "Front": LetterGrade("G"),
            "Pace": LetterGrade("G"),
            "Late": LetterGrade("G"),
            "End": LetterGrade("G"),
        },
    }

    # Skills list (Skill Names)
    skills: List[str]

    def __init__(
        self,
        name: str,
        outfit: str,
        score: int,
        stats: List,
        op_strategy: str,
        aptitudes: List[List[str]],
        skills: List[str],
    ) -> None:
        """
        Parameters
        ----------
        name : str
        outfit : str
        score : int
        stats : List
        op_strategy : str
        skills : List
        aptitudes : List
        """

        # Identifiers
        self.name = name
        self.outfit_id = outfit
        self.score = score

        # Stats
        (
            self.stats["speed"],
            self.stats["stamina"],
            self.stats["power"],
            self.stats["guts"],
            self.stats["wisdom"],
        ) = stats

        # Strategy
        self.strategy = op_strategy

        # Aptitudes
        self.distance_aptitudes = LetterGrade(aptitudes[0])
        self.surface_aptitudes = LetterGrade(aptitudes[1])
        self.strategy_aptitudes = LetterGrade(aptitudes[2])

        # Skills
        self.skills = skills

    def to_json(self) -> Dict:
        return {
            "name": self.name,
            "outfitId": self.outfit_id,
            "speed": self.speed,
            "stamina": self.stamina,
            "power": self.power,
            "guts": self.guts,
            "wisdom": self.wisdom,
            "strategy": self.strategy,
            "distanceAptitude": self.distance_aptitudes,
            "surfaceAptitude": self.surface_aptitudes,
            "strategyAptitude": self.strategy_aptitudes,
            "skills": self.skills,
        }
