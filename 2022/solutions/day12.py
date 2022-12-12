'''
=========================================
|| 🎄 Advent of Code 2022: Day 12 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
import heapq
from typing import DefaultDict


def part_one(input):
    grid, source, destination = parse_input(input)
    return get_shortest_path(grid, source, destination)

### Part Two
def part_two(input):
    grid, _, destination = parse_input(input)

    # Get all starting points with elevation 'a'
    starting_points = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]=='a']
    
    # Return the minimum shortest path from all starting points
    return(min([get_shortest_path(grid, source, destination) for source in starting_points]))


def parse_input(input): 
    grid = [list(line.strip()) for line in input]

    s_i, s_j = find_position(grid, 'S')
    e_i, e_j = find_position(grid, 'E')
    
    grid[s_i][s_j] = 'a'
    grid[e_i][e_j] = 'z'

    return grid, (s_i, s_j), (e_i, e_j)

def find_position(grid, char): return [(index, row.index(char)) for index, row in enumerate(grid) if char in row][0]

# Dijkstra's algorithm
def get_shortest_path(grid, source, destination):
    height, width = len(grid), len(grid[0])
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
            # Validate that the neighbour is reachable
            if neighbour not in visited and (ord(grid[neighbour[0]][neighbour[1]]) <= ord(grid[node[0]][node[1]])+1):
                
                # Update the new neighbour's distance if lower than previous
                if dist+1 < minimum_distances[neighbour]:
                    minimum_distances[neighbour] = dist+1

                    # If updated, add node to queue, for the next iterations
                    heapq.heappush(queue, (minimum_distances[neighbour], neighbour))
    
    return float('inf')

def valid_neighbours(i, j, h, w):
    neighbours = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
    return [n for n in neighbours if (min(n)>=0 and n[0]<h and n[1]<w)]
