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

    def check_neighbours(pt, visited=False) -> list[tuple[int, int]]:
        """
        Returns a list of possible neighbours.
        Can pass arg to only count visited neighbours
        """
        # Points will be added to this list if they havent been traversed yet
        possible_points = dict()

        # -- NORTH
        p_pt = north(pt)
        # This mess of a condition will evaluate to true if the cell is visited and the user is asking for a visited cell. Viceversa.
        if pt[1] > 0 and (bool(maze[maze_idx(p_pt)]) == (False or visited)):
            possible_points[p_pt] = "N"

        # -- EAST
        p_pt = east(pt)
        if pt[0] < width - 1 and (bool(maze[maze_idx(p_pt)]) == (False or visited)):
            possible_points[p_pt] = "E"

        # -- SOUTH
        p_pt = south(pt)
        if pt[1] < height - 1 and (bool(maze[maze_idx(p_pt)]) == (False or visited)):
            possible_points[p_pt] = "S"

        # -- WEST
        p_pt = west(pt)
        if pt[0] > 0 and (bool(maze[maze_idx(p_pt)]) == (False or visited)):
            possible_points[p_pt] = "W"

        return possible_points

    # First, connect to a random neighbour that has been visited.
    starting_n = check_neighbours(start, True)
    if starting_n:
        neigh, dire = random.choice(tuple(starting_n.items()))

        maze[maze_idx(neigh)] |= DIRS[O_DIRS[dire]]
        maze[maze_idx(start)] |= DIRS[dire]

    step = start

    # Walk randomly until out of options
    while possible_n := check_neighbours(step):
        next_step, direction = random.choice(tuple(possible_n.items()))

        # Connect the two cells
        maze[maze_idx(step)] |= DIRS[direction]
        maze[maze_idx(next_step)] |= DIRS[O_DIRS[direction]]

        # Go to next
        step = next_step



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
    main()
