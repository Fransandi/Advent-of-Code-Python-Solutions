'''
=========================================
|| 🎄 Advent of Code 2024: Day 19 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    towels, designs = [], []
    for line in [line.strip() for line in input]:
        if ',' in line:
            towels = [towel.strip() for towel in line.split(',')]
        elif line:
            designs.append(line)
    return towels, designs


def design_is_possible(towels, design, index=0):
    # Base case, the design is possible
    if index == len(design):
        return True

    # Explore all possible towels
    for towel in towels:
        if towel == design[index:index+len(towel)]:
            # If the towel fits, try the next part of the design
            if design_is_possible(towels, design, index+len(towel)):
                return True

    # If no towel fits, the design is impossible
    return False


def count_possible_designs(towels, design, cache):
    # Base case, the design is possible
    if len(design) == 0:
        return 1

    # Check if the result is already in the cache
    if design in cache:
        return cache[design]

    # Count the number of possible designs
    result = 0
    for towel in towels:
        if towel == design[:len(towel)]:
            result += count_possible_designs(towels,
                                             design[len(towel):], cache)

    # Store the result in the cache
    cache[design] = result

    # Return the result
    return result


# Part One
def part_one(input):
    # Parse input
    towels, designs = parse_input(input)

    # Count the number of designs that are possible
    return sum(1 for design in designs if design_is_possible(towels, design))


# Part Two
def part_two(input):
    # Parse input
    towels, designs = parse_input(input)

    # Count the number of possible designs
    return sum(count_possible_designs(towels, design, {}) for design in designs)
