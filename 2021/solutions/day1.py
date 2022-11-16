'''
=========================================
|| 🎄 Advent of Code 2021: Day 1 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    report = [int(line) for line in input]
    return calculate_increases(report)

### Part Two
def part_two(input):
    report = [int(line) for line in input]
    group_report = [sum(report[index:index+3]) for index in range(len(report)-2)]

    return calculate_increases(group_report)


def calculate_increases(group_report):
    increases_count = 0
    for index in range(len(group_report)-1):
        if group_report[index] < group_report[index+1]: increases_count += 1

    return increases_count
