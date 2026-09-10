import curses
import time
from assets import menu_screen

def main(stdscr):
    game_state = "START"

    stdscr.nodelay(True)
    curses.use_default_colors()
    curses.curs_set(0)

    stdscr.clear()

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == 'q':
            break
        elif key in ["\n", "\r", "KEY_ENTER"]:
            game_state = "PLAYING"

        if game_state == "START":
            stdscr.addstr(0, 0, menu_screen)
            stdscr.addstr(12, 20, "PRESS ENTER TO START", curses.A_BLINK)

        stdscr.refresh()

        time.sleep(0.015)

curses.wrapper(main)
