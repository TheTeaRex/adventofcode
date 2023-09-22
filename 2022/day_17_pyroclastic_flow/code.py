#! /usr/bin/python3


import os
from jet import Jet
from typing import List


class Solution(object):
    def __init__(self, filename: str, num: int) -> None:
        self.jet = Jet(self.read_file(filename))
        self.rock_id = 0
        # self.part_one(num, Chamber())
        self.part_one_solution(num)

    def read_file(self, file_name: str) -> str:
        f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
        text = f.read()
        f.close()
        return text

    def prints_rock(self, rock: List[int]) -> None:
        for i in rock[::-1]:
            print(format(i, '09b'))

    def prints_chamber(self, chamber: List[int]) -> None:
        for i in chamber[:-len(chamber):-1]:
            line = f'{format(i ^ 257, "09b")}'
            line = line.replace('1', '#')
            line = line.replace('0', '.')
            line = '|' + line[1:len(line) - 1] + '|'
            print(line)
        print('+-------+')

    def can_rock_move_sideway_then_down(self, rock: List[int], jet_dir: str, chamber: List[int], level: int):
        if jet_dir == '>':
            new_position = [i >> 1 for i in rock]
        else: # if dir == '<'
            new_position = [i << 1 for i in rock]
        # check to see if the sideway new position is valid
        for i in range(level, level + len(rock)):
            if new_position[i - level] & chamber[i] != 0:
                break
        else:
            # valid, so get to new position
            rock = new_position

        # check to see if can move down 1 unit
        settled = False
        for i in range(level - 1, level - 1 + len(rock)):
            if rock[i - level + 1] & chamber[i] != 0:
                # can't move down anymore, be part of the chamber
                settled = True
                break

        if settled:
            for i in range(level, level + len(rock)):
                if rock[i - level] & chamber[i] == 1:
                    raise Exception
                chamber[i] = rock[i - level] | chamber[i]
            while chamber[-1] == 257:
                chamber.pop()

        return (settled, rock, chamber)

    def part_one_solution(self, num: int) -> int:
        chamber = [511] # 0b1111111
        rocks = [
            [60], # 0b0011110
            [16, 56, 16], # 0b0001000, 0b0011100, 0b0001000
            [56, 8, 8], # 0b0011100, 0b0000100, 0b0000100
            [32, 32, 32, 32], # 0b0010000 x4
            [48, 48] # 0b0011000 x2
        ]

        for i in range(num):
            rock = rocks[i % len(rocks)]
            chamber += [257 for _ in range(len(rock) + 3)]
            position = len(chamber) -len(rock)
            while True:
                jet_dir = self.jet.current
                settled, rock, chamber = self.can_rock_move_sideway_then_down(rock, jet_dir, chamber, position)
                position -= 1
                if settled:
                    break

        print(f'Part 1: {len(chamber) - 1}')


if __name__ == "__main__":
    # Part 1 solution
    Solution('matt_input', 2022)