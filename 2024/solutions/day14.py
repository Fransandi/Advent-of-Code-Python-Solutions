'''
=========================================
|| 🎄 Advent of Code 2024: Day 14 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

WIDTH = 101
HEIGHT = 103


def parse_input(input):
    robots = []
    for line in input:
        line = line.strip().replace('p=', '').replace('v=', '').split(' ')
        position = tuple(map(int, line[0].split(',')))
        velocity = tuple(map(int, line[1].split(',')))
        robots.append([position, velocity])
    return robots


def update_position(position, velocity):
    # Update the position of the robot
    x = position[0] + velocity[0] % WIDTH
    y = position[1] + velocity[1] % HEIGHT

    # Wrap around the grid if the robot goes out of bounds
    if x < 0:
        x = WIDTH - x
    if y < 0:
        y = HEIGHT - y
    if x >= WIDTH:
        x -= WIDTH
    if y >= HEIGHT:
        y -= HEIGHT

    # Return the new position
    return (x, y)


def get_quadrants(positions):
    # Count the number of positions that are in each quadrant
    x_left_bound, x_right_bound = WIDTH // 2, WIDTH - (WIDTH // 2)
    y_top_bound, y_bottom_bound = HEIGHT // 2, HEIGHT - (HEIGHT // 2)

    # Return the number of positions in each quadrant
    quadrants = [0, 0, 0, 0]
    for position in positions:
        x, y = position
        if x < x_left_bound and y < y_top_bound:
            quadrants[0] += 1
        elif x < x_left_bound and y >= y_bottom_bound:
            quadrants[1] += 1
        elif x >= x_right_bound and y < y_top_bound:
            quadrants[2] += 1
        elif x >= x_right_bound and y >= y_bottom_bound:
            quadrants[3] += 1

    # Return the number of positions in each quadrant
    return quadrants


# Part One
def part_one(input):
    # Parse the input
    robots = parse_input(input)

    # Simulate the robots' movement for 100 steps, and store the final positions
    positions = []
    for (position, velocity) in robots:
        for _ in range(100):
            position = update_position(position, velocity)
        positions.append(position)

    # Return the product of the number of positions in each quadrant
    quadrants = get_quadrants(positions)

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


# Part Two
def part_two(inputa):
    # Parse the input
    robots = parse_input(inputa)

    # Skip the Example
    if len(robots) < 15:
        return -1

    # Display the robots' movement for many steps
    for step in range(10000):
        positions = []
        for r in range(len(robots)):
            position = update_position(robots[r][0], robots[r][1])
            robots[r][0] = position
            positions.append(position)

        # Print the positions if there are no repeated positions (easter egg)
        if len(positions) == len(set(positions)):
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if (j, i) in positions:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()

            # Return the step number
            return step + 1

    # Return -1 if condition is not met
    return -1
