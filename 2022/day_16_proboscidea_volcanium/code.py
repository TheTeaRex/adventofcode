#! /usr/bin/python3


from typing import List
from room import Room
import os
import re


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def maps_rooms(lines: List[str]) -> List[Room]:
    rooms = []
    for line in lines:
        m = re.match(
            r'Valve (?P<name>\w+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<to_rooms>((\S+)( )?)+)',
            line
        )
        room = Room(
            m.groupdict()['name'],
            int(m.groupdict()['rate']),
            m.groupdict()['to_rooms'].split(', ')
        )
        rooms.append(room)
    return rooms


def prints_rooms(rooms: List[Room]) -> None:
    for room in rooms:
        print(room)

if __name__ == "__main__":
    text = read_file('sample_input').split('\n')
    rooms = maps_rooms(text)
    prints_rooms(rooms)