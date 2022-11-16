'''
=========================================
|| 🎄 Advent of Code 2021: Day 21 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from functools import lru_cache
from itertools import product

### Part One
def part_one(input):
    positions = [int(line.split()[-1]) for line in input]
    score = [0, 0]
    cur_player = 0
    die = 1
    
    while max(score) < 1000:
        # Roll the dices
        roll, die = (die*3)+3, die+3

        # Calculate current player new position
        new_pos = (positions[cur_player]+(roll))%10
        if not new_pos: new_pos=10
    
        # Update current player position
        positions[cur_player]=new_pos

        # Update current player score
        score[cur_player]+=new_pos

        # Switch current player and update dice
        cur_player = 1-cur_player

    return min(score)*(die-1)

### Part Two
def part_two(input):
    # Initialize players' positions
    p1_pos = int(input[0].split()[-1])
    p2_pos = int(input[1].split()[-1])
    
    wins_count = simulate_game(p1_pos, p2_pos)
    
    return(max(wins_count))

# Adding lru cache for memoization
@lru_cache(maxsize=None)
def simulate_game(p1_pos, p2_pos, p1_score=0, p2_score=0):
    
    # Base cases: a player has won
    if p1_score >= 21: return 1, 0
    if p2_score >= 21: return 0, 1

    p1_wins_count, p2_wins_count = 0, 0
    # Simulate all possible rolls
    for roll in [sum(p) for p in product([1, 2, 3], repeat=3)]:
        # Calculate current player new position
        p1_new_pos = (p1_pos+roll)%10
        if p1_new_pos==0: p1_new_pos=10

        # Calculate current player new score
        p1_new_score = p1_score + p1_new_pos

        # Simulate next turn
        p2_wins, p1_wins = simulate_game(p2_pos, p1_new_pos, p2_score, p1_new_score)

        # Add wins count for both players
        p1_wins_count+=p1_wins
        p2_wins_count+=p2_wins
    
    return p1_wins_count, p2_wins_count
