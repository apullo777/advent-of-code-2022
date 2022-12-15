import re

with open('input.txt') as file:
    data = file.readlines()

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(int(x1)-int(x2)) + abs(int(y1)-int(y2))

def project(sensor, target, beacon):
    x, y, d = int(sensor['loc'][0]), int(sensor['loc'][1]), int(sensor['dis'])
    if y > target + d or y < target - d: return beacon
    else: 
        to_target = abs(y - target)
        return [x-d+to_target, x+d-to_target]

def sum_intervals(intervals):
    interval_lengths = []
    intervals.sort(key=lambda interval: interval[0])

    current_interval = intervals[0]

    for interval in intervals[1:]:
        # If the current interval overlaps with the next one, merge them
        if interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], interval[1])
        else:
        # If the current interval does not overlap with the next one, 
        # add its length to the list of interval lengths and start a new interval
            interval_lengths.append(current_interval[1] - current_interval[0])
            current_interval = interval

    interval_lengths.append(current_interval[1] - current_interval[0])

    return sum(interval_lengths)

sensors = []
for line in data:
    s, b = line.strip().split(":")
    s, b = re.findall(r"x=(-?\d+), y=(-?\d+)", s)[0], re.findall(r"x=(-?\d+), y=(-?\d+)", b)[0]
    sensor = {"loc": s, "dis": distance(s, b)}
    sensors.append(sensor)

intervals = []
for sensor in sensors:
    intervals.append(project(sensor, 2000000, [-208427, 2000000]))
print(sum_intervals(intervals))