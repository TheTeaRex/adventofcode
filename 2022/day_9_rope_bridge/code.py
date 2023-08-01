#! /usr/bin/python3

import os
from typing import List

def read_file() -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def is_tail_next_to_head(head: List[List[int]], tail: List[List[int]]) -> bool:
    if abs(tail[0] - head[0]) < 2 and abs(tail[1] - head[1]) < 2:
        return True
    return False

def solution_part_1(steps: List[str]) -> int:
    coordinates = {
        'U': [0, 1],
        'R': [1, 0],
        'D': [0, -1],
        'L': [-1, 0]
    }
    tailx = taily = 0
    headx = heady = 0
    visited = set()
    visited.add((tailx, taily))
    for step in steps:
        direction, num = step.split(' ')
        for _ in range(int(num)):
            oldx = headx
            oldy = heady
            headx += coordinates[direction][0]
            heady += coordinates[direction][1]
            if not is_tail_next_to_head([headx, heady], [tailx, taily]):
                tailx = oldx
                taily = oldy
                visited.add((tailx, taily))

    return len(visited)

if __name__ == "__main__":
    text = read_file()
    steps = text.split('\n')
    print(solution_part_1(steps))
