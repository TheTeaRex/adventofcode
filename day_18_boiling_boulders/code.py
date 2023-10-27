#! /usr/bin/python3


import os
from typing import List, Set, Tuple


class Solution:
    def __init__(self, filename: str) -> None:
        lines = self.read_file(filename).split("\n")
        self.minb = float("inf")
        self.maxb = float("-inf")
        self.neighbors = [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]
        self.droplets = self.gets_droplets(lines)
        self.result_1 = self.solution_part_1()
        self.result_2 = self.solution_part_2()

    # pylint: disable=C0116
    def read_file(self, file_name: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    # pylint: disable=C0116
    def gets_droplets(self, lines: List[Tuple[int]]) -> Set[Tuple[int]]:
        """
        gets all the dropelets from file
        also keeps track of min and max on the numbers we have seen
        """
        result = set()
        for line in lines:
            temp = tuple(int(x) for x in line.split(","))
            # pylint: disable=W3301
            self.maxb = max(self.maxb, max(temp))
            self.minb = min(self.minb, min(temp))
            result.add(temp)

        self.minb -= 1
        self.maxb += 1
        return result

    # pylint: disable=C0116
    def solution_part_1(self) -> int:
        """
        get the highest possible surface (6 * the number of droplets)
        then loop through the droplet to see if they have a neighbor
        if so, -1 on the surface
        otherwise do nothing
        """
        surface_area = 6 * len(self.droplets)
        for x, y, z in self.droplets:
            for dx, dy, dz in self.neighbors:
                if (x + dx, y + dy, z + dz) in self.droplets:
                    surface_area -= 1
        return surface_area

    # pylint: disable=C0116
    def solution_part_2(self) -> int:
        """
        BFS to flood-filled the a finited box
        when we reach a node where it's a droplet, surface += 1
        """
        size = self.maxb - self.minb + 1
        seen = [
            [[False for _ in range(size)] for _ in range(size)] for _ in range(size)
        ]
        q = [(self.minb, self.minb, self.minb)]
        result = 0
        while q:
            x, y, z = q.pop()
            if seen[x][y][z]:
                continue
            seen[x][y][z] = True
            for dx, dy, dz in self.neighbors:
                nx, ny, nz = x + dx, y + dy, z + dz
                nitem = (nx, ny, nz)
                if (
                    self.minb <= nx <= self.maxb
                    and self.minb <= ny <= self.maxb
                    and self.minb <= nz <= self.maxb
                ):
                    if nitem in self.droplets:
                        result += 1
                    else:
                        q.append(nitem)

        return result


if __name__ == "__main__":
    solution = Solution("input")
    print(f"Part 1: {solution.result_1}")
    print(f"Part 2: {solution.result_2}")
