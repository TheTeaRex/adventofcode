#! /usr/bin/python3

import os
from typing import List


def read_file() -> str:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/input", "r", encoding="utf-8"
    ) as f:
        text = f.read()
    return text


def map_the_input(text: str) -> List[List[int]]:
    rows = text.split("\n")
    return [[int(c) for c in row] for row in rows]


def solution_part_1(grid: List[List[int]]) -> int:  # noqa: C901
    max_scenic_score = 0
    visible_trees = (len(grid) * len(grid[0])) - ((len(grid) - 2) * (len(grid[0]) - 2))

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            tree_height = grid[r][c]
            count = [0 for _ in range(4)]
            for i in range(r - 1, -1, -1):
                count[0] += 1
                if tree_height - grid[i][c] <= 0:
                    up = False
                    break
            else:
                up = True
                count[0] = r

            for i in range(r + 1, len(grid)):
                count[1] += 1
                if tree_height - grid[i][c] <= 0:
                    down = False
                    break
            else:
                down = True
                count[1] = len(grid) - r - 1

            for i in range(c - 1, -1, -1):
                count[2] += 1
                if tree_height - grid[r][i] <= 0:
                    left = False
                    break
            else:
                left = True
                count[2] = c

            for i in range(c + 1, len(grid[0])):
                count[3] += 1
                if tree_height - grid[r][i] <= 0:
                    right = False
                    break
            else:
                right = True
                count[3] = len(grid[0]) - c - 1

            if any([up, down, left, right]):
                visible_trees += 1
            max_scenic_score = max(
                count[0] * count[1] * count[2] * count[3], max_scenic_score
            )

    return (visible_trees, max_scenic_score)


if __name__ == "__main__":
    text = read_file()
    # print(text)
    grid = map_the_input(text)
    answer = solution_part_1(grid)
    print(f"Part 1's answer: {answer[0]}")
    print(f"Part 2's answer: {answer[1]}")
