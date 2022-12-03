import numpy as np
import string

def to_priority(items):
    return list(map(lambda item: string.ascii_letters.index(item) + 1, items))

with open('input.txt') as file:
    print(sum(map(lambda items: np.intersect1d(items[:len(items) // 2], items[len(items) // 2:])[0], map(to_priority, file.read().strip().splitlines()))))