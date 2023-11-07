#! /usr/bin/python3


import copy
import os
from collections import deque
from typing import Dict, List, Tuple


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        """
        self.part2 = 0
        self.start = None
        self.end = None
        self.blizzards = {}
        self.edges = set()
        self.cur = None
        lines = self.read_file(filename).split("\n")
        self.row_size = len(lines)
        self.col_size = len(lines[0])
        self.parse_data(lines)
        #self.print_grid(self.blizzards, (0, 1))
        self.part1 = self.solution_part1()
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

    def parse_data(self, lines: List[str]):
        self.start = (0, 1)
        self.end = (self.row_size - 1, self.col_size - 2)
        #print(self.end)
        self.blizzards = {}
        self.edges = set()
        for r in range(self.row_size):
            for c in range(self.col_size):
                if r == 0 or r == self.row_size - 1 or c == 0 or c == self.col_size - 1:
                    self.edges.add((r, c))
                elif lines[r][c] != '.':
                    self.blizzards[(r, c)] = [lines[r][c]]
        self.edges.remove(self.start)
        self.edges.remove(self.end)
        #print(self.edges)
        #print(self.blizzards)

    def print_grid(self, blizzards: Dict[Tuple[int], List[str]], cur: Tuple[int]=None) -> None:
        for r in range(self.row_size):
            row = []
            for c in range(self.col_size):
                if (r, c) in self.edges:
                    row.append('#')
                elif (r, c) in blizzards:
                    num = len(blizzards[(r, c)])
                    if num > 1:
                        row.append(str(num))
                    else:
                        row.append(blizzards[(r, c)][0])
                elif cur is not None and (r, c) == cur:
                    row.append('E')
                else:
                    row.append('.')
            print(''.join(row))

    def move_blizzards(self, time: int) -> Dict[Tuple[int], List[str]]:
        new_blizzards = {}
        for b_pos in self.blizzards:
            for dir in self.blizzards[b_pos]:
                if dir == '>':
                    size = self.col_size - 2
                    new_row = b_pos[0]
                    new_col = (((b_pos[1] - 1) + (time % size)) % size) + 1
                elif dir == '<':
                    size = self.col_size - 2
                    new_row = b_pos[0]
                    new_col = 1 + ((b_pos[1] - time) % (self.col_size - 2))
                    new_col = (((b_pos[1] - 1) + (-time % size)) % size) + 1
                elif dir == 'v':
                    size = self.row_size - 2
                    new_row = (((b_pos[0] - 1) + (time % size)) % size) + 1
                    new_col = b_pos[1]
                else: # '^'
                    size = self.row_size - 2
                    new_row = (((b_pos[0] - 1) + (-time % size)) % size) + 1
                    new_col = b_pos[1]
                new_pos = (new_row, new_col)
                if new_pos in new_blizzards:
                    new_blizzards[new_pos].append(dir)
                else:
                    new_blizzards[new_pos] = [dir]

        return new_blizzards

    def dfs(self, cur_pos, time, blizzards, cache):
        if cur_pos == self.end:
            return time

        key = tuple([cur_pos, tuple(blizzards)])
        if key in cache:
            return cache[key]

        # advance each blizzard by 1 unit
        new_blizzards = self.move_blizzards(blizzards)

        result = float('inf')
        for dr, dc in [(0, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]:
            new_pos = (cur_pos[0] + dr, cur_pos[1] + dc)
            if new_pos in self.edges or new_pos in new_blizzards:
                continue
            else:
                result = min(result, self.dfs(new_pos, time + 1, new_blizzards, cache))

        cache[key] = result
        self.part1 = min(self.part1, result)
        return result

    def solution_part1(self):
        #self.dfs(copy.deepcopy(self.start), 0, blizzards, {})
        q = deque([[(0, 1), 0]])
        blizzard_patterns = [self.blizzards]
        visited = {((0, 1), 0)}
        while q:
            cur_pos, time = q.popleft()
            #print(f'current_position: {cur_pos}')
            #print(f'current time: {time}')

            if cur_pos == self.end:
                return time

            ntime = time + 1
            if len(blizzard_patterns) <= ntime:
                blizzard_patterns.append(self.move_blizzards(ntime))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]:
                new_pos = (cur_pos[0] + dr, cur_pos[1] + dc)
                #print(new_pos)
                if new_pos in self.edges or new_pos in blizzard_patterns[ntime] or new_pos[0] < 0 or new_pos[0] >= self.row_size or new_pos[1] < 0 or new_pos[1] >= self.col_size:
                    # invalid position
                    continue
                else:
                    if (new_pos, ntime) not in visited:
                        visited.add((new_pos, ntime))
                        q.append([new_pos, ntime])
                #print(q)
            #print('=========================')
            # input('okay./....')



if __name__ == "__main__":
    solution = Solution("input")
    """blizzards = copy.deepcopy(solution.blizzards)
    solution.print_grid(blizzards)
    solution.print_grid(solution.move_blizzards(5))
    solution.print_grid(solution.move_blizzards(18))
    print('-----------------')"""
