import re
from collections import deque
from multiprocessing import Pool

class Blueprint:
    def __init__(self, ore, clay, obsidian, geode) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __repr__(self) -> str:
        return f'Blueprint ore: {self.ore}, clay: {self.clay}, obsidian: {self.obsidian}, geode: {self.geode}'

class Resources:
    def __init__(self, ore, clay, obsidian, geode) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __repr__(self) -> str:
        return f'Resources ore: {self.ore}, clay: {self.clay}, obsidian: {self.obsidian}, geode: {self.geode}'

    def add(self, other):
        return Resources(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)

def get_blueprints():
    with open('input.txt') as file:
        return file.read().strip().splitlines()

def parse_input():
    blueprints = []
    for blueprint in get_blueprints():
        lines = blueprint.split(':')[1].split('.')
        ore = int(re.search('\d+', lines[0]).group(0))
        clay = int(re.search('\d+', lines[1]).group(0))
        obsidian = tuple(map(int, re.findall('\d+', lines[2])))
        geode = tuple(map(int, re.findall('\d+', lines[3])))
        blueprints.append(Blueprint(ore, clay, obsidian, geode))
    return blueprints

def max_geodes(blueprint: Blueprint):
    print(blueprint)
    q = deque()
    q.appendleft((Resources(1, 0, 0, 0), Resources(0, 0, 0, 0), 0))
    max_geodes = dict()
    while q:
        robots, resources, time_left = q.pop()
        l = len(q)
        if time_left < 32:
            if max_geodes.get(time_left):
                if resources.geode + robots.geode < max_geodes.get(time_left):
                    continue

            # Geode robot, require ore and obsidian
            if resources.ore >= blueprint.geode[0] and resources.obsidian >= blueprint.geode[1]:
                new_robots = Resources(robots.ore, robots.clay, robots.obsidian, robots.geode + 1)
                new_resources = Resources(resources.ore - blueprint.geode[0], resources.clay, resources.obsidian - blueprint.geode[1], resources.geode).add(robots)
                q.append((new_robots, new_resources, time_left + 1))

            # Obsidian robot, require ore and clay
            elif resources.ore >= blueprint.obsidian[0] and resources.clay >= blueprint.obsidian[1]:
                new_robots = Resources(robots.ore, robots.clay, robots.obsidian + 1, robots.geode)
                new_resources = Resources(resources.ore - blueprint.obsidian[0], resources.clay - blueprint.obsidian[1], resources.obsidian, resources.geode).add(robots)
                q.append((new_robots, new_resources, time_left + 1))

            # Clay robot, requires ore
            if resources.ore >= blueprint.clay:
                new_robots = Resources(robots.ore, robots.clay + 1, robots.obsidian, robots.geode)
                new_resources = Resources(resources.ore - blueprint.clay, resources.clay, resources.obsidian, resources.geode).add(robots)
                q.append((new_robots, new_resources, time_left + 1))

            # Ore robot, requires ore
            if resources.ore >= blueprint.ore:
                new_robots = Resources(robots.ore + 1, robots.clay, robots.obsidian, robots.geode)
                new_resources = Resources(resources.ore - blueprint.ore, resources.clay, resources.obsidian, resources.geode).add(robots)
                q.append((new_robots, new_resources, time_left + 1))

            resources = robots.add(resources)
            max_geodes[time_left] = max(max_geodes.get(time_left, 0), resources.geode)
            if len(q) == l:
                q.appendleft((robots, resources, time_left + 1))
    return max_geodes[31]

if __name__ == '__main__':
    blueprints = parse_input()
    total = 1
    with Pool() as p:
        for m in p.map(max_geodes, blueprints[:3]):
            total *= m
    print(total)