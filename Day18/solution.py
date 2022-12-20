from time import time_ns
from itertools import product, combinations 

def parse_input():
    cubes = set()
    MAX_X, MAX_Y, MAX_Z  = 0, 0, 0

    with open('input.txt') as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))
            cubes.add((x, y, z))
    return cubes

def count_exposed_surface(cubes):
    surface_areas = 6 * len(cubes)
    for cube in cubes:
        for direction in OFFSETS:
            if tuple(sum(x) for x in zip(cube, direction)) in cubes:
                surface_areas -= 1
    return surface_areas

def compute_neighbours(graph, offsets):
    neighbours = {}
    for node in graph:
        neighbours[node] = [tuple(sum(x) for x in zip(node, direction)) for direction in offsets]
    return neighbours

# bfs to return a list of nodes representing the shortest path from start to end, or an empty list if no such path exists
def bfs(graph, start, end, neighbours):
    queue = [[start]]
    visited = set()
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end: return path
        elif node not in visited:
            for neighbour in neighbours[node]:
                if neighbour in graph:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
            visited.add(node)


def part2(cubes, surface_area):
    MAX_X, MAX_Y, MAX_Z = [max(cubes, key=lambda x: x[i])[i] + 1 for i in range(3)]
    air = set(product(range(MAX_X), range(MAX_Y), range(MAX_Z))) - cubes
    air_neighbours = compute_neighbours(air, OFFSETS)
    trapped_air = [node for node in air if not bfs(air, node, (0, 0, 0), air_neighbours)]
    return surface_area - count_exposed_surface(trapped_air)
    
OFFSETS = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
cubes = parse_input()
cube_neighbours = compute_neighbours(cubes, OFFSETS)

start = time_ns()
print(f"Part 1: {count_exposed_surface(cubes)} in {(time_ns()-start)/1e6}ms")

surface_area = count_exposed_surface(cubes)

start = time_ns()
print(f"Part 2: {part2(cubes, surface_area)} in {(time_ns()-start)/1e6}ms")