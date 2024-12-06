'''
=========================================
|| 🎄 Advent of Code 2024: Day 6 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


DIRECTIONS = {
    'UP': (-1, 0, 'RIGHT'),
    'RIGHT': (0, 1, 'DOWN'),
    'DOWN': (1, 0, 'LEFT'),
    'LEFT': (0, -1, 'UP'),
}


def parse_input(input):
    grid = [list(line.strip()) for line in input]

    # Find the guard starting position
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                guard_position = (i, j)
                break

    return grid, guard_position


def is_in_bounds(position, grid):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def evaluate_scenario(grid, guard_position):
    # Recreate the guard's path
    is_loop, path, direction = False, {}, 'UP'
    while is_in_bounds(guard_position, grid):

        # Update the path
        if guard_position not in path:
            path[guard_position] = set()
        path[guard_position].add(direction)

        # Next move
        next_position = (
            guard_position[0] + DIRECTIONS[direction][0],
            guard_position[1] + DIRECTIONS[direction][1],
        )

        # If the next position is out of bounds, break
        if not is_in_bounds(next_position, grid):
            break

        # Next move
        if grid[next_position[0]][next_position[1]] != '#':
            # If not obstacle, update the guard's position
            guard_position = next_position

        else:
            # If obstacle, change direction
            direction = DIRECTIONS[direction][2]

            # If the guard has been in this position, facing the same direction, a loop is found
            if guard_position in path and direction in path[guard_position]:
                is_loop = True
                break

    return path, is_loop


# Part One
def part_one(input):
    # Parse input
    grid, guard_position = parse_input(input)

    # Recreate the guard's path
    path, _ = evaluate_scenario(grid, guard_position)

    return len(path)


# Part Two
def part_two(input):
    # Parse input
    grid, guard_position = parse_input(input)

    # Recreate the guard's path
    path, _ = evaluate_scenario(grid, guard_position)

    # Evaluate all possible scenarios, adding obstacles one by one
    loop_count = 0
    for obstacle in list(path.keys()):
        grid_copy = [row[:] for row in grid]
        grid_copy[obstacle[0]][obstacle[1]] = '#'

        # Add 1, if a loop was found
        _, is_loop = evaluate_scenario(grid_copy, guard_position)
        loop_count += is_loop

    return loop_count
