'''
=========================================
|| 🎄 Advent of Code 2023: Day 10 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    mat = [list(line.strip()) for line in input]
    nodes = explore_graph(mat)
    return len(nodes) // 2
    
### Part Two
def part_two(input):
    mat = [list(line.strip()) for line in input]
    nodes = explore_graph(mat)

    # Calculate enclosed area
    area = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i, j) not in nodes:
                passes, crossing = 0, ""
                for cell in range(j + 1, len(mat[0])):
                    if (i, cell) in nodes:
                        if mat[i][cell] == '|': passes += 1
                        elif mat[i][cell] in ['F', 'L']: crossing = mat[i][cell]
                        elif mat[i][cell] in ['7', 'J']:
                            if (mat[i][cell], crossing) in [('7', 'L'), ('J', 'F')]: passes += 1
                            crossing = ""

                if passes % 2 == 1: 
                    area += 1
    
    return area
    

def explore_graph(mat):
    # Find starting point "S"
    start = (-1, -1)
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            if col == 'S':
                start = (i, j)

    # Find starting nodes to start exploration
    nodes = []
    if start[0] > 0 and mat[start[0]-1][start[1]] in '|7F':
        nodes.append((start[0]-1, start[1]))
    if start[1] > 0 and mat[start[0]][start[1]-1] in '-LF':
        nodes.append((start[0], start[1]-1))
    if start[1] < len(mat[0])-1 and mat[start[0]][start[1]+1] in '-J7':
        nodes.append((start[0], start[1]+1))
    if start[0] < len(mat)-1 and mat[start[0]+1][start[1]] in '|JL':
        nodes.append((start[0]+1, start[1]))

    # Explore graph
    visited = {start}
    while nodes[0] != nodes[1]:
        next_nodes = []
        while nodes:
            y, x = nodes.pop()
            visited.add((y, x))

            if mat[y][x] == "|":
                next_nodes.append((y-1, x) if (y-1, x) not in visited else (y+1, x))

            if mat[y][x] == "-":
                next_nodes.append((y, x-1) if (y, x-1) not in visited else (y, x+1))

            if mat[y][x] == "L":
                next_nodes.append((y-1, x) if (y-1, x) not in visited else (y, x+1))

            if mat[y][x] == "J":
                next_nodes.append((y-1, x) if (y-1, x) not in visited else (y, x-1))

            if mat[y][x] == "7":
                next_nodes.append((y+1, x) if (y+1, x) not in visited else (y, x-1))

            if mat[y][x] == "F":
                next_nodes.append((y+1, x) if (y+1, x) not in visited else (y, x+1))

        nodes = next_nodes
    
    visited.add(nodes[0])
    return visited