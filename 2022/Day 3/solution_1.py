import numpy as np
import string

def priority(item):
    return string.ascii_letters.index(item) + 1

with open('input.txt') as file:
    print(sum(map(lambda items: np.intersect1d(list(map(priority, items[:len(items) // 2])), list(map(priority, items[len(items) // 2:])))[0], file.read().strip().splitlines())))