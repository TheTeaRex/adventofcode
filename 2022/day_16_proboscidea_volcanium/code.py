#! /usr/bin/python3


from collections import deque
from typing import Dict, List, Set
from room import Room
import os
import re


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def maps_rooms(lines: List[str]) -> Dict[str, Room]:
    '''
    Input: processed input file in list of strs
    Output: dictionary where the key is the room name, value is the room object
    '''
    result = {}
    for line in lines:
        m = re.match(
            r'Valve (?P<name>\w+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<to_rooms>((\S+)( )?)+)',
            line
        )
        temp = {}
        name = m.groupdict()['name']
        flow = int(m.groupdict()['rate'])
        for dest in m.groupdict()['to_rooms'].split(', '):
            temp[dest] = 1
        result[name] = Room(name, flow, temp)
    return result


def maps_dist_from_room_to_room(rooms: Dict[str, Room]) -> Dict[str, Room]:
    '''
    Take the given rooms and calculate the distances to every other room
    except for the ones that have flow rate == 0
    '''
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


def creates_all_combos_valve_states(num: int) -> List[List[bool]]:
    '''
    Input: the size of the combo needed
    Output: return a list of all possible boolean combo with the given size
    '''
    result = [[]]
    for _ in range(num):
        temp = []
        for item in result:
            for a in [True, False]:
                temp.append([a] + item)
        result = temp
    return result


def solution(start_room: Room, time_left: int, rooms: Dict[str, Room], part: int) -> int:
    '''
    Input: the object of the starting room, time givent to get out, all the rooms objects
    Output: the maximum pressure to be release with the given time
    '''
    # creating an indicies for faster access
    rooms_ref = {}
    count = 0
    for room in rooms.values():
        if room.flow_rate != 0 or room is start_room:
            rooms_ref[room.name] = count
            count += 1

    cache = {}
    def dfs(room: Room, time: int, valves_state: List[bool]) -> int:
        if (room.name, time, tuple(valves_state)) in cache:
            return cache[(room.name, time, tuple(valves_state))]

        max_val = 0
        for neighbor, dist in room.to_all_rooms.items():
            # - 1 for turnning the value
            remaining_time = time - dist - 1
            if remaining_time <= 0:
                continue
            if valves_state[rooms_ref[neighbor]]:
                continue
            max_val = max(
                max_val,
                dfs(
                    rooms[neighbor],
                    remaining_time,
                    [True if rooms_ref[neighbor] == i else state for i, state in enumerate(valves_state)]) + \
                        (rooms[neighbor].flow_rate * remaining_time)
            )
        cache[(room.name, time, tuple(valves_state))] = max_val
        return max_val
    
    if part == 1:
        return dfs(start_room, time_left, [False for _ in range(len(rooms_ref))])
    else:
        time_left -= 4
        result = 0
        for i in creates_all_combos_valve_states(len(rooms_ref)):
            count += 1
            result = max(
                result,
                dfs(start_room, time_left, i) + dfs(start_room, time_left, [False if state else True for state in i])
            )
        return result


def prints_rooms(rooms: Dict[str, Room]) -> None:
    '''
    Print info about all the given rooms
    '''
    for room in rooms.values():
        print(room)


if __name__ == "__main__":
    text = read_file('input').split('\n')
    rooms = maps_rooms(text)
    rooms = maps_dist_from_room_to_room(rooms)
    print(f'Part 1: {solution(rooms["AA"], 30, rooms, 1)}')
    print(f'Part 2: {solution(rooms["AA"], 30, rooms, 2)}')