#! /usr/bin/python3


import copy
import os
from world import World


class Solution:
    def __init__(self, filename: str):
        text = self.read_file(filename).split("\n")
        world = World(text)
        world1 = copy.deepcopy(world)
        self.solution(world1, 20, world1.modulo, 3)
        self.part1 = self.print_answer(world1)
        print(f"Part 1: {self.part1}")
        world2 = copy.deepcopy(world)
        self.solution(world2, 10000, world2.modulo, 1)
        self.part2 = self.print_answer(world2)
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def solution(self, world: World, rounds, modulo: int, relief: int) -> None:
        for _ in range(rounds):
            for monkey in world.monkeys:
                while monkey.has_items():
                    item = monkey.inspects_item()
                    to_monkey, item = monkey.performs_operation(item, modulo, relief)
                    world.monkeys[to_monkey].catches_item(item)

    def print_answer(self, world: World) -> None:
        result = sorted(
            world.monkeys, key=lambda monkey: monkey.num_of_inspections, reverse=True
        )
        return result[0].num_of_inspections * result[1].num_of_inspections


if __name__ == "__main__":
    Solution("input")
