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


# Part One
def part_one(input):
    # Parse input
    grid = [list(line.strip()) for line in input]

    # Find the start position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == START:
                start = (0, RIGHT, (i, j))
                break

    # DFS with priority queue, to explore the grid
    visited, queue = set(), [start]
    while queue:
        cost, direction, position = heapq.heappop(queue)
        i, j = position

        # Check if the goal is reached
        if grid[i][j] == GOAL:
            return cost

        # Skip if the position was already visited from the same direction
        if (position, direction) in visited:
            continue

        # Mark the position as visited
        visited.add((position, direction))

        # Explore move in the current direction
        next_position = get_next_position(i, j, direction)
        if grid[next_position[0]][next_position[1]] != WALL:
            heapq.heappush(queue, (cost + 1, direction, next_position))

        # Explore turn left or right 90 degrees
        for next_direction in {
            UP: [LEFT, RIGHT],
            DOWN: [LEFT, RIGHT],
            LEFT: [UP, DOWN],
            RIGHT: [UP, DOWN]
        }[direction]:
            next_position = get_next_position(i, j, next_direction)
            if grid[next_position[0]][next_position[1]] != WALL:
                heapq.heappush(queue, (cost + 1000, next_direction, position))


# Part Two
def part_two(input):
    pass
