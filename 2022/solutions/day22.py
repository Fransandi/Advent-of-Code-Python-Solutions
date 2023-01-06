'''
=========================================
|| 🎄 Advent of Code 2022: Day 22 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

SPACE = '.'
VOID = ' '
WALL = '#'
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
SAMPLE_INPUT = None
IS_3D = None

### Part One
def part_one(input):
    board, instructions = parse_input(input)
    set_config(board)
    return simulate(board, instructions)

### Part Two
def part_two(input):
    board, instructions = parse_input(input)
    set_config(board, is_3d=True)
    return simulate(board, instructions)


def parse_input(input):
    # Parse board
    board, row_length = [], 0
    for line in input:
        board.append(line[:-1])
        row_length = max(row_length, len(line))
        if line == '\n': break

    for row in range(len(board)): board[row] += ' '*(row_length-len(board[row])-1)

    # Parse instructions
    instructions = []
    for line in input:
        split_positions = [i for i, ltr in enumerate(line) if ltr in {'R', 'L'}]
        a = 0
        while split_positions: 
            b = split_positions.pop(0)
            instructions.append(int(line[a:b]))
            instructions.append(line[b])
            a = b+1
        instructions.append(int(line[a:]))

    return board, instructions

def set_config(board, is_3d=False):
    global SAMPLE_INPUT
    global IS_3D
    SAMPLE_INPUT = len(board)<200
    IS_3D = is_3d

def simulate(board, instructions):
    i, j, direction = 0, board[0].index(SPACE), RIGHT
    for instruction in instructions:
        if isinstance(instruction, int):
            i, j, direction = move(board, instruction, i, j, direction)
        else:
            if instruction == 'R': direction = 0 if direction == 3 else direction+1
            if instruction == 'L': direction = 3 if direction == 0 else direction-1

    return 1000*(i+1) + 4*(j+1) + direction

def move(board, n, i, j, direction):
    for step in range(n):
        if outside_bounds(board, i, j, direction):
            next_i, next_j, next_direction = wrap(board, i, j, direction)
            if board[next_i][next_j] == WALL: break
            return move(board, n-step-1, next_i, next_j, next_direction)
        else: 
            if direction == RIGHT: next_i, next_j = i, j+1
            if direction == LEFT:  next_i, next_j = i, j-1
            if direction == DOWN:  next_i, next_j = i+1, j
            if direction == UP:    next_i, next_j = i-1, j

            if board[next_i][next_j] == WALL: break

            if direction in { RIGHT, LEFT }: j = next_j
            if direction in { DOWN, UP }:    i = next_i
    
    return i, j, direction

def outside_bounds(board, i, j, direction):
    if direction == RIGHT: return j==len(board[i])-1 or board[i][j+1] == VOID
    if direction == LEFT:  return j==0               or board[i][j-1] == VOID
    if direction == DOWN:  return i==len(board)-1    or board[i+1][j] == VOID
    if direction == UP:    return i==0               or board[i-1][j] == VOID

def wrap(board, i, j, direction):
    if IS_3D: 
        if SAMPLE_INPUT: return wrap_3d_sample_cube(i, j, direction)
        else: return wrap_3d_real_cube(i, j, direction)
    else:
        return wrap_flat_cube(board, i, j, direction)

def wrap_flat_cube(board, i, j, direction):
    if direction == RIGHT:
        j = 0
        while board[i][j] == VOID: j+=1
    if direction == LEFT:
        j = len(board[0])-1
        while board[i][j] == VOID: j-=1
    if direction == DOWN:
        i = 0
        while board[i][j] == VOID: i+=1
    if direction == UP:
        i = len(board)-1
        while board[i][j] == VOID: i-=1

    return (i, j, direction)

def wrap_3d_sample_cube(i, j, direction):
    if direction == RIGHT:
        if 0 <= i <=  3:  return (11-i, 15, LEFT)
        if 4 <= i <=  7:  return (8, 15-(i-4), DOWN)
        if 8 <= i <= 11: return (3-(i-8), 11, LEFT)
    if direction == LEFT:
        if 0 <= i <=  3: return (4, i+4, DOWN)
        if 4 <= i <=  7: return (11, 15-(4-i), UP)
        if 8 <= i <= 11: return (7, 7-(8-i), UP)
    if direction == UP:
        if  0 <= j <=  3: return (0, 11-j, DOWN)
        if  4 <= j <=  7: return (j-4, 8, RIGHT)
        if  8 <= j <= 11: return (4, 11-j, DOWN)
        if 12 <= j <= 15: return (7-(12-j), 11, LEFT)
    if direction == DOWN:
        if  0 <= j <=  3: return (11, 11-j, UP)
        if  4 <= j <=  7: return (11-(j-4), 8, RIGHT)
        if  8 <= j <= 11: return (7, 3-(j-8), UP)
        if 12 <= j <= 15: return (7-(j-12), 0, RIGHT)

def wrap_3d_real_cube(i, j, direction):
    if direction == RIGHT:
        if    0 <= i <=  49: return (149-i, 99, LEFT)
        if   50 <= i <=  99: return (49, 100+(i-50), UP)
        if  100 <= i <= 149: return (49-(i-100), 149, LEFT)
        if  150 <= i <= 199: return (149, 50+(i-150), UP)
    if direction == LEFT:
        if    0 <= i <=  49: return (149-i, 0, RIGHT)
        if   50 <= i <=  99: return (100, i-50, DOWN)
        if  100 <= i <= 149: return (49-(i-100), 50, RIGHT)
        if  150 <= i <= 199: return (0, 50+(i-150), DOWN)
    if direction == UP:
        if    0 <= j <=  49: return (50+j, 50, RIGHT)
        if   50 <= j <=  99: return (150+(j-50), 0, RIGHT)
        if  100 <= j <= 149: return (199, j-100, UP)
    if direction == DOWN:
        if    0 <= j <=  49: return (0, 100+j, DOWN)
        if   50 <= j <=  99: return (150+(j-50), 49, LEFT)
        if  100 <= j <= 149: return (50+(j-100), 99, LEFT)
