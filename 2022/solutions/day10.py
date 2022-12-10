'''
=========================================
|| 🎄 Advent of Code 2022: Day 10 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

NOOP = 'noop'
ADDX = 'addx'

### Part One
def part_one(input):
    program = [line.strip() for line in input]
    i, x, signal_strength = 0, 1, 0
    
    for instruction in program: 
        if instruction == NOOP: 
            i, signal_strength = execute_signal_strength_cycle(i, x, signal_strength)

        if instruction.startswith(ADDX):
            i, signal_strength = execute_signal_strength_cycle(i, x, signal_strength)
            i, signal_strength = execute_signal_strength_cycle(i, x, signal_strength)
            
            x+=int(instruction.split()[-1])
            
    return(signal_strength)

### Part Two
def part_two(input):
    program = [line.strip() for line in input]
    i, x, screen, row = 0, 1, [], ''

    for instruction in program: 
        if instruction == NOOP: 
            i, row = execute_draw_cycle(i, x, screen, row)

        if instruction.startswith(ADDX):
            i, row = execute_draw_cycle(i, x, screen, row)
            i, row = execute_draw_cycle(i, x, screen, row)

            x+=int(instruction.split()[-1])

    # Uncomment next line to see the outcome printed in the screen
    # for row in screen: print(row)
    
    return True


def execute_signal_strength_cycle(i, x, signal_strength):
    i+=1
    
    # Check if the total signal strength needs to be incremented in this cycle
    if i in [20, 60, 100, 140, 180, 220]: signal_strength+=(i*x)

    return i, signal_strength

def execute_draw_cycle(i, x, screen, row):
    row += '#' if i in [x-1, x, x+1] else ' '
    i+=1

    # Check if the row is ready to be added to the screen
    if i == 40: 
        screen.append(row)
        return 0, ''

    return i, row
