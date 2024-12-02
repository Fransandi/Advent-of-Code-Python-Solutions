'''
=========================================
|| 🎄 Advent of Code 2024: Day 2 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def report_is_safe(report):
    # Calculate differences
    differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]

    # Check if all differences have the same sign (increasing or decreasing)
    same_sign = all(diff * differences[0] > 0 for diff in differences)

    # Check if all absolute differences are between 0 and 3
    valid_levels = all(0 <= abs(diff) <= 3 for diff in differences)

    return same_sign and valid_levels


# Part One
def part_one(input):
    # Read input
    reports = [list(map(int, line.split())) for line in input]

    # Count safe reports
    return sum(report_is_safe(report) for report in reports)


# Part Two
def part_two(input):
    # Read input
    reports = [list(map(int, line.split())) for line in input]

    # Count safe reports
    safe_reports = 0
    for report in reports:
        # Remove one element at a time and check if the report is safe
        for i in range(len(report)):
            if report_is_safe(report[:i] + report[i + 1:]):
                safe_reports += 1
                break

    return safe_reports
