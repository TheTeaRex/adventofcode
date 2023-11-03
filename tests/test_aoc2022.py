#! /usr/bin/python3

from day_01_calorie_counting import day01
from day_02_rock_paper_scissors import day02
from day_03_rucksack_reorganization import day03
from day_04_camp_cleanup import day04
from day_05_supply_stacks import day05
from day_06_tuning_trouble import day06
from day_07_no_space_left_on_device import day07
from day_08_treetop_tree_house import day08
from day_09_rope_bridge import day09
from day_10_cathod_ray_tube import day10
from day_11_monkey_in_the_middle import day11
from day_12_hill_climbing_algorithm import day12
from day_13_distress_signal import day13
from day_14_regolith_reservoir import day14
from day_15_beacon_exclusion_zone import day15
from day_16_proboscidea_volcanium import day16
from day_17_pyroclastic_flow import day17
from day_18_boiling_boulders import day18
from day_19_not_enough_minerals import day19
from day_20_grove_positioning_system import day20
from day_21_monkey_math import day21

# missing day22
from day_23_unstable_diffusion import day23
import pytest


@pytest.mark.parametrize(
    "instance, name",
    [
        (day01, "day01"),
        (day02, "day02"),
        (day03, "day03"),
        (day04, "day04"),
        (day05, "day05"),
        (day06, "day06"),
        (day07, "day07"),
        (day08, "day08"),
        (day09, "day09"),
        (day10, "day10"),
        (day11, "day11"),
        (day12, "day12"),
        (day13, "day13"),
        (day14, "day14"),
        (day15, "day15"),
        (day16, "day16"),
        (day17, "day17"),
        (day18, "day18"),
        (day19, "day19"),
        (day20, "day20"),
        (day21, "day21"),
        (day23, "day23"),
    ],
    scope="session",
)
class TestAOC2022:
    @pytest.fixture()
    def example_filename(self):
        return "example_input"

    @pytest.fixture()
    def filename(self):
        return "input"

    @pytest.fixture()
    def example_answer(self):
        day10_part2 = "\n##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######....."  # noqa: E501
        return {
            "day01": [24000, 45000],
            "day02": [15, 12],
            "day03": [157, 70],
            "day04": [2, 4],
            "day05": ["CMZ", "MCD"],
            "day06": [11, 26],
            "day07": [95437, 24933642],
            "day08": [21, 8],
            "day09": [88, 36],
            "day10": [13140, day10_part2],
            "day11": [10605, 2713310158],
            "day12": [31, 29],
            "day13": [13, 140],
            "day14": [24, 93],
            "day15": [26, 56000011],
            "day16": [1651, 1707],
            "day17": [3068, 1514285714288],
            "day18": [64, 58],
            "day19": [33, 3472],
            "day20": [3, 1623178306],
            "day21": [152, 301],
            "day23": [110, 20],
        }

    @pytest.fixture()
    def answer(self):
        day10_part2 = "\n###..#..#..##..####..##....##.###..###..\n#..#.#.#..#..#....#.#..#....#.#..#.#..#.\n#..#.##...#..#...#..#..#....#.###..#..#.\n###..#.#..####..#...####....#.#..#.###..\n#.#..#.#..#..#.#....#..#.#..#.#..#.#.#..\n#..#.#..#.#..#.####.#..#..##..###..#..#."  # noqa: E501
        return {
            "day01": [68467, 203420],
            "day02": [11666, 12767],
            "day03": [8139, 2668],
            "day04": [556, 876],
            "day05": ["ZSQVCCJLL", "QZFJRWHGS"],
            "day06": [1080, 3645],
            "day07": [1490523, 12390492],
            "day08": [1713, 268464],
            "day09": [6503, 2724],
            "day10": [16880, day10_part2],
            "day11": [58794, 20151213744],
            "day12": [456, 454],
            "day13": [5557, 22425],
            "day14": [1133, 27566],
            "day15": [5878678, 11796491041245],
            "day16": [2056, 2513],
            "day17": [3159, 1566272189352],
            "day18": [3396, 2044],
            "day19": [2301, 10336],
            "day20": [2622, 1538773034088],
            "day21": [291425799367130, 3219579395609],
            "day23": [4195, 1069],
        }

    def test_example_input(self, instance, name, example_filename, example_answer):
        solution = instance.Solution(example_filename)
        assert solution.part1 == example_answer[name][0]
        assert solution.part2 == example_answer[name][1]

    def test_my_input(self, instance, name, filename, answer):
        solution = instance.Solution(filename)
        assert solution.part1 == answer[name][0]
        assert solution.part2 == answer[name][1]
