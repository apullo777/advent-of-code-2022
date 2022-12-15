from collections import defaultdict
from itertools import combinations
import re

def distance(sx, sy, bx, by):
    return abs(sx-bx) + abs(sy-by)

sensors = []
with open('input.txt') as file:
    data = file.readlines()
    for line in data:
        sx, sy, bx, by = map(int, re.findall(r"([\-\d]+)", line))
        sensors.append((sx, sy, bx, by, distance(sx, sy, bx, by)))

# Find the points on the periphery of the sensor
def periphery(sensor):
    points = set()
    
    # Helper function to search the area around the sensor
    def search_area(points, x, y):
        LOWER, UPPER = 0, 4000000
        if x >= LOWER and x <= UPPER and y >= LOWER and y <= UPPER:
            points.add((x, y))

    # return the list of points on the periphery of the sensor
    (sx, sy, _, _, dist) = sensor
    for i in range(dist+2):
        search_area(points, sx-dist-1+i, sy-i)
        search_area(points, sx+dist+1-i, sy-i)
        search_area(points, sx-dist-1+i, sy+i)
        search_area(points, sx+dist+1-i, sy+i)
    return points

# Check if a point is inside the coverage area of any sensor
def is_inside(sensors, x, y):
    for (sx, sy, _, _, dist) in sensors:
        if distance(sx, sy, x, y) <= dist:
            return True
    return False

# Find the gap in the sensor coverage
def find_gap(sensors):

    peripheries = {}
    # Store the peripheries of all sensors
    for sensor in sensors:
        peripheries[sensor] = periphery(sensor) 

    candidates = defaultdict(int)
    # Find the intersection of the peripheries of all sensors
    for s1, s2 in combinations(sensors, 2):
        p1, p2 = peripheries[s1], peripheries[s2]
        intersection = p1.intersection(p2)
        if intersection:
            for point in intersection:
                candidates[point] += 1

    # look for a point that is the intersection of the peripheries of as many sensors as possible.     
    # such a point would be the most likely to be a gap in the sensor coverage, 
    # since it would be the point where the least amount of sensors are providing coverage.
    for point in candidates:
        if candidates[point] >= 4:
            if not is_inside(sensors, *point):
                return point[0] * 4000000 + point[1]

    return 0  # If no suitable candidate is found, return 0

print(find_gap(sensors))