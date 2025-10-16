"""
UmaTournament written by Turtle.ca with libraries [uma-skill-tools] and [umamusume-ocr]
Liscenced under GNU V.3

This Program takes in the .csv (from or adjusted) [umamusume-ocr] and pits automatic comparisons
in a round robin style bracket for CM &/or Teams Trials.
"""

import base64
import csv
import gzip
import json
import logging
import os
import re
import subprocess
import sys
import threading
import tkinter as tk
import urllib.parse
from typing import Callable, Dict, List

from rapidfuzz import fuzz, process

import Racecourse as rc
import Uma as um


def create_match(uma_1: um.Uma, uma_2: um.Uma, track: rc.RaceCourse) -> Dict[str, int]:
    pass


def read_csv(filepath: str) -> List[Uma]:
    pass


def trournament_teamstrials(distance: str) -> List[Uma]:
    pass


def tournament_CM(conditions) -> List[Uma]:
    pass


def main(**args):
    pass


if __name__ == "__main__":
    main()
