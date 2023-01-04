'''
=========================================
|| 🎄 Advent of Code 2022: Day 19 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from collections import defaultdict

NO_ROBOT = -1
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
ROBOT_TYPES = [ORE, CLAY, OBSIDIAN, GEODE]

### Part One
def part_one(input):
    quality_levels = 0
    for i, blueprint in enumerate([blueprint for blueprint in input], start=1):
        quality_levels += i * calculate_max_geodes(blueprint, 25)

    return quality_levels

### Part Two
def part_two(input):
    total = 1
    for i, blueprint in enumerate([blueprint for blueprint in input], start=1):
        max_geodes = calculate_max_geodes(blueprint, 33)
        total *= max_geodes

        if i==3: return total

    return total


def calculate_max_geodes(blueprint, total_time):
    costs = get_costs(blueprint)
    max_robots = get_max_robots(costs)
    most_geodes_in_time = defaultdict(int)
    explored_states = set()

    # Explore all possible paths
    stack = [(1, [1, 0, 0, 0], [0, 0, 0, 0], [])]
    while stack:
        minute, robots, resources, skipped = stack.pop(0)
        
        # Only check relevant paths
        if minute <= total_time and resources[GEODE] >= most_geodes_in_time[minute]:
            
            # Update the best scenario so far
            most_geodes_in_time[minute] = resources[GEODE]

            # Generate all possible robot options to build
            robot_options = get_robot_options(resources, robots, costs, max_robots)

            # Generate resources
            for i in range(len(ROBOT_TYPES)): resources[i] += robots[i]

            # Explore all possible paths
            for new_robot in robot_options:        
                if new_robot not in skipped:
                    updated_robots, updated_resources = build_robot(new_robot, costs, robots, resources)

                    # Don't explore the path of building a robot we ignored last turn
                    to_skip = [option for option in robot_options if option != NO_ROBOT] if new_robot == NO_ROBOT else []
                    
                    next_state = (minute+1, updated_robots, updated_resources, to_skip)

                    # Only explore new states
                    if hash_state(next_state) not in explored_states:
                        stack.append(next_state)
                        explored_states.add(hash_state(next_state))

    return most_geodes_in_time[total_time]


def get_costs(blueprint):
    bp = blueprint.strip().split('.')
    return [
        [int(bp[0].split()[-2]), 0, 0],
        [int(bp[1].split()[-2]), 0, 0],
        [int(bp[2].split()[-5]), int(bp[2].split()[-2]), 0],
        [int(bp[3].split()[-5]), 0, int(bp[3].split()[-2])]
    ]

def get_max_robots(costs):
    max_storage = [0]*3
    for i in range(3):
        for cost in costs:
            max_storage[i] = max(max_storage[i], cost[i])
    return max_storage + [float('inf')]

def get_robot_options(resources, robots, costs, max_robots):
    new_robots = [NO_ROBOT]
    for robot in ROBOT_TYPES:
        if robots[robot] < max_robots[robot] and all(resources[i] >= costs[robot][i] for i in range(3)):
            new_robots.append(robot)

            # If a geode robot can be built, it's always the best option
            if robot == GEODE: return [GEODE]

    return new_robots

def build_robot(new_robot, costs, robots, resources):
    updated_robots, updated_resources = robots.copy(), resources.copy()

    if new_robot in ROBOT_TYPES:
        for i in range(3): updated_resources[i] -= costs[new_robot][i]
        updated_robots[new_robot]+=1
    
    return updated_robots, updated_resources

def hash_state(state): return (state[0], tuple(state[1]), tuple(state[2]))