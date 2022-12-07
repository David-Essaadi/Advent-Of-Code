from collections import defaultdict
from collections import deque
import re

def index_to_pile(index):
    return int((index - 1) / 4 + 1)

def get_piles(file):
    piles = defaultdict(deque)
    for line in file:
        indexes = [i + 1 for i, c in enumerate(line) if c == '[']
        if not indexes:
            break
        characters = [line[i] for i in indexes]
        for i, c in zip(map(index_to_pile, indexes), characters):
            piles[i].append(c)
    return piles

def perform_moves(moves, piles):
    for move in moves:
        m = list(map(int, re.findall(r'\d+', move)))
        n, fr, to = m
        for _ in range(n):
            piles[to].appendleft(piles[fr].popleft())
    return piles


with open('input.txt') as file:
    piles = get_piles(file)
    moves = file.read().strip().splitlines()
    piles = perform_moves(moves, piles)
    print("".join([piles[key].popleft() for key in sorted(piles.keys())]))
    