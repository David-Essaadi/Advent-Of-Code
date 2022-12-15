import re

def read_input(path) -> list:
    with open(path) as file:
        return file.read().strip().splitlines()

def distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def simulate():
    size = 4000000
    lines = read_input('input.txt')
    sensors = []

    for line in lines:
        sensor_x, beacon_x = list(map(int, re.findall(r'(?<=x=)-*\d+', line)))
        sensor_y, beacon_y = list(map(int, re.findall(r'(?<=y=)-*\d+', line)))
        sensor = (sensor_x, sensor_y)
        beacon = (beacon_x, beacon_y)
        dist = distance(sensor, beacon)
        sensors.append((sensor_x, sensor_y, dist))

    for y in range(size + 1):
        if y % 1000 == 0:
            print(y)
        s = []
        for sensor_x, sensor_y, dist in sensors:
            diff_y = abs(sensor_y - y)
            if diff_y >= dist:
                continue
            dx = dist - diff_y
            start_x = max(0, min(sensor_x - dx, size + 1))
            end_x = max(0, min(sensor_x + dx + 1, size + 1))
            s.append((start_x, end_x))
        s = sorted(s, key=lambda tup: tup[0])
        end = s[0][1]
        for l, r in s[1:]:
            if l > end:
                return end, y
            if r > end:
                end = r

x, y = simulate()
print(x, y, x*4000000 + y)