'''
=========================================
|| 🎄 Advent of Code 2022: Day 13 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import ast
from copy import deepcopy
from functools import cmp_to_key

DIVIDER_PACKAGES = [[[2]], [[6]]]

### Part One
def part_one(input):
    packages = [ast.literal_eval(line.strip()) for line in input if line.strip()]
    pairs = [packages[i:i+2] for i in range(0, len(packages), 2)]
    return sum([i for i, pair in enumerate(pairs, start=1) if in_right_order(*pair)])

### Part Two
def part_two(input):
    packages = [ast.literal_eval(line.strip()) for line in input if line.strip()] + DIVIDER_PACKAGES
    packages.sort(key=cmp_to_key(compare))
    return (packages.index(DIVIDER_PACKAGES[0])+1) * (packages.index(DIVIDER_PACKAGES[1])+1)
     

def in_right_order(val1, val2):
    type1, type2 = type(val1), type(val2)

    # Compare two integers
    if (type1, type2) == (int, int): return val1<val2

    # Adjust mixed types
    if type1 == int: val1 = [val1]
    if type2 == int: val2 = [val2]

    # Compare two lists
    while len(val1) and len(val2):
        el1, el2 =  val1.pop(0), val2.pop(0)
        # Skip if equal
        if el1==el2: continue
            
        return in_right_order(el1, el2)
        
    return not len(val1)

def compare(val1, val2): return -1 if in_right_order(deepcopy(val1), deepcopy(val2)) else 1
