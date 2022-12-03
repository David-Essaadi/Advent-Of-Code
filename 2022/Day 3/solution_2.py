import numpy as np
import string

def to_priority(items):
    return list(map(lambda item: string.ascii_letters.index(item) + 1, items))

with open('input.txt') as file:
    print(sum(map(lambda items: np.intersect1d(items[0], np.intersect1d(items[1], items[2]))[0], list(zip(*(iter(map(to_priority, file.read().strip().splitlines())),) * 3)))))
    