import sys
import importlib
import fileinput
import os

YEAR = None
DAY = None
EXAMPLE_INPUT_DIR = None
INPUT_DIR = None
SOLUTIONS_MODULE = None
PART_ONE = None
PART_TWO = None

def valid_input(input_dir, print_enabled=True):
    input = fileinput.FileInput(input_dir)
    is_valid = len([line for line in input]) > 0
    if not is_valid and print_enabled:
        print("\n👉 Please add the input before running your solution\n")
    return is_valid

def valid_output(expected_output, print_enabled=True):
    is_valid = expected_output != None
    if not is_valid and print_enabled:
        print("\n👉 Please fill the example's expected output before running your solution\n")
    return is_valid

def test_example(solution, print_enabled=True):
    if print_enabled: print(f'> Testing Part {"1" if solution.__name__ == "part_one" else "2"}:')
    expected_output = importlib.import_module(f'{YEAR}.example.outputs').example_outputs[f'day{DAY}'][solution.__name__]
    if valid_input(EXAMPLE_INPUT_DIR, print_enabled) and valid_output(expected_output, print_enabled):
        input = fileinput.FileInput(EXAMPLE_INPUT_DIR)
        output = solution(input)
        passed = output == expected_output
        if print_enabled: 
            print(f'Example: Passed ✅ (result = {output})' if passed else f'Example: Failed ❌ (result = {output}, expected = {expected_output})')
        return passed

def test_solution(solution):
    if valid_input(INPUT_DIR):
        input = fileinput.FileInput(INPUT_DIR)
        output = solution(input)
        print(f'👉 Your solution: {output} ⭐️ \n')

def printProgressBar (progress, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (progress / float(total)))
    filledLength = int(length * progress // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\n\r{prefix} |{bar}| {percent}% {suffix}\n', end = printEnd)
    print()

if __name__ == "__main__":
    args = sys.argv[1]

    # Run specific test (YEAR/DAY)
    if '/' in args:
        YEAR, DAY = args.split('/')
        EXAMPLE_INPUT_DIR = f'{YEAR}/example/inputs/day{DAY}.txt'
        INPUT_DIR = f'{YEAR}/inputs/day{DAY}.txt'
        SOLUTIONS_MODULE = importlib.import_module(f'{YEAR}.solutions.day{DAY}')
        PART_ONE = getattr(SOLUTIONS_MODULE, 'part_one')
        PART_TWO = getattr(SOLUTIONS_MODULE, 'part_two')
        
        # Run Tests
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f'{"="*38}\n|| 🎄 Advent of Code {YEAR}: Day {DAY} 🗓 || \n{"="*38}\n')
        if test_example(PART_ONE):
            test_solution(PART_ONE)
            if test_example(PART_TWO):
                test_solution(PART_TWO)
    
    # Run all tests (YEAR)
    else:
        YEAR = args
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f'{"="*40}\n|| 🎄 Advent of Code {YEAR}: All days 🗓 || \n{"="*40}\n')
        passed_tests = 0
        for i in range(1,26):
            DAY = i
            EXAMPLE_INPUT_DIR = f'{YEAR}/example/inputs/day{DAY}.txt'
            INPUT_DIR = f'{YEAR}/inputs/day{DAY}.txt'
            SOLUTIONS_MODULE = importlib.import_module(f'{YEAR}.solutions.day{DAY}')
            PART_ONE, PART_TWO = getattr(SOLUTIONS_MODULE, 'part_one'), getattr(SOLUTIONS_MODULE, 'part_two')
            part_one_result, part_two_result = test_example(PART_ONE, False), test_example(PART_TWO, False)
            if part_one_result: passed_tests+=1
            if part_two_result: passed_tests+=1
            part_one_msg = f'Part 1: { "Passed ✅" if part_one_result else "Failed ❌"}'
            part_two_msg = f'Part 2: { "Passed ✅" if part_two_result else "Failed ❌"}'
            print(f'> Day {DAY} {"" if DAY > 9 else " "} 👉 {part_one_msg},  {part_two_msg}')

        printProgressBar(passed_tests, 50, prefix = 'Progress:', suffix = 'Complete', length = 25)
