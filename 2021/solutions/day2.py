'''
=========================================
|| 🎄 Advent of Code 2021: Day 2 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

### Part One
def part_one(input):
    instructions = [line.strip().split() for line in input]
    horizontal = depth = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        # Run through the instructions
        if direction == FORWARD: horizontal += distance
        elif direction == DOWN: depth += distance
        elif direction == UP: depth -= distance
    
    return horizontal*depth

### Part Two
def part_two(input):
    instructions = [line.strip().split() for line in input]
    horizontal = depth = aim = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])
        
        # Run through the instructions
        if direction == FORWARD:
            horizontal += distance
            depth += aim*distance
        elif direction == DOWN: aim += distance
        elif direction == UP: aim -= distance
    
    return horizontal*depth
