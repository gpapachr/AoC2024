def read_input_file(file_path):
    with open(file_path, 'r') as file:
        grid = file.read().splitlines()  # Split into lines, each representing a row
    return grid

def find_word_in_direction(grid, word, di, dj):
    """Find all occurrences of a word in the grid, moving in direction (di, dj)."""
    occurrences = []
    n = len(grid)
    m = len(grid[0])
    word_len = len(word)
    
    for i in range(n):
        for j in range(m):
            # Check if the word can fit in the grid in the given direction
            if 0 <= i + di * (word_len - 1) < n and 0 <= j + dj * (word_len - 1) < m:
                # Check if all characters match the word
                match = True
                for k in range(word_len):
                    ni, nj = i + di * k, j + dj * k
                    if grid[ni][nj] != word[k]:
                        match = False
                        break
                if match:
                    occurrences.append((i, j))
    return occurrences

def count_xmas_occurrences(grid):
    word = "XMAS"
    word_reverse = "SAMX"
    
    n = len(grid)  # Number of rows
    m = len(grid[0])  # Number of columns
    
    count = 0

    xmas_occurrences = []
    
    # Horizontal (left to right)
    xmas_occurrences.extend(find_word_in_direction(grid, word, 0, 1))
    # Vertical (top to bottom)
    xmas_occurrences.extend(find_word_in_direction(grid, word, 1, 0))
    # Diagonal top-left to bottom-right
    xmas_occurrences.extend(find_word_in_direction(grid, word, 1, 1))
    # Diagonal bottom-left to top-right
    xmas_occurrences.extend(find_word_in_direction(grid, word, -1, 1))
    
    samx_occurrences = []
    
    # Horizontal (left to right)
    samx_occurrences.extend(find_word_in_direction(grid, word_reverse, 0, 1))
    # Vertical (top to bottom)
    samx_occurrences.extend(find_word_in_direction(grid, word_reverse, 1, 0))
    # Diagonal top-left to bottom-right
    samx_occurrences.extend(find_word_in_direction(grid, word_reverse, 1, 1))
    # Diagonal bottom-left to top-right
    samx_occurrences.extend(find_word_in_direction(grid, word_reverse, -1, 1))
    
    count = len(xmas_occurrences) + len(samx_occurrences)
    
    return count

def count_x_shaped_mas(grid):
    rows = len(grid)  # Number of rows
    cols = len(grid[0])  # Number of columns
    count = 0
    
    # Loop through the grid to find 'A' as the center of the 'X' pattern
    for i in range(1, rows - 1):  # Avoid out-of-bounds on top and bottom
        for j in range(1, cols - 1):  # Avoid out-of-bounds on left and right
            if grid[i][j] == 'A':
                # Check for possible 'X' patterns
                # Top-left, Top-right, Bottom-left, Bottom-right positions
                top_left = grid[i-1][j-1]
                top_right = grid[i-1][j+1]
                bottom_left = grid[i+1][j-1]
                bottom_right = grid[i+1][j+1]
                
                # Check the 'X' pattern for MAS
                if ((top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M')) and \
                   ((top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M')):
                    count += 1
    
    return count

# Part 1:
file_path = 'inputs/input4.txt'
grid = read_input_file(file_path)
result = count_xmas_occurrences(grid)
print("Total occurrences:", result)

# Part 2:
file_path = 'inputs/input4.txt'
grid = read_input_file(file_path)
result = count_x_shaped_mas(grid)
print("Total 'MAS' X patterns:", result)
