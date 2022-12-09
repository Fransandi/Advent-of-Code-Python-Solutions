'''
=========================================
|| 🎄 Advent of Code 2022: Day 9 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    return helper(input, 2)

### Part Two
def part_two(input):
    return helper(input, 10)


def helper(input, rope_length):
    rope = [[0, 0] for _ in range(rope_length)]
    visited = {(0, 0)}

    for direction, steps in [line.split() for line in input]:   
        for _ in range(int(steps)):
            update_head(rope[0], direction)

            # Update the rest of the knots if needed
            for i in range(1, len(rope)):
                if not_touching(rope[i-1], rope[i]):
                    update_knot(rope[i-1], rope[i])

                    if i==rope_length-1: 
                        visited.add(tuple(rope[-1]))

    return len(visited)

def update_head(head, direction):
    if direction == 'R': head[0]+=1
    if direction == 'L': head[0]-=1
    if direction == 'D': head[1]+=1
    if direction == 'U': head[1]-=1

def not_touching(p1, p2): return abs(p1[0]-p2[0])>1 or abs(p1[1]-p2[1])>1

def update_knot(prev, knot):
    if prev[0]<knot[0]: knot[0]-=1
    if prev[0]>knot[0]: knot[0]+=1
    if prev[1]<knot[1]: knot[1]-=1
    if prev[1]>knot[1]: knot[1]+=1
