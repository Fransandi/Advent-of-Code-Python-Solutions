'''
=========================================
|| 🎄 Advent of Code 2024: Day 5 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    rules, updates = {}, []

    for line in input:
        if "|" in line:
            n1, n2 = line.strip().split("|")
            if n2 not in rules:
                rules[n2] = set()
            rules[n2].add(n1)

        if "," in line:
            updates.append(line.strip().split(","))

    return rules, updates


def is_ordered_update(update, rules):
    for i, num in enumerate(update):
        if num in rules:
            if list(set(update[i+1:]) & rules[num]):
                return False
    return True


# Part One
def part_one(input):
    # Parse input
    rules, updates = parse_input(input)

    # Evaluate updates
    total = 0
    for update in updates:
        # Check if the update is ordered
        if is_ordered_update(update, rules):
            # Add the middle number to the total
            total += int(update[int(len(update) / 2)])

    return total


# Part Two
def part_two(input):
    # Parse input
    rules, updates = parse_input(input)

    # Find invalid updates
    invalid_updates = [
        update for update in updates if not is_ordered_update(update, rules)]

    # Fix invalid updates
    for update in invalid_updates:
        while not is_ordered_update(update, rules):
            for i, num in enumerate(update):
                if num in rules:
                    for j, n in enumerate(update[i+1:]):
                        # Check if the number is out of order, if so, remove it and add it after its last precondition
                        if n in rules[num]:
                            update.remove(num)
                            if j > len(update):
                                update.append(num)
                            else:
                                update.insert(j+i+1, num)

    # Return the sum of the middle numbers of the now fixed updates
    return sum(int(update[int(len(update) / 2)]) for update in invalid_updates)
