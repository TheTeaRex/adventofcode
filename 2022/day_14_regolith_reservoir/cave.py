#! /usr/bin/python3


from typing import List, Set, Tuple


class Cave:
    def __init__(self, lines: List[str]) -> None:
        self.sand_start = (500, 0)
        self.cave_lowest_point = 0
        self.sands = set()
        self.rocks = self.scan_for_rocks(lines)
        self.unit_of_sand_until_abyss = 0

    def scan_for_rocks(self, lines: List[str]) -> Set[Tuple[int, int]]:
        rocks = set()
        for line in lines:
            points = line.split(' -> ')
            pi, pj = points[0].split(',')
            pi, pj = int(pi), int(pj)
            self.cave_lowest_point = max(self.cave_lowest_point, pj)
            for a in range(1, len(points)):
                i, j = points[a].split(',')
                i, j = int(i), int(j)
                di = i - pi
                if di != 0:
                    for b in range(pi, i + 1 if di > 0 else i - 1, 1 if di > 0 else -1):
                        rocks.add((b, j))
                else:
                    dj = j - pj
                    for b in range(pj, j + 1 if dj > 0 else j - 1, 1 if dj > 0 else -1):
                        rocks.add((i, b))
                self.cave_lowest_point = max(self.cave_lowest_point, j)
                pi, pj = i, j
        return rocks

    def sand_drops(self) -> Tuple[int, int]:
        sand = self.sand_start
        while True:
            next_spot = (sand[0], sand[1] + 1)
            while next_spot not in self.rocks and\
                  next_spot not in self.sands and\
                  next_spot[1] <= self.cave_lowest_point:
                sand = next_spot
                next_spot = (sand[0], sand[1] + 1)

            next_spot = (sand[0] - 1, sand[1] + 1)
            if next_spot not in self.rocks and\
               next_spot not in self.sands and\
               next_spot[1] <= self.cave_lowest_point:
                sand = next_spot
                continue
            next_spot = (sand[0] + 1, sand[1] + 1)
            if next_spot not in self.rocks and\
               next_spot not in self.sands and\
               next_spot[1] <= self.cave_lowest_point:
                sand = next_spot
                continue
            break
        return sand

    def is_sand_in_abyss(self, sand: Tuple[int, int]) -> bool:
        return sand[1] >= self.cave_lowest_point

    def fills_sand_until_abyss(self) -> None:
        i = 0
        while True:
            sand = self.sand_drops()
            if self.is_sand_in_abyss(sand):
                break
            self.sands.add(sand)
            i += 1
            self.unit_of_sand_until_abyss += 1