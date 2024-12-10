from itertools import product

def read_input(file_path):
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            test_value, numbers = line.strip().split(":")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def find_valid_equations_sum(file_path):
    equations = read_input(file_path)
    valid_test_values_sum = 0

    for test_value, numbers in equations:
        n = len(numbers) - 1  # Number of operator slots
        valid = False
        # Generate all possible combinations of operators (+, *)
        for operator_combo in product(['+', '*'], repeat=n):
            if evaluate_expression(numbers, operator_combo) == test_value:
                valid = True
                break  # Stop checking further if we find a valid solution
        
        if valid:
            valid_test_values_sum += test_value

    return valid_test_values_sum

def concatenate(a, b):
    return int(f"{a}{b}")

def evaluate_expression_with_concat(numbers, operator_combo):
    result = numbers[0]
    for i, op in enumerate(operator_combo):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = concatenate(result, numbers[i + 1])
    return result

def sum_of_valid_equations_with_concat(file_path):
    equations = read_input(file_path)
    valid_test_values_sum = 0

    for test_value, numbers in equations:
        n = len(numbers) - 1  # Number of operator slots
        valid = False
        # Generate all possible combinations of operators (+, *, ||)
        for operator_combo in product(['+', '*', '||'], repeat=n):
            if evaluate_expression_with_concat(numbers, operator_combo) == test_value:
                valid = True
                break  # Stop checking further if we find a valid solution
        
        if valid:
            valid_test_values_sum += test_value

    return valid_test_values_sum

# Part 1
file_path = "inputs/input7.txt"
result = find_valid_equations_sum(file_path)
print(f"Sum of valid test values: {result}")

# Part 2
result = sum_of_valid_equations_with_concat(file_path)
print(f"Sum of valid test values with concat: {result}")