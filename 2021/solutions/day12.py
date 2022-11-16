'''
=========================================
|| 🎄 Advent of Code 2021: Day 12 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from typing import DefaultDict

START = 'start'
END = 'end'

### Part One
def part_one(input):
    graph = build_graph(input)
    return count_paths_1(graph, START)

### Part Two
def part_two(input):
    graph = build_graph(input)
    return count_paths_2(graph, START)


def build_graph(input):
    graph = DefaultDict(list)
    for line in input:
        node1, node2 = line.strip().split('-')

        if node1 != START and node2 != END:
            graph[node2].append(node1)
        graph[node1].append(node2)

    return graph


def is_small_cave(node): 
    return node == node.lower()

def count_paths_1(graph, node, visited=set()):
    # Base case
    if node == END: return 1

    # If small cave, mark as visited
    if is_small_cave(node): visited.add(node)

    # Count the paths exploring all neighbours recursively
    paths = 0
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in visited:
                paths += count_paths_1(graph, neighbour, visited.copy())

    return paths


def count_paths_2(graph, node, visited=set(), skip_allowed=True):
    # Base case
    if node == END: return 1

    # If small cave, mark as visited
    if is_small_cave(node): visited.add(node)

    # Count the paths exploring all neighbours recursively
    paths = 0
    if node in graph:
        for neighbour in graph[node]:
            visited_copy = visited.copy()
            skip_allowed_copy = skip_allowed

            # Apply special rule of allowing to revisit a small cave only once
            if neighbour in visited_copy and skip_allowed_copy:
                visited_copy.remove(neighbour)
                skip_allowed_copy = False

            if neighbour not in visited_copy:
                paths += count_paths_2(graph, neighbour, visited_copy, skip_allowed_copy)

    return paths
