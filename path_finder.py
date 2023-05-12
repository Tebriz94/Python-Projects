import curses
from curses import wrapper
import queue
import time


maze = [
    
    ["#","#","#","#","#","O","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#"," ","#","#"," ","#","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","X","#"]

]



def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):

            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"

    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, column = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][column] == end:
            return path
        
        neighbors = find_neighbors(maze, row, column)

        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, column):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, column))
    if row + 1 < len(maze): #Down
        neighbors.append((row + 1, column))
    if column > 0: #Left
        neighbors.append((row, column - 1))
    if column + 1 < len[maze[0]]: #Right
        neighbors.append((row, column + 1))





def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()
    #blue_and_black = curses.color_pair(1)
    #stdscr.clear()
    #print_maze(maze, stdscr)
    #stdscr.addstr(0, 0, "Hello World",)
    #stdscr.refresh()
    #stdscr.getch()

wrapper(main)
