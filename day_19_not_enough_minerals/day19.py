#! /usr/bin/python3


import copy
import math
import os
import re
from typing import Dict, List, Tuple


class Solution:
    def __init__(self, filename: str) -> None:
        """
        bps: stores all the blueprints
        [bp] -> [[ore robot recipe], [clay robot recipe], [obsidian robot recipe], [geode robot recipe]]
        bps_max_mats: used to store the highest required material for building robots
        set_blueprints(): parse the read file
        cur_max: use as a global var in this class
        part1: answer to part 1, need to run self.solution1() to calculate the answer though
        part2: answer to part 2, need to run self.solution2() to calculate the answer though
        """
        lines = self.read_file(filename).split("\n")
        self.mats = ["ore", "clay", "obsidian"]
        self.bps = []
        self.bps_max_mats = []
        self.set_blueprints(lines)
        self.cur_max = 0
        self.part1 = 0
        self.part2 = 1
        self.solution1()
        print(f"Part 1: {self.part1}")
        self.solution2()
        print(f"Part 2: {self.part2}")

    def read_file(self, filename: str) -> str:
        """
        Typical file read
        Output: the str of the file
        """
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}",
            "r",
            encoding="utf-8",
        ) as f:
            text = f.read()
        return text

    def set_blueprints(self, lines: List[str]) -> None:
        """
        Given the list of str after reading in the file
        parse the list of str to our data structure of sort
        """
        for line in lines:
            bp = []
            mats_required = [0, 0, 0]
            robot_recipes = line.split(": ")[1].split(". ")
            for robot in robot_recipes:
                recipe = []
                for quatity, ingredient in re.findall(r"(\d+) (\w+)", robot):
                    i = int(quatity)
                    j = self.mats.index(ingredient)
                    recipe.append((i, j))
                    mats_required[j] = max(mats_required[j], i)
                bp.append(recipe)
            # bp = [recipe for ore robot, recipe for clay robot, recipe for obsidian robot, recipe for geode robot]
            self.bps.append(bp)
            self.bps_max_mats.append(mats_required)

    def get_potential_max_geode(self, time: int) -> int:
        """
        Given the time, it will give you what is the potential geode you can get
        assuming that you can build a robot every min
        """
        if time <= 1:
            return 0
        result = 0
        for i in range(time - 1):
            result += i + 1
        return result

    def dfs(  # noqa: C901
        self,
        bp: List[List[Tuple[int, int]]],
        max_mats: List[int],
        cache: Dict[List[int], int],
        time: int,
        robots: List[int],
        mats: List[int],
    ):
        """
        Given a blueprint, use DFS to return the highest amount of geode that you can farm

        Note: Pruning/optimization technic from the internet
        - For each robot type, we only build X of them that is equal to the max amount required to build any robots
          So if the most expensive robot requires 4 ores, then we only build 4 ore robots for that blueprint
        - Calculate the potential maximum of geode by assuming that we can build a geode robot at each time step.
          If that estimation is less or equal than the currently known maximal amount of geode, move on
        - Caching
        - Implement time skip for fast forward to a period with the robot built
        """
        if time == 0:
            return mats[3]

        index = tuple([time] + robots + mats)
        if index in cache:
            return cache[index]

        max_geode = mats[3] + robots[3] * time

        for i, recipe in enumerate(bp):
            if i != 3 and robots[i] >= max_mats[i]:
                continue

            if self.cur_max >= max_geode + self.get_potential_max_geode(time):
                continue

            time_skip = 0
            for mat_required, mat_index in recipe:
                # if we dont' have that specific robot, can't farm that mat, so no point for timeskipping
                if robots[mat_index] == 0:
                    break
                time_skip = max(
                    time_skip,
                    math.ceil((mat_required - mats[mat_index]) / robots[mat_index]),
                )
            else:
                time_left = time - time_skip - 1
                # no time left after time_skip, move on
                if time_left <= 0:
                    continue
                new_robots = copy.deepcopy(robots)
                new_mats = [x + (y * (time_skip + 1)) for x, y in zip(mats, robots)]
                for amt, item in recipe:
                    new_mats[item] -= amt
                new_robots[i] += 1

                for a in range(3):
                    new_mats[a] = min(new_mats[a], max_mats[a] * time_left)

                max_geode = max(
                    max_geode,
                    self.dfs(bp, max_mats, cache, time_left, new_robots, new_mats),
                )

        cache[index] = max_geode
        self.cur_max = max(self.cur_max, max_geode)
        return max_geode

    def solution1(self) -> None:
        """
        Run this to calculate part 1's answer
        the answer is store in self.part1
        """
        for i, bp in enumerate(self.bps):
            self.cur_max = 0
            self.part1 += (i + 1) * self.dfs(
                bp, self.bps_max_mats[i], {}, 24, [1, 0, 0, 0], [0, 0, 0, 0]
            )

    def solution2(self) -> None:
        """
        Run this to calculate part 2's answer
        the answer is store in self.part2
        """
        for i, bp in enumerate(self.bps[:3]):
            self.cur_max = 0
            self.part2 *= self.dfs(
                bp, self.bps_max_mats[i], {}, 32, [1, 0, 0, 0], [0, 0, 0, 0]
            )


if __name__ == "__main__":
    solution = Solution("example_input")
