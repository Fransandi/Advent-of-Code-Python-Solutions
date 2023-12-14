'''
=========================================
|| 🎄 Advent of Code 2023: Day 14 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# Part One
def part_one(input):
    grid = [list(line.strip()) for line in input]
    grid = tilt(grid)
    return calculate_load(grid)


# Part Two
def part_two(input):
    grid = [list(line.strip()) for line in input]
    sample_limits = (200, 300)
    sample = []
    for i in range(sample_limits[1]):
        # Entire cycle
        for _ in range(4):
            grid = tilt(grid)
            grid = rotate_matrix(grid)

        # Save load in a sample
        if i >= sample_limits[0]:
            sample.append(calculate_load(grid))

    # Find cycle and predict load from sample
    cycle_start = find_cycle_start(sample)
    if cycle_start:
        return sample[(1000000000 - sample_limits[0] - 1) % cycle_start]
    else:
        print('No cycle found. Try ajusting the cycle sample limits.')


def tilt(grid):
    for row in range(len(grid[0])):
        pointer = 0
        while pointer <= len(grid) - 1:
            move_pointer = pointer
            while move_pointer > 0 and grid[move_pointer][row] == 'O' and grid[move_pointer-1][row] == '.':
                grid[move_pointer][row] = '.'
                grid[move_pointer-1][row] = 'O'
                move_pointer -= 1
            pointer += 1
    return grid


def calculate_load(mat):
    total = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'O':
                total += len(mat) - i
    return total


def rotate_matrix(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    rotated_matrix = [row[::-1] for row in transposed_matrix]
    return rotated_matrix


def find_cycle_start(nums):
    candidates = [i for i in range(1, len(nums)) if nums[i] == nums[0]]

    while candidates:
        start = candidates.pop(0)
        # Cycle start found
        if nums[:start] == nums[start:start+start]:
            return start
    return
