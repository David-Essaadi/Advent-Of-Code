import re

def distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

sensor_x, beacon_x = re.findall(r'(?<=x=)-*\d+', 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15')
sensor_y, beacon_y = re.findall(r'(?<=y=)-*\d+', 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15')
sensor = (sensor_x, sensor_y)
beacon = (beacon_x, beacon_y)