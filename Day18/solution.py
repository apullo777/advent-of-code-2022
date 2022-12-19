from itertools import combinations 

array = []

with open("input.txt") as file:
    data = file.readlines()
    for line in data:
        x, y, z = line.split(",")
        array.append((int(x), int(y), int(z)))

def is_adjacent(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2) == 1

def count_surface(array):
    count = 0
    comb = combinations(array, 2)
    for pair in list(comb): 
        a, b = pair 
        if is_adjacent(a, b): 
            count +=1
    return len(array) * 6 - count * 2

print(count_surface(array))