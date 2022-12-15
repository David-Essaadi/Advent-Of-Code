import re

def read_input(path) -> list:
    with open(path) as file:
        return file.read().strip().splitlines()

def distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

row = 2000000

lines = read_input('input.txt')
total = 0
visited = dict()
beacons = set()

for line in lines:
    sensor_x, beacon_x = list(map(int, re.findall(r'(?<=x=)-*\d+', line)))
    sensor_y, beacon_y = list(map(int, re.findall(r'(?<=y=)-*\d+', line)))
    sensor = (sensor_x, sensor_y)
    beacon = (beacon_x, beacon_y)
    dist = distance(sensor, beacon)
    beacons.add(beacon)

    start_x = sensor_x - dist
    end_x = sensor_x + dist
    for x in range(start_x, end_x):
        if not visited.get((x, row)) and distance((x, row), sensor) <= dist:
            visited[(x, row)] = 1
            total += 1

for beacon in beacons:
    if visited.get(beacon):
        total -= 1
print(total)