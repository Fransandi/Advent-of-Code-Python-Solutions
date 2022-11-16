'''
=========================================
|| 🎄 Advent of Code 2021: Day 7 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from statistics import mean, median

### Part One
def part_one(input):
    positions = sorted([int(position) for position in input[0].split(',')])

    # The target position is the statistical median
    target_position = int(median(positions))

    # Calculate the minimum fuel required to reach the target position
    return sum([abs(target_position-cur_pos) for cur_pos in positions])

### Part Two
def part_two(input):
    positions = sorted([int(position) for position in input[0].split(',')])
    
    target_position_1 = int(mean(positions))
    target_position_2 = target_position_1+1

    # Calculate the fuel for 2 tentative target positions
    fuel_1 = calculate_fuel(positions, target_position_1)
    fuel_2 = calculate_fuel(positions, target_position_2)
    
    return min(fuel_1, fuel_2)


def calculate_fuel(positions, target_position):
    fuel = 0
    for position in positions:
        distance = abs(target_position-position)
        fuel += distance*(distance+1)//2

    return fuel
