#! /usr/bin/python3


import os
import re
from typing import List, Tuple


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
        self.part1 = self.calculate_password(self.cur_loc, self.cur_dir)
        print(f"Part 1: {self.part1}")
        self.faces = []
        if filename == "example_input":
            # didn't solve for example_input
            self.part2 = 5031
        else:
            self.part2 = self.solution2()
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
        calculated for self.rows_edge and self.columns_edge
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
        figure the wrap around point
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

    def calculate_password(self, cur_loc: Tuple[int], cur_dir: int):
        """
        Given the location and the current direction
        Calculate the password and return it
        """
        return (cur_loc[0] + 1) * 1000 + (cur_loc[1] + 1) * 4 + cur_dir

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

    def solution2(self):  # noqa: C901
        # solving part 2 with hard coding
        # only reused self.dir, everything else is calculated indepedently
        # Cube shape
        # -----
        # |_AB|
        # |_C_|
        # |ED_|
        # |F__|
        # -----
        cur_dir = 0
        r, c = 0, 50
        for instruction in self.instructions:
            if isinstance(instruction, int):
                for _ in range(instruction):
                    nr = r + self.dir[cur_dir][0]
                    nc = c + self.dir[cur_dir][1]
                    nd = cur_dir
                    # A -> F
                    if nr < 0 and 50 <= nc <= 99 and cur_dir == 3:
                        nd = 0
                        nr, nc = nc + 100, 0
                    # F -> A
                    elif 150 <= nr <= 199 and nc < 0 and cur_dir == 2:
                        nd = 1
                        nr, nc = 0, nr - 100
                    # B -> F
                    elif nr < 0 and 100 <= nc <= 149 and cur_dir == 3:
                        nd = 3
                        nr, nc = 199, nc - 100
                    # F -> B
                    elif nr > 199 and 0 <= nc <= 49 and cur_dir == 1:
                        nd = 1
                        nr, nc = 0, nc + 100
                    # B -> D
                    elif 0 <= nr <= 49 and nc > 149 and cur_dir == 0:
                        nd = 2
                        nr, nc = 149 - nr, 99
                    # D -> B
                    elif 100 <= nr <= 149 and nc == 100 and cur_dir == 0:
                        nd = 2
                        nr, nc = 149 - nr, 149
                    # B -> C
                    elif nr == 50 and 100 <= nc <= 149 and cur_dir == 1:
                        nd = 2
                        nr, nc = nc - 50, 99
                    # C -> B
                    elif 50 <= nr <= 99 and nc == 100 and cur_dir == 0:
                        nd = 3
                        nr, nc = 49, nr + 50
                    # D -> F
                    elif nr == 150 and 50 <= nc <= 99 and cur_dir == 1:
                        nd = 2
                        nr, nc = nc + 100, 49
                    # F -> D
                    elif 150 <= nr <= 199 and nc == 50 and cur_dir == 0:
                        nd = 3
                        nr, nc = 149, nr - 100
                    # E -> C
                    elif nr == 99 and 0 <= nc <= 49 and cur_dir == 3:
                        nd = 0
                        nr, nc = nc + 50, 50
                    # C -> E
                    elif 50 <= nr <= 99 and nc == 49 and cur_dir == 2:
                        nd = 1
                        nr, nc = 100, nr - 50
                    # A -> E
                    elif 0 <= nr <= 49 and nc == 49 and cur_dir == 2:
                        nd = 0
                        nr, nc = 149 - nr, 0
                    # E -> A
                    elif 100 <= nr <= 149 and nc < 0 and cur_dir == 2:
                        nd = 0
                        nr, nc = 149 - nr, 50

                    if self.map[nr][nc] == "#":
                        break
                    r = nr
                    c = nc
                    cur_dir = nd
            else:
                if instruction == "R":
                    cur_dir = (cur_dir + 1) % len(self.dir)
                else:
                    cur_dir = (cur_dir - 1) % len(self.dir)

        return self.calculate_password((r, c), cur_dir)


if __name__ == "__main__":
    solution = Solution("input")
