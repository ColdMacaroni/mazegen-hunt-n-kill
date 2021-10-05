##
# pygame_maze.py
# Wed 06 Oct 2021
# Takes a generated maze and puts it in pygame
# S
import pygame
from sys import argv

from hunt_and_kill import DIRS
import hunt_and_kill

CELL_SIZE = 10 if len(argv) < 3 else int(argv[2])

def draw_maze(screen, maze, width, height, fg,
        start=pygame.Color(0xFA4444FF),
        end=pygame.Color(0x4444FAFF)):
    """
    Draws the maze! What did you expect?
    """
    # Line thickness
    STROKE = CELL_SIZE // 5

    # This function is just so useful
    maze_idx = lambda p: p[1] * width + p[0]

    # start
    pygame.draw.rect(screen, start, (CELL_SIZE, CELL_SIZE,
                                     CELL_SIZE, CELL_SIZE))
    # end
    pygame.draw.rect(screen, end, (width * CELL_SIZE, height * CELL_SIZE,
                                     CELL_SIZE, CELL_SIZE))

    # No need to draw borders, those are always blocked
    # Start drawin the stuff. Shift all by one to make use of the padding
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            # Have to -1 due to the shift
            point = maze[maze_idx((x - 1, y - 1))]

            # The and at the end of each condition creates the exits
            # -- NORTH
            if not (point & DIRS["N"]):
                pygame.draw.line(screen, fg,
                        (x * CELL_SIZE, y * CELL_SIZE),
                        ((x + 1) * CELL_SIZE, y * CELL_SIZE),
                        STROKE)

            # -- EAST
            if not (point & DIRS["E"]):
                pygame.draw.line(screen, fg,
                        ((x + 1) * CELL_SIZE, y * CELL_SIZE),
                        ((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE),
                        STROKE)

            # -- SOUTH
            if not (point & DIRS["S"]):
                pygame.draw.line(screen, fg,
                        (x * CELL_SIZE, y * CELL_SIZE + CELL_SIZE), 
                        ((x + 1) * CELL_SIZE, (y + 1 ) * CELL_SIZE),
                        STROKE)

            # -- WEST
            if not (point & DIRS["W"]):
                pygame.draw.line(screen, fg,
                        (x * CELL_SIZE, y * CELL_SIZE), 
                        (x * CELL_SIZE, (y + 1) * CELL_SIZE),
                        STROKE)




def main(width = 10, height = 10, *args):
    """
    Display a maze generated by the hunt and kill algorithm
    """
    BG = pygame.Color(0xF0F4EEFF)
    FG = pygame.Color(0x3C3C4CFF)

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width * CELL_SIZE + CELL_SIZE*2, height * CELL_SIZE + CELL_SIZE*2))

    maze = hunt_and_kill.gen_maze(width, height)

    running = True
    while running:
        screen.fill(BG)

        draw_maze(screen, maze, width, height, FG)

        pygame.display.flip()

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    filename = f"mazes/maze_{width}x{height}-{CELL_SIZE}.png"
    pygame.image.save(screen, filename)
    print(f"Image saved as {filename}!")

    pygame.quit()


if __name__ == "__main__":
    # Send in cli args to size
    if len(argv) > 1:
        main(*map(int, argv[1].split('x')))
    else:
        main()
