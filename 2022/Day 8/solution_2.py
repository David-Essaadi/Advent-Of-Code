def max_scenic_score(grid):
    high = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            sum = 1
            size = grid[y][x]
            sum *= scenic_left(grid, x - 1, y, size)
            sum *= scenic_right(grid, x + 1, y, size)
            sum *= scenic_up(grid, x, y - 1, size)
            sum *= scenic_down(grid, x, y + 1, size)
            if sum > high:
                high = sum
    return high

def scenic_left(grid, x, y, size):
    if x < 0:
        return 0
    if grid[y][x] >= size:
        return 1
    return scenic_left(grid, x-1, y, size) + 1
        
def scenic_right(grid, x, y, size):
    if x >= len(grid[y]):
        return 0
    if grid[y][x] >= size:
        return 1
    return scenic_right(grid, x+1, y, size) + 1

def scenic_up(grid, x, y, size):
    if y < 0:
        return 0
    if grid[y][x] >= size:
        return 1
    return scenic_up(grid, x, y-1, size) + 1

def scenic_down(grid, x, y, size):
    if y >= len(grid):
        return 0
    if grid[y][x] >= size:
        return 1
    return scenic_down(grid, x, y+1, size) + 1

with open('input.txt') as file:
    grid = file.read().strip().splitlines()
    grid = list(map(lambda l: [int(x) for x in l], grid))
    print(max_scenic_score(grid))