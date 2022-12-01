'''
=========================================
|| 🎄 Advent of Code 2022: Day 1 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

### Part One
def part_one(input):
    total_calories = get_total_calories(input)
    return max(total_calories)

### Part Two
def part_two(input):
    total_calories = get_total_calories(input)
    return sum(sorted(total_calories)[-3:])

def get_total_calories(input):
    calories = []
    temp = 0

    for line in input:
        if line == '\n':
            calories.append(temp)
            temp = 0
        else:
            temp += int(line)
    calories.append(temp)

    return calories