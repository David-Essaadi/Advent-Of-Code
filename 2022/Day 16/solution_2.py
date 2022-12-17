import re
from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Entity:
    location: str = 'AA'
    minutes_left: int = 26

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

distances = dict()

def init():
    tunnels, flows = parse_input(read_input())
    for valve in tunnels.keys():
        distances[valve] = find_distances(tunnels, flows, valve)

    # remove tunnels which have 0-flow valves
    for flow in flows:
        if flows[flow] == 0:
            for d in distances.values():
                del d[flow]

    return deque([(Entity(), Entity(), dict(), 0)]), flows

def find_moves(entity:Entity, opened: dict):
    moves = []
    for dest, dist in distances[entity.location].items():
        if not opened.get(entity.location) and dist < entity.minutes_left - 1:
            moves.append(dest)
    return moves

def open_valve(a:Entity, opened: dict):
    opened[a.location] = 1
    return Entity(a.location, a.minutes_left - 1), opened, flows[a.location] * a.minutes_left

def simulate(q, flows):
    max_flow = 0
    while q:
        me, elephant, opened, curr_flow = q.pop()
        print(me, elephant, opened, curr_flow)
        if curr_flow > max_flow:
            max_flow = curr_flow

        our_moves = find_moves(me, opened)
        elephant_moves = find_moves(elephant, opened)
        # option 0: we open the valve AND the elephant does nothing
        if flows[me.location] > 0 and me.minutes_left > 0:
            me_new, opened_new, added_flow = open_valve(me, opened.copy())
            q.appendleft(me_new, elephant, opened_new, curr_flow + added_flow)

        # option 1: the elephant opens the valve AND we do nothing
        if flows[elephant.location] > 0 and elephant.minutes_left > 0:
            elephant_new, opened_new, added_flow = open_valve(elephant, opened.copy())
            q.appendleft(me, elephant_new, opened_new, curr_flow + added_flow)

        # option 2: we open the valve AND the elephant moves to another valve
        if flows[me.location] > 0 and me.minutes_left > 0:
            for dest in elephant_moves:
                opened[me.location] = 1
                dist = distances[elephant.location][dest]
                if not opened.get(dest) and dist < elephant.minutes_left - 1:
                    q.appendleft(Entity(me.location, me.minutes_left - 1), Entity(dest, elephant.minutes_left - dist), opened.copy(), curr_flow + (me.minutes_left - 1) * flows[me.location])


        # option 3: the elephant opens the valve AND we move to another

        # option 4: we open NO valves AND BOTH move to another

        # option 5: we both open valves (only if we are at different valves)
        
    return max_flow

q, flows = init()
res = simulate(q, flows)
print(res)