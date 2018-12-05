import re
from collections import defaultdict
from itertools import combinations


def solve_part_1_and_part_2(lines):
    claims = parse(lines)

    claimed = defaultdict(int)
    overlaps, candidates = set(), set()

    for left, right in combinations(claims, 2):
        l_id, l_x, l_y, l_width, l_height = left
        r_id, r_x, r_y, r_width, r_height = right

        range_x = range(max(l_x, r_x), min(l_x + l_width, r_x + r_width))
        range_y = range(max(l_y, r_y), min(l_y + l_height, r_y + r_height))

        for coordinate in [(x, y) for x in range_x for y in range_y]:
            claimed[coordinate] += 1

            overlaps.update([l_id, r_id])
        else:
            candidates.update([l_id, r_id])

    return len(claimed), candidates.difference(overlaps)


def parse(lines):
    return [
        tuple(map(lambda x: int(x), t)) for t in [
            re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups() for line in lines
        ]
    ]


if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()

    print(solve_part_1_and_part_2(puzzle_input))
