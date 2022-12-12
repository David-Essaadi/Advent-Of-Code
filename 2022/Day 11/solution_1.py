import re
from collections import deque

class Monkey:
    def __init__(self, id, items, op, test, true, false) -> None:
        self.id = id
        self.items = items
        self.operation = op
        self.test = test
        self.true = true
        self.false = false

def parse_int(line: str):
    return int(re.search(r'\d+', line).group(0))

def parse_ints(line: str):
    return ([int(x) for x in re.findall(r'\d+', line)])

def parse_monkeys() -> list:
    with open('input.txt') as file:
        lines = file.read().strip().splitlines()
        i = 0
        monkeys = []
        while i < len(lines):
            id = parse_int(lines[i])
            starting_items = deque(parse_ints(lines[i + 1]))
            operation = re.search(r'(?<=Operation: ).*', lines[i + 2]).group(0)
            test = parse_int(lines[i + 3])
            true = parse_int(lines[i + 4])
            false = parse_int(lines[i + 5])
            i += 7
            monkeys.append(Monkey(id, starting_items, operation, test, true, false))
        return monkeys

def simulate(monkeys):
    print(monkeys[0].items)

monkeys = parse_monkeys()
simulate(monkeys)
