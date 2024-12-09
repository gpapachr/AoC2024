from collections import Counter


def read_columns_to_lists(file_path):
    column1 = []
    column2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two parts based on whitespace
            parts = line.split()
            if len(parts) == 2:  # Ensure the line has exactly two columns
                column1.append(int(parts[0]))
                column2.append(int(parts[1]))
    
    return column1, column2

def sort_lists(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    return sorted_list1, sorted_list2

def sum_absolute_differences(sorted_list1, sorted_list2):
    if len(sorted_list1) != len(sorted_list2):
        raise ValueError("The two lists must have the same size.")
    
    total_difference = sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))
    return total_difference

def similarity_sum(column1, column2):
    # Count the occurrences of each element in the second column
    column2_counts = Counter(column2)
    
    # Calculate the similarity sum
    similarity_sum = sum(value * column2_counts[value] for value in column1)
    return similarity_sum

# Part 1
try:
    column1, column2 = read_columns_to_lists('inputs/input1.txt')
    sorted_list1, sorted_list2 = sort_lists(column1, column2)
    difference_sum = sum_absolute_differences(sorted_list1, sorted_list2)
    print("Sum of Absolute Differences:", difference_sum)
except ValueError as e:
    print(e)

# Part 2
# Example usage:
result = similarity_sum(column1, column2)
print("Weighted Sum:", result)