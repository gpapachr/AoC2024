def parse_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def calculate_antinodes(file_path):
    grid = parse_grid(file_path)
    rows, cols = len(grid), len(grid[0])

    # Use a dictionary to store coordinates for each antenna type
    antennas = {}

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != ".":
                # Add coordinates to the corresponding antenna frequency list
                if grid[row][col] not in antennas:
                    antennas[grid[row][col]] = []
                antennas[grid[row][col]].append((row, col))

    antinodes = set()

    # Process each type of antenna
    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                # Calculate antinode positions
                for id, dir in [(i, -1), (j, 1)]:
                    pos = tuple([a + b * dir for a, b in zip(coords[id], diff)])
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        antinodes.add(pos)
    
    return len(antinodes)

def calculate_antinodes_with_harmonics(file_path):
    grid = parse_grid(file_path)
    rows, cols = len(grid), len(grid[0])

    # Use a dictionary to store coordinates for each antenna type
    antennas = {}

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != ".":
                # Add coordinates to the corresponding antenna frequency list
                if grid[row][col] not in antennas:
                    antennas[grid[row][col]] = []
                antennas[grid[row][col]].append((row, col))

    antinodes = set()

    # Process each type of antenna
    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                # Calculate antinode positions
                for id, dir in [(i, -1), (j, 1)]:
                    pos = coords[id]
                    while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)
                            pos = tuple([a + b * dir for a, b in zip(pos, diff)])    
    return len(antinodes)

# Part 1 :
file_path = 'inputs/input8.txt'  # Path to the grid input file
result = calculate_antinodes(file_path)
print(f"The total number of unique antinodes is: {result}")

# Part 2:
result = calculate_antinodes_with_harmonics(file_path)
print(f"The total number of unique antinodes with armonics is: {result}")
