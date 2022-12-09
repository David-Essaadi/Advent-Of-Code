import re

d = dict()

def sign(x):
    s = 1-(x<=0)
    if (s == 0):
        return -1
    return 1

def move_tail(head: tuple, tail: tuple):
    if head[0] == tail[0] and head[1] == tail[1]:
        return head, tail

    dir = (head[0] - tail[0], head[1] - tail[1])

    if abs(dir[0]) <= 1 and abs(dir[1]) <= 1:
        return head, tail

    if abs(dir[0]) == 2 and head[1] == tail[1]:
        tail = (tail[0] + dir[0] / 2, tail[1])

    elif abs(dir[1]) == 2 and head[0] == tail[0]:
        tail = (tail[0], tail[1] + dir[1]/2)

    if not (head[0] == tail[0]) and not (head[1] == tail[1]):
        tail = (tail[0] + sign(dir[0]), tail[1] + sign(dir[1]))

    d[tail] = 1
    return head, tail

with open('input.txt') as file:
    moves = file.read().strip().splitlines()
    head = (0,0)
    tail = (0,0)
    d[tail] = 1
    for move in moves:
        n = int(re.search(r'\d+', move).group(0))
        for i in range(n):
            match move[0]:
                case 'U':
                    head, tail = move_tail((head[0], head[1] - 1), tail)
                case 'L':
                    head, tail = move_tail((head[0] - 1, head[1]), tail)
                case 'D':
                    head, tail = move_tail((head[0], head[1] + 1), tail)
                case 'R':
                    head, tail = move_tail((head[0] + 1, head[1]), tail)
    print(len(d.keys()))

