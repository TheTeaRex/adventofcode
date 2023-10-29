#! /usr/bin/python3


from typing import Dict


class Room:
    def __init__(
        self, name: str, flow_rate: int, to_room_names: Dict[str, int]
    ) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.to_room_names = to_room_names
        self.to_all_rooms = {}

    def __repr__(self) -> str:
        result = f"Room name: {self.name}\n"
        result += f"Flow rate: {self.flow_rate}\n"
        result += f"To neighbor rooms: {self.to_room_names}\n"
        result += f"To all rooms: {self.to_all_rooms}\n"
        return result
