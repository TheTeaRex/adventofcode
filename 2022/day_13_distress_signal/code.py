#! /usr/bin/python3


import json
import os
from typing import List


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def parse_data(lines: List[str]) -> List[dict]:
    packets = []
    i = 0
    while i < len(lines):
        packets.append(
            {
                'left': json.loads(lines[i]),
                'right': json.loads(lines[i + 1])
            }
        )
        i += 3
    return packets


def solution_part_1(packets) -> int:
    '''
    take the list of pair packets, make the comparison
    collect the "right" order indices (starts at 1) and
    return the sum of the indices
    '''
    return sum([i + 1 if is_pair_in_right_order(packets[i]['left'], packets[i]['right']) else 0 for i in range(len(packets))])


def is_pair_in_right_order(left, right) -> bool:
    '''
    Given a pair of lists
    Return if they are in the right order
    '''
    i = 0
    while i < len(left) or i < len(right):
        if i >= len(left): return True
        if i >= len(right): return False
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]: return True
            elif left[i] > right[i]: return False
        elif isinstance(left[i], list) and isinstance(right[i], list):
            result = is_pair_in_right_order(left[i], right[i])
            if result is not None:
                return result
        elif isinstance(left[i], list) and isinstance(right[i], int):
            result = is_pair_in_right_order(left[i], [right[i]])
            if result is not None:
                return result
        elif isinstance(left[i], int) and isinstance(right[i], list):
            result = is_pair_in_right_order([left[i]], right[i])
            if result is not None:
                return result

        i += 1
    # if reach here, it means all numbers in list are the same
    # and the length of the two lists are the same
    return None



if __name__ == "__main__":
    text = read_file('input').split('\n')
    packets = parse_data(text)
    print(f'Part 1: {solution_part_1(packets)}')