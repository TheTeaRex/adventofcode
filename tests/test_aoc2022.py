#! /usr/bin/python3

from day_01_calorie_counting import day01
from day_02_rock_paper_scissors import day02
from day_03_rucksack_reorganization import day03
from day_04_camp_cleanup import day04
from day_05_supply_stacks import day05
from day_06_tuning_trouble import day06
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
        return {
            "day01": [24000, 45000],
            "day02": [15, 12],
            "day03": [157, 70],
            "day04": [2, 4],
            "day05": ["CMZ", "MCD"],
            "day06": [11, 26],
        }

    @pytest.fixture()
    def answer(self):
        return {
            "day01": [68467, 203420],
            "day02": [11666, 12767],
            "day03": [8139, 2668],
            "day04": [556, 876],
            "day05": ["ZSQVCCJLL", "QZFJRWHGS"],
            "day06": [1080, 3645],
        }

    def test_example_input(self, instance, name, example_filename, example_answer):
        solution = instance.Solution(example_filename)
        assert solution.part1 == example_answer[name][0]
        assert solution.part2 == example_answer[name][1]

    def test_my_input(self, instance, name, filename, answer):
        solution = instance.Solution(filename)
        assert solution.part1 == answer[name][0]
        assert solution.part2 == answer[name][1]
