#! /usr/bin/python3


import os
import re
from typing import List


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        """
        self.map = []
        self.instructions = []
        self.rows_edge = []
        self.columns_edge = []
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.cur_dir = 0
        lines = self.read_file(filename).split("\n")
        self.parse_data(lines)
        self.cur_loc = [0, self.rows_edge[0][0]]
        self.solution1()
        self.part1 = self.calculate_password()
        print(f"Part 1: {self.part1}")
        self.part2 = 0
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
        data are stored in self.map and self.instructions
        """
        self.map = []
        column_size = 0
        for line in lines[:-2]:
            self.map.append(line)
            column_size = max(column_size, len(line))
            # get the rows edges
            for j, c in enumerate(line):
                if c != " ":
                    start = j
                    end = start + len(line.strip()) - 1
                    break
            self.rows_edge.append((start, end))

        # get the columns edges
        self.columns_edge = [None] * column_size
        # including the empty line to get the ends
        for i, line in enumerate(lines[:-1]):
            for j in range(column_size):
                if self.columns_edge[j] is None and j < len(line) and line[j] != " ":
                    self.columns_edge[j] = i
                elif isinstance(self.columns_edge[j], int) and (
                    j >= len(line) or line[j] == " "
                ):
                    self.columns_edge[j] = (self.columns_edge[j], i - 1)

        # getting the instructions
        match = re.findall(r"(\d+)(\w)?", lines[-1])
        self.instructions = []
        for item in match:
            self.instructions.append(int(item[0]))
            # the last item doesn't have the turn direction
            if len(item[1]) != 0:
                self.instructions.append(item[1])

    def find_wrap_around_point(self):
        """
        uses self.dir, self.cur_dir and self.cur_loc to
        figure the wrap aroudn point
        """
        if self.cur_dir == 0:  # facing right
            result = [self.cur_loc[0], self.rows_edge[self.cur_loc[0]][0]]
        elif self.cur_dir == 1:  # facing down
            result = [self.columns_edge[self.cur_loc[1]][0], self.cur_loc[1]]
        elif self.cur_dir == 2:  # facing left
            result = [self.cur_loc[0], self.rows_edge[self.cur_loc[0]][1]]
        else:  # facing up
            result = [self.columns_edge[self.cur_loc[1]][1], self.cur_loc[1]]
        return result

    def calculate_password(self):
        return (self.cur_loc[0] + 1) * 1000 + (self.cur_loc[1] + 1) * 4 + self.cur_dir

    def solution1(self):
        for instruction in self.instructions:
            if isinstance(instruction, int):
                i = 0
                nr = self.cur_loc[0] + self.dir[self.cur_dir][0]
                nc = self.cur_loc[1] + self.dir[self.cur_dir][1]
                while i < instruction:
                    if (
                        nr < 0
                        or nr >= len(self.map)
                        or nc < 0
                        or nc >= len(self.map[nr])
                        or self.map[nr][nc] == " "
                    ):
                        nr, nc = self.find_wrap_around_point()
                    if self.map[nr][nc] == "#":
                        break
                    self.cur_loc = [nr, nc]
                    nr = self.cur_loc[0] + self.dir[self.cur_dir][0]
                    nc = self.cur_loc[1] + self.dir[self.cur_dir][1]
                    i += 1
            else:  # instruction would be a direction change
                if instruction == "R":
                    self.cur_dir = (self.cur_dir + 1) % len(self.dir)
                else:
                    self.cur_dir = (self.cur_dir - 1) % len(self.dir)

    def print_map(self):
        for line in self.map:
            print("".join(line))


if __name__ == "__main__":
    solution = Solution("input")
