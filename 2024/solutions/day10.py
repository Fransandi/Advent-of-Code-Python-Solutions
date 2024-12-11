'''
=========================================
|| 🎄 Advent of Code 2024: Day 10 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

def is_within_bounds(grid, i, j):
    height, width = len(grid), len(grid[0])
    return 0 <= i < height and 0 <= j < width

def get_neighbors(grid, i, j):
    return [n for n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if is_within_bounds(grid, n[0], n[1])]


### Part One
def part_one(input):
    # Parse input
    grid = [list(line.strip()) for line in input]

    # Find all trailheads
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '0':
                trailheads.append((0, i, j))

    # BFS to find all trails
    score = 0
    for trailhead in trailheads:
        queue = [trailhead]
        trails = set()
        while queue:
            value, i, j = queue.pop(0)

            # Base case: if we've reached the end, add to trails
            if value == 9:
                trails.add((i, j))
                continue

            # Add all valid neighbors to the queue
            for (next_i, next_j) in get_neighbors(grid, i, j):
                if grid[next_i][next_j] == str(value + 1):
                    queue.append((value + 1, next_i, next_j))

        score += len(trails)

    return score
        

### Part Two
def part_two(input):
    # Parse input
    grid = [list(line.strip()) for line in input]

    # Find all trailheads
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '0':
                trailheads.append((0, i, j))

    # BFS to find all trails
    score = 0
    for trailhead in trailheads:
        queue = [trailhead]
        while queue:
            value, i, j = queue.pop(0)

            # Base case: if we've reached the end, increment score
            if value == 9:
                score += 1
                continue

            # Add all valid neighbors to the queue
            for (next_i, next_j) in get_neighbors(grid, i, j):
                if grid[next_i][next_j] == str(value + 1):
                    queue.append((value + 1, next_i, next_j))

    return score
    