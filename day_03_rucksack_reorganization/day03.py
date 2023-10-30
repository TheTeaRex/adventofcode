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

        # lower case minus 96
        # upper case minus 38
        # text = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw" # noqa: E501
        lines = text.split("\n")

        # part 1
        result = 0

        for line in lines:
            mid = len(line) // 2
            items = set()
            dup = set()
            for i in range(0, mid):
                items.add(line[i])
            for i in range(mid, len(line)):
                if line[i] in items and line[i] not in dup:
                    dup.add(line[i])
                    result += (
                        ord(line[i]) - 38 if line[i].isupper() else ord(line[i]) - 96
                    )

        self.part1 = result
        print(result)

        # part 2
        j = 0
        result = 0
        while j < len(lines):
            # make the first elf's rucksack a set
            items = set(lines[j])
            # iterate through the second elf's rucksack
            j += 1
            dup = set()
            for item in lines[j]:
                if item in items:
                    dup.add(item)
            # iterate through the third elf's rucksack
            items = set()
            j += 1
            for item in lines[j]:
                if item in dup:
                    result += ord(item) - 38 if item.isupper() else ord(item) - 96
                    break
            j += 1

        self.part2 = result
        print(result)


if __name__ == "__main__":
    Solution("input")
