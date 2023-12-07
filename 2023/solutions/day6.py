'''
=========================================
|| 🎄 Advent of Code 2023: Day 6 🗓
|| Link: https://adventofcode.com/2023
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

import math


# Part One
def part_one(input):
    races = [line.split(':')[1] for line in input]
    time = [int(ms) for ms in races[0].split()]
    distance = [int(ms) for ms in races[1].split()]
    return calculate_total_score(time, distance)


# Part Two
def part_two(input):
    race = [line.split(':')[1] for line in input]
    time = [int(race[0].replace(' ', ''))]
    distance = [int(race[1].replace(' ', ''))]
    return calculate_total_score(time, distance)


# Binary search
def get_starting_position(record, time, start):
    if get_score(start, time) > record:
        return start

    left_pointer = start // 2
    right_pointer = start + (time - start) // 2

    if start != left_pointer:
        left = get_starting_position(record, time, left_pointer)
        if left:
            return left

    if start != right_pointer:
        right = get_starting_position(record, time, right_pointer)
        if right:
            return right


def get_score(button, time):
    return ((time - button) * button)


def calculate_total_score(time, distance):
    total_score = 1
    for i in range(len(time)):
        score = 0
        start = get_starting_position(
            distance[i], time[i], math.trunc(math.sqrt(time[i])))

        left = start
        while get_score(left, time[i]) > distance[i]:
            left -= 1
            score += 1

        right = start + 1
        while get_score(right, time[i]) > distance[i]:
            right += 1
            score += 1

        total_score *= score

    return total_score
