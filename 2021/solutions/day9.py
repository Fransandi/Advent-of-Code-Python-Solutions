'''
=========================================
|| 🎄 Advent of Code 2021: Day 9 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    smoke_matrix = [[int(num) for num in list(row.strip())] for row in input]
    width, height = len(smoke_matrix[0]), len(smoke_matrix)
    low_points_count = 0

    for i in range(height):
        for j in range(width):
            # Check wether this is a low point
            if is_low_point(i, j, smoke_matrix, height, width):
                low_points_count += smoke_matrix[i][j]+1

    return low_points_count

### Part Two
def part_two(input):
    smoke_matrix = [[int(num) for num in list(row.strip())] for row in input]
    width, height = len(smoke_matrix[0]), len(smoke_matrix)
    basins = []

    for i in range(height):
        for j in range(width):
            # Check wether this is a low point
            if is_low_point(i, j, smoke_matrix, height, width):

                # Calculate basins' size recursively
                basin_size = calculate_basin_size(i, j, smoke_matrix, height, width)
                basins.append(basin_size)

    basins.sort()
    return (basins[-1]*basins[-2]*basins[-3])

def is_low_point(i, j, smoke_matrix, height, width):
    point = smoke_matrix[i][j]

    # Check all neighbours
    for n_i, n_j in valid_neighbours(i, j, height, width):
        if smoke_matrix[n_i][n_j] <= point: return False
    return True

def calculate_basin_size(i, j, smoke_matrix, height, width):
    # Base case
    if smoke_matrix[i][j] == 9: return 0
    
    smoke_matrix[i][j] = 9

    size = 1
    for n_i, n_j in valid_neighbours(i, j, height, width):
        size += calculate_basin_size(n_i, n_j, smoke_matrix, height, width)

    return size

def valid_neighbours(i, j, h, w):
    neighbours = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    return [n for n in neighbours if (min(n)>=0 and n[0]<h and n[1]<w)]