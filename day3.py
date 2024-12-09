import re

def extract_mul_matches(input_string):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    return re.findall(pattern, input_string)

def calculate_sum_from_matches(matches):
    total_sum = 0
    for match in matches:
        i, j = int(match[0]), int(match[1])
        total_sum += i * j
    return total_sum

def readFile(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
    return input_string

def extract_and_multiply_from_file(file_path):
    input_string = readFile(file_path)

    matches = extract_mul_matches(input_string)
    return calculate_sum_from_matches(matches)

def extract_and_multiply_with_control(file_path):
    input_string = readFile(file_path)

    total_sum = 0
    mul_enabled = True

    # Regular expression to match do() and don't() instructions
    control_pattern = r'do\(\)|don\'t\(\)'

    # Split the input string into parts for processing both mul and control instructions
    parts = re.split(f'({control_pattern})', input_string)

    for part in parts:
        if part == 'do()':
            mul_enabled = True
        elif part == "don't()":
            mul_enabled = False
        else:
            matches = extract_mul_matches(part)
            total_sum += calculate_sum_from_matches(matches) if mul_enabled else 0

    return total_sum

# Part 1:
file_path = 'inputs/input3.txt'
result = extract_and_multiply_from_file(file_path)
print("Sum of multiplications:", result)

# Part 2:
result_with_control = extract_and_multiply_with_control(file_path)
print("Sum of multiplications with control:", result_with_control)
