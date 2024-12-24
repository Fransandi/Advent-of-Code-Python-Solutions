'''
=========================================
|| 🎄 Advent of Code 2024: Day 18 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    # Parse falling bytes
    walls = []
    for line in input:
        x, y = line.strip().split(',')
        walls.append((int(x), int(y)))

    # Calculate size of grid
    height = max([y for _, y in walls]) + 1
    width = max([x for x, _ in walls]) + 1

    return walls, height, width


def build_grid(walls, height, width, steps=1024):
    # Build grid with walls up to a certain step
    return [['#' if (x, y) in walls[:steps] else '.' for x in range(width)] for y in range(height)]


def shortest_path(grid, width, height):
    # BFS to find shortest path from start to goal
    start = (0, 0)
    goal = (width - 1, height - 1)
    queue = [(start[0], start[1], 0)]
    while queue:
        x, y, distance = queue.pop(0)

        # If we reach the goal, return the distance
        if (x, y) == goal:
            return distance

        # If we've already visited this cell (or is a wall), skip it
        if grid[y][x] == '#':
            continue

        # Mark cell as visited
        grid[y][x] = '#'

        # Add neighbors to queue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            queue.append((nx, ny, distance + 1))

    return -1


# Part One
def part_one(input):
    # Parse input
    walls, height, width = parse_input(input)
    grid = build_grid(walls, height, width)

    # Return shortest path from start to goal
    return shortest_path(grid, width, height)


# Part Two
def part_two(input):
    # Parse input
    walls, height, width = parse_input(input)

    # Use binary search to find the first step where we can reach the goal
    reachable = set()
    left, right, step = 1, len(walls), None
    while left <= right:
        step = (left + right) // 2

        # If we've already explored this step, break
        if step in reachable:
            break

        # Explore the grid up to the current step
        grid = build_grid(walls, height, width, step)
        path = shortest_path(grid, width, height)

        # If we can reach the goal, update the left bound, else update the right bound
        if path == -1:
            right = step
        else:
            left = step
            reachable.add(step)

    # Return the first step where we can reach the goal
    return f"{walls[step][0]},{walls[step][1]}"
