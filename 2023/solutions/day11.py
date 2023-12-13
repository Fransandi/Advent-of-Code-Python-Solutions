'''
=========================================
|| 🎄 Advent of Code 2023: Day 11 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# Part One
def part_one(input):
    return helper(input, 1)


# Part Two
def part_two(input):
    return helper(input, 999999)


def helper(input, n=1):
    galaxies, empty_rows, empty_cols = parse_input(input)
    galaxies = expand_space(galaxies, empty_rows, empty_cols, n)
    return calculate_distance(galaxies)


def parse_input(input):
    mat = [line.strip() for line in input]
    galaxies, empty_rows, empty_cols = [], [], []

    # Count galaxies
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '#':
                galaxies.append((i, j))

    # Find empty rows
    for row in range(len(mat)):
        if all([x == '.' for x in mat[row]]):
            empty_rows.append(row)

    # Find empty cols
    for col in range(len(mat[0])):
        if all([mat[row][col] == '.' for row in range(len(mat))]):
            empty_cols.append(col)

    return galaxies, empty_rows, empty_cols


def expand_space(galaxies, empty_rows, empty_cols, n):
    for i in range(len(galaxies)):
        galaxies[i] = (galaxies[i][0] + sum([n for row in empty_rows if row < galaxies[i][0]]),
                       galaxies[i][1] + sum([n for col in empty_cols if col < galaxies[i][1]]))

    return galaxies


def calculate_distance(galaxies):
    distance = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance += abs(galaxies[i][0] - galaxies[j][0]) + \
                abs(galaxies[i][1] - galaxies[j][1])

    return distance
