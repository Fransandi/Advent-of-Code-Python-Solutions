'''
=========================================
|| 🎄 Advent of Code 2023: Day 4 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# Part One
def part_one(input):
    total_points = 0
    for card in [line.strip().split(':')[1].split('|') for line in input]:
        common_numbers = len(set(card[0].split()) & set(card[1].split()))

        # Add points if common_numbers found
        if common_numbers:
            points = 1
            for _ in range(common_numbers - 1):
                points *= 2
            total_points += points

    return total_points


# Part Two
def part_two(input):
    cards = [line.strip().split(':')[1].split('|') for line in input]
    count = dict([(i, 1) for i in range(len(cards))])

    for i, card in enumerate(cards):
        common_numbers = len(set(card[0].split()) & set(card[1].split()))

        for next in range(common_numbers):
            count[i + next + 1] += 1 * count[i]

    return (sum(count.values()))
