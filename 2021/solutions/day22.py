'''
=========================================
|| 🎄 Advent of Code 2021: Day 22 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

ON = 'on'

### Part One
def part_one(input):
    all_instructions = parse_input(input)
    reactor_core = set()

    for instruction in all_instructions:
        turn_on, cuboid = instruction
        x1, x2, y1, y2, z1, z2 = cuboid

        # Filter only the cuboids inside the initialization procedure region
        if min(x1, y1, z1)<-50 or max(x2, y2, z2)>50: continue

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    new_cube = (x, y, z)
                        
                    # Add the cube if 'on', else remove it if present
                    if turn_on: reactor_core.add(new_cube)
                    else: reactor_core.discard(new_cube)

    return len(reactor_core)

### Part Two
def part_two(input):
    all_instructions = parse_input(input)
    on_cuboids, off_cuboids = [], []

    for instruction in all_instructions:
        turn_on, new_cuboid = instruction

        # Add the intersection of cuboids to the opposite list, to avoid overcalculation
        new_off_cuboids = []
        for cuboid in on_cuboids:
            intersection = get_intersection(cuboid, new_cuboid)
            if intersection: new_off_cuboids.append(intersection)

        for cuboid in off_cuboids:
            intersection = get_intersection(cuboid, new_cuboid)
            if intersection: on_cuboids.append(intersection)

        off_cuboids.extend(new_off_cuboids)

        # Add the turn_on cuboids to the on_cuboids list
        if turn_on: on_cuboids.append(new_cuboid)

    # Sum all on cubes and substract all off cubes
    cubes_count = 0
    for cuboid in on_cuboids: 
        cubes_count += count_cubes_in_cuboid(*cuboid)
    
    for cuboid in off_cuboids: 
        cubes_count -= count_cubes_in_cuboid(*cuboid)
    
    return cubes_count

def parse_input(input):
    all_instructions = []
    for instruction in [line.split() for line in input]:
        turn_on = instruction[0] == ON
        coordinates = instruction[1].split(',')
        cuboid = []

        for coordinate in coordinates:
            interval = (coordinate.split('=')[1]).split('..')
            cuboid.extend([int(interval[0]), int(interval[1])])

        all_instructions.append((turn_on, cuboid))
    
    return all_instructions

def get_intersection(intervals_a, intervals_b):
    x1_a, x2_a, y1_a, y2_a, z1_a, z2_a = intervals_a
    x1_b, x2_b, y1_b, y2_b, z1_b, z2_b = intervals_b

    x1_ab, x2_ab = max(x1_a, x1_b), min(x2_a, x2_b)
    y1_ab, y2_ab = max(y1_a, y1_b), min(y2_a, y2_b)
    z1_ab, z2_ab = max(z1_a, z1_b), min(z2_a, z2_b)

    # Don't return coordinates, if no intersection was found
    if x1_ab >= x2_ab or y1_ab >= y2_ab or z1_ab >= z2_ab: 
        return None    
    
    return x1_ab, x2_ab, y1_ab, y2_ab, z1_ab, z2_ab

def count_cubes_in_cuboid(x1, x2, y1, y2, z1, z2):
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


