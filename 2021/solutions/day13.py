'''
=========================================
|| 🎄 Advent of Code 2021: Day 13 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    paper, instructions = parse_input(input)
    folded_paper = fold(paper, instructions[:1])
    return sum([row_sum for row_sum in [sum(row) for row in folded_paper]])

### Part Two
def part_two(input):
    paper, instructions = parse_input(input)
    folded_paper = fold(paper, instructions)
    
    # Uncomment the following line to see the characters printed on the terminal
    # print_message(folded_paper)
    return 0


def parse_input(input):
    points, instructions = [], []
    width = height = 0

    for line in input:
        # Parse points
        if ',' in line:
            point = line.strip().split(',')
            x, y = int(point[0]), int(point[1])
            width, height = max(width, x), max(height, y)
            points.append((x, y))
        
        # Parse instructions
        elif 'fold along' in line:
            instruction = line.split()[-1].split('=')
            instructions.append((instruction[0], int(instruction[1])))

    # Initial paper configuration
    paper = [[False]*(width+1) for _ in range(height+1)]
    for x, y in points: 
        paper[y][x] = True

    return paper, instructions

def fold(paper, instructions):
    for direction, line in instructions:
        if direction == 'y': paper = fold_up(paper, line)
        if direction == 'x': paper = fold_left(paper, line)
    return paper

def fold_up(paper, line):
    upper_half = [row for i, row in enumerate(paper) if i < line]
    lower_half = [row for i, row in enumerate(paper) if i > line]

    for y in range(len(lower_half)):
        for x in range(len(lower_half[0])):
            if lower_half[y][x]:
                upper_half[len(upper_half)-y-1][x] = True

    return upper_half

def fold_left(paper, line):
    right_half = [row[:line] for row in paper]
    left_half = [row[line+1:][::-1] for row in paper]

    for y in range(len(left_half)):
        for x in range(len(left_half[0])):
            if left_half[y][x]:
                right_half[y][x] = True
    
    return right_half

def print_message(paper):
    for row in paper: 
        print(''.join('#' if mark else ' ' for mark in row))
