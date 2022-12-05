'''
=========================================
|| 🎄 Advent of Code 2022: Day 5 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    stacks, instructions = parse_input(input)

    for instruction in instructions:
        for _ in range(instruction[0]): 
            stacks[instruction[2]].append(stacks[instruction[1]].pop())
    
    return ''.join([stack[-1] for stack in stacks])

### Part Two
def part_two(input):
    stacks, instructions = parse_input(input)

    for instruction in instructions:
        temp_cranes = []
        for _ in range(instruction[0]): 
            temp_cranes += stacks[instruction[1]].pop()
        stacks[instruction[2]] += temp_cranes[::-1]
    
    return ''.join([stack[-1] for stack in stacks])


def parse_input(input):
    input = [line for line in input]
    raw_stacks = input[:input.index('\n')-1]
    raw_instructions = input[input.index('\n')+1:]

    # Parsing cranes initial configuration
    num_stacks = len(raw_stacks[0])//4
    stacks = [[] for _ in range(num_stacks)]
    for line in raw_stacks:
        for i in range(num_stacks):
            char = line[(i*4)+1]
            if char != ' ': stacks[i].insert(0, char)
    
    # Parsing instructions
    instructions = []
    for instruction in raw_instructions:
        temp = instruction.split()
        instructions.append((int(temp[1]), int(temp[3])-1, int(temp[5])-1))

    return stacks, instructions
