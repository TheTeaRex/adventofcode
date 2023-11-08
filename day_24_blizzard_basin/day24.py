#! /usr/bin/python3

import os
from collections import deque
from typing import Dict, List, Tuple


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        solution() will set the answer to self.part1 and self.part2
        """
        self.part1 = 0
        self.part2 = 0
        self.blizzards = {}
        self.edges = set()
        lines = self.read_file(filename).split("\n")
        self.row_size = len(lines)
        self.col_size = len(lines[0])
        self.parse_data(lines)
        self.solution()
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
        parse the data
        store the blizzards as dict with pos as key and list[dir] as value in self.blizzards
        store the edge as set in self.edges
        """
        self.blizzards = {}
        self.edges = set()
        for r in range(self.row_size):
            for c in range(self.col_size):
                if r == 0 or r == self.row_size - 1 or c == 0 or c == self.col_size - 1:
                    self.edges.add((r, c))
                elif lines[r][c] != ".":
                    self.blizzards[(r, c)] = [lines[r][c]]
        self.edges.remove((0, 1))
        self.edges.remove((self.row_size - 1, self.col_size - 2))

    def print_grid(
        self, blizzards: Dict[Tuple[int], List[str]], cur: Tuple[int] = None
    ) -> None:
        """
        print the given grid, if cur is given, the current position will be printed as 'E'
        """
        for r in range(self.row_size):
            row = []
            for c in range(self.col_size):
                if (r, c) in self.edges:
                    row.append("#")
                elif (r, c) in blizzards:
                    num = len(blizzards[(r, c)])
                    if num > 1:
                        row.append(str(num))
                    else:
                        row.append(blizzards[(r, c)][0])
                elif cur is not None and (r, c) == cur:
                    row.append("E")
                else:
                    row.append(".")
            print("".join(row))

    def move_blizzards(self, time: int) -> Dict[Tuple[int], List[str]]:
        """
        give the time, will calculate where the blizzards are going to be off self.blizzards
        return the new blizzard locations
        """
        new_blizzards = {}
        for b_pos in self.blizzards:
            for dir in self.blizzards[b_pos]:
                if dir == ">":
                    size = self.col_size - 2
                    new_row = b_pos[0]
                    new_col = (((b_pos[1] - 1) + (time % size)) % size) + 1
                elif dir == "<":
                    size = self.col_size - 2
                    new_row = b_pos[0]
                    new_col = 1 + ((b_pos[1] - time) % (self.col_size - 2))
                    new_col = (((b_pos[1] - 1) + (-time % size)) % size) + 1
                elif dir == "v":
                    size = self.row_size - 2
                    new_row = (((b_pos[0] - 1) + (time % size)) % size) + 1
                    new_col = b_pos[1]
                else:  # '^'
                    size = self.row_size - 2
                    new_row = (((b_pos[0] - 1) + (-time % size)) % size) + 1
                    new_col = b_pos[1]
                new_pos = (new_row, new_col)
                if new_pos in new_blizzards:
                    new_blizzards[new_pos].append(dir)
                else:
                    new_blizzards[new_pos] = [dir]

        return new_blizzards

    def bfs(self, start: Tuple[int], end: Tuple[int]) -> int:
        """
        run a bfs algo to find the shortest time from start to end
        return the shortest time and store the blizzards locations during that time
        """
        q = deque([[start, 0]])
        blizzard_patterns = [self.blizzards]
        visited = {(start, 0)}
        while q:
            cur_pos, time = q.popleft()

            if cur_pos == end:
                self.blizzards = blizzard_patterns[time]
                return time

            ntime = time + 1
            if len(blizzard_patterns) <= ntime:
                blizzard_patterns.append(self.move_blizzards(ntime))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]:
                new_pos = (cur_pos[0] + dr, cur_pos[1] + dc)
                if (
                    new_pos in self.edges
                    or new_pos in blizzard_patterns[ntime]
                    or new_pos[0] < 0
                    or new_pos[0] >= self.row_size
                    or new_pos[1] < 0
                    or new_pos[1] >= self.col_size
                ):
                    # invalid position
                    continue
                else:
                    if (new_pos, ntime) not in visited:
                        visited.add((new_pos, ntime))
                        q.append([new_pos, ntime])

    def solution(self) -> None:
        """
        used to run both part 1 and part 2
        part 1 requires one run of bfs
        part 2 requires 3 runs of bfs with the continual blizzard locations
        """
        time = self.bfs((0, 1), (self.row_size - 1, self.col_size - 2))
        self.part1 = time
        time += self.bfs((self.row_size - 1, self.col_size - 2), (0, 1))
        time += self.bfs((0, 1), (self.row_size - 1, self.col_size - 2))
        self.part2 = time


if __name__ == "__main__":
    solution = Solution("input")
