#! /usr/bin/python3


class Item:
    def __init__(self, id: int, wlevel: int) -> None:
        self.id = id
        self.wlevel = wlevel

    def set_wlevel(self, wlevel: int) -> None:
        self.wlevel = wlevel