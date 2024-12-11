'''
=========================================
|| 🎄 Advent of Code 2024: Day 9 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def blocks_from_disk_map(disk_map):
    blocks = []
    for i in range(len(disk_map)):
        # Add the character to the file the number of times specified by the disk map
        blocks += [str(int(i/2)) if i % 2 == 0 else '.' for _ in range(int(disk_map[i]))]
    return blocks

def apply_amphipod_moves(blocks):
    # Iterate over the blocks from the end to the start
    for i in range(len(blocks)-1, 0, -1):
        # If the block is empty, skip it
        if blocks[i] == '.':
            continue

        # Find the first empty space
        first_empty = blocks.index('.')

        # If there is no empty space or the empty space is after the current block, break
        if first_empty == -1 or first_empty >= i:
            break

        # Swap the character with the first empty space
        blocks[first_empty], blocks[i] = blocks[i], blocks[first_empty]
    
    return blocks

def apply_amphipod_moves_in_blocks(blocks):
    # Iterate over the ids from right to left
    id = int(blocks[-1])
    while id >= 0:
        # Calculate the count and start of the current id blocks
        count = blocks.count(str(id))
        start = blocks.index(str(id))
        
        # Find a group of empty blocks with the same length as the id
        i, found = 0, False
        while not found and i + count <= start:          
            # If the group of empty blocks is found, swap them with the id
            if all(block == '.' for block in blocks[i:i+count]):
                blocks = blocks[:i] + [str(id)]*count + blocks[i+count:]
                blocks = blocks[:start] + ['.']*count + blocks[start+count:]
                found = True
            i += 1
        id -= 1

    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            checksum += int(blocks[i]) * i

    return checksum

# Part One
def part_one(input):
    # Parse the input
    disk_map = [line.strip() for line in input][0]

    # Convert the disk map to blocks
    blocks = blocks_from_disk_map(disk_map)

    # Apply the amphipod moves
    blocks = apply_amphipod_moves(blocks)
    
    # Calculate the checksum
    return calculate_checksum(blocks)


# Part Two
def part_two(input):
    # Parse the input
    disk_map = [line.strip() for line in input][0]

    # Convert the disk map to blocks
    blocks = blocks_from_disk_map(disk_map)

    # Apply the amphipod moves in blocks
    blocks = apply_amphipod_moves_in_blocks(blocks)
    
    # Calculate the checksum
    return calculate_checksum(blocks)
