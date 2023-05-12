import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(10,20,"Hello World",curses.A_UNDERLINE) #with this func we can add string content with 2 parameters we can define row and column
    stdscr.addstr(10,30,"DevOps Engineer",curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)


