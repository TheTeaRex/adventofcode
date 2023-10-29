#! /usr/bin/python3


import os
import re
from collections import deque
from typing import Dict, List
from room import Room


def read_file(file_name: str) -> str:
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r', encoding="utf-8") as f:
        text = f.read()
    return text


def maps_rooms(lines: List[str]) -> Dict[str, Room]:
    """
    Input: processed input file in list of strs
    Output: dictionary where the key is the room name, value is the room object
    """
    result = {}
    for line in lines:
        m = re.match(
            r"Valve (?P<name>\w+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<to_rooms>((\S+)( )?)+)",
            line,
        )
        temp = {}
        name = m.groupdict()["name"]
        flow = int(m.groupdict()["rate"])
        for dest in m.groupdict()["to_rooms"].split(", "):
            temp[dest] = 1
        result[name] = Room(name, flow, temp)
    return result


def maps_dist_from_room_to_room(rooms: Dict[str, Room]) -> Dict[str, Room]:
    """
    Take the given rooms and calculate the distances to every other room
    except for the ones that have flow rate == 0
    """
    for room in rooms.values():
        visited = set()
        dests = {room.name: 0}
        q = deque([(room.name, 0)])
        while q:
            name, dist = q.popleft()
            if name in visited:
                continue
            visited.add(name)
            if name not in dests and rooms[name].flow_rate != 0:
                dests[name] = dist
            for d_name in rooms[name].to_room_names:
                q.append((d_name, dist + 1))
        del dests[room.name]
        room.to_all_rooms = dests
    return rooms


def solution(
    start_room: Room, time_left: int, rooms: Dict[str, Room], part: int
) -> int:
    """
    Input: the object of the starting room, time givent to get out, all the rooms objects
    Output: the maximum pressure to be release with the given time
    """
    # creating an indicies for faster access
    rooms_ref = {}
    count = 0
    for room in rooms.values():
        if room.flow_rate != 0:
            rooms_ref[room.name] = count
            count += 1

    cache = {}

    def dfs(room: Room, time: int, bitmask: int, cur_value: int, max_val: int) -> int:
        index = (room.name, bitmask)
        if index in cache and cache[index] > cur_value:
            return cache[index]
        cache[index] = cur_value
        max_val = max(max_val, cur_value)

        for neighbor, dist in room.to_all_rooms.items():
            remaining_time = time - dist - 1
            if remaining_time <= 0:
                continue
            bit = 1 << rooms_ref[neighbor]
            if bitmask & bit:
                continue
            neighbor_state = bitmask | bit
            neighbor_value = cur_value + (rooms[neighbor].flow_rate * remaining_time)
            max_val = max(
                max_val,
                dfs(
                    rooms[neighbor],
                    remaining_time,
                    neighbor_state,
                    neighbor_value,
                    max_val,
                ),
            )
        return max_val

    if part == 1:
        return dfs(start_room, time_left, 0, 0, 0)
    # part 2 answers
    # use the cache to find the answer
    dfs(start_room, time_left, 0, 0, 0)
    result = 0
    # sort it by the value
    sorted_cache = deque(sorted(cache.items(), key=lambda x: x[1], reverse=True))
    while sorted_cache:
        item = sorted_cache.popleft()
        # since the list is sorted, if item's value * 2 is smaller than result, no point on looking more
        if item[1] * 2 < result:
            break
        for against in reversed(sorted_cache):
            # if we found a valve that are opened by both parties, that won't be the answer
            # since both parties shouldn't be opening the same valve
            if item[0][1] & against[0][1] == 0 and result < item[1] + against[1]:
                result = item[1] + against[1]
    return result


def prints_rooms(rooms: Dict[str, Room]) -> None:
    """
    Print info about all the given rooms
    """
    for room in rooms.values():
        print(room)


if __name__ == "__main__":
    text = read_file("input").split("\n")
    rooms = maps_rooms(text)
    rooms = maps_dist_from_room_to_room(rooms)
    print(f'Part 1: {solution(rooms["AA"], 30, rooms, 1)}')
    print(f'Part 2: {solution(rooms["AA"], 26, rooms, 2)}')
