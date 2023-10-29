#! /usr/bin/python3

from day_01_calorie_counting import day01
import pytest


class TestAOC2022:
    @pytest.fixture()
    def example_filename(self):
        return "example_input"

    @pytest.fixture()
    def filename(self):
        return "input"

    @pytest.fixture()
    def example_answer(self):
        return {"day01": [24000, 45000], "day02": [15, 12], "day03": [157, 70]}

    @pytest.fixture()
    def answer(self):
        return {
            "day01": [68467, 203420],
            "day02": [11666, 12767],
            "day03": [8139, 2668],
        }

    def test_day01_example(self, example_filename, example_answer):
        solution = day01.Solution(example_filename)
        assert solution.part1 == example_answer["day01"][0]
        assert solution.part2 == example_answer["day01"][1]

    def test_day01(self, filename, answer):
        solution = day01.Solution(filename)
        assert solution.part1 == answer["day01"][0]
        assert solution.part2 == answer["day01"][1]
