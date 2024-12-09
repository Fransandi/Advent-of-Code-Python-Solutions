'''
=========================================
|| 🎄 Advent of Code 2024: Day 8 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import itertools


def parse_input(input):
    grid = []
    for line in input:
        grid.append([c for c in line.strip()])

    antennas = {}
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != '.':
                antennas[char] = antennas.get(char, []) + [(i, j)]

    return grid, antennas, len(grid[0]), len(grid)


def is_within_grid(position, height, width):
    return 0 <= position[0] < height and 0 <= position[1] < width

# Part One


def part_one(input):
    # Parse the input
    grid, antennas, width, height = parse_input(input)
    antinodes = set()

    # Find all the antinodes
    for antenna, coords in antennas.items():
        # Find all combinations of two antennas of the same type
        all_combinations_of_two = list(itertools.combinations(coords, 2))

        for a1, a2 in all_combinations_of_two:
            # Calculate the absolute difference between the two antennas
            diff_y = abs(a1[0] - a2[0])
            diff_x = abs(a1[1] - a2[1])

            # Check if the first antenna is to the left of the second antenna
            a1_is_left = a1[1] <= a2[1]

            # Calculate the coordinates of the antinodes
            a1 = (a1[0] - diff_y, a1[1] -
                  diff_x if a1_is_left else a1[1] + diff_x)
            a2 = (a2[0] + diff_y, a2[1] +
                  diff_x if a1_is_left else a2[1] - diff_x)

            # Add the antinodes to the set if they are within the grid
            if is_within_grid(a1, height, width):
                antinodes.add(a1)

            if is_within_grid(a2, height, width):
                antinodes.add(a2)

    return len(antinodes)


# Part Two
def part_two(input):
    # Parse the input
    grid, antennas, width, height = parse_input(input)
    antinodes = set()

    # Add the antennas to the antinodes
    for antenna, coords in antennas.items():
        for coord in coords:
            antinodes.add(coord)

    # Find all the antinodes, considering the resonant harmonics rule
    for antenna, coords in antennas.items():
        # Find all combinations of two antennas of the same type
        all_combinations_of_two = list(itertools.combinations(coords, 2))

        for a1, a2 in all_combinations_of_two:
            # Calculate the absolute difference between the two antennas
            diff_y = abs(a1[0] - a2[0])
            diff_x = abs(a1[1] - a2[1])

            # Check if the first antenna is to the left of the second antenna
            a1_is_left = a1[1] <= a2[1]

            # Calculate the coordinates of all the valid with the grid
            while is_within_grid(a1, height, width):
                a1 = (a1[0] - diff_y, a1[1] -
                      diff_x if a1_is_left else a1[1] + diff_x)

                if is_within_grid(a1, height, width):
                    antinodes.add(a1)

            while is_within_grid(a2, height, width):
                a2 = (a2[0] + diff_y, a2[1] +
                      diff_x if a1_is_left else a2[1] - diff_x)

                if is_within_grid(a2, height, width):
                    antinodes.add(a2)

    return len(antinodes)
