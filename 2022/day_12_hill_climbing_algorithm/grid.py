#! /usr/bin/python3


from collections import deque
from typing import List, Tuple


class Grid:
    def __init__(self, blob: List[str]):
        self.map = self.create_grid(blob)
        self.start = None
        self.end = None
        self.find_end_to_end_and_convert_map()
        self.fewest_steps_from_actual_start = self.find_shortest_path(self.start[0],
                                                                      self.start[1],
                                                                      self.end[0],
                                                                      self.end[1])
        self.list_of_a = [self.start]
        self.list_of_a += self.find_all_a_locations()
        self.list_of_shorts = []
        for i, j in self.list_of_a:
            self.list_of_shorts.append(self.find_shortest_path(i, j, self.end[0], self.end[1]))
        self.fewest_steps_from_all_elevation_a = min(filter(lambda k: k is not None, self.list_of_shorts))


    def create_grid(self, lines: List[str]) -> List[List[str]]:
        grid = []
        for line in lines:
            grid.append([line[a] for a in range(len(line))])
        return grid

    def find_end_to_end_and_convert_map(self) -> None:
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 'S':
                    self.start = (i, j)
                    self.map[i][j] = 0
                elif self.map[i][j] == 'E':
                    self.end = (i, j)
                    self.map[i][j] = 27
                else:
                    self.map[i][j] = ord(self.map[i][j]) % 96 # ord('a') - 1

    def find_all_a_locations(self) -> List[Tuple]:
        result = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 1:
                    result.append((i, j))
        return result

    def find_shortest_path(self, starti: int, startj: int, endi: int, endj: int) -> int:
        visited = [[False for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
        q = deque([(starti, startj, 0)])
        while q:
            i, j, step = q.popleft()
            if (i, j) == (endi, endj):
                return step
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(self.map) and\
                   0 <= nj < len(self.map[0]) and\
                   visited[ni][nj] is False and\
                   self.map[ni][nj] <= self.map[i][j] + 1:
                    visited[ni][nj] = True
                    q.append((ni, nj, step + 1))