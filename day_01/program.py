import functools
import operator
from itertools import cycle


def solve_part_1(frequency_changes):
    return functools.reduce(operator.add, [int(x) for x in frequency_changes], 0)


def solve_part_2(frequency_changes):
    current, frequencies = 0, {0}

    for frequency_change in cycle(frequency_changes):
        current += int(frequency_change)

        if current in frequencies:
            return current

        frequencies.add(current)

    return current


if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()

    print(solve_part_1(puzzle_input))
    print(solve_part_2(puzzle_input))
