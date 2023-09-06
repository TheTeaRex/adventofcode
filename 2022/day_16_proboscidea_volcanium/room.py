#! /usr/bin/python3


from typing import List


class Room:
    def __init__(self, name: str, flow_rate: int, to_rooms: List[str]) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.to_rooms = to_rooms

    def __repr__(self) -> str:
        result = f'Room name: {self.name}\n'
        result += f'Flow rate: {self.flow_rate}\n'
        result += f'To rooms: {", ".join(self.to_rooms)}\n'
        return result