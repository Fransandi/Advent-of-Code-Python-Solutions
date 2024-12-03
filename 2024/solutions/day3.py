'''
=========================================
|| 🎄 Advent of Code 2024: Day 3 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import re


# Part One
def part_one(input):
    # Parse Input
    program = "".join(input)

    # Find all mul() operations
    matches = re.findall(r"mul\((\d+),(\d+)\)", program)

    # Sum all the results of the mul operations
    return sum(int(n1) * int(n2) for n1, n2 in matches)


# Part Two
def part_two(input):
    # Parse Input
    program = "".join(input)

    # Remove all disabled instructions from the program
    while "don't()" in program:
        dont = program.find("don't()")
        next_do = program.find(
            "do()", dont) if "do()" in program[dont:] else len(program)
        program = program[:dont] + program[next_do + 3:]

    # Find all mul() operations
    matches = re.findall(r"mul\((\d+),(\d+)\)", program)

    # Sum all the results of the mul operations
    return sum(int(n1) * int(n2) for n1, n2 in matches)
