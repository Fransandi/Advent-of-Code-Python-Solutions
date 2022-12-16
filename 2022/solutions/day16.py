'''
=========================================
|| 🎄 Advent of Code 2022: Day 16 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    valves = parse_input(input)
    return get_max_pressure(valves, 29)

### Part Two
def part_two(input):
    valves = parse_input(input)
    return get_max_pressure(valves, 25, True)


class Valve():
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = [tunnel.replace(',', '') for tunnel in tunnels]
        self.distance = {}

def parse_input(input):
    valves = {}
    # Read the input and create the valves
    for data in [line.split() for line in input]:
        name, flow, tunnels = data[1], int(data[4][5:-1]), data[next(i for i, el in enumerate(data) if 'valve' in el)+1:]
        valves[name] = Valve(name, flow, tunnels)

    # Calculate the distance between the non-zero flow valves (the ones worth to be opened)
    for v1 in [valve for valve in valves.values() if valve.flow or valve.name == 'AA']:
        for v2 in [valve for valve in valves.values() if valve.flow]:
            v1.distance[v2.name] = calculate_distance(valves, v1.tunnels, v2.name)
    
    return valves

def calculate_distance(valves, tunnels, destination):
    distance = 1
    while True:
        next_tunnels = set()
        for tunnel in tunnels:
            # Shortest distance to the destination found
            if tunnel == destination: return distance

            next_tunnels.update(set([next_tunnel for next_tunnel in valves[tunnel].tunnels]))

        tunnels = next_tunnels
        distance+=1

def get_max_pressure(valves, time_left, elephant_help=False, open=set(['AA']), pressure=0, current='AA'):
    max_pressure = pressure
    
    # Edge case: time's over, return the current pressure
    if time_left<=0: return max_pressure

    # Evaluate the strategy in which we open the valve
    if current not in open:
        max_pressure = max(max_pressure, get_max_pressure(valves, time_left-1, elephant_help, open.union([current]), pressure+(valves[current].flow*time_left), current))
        
        # If we're receiving help from an elephant, evaluate his turns as well
        if elephant_help:
            max_pressure = max(max_pressure, get_max_pressure(valves, 25, False, set([current]).union(open), pressure+(valves[current].flow*time_left), 'AA'))

    # Evaluate the strategy in which we follow all possible tunnel paths without opening valves
    else:
        for tunnel in [tunnel for tunnel in valves[current].distance.keys() if tunnel not in open]:
            max_pressure = max(max_pressure, get_max_pressure(valves, time_left-valves[current].distance[tunnel], elephant_help, open, pressure, tunnel))

    return max_pressure
