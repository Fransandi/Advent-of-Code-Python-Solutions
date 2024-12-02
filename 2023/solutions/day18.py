'''
=========================================
|| 🎄 Advent of Code 2023: Day 18 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import sys
sys.setrecursionlimit(999999999)

### Part One
def part_one(input):
    instructions = [(direction, int(steps)) for direction, steps, _ in [line.split() for line in input]]
    return follow_dig_plan(instructions)

### Part Two
def part_two(input):
    hex_digits = [row.strip()[-7:-1] for row in input]
    print('hex_digits', hex_digits)

    # for hex in hex_digits:
    #     print('hex:', hex)
    #     direction = 'RDLU'[int(hex[-1])]
    #     steps = int(hex[:-1], 16)

    #     # print('direction', direction)
    #     # print('steps', steps)
    #     print(direction, steps)

        # return

    instructions = [('RDLU'[int(hex[-1])], int(hex[:-1], 16)) for hex in hex_digits]
    return follow_dig_plan(instructions)
    # print('instructions', instructions)

    # instructions = [(direction, int(steps)) for direction, steps, _ in [line.split() for line in input]]

    




def follow_dig_plan(instructions):
    global points
    points = set()
    x, y = 0, 0

    for direction, steps in instructions:
        if direction == 'R':
            points.update([(x+i, y) for i in range(steps)])
            x += int(steps)
        elif direction == 'L':
            points.update([(x-i, y) for i in range(steps)])
            x -= int(steps)
        elif direction == 'U':
            points.update([(x, y-i) for i in range(steps)])
            y -= int(steps)
        elif direction == 'D':
            points.update([(x, y+i) for i in range(steps)])
            y += int(steps)

    add_content(1, 1)
    return len(points)
 

def add_content(x, y):
    global points
    
    # Base case
    if (x, y) in points:
        return 0
    
    points.add((x, y))
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        add_content(x+dx, y+dy)