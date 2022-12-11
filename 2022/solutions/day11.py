'''
=========================================
|| 🎄 Advent of Code 2022: Day 11 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import math

### Part One
def part_one(input):
    monkeys = parse_input(input)
    return simulate(monkeys, 20)
            
### Part Two
def part_two(input):
    monkeys = parse_input(input)
    lcm = math.lcm(*[monkey.test[0] for monkey in monkeys])
    return simulate(monkeys, 10000, False, lcm)


class Monkey():
    def __init__(self):
        self.items = []
        self.formula = None
        self.test = []
        self.inspected = 0

def parse_input(input):
    monkeys = []
    monkey = None
    for line in [line.strip() for line in input]:
        if line.startswith('Monkey'): 
            monkey = Monkey()
        elif line.startswith('Starting items'): 
            monkey.items = [int(item[:-1]) if item.endswith(',') else int(item) for item in line.split()[2:]]
        elif line.startswith('Operation'):
            monkey.formula = ''.join(line.split()[-3:])
        elif line.startswith('Test') or line.startswith('If'):
            monkey.test.append(int(line.split()[-1]))
        else:
            monkeys.append(monkey)
    monkeys.append(monkey)
    
    return monkeys

def simulate(monkeys, rounds, relief=True, lcm=None):
    for _ in range(rounds):
        for monkey in monkeys: 
            while monkey.items:
                formula = monkey.formula.replace('old', str(monkey.items.pop(0)))
                item = eval(formula)//3 if relief else eval(formula)%lcm
                next_monkey = monkey.test[1] if item % monkey.test[0]==0 else monkey.test[2]
                monkeys[next_monkey].items.append(item)
                monkey.inspected+=1
                
    return math.prod(sorted([monkey.inspected for monkey in monkeys])[-2:])
