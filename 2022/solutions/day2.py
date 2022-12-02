'''
=========================================
|| 🎄 Advent of Code 2022: Day 2 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

### Part One
def part_one(input):
    score = 0
    strategy_decode = { 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS }

    for line in input:
        opponent, player = line.strip().split(' ')
        player = strategy_decode[player]
        score += round_score(player, opponent)

    return score

### Part Two
def part_two(input):
    score = 0

    for line in input:
        opponent, player = line.strip().split(' ')
        player = part_two_strategy_decode(opponent, player)
        score += round_score(player, opponent)

    return score


def round_score(player, opponent):
    score = { ROCK: 1, PAPER: 2, SCISSORS: 3 }[player]
    
    # Draw
    if player == opponent: return score + 3

    # Player won
    if (player, opponent) in {(ROCK, SCISSORS),(SCISSORS, PAPER),(PAPER, ROCK)}: return score + 6
    
    # Player lost
    return score

def part_two_strategy_decode(opponent, player):
    # Player needs to draw round
    if player == 'Y': return opponent

    #  Player needs to either win or lose.
    if opponent == ROCK: return SCISSORS if player == 'X' else PAPER
    if opponent == SCISSORS: return PAPER if player == 'X' else ROCK
    if opponent == PAPER: return ROCK if player == 'X' else SCISSORS