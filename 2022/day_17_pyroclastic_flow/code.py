#! /usr/bin/python3


import os
from rocks import CRock, HRock, LRock, Rock, SRock, VRock
from chamber import Chamber
from jet import Jet


class Solution(object):
    def __init__(self, filename: str, num: int) -> None:
        self.jet = Jet(self.read_file(filename))
        self.rock_id = 0
        self.part_one(num, Chamber())

    def read_file(self, file_name: str) -> str:
        f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
        text = f.read()
        f.close()
        return text

    def gets_new_rock(self, x: int, y: int) -> Rock:
        remainder = self.rock_id % 5
        if remainder == 0:
            rock = HRock(x, y)
        elif remainder == 1:
            rock = CRock(x, y)
        elif remainder == 2:
            rock = LRock(x, y)
        elif remainder == 3:
            rock = VRock(x, y)
        else: # remainder == 4
            rock = SRock(x, y)

        self.rock_id += 1
        return rock

    def checks_is_rock_location_valid(self, rock: Rock, chamber: Chamber) -> bool:
        for r in rock.space:
            if r[0] <= chamber.l_wall or\
                r[0] >= chamber.r_wall or\
                r[1] <= chamber.floor or\
                r in chamber.state:
                return False
        return True

    def part_one(self, num: int, chamber: Chamber) -> None:
        for i in range(num):
            rock = self.gets_new_rock(chamber.l_wall + 3, chamber.height + 4)
            while True:
                # attempting to move with sideway according to the jet
                delta = self.jet.current
                old_position = rock.position
                rock.updates_position(old_position[0] + delta[0], old_position[1] + delta[1])
                if not self.checks_is_rock_location_valid(rock, chamber):
                    rock.updates_position(old_position[0], old_position[1])

                # attempting to move downwards
                old_position = rock.position
                rock.updates_position(old_position[0], old_position[1] - 1)
                if not self.checks_is_rock_location_valid(rock, chamber):
                    rock.updates_position(old_position[0], old_position[1])
                    break

            chamber.state.update(rock.space)
            chamber.height = max(chamber.height, rock.height)

        print(f'Part 1: {chamber.height}')


if __name__ == "__main__":
    solution = Solution('input', 2022)