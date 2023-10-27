#! /usr/bin/python3


from typing import List


class Jet(object):
    def __init__(self, order: List[str]) -> None:
        self.order = list(order)
        self.current_id = 0

    @property
    def current(self) -> str:
        direction = self.order[self.current_id % len(self.order)]
        self.next()
        return direction

    def next(self) -> None:
        self.current_id += 1