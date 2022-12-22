import re

def build_tree():
    tree = dict()
    with open('input.txt') as f:
        for line in f:
            l = line.strip().split(':')
            name = l[0]
            names = re.findall(r'[a-z,A-Z]{4}', l[1])
            if names:
                op = re.findall(r'[\*,\-,\/,\+]', l[1])[0]
                tree[name] = (names[0], names[1], op)
            else:
                tree[name] = int(re.findall(r'\d+', l[1])[0])
    return tree

def calc(tree, monkey):
    if type(tree[monkey]) == int:
        return tree[monkey]
    return eval(str(calc(tree, tree[monkey][0])) + tree[monkey][2] + str(calc(tree, tree[monkey][1])))

tree = build_tree()
res = calc(tree, 'root')
print(res)
