#! /usr/bin/python3


import re
from Item import Item
from Monkey import Monkey
from typing import List


class World:
    def __init__(self, blob: str) -> None:
        self.item_id = 0
        self.monkeys = []
        self.items = []
        self.parse_text(blob)

    def parse_text(self, blob: str) -> None:
        line = 0
        while line < len(blob):
            id = int(re.match(r'Monkey (?P<id>\d+):', blob[line]).groupdict()['id'])
            items_wlevel = re.match(r'\s*Starting items: (?P<items>.+)', blob[line + 1]).groupdict()['items'].split(', ')
            items = []
            for i in items_wlevel:
                self.items.append(Item(self.item_id, int(i)))
                items.append(self.items[-1])
                self.item_id += 1
            m = re.match(r'\s*Operation: new = (?P<param1>\S+) (?P<op>.) (?P<param2>\S+)', blob[line + 2])
            op = m.groupdict()['op']
            op_params = [m.groupdict()['param1'], m.groupdict()['param2']]
            test = int(re.match(r'\s*Test: divisible by (?P<test>\d+)', blob[line + 3]).groupdict()['test'])
            true_id = int(re.match(r'\s*If true: throw to monkey (?P<id>\d+)', blob[line + 4]).groupdict()['id'])
            false_id = int(re.match(r'\s*If false: throw to monkey (?P<id>\d+)', blob[line + 5]).groupdict()['id'])

            self.monkeys.append(Monkey(id, items, op, op_params, test, true_id, false_id))
            line += 7