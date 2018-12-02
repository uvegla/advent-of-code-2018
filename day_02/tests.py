from unittest import TestCase

from .program import solve_part_1, solve_part_2


class Day02TestCase(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(12, solve_part_1(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))

    def test_solve_part_2(self):
        self.assertEqual('fgij', solve_part_2(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']))
