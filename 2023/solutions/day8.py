'''
=========================================
|| 🎄 Advent of Code 2023: Day 8 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import copy
import math


# Part One
def part_one(input):
    instructions, map = parse_input(input)
    steps, instruction = 0, 0

    node = "AAA"
    while True:
        node = map[node][instructions[instruction]]
        instruction = (instruction + 1) % len(instructions)
        steps += 1

        # Found
        if node == "ZZZ":
            return steps


# Part Two
def part_two(input):
    instructions, map = parse_input(input)
    steps, instruction = 0, 0
    start = [node for node in map.keys() if node.endswith("A")]
    nodes = copy.copy(start)

    positions = {i: [] for i in range(len(nodes))}
    while any([len(nodes) < 2 for nodes in positions.values()]):
        for i in range(len(nodes)):
            nodes[i] = map[nodes[i]][instructions[instruction]]

            if nodes[i].endswith("Z") and len(positions[i]) < 2:
                positions[i].append(steps)

        instruction = (instruction + 1) % len(instructions)
        steps += 1

    return math.lcm(*[r[1] - r[0] for r in positions.values()])


def parse_input(input):
    instructions, map = "", {}
    for line in [line.strip() for line in input]:
        if line.strip():
            if not instructions:
                instructions = line
            else:
                node, children = [value.strip() for value in line.split("=")]
                children = children[1:-1].split(", ")
                map[node] = {
                    'L': children[0],
                    'R': children[1]
                }

    return instructions, map
