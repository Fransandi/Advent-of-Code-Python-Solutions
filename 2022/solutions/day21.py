'''
=========================================
|| 🎄 Advent of Code 2022: Day 21 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from sympy import solve, sympify, Symbol

ROOT = 'root'
HUMN = 'humn'
UNKNOWN = 'x'

### Part One
def part_one(input):
    dict = {}
    for monkey, number in [line.strip().split(':') for line in input]:
        dict[monkey] = number.strip().split()

    return decode(ROOT, dict)

### Part Two
def part_two(input):
    dict = {}
    for monkey, number in [line.strip().split(':') for line in input]:
        dict[monkey] = number.strip().split()
    
    dict[ROOT][1] = '='
    dict[HUMN] = [UNKNOWN]

    # Build and solve math expression
    expression = build_expression(ROOT, dict)
    sympy_eq = sympify('Eq(' + expression[1:-1].replace('=', ',') + ')')
    return solve(sympy_eq, Symbol(UNKNOWN))[0]


def decode(monkey, dict):
    number = dict[monkey] 

    # Base case: monkey yells a specific number
    if len(number)==1: return int(number[0])
    
    # Calculate number from math expression
    return int(eval(str(decode(number[0], dict)) + number[1] + str(decode(number[2], dict))))

def build_expression(monkey, dict):
    number = dict[monkey]

    # Base case: monkey yells a specific number
    if len(number)==1: return number[0]

    # Calculate number from math expression
    num1 = build_expression(number[0], dict)
    num2 = build_expression(number[2], dict)
    operation = number[1]
    
    return '(' + num1 + operation + num2 + ')'