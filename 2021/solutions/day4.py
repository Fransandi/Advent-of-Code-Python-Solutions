'''
=========================================
|| 🎄 Advent of Code 2021: Day 4 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 

SIZE = 5

### Part One
def part_one(input):
    draw_numbers, boards, boards_marks = parse_input(input)    

    # Simulate the draw of numbers and mark the boards
    for number in draw_numbers:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for col_index, cell in enumerate(row):
                    if cell == number:
                        boards_marks[board_index][row_index][col_index] = True

                        # Check if this board won, and its points if it did
                        winner_points = check_board(board, boards_marks[board_index])
                        
                        if winner_points: 
                            return winner_points*number
    return 0

### Part Two
def part_two(input):
    draw_numbers, boards, boards_marks = parse_input(input)    
    boards_won_count = [False]*len(boards)

    # Simulate the draw of numbers and mark the boards
    for number in draw_numbers:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for col_index, cell in enumerate(row):
                    if cell == number:
                        boards_marks[board_index][row_index][col_index] = True

                        # Check if this board won, and its points if it did
                        if not boards_won_count[board_index]:
                            winner_points = check_board(board, boards_marks[board_index])
                        
                        if winner_points:
                            boards_won_count[board_index] = True

                            # Check the last winning board and return its points
                            if sum(boards_won_count) == len(boards): return winner_points*number
    return 0


def parse_input(input):
    draw_numbers = [int(num) for num in input[0].split(',')]
    boards = build_boards(input)
    boards_marks = [[[False]*SIZE for _ in range(SIZE)] for _ in range(len(boards))]

    return draw_numbers, boards, boards_marks

def build_boards(input):
    boards = temp_board = []
    for line in input:
        if line != '\n': temp_board.append([int(num) for num in line.split()])
        else:
            if len(temp_board): 
                boards.append(temp_board)
            temp_board = []
    
    return [*boards, temp_board]

def check_board(board, board_marks):
    board_points = 0
    board_won = False

    # Check rows and columns to see if the board won
    for i in range(SIZE):
        row_candidate = col_candidate = True
        
        for j in range(SIZE):
            # Check row
            if not board_marks[i][j]:
                board_points += board[i][j]
                row_candidate = False

            # Check col
            if not board_marks[j][i]:
                col_candidate = False

        if row_candidate or col_candidate:
            board_won = True
    
    if board_won: 
        return board_points
    
    return 0
