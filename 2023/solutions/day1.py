'''
=========================================
|| 🎄 Advent of Code 2023: Day 1 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

### Part One
def part_one(input):
    count = 0
    for line in input:
        first, last = 0, 0
        for char in line:
            if char.isnumeric():
                if not first: first = char
                last = char

        count += int(first) * 10 + int(last)

    return count

### Part Two
def part_two(input):
    NUMS = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
    count = 0

    for line in input:
        first_val, last_val = 0, 0
        first_index, last_index = len(line), -1

        for substring in [str(num) for pair in NUMS.items() for num in pair]:
            if substring in line:
                left_index = line.find(substring)
                right_index = line.rindex(substring)

                if left_index < first_index:
                    first_val = substring
                    first_index = left_index

                if right_index > last_index:
                    last_val = substring
                    last_index = right_index

        if first_val in NUMS.keys(): first_val = NUMS[first_val]
        if last_val in NUMS.keys(): last_val = NUMS[last_val]

        count += int(first_val) * 10 + int(last_val)

    return count