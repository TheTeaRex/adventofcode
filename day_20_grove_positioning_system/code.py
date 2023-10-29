#! /usr/bin/python3


import os
from typing import List


class Solution:
    def __init__(self, filename: str) -> None:
        """
        numlist: to store the parse nums
        listsize: len(numlist)
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        """
        lines = self.read_file(filename).split("\n")
        self.numlist = self.parse_nums(lines)
        self.listsize = len(self.numlist)
        self.part1 = 0
        self.part2 = 0

    def read_file(self, file_name: str) -> str:
        """
        Typical file read
        Output: the str of the file
        """
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def parse_nums(self, lines: List[str]) -> List[int]:
        """
        Given the list of str, convert them to list of int
        """
        return [int(x) for x in lines]

    def move_nums(self, for_part_2: bool = False) -> List[int]:
        """
        Takes a boolean parameter to indicate if we are solving for part 2
        otherwise, assuming False, we are solving for part 1

        Part 1:
        Mix up the numbers once
        Do not use decryption key

        Part 2:
        Mix up the numbers ten times
        Decryption key was used
        """
        key = 811589153
        cycle = 1
        if for_part_2:
            cycle = 10

        result = list(range(self.listsize))

        for _ in range(cycle):
            for i, num in enumerate(self.numlist):
                pos = result.index(i)
                if num != 0:
                    if for_part_2:
                        num = (
                            (num % (self.listsize - 1)) * (key % (self.listsize - 1))
                        ) % (self.listsize - 1)
                    result.pop(pos)
                    to_pos = (pos + num) % (self.listsize - 1)
                else:
                    continue
                result.insert(to_pos, i)
        if for_part_2:
            return [self.numlist[num] * key for num in result]
        return [self.numlist[num] for num in result]

    def solution1(self) -> None:
        """
        Run this to calculate part 1's answer
        the answer is store in self.part1
        """
        self.part1 = 0
        final_list = self.move_nums(False)
        index = final_list.index(0)
        for pos in [1000, 2000, 3000]:
            pos = (pos + index) % self.listsize
            self.part1 += final_list[pos]

    def solution2(self) -> None:
        """
        Run this to calculate part 2's answer
        the answer is store in self.part2
        """
        self.part2 = 0
        final_list = self.move_nums(True)
        index = final_list.index(0)
        for pos in [1000, 2000, 3000]:
            pos = (pos + index) % self.listsize
            self.part2 += final_list[pos]


if __name__ == "__main__":
    solution = Solution("input")
    solution.solution1()
    print(f"Part 1: {solution.part1}")
    solution.solution2()
    print(f"Part 2: {solution.part2}")
