def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def get_trailheads(height_map):
    trailheads = []
    rows, cols = len(height_map), len(height_map[0])
    for row in range(rows):
        for col in range(cols):
            if height_map[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def is_valid_move(height_map, row, col, current_height):
    rows, cols = len(height_map), len(height_map[0])
    return (
        0 <= row < rows and
        0 <= col < cols and
        height_map[row][col] == current_height + 1
    )

def find_trail_score(height_map, start):
    stack = [start]
    visited = set()
    reachable_nines = set()

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))

        current_height = height_map[row][col]
        if current_height == 9:
            reachable_nines.add((row, col))

        # Explore valid neighbors (up, right, down, left)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_row, next_col = row + dr, col + dc
            if is_valid_move(height_map, next_row, next_col, current_height):
                stack.append((next_row, next_col))

    return len(reachable_nines)

def calculate_trailhead_scores(file_path):
    height_map = read_map(file_path)
    trailheads = get_trailheads(height_map)
    sum = 0

    for trailhead in trailheads:
        score = find_trail_score(height_map, trailhead)
        sum += score

    return sum

def find_trails(height_map, start, path, trails):
    row, col = start
    current_height = height_map[row][col]

    # If we reached height 9, record the trail
    if current_height == 9:
        trails.add(tuple(path))
        return

    # Explore valid neighbors (up, right, down, left)
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        next_row, next_col = row + dr, col + dc
        if is_valid_move(height_map, next_row, next_col, current_height):
            find_trails(height_map, (next_row, next_col), path + [(next_row, next_col)], trails)

def calculate_trailhead_ratings(file_path):
    height_map = read_map(file_path)
    trailheads = get_trailheads(height_map)
    sum = 0

    for trailhead in trailheads:
        trails = set() 
        find_trails(height_map, trailhead, [trailhead], trails)
        sum += len(trails)

    return sum

# Part 1: 
file_path = 'inputs/input10.txt'
sum = calculate_trailhead_scores(file_path)
print(f"Total scores sum: {sum}")

#Part 2:
sum = calculate_trailhead_ratings(file_path)
print(f"Total ratings sum: {sum}")
