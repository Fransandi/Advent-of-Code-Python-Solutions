'''
=========================================
|| 🎄 Advent of Code 2021: Day 5 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from typing import DefaultDict

### Part One
def part_one(input):
    points_count = DefaultDict(int)

    for line in input:
        # Parse line
        source = line.split()[0]
        end = line.split()[-1]
        [x1, y1] = list(map(int, source.split(',')))
        [x2, y2] = list(map(int, end.split(',')))

        # Count points for vertical lines
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points_count[(x1, y)]+=1

        # Count points for horizontal lines
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                points_count[(x, y1)]+=1

    # Return the total amount of overlapping points
    return len([key for key in points_count.keys() if points_count[key]>1])


### Part Two
def part_two(input):
    points_count = DefaultDict(int)
    
    for line in input:
        # Parse line
        source, end = line.split()[0], line.split()[-1]
        [x1, y1] = list(map(int, source.split(',')))
        [x2, y2] = list(map(int, end.split(',')))

        # Count points for vertical lines
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points_count[(x1, y)]+=1

        # Count points for horizontal lines
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                points_count[(x, y1)]+=1

        # Count points for diagonal lines
        elif abs(x1-x2) == abs(y1-y2):
            for i in range(abs(x1-x2)+1):
                x = x1-i if x1 > x2 else x1+i
                y = y1-i if y1 > y2 else y1+i
                points_count[(x, y)]+=1

    # Return the total amount of overlapping points
    return len([key for key in points_count.keys() if points_count[key]>1])
