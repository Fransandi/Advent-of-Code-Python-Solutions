'''
=========================================
|| 🎄 Advent of Code 2022: Day 21 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

ROOT = 'root'
HUMN = 'humn'
UNKNOWN = 'X'

### Part One
def part_one(input):
    dict = {}
    for monkey, yells in [line.strip().split(':') for line in input]:
        dict[monkey] = yells.strip()

    return decode(ROOT, dict)

### Part Two
def part_two(input):
    dict = {}
    for monkey, yells in [line.strip().split(':') for line in input]:
        dict[monkey] = yells.strip().split()

    # if monkey == HUMN: dict[HUMN] = [UNKNOWN]
    dict[ROOT][1] = '='
    dict[HUMN] = UNKNOWN

    print('>>> DIC: ', dict)
    # return build_equation(ROOT, dict)


def decode(monkey, dict):
    yell = dict[monkey]

    if yell.isnumeric(): dict[monkey] = int(yell)
    else:
        n1, operation, n2 = yell.split()
        decoded_n1 = decode(n1, dict)
        decoded_n2 = decode(n2, dict)
        dict[monkey] = int(eval(str(decoded_n1) + operation + str(decoded_n2)))
    
    return dict[monkey]

def build_equation(monkey, dict):
    yell = dict[monkey]
    print('Yell:', yell)


    
    if yell.isnumeric(): dict[monkey] = int(yell)



    return dict[monkey]


    if yell.isnumeric(): dict[monkey] = int(yell)
    elif yell == UNKNOWN or UNKNOWN in yell:
        return UNKNOWN
    else:
        n1, operation, n2 = yell.split()
        decoded_n1 = decode2(n1, dict)
        decoded_n2 = decode2(n2, dict)

        print('decoded_n1', decoded_n1)
        print('decoded_n2', decoded_n2)
        if UNKNOWN not in decoded_n1 and UNKNOWN not in decoded_n2:
            dict[monkey] = int(eval(str(decoded_n1) + operation + str(decoded_n2)))
    
    return dict[monkey]