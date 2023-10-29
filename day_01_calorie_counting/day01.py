#! /usr/bin/python3

import os


class Solution:
    def __init__(self, filename: str):
        self.part1 = 0
        self.part2 = 0
        self.solution(filename)

    def solution(self, filename: str):
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()

        calories = text.split("\n")
        elvies = []
        count = 0
        for calory in calories:
            if len(calory) != 0:
                count += int(calory)
            else:
                elvies.append(count)
                count = 0
        elvies.append(count)

        self.part1 = max(elvies)
        print(self.part1)
        elvies.sort(reverse=True)
        self.part2 = sum(elvies[:3])
        print(self.part2)


if __name__ == "__main__":
    solution = Solution("input")
