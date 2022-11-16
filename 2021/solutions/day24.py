'''
=========================================
|| 🎄 Advent of Code 2021: Day 24 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

INPUT = 'inp'
MULTIPLY = 'mul'
ADD = 'add'
MOD = 'mod'
DIV = 'div'
EQUAL = 'eql'

### Part One
def part_one(input):
    instructions = parse_input(input)
    storage = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    return  int(run_monad_program(instructions, storage))
    
### Part Two
def part_two(input):
    instructions = parse_input(input)
    storage = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    return int(run_monad_program(instructions, storage, False))


def parse_input(input):
    instructions = instructions_block = []
    for instruction in [line.split() for line in input]:
        if instruction[0] == INPUT:
            instructions.append(instructions_block)
            instructions_block = []
        else:
            instructions_block.append(instruction)

    return instructions[1:] + [instructions_block]

def hash(storage, model_number): return f'{storage}/{len(model_number)}'

def run_monad_program(instructions, storage, largest=True, model_number = '', cache = dict()):

    # Base case: all digits analyzed
    if len(model_number)==14: return model_number if storage['z']==0 else False

    result = False
    for digit in range(9, 0, -1) if largest else range(1, 10):
        temp_storage = storage.copy()
        temp_storage['w'] = digit
        temp_storage = execute_instruction(instructions, temp_storage, model_number)
        temp_model_number = model_number + str(digit)

        if (hash(temp_storage, temp_model_number)) in cache: continue

        valid_model_number = run_monad_program(instructions, temp_storage, largest, temp_model_number, cache)
        
        if valid_model_number: 
            result = valid_model_number
            break

    cache[hash(storage, model_number)] = result

    return result

def execute_instruction(instructions, storage, model_number): 
    block_instructions = instructions[len(model_number)]

    for instruction in block_instructions:
        command = instruction[0]
        variable = instruction[1]

        if command == INPUT: 
            storage[variable] = model_number.pop()
        else:
            param = instruction[2]
            value = storage[param] if param in storage else int(param)

            if command == MULTIPLY: storage[variable]*=value
            if command == ADD: storage[variable]+=value
            if command == MOD: storage[variable]%=value
            if command == DIV: storage[variable]//=value
            if command == EQUAL: storage[variable]= int(storage[variable]==value)
    
    return storage