'''
=========================================
|| 🎄 Advent of Code 2023: Day 12 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

DIC = {}


# Part One
def part_one(input):
    combinations = 0
    for line in input:
        blocks = line.split()[0]
        nums = [int(num) for num in line.split()[1].split(',')]
        combinations += count(blocks, nums)
    return combinations


# Part Two
def part_two(input):
    combinations = 0
    for line in input:
        blocks = "?".join([line.split()[0] for i in range(5)])
        nums = [int(num) for num in line.split()[1].split(',')] * 5
        DIC.clear()
        combinations += count_with_dp(blocks, nums)
    return combinations


def count(blocks, nums, i=0):
    if i == len(blocks):
        return 1 if is_valid(blocks, nums) else 0

    if blocks[i] == "?":
        return sum([count(blocks[:i] + symbol + blocks[i+1:], nums,
                          i+1) for symbol in "#."])
    else:
        return count(blocks, nums, i+1)


def is_valid(blocks, nums):
    seen, current = [], 0
    for symbol in blocks:
        if symbol == "#":
            current += 1
        elif current > 0:
            seen.append(current)
            current = 0
    if current:
        seen.append(current)

    return seen == nums


def count_with_dp(blocks, nums, i=0, num=0, current=0):
    # DP
    key = (i, num, current)
    if key in DIC:
        return DIC[key]

    # Base case
    if i == len(blocks):
        return 1 if (num == len(nums) and current == 0) or (num == len(nums) - 1 and nums[num] == current) else 0

    # Explore all valid scenarios
    count = 0
    for symbol in "#.":
        if blocks[i] in [symbol, "?"]:
            if symbol == "." and current == 0:
                count += count_with_dp(blocks, nums, i+1, num, current)
            elif symbol == "." and current > 0 and num < len(nums) and nums[num] == current:
                count += count_with_dp(blocks, nums, i+1, num+1, 0)
            elif symbol == "#":
                count += count_with_dp(blocks, nums, i+1, num, current+1)

    DIC[key] = count
    return count
