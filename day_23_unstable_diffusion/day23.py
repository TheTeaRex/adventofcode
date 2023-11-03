#! /usr/bin/python3


import os
from typing import Dict, List


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        """
        self.part1 = 0
        self.part2 = 0
        lines = self.read_file(filename).split("\n")
        self.elves_pos = []
        self.elves_dir_order = ["n", "s", "w", "e"]
        self.parse_data(lines)
        self.size = len(self.elves_pos)
        self.solution1_and_2()
        print(f"Part 1: {self.part1}")
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        """
        Typical file read
        Output: the str of the file
        """
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def parse_data(self, lines: List[str]) -> None:
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    self.elves_pos.append((r, c))

    def get_min_max_r_c(self) -> Dict[str, int]:
        result = {
            "min_r": float("inf"),
            "min_c": float("inf"),
            "max_r": float("-inf"),
            "max_c": float("-inf"),
        }
        for r, c in self.elves_pos:
            result["min_r"] = min(result["min_r"], r)
            result["max_r"] = max(result["max_r"], r)
            result["min_c"] = min(result["min_c"], c)
            result["max_c"] = max(result["max_c"], c)
        return result

    def form_map(self) -> List[List[str]]:
        min_max = self.get_min_max_r_c()
        offset_r = 0
        offset_c = 0
        if min_max["min_r"] < 0:
            offset_r = abs(min_max["min_r"])
        elif min_max["min_r"] > 0:
            offset_r = -min_max["min_r"]
        if min_max["min_c"] < 0:
            offset_c = abs(min_max["min_c"])
        elif min_max["min_c"] > 0:
            offset_c = -min_max["min_c"]

        map_pos = [(item[0] + offset_r, item[1] + offset_c) for item in self.elves_pos]
        map = []
        for _ in range(min_max["max_r"] + offset_r + 1):
            temp = []
            for _ in range(min_max["max_c"] + offset_c + 1):
                temp.append(".")
            map.append(temp)
        for r, c in map_pos:
            map[r][c] = "#"

        return map

    def print_map(self) -> None:
        for item in self.form_map():
            print("".join(item))

    def each_round(self) -> None:
        """
        go through the decision tree for each elf and move accordingly
        """
        checks = {
            "n": ((-1, -1), (-1, 0), (-1, 1)),
            "s": ((1, -1), (1, 0), (1, 1)),
            "w": ((-1, -1), (0, -1), (1, -1)),
            "e": ((-1, 1), (0, 1), (1, 1)),
            "around": (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
            ),
        }
        proposed_pos = [None] * self.size
        proposed_dir = [None] * self.size
        # first half of the round
        # for each elf
        for i, elf_pos in enumerate(self.elves_pos):
            # check to see if any elves are around
            for dr, dc in checks["around"]:
                if (elf_pos[0] + dr, elf_pos[1] + dc) in self.elves_pos:
                    break
            else:  # no elves are around, don't need to move, next elf
                continue

            # there are elves around, so
            # cycle through elf's direction order
            for dir in self.elves_dir_order:
                # check to see if any of the threes positions are occupied
                for dr, dc in checks[dir]:
                    if (elf_pos[0] + dr, elf_pos[1] + dc) in self.elves_pos:
                        break
                else:  # no elves are in the way for that one direction
                    proposed_dir[i] = dir
                    proposed_pos[i] = (
                        elf_pos[0] + checks[dir][1][0],
                        elf_pos[1] + checks[dir][1][1],
                    )
                    break

        # second half of the round
        move = [True] * self.size
        for i, item in enumerate(proposed_pos):
            if item is None:
                move[i] = False
                continue
            if move[i] is True:
                for j in range(i + 1, self.size):
                    if item == proposed_pos[j]:
                        move[i] = False
                        move[j] = False
        # actual move
        for i, item in enumerate(move):
            if item is True:
                self.elves_pos[i] = proposed_pos[i]
        # move first direction to the last choice
        self.elves_dir_order.append(self.elves_dir_order.pop(0))

    def solution1_and_2(self):
        i = 0
        # part 1
        while i < 10:
            self.each_round()
            i += 1

        min_max = self.get_min_max_r_c()
        self.part1 = (min_max["max_r"] - min_max["min_r"] + 1) * (
            min_max["max_c"] - min_max["min_c"] + 1
        ) - self.size


if __name__ == "__main__":
    solution = Solution("input")
