#! /usr/bin/python3


import copy
import json
import os
from typing import List


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename).split("\n")
        packets = self.parse_data(text)
        self.part1 = self.solution_part_1(packets)
        print(f"Part 1: {self.part1}")
        packets2 = copy.deepcopy(packets)
        self.part2 = self.solution_part_2_through_sorting(packets2)
        print(f"Part 2 with sorting: {self.part2}")
        packets3 = copy.deepcopy(packets)
        print(f"Part 2 with no sorting: {self.solution_part_2_no_sorting(packets3)}")

    def read_file(self, filename: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def parse_data(self, lines: List[str]) -> List[dict]:
        packets = []
        i = 0
        while i < len(lines):
            packets += [json.loads(lines[i]), json.loads(lines[i + 1])]
            i += 3
        return packets

    def solution_part_1(self, packets) -> int:
        """
        take the list of packets, make comparison two at a time
        collect the "right" order indices (starts at 1) and
        return the sum of the indices
        """
        result = []
        i = 0
        while i < len(packets):
            is_right_order = self.is_pair_in_right_order(packets[i], packets[i + 1])
            i += 2
            if is_right_order:
                result.append(i // 2)

        return sum(result)

    def solution_part_2_through_sorting(self, packets) -> int:
        a, b = [[2]], [[6]]
        packets += [a, b]
        i = 1
        while i < len(packets):
            is_right_order = self.is_pair_in_right_order(packets[i - 1], packets[i])
            j = i
            while (
                not is_right_order and j > 0
            ):  # ideally this wouldn't let j goes smaller than 1
                temp = packets[j]
                packets[j] = packets[j - 1]
                packets[j - 1] = temp
                j -= 1
                is_right_order = self.is_pair_in_right_order(packets[j - 1], packets[j])
            i += 1

        result = 1
        for i, v in enumerate(packets):
            if v in [a, b]:
                result *= i + 1
        return result

    def solution_part_2_no_sorting(self, packets) -> int:
        a, b = [[2]], [[6]]
        if self.is_pair_in_right_order(a, b):  # indices started 1
            cnta, cntb = 1, 2
        else:
            cnta, cntb = 2, 1

        for packet in packets:
            cnta += 1 if not self.is_pair_in_right_order(a, packet) else 0
            cntb += 1 if not self.is_pair_in_right_order(b, packet) else 0

        return cnta * cntb

    def is_pair_in_right_order(self, left, right) -> bool:  # noqa: C901
        """
        Given a pair of lists
        Return if they are in the right order
        """
        i = 0
        while i < len(left) or i < len(right):
            if i >= len(left):
                return True
            if i >= len(right):
                return False
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] < right[i]:
                    return True
                if left[i] > right[i]:
                    return False
            elif isinstance(left[i], list) and isinstance(right[i], list):
                result = self.is_pair_in_right_order(left[i], right[i])
                if result is not None:
                    return result
            elif isinstance(left[i], list) and isinstance(right[i], int):
                result = self.is_pair_in_right_order(left[i], [right[i]])
                if result is not None:
                    return result
            elif isinstance(left[i], int) and isinstance(right[i], list):
                result = self.is_pair_in_right_order([left[i]], right[i])
                if result is not None:
                    return result

            i += 1
        # if reach here, it means all numbers in list are the same
        # and the length of the two lists are the same
        return None


if __name__ == "__main__":
    Solution("input")
