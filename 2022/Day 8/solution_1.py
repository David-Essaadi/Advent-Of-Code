import numpy as np

def mark_visible(grid, m, n):
    arr = np.zeros(grid.shape)
    for y in range(0, n):
        high = -1
        for x in range(0, m):
            if (grid[y][x] > high):
                arr[y][x] = 1
                high = grid[y][x]
    return arr

with open('input.txt') as file:
    grid = file.read().strip().splitlines()
    m = len(grid[0])
    n = len(grid)
    grid = np.array(list(map(lambda l: [int(x) for x in l], grid)))
    left = mark_visible(grid, m, n)
    grid = np.rot90(grid)
    top = mark_visible(grid, m, n)
    grid = np.rot90(grid)
    right = mark_visible(grid, m, n) 
    grid = np.rot90(grid)
    bottom = mark_visible(grid, m, n)
    top = np.rot90(np.rot90(np.rot90(top)))
    right = np.rot90(np.rot90(right))
    bottom = np.rot90(bottom)
    sum = 0
    for y in range(0, n):
        for x in range(0, m):
            if top[y][x] == 1 or right[y][x] == 1 or bottom[y][x] == 1 or left[y][x] == 1:
                sum += 1
    print(sum)