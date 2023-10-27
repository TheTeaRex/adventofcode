#! /usr/bin/python3

import os
from typing import List

def read_file() -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def solution_part_1(instructions: List[str]) -> int:
    i = result = 0
    x_val = 1
    counter = 0
    cycle_counter = 0
    reads_instruction = True
    while i < len(instructions):
        counter += 1

        if (counter - 20) % 40 == 0:
            cycle_counter += 1
            result += (x_val * counter)
            if cycle_counter == 6:
                break

        if reads_instruction:
            if instructions[i] != 'noop':
                num = int(instructions[i].split(' ')[1])
                reads_instruction = False
            i += 1
        else: # don't need to read instruction as it's in a process of a addx
            # num variable is available
            x_val += num
            reads_instruction = True

    return result

def solution_part_2(instructions: List[str]) -> str:
    result = ''
    i = counter = 0
    cycle_counter = position = 0
    x_val = 1
    reads_instruction = True
    while i < len(instructions):
        counter += 1

        if (counter - 1) % 40 == 0:
            cycle_counter += 1
            result += '\n'
            position = 0
            if cycle_counter == 7:
                break

        if position == x_val or position == x_val - 1 or position == x_val + 1:
            result += '#'
        else:
            result += '.'
        position += 1

        if reads_instruction:
            if instructions[i] != 'noop':
                num = int(instructions[i].split(' ')[1])
                reads_instruction = False
            i += 1
        else: # don't need to read instruction as it's in a process of a addx
            # num variable is available
            x_val += num
            reads_instruction = True

    return result

if __name__ == "__main__":
    text = read_file().split('\n')
    print(f'Part 1: {solution_part_1(text)}')
    print(f'Part 2: {solution_part_2(text)}')