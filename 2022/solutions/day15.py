'''
=========================================
|| 🎄 Advent of Code 2022: Day 15 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

EXAMPLE_Y = 10
EXERCISE_Y = 2000000

### Part One
def part_one(input):
    sensors, distance = parse_input(input)
    min_x = sorted([sensor[0]-distance[sensor] for sensor in sensors.keys()])[0]
    max_x = sorted([sensor[0]+distance[sensor]+1 for sensor in sensors.keys()])[-1]

    # Condition to switch between the 'y' value in the example and exercise
    y = EXAMPLE_Y if max_x < EXERCISE_Y else EXERCISE_Y
    
    # Evaluate all the points in the horizontal line
    count = 0
    for point in [(x, y) for x in range(min_x, max_x+1) if (x, y) not in sensors.values()]:
        # Count 1 if any sensor invalidates this point to have a beacon
        count += point_reachable_by_sensors(distance, point)

    return count

### Part Two
def part_two(input):
    sensors, distance = parse_input(input)

    # Calculate edges of all sensor areas in both directions
    lines_dir1 = [s[0]+s[1]+directions for s, d in distance.items() for directions in (d, -d)]
    lines_dir2 = [s[0]-s[1]+directions for s, d in distance.items() for directions in (d, -d)]

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
        if not point_reachable_by_sensors(distance, (x, y)): return x * 4000000 + y


def parse_input(input):
    sensors, distance = {}, {}
    for line in input:
        instruction = line.split()
        sensor = (int(instruction[2].split('=')[-1][:-1]), int(instruction[3].split('=')[-1][:-1]))
        beacon = (int(instruction[8].split('=')[-1][:-1]), int(instruction[9].split('=')[-1]))
        sensors[sensor] = beacon
        distance[sensor] = manhattan_distance(sensor, beacon)
    return sensors, distance

def manhattan_distance(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def all_intersections(points_1, points_2): 
    return [((p1+p2)//2, (p2-p1)//2) for p1 in list(set(points_1)) for p2 in list(set(points_2))]

def point_reachable_by_sensors(distance, point):
    return any([manhattan_distance(sensor, point) <= dist for sensor, dist in distance.items()])
