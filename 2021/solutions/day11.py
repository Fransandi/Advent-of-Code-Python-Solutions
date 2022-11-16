'''
=========================================
|| 🎄 Advent of Code 2021: Day 11 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

STEPS = 100
WIDTH = HEIGHT = 10
TOTAL_OCTOPUSES = WIDTH * HEIGHT
FLASHING_THRESHOLD = 10

### Part One
def part_one(input):
    octopuses_matrix = [[int(octopus) for octopus in list(row.strip())] for row in input]
    flashes_count = 0

    # Count all the flashes iterating every step
    for _ in range(STEPS):
        flashes_count += next_step(octopuses_matrix)

    return flashes_count

### Part Two
def part_two(input):
    octopuses_matrix = [[int(octopus) for octopus in list(row.strip())] for row in input]

    # Iterate steps until all octopuses are flashing
    step = 1
    while True:
        if next_step(octopuses_matrix) == TOTAL_OCTOPUSES: 
            return step
        step += 1


def next_step(octopuses_matrix):
    flashes_count = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            octopuses_matrix[i][j] += 1

            # Check the effects of an octopus flashing
            if octopuses_matrix[i][j] == FLASHING_THRESHOLD:
                flashes_count += octopus_flash(octopuses_matrix, i, j)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if octopuses_matrix[i][j] >= FLASHING_THRESHOLD:
                octopuses_matrix[i][j] = 0

    return flashes_count


def octopus_flash(octopuses_matrix, i, j):
    flashes_count = 1

    # Update all neighbours
    for n_i, n_j in valid_neighbours(i, j, HEIGHT, WIDTH):
        octopuses_matrix[n_i][n_j] += 1
            
        # Recursively check the effects of an adjacent octopus flashing
        if octopuses_matrix[n_i][n_j] == FLASHING_THRESHOLD:
            flashes_count += octopus_flash(octopuses_matrix, n_i, n_j)
    
    return flashes_count

def valid_neighbours(i, j, h, w):
    neighbours = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    return [n for n in neighbours if (min(n)>=0 and n[0]<h and n[1]<w)]