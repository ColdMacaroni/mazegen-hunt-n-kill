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

O_DIRS = {
        'N': 'S',
        'E': 'W',
        'S': 'N',
        'W': 'E'
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

    # Shortcut funcs for surrounding points
    north   = lambda p: (p[0]   , p[1] -1)
    east    = lambda p: (p[0] +1, p[1]   )
    south   = lambda p: (p[0]   , p[1] +1)
    west    = lambda p: (p[0] -1, p[1]   )

    def check_neighbours(pt) -> list[tuple[int, int]]:
        """
        Returns a list of possible neighbours.
        """
        # Points will be added to this list if they havent been traversed yet
        possible_points = dict()

        # -- NORTH
        p_pt = north(pt)
        if pt[1] > 0 and maze[maze_idx(p_pt)] == 0:
            possible_points[p_pt] = "N"

        # -- EAST
        p_pt = east(pt)
        if pt[0] < width - 1 and maze[maze_idx(p_pt)] == 0:
            possible_points[p_pt] = "S"

        # -- SOUTH
        p_pt = south(pt)
        if pt[1] < height - 1 and maze[maze_idx(p_pt)] == 0:
            possible_points[p_pt] = "S"

        # -- WEST
        p_pt = west(pt)
        if pt[0] > 0 and maze[maze_idx(p_pt)] == 0:
            possible_points[p_pt] = "W"

        return possible_points

    # First, connect to a random neighbour, if there is one.
    starting_n = check_neighbours(start)
    if starting_n:
        n = random.choice(tuple(starting_n.keys()))
        maze[maze_idx(n)] |= DIRS[O_DIRS[starting_n[n]]]


def gen_maze(width: int, height: int) -> list[int]:
    maze = init_maze(width, height)

    maze_idx = lambda p: p[1] * width + p[0]
    for y in range(height):
        for x in range(width):
            if not maze[maze_idx((x, y))]:
                walk_maze(maze, width, height, (x, y))

    return maze

def print_maze(maze: list[int], width: int, height: int) -> None:
    """
    Print an ASCII maze!!!! Maybe works??
    """
    maze_idx = lambda p: p[1] * width + p[0]

    # top row
    print(' ' + '_' * (2 * width - 1))

    for y in range(height):
        for x in range(width):
            # left wall
            if maze[maze_idx((x, y))] & DIRS["W"]:
                # leave wall open if you can also go down
                if maze[maze_idx((x, y))] & DIRS["S"]:
                    print(' ', end='')
                else:
                    print('_', end='')

            else:
                print('|', end='')

            if maze[maze_idx((x, y))] & DIRS["S"]:
                print(' ', end='')
            else:
                print('_', end='')
        # right wall
        print('|')

def main():
    width = height = 10
    if len(argv) > 2:
        width = int(argv[1])
        height = int(argv[2])

    print(f"Generating maze size {width}x{height}")
    maze = gen_maze(width, height)
    print_maze(maze, width, height)
    return maze


if __name__ == "__main__":
    print(main())
