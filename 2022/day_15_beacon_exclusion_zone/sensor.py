#! /usr/bin/python3


import helper


class Sensor:
    def __init__(self, x: int, y: int, detection_distance: int) -> None:
        self.coordinate = (x, y)
        self.detection_distance = detection_distance
        self.up_plus_one = (self.coordinate[0], self.coordinate[1] + self.detection_distance + 1)
        self.right_plus_one = (self.coordinate[0] + self.detection_distance + 1, self.coordinate[1])
        self.down_plus_one = (self.coordinate[0], self.coordinate[1] - self.detection_distance - 1)
        self.left_plus_one = (self.coordinate[0] - self.detection_distance - 1, self.coordinate[1])
        self.p_edge_plus_one = []
        self.n_edge_plus_one = []
        self.updates_plus_one_edges()

    def __repr__(self) -> str:
        result = f'Sensor coordinate: {self.coordinate}, '
        result += f'Distance to closest beacon: {self.detection_distance}'
        return result

    def updates_plus_one_edges(self) -> None:
        '''
        a function to update the edges with detection_distance + 1
        this is for part 2 of the solution
        '''
        if all([self.up_plus_one, self.right_plus_one, self.down_plus_one, self.left_plus_one]):
            lines = [
                (self.up_plus_one, self.right_plus_one),
                (self.right_plus_one, self.down_plus_one),
                (self.down_plus_one, self.left_plus_one),
                (self.left_plus_one, self.up_plus_one)
            ]
            for line in lines:
                if helper.gets_slope(line[0], line[1]) > 0:
                    self.p_edge_plus_one.append(line)
                else:
                    self.n_edge_plus_one.append(line)