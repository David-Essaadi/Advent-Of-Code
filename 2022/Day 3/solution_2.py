import numpy as np
import string

def priority(item):
    return string.ascii_letters.index(item) + 1

with open('input.txt') as file:
    print(sum(map(lambda items: np.intersect1d(list(map(priority, items[0])), np.intersect1d(list(map(priority, items[1])), list(map(priority, items[2]))))[0], list(zip(*(iter(file.read().strip().splitlines()),) * 3)))))
    