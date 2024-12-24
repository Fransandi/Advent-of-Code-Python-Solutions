'''
=========================================
|| 🎄 Advent of Code 2024: Day 17 🗓
|| Link: https://adventofcode.com/2024
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


def parse_input(input):
    a, b, c, program = None, None, None, []
    for line in input:
        if 'A:' in line:
            a = int(line.split('A: ')[1])
        if 'B:' in line:
            b = int(line.split('B: ')[1])
        if 'C:' in line:
            c = int(line.split('C: ')[1])
        if 'Program:' in line:
            instructions = line.split('Program: ')[1].split(',')
            for i in range(len(instructions)//2):
                program.append(
                    (int(instructions[i*2]), int(instructions[i*2+1])))

    return a, b, c, program


def apply_opcode(opcode, operand, a, b, c, i, output):

    def get_combo_operand(operand, a, b, c):
        operand_map = {4: a, 5: b, 6: c}
        return operand_map.get(operand, operand)

    # Opcode 0: adv
    if opcode == 0:
        operand = get_combo_operand(operand, a, b, c)
        a = int(a/(pow(2, operand)))
        i += 1

    # Opcode 1: bxl
    elif opcode == 1:
        b = b ^ operand
        i += 1

    # Opcode 2: bst
    elif opcode == 2:
        operand = get_combo_operand(operand, a, b, c)
        b = operand % 8
        i += 1

    # Opcode 3: jnz
    elif opcode == 3:
        i = operand if a != 0 else i+1

    # Opcode 4: bxc
    elif opcode == 4:
        b = b ^ c
        i += 1

        # Opcode 5: out
    elif opcode == 5:
        operand = get_combo_operand(operand, a, b, c)
        output.append(operand % 8)
        i += 1

    # Opcode 6: bdv
    elif opcode == 6:
        operand = get_combo_operand(operand, a, b, c)
        b = int(a/(pow(2, operand)))
        i += 1

    # Opcode 7: cdv
    elif opcode == 7:
        operand = get_combo_operand(operand, a, b, c)
        c = int(a/(pow(2, operand)))
        i += 1

    return a, b, c, i, output


def run_program(a, b, c, program):
    i, output = 0, []
    while i < len(program):
        opcode, operand = program[i]
        a, b, c, i, output = apply_opcode(opcode, operand, a, b, c, i, output)

    return output


def part_two_handler(a, b, c, program, expected, index):
    result = set()

    # For each value of N from 0 to 7
    for n in range(8):
        # Shift A by 3 bits and add the new value of N
        new_a = (a << 3) | n

        # Run the program with the new value of A
        output = run_program(new_a, b, c, program)

        # Check if the last "index" elements of the output match the expected output
        if output == expected[-index:]:
            # If the output matches the expected output, add the value of A to the result
            if output == expected:
                result.add(new_a)
            else:
                # Increment the index and recursively call the function
                possible = part_two_handler(
                    new_a, b, c, program, expected, index+1)

                # If the recursive call returns a value, add it to the result
                if possible:
                    result.add(possible)

    # Return the minimum value of the result, if any
    return min(result) if len(result) > 0 else 0


# Part One
def part_one(input):
    # Parse input
    a, b, c, program = parse_input(input)

    # Run the program
    output = run_program(a, b, c, program)

    # Return the output, separated by commas
    return ','.join(map(str, output))


# Part Two
def part_two(input):
    # Parse input
    _, b, c, program = parse_input(input)

    # Determine the expected output
    expected = []
    for i in program:
        expected.extend([i[0], i[1]])

    # Recursively, find the value of A that produces the expected output
    return part_two_handler(0, b, c, program, expected, 1)
