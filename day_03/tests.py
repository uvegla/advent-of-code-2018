from unittest import TestCase

from .program import solve_part_1_and_part_2


class Day03TestCase(TestCase):
    def test_solve_part_1_and_part_2(self):
        self.assertEqual((4, {3}), solve_part_1_and_part_2([
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2'
        ]))
