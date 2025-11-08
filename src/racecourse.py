"""
Race course Parameters class
"""

from enum import Enum

# TODO:
# - Store the course parameters for a specific race
# - check the course id based on name and distance
# - export in a bash readable way


class RaceCourse:

    def __init__(
        self, track: str, distance: int, weather: str, ground: str, season: str
    ):
        self.track = track
        self.distance = int(distance)
        self.weather = weather
        self.ground = ground
        self.season = season

    def set_track(self):
        pass
