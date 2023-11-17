#! /usr/bin/python3

import os
from typing import List


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        solution() will set the answer to self.part1 and self.part2
        """
        lines = self.read_file(filename).split("\n")
        self.part1 = 0
        self.part2 = None
        self.solution(lines)
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

    def snafu_to_dec(self, input: str) -> int:
        map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        result = 0
        size = len(input)
        i = 1
        while i <= size:
            result += map[input[-i]] * (5 ** (i - 1))
            i += 1
        return result

    def snafu_addition(self, input1: str, input2: str) -> str:
        s_to_d = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        d_to_s = {
            -5: "-0",
            -4: "-1",
            -3: "-2",
            -2: "=",
            -1: "-",
            0: "0",
            1: "1",
            2: "2",
            3: "1=",
            4: "1-",
            5: "10",
        }
        result = ""
        size1 = len(input1)
        size2 = len(input2)
        size = max(size1, size2)
        diff = abs(size1 - size2)
        if size1 > size2:
            input2 = ("0" * diff) + input2
        else:
            input1 = ("0" * diff) + input1

        i = size - 1
        carry = "0"
        while i >= 0:
            temp = s_to_d[input1[i]] + s_to_d[input2[i]] + s_to_d[carry]
            temp = d_to_s[temp]
            if len(temp) == 2:
                carry = temp[0]
            else:
                carry = "0"
            result += temp[-1]
            i -= 1

        return result[::-1]

    def solution(self, inputs: List[str]) -> None:
        result = inputs[0]
        for i in range(1, len(inputs)):
            result = self.snafu_addition(result, inputs[i])
        self.part1 = result


if __name__ == "__main__":
    solution = Solution("input")
