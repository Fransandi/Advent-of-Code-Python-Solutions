'''
=========================================
|| 🎄 Advent of Code 2021: Day 14 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from typing import DefaultDict

### Part One
def part_one(input): return helper(input, 10)

### Part Two
def part_two(input): return helper(input, 40)


def helper(input, steps):
    polymer, rules = [], {}

    # Parse input
    for i, line in enumerate(input):
        if i == 0: polymer = line.strip()
        if i > 1:
            pair, new_char = line.strip().split(' -> ')
            rules[pair] = [pair[0]+new_char, new_char+pair[1]]

    # Count initial pairs
    pair_count = DefaultDict(int)
    for i in range(len(polymer)-1):
        pair_count[polymer[i]+polymer[i+1]] += 1

    # Iterate steps updating pairs count
    for i in range(steps):
        temp = DefaultDict(int)
        for pair in pair_count.keys():
            for new_pair in rules[pair]:
                temp[new_pair] += pair_count[pair]
        pair_count = temp

    # Count chars
    char_count = DefaultDict(int)
    char_count[polymer[0]] += 1
    char_count[polymer[-1]] += 1
    for pair in pair_count.keys():
        char_count[pair[0]] += pair_count[pair]
        char_count[pair[1]] += pair_count[pair]

    # Calculate return value
    sorted_count = sorted(count//2 for count in char_count.values())
    return sorted_count[-1]-sorted_count[0]
