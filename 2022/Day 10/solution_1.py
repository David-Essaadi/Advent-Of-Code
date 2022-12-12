import re

def check_cycle(cycle, x):
    if cycle % 40 == 20:
        return cycle * x
    return 0

with open('input.txt') as file:
    instructions = file.read().strip().splitlines()
    cycle = 1
    x = 1
    signal_strength = 0
    for instruction in instructions:
        match instruction[0:4]:
            case 'noop':
                signal_strength += check_cycle(cycle, x)
                cycle += 1
            case 'addx':
                v = int(re.search(r'-*\d+', instruction).group(0))
                for _ in range(2):
                    signal_strength += check_cycle(cycle, x)
                    cycle += 1
                x += v
    print(signal_strength)
