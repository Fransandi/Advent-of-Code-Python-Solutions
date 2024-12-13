'''
=========================================
|| 🎄 Advent of Code 2024: Day 12 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def is_within_bounds(grid, i, j):
    height, width = len(grid), len(grid[0])
    return 0 <= i < height and 0 <= j < width


def explore(grid, visited, i, j):
    # BFS to explore the section
    queue, positions, perimeter = [(i, j)], [], 0
    while queue:
        q_i, q_j = queue.pop(0)

        # Skip if already visited
        if (q_i, q_j) in visited:
            continue

        # Mark as visited
        visited.add((q_i, q_j))

        # Add the current cell to the section
        positions.append((q_i, q_j))

        # Get all neighbors with the same letter
        neighbors = []
        for ni, nj in [(q_i + i_next, q_j + j_next) for i_next, j_next in [(0, 1), (1, 0), (0, -1), (-1, 0)]]:
            if is_within_bounds(grid, ni, nj):
                if grid[ni][nj] == grid[q_i][q_j]:
                    neighbors.append((ni, nj))

        # Increment perimeter by 4 minus the number of neighbors
        perimeter += 4 - len(neighbors)

        # Add all non-visited neighbors to the queue
        queue.extend(
            [(ni, nj) for ni, nj in neighbors if (ni, nj) not in visited])

    # Return the section
    return {
        'char': grid[i][j],
        'positions': positions,
        'area': len(positions),
        'perimeter': perimeter
    }


def count_sides(grid, section):
    char, positions = section['char'], section['positions']

    # Get all the limits of the section, per direction
    limits = {'UP': [], 'DOWN': [], 'LEFT': [], 'RIGHT': []}
    for i, j in positions:
        if not is_within_bounds(grid, i - 1, j) or grid[i - 1][j] != char:
            limits['UP'].append((i, j))
        if not is_within_bounds(grid, i + 1, j) or grid[i + 1][j] != char:
            limits['DOWN'].append((i, j))
        if not is_within_bounds(grid, i, j - 1) or grid[i][j - 1] != char:
            limits['LEFT'].append((i, j))
        if not is_within_bounds(grid, i, j + 1) or grid[i][j + 1] != char:
            limits['RIGHT'].append((i, j))

    # Sort the positions for linear comparison, based on the direction
    limits['UP'].sort(key=lambda x: (x[0], x[1]))
    limits['DOWN'].sort(key=lambda x: (x[0], x[1]))
    limits['LEFT'].sort(key=lambda x: (x[1], x[0]))
    limits['RIGHT'].sort(key=lambda x: (x[1], x[0]))

    # Count the sides, for each direction
    sides = 0
    for limit in limits.items():
        direction, positions = limit
        sides += 1

        # Analyze each pair of positions
        for position in range(len(positions)-1):
            current, next = positions[position], positions[position+1]

            # Skip if the current pair is contiguous in the current direction
            if direction in ['UP', 'DOWN']:
                if current[0] == next[0] and abs(current[1] - next[1]) == 1:
                    continue
            elif direction in ['LEFT', 'RIGHT']:
                if current[1] == next[1] and abs(current[0] - next[0]) == 1:
                    continue

            # Increment the sides otherwise
            sides += 1

    return sides


# Part One
def part_one(input):
    # Parse the input
    grid = [list(line.strip()) for line in input]
    height, width = len(grid), len(grid[0])

    # Explore the grid
    price, visited = 0, set()
    for i in range(height):
        for j in range(width):
            # Explore a section if it's not visited already
            if (i, j) not in visited:
                section = explore(grid, visited, i, j)
                # Increment price by the area times the perimeter of the section
                price += section['area'] * section['perimeter']

    return price


# Part Two
def part_two(input):
    # Parse the input
    grid = [list(line.strip()) for line in input]
    height, width = len(grid), len(grid[0])

    # Explore the grid
    price, visited, sections = 0, set(), []
    for i in range(height):
        for j in range(width):
            # Explore a section if it's not visited already
            if (i, j) not in visited:
                section = explore(grid, visited, i, j)

                # Calculate the number of sides
                sides = count_sides(grid, section)

                # Increment the price by the area times the number of sides
                price += section['area'] * sides

    return price
