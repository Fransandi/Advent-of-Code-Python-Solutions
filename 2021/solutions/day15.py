'''
=========================================
|| 🎄 Advent of Code 2021: Day 15 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import heapq
from typing import DefaultDict

### Part One
def part_one(input):
    risk_level_grid = [list(map(int, line.strip())) for line in input]
    return shortest_path(risk_level_grid)
    
### Part Two
def part_two(input):
    risk_level_grid = [list(map(int, line.strip())) for line in input]
    risk_level_extended_grid = extend_grid(risk_level_grid)
    return shortest_path(risk_level_extended_grid)

# Dijkstra's algorithm
def shortest_path(grid):
    height, width = len(grid), len(grid[0])
    source = (0, 0)
    destination = (height-1, width-1)
    minimum_distances = DefaultDict(lambda:float('inf'))
    queue = [(0, source)]
    visited = set()

    while queue:
        # Always look for the node with the lowest distance
        dist, node = heapq.heappop(queue)

        # Destination reached, return distance
        if node == destination: return dist

        visited.add(node)
        
        for neighbour in valid_neighbours(node[0], node[1], height, width):
            if neighbour not in visited:
                
                # Update the new neighbour's distance if lower than previous
                new_dist = grid[neighbour[0]][neighbour[1]] + dist
                if new_dist < minimum_distances[neighbour]:
                    minimum_distances[neighbour] = new_dist

                    # If updated, add node to queue, for the next iterations
                    heapq.heappush(queue, (minimum_distances[neighbour], neighbour))
    return None

def valid_neighbours(i, j, h, w):
    neighbours = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    return [n for n in neighbours if (min(n)>=0 and n[0]<h and n[1]<w)]

def extend_grid(grid, times=5):
    height, width = len(grid), len(grid[0])

    # Extend grid horizontally
    for _ in range(times-1):
        for row in grid:
            row.extend([num+1 if num<9 else 1 for num in row[-width:]])

    # Extend grid vertically
    for _ in range(times-1):
        for row in grid[-height:]:
            grid.append([num+1 if num<9 else 1 for num in row])

    return grid