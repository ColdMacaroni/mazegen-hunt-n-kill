##
# maze.py
# Wed 06 Oct 2021
# Takes a generated maze and turns into an image
# S

from PIL import Image, ImageDraw
from sys import argv

from hunt_and_kill import DIRS
import hunt_and_kill

CELL_SIZE = 10 if len(argv) < 3 else int(argv[2])
# Line thickness
STROKE = max(CELL_SIZE // 5, 1)

def draw_maze(maze_draw, maze, width, height, fg,
        start=(0xFA, 0x44, 0x44),
        end=(0x44, 0x44, 0xFA)):
    """
    Draws the maze! What did you expect?
    """
    # This function is just so useful
    maze_idx = lambda p: p[1] * width + p[0]

    # Draw the colour squares at tl and br. -STROKE for aesthetic purposes
    # start
    # needs an extra pixel when stroke != 1
    maze_draw.rectangle((CELL_SIZE + STROKE + bool(STROKE - 1), CELL_SIZE + STROKE + bool(STROKE - 1),
                         CELL_SIZE*2 -STROKE, CELL_SIZE*2 -STROKE), fill=start)

    # end
    maze_draw.rectangle((width * CELL_SIZE +STROKE, height * CELL_SIZE +STROKE,
                         (width + 1) * CELL_SIZE -STROKE, (height + 1) * CELL_SIZE -STROKE), fill=end)

    # No need to draw borders, those are always blocked
    # Start drawin the stuff. Shift all by one to make use of the padding
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            # Have to -1 due to the shift
            point = maze[maze_idx((x - 1, y - 1))]

            # The and at the end of each condition creates the exits
            # -- NORTH
            if not (point & DIRS["N"]):
                maze_draw.line(
                        (
                            x      * CELL_SIZE, y * CELL_SIZE,
                            (x + 1) * CELL_SIZE, y * CELL_SIZE
                        ),
                        fill=fg,
                        width=STROKE)

            # -- EAST
            if not (point & DIRS["E"]):
                maze_draw.line(
                        (
                            (x + 1) * CELL_SIZE,  y      * CELL_SIZE,
                            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE
                        ),
                        fill=fg,
                        width=STROKE)

            # -- SOUTH
            if not (point & DIRS["S"]):
                maze_draw.line(
                        (
                             x      * CELL_SIZE, (y + 1) * CELL_SIZE,
                            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE
                        ),
                        fill=fg,
                        width=STROKE)

            # -- WEST
            if not (point & DIRS["W"]):
                maze_draw.line(
                        (
                            x * CELL_SIZE,  y      * CELL_SIZE,
                            x * CELL_SIZE, (y + 1) * CELL_SIZE
                        ),
                        fill=fg,
                        width=STROKE)



def main(width = 10, height = 10, *args):
    """
    Display a maze generated by the hunt and kill algorithm
    """
    BG = (0xF0, 0xF4, 0xEE)
    FG = (0x3C, 0x3C, 0x4C)

    # Plain image. With padding and extra STROKE so its even on all sides
    maze_img = Image.new('RGB', (width * CELL_SIZE + CELL_SIZE*2 + STROKE,
                                 height * CELL_SIZE + CELL_SIZE*2 + STROKE), BG)

    # Maze in list form
    maze = hunt_and_kill.gen_maze(width, height)

    draw_maze(ImageDraw.Draw(maze_img), maze, width, height, FG)


    maze_img.show()
    if input("Save? [Y/n]: ").strip().lower() not in ["n", "no"]:
        filename = f"mazes/maze_{width}x{height}-{CELL_SIZE}.png"
        maze_img.save(filename)
        print(f"Image saved as {filename}!")



if __name__ == "__main__":
    # Send in cli args to size
    if len(argv) > 1:
        main(*map(int, argv[1].split('x')))
    else:
        main()
