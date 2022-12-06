'''
=========================================
|| 🎄 Advent of Code 2022: Day 6 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    return helper(input[0], 4)

### Part Two
def part_two(input):
    return helper(input[0], 14)

def helper(datastream, marker):
    for i in range(marker, len(datastream)+1):
        if len(set(datastream[i-marker:i]))==marker: return i