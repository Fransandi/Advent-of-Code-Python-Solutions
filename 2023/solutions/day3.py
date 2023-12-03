'''
=========================================
|| 🎄 Advent of Code 2023: Day 3 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    grid = [line.strip() for line in input]
    sum = 0
    for i, row in enumerate(grid):
        current, valid = "", False
        for j, cell in enumerate(row):
            if cell.isnumeric():
                current += cell
                if any_symbol_neighbours(grid, i, j):
                    valid = True
            else:
                if current and valid:
                    sum += int(current)
                current, valid = "", False
        
        if current and valid: 
            sum += int(current)

    return sum
    

### Part Two
def part_two(input):
    grid = [line.strip() for line in input]
    gear_candidates = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '*']
    sum = 0

    for (i, j) in gear_candidates:
        part_numbers = []
        
        # Check left and right
        part_numbers.append(get_part_number(grid, i, j-1))
        part_numbers.append(get_part_number(grid, i, j+1))

        # Check top
        if (i > 0 and grid[i-1][j].isnumeric()):
            part_numbers.append(get_part_number(grid, i-1, j))
        else:
            part_numbers.append(get_part_number(grid, i-1, j-1))
            part_numbers.append(get_part_number(grid, i-1, j+1))
        
        # Check bottom
        if (i < len(grid) - 1 and grid[i+1][j].isnumeric()):
            part_numbers.append(get_part_number(grid, i+1, j))
        else:
            part_numbers.append(get_part_number(grid, i+1, j-1))
            part_numbers.append(get_part_number(grid, i+1, j+1))

        # Sum gears
        part_numbers = [num for num in part_numbers if num != None]
        if len(part_numbers) == 2: 
            sum += part_numbers[0] * part_numbers[1]

    return sum
    

def any_symbol_neighbours(grid, i, j):
    for y in range(max(0, i - 1), min(i + 2, len(grid))):
        for x in range(max(0, j - 1), min(j + 2, len(grid[0]))):
            cell = grid[y][x]
            if not cell.isnumeric() and cell != ".":
                return True
    return False

def get_part_number(grid, i, j):
    # Check if out of bounds or not numeric
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or not grid[i][j].isnumeric(): 
        return None

    # Find the start and end of the part number
    pointer_left, pointer_right = j, j
    while pointer_left > 0 and grid[i][pointer_left - 1].isnumeric(): 
        pointer_left -= 1
    while pointer_right < len(grid[i]) - 1 and grid[i][pointer_right + 1].isnumeric(): 
        pointer_right += 1

    return int(grid[i][pointer_left:pointer_right + 1])

