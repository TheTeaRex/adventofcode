#! /usr/bin/python3


import os
from typing import List
import helper
from cave import Cave


def read_file(file_name: str) -> str:
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r', encoding="utf-8") as f:
        text = f.read()
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
        up = sensor.coordinate[1] - sensor.detection_distance
        down = sensor.coordinate[1] + sensor.detection_distance
        if up <= row <= down:
            one = (
                sensor.detection_distance
                - abs(row - sensor.coordinate[1])
                + sensor.coordinate[0]
            )
            two = (
                -(sensor.detection_distance - abs(row - sensor.coordinate[1]))
                + sensor.coordinate[0]
            )
            ranges.append([min(one, two), max(one, two)])

    ranges = remove_overlapped_ranges(ranges)
    for item in ranges:
        result += item[1] - item[0] + 1

    # get rid of the beacon count on that row
    for beacon in cave.beacons:
        for item in ranges:
            if (
                beacon.coordinate[1] == row
                and item[0] <= beacon.coordinate[0] <= item[1]
            ):
                result -= 1

    # get rid of the sensor count on that row
    # sensors var only has the sensors with y=row
    for sensor in sensors:
        for item in ranges:
            if item[0] <= sensor.coordinate[0] <= item[1]:
                result -= 1

    return result


def solution_part_2(cave: Cave, grid_size: int) -> int:
    answer = None
    intersections = []
    sensors_that_could_intersect = cave.gets_sensors_that_are_close_enough()
    for sensor in sensors_that_could_intersect:
        for neighbor in sensors_that_could_intersect[sensor]:
            for s_slope in sensor.p_edge_plus_one:
                for n_slope in neighbor.n_edge_plus_one:
                    temp = helper.gets_line_intersection(s_slope, n_slope)
                    if 0 <= temp[0] <= grid_size and 0 <= temp[1] <= grid_size:
                        intersections.append(temp)
            for s_slope in sensor.n_edge_plus_one:
                for n_slope in neighbor.p_edge_plus_one:
                    temp = helper.gets_line_intersection(s_slope, n_slope)
                    if 0 <= temp[0] <= grid_size and 0 <= temp[1] <= grid_size:
                        intersections.append(temp)

    for intersection in intersections:
        for sensor in cave.sensors:
            if helper.is_within_distance(
                intersection, sensor.coordinate, sensor.detection_distance
            ):
                break
        else:
            answer = intersection
            break

    if answer is None:
        # should never reach this
        raise Exception("Error: no valid solution found for part 2")
    return answer[0] * 4000000 + answer[1]


if __name__ == "__main__":
    text = read_file("input").split("\n")
    cave = Cave(text)
    print(f"Part 1: {solution_part_1(cave, 2000000)}")
    print(f"Part 2: {solution_part_2(cave, 4000000)}")
