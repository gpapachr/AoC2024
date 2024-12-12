import time

def read_stones(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))
    
def simple_blink(stones):
    """Simulates one blink of the stones, applying the transformation rules."""
    new_stones = []
    cache = {}
    
    for stone in stones:
        if stone in cache:
            # If the stone's transformation is cached, add its result directly
            new_stones.extend(cache[stone])
            continue
        
        # Rule processing
        if stone == 0:
            # Rule 1: Replace stone with 1
            transformation = [1]
        elif len(str(stone)) % 2 == 0:
            # Rule 2: Split into two stones
            digits = str(stone)
            mid = len(digits) // 2
            left, right = int(digits[:mid]), int(digits[mid:])
            transformation = [left, right]
        else:
            # Rule 3: Multiply by 2024
            transformation = [stone *2024]
        
        cache[stone] = transformation
        new_stones.extend(transformation)
    return new_stones

def process_blink(stone, times, cache):
    """Simulates #times blink of a specific stone, applying the transformation rules."""
    if times == 0:
        return 1

    if (stone, times) in cache:
        # If the stone's transformation is cached, return its result directly
        return cache[(stone, times)]
    
    # Rule processing
    if stone == 0:
        # Rule 1: Replace stone with 1
        count = process_blink(1, times - 1, cache)
    elif len(str(stone)) % 2 == 0:
        # Rule 2: Split into two stones
        digits = str(stone)
        mid = len(digits) // 2
        left, right = int(digits[:mid]), int(digits[mid:])
        count = process_blink(left, times - 1, cache) + process_blink(right, times - 1, cache)
    else:
        # Rule 3: Multiply by 2024
        count = process_blink(stone * 2024, times - 1, cache)
    
    cache[(stone, times)] = count
    return count

def brute(file_path, times):
    stones = read_stones(file_path)
    for i in range(0, times):
        stones = simple_blink(stones)
    return stones, len(stones)

def cached(file_path, times):
    stones = read_stones(file_path)
    cache = {}
    sum = 0
    for stone in stones:
        sum += process_blink(stone, times, cache)
    return sum

# Part 1 brute:
started = time.time()
stones, sum = brute('inputs/input11.txt', 25)
print(f"Number of stones after 25 blinks: {sum}")
print(f"Took {round(time.time() - started, 4)} seconds...")

# Part 1 cached:
started = time.time()
sum = cached('inputs/input11.txt', 25)
print(f"Number of stones after 25 blinks: {sum}")
print(f"Took {round(time.time() - started, 4)} seconds...")

# Part 2:
started = time.time()
sum = cached('inputs/input11.txt', 75)
print(f"Number of stones after 75 blinks: {sum}")
