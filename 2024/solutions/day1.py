'''
=========================================
|| 🎄 Advent of Code 2024: Day 1 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# Part One
def part_one(input):
    # Read input
    left, right = zip(*(map(int, line.split()) for line in input))

    # Calculate sum of absolute differences between the sorted lists
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


# Part Two
def part_two(input):
    # Read input
    left, right = zip(*(map(int, line.split()) for line in input))

    # Calculate sum of products between left numbers and their count in right
    return sum(l * right.count(l) for l in left)
