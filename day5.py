from collections import deque

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    # Find the split point between rules and updates
    split_index = lines.index('')
    
    # The rules are in the first section
    rules = [line.split('|') for line in lines[:split_index]]
    
    # The updates are in the second section
    updates = [list(map(int, line.split(','))) for line in lines[split_index + 1:]]
    
    return rules, updates

def is_update_ordered(update, rules):
    # Create a map of the page numbers in the update
    page_set = set(update)
    
    # Check the rules for this update
    for rule in rules:
        page1, page2 = int(rule[0]), int(rule[1])
        
        # Skip rules that don't apply (if either page is not in the update)
        if page1 not in page_set or page2 not in page_set:
            continue
        
        # Check if page1 comes before page2
        if update.index(page1) > update.index(page2):
            return False
    
    return True

def find_middle_page(update):
    n = len(update)
    
    # Middle index for odd or even length
    middle_index = (n - 1) // 2  # This works for both odd and even-length lists
    
    return update[middle_index]

def process_updates(file_path):
    rules, updates = read_input_file(file_path)
    
    middle_sum = 0
    
    # Check each update
    for update in updates:
        if is_update_ordered(update, rules):
            middle_page = find_middle_page(update)
            middle_sum += middle_page
    
    return middle_sum

def correct_update_order(update, rules):
    # Create a deque to process the pages
    ordered_pages = deque(update)
    
    # Try to reorder the pages based on the rules
    # Continue applying rules until no more changes can be made
    changes_made = True
    while changes_made:
        changes_made = False
        for rule in rules:
            page1, page2 = int(rule[0]), int(rule[1])
            
            # If both pages are in the update and the order is incorrect, fix it
            if page1 in ordered_pages and page2 in ordered_pages:
                idx1 = ordered_pages.index(page1)
                idx2 = ordered_pages.index(page2)
                
                # If page1 comes after page2, swap them
                if idx1 > idx2:
                    ordered_pages[idx1], ordered_pages[idx2] = ordered_pages[idx2], ordered_pages[idx1]
                    changes_made = True
    return list(ordered_pages)

def process_and_correct_updates(file_path):
    rules, updates = read_input_file(file_path)
    
    middle_sum = 0
    
    # Check each update
    for update in updates:
        if not is_update_ordered(update, rules):
            # If the update is not ordered, correct it
            corrected_update = correct_update_order(update, rules)
            middle_page = find_middle_page(corrected_update)
            middle_sum += middle_page
    
    return middle_sum

# Part 1:
file_path = 'inputs/input5.txt'
result = process_updates(file_path)
print("Sum of middle page numbers for correctly ordered updates:", result)

# Part 2:
result = process_and_correct_updates(file_path)
print("Sum of middle page numbers for corrected updates:", result)
