'''
=========================================
|| 🎄 Advent of Code 2021: Day 10 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from statistics import median

PAIRS = { '(': ')', '{': '}', '[': ']', '<': '>', }

### Part One
def part_one(input):
    pairs = PAIRS
    points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    score = 0

    for line in input:
        stack = []
        for char in line.strip():
            # Add 'opening' characters to the stack
            if char in pairs.keys(): stack.append(char)

            # Check if 'closing' character is illegal
            elif pairs[stack.pop()] != char:
                score+=points[char]
                continue

    return(score)

### Part Two
def part_two(input):
    pairs = PAIRS
    points = { ')': 1, ']': 2, '}': 3, '>': 4 }
    total_scores = []

    for line in input:
        # Check if line is corrupted, to skip it from the score calculation
        stack, corrupted = [], False
        for char in line.strip():
            if char in pairs.keys(): stack.append(char)
            elif pairs[stack.pop()] != char: corrupted = True
        
        # Calculate score of incomplete line
        if not corrupted:
            score = 0
            while len(stack):
                score *= 5
                score += points[pairs[stack.pop()]]
            total_scores.append(score)

    # Return the middle score
    return median(total_scores)
    