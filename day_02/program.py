from collections import Counter
from itertools import product


def solve_part_1(box_ids):
    twos, threes = 0, 0

    for box_id in box_ids:
        counter = list(Counter(box_id).values())

        twos += min(1, counter.count(2))
        threes += min(1, counter.count(3))

    return twos * threes


def solve_part_2(box_ids):
    box_ids = [x.strip() for x in box_ids]
    for left, right in product(box_ids, box_ids):
        comparison = [x != y for x, y in zip(left, right)]

        if sum(comparison) == 1:
            return ''.join([x for index, x in enumerate(left) if not comparison[index]])

    return ''


if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()

    print(solve_part_1(puzzle_input))
    print(solve_part_2(puzzle_input))
