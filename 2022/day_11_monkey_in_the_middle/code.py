#! /usr/bin/python3


import os
from Monkey import Monkey
from World import World
from typing import List



def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def solution_part_1(world: World, rounds) -> None:
    for _ in range(rounds):
        for monkey in world.monkeys:
            while monkey.has_items():
                 item = monkey.inspects_item()
                 to_monkey, item = monkey.performs_operation(item)
                 world.monkeys[to_monkey].catches_item(item)


def print_part_1_answer(world: World) -> None:
    result = sorted(world.monkeys, key=lambda monkey: monkey.num_of_inspections, reverse=True)
    '''
    for i, monkey in enumerate(world.monkeys):
        print(f'Monkey {i} inspected items {monkey.num_of_inspections} times.')
    '''
    return result[0].num_of_inspections * result[1].num_of_inspections


if __name__ == "__main__":
    text = read_file('input').split('\n')
    world = World(text)
    solution_part_1(world, 20)
    print(f'Part 1: {print_part_1_answer(world)}')
