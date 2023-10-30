#! /usr/bin/python3

import os
from typing import List


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename).split("\n")
        self.part1 = self.solution_part_1(text)
        self.part2 = self.solution_part_2(text)
        print(f"Part 1: {self.part1}")
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def solution_part_1(self, instructions: List[str]) -> int:
        i = result = 0
        x_val = 1
        counter = 0
        cycle_counter = 0
        reads_instruction = True
        while i < len(instructions):
            counter += 1

            if (counter - 20) % 40 == 0:
                cycle_counter += 1
                result += x_val * counter
                if cycle_counter == 6:
                    break

            if reads_instruction:
                if instructions[i] != "noop":
                    num = int(instructions[i].split(" ")[1])
                    reads_instruction = False
                i += 1
            else:  # don't need to read instruction as it's in a process of a addx
                # num variable is available
                x_val += num
                reads_instruction = True

        return result

    def solution_part_2(self, instructions: List[str]) -> str:
        result = ""
        i = counter = 0
        cycle_counter = position = 0
        x_val = 1
        reads_instruction = True
        while i < len(instructions):
            counter += 1

            if (counter - 1) % 40 == 0:
                cycle_counter += 1
                result += "\n"
                position = 0
                if cycle_counter == 7:
                    break

            if position in [x_val, x_val - 1, x_val + 1]:
                result += "#"
            else:
                result += "."
            position += 1

            if reads_instruction:
                if instructions[i] != "noop":
                    num = int(instructions[i].split(" ")[1])
                    reads_instruction = False
                i += 1
            else:  # don't need to read instruction as it's in a process of a addx
                # num variable is available
                x_val += num
                reads_instruction = True

        return result


if __name__ == "__main__":
    Solution("input")
