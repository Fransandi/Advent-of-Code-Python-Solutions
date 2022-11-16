'''
=========================================
|| 🎄 Advent of Code 2021: Day 19 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from typing import DefaultDict
from itertools import permutations

SCANNER = 'scanner'
MIN_OVERLAP = 12
TINY_NUMBER = float('-inf')

### Part One
def part_one(input):
    scanners_report = parse_input(input)
    scanners_report_overlapped = overlap_all_reports(scanners_report)

    return len([value for value in scanners_report_overlapped.values() if value == True])

### Part Two
def part_two(input):
    scanners_report = parse_input(input)
    scanners_report_overlapped = overlap_all_reports(scanners_report)

    return calculate_longest_distance(scanners_report_overlapped)


def parse_input(input):
    scanners_report = report = []
    for line in [line.strip() for line in input if line.strip()]:
        if SCANNER in line:
            if report: scanners_report.append(report)
            report = []
        else:
            report.append(tuple([int(num) for num in line.split(',')]))
    
    return scanners_report + [report]

def overlap_all_reports(scanners_report):
    overlapped_reports = parse_report(scanners_report[0])
    visited = {0}
    # Iterate until we visit all reports
    while len(visited) != len(scanners_report):
        for i in range(1,len(scanners_report)):
            report = scanners_report[i]
            temp_report = overlap(overlapped_reports, report)
            
            # If an overlap is found, add it to visited
            if temp_report:
                overlapped_reports = temp_report
                visited.add(i)

    return overlapped_reports

def parse_report(scanners_report):
    report = DefaultDict(int)
    report[(0,0,0)] = False
    for scanner_report in scanners_report: 
        report[(scanner_report[0], scanner_report[1], scanner_report[2])] = True
    return report

def overlap(overlapped_reports, reports):
    for location in get_possible_locations(reports):
        parsed_report = parse_report(location)
        overlap = check_if_overlapping(overlapped_reports, parsed_report)
        
        if overlap: return overlap

def get_possible_locations(reports):
    possible_locations = []
    x_report = [report[0] for report in reports]
    y_report = [report[1] for report in reports]
    z_report = [report[2] for report in reports]

    # Look for all possible directions in all dimensions (24 possibilities)
    for x, y, z in list(permutations([x_report, y_report, z_report])):
        for temp_x in [x, get_opposite_array(x)]:
            for temp_y in [y, get_opposite_array(y)]:
                for temp_z in [z, get_opposite_array(z)]:
                    possible_locations.append([(x, y, z) for x, y, z in zip(temp_x, temp_y, temp_z)])   
    
    return possible_locations

def get_opposite_array(nums): return [(num * -1) for num in nums]

def check_if_overlapping(report_1, report_2):
    for x1, y1, z1 in report_1.keys():
        for x2, y2, z2 in report_2.keys():
            diff_x = x2 - x1
            diff_y = y2 - y1
            diff_z = z2 - z1
            
            # Explore overlap candidates
            temp_report = report_1.copy()
            for x2, y2, z2 in report_2.keys():
                temp_report[(x2 - diff_x, y2 - diff_y, z2-diff_z)] = report_2[(x2, y2, z2)]
            
            # Check if overlap was found
            if len(report_1) + len(report_2) - MIN_OVERLAP >= len(temp_report): return temp_report
    
    return False

def calculate_longest_distance(scanners_report):
    scanner_positions = [pos for pos, status in scanners_report.items() if status == False]
    largest_distance = TINY_NUMBER
    for position_a in scanner_positions:
        for position_b in scanner_positions:
            manhattan_distance = calculate_manhattan_distance(position_a, position_b)
            largest_distance = max(largest_distance, manhattan_distance)
    
    return largest_distance

def calculate_manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1]) + abs(pos_a[2] - pos_b[2])