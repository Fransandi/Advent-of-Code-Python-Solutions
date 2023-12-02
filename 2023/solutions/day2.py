'''
=========================================
|| 🎄 Advent of Code 2023: Day 2 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

### Part One
def part_one(input):
    possible = 0
    color_limits = { RED: 12, GREEN: 13, BLUE: 14 }

    for i, line in enumerate(input):
        cubes = [cube.strip() for cube in line.split(':')[1].replace(';', ',').split(',')]

        # Check if all cubes are within the limits
        if all(int(cube.split()[0]) <= color_limits.get(cube.split()[1], 0) for cube in cubes):
            possible += i+1

    return possible
    

### Part Two
def part_two(input):
    power = 0
    for line in input:
        cubes = [cube.strip() for cube in line.split(':')[1].replace(';', ',').split(',')]
        max_count = { RED: 0, GREEN: 0, BLUE: 0 }

        # Find the max amount of each color
        for cube in cubes:
            amount, color = cube.split()
            max_count[color] = max(max_count[color], int(amount))

        # Calculate the power
        power += max_count[RED] * max_count[GREEN] * max_count[BLUE]
    
    return power
