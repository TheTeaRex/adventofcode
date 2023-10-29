#! /usr/bin/python3


from collections import deque
from typing import List, Tuple
from CodeExceptions import MonkeyOperationError
from Item import Item


class Monkey:
    def __init__(
        self,
        id: int,
        items: List[Item],
        op: str,
        op_params: List[str],
        test: int,
        true_id: int,
        false_id: int,
    ) -> None:
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
            "id": self.id,
            "items": self.items,
            "operation": f"{self.op_params[0]} {self.op} {self.op_params[1]}",
            "test": self.test,
            "true_id": self.true_id,
            "false_id": self.false_id,
            "num_of_inspections": self.num_of_inspections,
        }
        return str(result)

    def has_items(self) -> bool:
        return len(self.items) != 0

    def inspects_item(self) -> Item:
        self.num_of_inspections += 1
        return self.items.popleft()

    def catches_item(self, item: Item) -> None:
        self.items.append(item)

    def performs_operation(
        self, item: Item, modulo: int, relief: int
    ) -> Tuple[int, Item]:
        """
        in: expects length of 2 item to operate on
        out: returns monkey id to pass item to
        """
        nums = []
        for num in self.op_params:
            if num == "old":
                nums.append(item.wlevel)
            else:
                nums.append(int(num))

        if self.op == "+":
            worry_level = nums[0] + nums[1]
        elif self.op == "*":
            worry_level = nums[0] * nums[1]
        else:  # self.op == '/'
            raise MonkeyOperationError()

        worry_level = worry_level // relief
        worry_level %= modulo
        item.set_wlevel(worry_level)
        return (
            (self.true_id, item)
            if worry_level % self.test == 0
            else (self.false_id, item)
        )
