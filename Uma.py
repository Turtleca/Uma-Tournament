"""
Uma Class file
"""


class Uma:
    """
    An Uma Object.
    Descrbes the entirety of one Uma.

    # Attributes
    ----------

    ### Identifiers
    name : str
    outfit_id : str
    score : int
    ### Stats
    speed : int
    stamina : int
    power : int
    guts : int
    wisdom : int
    strategy : str
    ### Skills
    skills : List[str]
    ### Aptitudes
    distance_aptitude : str
    surface_aptitude : str
    strategy_aptitude : str

    # Initialization
    ----------
    Initialize with the following parameters:

    name : str
    The name of the Uma
    outfit : str
    The Uma's Outfit tagline
    i.e. [Frontline Elegance]
    score : int
    The Uma's Calculated Score
    stats : List[int]
    List of Stats.
    [speed, stamina, power, guts, wit]
    op_strategy : str
    optimal strategy
    "Front", "Pace", "Late", or "End"
    skills : List[str]
    List of the skill names separated by '|'
    aptitudes : List[str]
    Aptitude Characters
    [Surface, Distance, Strategy]
    """

    # Identifiers
    name: str
    outfit_id: str
    score: int

    # Stats
    speed: int
    stamina: int
    power: int
    guts: int
    wisdom: int

    # Strategy
    strategy: str

    # Skills list (Skill Names)
    skills: List[str]

    # Aptitudes
    distance_aptitude: str
    surface_aptitude: str
    strategy_aptitude: str

    def __init__(
        self,
        name: str,
        outfit: str,
        score: int,
        stats: List,
        op_strategy: str,
        skills: List,
        aptitudes: List,
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
        self.name = name
        self.outfit_id = outfit
        self.score = score
        self.speed, self.stamina, self.power, self.guts, self.wit = stats
        self.strategy = op_strategy
        self.skills = skills
        self.surface_aptitude, self.distance_aptitude, self.strategy_aptitude = (
            aptitudes
        )

    def map_style(self) -> str:
        style_dict = {
            "Front": "Nige",
            "Pace": "Senjour",
            "Late": "Sasi",
            "End": "Oikomi",
        }

        return style_dict[self.strategy]

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
            "distanceAptitude": self.distance_aptitude,
            "surfaceAptitude": self.surface_aptitude,
            "strategyAptitude": self.strategy_aptitude,
            "skills": self.skills,
        }
