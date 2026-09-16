class Fruit:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.locations = []
        self.char = "."

    def render(self):
        for fruit in self.locations:
            self.stdscr.addstr(fruit[1], fruit[0], self.char)

    def eat(self, pos) -> bool:
        if pos in self.locations:
            self.locations.remove(pos)
            return True
        return False
