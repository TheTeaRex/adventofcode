#! /usr/bin/python3

import os
from typing import List

def read_file() -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def map_the_input(text: str) -> List[List[int]]:
    rows = text.split('\n')
    return [[int(c) for c in row] for row in rows]

def solution_part_1(grid: List[List[int]]) -> int:
    visible_trees = (len(grid) * len(grid[0])) - ((len(grid) - 2) * (len(grid[0]) - 2))

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            tree_height = grid[r][c]
            """
            up = all([tree_height - j > 0 for j in [grid[i][c] for i in range(0, r)]])
            down = all([tree_height - j > 0 for j in [grid[i][c] for i in range(r + 1, len(grid))]])
            left = all([tree_height - j > 0 for j in [grid[r][i] for i in range(0, c)]])
            right = all([tree_height - j > 0 for j in [grid[r][i] for i in range(c + 1, len(grid[0]))]])
            """
            for i in range(0, r):
                if tree_height - grid[i][c] <= 0:
                    up = False
                    break
            else:
                up = True

            for i in range(r + 1, len(grid)):
                if tree_height - grid[i][c] <= 0:
                    down = False
                    break
            else:
                down = True

            for i in range(0, c):
                if tree_height - grid[r][i] <= 0:
                    left = False
                    break
            else:
                left = True

            for i in range(c + 1, len(grid[0])):
                if tree_height - grid[r][i] <= 0:
                    right = False
                    break
            else:
                right = True

            if any([up, down, left, right]):
                visible_trees += 1

    return visible_trees

if __name__ == "__main__":
    text = read_file()
    # print(text)
    grid = map_the_input(text)
    print(f'Part 1\'s answer: {solution_part_1(grid)}')