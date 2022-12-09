import re

d = dict()

def sign(x):
    s = 1-(x<=0)
    if (s == 0):
        return -1
    return 1

def move_rope(head: tuple, t: tuple) -> tuple:
    if not t:
        d[head] = 1
        return head, t
    tail = t[0]

    if head[0] == tail[0] and head[1] == tail[1]:
        return head, move_rope(t[0], t[1])

    dir = (head[0] - tail[0], head[1] - tail[1])
    
    if abs(dir[0]) <= 1 and abs(dir[1]) <= 1:
        return head, move_rope(tail, t[1])

    if abs(dir[0]) == 2 and head[1] == tail[1]:
        tail = (tail[0] + dir[0] / 2, tail[1])

    elif abs(dir[1]) == 2 and head[0] == tail[0]:
        tail = (tail[0], tail[1] + dir[1]/2)

    if not (head[0] == tail[0]) and not (head[1] == tail[1]):
        tail = (tail[0] + sign(dir[0]), tail[1] + sign(dir[1]))

    return head, move_rope(tail, t[1])
    

with open('input.txt') as file:
    moves = file.read().strip().splitlines()
    rope = ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ((0, 0), ()))))))))))
    for move in moves:
        n = int(re.search(r'\d+', move).group(0))
        for i in range(n):
            print(rope)
            head = rope[0]
            match move[0]:
                case 'U':
                    rope = move_rope((head[0], head[1] - 1), rope[1])
                case 'L':
                    rope = move_rope((head[0] - 1, head[1]), rope[1])
                case 'D':
                    rope = move_rope((head[0], head[1] + 1), rope[1])
                case 'R':
                    rope = move_rope((head[0] + 1, head[1]), rope[1])
    print(len(d.keys()))

