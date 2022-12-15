'''
=========================================
|| 🎄 Advent of Code 2022: Day 15 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    sensors = parse_input(input)

    # Condition to switch between the 'row' value in the example and exercise
    row = 10 if all(abs(key[0])<1000 for key in sensors.keys()) else 2000000

    # Get all sensor's area segments touching the row to check
    segments = []
    for (s_x, s_y), dist in sensors.items():
        # Skip if area doesn't touch the row
        if s_y >= row and s_y-dist>row: continue
        if s_y < row and s_y+dist<row: continue

        segments.append((s_x - (dist-abs(s_y-row)), s_x + (dist-abs(s_y-row))))
    
    # Merge all the overlapping segments
    segments.sort()
    merged_segments = [segments.pop(0)]
    while segments:
        prev = merged_segments[-1]
        next = segments.pop(0)

        if prev[1]<next[0]: 
            merged_segments.append(next)
            continue

        merged_segments[-1] = ((min(prev[0], next[0]), max(prev[1], next[1])))

    # Return the sum of lenghts from all the segments
    return sum([segment[1]-segment[0] for segment in merged_segments])

### Part Two
def part_two(input):
    sensors = parse_input(input)

    # Calculate edges of all sensor areas in both directions
    lines_dir1 = [s[0]+s[1]+directions for s, d in sensors.items() for directions in (d, -d)]
    lines_dir2 = [s[0]-s[1]+directions for s, d in sensors.items() for directions in (d, -d)]

    # Determine the line candidates based on distance between edges
    candidates_dir1, candidates_dir2 = [], []
    for i in range(len(sensors)*2):
        for j in range(i+1, len(sensors)*2):
            a, b = lines_dir2[i], lines_dir2[j]
            if abs(a - b) == 2: candidates_dir1.append(min(a, b) + 1)

            a, b = lines_dir1[i], lines_dir1[j]
            if abs(a - b) == 2: candidates_dir2.append(min(a, b) + 1)

    # Check all interesections between line candidates, until discovering the point not reachable by the sensors
    for (x, y) in all_intersections(candidates_dir1, candidates_dir2):
        if not point_reachable_by_sensors(sensors, (x, y)): return x * 4000000 + y


def parse_input(input):
    sensors = {}
    for line in input:
        instruction = line.split()
        sensor = (int(instruction[2].split('=')[-1][:-1]), int(instruction[3].split('=')[-1][:-1]))
        beacon = (int(instruction[8].split('=')[-1][:-1]), int(instruction[9].split('=')[-1]))
        sensors[sensor] = manhattan_distance(sensor, beacon)
    return sensors

def manhattan_distance(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def all_intersections(points_1, points_2): 
    return [((p1+p2)//2, (p2-p1)//2) for p1 in list(set(points_1)) for p2 in list(set(points_2))]

def point_reachable_by_sensors(sensors, point):
    return any([manhattan_distance(sensor, point) <= distance for sensor, distance in sensors.items()])
