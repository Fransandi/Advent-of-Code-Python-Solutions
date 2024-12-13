'''
=========================================
|| 🎄 Advent of Code 2024: Day 13 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    machines = []
    machine = []
    for line in input:
        line = line.replace(',', '').replace('=', ' ').replace('+', ' ')

        if line.startswith('Button'):
            instructions = line.split()
            machine.append((int(instructions[3]), int(instructions[5])))

        if line.startswith('Prize'):
            instructions = line.split()
            machine.append((int(instructions[2]), int(instructions[4])))
            machines.append(machine)
            machine = []

    return machines


# Part One
def part_one(input):
    # Parse the input
    machines = parse_input(input)

    # For each machine, we calculate the minimum cost
    cost = 0
    for machine in machines:
        min_cost = float('inf')
        (a_x, a_y), (b_x, b_y), target = machine

        # Try all combinations of a_times and b_times
        for a_times in range(101):
            for b_times in range(101):
                # If it matches the target, we update the min cost
                if target == (a_x * a_times + b_x * b_times, a_y * a_times + b_y * b_times):
                    min_cost = min(min_cost, 3 * a_times + b_times)

        # If we can't make the target, we skip this machine
        if min_cost == float('inf'):
            continue

        # Add the minimum cost to the total cost
        cost += min_cost

    return cost


# Part Two
def part_two(input):
    # Parse the input
    machines = parse_input(input)

    # Correct the prize values
    machines = [(a, b, (t[0] + 10000000000000, t[1] + 10000000000000))
                for a, b, t in machines]

    # For each machine, we calculate the minimum cost
    cost = 0
    for machine in machines:
        (a_x, a_y), (b_x, b_y), (target_x, target_y) = machine

        # Solve as a system of linear equations
        a_times = round((target_y - ((b_y * target_x) / b_x)) /
                        (a_y - ((b_y * a_x) / b_x)))
        b_times = round((target_x - a_x * a_times) / b_x)

        # If it matches the target, we update the min cost
        if (target_x, target_y) == (a_x * a_times + b_x * b_times, a_y * a_times + b_y * b_times):
            cost += 3 * a_times + b_times

    return cost
