from collections import deque

# number of distinct characters in a row to find
n = 14

def solution():
    with open('input.txt') as file:
        input = file.read().strip()
        q = deque()
        for c in input[:n-1]:
            q.appendleft(c)
        for i,c in enumerate(input[n-1:]):
            if not c in q and len(set(q)) == n-1:
               return i + n
            else:
                q.appendleft(c)
                q.pop()

print(solution())