'''
=========================================
|| 🎄 Advent of Code 2023: Day 7 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


from functools import cmp_to_key


# Part One
def part_one(input):
    cards = [(line.split()[0], int(line.split()[1])) for line in input]
    key_function = cmp_to_key(rank_cards)
    ranked_cards = sorted(cards, key=key_function)
    return sum([(i+1) * card[1] for i, card in enumerate(ranked_cards)])


# Part Two
def part_two(input):
    cards = [(line.split()[0], int(line.split()[1])) for line in input]
    key_function = cmp_to_key(rank_cards_with_joker)
    ranked_cards = sorted(cards, key=key_function)
    return sum([(i+1) * card[1] for i, card in enumerate(ranked_cards)])


def rank_cards(x, y):
    x_type = get_type_of_hand(x[0])
    y_type = get_type_of_hand(y[0])

    if x_type != y_type:
        return x_type - y_type

    for i in range(5):
        x_pos = 'AKQJT98765432'.find(x[0][i])
        y_pos = 'AKQJT98765432'.find(y[0][i])

        if x_pos != y_pos:
            return y_pos - x_pos

    return 0


def rank_cards_with_joker(x, y):
    x_type = get_type_of_hand(x[0], True)
    y_type = get_type_of_hand(y[0], True)

    if x_type != y_type:
        return x_type - y_type

    for i in range(5):
        x_pos = 'AKQT98765432J'.find(x[0][i])
        y_pos = 'AKQT98765432J'.find(y[0][i])

        if x_pos != y_pos:
            return y_pos - x_pos

    return 0


def get_type_of_hand(cards, with_joker=False):
    char_counts = {}
    for char in cards:
        char_counts[char] = char_counts.get(char, 0) + 1

    jokers = 0
    if with_joker:
        if "J" in char_counts:
            jokers = char_counts.pop('J')
            if jokers == 5:
                return 7

    amounts = sorted(char_counts.values())
    amounts[-1] += jokers

    # Five of a kind
    if amounts[-1] == 5:
        return 7

    # Four of a kind
    if amounts[-1] == 4:
        return 6

    # Full house
    if amounts[-1] == 3 and amounts[-2] == 2:
        return 5

    # Three of a kind
    if amounts[-1] == 3:
        return 4

    # Two pairs
    if amounts[-1] == 2 and amounts[-2] == 2:
        return 3

    # One pair
    if amounts[-1] == 2:
        return 2

    # High card
    return 1
