'''
=========================================
|| 🎄 Advent of Code 2022: Day 25 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

SNAFU_DICTIONARY = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
SNAFU_VALUES = ['2', '1', '0', '-', '=']

### Part One
def part_one(input):
    decimal_total = sum(snafu_to_decimal(snafu) for snafu in input)
    return decimal_to_snafu(decimal_total)

### Part Two
def part_two(input):
    return True


def snafu_to_decimal(snafu):
    decimal, multiplier = 0, 1
    for digit in snafu.strip()[::-1]:
        decimal += SNAFU_DICTIONARY[digit]*multiplier
        multiplier*=5
    return decimal

def decimal_to_snafu(decimal):
    digits = 1
    while pow(5, digits) * 2 < decimal: digits+=1
    digits += 1
    
    snafu = ''
    value = snafu_to_decimal('2'*digits)
    for digit in range(digits):
        digit_value = pow(5, digits-digit-1)
        times = (value - decimal) // digit_value
        value -= times*digit_value
        snafu += SNAFU_VALUES[times]
    return snafu
