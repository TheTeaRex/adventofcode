#! /usr/bin/python3


class Rock(object):
    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        self.position = (x, y)
        self.length = length
        self.width = width
        self.height = y + length
        self.space = set()

    def updates_position(self, x: int, y: int) -> None:
        self.position = (x, y)

    def updates_height(self) -> None:
        self.height = sorted(list(self.space), key=lambda x: x[1], reverse=True)[0][1]

    def __repr__(self) -> str:
        result = ''
        for y in range(self.length - 1, -1, -1):
            for x in range(self.width):
                if (self.position[0] + x, self.position[1] + y) in self.space:
                    result += '#'
                else:
                    result += '.'
            result += '\n'
        return result


class HRock(Rock):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 1, 4)
        self.updates_space()
        self.updates_height()

    def updates_position(self, x: int, y: int) -> None:
        super().updates_position(x, y)
        self.updates_space()
        self.updates_height()

    def updates_space(self) -> None:
        self.space = set((self.position[0] + i, self.position[1]) for i in range(self.width))


class CRock(Rock):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3, 3)
        self.updates_space()
        self.updates_height()

    def updates_position(self, x: int, y: int) -> None:
        super().updates_position(x, y)
        self.updates_space()
        self.updates_height()

    def updates_space(self) -> None:
        result = set((self.position[0] + i, self.position[1] + 1) for i in range(self.width))
        for i in range(self.length):
            result.add((self.position[0] + 1, self.position[1] + i))
        self.space = result


class LRock(Rock):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3, 3)
        self.updates_space()
        self.updates_height()

    def updates_position(self, x: int, y: int) -> None:
        super().updates_position(x, y)
        self.updates_space()
        self.updates_height()

    def updates_space(self) -> None:
        result = set((self.position[0] + i, self.position[1] + 0) for i in range(self.width))
        for i in range(1, self.length):
            result.add((self.position[0] + 2, self.position[1] + i))
        self.space = result


class VRock(Rock):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 4, 1)
        self.updates_space()
        self.updates_height()

    def updates_position(self, x: int, y: int) -> None:
        super().updates_position(x, y)
        self.updates_space()
        self.updates_height()

    def updates_space(self) -> None:
        self.space = set((self.position[0] + 0, self.position[1] + i) for i in range(self.length))


class SRock(Rock):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 2, 2)
        self.updates_space()
        self.updates_height()

    def updates_position(self, x: int, y: int) -> None:
        super().updates_position(x, y)
        self.updates_space()
        self.updates_height()

    def updates_space(self) -> None:
        result = set()
        for i in range(self.length):
            for j in range(self.width):
                result.add((self.position[0] + j, self.position[1] + i))
        self.space = result