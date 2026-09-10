class Player:
    def __init__(self) -> None:
        self.body: list = [[0, 0]]
        self.char: str = "$"

    def render(self, stdscr):
        for tile in self.body:
            stdscr.addstr(tile[1], tile[0], self.char)

    def move(self, direction):
        if direction == "up":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - 1])
        elif direction == "down":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + 1])
        elif direction == "left":
            self.body.insert(0, [self.body[0][0] - 1, self.body[0][1]])
        elif direction == "right":
            self.body.insert(0, [self.body[0][0] + 1, self.body[0][1]])

        self.body.pop(self.length - 1)

    @property
    def length(self):
        return len(self.body)
