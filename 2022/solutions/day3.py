'''
=========================================
|| 🎄 Advent of Code 2022: Day 3 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 


### Part One
def part_one(input):
    total_priority = 0

    for rucksack in input:
        item = get_wrong_item(rucksack)
        total_priority += get_priority(item)

    return total_priority

### Part Two
def part_two(input):
    total_priority = 0
    common_items = set()

    for rucksack in [set(line.strip()) for line in input]:
        # Get the common item types of the current rucksack and the previous
        common_items = common_items & rucksack if common_items else rucksack

        # Once we found the only common item type, we get its priority and clean the set
        if len(common_items)==1: total_priority += get_priority(common_items.pop())

    return total_priority


def get_wrong_item(rucksack):
    first_compartment = set()

    for i, char in enumerate(rucksack):
        if i <= len(rucksack)/2-1:
            first_compartment.add(char)
        elif char in first_compartment:
            return char

def get_priority(item): return ord(item)-96 if item.islower() else ord(item)-38
