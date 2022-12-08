import re

def cd(command):
    return re.search(r'(?<=cd ).*', command).group(0)

def dir_name(line):
    return re.search(r'(?<=dir ).*', line).group(0)

def file_size(line):
    return int(re.search(r'\d+', line).group(0))
   

def ls(file):
    contents = []
    pos = file.tell()
    line = file.readline()
    while line:
        if line[0] == '$':
            file.seek(pos)
            return contents
        if line.startswith('dir'):
            contents.append(dir_name(line))
        else:
            contents.append(file_size(line))
        pos = file.tell()
        line = file.readline()
    return contents

def find_size(structure, working_dir):
    sum = 0
    for v in structure[working_dir]:
        if isinstance(v, int):
            sum += v
        else:
            sum += find_size(structure, working_dir + (v,))
    return sum


with open ('input.txt') as file:
    structure = dict()
    working_dir = ['/']
    line = file.readline()
    while line:
        if line.startswith('$ cd'):
            new_dir = cd(line)
            if new_dir == '/':
                working_dir = ['/']
            elif new_dir == '..':
                working_dir.pop()
            else:
                working_dir.append(new_dir)
        elif line.startswith('$ ls'):
            contents = ls(file)
            structure[tuple(working_dir)] = contents
        line = file.readline()
    
    sizes = []
    for key in structure.keys():
        sizes.append(find_size(structure, key))
    
    needed_space = 30000000 - (70000000 - find_size(structure, ('/', )))
    print(sorted(filter(lambda size: size > needed_space, sizes))[0])