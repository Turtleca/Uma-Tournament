"""
Uma Class file
"""

from enum import Enum
from typing import Dict, List, Self

from aptitudes import Aptitudes


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
    """
    # Uma Class
    Stores all attributes associated with a specific veteran Uma.
    Interact with Getters and Setters to keep class in line.

    Attributes
    ----------
    name : str
        Name of the Uma. Used with outfit_id to get unique skill
    outfit_id : str
        Outfit name. [Text in brackets]. Used with name to get unique skill
    score : int
        Score of the Uma. Used for Identification
    stats : Dict[str, int]
        Each stat with coresponding name.
    aptitudes : Dict[Dict[]] # TODO: CHANGE
        Total Aptitudes of an Uma
    skills : List[str]
        Full List of skills. skills[0] is ALWAYS unique
    """

    # Variables

    # Identifiers
    name: str  # Name in Plain Text
    outfit_id: str  # Outfit tagline
    score: int  # Score number

    # Stats
    stats: Dict[str, int] = {
        "speed": 1,
        "stamina": 1,
        "power": 1,
        "guts": 1,
        "wisdom": 1,
    }

    # Aptitudes
    aptitudes: Dict[str, Dict[str, LetterGrade]] = {
        "surface_aptitudes": {  # Ordered by uma-skill-tools
            "Turf": LetterGrade("G"),
            "Dirt": LetterGrade("G"),
        },
        "distance_aptitudes": {
            "Sprint": LetterGrade("G"),
            "Mile": LetterGrade("G"),
            "Medium": LetterGrade("G"),
            "Long": LetterGrade("G"),
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

    ### Methods

    ## Setters for each parameter (allow chaining)

    # Name & Outit -> Requires changing Unique skill (first?)
    def set_name_n_outfit(self, name: str, outfit: str) -> Self:
        self.name = name
        self.outfit_id = outfit

        # TODO: Find Unique skill from uma-skill-tools

        return self

    # Score -> Could be Automatically set with calculation?

    def set_score(self, score: int) -> Self:
        self.score = score

        return self

    # Stats -> Either full dictionary or individual values?
    def set_stat(self, stats_dict: Dict[str, int] = {}, **stat) -> Self:
        if stats_dict != {}:  # Case of full dictionary input (input validate)
            pass

        if len(stat) != 0:  # Case of single key value pair (input validate)
            pass

        else:  # Case of neither? Log redundant call.
            pass

        return self

    # Aptitudes -> Requires full double stacked Dictionary. (Maybe work better with a class?)
    def set_aptitudes(self, aptitudes_dict: Dict = {}, **aptitude) -> Self:
        return self

    # Skills -> Needs somewhat advanced array handling. Somehow want to keep Inherited seperate?
    def add_skills(self, skills: List[str]) -> Self:  # Add skills to list
        return self

    def rem_skills(self, skills: List[str]) -> Self:  # Remove specific skills
        return self

    def set_skills(self, skills: List[str]) -> Self:  # Reset Skills to defined list
        return self

    # Getters for each parameter

    # toJson(), which takes in a Racecourse class
    # and outputs the aptitudes relating to it.
