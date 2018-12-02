from unittest import TestCase

from .program import solve_part_1, solve_part_2


class Day01TestCase(TestCase):
    def test_solve_part_1_empty(self):
        self.assertEqual(0, solve_part_1([]))

    def test_solve_part_1_example_1(self):
        self.assertEqual(3, solve_part_1(['+1', '+1', '+1']))

    def test_solve_part_1_example_2(self):
        self.assertEqual(0, solve_part_1(['+1', '+1', '-2']))

    def test_solve_part_1_example_3(self):
        self.assertEqual(-6, solve_part_1(['-1', '-2', '-3']))

    def test_solve_part_2_empty(self):
        self.assertEqual(0, solve_part_2([]))

    def test_solve_part_2_example_1(self):
        self.assertEqual(0, solve_part_2(['+1', '-1']))

    def test_solve_part_2_example_2(self):
        self.assertEqual(10, solve_part_2(['+3', '+3', '+4', '-2', '-4']))

    def test_solve_part_2_example_3(self):
        self.assertEqual(5, solve_part_2(['-6', '+3', '+8', '+5', '-6']))

    def test_solve_part_2_example_4(self):
        self.assertEqual(14, solve_part_2(['+7', '+7', '-2', '-7', '-4']))
