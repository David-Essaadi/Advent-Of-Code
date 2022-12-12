import re
import numpy as np

def draw(grid, cycle, x):
    px = (cycle - 1) % 40
    row = (cycle - 1) // 40
    if px == x - 1 or px == x or px == x + 1:
        grid[row][px] = '#'
    else:
        grid[row][px] = '.'
    return grid

with open('input.txt') as file:
    instructions = file.read().strip().splitlines()
    cycle = 1
    x = 1
    grid = np.ndarray(shape=(6, 40), dtype='|U1')
    for instruction in instructions:
        match instruction[0:4]:
            case 'noop':
                draw(grid, cycle, x)
                cycle += 1
            case 'addx':
                v = int(re.search(r'-*\d+', instruction).group(0))
                for _ in range(2):
                    draw(grid, cycle, x)
                    cycle += 1
                x += v
    with open('output.txt', 'w') as output:
        for line in grid:
            for c in line:
                output.write(c)
            output.write('\n')
    
