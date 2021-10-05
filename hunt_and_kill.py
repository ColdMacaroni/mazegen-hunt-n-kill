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
    # Shortcut for accessing maze
    maze_idx = lambda p: p[1] * width + p[0]

    def check_neighbours(pt) -> list[tuple[int, int]]:
        """
        Returns a list of possible neighbours.
        """
        # Shortcut funcs for surrounding points
        north   = lambda p: (p[0]   , p[1] -1)
        east    = lambda p: (p[0] +1, p[1]   )
        south   = lambda p: (p[0]   , p[1] +1)
        west    = lambda p: (p[0] -1, p[1]   )

        # Points will be added to this list if they havent been traversed yet
        possible_points = list()

        # -- NORTH
        p_pt = north(pt)
        if pt[1] > 0 and maze[maze_idx(p_pt)] == 0:
            possible_points.append(p_pt)

        # -- EAST
        p_pt = east(pt)
        if pt[0] < width - 1 and maze[maze_idx(p_pt)] == 0:
            possible_points.append(p_pt)

        # -- SOUTH
        p_pt = south(pt)
        if pt[1] < height - 1 and maze[maze_idx(p_pt)] == 0:
            possible_points.append(p_pt)

        # -- WEST
        p_pt = west(pt)
        if pt[0] > 0 and maze[maze_idx(p_pt)] == 0:
            possible_points.append(p_pt)

        return possible_points

    check_neighbours(start)


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
