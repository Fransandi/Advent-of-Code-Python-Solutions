'''
=========================================
|| 🎄 Advent of Code 2022: Day 23 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

NORTH = 'NORTH'
SOUTH = 'SOUTH'
WEST = 'WEST'
EAST = 'EAST'

### Part One
def part_one(input):
    board, directions = parse_input(input), [NORTH, SOUTH, WEST, EAST]

    for _ in range(10):
        board, directions = simulate_round(board, directions)

    return empty_grounds(board)

### Part Two
def part_two(input):
    board, directions = parse_input(input), [NORTH, SOUTH, WEST, EAST]

    round=1
    while True:
        temp_board = board.copy()
        board, directions = simulate_round(board, directions)
        
        if board == temp_board: return round

        round+=1

def parse_input(input):
    elves = set()
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '#': elves.add((i, j))
    return elves

def in_position(board, elf): return all((i, j) not in board for (i, j) in get_neighbours(elf[0], elf[1]))

def get_neighbours(i, j): return [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]

def simulate_round(board, directions):
    # Analyse movement proposal for all elves
    all_proposals = get_round_proposals(board, directions)
    valid_proposals = [proposal for proposal in all_proposals.items() if list(all_proposals.values()).count(proposal[1])==1]

    # Move elves into valid positions
    for (old, new) in valid_proposals:
        board.remove(old)
        board.add(new)
        
    # Update directions order
    directions.append(directions.pop(0))
    
    return board, directions

def get_round_proposals(board, directions):
    proposals = {}
    for elf in board:
        if not in_position(board, elf):
            # Check all 4 directions
            for direction in directions:
                proposal = check_direction(board, elf, direction)
                if proposal: 
                    proposals[elf] = proposal
                    break
    return proposals

def check_direction(board, elf, direction):
    i, j = elf
    if direction == NORTH:
        return (i-1,j) if all((i,j) not in board for (i,j) in [(i-1,j-1),(i-1,j),(i-1,j+1)]) else None
    if direction == SOUTH:
        return (i+1,j) if all((i,j) not in board for (i,j) in [(i+1,j-1),(i+1,j),(i+1,j+1)]) else None
    if direction == WEST:
        return (i,j-1) if all((i,j) not in board for (i,j) in [(i-1,j-1),(i,j-1),(i+1,j-1)]) else None
    if direction == EAST:
        return (i,j+1) if all((i,j) not in board for (i,j) in [(i-1,j+1),(i,j+1),(i+1,j+1)]) else None

def empty_grounds(board):
    min_i, max_i, min_j, max_j = float('inf'), float('-inf'), float('inf'), float('-inf')
    for elf in board:
        min_i, max_i = min(min_i, elf[0]), max(max_i, elf[0])
        min_j, max_j = min(min_j, elf[1]), max(max_j, elf[1])

    return ((max_i - min_i + 1) * (max_j - min_j + 1)) - len(board)