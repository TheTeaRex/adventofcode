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

def returns_tail_position(head: List[int], tail: List[int]) -> List[int]:
    # tail doesn't need to move since it's 1 step within the head in all directions
    if abs(tail[0] - head[0]) < 1 and abs(tail[1] - head[1]) < 1:
        return tail

    # tail is on the same row or column as head but 2 steps ahead
    if tail[0] == head[0]:
        if tail[1] - head[1] > 1:
            tail[1] -= 1
        elif tail[1] - head[1] < -1:
            tail[1] += 1
    elif tail[1] == head[1]:
        if tail[0] - head[0] > 1:
            tail[0] -= 1
        elif tail[0] - head[0] < -1:
            tail[0] += 1
    # tail is not on the same row or column as head, so move diagonally to get to the head
    elif (tail[1] - head[1] > 1 and tail[0] - head[0] == 1) or\
        (tail[0] - head[0] > 1 and tail[1] - head[1] == 1):
        tail[0] -= 1
        tail[1] -= 1
    elif (tail[0] - head[0] > 1 and tail[1] - head[1] == -1) or\
        (tail[1] - head[1] < -1 and tail[0] - head[0] == 1):
        tail[0] -= 1
        tail[1] += 1
    elif (tail[1] - head[1] < -1 and tail[0] - head[0] == -1) or\
        (tail[0] - head[0] < -1 and tail[1] - head[1] == -1):
        tail[0] += 1
        tail[1] += 1
    elif (tail[0] - head[0] < -1 and tail[1] - head[1] == 1) or\
        (tail[1] - head[1] > 1 and tail[0] - head[0] == -1):
        tail[0] += 1
        tail[1] -= 1

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
            print(snake)

    return len(visited)

if __name__ == "__main__":
    text = read_file()
    print(solution_part_1(text.split('\n')))
    print(improved_part_1(text.split('\n'), 10))