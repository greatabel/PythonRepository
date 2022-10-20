import turtle  # import turtle library
import time
import sys
from collections import deque

from i0common import *

wn = turtle.Screen()  # define the turtle screen
wn.bgcolor("black")  # set the background colour
wn.title("Fractal Maze Generetor")
wn.setup(700, 700)  # setup the dimensions of the working window


grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                # change here to change 'empty space color'
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        time.sleep(0)
        x, y = frontier.popleft()

        if (x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y

            frontier.append(cell)
            visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):  # stop loop when current cells == start cell
        yellow.goto(
            solution[x, y]
        )  # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]  # "key value" now becomes the new key


# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}


# main program starts here ####
setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
