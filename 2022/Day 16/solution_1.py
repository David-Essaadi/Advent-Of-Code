import re
from collections import deque

def read_input():
    with open('input.txt') as file:
        return file.read().strip().splitlines()

def parse_input(lines):
    tunnels = dict()
    flows = dict()
    for line in lines:
        valve_from, *valves_to = re.findall(r'[A-Z]{2}', line)
        flow_rate = int(re.search(r'(?<=rate=)\d+', line).group(0))
        tunnels[valve_from] = valves_to
        flows[valve_from] = flow_rate
    return tunnels, flows

def find_distances(d:dict, flows, valve_from):
    distances = dict()
    q = deque()
    depth = 1
    for valve_to in d[valve_from]:
        q.appendleft((valve_to, depth))
    while q:
        valve_to, depth = q.pop()
        if not distances.get(valve_to):
            distances[valve_to] = depth
        for next_valve in d[valve_to]:
            if not distances.get(next_valve):
                q.appendleft((next_valve, depth + 1))
    return distances


tunnels, flows = parse_input(read_input())
distances = dict()
for valve in tunnels.keys():
    distances[valve] = find_distances(tunnels, flows, valve)

# remove tunnels which have 0-flow valves
for flow in flows:
    if flows[flow] == 0:
        for d in distances.values():
            del d[flow]

q = deque()
minutes_left = 30
max_flow = 0
q.appendleft(('AA', minutes_left, dict(), max_flow))

while q:
    valve, minutes_left, valves_opened, curr_flow = q.pop()
    if curr_flow > max_flow:
        max_flow = curr_flow
    # two options, either open the current valve OR go to another valve
    if minutes_left > 0:
        if not valves_opened.get(valve) and flows[valve] > 0:
            valves_opened[valve] = 1
            q.appendleft((valve, minutes_left - 1, valves_opened.copy(), curr_flow + (minutes_left - 1) * flows[valve]))
        for valve_to in distances[valve]:
            distance = distances[valve][valve_to]
            if not valves_opened.get(valve_to) and distance < minutes_left - 1:
                q.appendleft((valve_to, minutes_left - distance, valves_opened.copy(), curr_flow))
        
print(max_flow)