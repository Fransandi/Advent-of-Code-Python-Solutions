'''
=========================================
|| 🎄 Advent of Code 2024: Day 15 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

UP, DOWN, LEFT, RIGHT = '^', 'v', '<', '>'
ROBOT, WALL, EMPTY, BOX = '@', '#', '.', 'O'
BOX_LEFT, BOX_RIGHT = '[', ']'


def get_next_pos(pos, move, steps=1):
    return {
        UP: [pos[0] - steps, pos[1]],
        DOWN: [pos[0] + steps, pos[1]],
        LEFT: [pos[0], pos[1] - steps],
        RIGHT: [pos[0], pos[1] + steps]
    }[move]


def parse_input(input):
    grid, moves = [], []

    grid_complete = False
    for line in input:
        line = list(line.strip())
        if not len(line):
            grid_complete = True
        elif grid_complete:
            moves.extend(line)
        else:
            grid.append(line)

    return grid, moves


def calculate_score(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in [BOX, BOX_LEFT]:
                total += 100 * i + j
    return total


# Part One
def part_one(input):
    grid, moves = parse_input(input)
    height, width = len(grid), len(grid[0])

    # Find starting position of the robot
    pos = next(([i, j] for i in range(height)
               for j in range(width) if grid[i][j] == ROBOT), [None, None])

    for move in moves:
        # Next position
        next_pos = get_next_pos(pos, move)

        # Case 1: The next position is a wall, skip
        if grid[next_pos[0]][next_pos[1]] == WALL:
            continue

        # Case 2: The next position is empty, move the robot
        if grid[next_pos[0]][next_pos[1]] == EMPTY:
            grid[pos[0]][pos[1]] = EMPTY
            grid[next_pos[0]][next_pos[1]] = ROBOT
            pos = next_pos
            continue

        # Case 3: The next position is a box
        if grid[next_pos[0]][next_pos[1]] == BOX:
            ball_pos = next_pos

            # Find the position of the last consecutive box in the row
            ball_next_pos = get_next_pos(ball_pos, move)
            while grid[ball_next_pos[0]][ball_next_pos[1]] == BOX:
                ball_pos = ball_next_pos
                ball_next_pos = get_next_pos(ball_pos, move)
            ball_next_pos = get_next_pos(ball_pos, move)

            # Case 3.1: The next position of the box is a wall, skip
            if grid[ball_next_pos[0]][ball_next_pos[1]] == WALL:
                continue

            # Case 3.2: The next position of the box is empty, move the box and the robot
            if grid[ball_next_pos[0]][ball_next_pos[1]] == EMPTY:
                grid[pos[0]][pos[1]] = EMPTY
                grid[ball_next_pos[0]][ball_next_pos[1]] = BOX
                grid[next_pos[0]][next_pos[1]] = ROBOT
                pos = next_pos
                continue

    # Return the total score
    return calculate_score(grid)


# Part Two
def part_two(inputa):
    initial_grid, moves = parse_input(inputa)

    # Amplify the grid
    grid = []
    for initial_row in initial_grid:
        row = []
        for cell in initial_row:
            row.extend({
                ROBOT: [ROBOT, EMPTY],
                WALL: [WALL, WALL],
                BOX: [BOX_LEFT, BOX_RIGHT],
                EMPTY: [EMPTY, EMPTY]
            }[cell])
        grid.append(row)

    height, width = len(grid), len(grid[0])

    # Find starting position of the robot
    pos = next(([i, j] for i in range(height)
               for j in range(width) if grid[i][j] == ROBOT), [None, None])

    for move in moves:
        # Next position
        next_pos = get_next_pos(pos, move)

        # Case 1: The next position is a wall, skip
        if grid[next_pos[0]][next_pos[1]] == WALL:
            continue

        # Case 2: The next position is empty, move the robot
        if grid[next_pos[0]][next_pos[1]] == EMPTY:
            grid[pos[0]][pos[1]] = EMPTY
            grid[next_pos[0]][next_pos[1]] = ROBOT
            pos = next_pos
            continue

        # Case 3: The next position is a box
        if grid[next_pos[0]][next_pos[1]] in [BOX_LEFT, BOX_RIGHT]:

            # Case 3.1: Evaluate vertical moves
            can_be_moved = True
            if move in [UP, DOWN]:

                # Explore all boxes that would be moved
                queue, boxes = [next_pos], []
                while queue:
                    box_pos = queue.pop(0)

                    # Determine the left and right position of the box
                    is_right = grid[box_pos[0]][box_pos[1]] == BOX_RIGHT
                    left = [box_pos[0], box_pos[1] - is_right]
                    right = [left[0], left[1] + 1]

                    # Add the box to the list of boxes
                    boxes.extend([(left, BOX_LEFT), (right, BOX_RIGHT)])

                    # Case 3.1.1: The next position of the box is a block, add to the queue
                    left_next_pos = get_next_pos(left, move)
                    left_next_val = grid[left_next_pos[0]][left_next_pos[1]]
                    if left_next_val in [BOX_LEFT, BOX_RIGHT]:
                        queue.append(left_next_pos)

                    right_next_pos = get_next_pos(right, move)
                    right_next_val = grid[right_next_pos[0]][right_next_pos[1]]
                    if right_next_val in [BOX_LEFT, BOX_RIGHT]:
                        queue.append(right_next_pos)

                    # Case 3.1.2: The next position of the box is a wall, skip
                    if WALL in [left_next_val, right_next_val]:
                        can_be_moved = False
                        break

                if can_be_moved:
                    # Move the boxes and the robot
                    while boxes:
                        box, direction = boxes.pop()
                        n = get_next_pos(box, move)
                        grid[n[0]][n[1]] = direction
                        grid[box[0]][box[1]] = EMPTY

                    grid[next_pos[0]][next_pos[1]] = ROBOT
                    grid[pos[0]][pos[1]] = EMPTY
                    pos = next_pos

            # Case 3.2: Evaluate horizontal moves
            if move in [LEFT, RIGHT]:
                # Find the position of the last consecutive box in the row
                last_pos = next_pos
                while grid[last_pos[0]][last_pos[1]] in [BOX_LEFT, BOX_RIGHT]:
                    last_pos = get_next_pos(last_pos, move)

                # Case 3.2.1: The next position of the box is a wall, skip
                if grid[last_pos[0]][last_pos[1]] == WALL:
                    continue

                # Case 3.2.2: The next position of the box is empty, move the box and the robot
                if move == RIGHT:
                    for i in range(last_pos[1], pos[1], -1):
                        grid[next_pos[0]][i] = grid[next_pos[0]][i - 1]

                if move == LEFT:
                    for i in range(last_pos[1], pos[1]):
                        grid[next_pos[0]][i] = grid[next_pos[0]][i + 1]

                grid[pos[0]][pos[1]] = EMPTY
                pos = next_pos

    # Return the total score
    return calculate_score(grid)
