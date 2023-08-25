#! /usr/bin/python3


from typing import List, Set, Tuple


class Cave:
    def __init__(self, lines: List[str], has_floor: bool=False, offset_lowest: int=0) -> None:
        self.sand_start = (500, 0)
        self.cave_lowest_point = 0 # should be the floor where there is no sand
        self.sands = set()
        self.has_floor = has_floor
        self.rocks = self.scan_for_rocks(lines, offset_lowest)
        self.units_of_sand_until_abyss = 0
        self.units_of_sand_until_block = 0

    def scan_for_rocks(self, lines: List[str], offset_lowest) -> Set[Tuple[int, int]]:
        '''
        cave's lowest point is determine by whethere there is a floor or not

        if it's the abyss, then getting to the coordinate of the lowest rock counts
        (cave_lowest_point) will break out of the sand drop look

        if there is floor, then sand drop will not ever get to the cave_lowest_point
        '''
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
        if self.has_floor:
            self.cave_lowest_point += (offset_lowest - 1)
        else:
            self.cave_lowest_point += offset_lowest
        return rocks

    def print_cave(self, offset: int=0) -> None:
        '''
        if know grid size, can use offset to not print so much
        '''
        cave = [['.' for _ in range(400, 600)] for _ in range(200)]
        cave[self.sand_start[1]][self.sand_start[0] - offset] = '+'
        for i, j in self.sands:
            cave[j][i - offset] = 's'
        for i, j in self.rocks:
            cave[j][i - offset] = '#'
        for line in cave:
            print(''.join(line))

    def sand_drops(self) -> Tuple[int, int]:
        '''
        simulate the sand drop
        1) sand will attempt to step straight down forever, until stopped
        2) if not 1, then attempt to step down left once
        3) if not 2, then attempt to step down right once
        if 2 or 3, then repeat all the steps again

        return sand's coordinate
        '''
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
        '''
        return True if sand is at the lowest rock's depth
        '''
        return sand[1] >= self.cave_lowest_point

    def fills_sand_until_abyss(self) -> None:
        '''
        fills sand until detects sand is at the lowest rock's depth
        '''
        i = 0
        while True:
            sand = self.sand_drops()
            if self.is_sand_in_abyss(sand):
                break
            self.sands.add(sand)
            i += 1
            self.units_of_sand_until_abyss += 1

    def is_sand_blocking_sand_start(self, sand: Tuple[int, int]) -> bool:
        '''
        return True, if sand is piled up to the starting point
        '''
        return sand == self.sand_start

    def fills_sand_until_block(self) -> None:
        '''
        fills sand until the starting point is blocked
        '''
        i = 0
        while True:
            sand = self.sand_drops()
            self.sands.add(sand)
            i += 1
            self.units_of_sand_until_block += 1
            if self.is_sand_blocking_sand_start(sand):
                break