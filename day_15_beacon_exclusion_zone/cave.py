#! /usr/bin/python3


import re
from typing import Dict, List, Tuple
import helper
from beacon import Beacon
from sensor import Sensor


class Cave:
    def __init__(self, lines: List[str]) -> None:
        self.sensors = []
        self.beacons = []
        self.beacon_coordinates_set = set()
        self.scans_the_cave(lines)

    # pylint: disable=C0116
    def scans_the_cave(self, lines: List[str]) -> None:
        for line in lines:
            m = re.match(
                r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",
                line,
            )
            sx = int(m.groupdict()["sx"])
            sy = int(m.groupdict()["sy"])
            bx = int(m.groupdict()["bx"])
            by = int(m.groupdict()["by"])
            dist = helper.calculates_the_distance((sx, sy), (bx, by))
            self.sensors.append(Sensor(sx, sy, dist))
            self.add_beacon_to_cave_if_not_exists(Beacon(bx, by))

    # pylint: disable=C0116
    def add_beacon_to_cave_if_not_exists(self, beacon: Beacon) -> None:
        """
        checks if given beacon exists already using the coordinate
        if not, add it, otherwise no op
        """
        if not self.does_beacon_exist_in_given_coordinate(beacon.coordinate):
            self.beacons.append(beacon)
            self.beacon_coordinates_set.add(beacon.coordinate)

    # pylint: disable=C0116
    def does_beacon_exist_in_given_coordinate(self, coordinate: Tuple[int]) -> bool:
        """
        checks if a beacon already recorded with the given coordinate
        """
        return coordinate in self.beacon_coordinates_set

    # pylint: disable=C0116
    def gets_sensors_that_are_close_enough(self) -> Dict[Sensor, List[Sensor]]:
        """
        gathers all the sensors that could intersect when distance + 1
        this is for part 2 solution
        """
        result = {}
        for i, sensor in enumerate(self.sensors):
            result[sensor] = []
            for j in range(i + 1, len(self.sensors)):
                for item in [
                    sensor.up_plus_one,
                    sensor.right_plus_one,
                    sensor.down_plus_one,
                    sensor.left_plus_one,
                ]:
                    # adding 1 distance to include sensors that are next to it
                    if helper.is_within_distance(
                        self.sensors[j].coordinate,
                        item,
                        self.sensors[j].detection_distance + 1,
                    ):
                        result[sensor].append(self.sensors[j])
                        break
        return result
