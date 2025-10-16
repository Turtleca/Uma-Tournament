"""
UmaTournament written by Turtle.ca with libraries [uma-skill-tools] and [umamusume-ocr]
Liscenced under GNU V.3

This Program takes in the .csv (from or adjusted) [umamusume-ocr] and pits automatic comparisons
in a round robin style bracket for CM &/or Teams Trials.
"""

import csv
import gzip
import json
from typing import Dict, List

import Racecourse as rc
import Uma as um

###
# 1. Load the custom ~ish csv into a list of Uma classes
# 2. Run either
#     - Teams Trials
#         - Get matches on several races of the same dist
#         - Randomize conditions and(?) mood(?)
#     - Champions meeting
#         - Run all matches on one singular condition
# 3. Export data ranked by largest winrate/teams-trials score
#


def read_csv(filepath: str) -> List[Uma]:
    pass


def trournament_teamstrials(distance: str) -> List[Uma]:
    pass


def tournament_CM(conditions) -> List[Uma]:
    pass


def create_match(uma_1: um.Uma, uma_2: um.Uma, track: rc.RaceCourse) -> Dict[str, int]:
    pass


def main(**args):
    pass


if __name__ == "__main__":
    main()
