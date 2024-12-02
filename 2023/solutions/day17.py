'''
=========================================
|| 🎄 Advent of Code 2023: Day 17 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


import heapq


### Part One
def part_one(input):
    grid = [list(line.strip()) for line in input]
    
    def rules(new_count, new_dir, dir, count): return new_count <= 3
    
    return shortest_path(grid, rules)

### Part Two
def part_two(input):
    grid = [list(line.strip()) for line in input]
    
    def rules(new_count, new_dir, dir, count): return (new_count <= 10 and (new_dir==dir or count >=4 or count==-1))
    
    return shortest_path(grid, rules)

def shortest_path(grid, rules):
    rows, cols = len(grid), len(grid[0])
    queue = [(0, 0, 0, (-1, -1), -1)]
    dic = {}

    while queue:
        heat, r, c, dir, count = heapq.heappop(queue)
        key = (r, c, dir, count)

        # Skip if visited
        if key in dic: continue
        dic[key] = heat

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + dr
            new_c = c + dc
            new_dir = (dr, dc)
            new_count = (1 if new_dir != dir else count + 1)

            # Consider specific rules
            is_valid = rules(new_count, new_dir, dir, count)

            # Keep exploring
            if 0 <= new_r < rows and 0 <= new_c < cols and dir != (dr*-1, dc*-1) and is_valid:
                new_heat = heat + int(grid[new_r][new_c])
                heapq.heappush(queue, (new_heat, new_r, new_c, new_dir, new_count))
    
    min_heat = float('inf')
    for (r, c, _, _), heat in dic.items():
        if r==rows-1 and c==cols-1:
            min_heat = min(min_heat, heat)
    
    return min_heat