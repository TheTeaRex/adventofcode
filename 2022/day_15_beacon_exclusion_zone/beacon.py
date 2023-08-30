#! /usr/bin/python3


class Beacon:
    def __init__(self, x: int, y: int) -> None:
        self.coordinate = (x, y)

    def __repr__(self) -> str:
        return f'Beacon coordinate: {self.coordinate}'