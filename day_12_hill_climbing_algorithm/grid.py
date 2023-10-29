#! /usr/bin/python3


from collections import deque
from typing import List, Tuple


class Grid:
    def __init__(self, blob: List[str]):
        self.map = self.create_grid(blob)
        self.start = None
        self.end = None
        self.find_end_to_end_and_convert_map()

    def create_grid(self, lines: List[str]) -> List[List[str]]:
        grid = []
        for line in lines:
            grid.append([line[a] for a in range(len(line))])
        return grid

    def find_end_to_end_and_convert_map(self) -> None:
        """
        input: None
        output: None

        This function takes the object's map, which is a List[List[str]],
        and convert it to a List[List[int]]
        'S' -> 0
        'E' -> 27
        'a' -> 1
        'b' -> 2
        ...
        ...
        'y' -> 25
        'z' -> 26
        """
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == "S":
                    self.start = (i, j)
                    self.map[i][j] = 0
                elif self.map[i][j] == "E":
                    self.end = (i, j)
                    self.map[i][j] = 27
                else:
                    self.map[i][j] = ord(self.map[i][j]) % 96  # ord('a') - 1

    def find_shortest_path_from_the_end(
        self, end: Tuple[int], start: Tuple[int] = (None, None)
    ) -> int:
        """
        input:
        - end in tuple as a destination
        - start in tuple as a starting point (optional)
        output:
        - if the starting point is provided -> fewest step start to end
        - assuming no starting point is provided -> min(from all elevation a + the grid starting point to end)
        """
        visited = [
            [False for _ in range(len(self.map[0]))] for _ in range(len(self.map))
        ]
        steps_to_all_a = []
        q = deque([(end[0], end[1], 0)])
        while q:
            i, j, step = q.popleft()
            if start == (None, None) and (self.map[i][j] == 1 or self.map[i][j] == 0):
                steps_to_all_a.append(step)
                continue
            if (i, j) == start:
                return step
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if (
                    0 <= ni < len(self.map)
                    and 0 <= nj < len(self.map[0])
                    and visited[ni][nj] is False
                    and self.map[ni][nj] >= self.map[i][j] - 1
                ):
                    visited[ni][nj] = True
                    q.append((ni, nj, step + 1))

        return min(steps_to_all_a)
