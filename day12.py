def read_garden_plots(file_path):
    regions = {}
    visited = set()
    grid = []

    # Read the file and create a grid of garden plots
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        grid = [list(line) for line in lines]

    def dfs(row, col, label):
        """DFS (Depth-First Search) to explore the connected plots with the same label"""
        stack = [(row, col)]  # Start from the given cell
        region = []
        while stack:
            row, col = stack.pop()  # Get the next cell to explore
            if (row, col) not in visited and grid[row][col] == label:  # Check if not visited and has matching label
                visited.add((row, col))
                region.append((row, col))
                
                # Explore neighboring cells (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_col = row + dr, col + dc  # Calculate the neighbor's position
                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):  # Check if within grid bounds
                        if (next_row, next_col) not in visited and grid[next_row][next_col] == label:
                            stack.append((next_row, next_col))  # Add neighbor to stack for exploration
        return region

    # Loop through the entire grid to find all regions with the same label
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            label = grid[row][col]  
            if (row, col) not in visited:  
                region = dfs(row, col, label)  
                if label not in regions:
                    regions[label] = []  
                regions[label].append(region)  

    return regions, grid


def calculate_area(region):
    return len(region)


def calculate_perimeter(region, grid):
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row, col in region:
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or grid[nr][nc] != grid[row][col]:
                perimeter += 1
    return perimeter


def calculate_sides(region):
    """Calculates the number of sides for a region."""
    min_x = min(region, key=lambda x: x[0])[0]
    max_x = max(region, key=lambda x: x[0])[0]
    min_y = min(region, key=lambda x: x[1])[1]
    max_y = max(region, key=lambda x: x[1])[1]
    
    rows = max_x - min_x + 1
    cols = max_y - min_y + 1

    new_region = [(x - min_x, y - min_y) for x, y in region]

    grid = [[" " for _ in range(cols + 2)] for _ in range(rows + 2)]

    for x, y in new_region:
        grid[x + 1][y + 1] = "X"

    sides = 0
    for _ in range(2):
        for x in range(1, rows + 1):
            sides += len("".join(["X" if current != above and current == "X" else " " for current, above in zip(grid[x], grid[x - 1])]).split())
            sides += len("".join(["X" if current != above and current == "X" else " " for current, above in zip(grid[x], grid[x + 1])]).split())

        grid = list(zip(*grid[::-1]))
        rows, cols = cols, rows

    return sides


def calculate_fencing_cost(regions, grid):
    cost = 0
    for label, region_list in regions.items():
        for region in region_list:
            area = calculate_area(region)
            perimeter = calculate_perimeter(region, grid)
            cost += area * perimeter
    return cost


def calculate_fencing_cost_with_sides(regions, grid):
    cost = 0
    for label, region_list in regions.items():
        for region in region_list:
            area = calculate_area(region)
            sides = calculate_sides(region)
            cost += area * sides
    return cost


# Part 1: 
regions, grid = read_garden_plots("inputs/input12.txt")
cost = calculate_fencing_cost(regions, grid)
print(f"Total fencing cost: {cost}")

# Part 2: 
fencing_cost = calculate_fencing_cost_with_sides(regions, grid)
print(f"Total fencing cost (using sides): {fencing_cost}")
