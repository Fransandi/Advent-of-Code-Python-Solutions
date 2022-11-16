'''
=========================================
|| 🎄 Advent of Code 2021: Day 3 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
''' 

from collections import Counter
from statistics import mode

### Part One
def part_one(input):
    diagnostic_report = [line.strip() for line in input]
    digits_len = len(diagnostic_report[0])
    gamma_rate = epsilon_rate = ''

    for digit_index in range(digits_len):
        most_common_digit = mode([entry[digit_index] for entry in diagnostic_report])
        gamma_rate += most_common_digit
        epsilon_rate += '1' if most_common_digit == '0' else '0'

    return int(gamma_rate, 2)*int(epsilon_rate, 2)

### Part Two
def part_two(input):
    diagnostic_report = [line.strip() for line in input]
    
    # Calculate oxygen rating
    oxygen_rating = calculate_rating(diagnostic_report.copy(), 0)

    # Calculate co2 rating
    co2_rating = calculate_rating(diagnostic_report.copy(), 1)

    return int(oxygen_rating, 2)*int(co2_rating, 2)

def calculate_rating(report, primary_bit, digit_index=0):
    secondary_bit = 1 - primary_bit    
    while len(report) > 1:
        count = Counter([entry[digit_index] for entry in report])
        selected_digit = str(primary_bit) if count['0'] > count['1'] else str(secondary_bit)
        report = [entry for entry in report if entry[digit_index] == selected_digit]
        digit_index+=1
    
    return report[0]