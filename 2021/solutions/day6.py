'''
=========================================
|| 🎄 Advent of Code 2021: Day 6 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import collections

### Part One
def part_one(input): return helper(input, 80)

### Part Two
def part_two(input): return helper(input, 256)


def helper(input, total_days):
    lanternfish_ages = [int(val) for val in input[0].split(',')]
    ages_count = collections.Counter(lanternfish_ages)
    
    # Simulate the next 10 days
    next_10_days = [ages_count[day] for day in range(10)]

    # Move through the days, simulating the born of new lanternfishes
    for _ in range(total_days):
        cur_day = next_10_days.pop(0)
        if cur_day:
            next_10_days[6] += cur_day
            next_10_days[8] += cur_day
        next_10_days += [0]
    
    # Return the total amount of lanternfishes
    return sum(next_10_days)
