import os
import argparse

# Generate a solution file for each day of the year
def generate_solution_file(year, day):
    template = """'''
=========================================
|| 🎄 Advent of Code {0}: Day {1} 🗓
|| Link: https://adventofcode.com/{0}
|| Template by: @fransandi
|| Solution by: ...
=========================================
'''


### Part One
def part_one(input):
    pass

### Part Two
def part_two(input):
    pass
    """.format(year, day)

    dir_name = '{}/solutions'.format(year)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open('{}/solutions/day{}.py'.format(year, day), 'w') as f:
        f.write(template)

# Generate input files for each day of the year
def generate_input_file(year, day):
    dir_name = '{}/inputs'.format(year)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open('{}/inputs/day{}.txt'.format(year, day), 'w') as f:
        pass

# Generate example output file for each day of the year
def generate_example_input_file(year, day):
    dir_name = '{}/example/inputs'.format(year)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open('{}/example/inputs/day{}.txt'.format(year, day), 'w') as f:
        pass

# Generate example output files for each day of the year
def generate_example_output_file(year):
    template = '''example_outputs = {
    'day1': {
        'part_one': None,
        'part_two': None,
    },
    'day2': {
        'part_one': None,
        'part_two': None,
    },
    'day3': {
        'part_one': None,
        'part_two': None,
    },
    'day4': {
        'part_one': None,
        'part_two': None,
    },
    'day5': {
        'part_one': None,
        'part_two': None,
    },
    'day6': {
        'part_one': None,
        'part_two': None,
    },
    'day7': {
        'part_one': None,
        'part_two': None,
    },
    'day8': {
        'part_one': None,
        'part_two': None,
    },
    'day9': {
        'part_one': None,
        'part_two': None,
    },
    'day10': {
        'part_one': None,
        'part_two': None,
    },
    'day11': {
        'part_one': None,
        'part_two': None,
    },
    'day12': {
        'part_one': None,
        'part_two': None,
    },
    'day13': {
        'part_one': None,
        'part_two': None,
    },
    'day14': {
        'part_one': None,
        'part_two': None,
    },
    'day15': {
        'part_one': None,
        'part_two': None,
    },
    'day16': {
        'part_one': None,
        'part_two': None,
    },
    'day17': {
        'part_one': None,
        'part_two': None,
    },
    'day18': {
        'part_one': None,
        'part_two': None,
    },
    'day19': {
        'part_one': None,
        'part_two': None,
    },
    'day20': {
        'part_one': None,
        'part_two': None,
    },
    'day21': {
        'part_one': None,
        'part_two': None,
    },
    'day22': {
        'part_one': None,
        'part_two': None,
    },
    'day23': {
        'part_one': None,
        'part_two': None,
    },
    'day24': {
        'part_one': None,
        'part_two': None,
    },
    'day25': {
        'part_one': None,
        'part_two': None,
    }
}'''

    with open('{}/example/outputs.py'.format(year), 'w') as f:
        f.write(template)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate Advent of Code template files for a given year.')
parser.add_argument('year', type=int, help='The year for the Advent of Code event.')
args = parser.parse_args()
year = args.year

# Generate solution and input files for each day of the year
for day in range(1, 26):
    generate_solution_file(year, day)
    generate_input_file(year, day)
    generate_example_input_file(year, day)
generate_example_output_file(year)