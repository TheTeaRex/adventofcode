#! /usr/bin/python3

import os
import re
from collections import deque
from typing import List, Tuple

class MonkeyOperationError(Exception):
    pass


class Monkey:
    def __init__(self, id: int, items: List[int], op: str, op_params: List[str], test: int, true_id: int, false_id: int):
        self.id = id
        self.items = deque(items)
        self.op = op
        self.op_params = op_params
        self.test = test
        self.true_id = true_id
        self.false_id = false_id
        self.num_of_inspections = 0

    def __repr__(self) -> str:
        result = {
            'id': self.id,
            'items': self.items,
            'operation': f'{self.op_params[0]} {self.op} {self.op_params[1]}',
            'test': self.test,
            'true_id': self.true_id,
            'false_id': self.false_id
        }
        return str(result)

    def has_items(self) -> bool:
        return len(self.items) != 0

    def inspects_item(self) -> int:
        self.num_of_inspections += 1
        return self.items.popleft()

    def catches_item(self, item: int) -> None:
        self.items.append(item)
        return None

    def performs_operation(self, param: int) -> Tuple[int, int]:
        '''
        in: expects length of 2 item to operate on
        out: returns monkey id to pass item to
        '''
        nums = []
        for num in self.op_params:
            if num == 'old':
                nums.append(param)
            else:
                nums.append(int(num))

        if self.op == '+':
            worry_level = nums[0] + nums[1]
        elif self.op == '-':
            worry_level = nums[0] - nums[1]
        elif self.op == '*':
            worry_level = nums[0] * nums[1]
        else: # self.op == '/'
            raise MonkeyOperationError()

        worry_level = worry_level // 3
        return (self.true_id, worry_level) if worry_level % self.test == 0 else (self.false_id, worry_level)

def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def parse_text(blob: str) -> List[Monkey]:
    monkeys = []
    i = 0
    while i < len(blob):
        id = int(re.match(r'Monkey (?P<id>\d+):', blob[i]).groupdict()['id'])
        items = re.match(r'\s*Starting items: (?P<items>.+)', blob[i + 1]).groupdict()['items'].split(', ')
        items = [int(i) for i in items]
        m = re.match(r'\s*Operation: new = (?P<param1>\S+) (?P<op>.) (?P<param2>\S+)', blob[i + 2])
        op = m.groupdict()['op']
        op_params = [m.groupdict()['param1'], m.groupdict()['param2']]
        test = int(re.match(r'\s*Test: divisible by (?P<test>\d+)', blob[i + 3]).groupdict()['test'])
        true_id = int(re.match(r'\s*If true: throw to monkey (?P<id>\d+)', blob[i + 4]).groupdict()['id'])
        false_id = int(re.match(r'\s*If false: throw to monkey (?P<id>\d+)', blob[i + 5]).groupdict()['id'])
        monkeys.append(Monkey(id, items, op, op_params, test, true_id, false_id))
        i += 7

    return monkeys


def solution_part_1(monkeys: List[Monkey], rounds) -> None:
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                 item = monkey.inspects_item()
                 to_monkey, item = monkey.performs_operation(item)
                 monkeys[to_monkey].catches_item(item)
    return None


def print_part_1_answer(monkeys: List[Monkey]) -> None:
    result = sorted(monkeys, key=lambda monkey: monkey.num_of_inspections, reverse=True)
    '''
    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i} inspected items {monkey.num_of_inspections} times.')
    '''
    return result[0].num_of_inspections * result[1].num_of_inspections


if __name__ == "__main__":
    text = read_file('input').split('\n')
    monkeys = parse_text(text)
    solution_part_1(monkeys, 20)
    print(f'Part 1: {print_part_1_answer(monkeys)}')
