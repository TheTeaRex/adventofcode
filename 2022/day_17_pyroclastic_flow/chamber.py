#! /usr/bin/python3


class Chamber(object):
    def __init__(self) -> None:
        self.floor = 0
        self.height = 0
        self.width = 7
        self.state = set((i, 0) for i in range(1, self.width))
        self.l_wall = 0
        self.r_wall = self.l_wall + self.width + 1

    def __repr__(self) -> str:
        return str(sorted(list(self.state), key=lambda x: x[1]))
