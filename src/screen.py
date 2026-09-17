class Screen:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.border_h = 30
        self.border_w = 30

    def render_border(self):
        for i in range(self.border_h):
            if i == 0:
                self.stdscr.addstr(i, 0, "╭" + "─" * (self.border_w * 2 - 2) + "╮")
                continue
            if i == self.border_h - 1:
                self.stdscr.addstr(i, 0, "╰" + "─" * (self.border_w * 2 - 2) + "╯")
                continue
            self.stdscr.addstr(i, 0, "│")
            self.stdscr.addstr(i, (self.border_w * 2 - 1), "│")
