'''
=========================================
|| 🎄 Advent of Code 2022: Day 17 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

RIGHT = '>'
LEFT = '<'

### Part One
def part_one(input):
    return simulate(input, 2022)


### Part Two
def part_two(input):

    # instruction = input[0]

    # a, b = 35, 53

    # num = 1000000000000
    num = 2022

    return simulate(input, 2022)

    return 0


    # return simulate(instruction, num%a) + (num//a)*b


    moves, round = input[0], 0
    rock, next_rock = set(), 0
    floor = set([(x, 0) for x in range(7)])
    stopped_rocks, max_height = 0, 0


    memo = set()
    states = {}


    # a = 1000000000000//35
    # print('a', a)

    # return 0

    89, 142, 195

    while True:
        move = moves[round]

        # Finish condition
        # if stopped_rocks == 28571428571:
        if stopped_rocks == 27: 
            
            # for y in range(max_height):
            #     if all((x, y) in floor for x in range(7)): print(y)
            
            return max_height
        
        if not len(rock):
            rock = get_next_rock(next_rock, max_height)
            next_rock = (next_rock+1)%5

            # for y in range(max_height, max_height+5):
            #     if all((x, y) in floor for x in range(7)): print(y)

        # Move either to the left or right if possible
        if move == RIGHT: rock = move_to_right(rock, floor)
        elif move == LEFT: rock = move_to_left(rock, floor)

        # Move the rock down if possible
        if can_go_down(rock, floor): rock = move_down(rock)
        else:
            # Rock has stopped and becomes part of the floor
            max_height = max(max_height, max([y for (_, y) in rock]))

            # if any(max_height == y for (_, y) in rock): print(rock)

            floor.update(rock)
            rock.clear()
            stopped_rocks+=1
            
            hash = str(next_rock) + '-' + str(round) + '-'
            for y in range(10): hash += ''.join(['#' if (x, max_height-y) in floor else '.' for x in range(7)])+ '|'

            # print('HASH: ', hash)
            if hash in memo:
                print('REPETIDO', hash, states[hash], max_height)

                # return -1
            memo.add(hash)

            if hash not in states: 
                states[hash] = [stopped_rocks]
            else: states[hash].append(stopped_rocks)


            

            # if all((x, max_height) in floor for x in range(7)):                
            #     print(round, '-' ,stopped_rocks)

            
        
        round = (round+1)%len(moves)


def get_next_rock(next_rock, max_height):
    x, y = 2, max_height+4

    if next_rock == 0: return set([(x,y),(x+1,y),(x+2,y),(x+3,y)])
    if next_rock == 1: return set([(x+1,y),(x,y+1),(x+1,y+1),(x+2,y+1),(x+1,y+2)])
    if next_rock == 2: return set([(x,y),(x+1,y),(x+2,y),(x+2,y+1),(x+2,y+2)])
    if next_rock == 3: return set([(x,y),(x,y+1),(x,y+2),(x,y+3)])
    if next_rock == 4: return set([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])

def move_to_right(rock, floor): 
    if not any(x==6 or (x+1, y) in floor for (x, y) in list(rock)):
        return set([(x+1, y) for (x, y) in list(rock)])
    return rock

def move_to_left(rock, floor): 
    if not any(x==0 or (x-1, y) in floor for (x, y) in list(rock)):
        return set([(x-1, y) for (x, y) in list(rock)])
    return rock

def can_go_down(rock, floor): return not any((x, y-1) in floor for (x, y) in list(rock))

def move_down(rock): return set([(x, y-1) for (x, y) in list(rock)])

def simulate(input, num):
    moves, round = input[0], 0
    rock, next_rock = set(), 0
    floor = set([(x, 0) for x in range(7)])
    stopped_rocks, max_height = 0, 0

    while True:
        move = moves[round%len(moves)]

        # Finish condition
        if stopped_rocks == num: return max_height
        
        if not len(rock):
            rock = get_next_rock(next_rock, max_height)
            next_rock = (next_rock+1)%5

        # Move either to the left or right if possible
        if move == RIGHT: rock = move_to_right(rock, floor)
        elif move == LEFT: rock = move_to_left(rock, floor)

        # Move the rock down if possible
        if can_go_down(rock, floor): rock = move_down(rock)
        else:
            # Rock has stopped and becomes part of the floor
            max_height = max(max_height, max([y for (_, y) in rock]))
            floor.update(rock)
            rock.clear()
            stopped_rocks+=1
        
        round+=1


def get_cycle_values(input):
    moves, round = input[0], 0
    rock, next_rock = set(), 0
    floor = set([(x, 0) for x in range(7)])
    stopped_rocks, max_height = 0, 0

    memo = set()
    states = {}

    while True:
        move = moves[round%len(moves)]

        # Finish condition
        if stopped_rocks == 10000: return 1, 2
        
        if not len(rock):
            rock = get_next_rock(next_rock, max_height)
            next_rock = (next_rock+1)%5

        # Move either to the left or right if possible
        if move == RIGHT: rock = move_to_right(rock, floor)
        elif move == LEFT: rock = move_to_left(rock, floor)

        # Move the rock down if possible
        if can_go_down(rock, floor): rock = move_down(rock)
        else:
            # Rock has stopped and becomes part of the floor
            max_height = max(max_height, max([y for (_, y) in rock]))
            floor.update(rock)
            rock.clear()
            stopped_rocks+=1

            hash = str(next_rock) + '-' + str(round) + '-'
            for y in range(5): hash += ''.join(['#' if (x, max_height-y) in floor else '.' for x in range(7)])+ '|'

            # print('HASH: ', hash)
            if hash in memo:
                print('REPETIDO', hash, states[hash], max_height)

                # return -1
            memo.add(hash)

            if hash not in states: 
                states[hash] = [stopped_rocks]
            else: states[hash].append(stopped_rocks)
        
        round+=1
