#! /usr/bin/python3


import os
from day_12_hill_climbing_algorithm.grid import Grid


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename).split("\n")
        grid = Grid(text)
        self.part1 = grid.find_shortest_path_from_the_end(grid.end, grid.start)
        self.part2 = grid.find_shortest_path_from_the_end(grid.end)
        print(f"Part 1: {self.part1} steps")
        print(f"Part 2: {self.part2} steps")

    def read_file(self, filename: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text


if __name__ == "__main__":
    Solution('input')
