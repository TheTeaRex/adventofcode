#! /usr/bin/python3


import os
from cave import Cave


# pylint: disable=C0116
def read_file(file_name: str) -> str:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}",
        "r",
        encoding="utf-8",
    ) as f:
        text = f.read()
    return text


if __name__ == "__main__":
    text = read_file("input").split("\n")
    cave = Cave(text)
    cave.fills_sand_until_abyss()
    print(f"Part 1: {cave.units_of_sand_until_abyss}")
    cave2 = Cave(text, True, 2)
    cave2.fills_sand_until_block()
    print(f"Part 2: {cave2.units_of_sand_until_block}")
