'''
=========================================
|| 🎄 Advent of Code 2022: Day 18 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    cubes = set(tuple(map(int, line.strip().split(','))) for line in input)
    return sum([1 for x, y, z in cubes for neighbour in get_neighbours(x, y, z) if neighbour not in cubes])

### Part Two
def part_two(input):
    cubes = set(tuple(map(int, line.strip().split(','))) for line in input)
    
    # Calculate the bounds for exploration
    min_x, max_x = min(x for (x, _, _) in cubes)-1, max(x for (x, _, _) in cubes)+1
    min_y, max_y = min(y for (_, y, _) in cubes)-1, max(y for (_, y, _) in cubes)+1
    min_z, max_z = min(z for (_, _, z) in cubes)-1, max(z for (_, _, z) in cubes)+1
    bounds = (min_x, max_x,  min_y, max_y, min_z, max_z)
    
    queue = [(min_x, min_y, min_z)]
    visited = set()
    count = 0
    while queue:
        (x, y, z) = queue.pop(0)
        visited.add((x, y, z))
        for cube in get_neighbours(x, y, z):
            if is_within_bounds(cube, bounds) and cube not in visited and cube not in queue:
                # Count each cube that could be reached from outside
                if cube in cubes:
                    count+=1
                # Add every other cube within range for exploration
                else:
                    queue.append(cube)
    return count


def get_neighbours(x, y, z): return [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

def is_within_bounds(cube, bounds):
    x, y, z = cube
    min_x, max_x,  min_y, max_y, min_z, max_z = bounds
    return x >= min_x and x <= max_x and y >= min_y and y <= max_y and z >= min_z and z <= max_z