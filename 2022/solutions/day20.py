'''
=========================================
|| 🎄 Advent of Code 2022: Day 20 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from collections import deque

DECRIPTION_KEY = 811589153

### Part One
def part_one(input):
    file = deque([(index, int(number.strip())) for index, number in enumerate(input)])
    file = mix_file(file)
    return groove_coordinates(file)
    
### Part Two
def part_two(input):
    file = deque([(index, int(number.strip())*DECRIPTION_KEY) for index, number in enumerate(input)])
    file = mix_file(file, 10)
    return groove_coordinates(file)
    

def mix_file(file, times=1):
    for _ in range(times):
        for index in range(len(file)):
            # Move the next number to the beggining of the list
            while file[0][0] != index: file.rotate(-1)

            # Move the circular list until the next position
            next_number = file.popleft()
            move = next_number[1]%len(file)
            file.rotate(-move)

            # Insert the number in its new position
            file.append(next_number)

    return file

def groove_coordinates(file):
    zero_position = [index for (index, number) in enumerate(file) if number[1]==0][0]
    return sum([file[(zero_position + groove)%len(file)][1] for groove in [1000, 2000, 3000]])