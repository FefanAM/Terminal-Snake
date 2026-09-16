import curses
import time
from assets import menu_screen
from player import Player
from fruit import Fruit


def main(stdscr):
    game_state = "START"

    stdscr.nodelay(True)
    curses.use_default_colors()
    curses.curs_set(0)

    stdscr.clear()

    snake = Player(stdscr)
    fruits = Fruit(stdscr)
    direction = "right"

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "q":
            break
        elif key in ["\n", "\r", "KEY_ENTER"]:
            game_state = "PLAYING"
            stdscr.clear()
        elif key == "g":
            snake.grow()
        elif key == "w":
            direction = "up"
        elif key == "s":
            direction = "down"
        elif key == "a":
            direction = "left"
        elif key == "d":
            direction = "right"

        if game_state == "START":
            stdscr.addstr(0, 0, menu_screen)
            stdscr.addstr(12, 20, "PRESS ENTER TO START", curses.A_BLINK)

        elif game_state == "PLAYING":
            snake.move(direction)
            snake.render()

        stdscr.refresh()

        time.sleep(0.015)


curses.wrapper(main)
