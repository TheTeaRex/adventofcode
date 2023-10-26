#! /usr/bin/python3


import os
from typing import List


class Solution(object):
    def __init__(self, filename: str) -> None:
        lines = self.read_file(filename).split('\n')
        self.numlist = self.parse_nums(lines)
        self.listsize = len(self.numlist)
        self.part1 = 0
        self.part2 = 0

    def read_file(self, file_name: str) -> str:
        """
        Typical file read
        Output: the str of the file
        """
        f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
        text = f.read()
        f.close()
        return text

    def parse_nums(self, lines: List[str]) -> List[int]:
        return [int(x) for x in lines]

    def move_nums(self) -> List[int]:
        result = [x for x in range(self.listsize)]
        for i, num in enumerate(self.numlist):
            pos = result.index(i)
            if num != 0:
                result.pop(pos)
                to_pos = (pos + num) % (self.listsize - 1)
            else:
                continue
            result.insert(to_pos, i)
        return [self.numlist[num] for num in result]

    def solution1(self) -> None:
        """
        Run this to calculate part 1's answer
        the answer is store in self.part1
        """
        self.part1 = 0
        final_list = self.move_nums()
        index = final_list.index(0)
        for pos in [1000, 2000, 3000]:
            pos = (pos + index) % self.listsize
            self.part1 += final_list[pos]

    def solution2(self) -> None:
        """
        Run this to calculate part 2's answer
        the answer is store in self.part2
        """
        pass


if __name__ == "__main__":
    solution = Solution('input')
    solution.solution1()
    print(f'Part 1: {solution.part1}')
    solution.solution2()
    print(f'Part 2: {solution.part2}')