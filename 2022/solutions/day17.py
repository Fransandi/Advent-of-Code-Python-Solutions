'''
=========================================
|| 🎄 Advent of Code 2022: Day 17 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

RIGHT = '>'
LEFT = '<'

### Part One
def part_one(input):
    return simulate(input[0], 2022)

### Part Two
def part_two(input):
    return simulate(input[0], 1000000000000)

def get_next_rock(next_rock, max_height):
    x, y = 2, max_height+4

    if next_rock == 0: return set([(x,y),(x+1,y),(x+2,y),(x+3,y)])
    if next_rock == 1: return set([(x+1,y),(x,y+1),(x+1,y+1),(x+2,y+1),(x+1,y+2)])
    if next_rock == 2: return set([(x,y),(x+1,y),(x+2,y),(x+2,y+1),(x+2,y+2)])
    if next_rock == 3: return set([(x,y),(x,y+1),(x,y+2),(x,y+3)])
    if next_rock == 4: return set([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])

def move_to_right(rock, floor): 
    if not any(x==6 or (x+1, y) in floor for (x, y) in list(rock)):
        return set([(x+1, y) for (x, y) in list(rock)])
    return rock

def move_to_left(rock, floor): 
    if not any(x==0 or (x-1, y) in floor for (x, y) in list(rock)):
        return set([(x-1, y) for (x, y) in list(rock)])
    return rock

def can_go_down(rock, floor): return not any((x, y-1) in floor for (x, y) in list(rock))

def move_down(rock): return set([(x, y-1) for (x, y) in list(rock)])

def simulate(moves, num):
    rock, next_rock = set(), 0
    floor = set([(x, 0) for x in range(7)])
    stopped_rocks, max_height, round = 0, 0, 0
    memo = set()
    states = {}

    while True:
        move = moves[round]

        # Finish condition
        if stopped_rocks == num: return max_height
        
        if not len(rock):
            rock = get_next_rock(next_rock, max_height)
            next_rock = (next_rock+1)%5

        # Move either to the left or right if possible
        if move == RIGHT: rock = move_to_right(rock, floor)
        elif move == LEFT: rock = move_to_left(rock, floor)

        # Move the rock down if possible
        if can_go_down(rock, floor): rock = move_down(rock)
        else:
            # Rock has stopped and becomes part of the floor
            max_height = max(max_height, max([y for (_, y) in rock]))
            floor.update(rock)
            rock.clear()
            stopped_rocks+=1

            # Hash state to compare later and find the cycle
            hash = hash_state(next_rock, round, max_height, floor)
            memo.add(hash)
            if hash not in states: states[hash] = [(stopped_rocks, max_height)]
            else: states[hash].append((stopped_rocks, max_height))

            # Cycle was found, calculate based on a simulation with a smaller value
            if hash in memo and len(states[hash])>1:
                rocks_cycle, height_cycle = states[hash][1][0] - states[hash][0][0], states[hash][1][1] - states[hash][0][1]
                return simulate(moves, num%rocks_cycle) + (num//rocks_cycle)*height_cycle

        round = (round+1)%len(moves)


def hash_state(next_rock, round, max_height, floor):
    hash = str(next_rock) + '-' + str(round) + '-'
    for y in range(20): hash += ''.join(['#' if (x, max_height-y) in floor else '.' for x in range(7)])+ '|'
    return hash