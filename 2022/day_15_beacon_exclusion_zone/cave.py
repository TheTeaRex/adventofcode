#! /usr/bin/python3


import re
from beacon import Beacon
from sensor import Sensor
from typing import List, Tuple


class Cave:
    def __init__(self, lines: List[str]) -> None:
        self.sensors = []
        self.beacons = []
        self.beacon_coordinates_set = set()
        self.scans_the_cave(lines)

    def scans_the_cave(self, lines: List[str]) -> None:
        for line in lines:
            m = re.match(
                r'Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)',
                line
            )
            sx = int(m.groupdict()['sx'])
            sy = int(m.groupdict()['sy'])
            bx = int(m.groupdict()['bx'])
            by = int(m.groupdict()['by'])
            dist = self.calculates_the_distance((sx, sy), (bx, by))
            self.sensors.append(Sensor(sx, sy, dist))
            self.add_beacon_to_cave_if_not_exists(Beacon(bx, by))

    def calculates_the_distance(self, a: Tuple[int], b: Tuple[int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def is_within_distance(self, a: Tuple[int], b: Tuple[int], distance: int) -> bool:
        return self.calculates_the_distance(a, b) <= distance

    def add_beacon_to_cave_if_not_exists(self, beacon: Beacon) -> None:
        if not self.does_beacon_exist_in_given_coordinate(beacon.coordinate):
            self.beacons.append(beacon)
            self.beacon_coordinates_set.add(beacon.coordinate)

    def does_beacon_exist_in_given_coordinate(self, coordinate: Tuple[int]) -> bool:
        return coordinate in self.beacon_coordinates_set