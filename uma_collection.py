import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Skill:
    """Represents a skill with its level."""
    skill_id: int
    level: int


@dataclass
class SupportCard:
    """Represents an equipped support card."""
    position: int
    support_card_id: int
    exp: int
    limit_break_count: int


@dataclass
class RaceResult:
    """Represents a race result."""
    turn: int
    program_id: int
    weather: int
    ground_condition: int
    running_style: int
    popularity: int
    result_rank: int
    result_time: int
    prize_money: int


@dataclass
class SuccessionCharaInfo:
    """Represents information about a succession character."""
    position_id: int
    card_id: int
    rank: int
    rarity: int
    talent_level: int
    factor_id_array: List[int]
    factor_info_array: List[Dict[str, int]]
    win_saddle_id_array: List[int]
    owner_viewer_id: int


@dataclass
class Uma:
    """
    Represents an individual Uma (Umamusume character).
    This class encapsulates all data from a single Uma entry in data.json.
    """
    # Basic identification
    trained_chara_id: int
    owner_trained_chara_id: int
    single_mode_chara_id: int
    chara_seed: int
    card_id: int
    
    # Stats
    speed: int
    stamina: int
    power: int
    wiz: int  # wisdom
    guts: int
    
    # Performance metrics
    fans: int
    rank_score: int
    rank: int
    wins: int
    
    # Training info
    scenario_id: int
    route_id: int
    arrive_route_race_id: int
    running_style: int
    talent_level: int
    
    # Aptitudes (1-7 scale)
    proper_ground_turf: int
    proper_ground_dirt: int
    proper_running_style_nige: int
    proper_running_style_senko: int
    proper_running_style_sashi: int
    proper_running_style_oikomi: int
    proper_distance_short: int
    proper_distance_mile: int
    proper_distance_middle: int
    proper_distance_long: int
    
    # Character info
    chara_grade: int
    rarity: int
    nickname_id: int
    
    # Support & skills
    skills: List[Skill] = field(default_factory=list)
    support_card_list: List[SupportCard] = field(default_factory=list)
    
    # Race history
    race_result_list: List[RaceResult] = field(default_factory=list)
    win_saddle_id_array: List[int] = field(default_factory=list)
    nickname_id_array: List[int] = field(default_factory=list)
    
    # Factors & succession
    factor_id_array: List[int] = field(default_factory=list)
    factor_info_array: List[Dict[str, int]] = field(default_factory=list)
    succession_chara_array: List[SuccessionCharaInfo] = field(default_factory=list)
    succession_history_array: List[Dict[str, Any]] = field(default_factory=list)
    succession_trained_chara_id_1: Optional[int] = None
    succession_trained_chara_id_2: Optional[int] = None
    succession_num: int = 0
    
    # Status
    use_type: int = 0
    is_saved: int = 1
    is_locked: int = 1
    race_cloth_id: int = 101
    register_time: str = ""
    create_time: str = ""
    
    def get_total_stats(self) -> int:
        """Get the total of all base stats."""
        return self.speed + self.stamina + self.power + self.wiz + self.guts
    
    def get_aptitude_dict(self) -> Dict[str, int]:
        """Get all aptitudes as a dictionary."""
        return {
            'turf': self.proper_ground_turf,
            'dirt': self.proper_ground_dirt,
            'nige': self.proper_running_style_nige,
            'senko': self.proper_running_style_senko,
            'sashi': self.proper_running_style_sashi,
            'oikomi': self.proper_running_style_oikomi,
            'short': self.proper_distance_short,
            'mile': self.proper_distance_mile,
            'middle': self.proper_distance_middle,
            'long': self.proper_distance_long,
        }
    
    def __repr__(self) -> str:
        return (f"Uma(id={self.trained_chara_id}, card={self.card_id}, "
                f"stats={self.get_total_stats()}, rank={self.rank})")


