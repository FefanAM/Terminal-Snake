import time
import keyboard
import random
from math import sqrt
from rich.console import Console
import os
from assets import menu_screen

running = True
width = 60
height = 60
speed = 1
fruit_count = 25
facing = 'east'
new_tile_x = 0
new_tile_y = 0
y_count = 0
previous_time = time.time()
game_contents = [[], []]  # stores all objects currently in game -- used for rendering -- list 0 is player -- list 1 is fruits
current_row = []
in_menu = True
console = Console()
can_change_dir = True
score = 0


class GameObject:
    def __init__(self, name, pos_x, pos_y, char):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.char = char


def print_row(current_y):
    # loop through every object in game contents and add them to currently printed row
    global current_row
    current_row.clear()
    for x in range(width - 2):
        current_row.append(" ")
    for group in game_contents:
        for item in group:
            if item.pos_y // 1 == current_y:
                current_row.pop(int(item.pos_x // 1))
                current_row.insert(int(item.pos_x // 1), item.char)


def new_frame() -> str:
    # print a new frame in terminal
    this_frame = ""
    for x in range(height):
        if x == 0:
            this_frame = this_frame + f'[green]┏{ "━" * (width - 2)}┓[/green] {score}\n'
        elif x == height - 1:
            this_frame = this_frame + f'[green]┗{ "━" * (width - 2)}┛[/green]'
        else:
            print_row(x)
            this_frame = this_frame + f'[green]┃[/green]{"".join(map(str, current_row))}[green]┃[/green]\n'
    return this_frame


def set_facing_dir():
    global facing
    if can_change_dir:
        if (keyboard.is_pressed('w') or keyboard.is_pressed('up arrow')) and facing != 'south':
            facing = 'north'
            return False
        elif (keyboard.is_pressed('s') or keyboard.is_pressed('down arrow')) and facing != 'north':
            facing = 'south'
            return False
        elif (keyboard.is_pressed('a') or keyboard.is_pressed('left arrow')) and facing != 'east':
            facing = 'west'
            return False
        elif (keyboard.is_pressed('d') or keyboard.is_pressed('right arrow')) and facing != 'west':
            facing = 'east'
            return False
        else:
            return True
    else:
        return False


def move_player():
    # set the facing direction via key input
    global in_menu
    global new_tile_x
    global new_tile_y
    global previous_time
    global can_change_dir
    can_change_dir = set_facing_dir()
    # move all other snake parts
    new_tile_x = game_contents[0][len(game_contents[0]) - 1].pos_x
    new_tile_y = game_contents[0][len(game_contents[0]) - 1].pos_y
    if time.time() - previous_time >= 0.08:
        for tile in range(len(game_contents[0]) - 1):
            tile = len(game_contents[0]) - 1 - tile
            if tile == 0:
                continue
            else:
                game_contents[0][tile].pos_x = game_contents[0][tile - 1].pos_x
                game_contents[0][tile].pos_y = game_contents[0][tile - 1].pos_y
        # move the player in right direction
        if facing == 'north':
            game_contents[0][0].pos_y -= speed
        if facing == 'south':
            game_contents[0][0].pos_y += speed
        if facing == 'west':
            game_contents[0][0].pos_x -= speed
        if facing == 'east':
            game_contents[0][0].pos_x += speed
        can_change_dir = True
        # make sure player cannot get out of bound
        if game_contents[0][0].pos_x > width - 3 or game_contents[0][0].pos_x < 0 or game_contents[0][0].pos_y > height - 2 or game_contents[0][0].pos_y < 1:
            in_menu = True
            reset()
            with open('leaderboard.txt', 'a') as file:
                file.write(get_player_highscore())
        previous_time = time.time()


def place_fruits():
    # if number of fruits is less than is set, add a new fruit
    while len(game_contents[1]) < fruit_count:
        game_contents[1].append(GameObject('fruit', random.randrange(0, width - 2), random.randrange(1, height - 2), '[on red] [/on red]'))


def get_player_highscore():
    os.system('cls')
    print(f'Your score is: {score}')
    highscore = f'{input('Enter your nickname:')};{score}\n'
    return highscore


def eat_fruit():
    global score
    for fruit in game_contents[1]:
        if fruit.pos_y == game_contents[0][0].pos_y // 1 and fruit.pos_x == game_contents[0][0].pos_x // 1:
            del game_contents[1][game_contents[1].index(fruit)]
            game_contents[0].append(GameObject('player', new_tile_x, new_tile_y, '█'))
            score += 1


def reset():
    global facing
    global game_contents
    game_contents = [[], []]
    game_contents[0].append(GameObject('player', width // 2, height // 2, '█'))
    facing = 'east'
    row_size = int(sqrt(fruit_count) // 1)
    for y in range(row_size):
        for x in range(row_size):
            game_contents[1].append(GameObject('fruit', (width * 2) // 3 + x, height // 2 - row_size + y, '[on red] [/on red]'))


reset()

if not os.path.exists('leaderboard.txt'):
    with open('leaderboard.txt', 'w') as file:
        pass

while running:
    while in_menu:
        os.system('cls')
        print(menu_screen)
        console.print(int((width / 2) - 10) * ' ' + 'Press enter to start', style='blink')
        input()
        in_menu = False
    place_fruits()
    console.print(new_frame())
    move_player()
    eat_fruit()
