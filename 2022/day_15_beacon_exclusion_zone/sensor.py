#! /usr/bin/python3


class Sensor:
    def __init__(self, x: int, y: int, distance_to_closest_beacon: int) -> None:
        self.coordinate = (x, y)
        self.distance_to_closest_beacon = distance_to_closest_beacon

    def __repr__(self) -> str:
        result = f'Sensor coordinate: {self.coordinate}, '
        result += f'Distance to closest beacon: {self.distance_to_closest_beacon}'
        return result
