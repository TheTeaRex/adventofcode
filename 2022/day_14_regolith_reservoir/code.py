#! /usr/bin/python3


import os
from cave import Cave


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


if __name__ == "__main__":
    text = read_file('input').split('\n')
    cave = Cave(text)
    cave.fills_sand_until_abyss()
    print(f'Part 1: {cave.unit_of_sand_until_abyss}')