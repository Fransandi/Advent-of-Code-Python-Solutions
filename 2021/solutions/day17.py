'''
=========================================
|| 🎄 Advent of Code 2021: Day 17 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import re

### Part One
def part_one(input):
    target = parse_input(input)

    # Calculate last vertical movement's speed
    y_target = abs(target[2])-1

    # Here we calculate the max altitude according to the last movement from y=0 until the target
    return (y_target*(y_target+1))//2

### Part Two
def part_two(input):
    target = parse_input(input)

    # Calculate range of possible initial velocities in x
    vx_range = calculate_vx_range(target)

    # Calculate range of possible initial velocities in y
    vy_range = calculate_vy_range(target)

    # Simulate all possible velocities within the range to check if the target is reached
    count = 0
    for vx in range(vx_range[0], vx_range[1]+1):
        for vy in range(vy_range[0], vy_range[1]+1):
            if target_reached(vx, vy, target):
                count += 1

    return count


def parse_input(input):
    instructions = re.split('=|,|\.', input[0])
    return [int(val) for val in instructions[1::2]]

def calculate_vx_range(target):
    min_vx = distance = 0
    while distance < target[0]:
        min_vx += 1
        distance += min_vx

    return (min_vx, target[1])

def calculate_vy_range(target):
    y_target = abs(target[2])-1
    return (target[2], y_target)

def target_reached(vx, vy, target):
    pos_x = pos_y = 0
    while pos_x <= target[1] and pos_y >= target[2]:
        # The target was reached
        if pos_x >= target[0] and pos_y <= target[3]:
            return True

        pos_x += vx
        pos_y += vy
        vy -= 1
        if vx > 0: vx -= 1

    return False
