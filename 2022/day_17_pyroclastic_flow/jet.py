#! /usr/bin/python3


from typing import List


class Jet(object):
    def __init__(self, order: List[str]) -> None:
        self.order = list(order)
        self.current_id = 0

    @property
    def current(self) -> str:
        direction = self.order[self.current_id]
        self.next()
        if direction == '<':
            return (-1, 0)
        else:
            return (1, 0)

    def next(self) -> None:
        if self.current_id == len(self.order) - 1:
            self.current_id = 0
        else:
            self.current_id += 1