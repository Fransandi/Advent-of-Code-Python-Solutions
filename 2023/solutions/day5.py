'''
=========================================
|| 🎄 Advent of Code 2023: Day 5 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: ...
=========================================
'''


# Part One
def part_one(input):
    seeds, all_levels = parse_input(input)

    # Convert all seeds one by one
    for seed_index in range(len(seeds)):
        for level in all_levels:
            seed = seeds[seed_index]
            for destination, source, length in level:
                if seed >= source and seed <= source + length - 1:
                    seeds[seed_index] = (seed - source) + destination
                    continue

    return min(seeds)


# Part Two
def part_two(input):
    seeds_range, all_levels = parse_input(input)

    # Parse seeds ranges
    seeds = []
    for i in range(len(seeds_range) // 2):
        left = seeds_range[i*2]
        right = left + seeds_range[(i*2)+1] - 1
        seeds.append((left, right))

    # Explore all levels of conversion
    for level in all_levels:
        updated_seeds = []
        next_level = []
        for destination, source, length in level:
            while seeds:
                seed = seeds.pop()
                left, right = source, source + length - 1
                overlap = get_overlapping_ranges(seed, (left, right))

                # No overlap was found
                if len(overlap) == 0:
                    next_level.append(seed)

                # Analyze overlapping ranges
                for seed_range in overlap:
                    if (left <= seed_range[0] and right >= seed_range[1]):
                        updated_left = (seed_range[0] - source) + destination
                        updated_right = (seed_range[1] - source) + destination
                        updated_seeds.append((updated_left, updated_right))
                    else:
                        next_level.append(seed_range)

            seeds = next_level
            next_level = []

        seeds = list(set(seeds + updated_seeds))

    return min([val[0] for val in list(set(seeds + updated_seeds))])


def parse_input(input):
    almanac = [line.strip() for line in input]
    seeds = [int(seed) for seed in almanac[0].split(':')[1].split()]
    all_levels, current_level = [], []
    for line in almanac[2:]:
        if 'map' not in line:
            if line == '':
                all_levels.append(current_level)
                current_level = []
            else:
                current_level.append([int(num) for num in line.split()])
    all_levels.append(current_level)

    return seeds, all_levels


def get_overlapping_ranges(range1, range2):
    start1, end1 = range1
    start2, end2 = range2

    # Full overlap
    if start1 >= start2 and end1 <= end2:
        return [range1]

    # No overlap
    if end2 < start1 or start2 > end1:
        return []

    # Left overlap
    if start2 <= start1 and end2 < end1:
        return [(start1, end2), (end2+1, end1)]

    # Right overlap
    if end2 >= end1 and start2 > start1:
        return [(start1, start2-1), (start2, end1)]

    # Narrow overlap
    if start1 < start2 and end1 > end2:
        return [(start1, start2-1), (start2, end2), (end2+1, end2)]

    return []
