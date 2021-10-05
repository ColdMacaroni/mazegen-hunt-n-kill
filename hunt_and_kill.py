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


def init_maze(width: int, height: int) -> list[int]:
    """
    Set up a 2D list with 0 as starting value. Basically an empty maze
    """
    return [0] * width * height


def walk_maze(maze: list[int], width: int, height: int, start: tuple[int, int]) -> None:
    """
    Does a random walk, setting the cells as it goes, until it cant find a
    path.
    """
    def check_neightbours(pt) -> list[tuple[int, int]]:
        """
        Returns a list of possible neighbours.
        """
        possible_points = list()
        # -- NORTH
        # Will skip if on the first row
        if pt[0] != 0 and maze[(pt[0] - 1) * width + pt[1]] == 0:


        # -- EAST
        # -- SOUTH
        # -- WEST


def gen_maze(width: int, height: int) -> list[int]:
    maze = init_maze(width, height)
    for y in range(height):
        for x in range(width):
            if not maze[y * width + x]:
                walk_maze(maze, width, height, (x, y))

    return maze

def main():
    width = height = 10
    if len(argv) > 2:
        width = int(argv[1])
        height = int(argv[2])

    print(f"Generating maze size {width}x{height}")
    maze = gen_maze(width, height)
    return maze


if __name__ == "__main__":
    print(main())
