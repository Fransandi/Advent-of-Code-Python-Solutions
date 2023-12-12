'''
=========================================
|| 🎄 Advent of Code 2023: Day 9 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    total = 0
    for line in input:
        numbers = generate_steps(line)
        history, below = 0, 0
        while numbers:
            below = history
            history = numbers.pop()[-1] + below
        total += history
    return total
            

### Part Two
def part_two(input):
    total = 0
    for line in input:
        numbers = generate_steps(line)
        history, below = 0, 0
        while numbers:
            below = history
            history = numbers.pop()[0] - below
        total += history
    return total
    

def generate_steps(initial):
    numbers = [[int(num) for num in initial.split()]]
    while not min(numbers[-1]) == max(numbers[-1]):
        numbers.append([])
        for i in range(len(numbers[-2]) - 1):
            numbers[-1].append(numbers[-2][i + 1] - numbers[-2][i])
    return numbers
