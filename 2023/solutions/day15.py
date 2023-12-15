'''
=========================================
|| 🎄 Advent of Code 2023: Day 15 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# Part One
def part_one(input):
    steps = [line.strip().split(',') for line in input][0]
    result = 0
    for step in steps:
        result += hash_algorithm(step)
    return result


# Part Two
def part_two(input):
    steps = [line.strip().split(',') for line in input][0]
    boxes = {i: [] for i in range(256)}

    for step in steps:
        if '=' in step:
            lens = step.split('=')
            box = hash_algorithm(lens[0])

            found = False
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == lens[0]:
                    boxes[box][i][1] = lens[1]
                    found = True

            if not found:
                boxes[box].append(lens)

        else:
            lens = step[:-1]
            box = hash_algorithm(lens)
            boxes[box] = [item for item in boxes[box] if item[0] != lens]

    score = 0
    for box in range(256):
        for slot in range(len(boxes[box])):
            score += (box + 1) * (slot + 1) * int(boxes[box][slot][1])

    return score


def hash_algorithm(string):
    current_value = 0
    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256
    return current_value
