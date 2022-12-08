'''
=========================================
|| 🎄 Advent of Code 2022: Day 8 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    grid = [[int(cell) for cell in row.strip()] for row in input]
    height, width = len(grid), len(grid[0])
    count = 4 + (height-2)*2 + (width-2)*2

    for row in range(1, height-1):
        for col in range(1, width-1):
            count += int(is_visible(grid, row, col))

    return count

### Part Two
def part_two(input):
    grid = [[int(cell) for cell in row.strip()] for row in input]
    height, width = len(grid), len(grid[0])
    max_scenic_score = 0

    for row in range(1, height-1):
        for col in range(1, width-1):
            max_scenic_score = max(max_scenic_score, calculate_scenic_score(grid, row, col))

    return max_scenic_score


def ngbrs_to_left(grid, row, col): return grid[row][:col]

def ngbrs_to_right(grid, row, col): return grid[row][col+1:]

def ngbrs_to_top(grid, row, col): return [grid[r][col] for r in range(0,row)]

def ngbrs_to_bottom(grid, row, col): return [grid[r][col] for r in range(row+1,len(grid))]

def is_visible(grid, row, col):
    tree = grid[row][col]

    if all(ngbr < tree for ngbr in ngbrs_to_left(grid, row, col)): return True
    if all(ngbr < tree for ngbr in ngbrs_to_right(grid, row, col)): return True
    if all(ngbr < tree for ngbr in ngbrs_to_top(grid, row, col)): return True
    if all(ngbr < tree for ngbr in ngbrs_to_bottom(grid, row, col)): return True

    return False

def calculate_scenic_score(grid, row, col):
    tree = grid[row][col]

    scenic_score = count_visible_trees(tree, ngbrs_to_left(grid, row, col)[::-1])
    scenic_score *= count_visible_trees(tree, ngbrs_to_right(grid, row, col))
    scenic_score *= count_visible_trees(tree, ngbrs_to_top(grid, row, col)[::-1])
    scenic_score *= count_visible_trees(tree, ngbrs_to_bottom(grid, row, col))

    return scenic_score

def count_visible_trees(tree, neighbours):
    score = 0
    for ngbr in neighbours:
        score+=1
        if ngbr >= tree: break
    return score
