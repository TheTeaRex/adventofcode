#! /usr/bin/python3


import os
from typing import List, Tuple
from droplet import Droplet


class Solution(object):
    def __init__(self, filename: str) -> None:
        lines = self.read_file(filename).split('\n')
        self.droplets = self.gets_droplets(lines)
        self.result_1 = self.solution_part_1()

    def read_file(self, file_name: str) -> str:
        f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
        text = f.read()
        f.close()
        return text

    def gets_droplets(self, lines: List[Tuple[int]]) -> List[Droplet]:
        result = []
        for line in lines:
            a = Droplet(tuple(int(x) for x in line.split(',')))
            for item in result:
                self.checks_adjacent(a, item)
            result.append(a)
        return result

    def checks_adjacent(self, a: Droplet, b: Droplet) -> None:
        # assuming there isn't any duplicate coordinates
        if (a.position[0] - 1 <= b.position[0] <= a.position[0] + 1 and\
            a.position[1] == b.position[1] and a.position[2] == b.position[2]) or\
            (a.position[1] - 1 <= b.position[1] <= a.position[1] + 1 and\
            a.position[0] == b.position[0] and a.position[2] == b.position[2]) or\
            (a.position[2] - 1 <= b.position[2] <= a.position[2] + 1 and\
            a.position[1] == b.position[1] and a.position[0] == b.position[0]):
            a.num_surface -= 1
            b.num_surface -= 1

    def solution_part_1(self) -> int:
        result = 0
        for droplet in self.droplets:
            result += droplet.num_surface
        return result


if __name__ == "__main__":
   solution = Solution('input')
   print(f'Part 1: {solution.result_1}')