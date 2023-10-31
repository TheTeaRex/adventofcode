#! /usr/bin/python3


import os
from typing import List


class Solution:
    def __init__(self, filename: str) -> None:
        """
        part1: answer for part 1, required to run solution1()
        part2: answer for part 2, required to run solution2()
        """
        lines = self.read_file(filename).split("\n")
        self.monkeys = self.parse_data(lines)
        self.part1 = self.dfs('root', self.monkeys['root'])
        self.part2 = 0
        print(f"Part 1: {self.part1}")
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        """
        Typical file read
        Output: the str of the file
        """
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def parse_data(self, lines: List[str]):
        monkeys = {}
        for line in lines:
            name, item = line.split(': ')
            items = item.split(' ')
            if name not in monkeys:
                if len(items) == 1:
                    monkeys[name] = {
                        'name': name,
                        'result': int(items[0])
                    }
                else:
                    monkeys[name] = {
                        'name': name,
                        'monkey1': items[0],
                        'operator': items[1],
                        'monkey2': items[2]
                    }
            else:
                # should not reach here
                raise Exception('found repeated monkey name in file')

        return monkeys

    def dfs(self, name, monkey):
        if 'result' in monkey:
            return monkey['result']

        two_monkeys = []
        for monkey_ref in ['monkey1', 'monkey2']:
            other_monkey_name = self.monkeys[name][monkey_ref]
            if 'result' not in self.monkeys[other_monkey_name]:
                two_monkeys.append(self.dfs(other_monkey_name, self.monkeys[other_monkey_name]))
            else:
                two_monkeys.append(self.monkeys[other_monkey_name]['result'])
        if self.monkeys[name]['operator'] == '+':
            result = two_monkeys[0] + two_monkeys[1]
        elif self.monkeys[name]['operator'] == '*':
            result = two_monkeys[0] * two_monkeys[1]
        elif self.monkeys[name]['operator'] == '-':
            result = two_monkeys[0] - two_monkeys[1]
        else:
            result = two_monkeys[0] // two_monkeys[1]
        self.monkeys[name]['result'] = result

        return result

if __name__ == "__main__":
    solution = Solution("input")
