'''
=========================================
|| 🎄 Advent of Code 2022: Day 11 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import math

MONKEY = 'Monkey'
STARTING_ITEMS = 'Starting items'
OPERATIONS = 'Operation'
TEST = 'Test'
IF_TRUE = 'If true'
IF_FALSE = 'If false'

### Part One
def part_one(input):
    monkeys = parse_input(input)

    for i in range(20):
        for monkey in monkeys: 
            # print(monkey.items, monkey.operation, monkey.test)
            
            monkey.inspected+=len(monkey.items)
            while monkey.items:
                worry_level = monkey.items.pop(0)
                # operation, val = monkey.operation
                # val = int(val) if val.isdigit() else worry_level

                # if operation == '+': worry_level+=val
                # if operation == '*': worry_level*=val

                formula = ''.join(monkey.operation)
                formula.replace('old', worry_level)
                worry_level = eval(formula)
                # print(formula)
                # val = int(val) if val.isdigit() else worry_level

                # if operation == '+': worry_level+=val
                # if operation == '*': worry_level*=val



                worry_level = worry_level//3

                test, if_true, if_false = monkey.test
                next_monkey = if_true if worry_level%test==0 else if_false
                monkeys[next_monkey].items.append(worry_level)
                
    return math.prod(sorted([monkey.inspected for monkey in monkeys])[-2:])

            
### Part Two
def part_two(input):
    pass


class Monkey():
    def __init__(self):
        self.items = []
        self.operation = [None]*2
        self.test = [0]*3
        self.inspected = 0

def parse_input(input):
    monkeys = []
    monkey = None
    for line in [line.strip() for line in input]:
        if line.startswith(MONKEY):
            monkey = Monkey()
        elif line.startswith(STARTING_ITEMS):
            monkey.items = [int(item[:-1]) if item.endswith(',') else int(item) for item in line.split()[2:]]
        elif line.startswith(OPERATIONS):
            monkey.operation = line.split()[-3:]
        elif line.startswith(TEST):
            monkey.test[0] = int(line.split()[-1])
        elif line.startswith(IF_TRUE):
            monkey.test[1] = int(line.split()[-1])
        elif line.startswith(IF_FALSE):
            monkey.test[2] = int(line.split()[-1])
        else:
            monkeys.append(monkey)
    monkeys.append(monkey)
    
    return monkeys
