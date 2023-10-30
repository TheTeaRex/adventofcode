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
    ],
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
        day10_part2 = '\n##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....'  # noqa: E501
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
        }

    @pytest.fixture()
    def answer(self):
        day10_part2 = '\n###..#..#..##..####..##....##.###..###..\n#..#.#.#..#..#....#.#..#....#.#..#.#..#.\n#..#.##...#..#...#..#..#....#.###..#..#.\n###..#.#..####..#...####....#.#..#.###..\n#.#..#.#..#..#.#....#..#.#..#.#..#.#.#..\n#..#.#..#.#..#.####.#..#..##..###..#..#.'  # noqa: E501
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
        }

    def test_example_input(self, instance, name, example_filename, example_answer):
        solution = instance.Solution(example_filename)
        assert solution.part1 == example_answer[name][0]
        assert solution.part2 == example_answer[name][1]

    def test_my_input(self, instance, name, filename, answer):
        solution = instance.Solution(filename)
        assert solution.part1 == answer[name][0]
        assert solution.part2 == answer[name][1]
