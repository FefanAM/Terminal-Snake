class Player:
    def __init__(self, stdscr) -> None:
        self.body: list = [[0, 0]]
        self.stdscr = stdscr
        self.char: str = "#"
        self.end = None

    def render(self):
        for tile in self.body:
            self.stdscr.addstr(tile[1], tile[0], self.char)
        self.stdscr.addstr(self.body[0][1], self.body[0][0], "O")
        if self.end is not None:
            self.stdscr.addstr(self.end[1], self.end[0], " ")

    def move(self, direction):
        if direction == "up":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - 1])
        elif direction == "down":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + 1])
        elif direction == "left":
            self.body.insert(0, [self.body[0][0] - 1, self.body[0][1]])
        elif direction == "right":
            self.body.insert(0, [self.body[0][0] + 1, self.body[0][1]])

        self.end = self.body.pop(self.length - 1)

    def grow(self):
        if self.end is not None:
            self.body.append(self.end)
            self.stdscr.addstr(self.end[1], self.end[0], self.char)
            self.end = None

    @property
    def length(self):
        return len(self.body)
