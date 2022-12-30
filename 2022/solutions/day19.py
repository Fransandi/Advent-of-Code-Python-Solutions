'''
=========================================
|| 🎄 Advent of Code 2022: Day 19 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
from functools import lru_cache


def part_one(input):
    for i, blueprint in enumerate([line for line in input]):
        costs = parse_blueprint(blueprint)
        robots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]

        return simulate(0, costs, tuple(robots), tuple(resources))

### Part Two
def part_two(input):
    pass

def parse_blueprint(blueprint):
    blueprint = blueprint.strip().split('.')
    ore = (int(blueprint[0].split()[-2]), 0, 0, 0)
    clay = (int(blueprint[1].split()[-2]), 0, 0, 0)
    obsidian = (int(blueprint[2].split()[-5]), int(blueprint[2].split()[-2]), 0, 0)
    geode = (int(blueprint[3].split()[-5]), 0, int(blueprint[3].split()[-2]), 0)

    return (ore, clay, obsidian, geode)

# def can_be_built(robot_type, resources, cost):

#     if ]

@lru_cache(maxsize=None)
def simulate(step, costs, robots, resources):
    # print(step, robots, resources)
    robots, resources = list(robots), list(resources)

    # Base case: last step reached
    if step == 24: return resources[-1]

    # Get all possible next moves
    new_robots = [-1]
    for robot in range(4):
        if all(resources[i] >= costs[robot][i] for i in range(4)): 
            new_robots.append(robot)

    # Generate resources
    for i in range(4): resources[i] += robots[i]

    # Explore all possible paths
    geodes = float('-inf')
    for new_robot in new_robots:
        temp_robots, temp_resources = create_robot(new_robot, costs, robots, resources)
        geodes = max(geodes, simulate(step+1, costs, tuple(temp_robots), tuple(temp_resources)))

    return geodes

def create_robot(new_robot, costs, robots, resources):
    temp_robots, temp_resources = robots.copy(), resources.copy()

    if new_robot >= 0:
        for i in range(4): temp_resources[i] -= costs[new_robot][i]
        temp_robots[new_robot]+=1
    
    return temp_robots, temp_resources