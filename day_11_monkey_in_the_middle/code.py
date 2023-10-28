#! /usr/bin/python3


import copy
import os
from World import World


# pylint: disable=C0116
def read_file(file_name: str) -> str:
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r', encoding="utf-8") as f:
        text = f.read()
    return text


# pylint: disable=C0116
def solution(world: World, rounds, modulo: int, relief: int = 1) -> None:
    for _ in range(rounds):
        for monkey in world.monkeys:
            while monkey.has_items():
                item = monkey.inspects_item()
                to_monkey, item = monkey.performs_operation(item, modulo, relief)
                world.monkeys[to_monkey].catches_item(item)


# pylint: disable=C0116
def print_answer(world: World) -> None:
    result = sorted(
        world.monkeys, key=lambda monkey: monkey.num_of_inspections, reverse=True
    )
    return result[0].num_of_inspections * result[1].num_of_inspections


if __name__ == "__main__":
    text = read_file("input").split("\n")
    world = World(text)
    world1 = copy.deepcopy(world)
    solution(world1, 20, world1.modulo, 3)
    print(f"Part 1: {print_answer(world1)}")
    world2 = copy.deepcopy(world)
    solution(world2, 10000, world2.modulo)
    print(f"Part 2: {print_answer(world2)}")
