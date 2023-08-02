#! /usr/bin/python3

import os
from typing import List

def read_file() -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def returns_tail_position(head: List[int], tail: List[int]) -> List[int]:
    # tail doesn't need to move since it's 1 step within the head in all directions
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return tail

    diffy = tail[1] - head[1]
    diffx = tail[0] - head[0]
    if diffx > 0:
        tail[0] -= 1
    elif diffx < 0:
        tail[0] += 1

    if diffy > 0:
        tail[1] -= 1
    elif diffy < 0:
        tail[1] += 1

    return tail

def improved_part_1(steps: List[str], num_knots: int = 2) -> int:
    coordinates = {
        'U': {
            'index': 1,
            'diff': 1
        },
        'R': {
            'index': 0,
            'diff': 1
        },
        'D': {
            'index': 1,
            'diff': -1
        },
        'L': {
            'index': 0,
            'diff': -1
        }
    }
    snake = []
    visited = set()
    for _ in range(num_knots):
        snake.append([0, 0])
    visited.add(tuple(snake[-1]))
    for step in steps:
        if len(step) == 0:
            break
        direction, num = step.split(' ')
        for _ in range(int(num)):
            snake[0][coordinates[direction]['index']] += coordinates[direction]['diff']
            # move the rest of the body per step
            for i in range(1, len(snake)):
                snake[i] = returns_tail_position(snake[i - 1], snake[i])
            # finished moving the snake, add last section to visited
            visited.add(tuple(snake[-1]))

    return len(visited)

if __name__ == "__main__":
    text = read_file().split('\n')
    print(f'Part 1: {improved_part_1(text)}')
    print(f'Part 2: {improved_part_1(text, 10)}')