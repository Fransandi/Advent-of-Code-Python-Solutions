'''
=========================================
|| 🎄 Advent of Code 2024: Day 16 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import heapq

UP, DOWN, LEFT, RIGHT = 'UP', 'DOWN', 'LEFT', 'RIGHT'
START, WALL, GOAL = 'S', '#', 'E'


def get_next_position(i, j, direction):
    return {
        UP: (i - 1, j),
        DOWN: (i + 1, j),
        LEFT: (i, j - 1),
        RIGHT: (i, j + 1)
    }[direction]


def get_neighbors(grid, i, j, direction):
    neighbors = []

    # Explore move in the current direction
    next_position = get_next_position(i, j, direction)
    if grid[next_position[0]][next_position[1]] != WALL:
        neighbors.append((next_position, 1, direction))

    # Explore moves in the adjacent directions
    for next_direction in {
        UP: [LEFT, RIGHT],
        DOWN: [LEFT, RIGHT],
        LEFT: [UP, DOWN],
        RIGHT: [UP, DOWN]
    }[direction]:
        next_position = get_next_position(i, j, next_direction)
        if grid[next_position[0]][next_position[1]] != WALL:
            neighbors.append((next_position, 1001, next_direction))

    return neighbors


def dijkstra(grid, start, start_direction=RIGHT):
    # Initialize the distance dictionary
    distances = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            distances[(i, j)] = 0 if (i, j) == start else float('inf')

    # Dijkstra algorithm
    priority_queue = [(start, 0, start_direction)]
    while priority_queue:
        current_position, current_distance, current_direction = heapq.heappop(
            priority_queue)

        # Skip processing if we already have a shorter path
        if current_distance > distances[current_position]:
            continue

        # Explore neighbors
        for neighbor, weight, direction in get_neighbors(grid, current_position[0], current_position[1], current_direction):
            distance = current_distance + weight

            # If a shorter path is found, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(
                    priority_queue, (neighbor, distance,  direction))

    return distances


# Part One
def part_one(input):
    # Parse input
    grid = [list(line.strip()) for line in input]

    # Find the start and goal positions
    start, goal = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == START:
                start = (i, j)
            elif grid[i][j] == GOAL:
                goal = (i, j)

    # Use the Dijkstra algorithm to find the shortest path
    distances = dijkstra(grid, start)

    # Return the minimum distance to the goal
    return distances[goal]


# Part Two
def part_two(input):
    # Parse input
    grid = [list(line.strip()) for line in input]

    # Find the start and goal positions
    start, goal = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == START:
                start = (i, j)
            elif grid[i][j] == GOAL:
                goal = (i, j)

    # Use the Dijkstra algorithm to find the shortest path from the start to the goal
    distances_from_start = dijkstra(grid, start, RIGHT)

    # Use the Dijkstra algorithm to find the shortest path from the goal to start
    distances_from_goal_left = dijkstra(grid, goal, LEFT)
    distances_from_goal_down = dijkstra(grid, goal, DOWN)

    # Find the minimum distance to the goal
    minimum_distance_to_goal = distances_from_start[goal]

    # Explore all tiles to count the tiles that are part of the minimum paths
    tiles_in_minimum_paths = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # All minimum distances to the position, from the start, and goal
            from_start = distances_from_start[(i, j)]
            from_goal_left = distances_from_goal_left[(i, j)]
            from_goal_up = distances_from_goal_down[(i, j)]

            # Count the tile if the sum of the distances is equal to the minimum distance to the goal
            if minimum_distance_to_goal in [from_start + from_goal_left, from_start + from_goal_up]:
                tiles_in_minimum_paths += 1

    return tiles_in_minimum_paths
