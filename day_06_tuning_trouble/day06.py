#! /usr/bin/python3

import os


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename)
        self.part1 = self.better_solution(text, 4)
        self.part2 = self.better_solution(text, 14)
        print(self.part1)
        print(self.part2)

    def read_file(self, filename):
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def solution(self, text, unique):
        j = 0
        buffer = set()
        while j < len(text):
            if text[j] in buffer:
                buffer.clear()
                buffer.add(text[j])
                for k in range(j - 1, j - unique, -1):
                    if text[k] == text[j]:
                        break
                    buffer.add(text[k])
            else:
                buffer.add(text[j])
            j += 1
            if len(buffer) == unique:
                break

        return j

    def better_solution(self, text, unique):
        buffer = set()
        i = j = 0
        while j < len(text):
            if text[j] not in buffer:
                buffer.add(text[j])
            else:
                while i < j:
                    if text[i] == text[j]:
                        i += 1
                        break
                    buffer.remove(text[i])
                    i += 1
            j += 1
            if len(buffer) == unique:
                return j
        return None


if __name__ == "__main__":
    Solution("example_input")
