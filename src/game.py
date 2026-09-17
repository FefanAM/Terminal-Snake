import curses
import time
from assets import menu_screen
from player import Player
from fruit import Fruit
from screen import Screen


def main(stdscr):
    game_state = "START"

    stdscr.nodelay(True)
    curses.use_default_colors()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)

    stdscr.clear()

    snake = Player(stdscr)
    fruits = Fruit(stdscr)
    screen = Screen(stdscr)

    direction = "right"
    game_speed = 10
    prev_time = 0

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
        elif key == "w" and direction != "down":
            direction = "up"
        elif key == "s" and direction != "up":
            direction = "down"
        elif key == "a" and direction != "right":
            direction = "left"
        elif key == "d" and direction != "left":
            direction = "right"

        if game_state == "START":
            stdscr.addstr(0, 0, menu_screen)
            stdscr.addstr(12, 20, "PRESS ENTER TO START", curses.A_BLINK)

        elif game_state == "PLAYING":
            screen.render_border()
            if time.time() - prev_time >= 1 / game_speed:
                snake.move(direction)
                fruits.render()
                snake.render()
                prev_time = time.time()

        stdscr.refresh()

        time.sleep(0.015)


curses.wrapper(main)
