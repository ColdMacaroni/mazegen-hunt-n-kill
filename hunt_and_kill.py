##
# hunt_and_kill.py
# 05 Oct 2021
# Generates a maze using the hunt and kill algorithm
# S
from sys import argv
from enum import Enum
import random

# Cardinal directions, can be OR'd and AND'd
DIRS = {
        'N': 1 << 0,
        'E': 1 << 1,
        'S': 1 << 2,
        'W': 1 << 3
}

def gen_maze(width: int, height: int):
    ...


def main():
    ...

if __name__ == "__main__":
    main()
