import re
from collections import defaultdict
from datetime import datetime


def solve_part_1_and_part_2(lines):
    records = collect_records(lines)

    return solve_part_1(records), solve_part_2(records)


def solve_part_1(records):
    leader_board = [
        (guard, records[guard]) for guard in sorted(records, key=lambda k: records[k]['overall'], reverse=True)
    ]

    leader_id, leader_record = leader_board[0]
    return leader_id * max(leader_record['minutes'], key=leader_record['minutes'].get)


def solve_part_2(records):
    leader_board = [
        (guard, records[guard]) for guard in sorted(
            records, key=lambda k: max(records[k]['minutes'].values() or [0]), reverse=True
        )
    ]

    leader_id, leader_record = leader_board[0]
    return leader_id * max(leader_record['minutes'], key=lambda k: leader_record['minutes'][k])


def collect_records(lines):
    records, current_guard, fall_asleep_time = {}, '', 0

    for moment, action in parse(lines):
        if action.startswith('Guard'):
            current_guard = int(re.search(r'Guard #(\d+) begins shift', action).group(1))
            records.setdefault(current_guard, {
                'overall': 0,
                'minutes': defaultdict(int)
            })
        elif action == 'falls asleep':
            fall_asleep_time = moment.minute
        else:
            wake_up_time = moment.minute

            for minute in range(fall_asleep_time, wake_up_time):
                records[current_guard]['overall'] += 1
                records[current_guard]['minutes'][minute] += 1

    return records


def parse(lines):
    logs = [
        (datetime.strptime(moment, '%Y-%m-%d %H:%M'), action) for moment, action in [
            re.search(r'\[(.+)\] (.+)', line).groups() for line in lines
        ]
    ]

    logs.sort(key=lambda t: t[0])

    return logs


if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()

    print(solve_part_1_and_part_2(puzzle_input))
