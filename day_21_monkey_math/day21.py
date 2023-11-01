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
        self.part1 = self.solution1_dfs("root", self.monkeys["root"])[0]
        print(f"Part 1: {self.part1}")
        self.part2 = self.solution2()
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
            name, item = line.split(": ")
            items = item.split(" ")
            if name not in monkeys:
                if len(items) == 1:
                    monkeys[name] = {
                        "name": name,
                        "result": int(items[0]),
                        # setup for part2
                        "humn": False,
                    }
                else:
                    monkeys[name] = {
                        "name": name,
                        "monkey1": items[0],
                        "operator": items[1],
                        "monkey2": items[2],
                        # setup for part2
                        "humn": False,
                    }
            else:
                # should not reach here
                raise Exception("found repeated monkey name in file")

        return monkeys

    def solution1_dfs(self, name, monkey):
        if "result" in monkey:
            if name == "humn":
                self.monkeys[name]["humn"] = True
                return [monkey["result"], True]
            else:
                return [monkey["result"], monkey["humn"]]

        two_monkeys = []
        has_humn = False
        for monkey_ref in ["monkey1", "monkey2"]:
            other_monkey_name = self.monkeys[name][monkey_ref]
            temp = self.solution1_dfs(
                other_monkey_name, self.monkeys[other_monkey_name]
            )
            two_monkeys.append(temp[0])
            has_humn = has_humn | temp[1]

        if self.monkeys[name]["operator"] == "+":
            result = two_monkeys[0] + two_monkeys[1]
        elif self.monkeys[name]["operator"] == "*":
            result = two_monkeys[0] * two_monkeys[1]
        elif self.monkeys[name]["operator"] == "-":
            result = two_monkeys[0] - two_monkeys[1]
        else:
            result = two_monkeys[0] // two_monkeys[1]

        self.monkeys[name]["result"] = result
        self.monkeys[name]["humn"] = has_humn

        return [result, has_humn]

    def solution2_dfs(self, name, monkey, num):
        if name == "humn":
            return num

        left = monkey["monkey1"]
        right = monkey["monkey2"]
        if self.monkeys[left]["humn"]:
            if self.monkeys[name]["operator"] == "+":
                new_num = num - self.monkeys[right]["result"]
            elif self.monkeys[name]["operator"] == "-":
                new_num = num + self.monkeys[right]["result"]
            elif self.monkeys[name]["operator"] == "*":
                new_num = num // self.monkeys[right]["result"]
            else:
                new_num = num * self.monkeys[right]["result"]
            return self.solution2_dfs(left, self.monkeys[left], new_num)
        else:
            if self.monkeys[name]["operator"] == "+":
                new_num = num - self.monkeys[left]["result"]
            elif self.monkeys[name]["operator"] == "-":
                new_num = -num + self.monkeys[left]["result"]
            elif self.monkeys[name]["operator"] == "*":
                new_num = num // self.monkeys[left]["result"]
            else:
                new_num = (1 // num) * self.monkeys[left]["result"]
            return self.solution2_dfs(right, self.monkeys[right], new_num)

    def solution2(self):
        # this assume only one of the two children of root touches the name 'humn'
        left = self.monkeys["root"]["monkey1"]
        right = self.monkeys["root"]["monkey2"]
        if self.monkeys[left]["humn"]:
            num = self.monkeys[right]["result"]
            investigate_monkey_name = left
        else:
            num = self.monkeys[left]["result"]
            investigate_monkey_name = right

        return self.solution2_dfs(
            investigate_monkey_name, self.monkeys[investigate_monkey_name], num
        )


if __name__ == "__main__":
    solution = Solution("input")
