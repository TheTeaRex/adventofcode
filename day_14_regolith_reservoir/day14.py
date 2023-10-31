#! /usr/bin/python3


import os
from day_14_regolith_reservoir.cave import Cave


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename).split("\n")
        cave = Cave(text)
        cave.fills_sand_until_abyss()
        self.part1 = cave.units_of_sand_until_abyss
        print(f"Part 1: {self.part1}")
        cave2 = Cave(text, True, 2)
        cave2.fills_sand_until_block()
        self.part2 = cave2.units_of_sand_until_block
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text


if __name__ == "__main__":
    Solution("input")
