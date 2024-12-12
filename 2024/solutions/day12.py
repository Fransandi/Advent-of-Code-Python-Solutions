'''
=========================================
|| 🎄 Advent of Code 2024: Day 12 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


# def explore(grid, visited, queue):
#     area = 0
#     perimeter = 0

#     while queue:
#         i, j = queue.pop(0)
#         if grid[i][j] in visited:
#             continue
#         visited.add(grid[i][j])

#         # Increment area by 1
#         area += 1

#         # Count neighbors with the same letter
#         for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
#                 if grid[ni][nj] == grid[i][j]:
#                     queue.append((ni, nj))

#         # Increment perimeter by 4 minus the number of '.'
# perimeter += 4 - grid[i][j].count('.')


# Part One
def part_one(input):
    grid = [list(line.strip()) for line in input]
    height, width = len(grid), len(grid[0])
    visited = set()
    price = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] not in visited:
                queue, area, perimeter = [(i, j)], 0, 0
                while queue:
                    i, j = queue.pop(0)
                    if (i, j) in visited:
                        continue

                    visited.add((i, j))
                    area += 1

                    # Get neighbors with the same letter
                    neighbors = []
                    for ni, nj in [(i + i_next, j + j_next) for i_next, j_next in [(0, 1), (1, 0), (0, -1), (-1, 0)]]:
                        if 0 <= ni < height and 0 <= nj < width:
                            if grid[ni][nj] == grid[i][j]:
                                neighbors.append((ni, nj))

                    perimeter += 4 - len(neighbors)

                    queue.extend(
                        [(ni, nj) for ni, nj in neighbors if (ni, nj) not in visited])

                price += area * perimeter

    return price

# Part Two


def part_two(input):
    pass
