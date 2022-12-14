'''
=========================================
|| 🎄 Advent of Code 2022: Day 14 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

SAND_START = (500, 0)

### Part One
def part_one(input):
    all_blocks, edge = parse_input(input)
    i = 0
    while True:
        sand_position = get_sand_rest_position(all_blocks, edge)

        # Simulation ends
        if not sand_position: return i
        
        all_blocks.add(sand_position)
        i+=1

### Part Two
def part_two(input):
    all_blocks, edge = parse_input(input)
    all_blocks.update(get_floor_points(edge+2))
    i = 0
    while True:
        sand_position = get_sand_rest_position(all_blocks)
        all_blocks.add(sand_position)
        i+=1
        
        # Simulation ends
        if SAND_START in all_blocks: return i


def parse_input(input):
    rock_blocks = set()
    for line in input:
        path = [tuple(map(int, point.split(','))) for point in line.strip().split(' -> ')]        
        rock_blocks.update(get_all_points(path))
    return rock_blocks, max([block[1] for block in rock_blocks])

def get_all_points(path):
    points, start = set(), path.pop()
    while path:
        next = path.pop()
        s_x, s_y, n_x, n_y = start[0], start[1], next[0], next[1]
        if s_x == n_x: points.update(set([(s_x, y) for y in range(min(s_y, n_y), max(s_y, n_y)+1)]))
        if s_y == n_y: points.update(set([(x, s_y) for x in range(min(s_x, n_x), max(s_x, n_x)+1)]))
        start = next
    return points

def get_sand_rest_position(all_blocks, edge=float('inf')):
    sand = SAND_START
    while sand[1] <= edge:
        x, y = sand
        if (x, y+1) not in all_blocks: sand = (x, y+1)
        elif (x-1, y+1) not in all_blocks: sand = (x-1, y+1)
        elif (x+1, y+1) not in all_blocks: sand = (x+1, y+1)
        else: return sand
    return None

def get_floor_points(floor): return set([(x, floor) for x in range(SAND_START[0]-floor-1, SAND_START[0]+floor+1)])