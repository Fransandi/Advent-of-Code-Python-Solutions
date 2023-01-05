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

### Part One
def part_one(input):
    board, instructions = parse_input(input)
    i, j, direction = 0, board[0].index(SPACE), RIGHT
    while instructions:
        next_move = instructions.pop(0)

        if isinstance(next_move, int):
            if direction == RIGHT: i, j = move_right(board, i, j, next_move)
            if direction == DOWN:  i, j = move_down(board, i, j, next_move)
            if direction == LEFT:  i, j = move_left(board, i, j, next_move)
            if direction == UP:    i, j = move_up(board, i, j, next_move)
        else:
            if next_move == 'R': direction = 0 if direction == 3 else direction+1
            if next_move == 'L': direction = 3 if direction == 0 else direction-1

    return 1000*(i+1) + 4*(j+1) + direction

### Part Two
def part_two(input):
    pass


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

def move_right(board, i, j, n):
    wrap_j = 0
    while board[i][wrap_j] == VOID: wrap_j+=1
    for _ in range(n):
        next_j = wrap_j if j==len(board[i])-1 or board[i][j+1] == VOID else j+1
        if board[i][next_j] == WALL: break
        j = next_j
    return i, j

def move_down(board, i, j, n):
    wrap_i = 0
    while board[wrap_i][j] == VOID: wrap_i+=1
    for _ in range(n):
        next_i = wrap_i if i==len(board)-1 or board[i+1][j] == VOID else i+1
        if board[next_i][j] == WALL: break
        i = next_i
    return i, j

def move_left(board, i, j, n):
    wrap_j = len(board[0])-1
    while board[i][wrap_j] == VOID: wrap_j-=1
    for _ in range(n):
        next_j = wrap_j if j==0 or board[i][j-1] == VOID else j-1
        if board[i][next_j] == WALL: break
        j = next_j
    return i, j

def move_up(board, i, j, n):
    wrap_i = len(board)-1
    while board[wrap_i][j] == VOID: wrap_i-=1
    for _ in range(n):
        next_i = wrap_i if i==0 or board[i-1][j] == VOID else i-1
        if board[next_i][j] == WALL: break
        i = next_i
    return i, j
