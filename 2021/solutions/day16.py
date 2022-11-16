'''
=========================================
|| 🎄 Advent of Code 2021: Day 16 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import math

# Part One
def part_one(input):
    decode_transmission(input[0])
    packets = decode_next_packet()
    return calculate_version_sum(packets)

# Part Two
def part_two(input):
    decode_transmission(input[0])
    packets = decode_next_packet()
    return calculate_value(packets)

def decode_transmission(hex_transmission):
    # This function decodes the transmission and initializes the pointer
    global transmission
    global pointer

    transmission = str(bin(int(hex_transmission, base=16)))[2:].zfill(len(hex_transmission) * 4)
    pointer = 0

def decode_next_n_bits(n):
    # This function decodes the next n bits to int, and updates the pointer
    global pointer
    pointer+=n

    return int(transmission[pointer-n:pointer], 2)

def decode_next_packet(pointer = 0):
    # This function decodes the next packet
    version = decode_next_n_bits(3)
    type_id = decode_next_n_bits(3)

    if type_id == 4: 
        value = calculate_literal_value()
    else: 
        value = decode_operator_packet()

    return (version, type_id, value)

def calculate_literal_value():
    literal_value = ''

    while True:
        prefix = decode_next_n_bits(1)
        literal_value += transmission[pointer:pointer+4]
        decode_next_n_bits(4)
        if not prefix: break

    return int(literal_value, 2)

def decode_operator_packet():
        length_type_id = decode_next_n_bits(1)

        if length_type_id:
            num_of_packets = decode_next_n_bits(11)
            return [decode_next_packet() for _ in range(num_of_packets)]
        else:
            subpackets, subpackets_length = [], decode_next_n_bits(15)
            end = pointer + subpackets_length

            while pointer < end:
                subpackets.append(decode_next_packet())
            return subpackets

def calculate_version_sum(packets):
    version, type_id, value = packets

    # Base case: the packet has a literal value
    if type_id == 4: 
        return version
    
    return version + sum([calculate_version_sum(subpacket) for subpacket in value ])

def calculate_value(packets):
    _, type_id, value = packets

    # Base case: the packet has a literal value
    if type_id == 4: 
        return value

    subpackets_val = [calculate_value(subpacket) for subpacket in value]

    if type_id == 0: return sum(subpackets_val)
    if type_id == 1: return math.prod(subpackets_val)
    if type_id == 2: return min(subpackets_val)
    if type_id == 3: return max(subpackets_val)
    if type_id == 5: return 1 if subpackets_val[0] > subpackets_val[1] else 0
    if type_id == 6: return 1 if subpackets_val[0] < subpackets_val[1] else 0
    if type_id == 7: return 1 if subpackets_val[0] == subpackets_val[1] else 0
