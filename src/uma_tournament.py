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

import racecourse as rc
import uma

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


def read_csv(filepath: str) -> List[uma.Uma]:
    pass


def trournament_teamstrials(distance: str) -> List[uma.Uma]:
    pass


def tournament_CM(conditions) -> List[uma.Uma]:
    pass


def create_match(
    uma_1: uma.Uma, uma_2: uma.Uma, track: rc.RaceCourse
) -> Dict[str, int]:
    pass


def main(**args):

    mqueen = uma.Uma(
        "Mejiro Mqueen",
        "[idk]",
        200,
        [100, 100, 100, 100, 100],
        "Nige",
        [],
        ["A", "A", "A"],
    )
    print(mqueen)


if __name__ == "__main__":
    main()
