'''
=========================================
|| 🎄 Advent of Code 2022: Day 24 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

RIGHT = '>'
LEFT = '<'
UP = '^'
DOWN = 'v'

### Part One
def part_one(input):
    blizzards, width, height = parse_input(input)
    blizzard_states = precompute_blizzard_states(blizzards, width, height)
    start, end = (0, 1), (height, width-1)
    return best_time(1, start, end, blizzard_states, width, height)

### Part Two
def part_two(input):
    blizzards, width, height = parse_input(input)
    blizzard_states = precompute_blizzard_states(blizzards, width, height)
    start, end = (0, 1), (height, width-1)
    first_travel = best_time(1, start, end, blizzard_states, width, height)
    round_travel = best_time(first_travel, end, start, blizzard_states, width, height)
    total_time = best_time(round_travel, start, end, blizzard_states, width, height)
    return total_time


def parse_input(input):
    grid = [line.strip() for line in input]
    width, height = len(grid[0])-1, len(grid)-1
    blizzards = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char in [RIGHT, LEFT, UP, DOWN]:
                blizzards.append([i, j, char])

    return blizzards, width, height

def precompute_blizzard_states(blizzards, width, height):
    blizzard_positions = []

    while True:
        new_state = update_blizzards(blizzards, width, height)
        new_positions = set([(i, j) for i, j, _ in new_state])

        # Blizzards cycle found
        if new_positions in blizzard_positions: break

        blizzard_positions.append(new_positions)
        blizzards = new_state
    
    return blizzard_positions

def update_blizzards(blizzards, width, height):
    updated_blizzards = []
    for i, j, direction in blizzards:
        next_i, next_j = i, j
        
        # Move blizzard
        if direction == RIGHT: next_j = j+1
        if direction == LEFT:  next_j = j-1
        if direction == DOWN:  next_i = i+1
        if direction == UP:    next_i = i-1
        
        # Adjust blizzards reaching a wall
        if next_j == width:  next_j = 1
        if next_j == 0:      next_j = width-1
        if next_i == height: next_i = 1
        if next_i == 0:      next_i = height-1

        updated_blizzards.append([next_i, next_j, direction])
    
    return updated_blizzards

def best_time(minute, start, end, blizzard_states, width, height):
    positions = {start}
    while True:
        blizzards = blizzard_states[minute%len(blizzard_states)]
        next_positions = set()
        for position in positions:
            # Best time found
            if position == end: return minute

            # Evaluate all possible movements
            for next_position in get_next_positions(position, width, height, blizzards): next_positions.add(next_position)
            
        positions = next_positions
        minute+=1

def get_next_positions(position, width, height, blizzards):
    valid_positions = []
    i, j = position
    for next_pos in [(i+1,j),(i-1,j),(i,j),(i,j+1),(i,j-1)]:
        if is_within_bounds(next_pos, width, height) and next_pos not in blizzards:
            valid_positions.append(next_pos)
    return valid_positions

def is_within_bounds(position, width, height): 
    if position in {(0, 1), (height, width-1)}: return True
    return (position[0]>0 and position[0]<height and position[1]>0 and position[1]<width)
