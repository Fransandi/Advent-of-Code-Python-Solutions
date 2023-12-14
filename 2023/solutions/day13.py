'''
=========================================
|| 🎄 Advent of Code 2023: Day 13 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


ROW = 'ROW'
COL = 'COL'


# Part One
def part_one(input):
    grids = parse_input(input)
    total = 0
    for grid in grids:
        type, reflection = solve(grid)
        if type == COL:
            total += 100 * reflection
        elif type == ROW:
            total += reflection
    return total


# Part Two
def part_two(input):
    grids = parse_input(input)
    total = 0
    for grid in grids:
        prev_answer = solve(grid)
        found = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                updated_grid = grid.copy()
                updated_grid[i] = list(updated_grid[i])
                updated_grid[i][j] = "#" if updated_grid[i][j] == "." else "."
                updated_grid[i] = "".join(updated_grid[i])

                type, score = solve(updated_grid, prev_answer)

                if score and (type, score) != prev_answer:
                    total += 100 * score if type == COL else score
                    found = True
                    break

            if found:
                break

    return total


def parse_input(input):
    current, patterns = [], []
    for line in input:
        if line.strip():
            current.append(line.strip())
        else:
            patterns.append(current)
            current = []
    patterns.append(current)
    return patterns


def solve(grid, prev_answer=(None, 0)):
    # Check for reflection
    reflection = find_reflection(
        grid, prev_answer[1] if prev_answer[0] == COL else None)
    if reflection:
        return COL, reflection
    else:
        # Rotate matrix and check again
        reflection = find_reflection(rotate_matrix(
            grid), prev_answer[1] if prev_answer[0] == ROW else None)
        if reflection:
            return ROW, reflection
    return None, 0


def find_reflection(grid, prev_answer=None):
    for i in range(len(grid)-1):
        if grid[i] == grid[i + 1] and (prev_answer == None or i+1 != prev_answer):
            is_valid = validate_reflection(grid, i)
            if is_valid:
                return i + 1
    return 0


def validate_reflection(grid, start):
    rows = min(start+1, len(grid)-start-1)
    for i in range(0, rows):
        if (grid[start-i] != grid[start+1+i]):
            return False
    return True


def rotate_matrix(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))
    rotated_matrix = ["".join(row[::-1]) for row in transposed_matrix]
    return rotated_matrix
