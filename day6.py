import time

def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def find_guard_start_position(map_grid):
    for i, row in enumerate(map_grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j  # Return the position of the guard
    return None

def move_guard(map_grid, start_row, start_col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left (clockwise)
    direction = 0  # Start by facing up (0 = up)
    row, col = start_row, start_col
    
    # Mark the starting position as visited
    map_grid[row][col] = 'X'

    while True:
        # Try to move forward
        next_row, next_col = row + directions[direction][0], col + directions[direction][1]
        
        # Check if the next position is within bounds
        if 0 <= next_row < len(map_grid) and 0 <= next_col < len(map_grid[0]):
            # Check if there's an obstruction in front
            if map_grid[next_row][next_col] == '#':
                # Turn right 90 degrees (clockwise)
                direction = (direction + 1) % 4
            else:
                row, col = next_row, next_col
                map_grid[row][col] = 'X'
        else:
            # Exit if the guard tries to move out of bounds
            break

    # Count the number of 'X's in the grid
    return sum(row.count('X') for row in map_grid)

def guard_patrol(file_path):
    map_grid = read_map(file_path)
    start_row, start_col = find_guard_start_position(map_grid)
    
    if start_row is None:
        return 0  # If no guard found, return 0
    
    # Simulate the patrol and count the number of visited positions (X)
    return move_guard(map_grid, start_row, start_col)

def check_for_possible_loop(map_grid, start_row, start_col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left (clockwise)
    direction = 0  # Start by facing up (0 = up)
    row, col = start_row, start_col
    
    # Mark the starting position as visited
    map_grid[row][col] = 'X'
    
    # Set to track visited states (position + direction)
    visited_states = set()
    visited_states.add((row, col, direction))

    while True:
        # Try to move forward
        next_row, next_col = row + directions[direction][0], col + directions[direction][1]
        
        # Check if the guard is out of bounds
        if not (0 <= next_row < len(map_grid) and 0 <= next_col < len(map_grid[0])):
            return False  # Out of bounds, no loop
        
        # Check if there's an obstruction in front
        if map_grid[next_row][next_col] == '#' or map_grid[next_row][next_col] == 'O':
            # Turn right 90 degrees (clockwise)
            direction = (direction + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
            # Check if this state has been visited before
            current_state = (row, col, direction)
            if current_state in visited_states:
                return True  # Loop detected
            visited_states.add(current_state)

            # Mark the position as visited
            map_grid[row][col] = 'X'

def find_possible_obstruction_positions(file_path):
    # Read the map from the input file
    grid = read_map(file_path)
    
    # Starting position of the guard
    start_row, start_col = find_guard_start_position(grid)
    
    # Count the positions where a new obstruction will make the guard get stuck
    count = 0
    # Iterate over all positions on the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Skip the guard's starting position and existing obstructions
            if (row, col) == (start_row, start_col) or grid[row][col] == '#':
                continue

            # Temporarily place an obstruction 'O' at the current position
            original_value = grid[row][col]
            grid[row][col] = 'O'

            # Simulate the guard's movement
            if check_for_possible_loop([list(row) for row in grid], start_row, start_col):
                count += 1

            # Restore the original value
            grid[row][col] = original_value

    return count

# Part 1:
file_path = 'inputs/input6.txt'
result = guard_patrol(file_path)
print("Count of X's:", result)

# Part 2:
start_time = time.time()
result = find_possible_obstruction_positions(file_path)
print("Number of positions that could cause a loop:", result)
end_time = time.time()
print(f"Investigation took {round(end_time-start_time, 4)} seconds")