class UmaCollection:
    """
    Manages a collection of Uma objects loaded from data.json.
    This is a flexible container for any number of Uma objects without specific team requirements.
    """
    
    def __init__(self, filepath: Optional[str] = None):
        """
        Initialize the UmaCollection.
        
        Args:
            filepath: Optional path to data.json file. If provided, loads immediately.
        """
        self.umas: List[Uma] = []
        self.filepath = filepath
        
        if filepath:
            self.load_from_file(filepath)
    
    def load_from_file(self, filepath: str) -> None:
        """
        Load Uma data from a JSON file.
        
        Args:
            filepath: Path to the data.json file
            
        Raises:
            FileNotFoundError: If the JSON file doesn't exist
            json.JSONDecodeError: If the JSON file is malformed
            ValueError: If required fields are missing from Uma data
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("data.json must contain a JSON array of Uma objects")
        
        self.umas = [self._create_uma_from_dict(uma_data) for uma_data in data]
    
    def _create_uma_from_dict(self, uma_data: Dict[str, Any]) -> Uma:
        """
        Create a Uma object from dictionary data.
        
        Args:
            uma_data: Dictionary containing Uma attributes from data.json
            
        Returns:
            Uma object
            
        Raises:
            ValueError: If required fields are missing
        """
        # Required fields validation
        required_fields = [
            'trained_chara_id', 'speed', 'stamina', 'power', 'wiz', 'guts',
            'rank', 'rank_score', 'running_style', 'card_id'
        ]
        
        missing_fields = [f for f in required_fields if f not in uma_data]
        if missing_fields:
            raise ValueError(f"Missing required fields in Uma data: {missing_fields}")
        
        # Parse skills
        skills = [
            Skill(skill_id=s['skill_id'], level=s['level'])
            for s in uma_data.get('skill_array', [])
        ]
        
        # Parse support cards
        support_cards = [
            SupportCard(
                position=sc['position'],
                support_card_id=sc['support_card_id'],
                exp=sc['exp'],
                limit_break_count=sc['limit_break_count']
            )
            for sc in uma_data.get('support_card_list', [])
        ]
        
        # Parse race results
        race_results = [
            RaceResult(
                turn=rr['turn'],
                program_id=rr['program_id'],
                weather=rr['weather'],
                ground_condition=rr['ground_condition'],
                running_style=rr['running_style'],
                popularity=rr['popularity'],
                result_rank=rr['result_rank'],
                result_time=rr['result_time'],
                prize_money=rr['prize_money']
            )
            for rr in uma_data.get('race_result_list', [])
        ]
        
        # Parse succession characters
        succession_charas = [
            SuccessionCharaInfo(
                position_id=sc['position_id'],
                card_id=sc['card_id'],
                rank=sc['rank'],
                rarity=sc['rarity'],
                talent_level=sc['talent_level'],
                factor_id_array=sc.get('factor_id_array', []),
                factor_info_array=sc.get('factor_info_array', []),
                win_saddle_id_array=sc.get('win_saddle_id_array', []),
                owner_viewer_id=sc.get('owner_viewer_id', 0)
            )
            for sc in uma_data.get('succession_chara_array', [])
        ]
        
        # Create Uma object
        uma = Uma(
            trained_chara_id=uma_data['trained_chara_id'],
            owner_trained_chara_id=uma_data.get('owner_trained_chara_id', 0),
            single_mode_chara_id=uma_data.get('single_mode_chara_id', 0),
            chara_seed=uma_data.get('chara_seed', 0),
            card_id=uma_data['card_id'],
            speed=uma_data['speed'],
            stamina=uma_data['stamina'],
            power=uma_data['power'],
            wiz=uma_data['wiz'],
            guts=uma_data['guts'],
            fans=uma_data.get('fans', 0),
            rank_score=uma_data.get('rank_score', 0),
            rank=uma_data['rank'],
            wins=uma_data.get('wins', 0),
            scenario_id=uma_data.get('scenario_id', 1),
            route_id=uma_data.get('route_id', 0),
            arrive_route_race_id=uma_data.get('arrive_route_race_id', 0),
            running_style=uma_data['running_style'],
            talent_level=uma_data.get('talent_level', 0),
            proper_ground_turf=uma_data.get('proper_ground_turf', 0),
            proper_ground_dirt=uma_data.get('proper_ground_dirt', 0),
            proper_running_style_nige=uma_data.get('proper_running_style_nige', 0),
            proper_running_style_senko=uma_data.get('proper_running_style_senko', 0),
            proper_running_style_sashi=uma_data.get('proper_running_style_sashi', 0),
            proper_running_style_oikomi=uma_data.get('proper_running_style_oikomi', 0),
            proper_distance_short=uma_data.get('proper_distance_short', 0),
            proper_distance_mile=uma_data.get('proper_distance_mile', 0),
            proper_distance_middle=uma_data.get('proper_distance_middle', 0),
            proper_distance_long=uma_data.get('proper_distance_long', 0),
            chara_grade=uma_data.get('chara_grade', 0),
            rarity=uma_data.get('rarity', 0),
            nickname_id=uma_data.get('nickname_id', 0),
            skills=skills,
            support_card_list=support_cards,
            race_result_list=race_results,
            win_saddle_id_array=uma_data.get('win_saddle_id_array', []),
            nickname_id_array=uma_data.get('nickname_id_array', []),
            factor_id_array=uma_data.get('factor_id_array', []),
            factor_info_array=uma_data.get('factor_info_array', []),
            succession_chara_array=succession_charas,
            succession_history_array=uma_data.get('succession_history_array', []),
            succession_trained_chara_id_1=uma_data.get('succession_trained_chara_id_1'),
            succession_trained_chara_id_2=uma_data.get('succession_trained_chara_id_2'),
            succession_num=uma_data.get('succession_num', 0),
            use_type=uma_data.get('use_type', 0),
            is_saved=uma_data.get('is_saved', 1),
            is_locked=uma_data.get('is_locked', 1),
            race_cloth_id=uma_data.get('race_cloth_id', 101),
            register_time=uma_data.get('register_time', ''),
            create_time=uma_data.get('create_time', ''),
        )
        
        return uma
    
    # Collection management methods
    
    def add_uma(self, uma: Uma) -> None:
        """Add a single Uma to the collection."""
        self.umas.append(uma)
    
    def remove_uma(self, trained_chara_id: int) -> bool:
        """
        Remove a Uma from the collection by trained_chara_id.
        
        Returns:
            True if Uma was found and removed, False otherwise
        """
        original_count = len(self.umas)
        self.umas = [u for u in self.umas if u.trained_chara_id != trained_chara_id]
        return len(self.umas) < original_count
    
    def get_all(self) -> List[Uma]:
        """Get all Umas in the collection."""
        return self.umas.copy()
    
    def get_by_id(self, trained_chara_id: int) -> Optional[Uma]:
        """Get a specific Uma by trained_chara_id."""
        for uma in self.umas:
            if uma.trained_chara_id == trained_chara_id:
                return uma
        return None
    
    def get_by_card_id(self, card_id: int) -> List[Uma]:
        """Get all Umas with a specific card_id."""
        return [u for u in self.umas if u.card_id == card_id]
    
    def get_count(self) -> int:
        """Get the total number of Umas in the collection."""
        return len(self.umas)
    
    # Filtering methods
    
    def filter_by_rank(self, min_rank: Optional[int] = None, max_rank: Optional[int] = None) -> List[Uma]:
        """
        Filter Umas by rank range.
        
        Args:
            min_rank: Minimum rank (inclusive)
            max_rank: Maximum rank (inclusive)
        """
        result = self.umas
        if min_rank is not None:
            result = [u for u in result if u.rank >= min_rank]
        if max_rank is not None:
            result = [u for u in result if u.rank <= max_rank]
        return result
    
    def filter_by_rarity(self, rarity: int) -> List[Uma]:
        """Get all Umas with a specific rarity."""
        return [u for u in self.umas if u.rarity == rarity]
    
    def filter_by_running_style(self, running_style: int) -> List[Uma]:
        """Get all Umas with a specific running style."""
        return [u for u in self.umas if u.running_style == running_style]
    
    def filter_by_min_total_stats(self, min_stats: int) -> List[Uma]:
        """Get all Umas with at least the specified total stats."""
        return [u for u in self.umas if u.get_total_stats() >= min_stats]
    
    def filter_locked(self, locked: bool = True) -> List[Uma]:
        """Get all locked or unlocked Umas."""
        return [u for u in self.umas if (u.is_locked == 1) == locked]
    
    # Statistics methods
    
    def get_average_stats(self) -> Dict[str, float]:
        """Calculate average stats across all Umas."""
        if not self.umas:
            return {}
        
        count = len(self.umas)
        return {
            'avg_speed': sum(u.speed for u in self.umas) / count,
            'avg_stamina': sum(u.stamina for u in self.umas) / count,
            'avg_power': sum(u.power for u in self.umas) / count,
            'avg_wisdom': sum(u.wiz for u in self.umas) / count,
            'avg_guts': sum(u.guts for u in self.umas) / count,
            'avg_total': sum(u.get_total_stats() for u in self.umas) / count,
        }
    
    def get_top_umas(self, n: int = 10, sort_by: str = 'rank_score') -> List[Uma]:
        """
        Get top N Umas sorted by a specific attribute.
        
        Args:
            n: Number of Umas to return
            sort_by: Attribute to sort by ('rank_score', 'rank', 'total_stats', 'fans')
        """
        if sort_by == 'total_stats':
            sorted_umas = sorted(self.umas, key=lambda u: u.get_total_stats(), reverse=True)
        elif sort_by == 'rank':
            sorted_umas = sorted(self.umas, key=lambda u: u.rank, reverse=True)
        elif sort_by == 'fans':
            sorted_umas = sorted(self.umas, key=lambda u: u.fans, reverse=True)
        else:  # rank_score
            sorted_umas = sorted(self.umas, key=lambda u: u.rank_score, reverse=True)
        
        return sorted_umas[:n]


# Example usage
if __name__ == "__main__":
    # Load collection from file
    collection = UmaCollection("umas/data.json")
    
    print(f"Total Umas: {collection.get_count()}")
    print(f"\nTop 5 by Rank Score:")
    for uma in collection.get_top_umas(5, 'rank_score'):
        print(f"  {uma}")
    
    print(f"\nAverage Stats:")
    stats = collection.get_average_stats()
    for stat, value in stats.items():
        print(f"  {stat}: {value:.0f}")
    
    print(f"\nLocked Umas: {len(collection.filter_locked(locked=True))}")
