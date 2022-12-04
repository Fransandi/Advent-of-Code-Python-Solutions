'''
=========================================
|| 🎄 Advent of Code 2022: Day 4 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 


### Part One
def part_one(input):
    pair_assignments = parse_input(input)
    
    # Count the pairs with a full overlap
    return sum(map(lambda pair : pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1], pair_assignments))

### Part Two
def part_two(input):
    pair_assignments = parse_input(input)
    
    # Count the pairs with any overlap
    return sum(map(lambda pair : pair[0][1] >= pair[1][0], pair_assignments))


def parse_input(input): 
    pair_assignments = []

    for line in input:
        pair = line.strip().split(',')
        elf_1 = [eval(num) for num in pair[0].split('-')]
        elf_2 = [eval(num) for num in pair[1].split('-')]

        # The first assignment is the one that starts more to the left
        if elf_1[0] > elf_2[0]: elf_1, elf_2 = elf_2, elf_1

        pair_assignments.append((elf_1, elf_2))
    
    return pair_assignments
