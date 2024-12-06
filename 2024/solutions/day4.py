'''
=========================================
|| 🎄 Advent of Code 2024: Day 4 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

STRAIGHT_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ALL_DIRECTIONS = STRAIGHT_DIRECTIONS + DIAGONAL_DIRECTIONS


def is_in_bounds(r, c, height, width):
    return 0 <= r < height and 0 <= c < width


# Part One
def part_one(input):
    # Parse input
    grid = [list(row.strip()) for row in input]
    height, width = len(grid), len(grid[0])

    # Explore the grid
    count = 0
    for row in range(height):
        for col in range(width):
            # If X found, check all directions
            if grid[row][col] == "X":
                for direction in ALL_DIRECTIONS:
                    i, r, c = 0, row, col
                    while is_in_bounds(r, c, height, width) and i < 4 and grid[r][c] == "XMAS"[i]:
                        r, c = r + direction[0], c + direction[1]
                        i += 1

                    # If XMAS found, increment count
                    if i == 4:
                        count += 1
    return count


# Part Two
def part_two(input):
    # Parse input
    grid = [list(row.strip()) for row in input]
    height, width = len(grid), len(grid[0])

    # Explore the grid
    count = 0
    for row in range(height):
        for col in range(width):
            # If A found, check all corners
            if grid[row][col] == "A":
                corners = [grid[row+r][col+c]
                           for r, c in DIAGONAL_DIRECTIONS if is_in_bounds(row+r, col+c, height, width)]

                # Check if corners form a valid X-MAS
                if "".join(corners) in ["MSMS", "SMSM", "MMSS", "SSMM"]:
                    count += 1
    return count
