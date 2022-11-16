'''
=========================================
|| 🎄 Advent of Code 2021: Day 25 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

RIGHT = '>'
DOWN = 'v'
EMPTY = '.'

### Part One
def part_one(input):
    grid = [list(line.strip()) for line in input]
    height, width = len(grid), len(grid[0])

    step = 1
    while True:
        updated_grid = execute_step(grid, height, width)
        
        # Step without moving found
        if grid == updated_grid: return step

        grid = updated_grid
        step+=1

### Part Two
def part_two(input):
    return True


def execute_step(grid, height, width):
    temp_grid = [row.copy() for row in grid]

    for i in range(height):
        for j in range(width):
            next_j = (j+1) % width

            if grid[i][j] == RIGHT and grid[i][next_j] == EMPTY:
                temp_grid[i][j] = EMPTY
                temp_grid[i][next_j] = RIGHT

    grid = temp_grid
    temp_grid = [row.copy() for row in temp_grid]

    for i in range(height):
        for j in range(width):
            next_i = (i+1) % height

            if grid[i][j] == DOWN and grid[next_i][j] == EMPTY:
                temp_grid[i][j] = EMPTY
                temp_grid[next_i][j] = DOWN

    return temp_grid