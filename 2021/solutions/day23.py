'''
=========================================
|| 🎄 Advent of Code 2021: Day 23 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from functools import lru_cache

ROOM_POS_IN_HALLWAY = {0: 2, 1: 4, 2: 6, 3: 8}
ALLOWED_HALLWAY_POSITIONS = [0, 1, 3, 5, 7, 9, 10]
LARGE_NUMBER = float('inf')

### Part One
def part_one(input):
    hallway, rooms = parse_input(input)
    return simulate(*serialize_input(rooms, hallway))

### Part Two
def part_two(input):
    hallway, rooms = parse_input(input) 
    # Add new amphipods to the rooms
    new_amphipods = [[3, 3], [2, 1], [1, 0], [0, 2]]
    rooms = [rooms[i][:1] + new_amphipods[i] + rooms[i][1:] for i in range(4)]
    return(simulate(*serialize_input(rooms, hallway)))


def parse_input(input):
    amphiphods = [line.strip().replace('#','') for line in input if any(x in line for x in list('ABCD'))]
    rooms = [['ABCD'.index(amphiphods[i][j]) for i in range(len(amphiphods))] for j in range(4)]
    hallway = [None]*11
    return hallway, rooms

@lru_cache(maxsize=None)
def simulate(rooms, hallway):
    rooms, hallway = deserialize_input(rooms, hallway)
    min_energy = LARGE_NUMBER

    # Base case: all amphiphods are in its final position
    if amphiphods_ready(rooms): return 0

    # Move amphiphods from hallway to room, if possible
    for h_amph, h_pos in [(hallway[pos], pos) for pos in ALLOWED_HALLWAY_POSITIONS if hallway[pos]!=None]:
        room = rooms[h_amph]
        
        if cannot_enter_room(h_amph, room): continue
        
        r_pos = len(room)-1-room[::-1].index(None)
        energy = calculate_energy(hallway, h_amph, ROOM_POS_IN_HALLWAY[h_amph], h_pos, r_pos, True)

        if energy != LARGE_NUMBER:
            temp_room = room[:r_pos] + [h_amph] + room[r_pos+1:]
            temp_rooms = rooms[:h_amph] + [temp_room] + rooms[h_amph+1:]
            temp_hallway = hallway[:h_pos] + [None] + hallway[h_pos+1:]
            
            min_energy = min(min_energy, energy + simulate(*serialize_input(temp_rooms, temp_hallway)))
    
    # Move amphiphods from rooms to hallway, if possible
    for r_num, room in enumerate(rooms):
        if room_cannot_be_left(r_num, room): continue
        
        r_pos, r_amph = next((pos, amph) for pos, amph in enumerate(room) if amph!=None)

        if amph_cannot_leave(r_pos, r_num, room): continue

        for h_pos in [pos for pos in ALLOWED_HALLWAY_POSITIONS if hallway[pos]==None]:
            energy = calculate_energy(hallway, r_amph, ROOM_POS_IN_HALLWAY[r_num], h_pos, r_pos)

            if energy != LARGE_NUMBER:
                temp_room = room[:r_pos] + [None] + room[r_pos+1:]
                temp_rooms = rooms[:r_num] + [temp_room] + rooms[r_num+1:]
                temp_hallway = hallway[:h_pos] + [r_amph] + hallway[h_pos+1:]
                
                min_energy = min(min_energy, energy + simulate(*serialize_input(temp_rooms, temp_hallway)))

    return min_energy

def calculate_energy(hallway, amph, d_pos, h_pos, r_pos, amph_in_hallway=False):
    path_to_door = hallway[min(d_pos,h_pos):max(d_pos,h_pos)+1]

    # Return LARGE_NUMBER if any unexpected amphiphod is blocking the path
    if len([amph for amph in path_to_door if amph!=None])!= amph_in_hallway: 
        return LARGE_NUMBER

    return (len(path_to_door) + r_pos) * 10**amph

def serialize_input(rooms, hallway): return tuple(tuple(room) for room in rooms), tuple(hallway)

def deserialize_input(rooms, hallway): return list(list(room) for room in rooms), list(hallway)

def amphiphods_ready(rooms): return all(room_has_only(room, amph) for amph, room in enumerate(rooms))

def room_cannot_be_left(r_num, room): return room_has_only(room, r_num) or room_has_only(room, None)

def amph_cannot_leave(r_pos, r_num, room): return room_has_only(room[r_pos:], r_num)

def room_has_only(room, obj): return all(pos==obj for pos in room)

def cannot_enter_room(amph, room): return not all(room_amph in {amph, None} for room_amph in room)
