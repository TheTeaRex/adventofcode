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
        self.elves_pos = set()
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
        """
        store result in self.elves_pos
        """
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    self.elves_pos.add((r, c))

    def get_min_max_r_c(self) -> Dict[str, int]:
        """
        calculate the min and max for row and column
        return in dict
        """
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
        """
        calculate offset to make a visualization of the map in a list
        return the list
        """
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
        map = [
            ["." for _ in range(min_max["max_c"] + offset_c + 1)]
            for _ in range(min_max["max_r"] + offset_r + 1)
        ]
        for r, c in map_pos:
            map[r][c] = "#"

        return map

    def print_map(self) -> None:
        """
        print the map and allow user to visualize it
        """
        for item in self.form_map():
            print("".join(item))

    def each_round(self) -> bool:
        """
        go through the decision tree for each elf and move accordingly
        return True if all the elves are settled, meaning they don't move for the round
        return False if any of the elves moved for the round
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
        proposals = {}
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
                    new_pos = (
                        elf_pos[0] + checks[dir][1][0],
                        elf_pos[1] + checks[dir][1][1],
                    )
                    # if we haven't see this new position, store the elf that's moving and it's dir
                    # if we have seen it, mark new_pos as dup
                    if new_pos not in proposals:
                        proposals[new_pos] = {"elf": elf_pos, "dup": False}
                    else:
                        proposals[new_pos]["dup"] = True
                    break

        if len(proposals) == 0:
            return True

        # second half of the round
        # move the non-dup elfs
        for new_pos in proposals:
            if proposals[new_pos]["dup"] is False:
                self.elves_pos.remove(proposals[new_pos]["elf"])
                self.elves_pos.add(new_pos)

        # move first direction to the last choice
        self.elves_dir_order.append(self.elves_dir_order.pop(0))

        return False

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

        # part 2
        while True:
            if self.each_round():
                break
            i += 1

        self.part2 = i + 1


if __name__ == "__main__":
    solution = Solution("input")
