#! /usr/bin/python3


# pylint: disable=R0903
class Item:
    # pylint: disable=W0622
    def __init__(self, id: int, wlevel: int) -> None:
        self.id = id
        self.wlevel = wlevel

    # pylint: disable=C0116
    def set_wlevel(self, wlevel: int) -> None:
        self.wlevel = wlevel
