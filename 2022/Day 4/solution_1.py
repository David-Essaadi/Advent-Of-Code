from itertools import starmap

def to_pair(input: list) -> list:
    return [tuple(map(int, pair.split('-'))) for pair in input.split(',')]

def is_contained(t1: tuple, t2: tuple) -> bool:
    return (t1[0] >= t2[0] and t1[1] <= t2[1]) or (t2[0] >= t1[0] and t2[1] <= t1[1])

with open('input.txt') as file:
    input = file.read().splitlines()
    output = sum(starmap(is_contained, map(to_pair, input)))
    print(output)