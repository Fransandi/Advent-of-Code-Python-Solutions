'''
=========================================
|| 🎄 Advent of Code 2024: Day 7 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    parsed_input = []
    for line in input:
        result = int(line.split(':')[0])
        numbers = [int(n) for n in line.split(':')[1].split()]
        parsed_input.append((result, numbers))
    return parsed_input


def is_valid(result, numbers, operators):
    # Initialize queue with the first number and next index
    queue = [(numbers[0], 1)]

    # While there are possible numbers to process
    while queue:
        number, index = queue.pop(0)

        # Edge case: If we've reached the result, return True
        if index == len(numbers):
            if number == result:
                return True
            else:
                continue

        # Calculate possible numbers with the given operators
        possible_numbers = []

        if '+' in operators:
            possible_numbers.append(number + numbers[index])

        if '*' in operators:
            possible_numbers.append(number * numbers[index])

        if '||' in operators:
            possible_numbers.append(int(str(number) + str(numbers[index])))

        # Add possible numbers to the queue if they are less than or equal to the result
        queue.extend([(n, index + 1) for n in possible_numbers if n <= result])

    return False


# Part One
def part_one(input):
    total = 0
    for result, numbers in parse_input(input):
        # If we can reach the result with the given operators, add it to the total
        if is_valid(result, numbers, ['+', '*']):
            total += result

    return total


# Part Two
def part_two(input):
    total = 0
    for result, numbers in parse_input(input):

        # If we can reach the result with the given operators, add it to the total
        if is_valid(result, numbers, ['+', '*', '||']):
            total += result

    return total
