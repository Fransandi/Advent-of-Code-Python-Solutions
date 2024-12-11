'''
=========================================
|| 🎄 Advent of Code 2024: Day 11 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


from functools import lru_cache


# Memoization, to avoid re-calculating the same stone multiple times
@lru_cache(maxsize=None)
def count_final_stones(stone, blink):
    # Base case: if depth is 0, return 1
    if blink == 0:
        return 1

    # Rule 1: If stone is 0, return 1
    if stone == 0:
        return count_final_stones(1, blink - 1)

    # Rule 2: If stone has an even number of digits, split it into two halves
    digits = len(str(stone))
    if digits % 2 == 0:
        left = stone // 10 ** (digits // 2)
        right = stone % 10 ** (digits // 2)
        return count_final_stones(left, blink - 1) + count_final_stones(right, blink - 1)

    # Rule 3: Multiply it by 2024
    return count_final_stones(stone * 2024, blink - 1)


# Part One
def part_one(input):
    # Parse input
    stones = [int(num) for line in input for num in line.split()]

    # Count the final number of stones after 25 blinks
    return sum(count_final_stones(stone, 25) for stone in stones)


# Part Two
def part_two(input):
    # Parse input
    stones = [int(num) for line in input for num in line.split()]

    # Count the final number of stones after 75 blinks
    return sum(count_final_stones(stone, 75) for stone in stones)
