#! /usr/bin/python3


import os
from cave import Cave
from typing import List


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


def remove_overlapped_ranges(ranges: List[List[int]]):
    ranges = sorted(ranges, key=lambda r: r[0])
    result = []
    cur = ranges[0]
    for i in range(1, len(ranges)):
        if cur[0] <= ranges[i][0] <= cur[1]:
            cur[1] = max(ranges[i][1], cur[1])
        else:
            result.append(cur)
            cur = ranges[i]
    result.append(cur)
    return result


def solution_part_1(cave: Cave, row: int) -> int:
    ranges = []
    sensors = []
    result = 0
    for sensor in cave.sensors:
        if sensor.coordinate[1] == row:
            sensors.append(sensor)
        up = sensor.coordinate[1] - sensor.distance_to_closest_beacon
        down = sensor.coordinate[1] + sensor.distance_to_closest_beacon
        if up <= row <= down:
            one = sensor.distance_to_closest_beacon - abs(row - sensor.coordinate[1]) + sensor.coordinate[0]
            two = -(sensor.distance_to_closest_beacon - abs(row - sensor.coordinate[1])) + sensor.coordinate[0]
            ranges.append([min(one, two), max(one, two)])

    ranges = remove_overlapped_ranges(ranges)
    for item in ranges:
        result += item[1] - item[0] + 1

    # get rid of the beacon count on that row
    for beacon in cave.beacons:
        for item in ranges:
            if beacon.coordinate[1] == row and item[0] <= beacon.coordinate[0] <= item[1]:
                result -= 1

    # get rid of the sensor count on that row
    # sensors var only has the sensors with y=row
    for sensor in sensors:
        for item in ranges:
            if item[0] <= sensor.coordinate[0] <= item[1]:
                result -= 1

    return result


if __name__ == "__main__":
    text = read_file('input').split('\n')
    cave = Cave(text)
    print(f'Part 1: {solution_part_1(cave, 2000000)}')