'''
=========================================
|| 🎄 Advent of Code 2021: Day 8 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''


### Part One
def part_one(input):
    total_count = 0

    for line in input:
        digit_output = line.split('|')[1].split()
        for digit in digit_output:
            if len(digit) in {2, 3, 4, 7}: total_count += 1

    return (total_count)

### Part Two
def part_two(input):
    total_output_value = 0

    for line in input:
        # Parse input
        signal_patterns = [set(val) for val in line.split('|')[0].split()]    
        digit_output = line.split('|')[1].split()  

        # Decode signal to build digits dictionary  
        digits_dictionary = decode_signal(signal_patterns)

        # Calculate output value
        output_value = ''
        for val in [''.join(sorted(digit)) for digit in digit_output]:
            output_value += str(digits_dictionary[val])
        total_output_value += int(output_value)
    
    return total_output_value


def decode_signal(signal_patterns):
    dic = {}

    # Decode the easy digits first (1, 4, 7, 8)
    for pattern in signal_patterns:
        if len(pattern) == 2: dic[1] = pattern
        elif len(pattern) == 3: dic[7] = pattern
        elif len(pattern) == 4: dic[4] = pattern
        elif len(pattern) == 7: dic[8] = pattern

    for pattern in signal_patterns:

        # Decode 6 digit patterns (6, 9, 0)
        if len(pattern) == 6:
            if len(pattern.difference(dic[7])) == 4: dic[6] = pattern
            elif len(pattern.difference(dic[4])) == 2: dic[9] = pattern
            else: dic[0] = pattern
        
        # Decode 5 digit patterns (2, 3, 5)
        elif len(pattern) == 5:
            if len(pattern.difference(dic[1])) == 3: dic[3] = pattern
            elif len(pattern.difference(dic[4])) == 2: dic[5] = pattern
            else: dic[2] = pattern

    # Build digits dictionary
    digits_dictionary = {}
    for num in range(10):
        digits_dictionary[''.join(sorted(dic[num]))] = num
    
    return digits_dictionary