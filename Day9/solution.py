with open('input.txt') as file:
    data = file.readlines()

# relative positon from view of tail point
# ex. (-1, -1) means head is bottom left to tail
def relative_position(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    return (x_diff, y_diff)

to = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}

def move(point, vector):
    x1, y1 = point    
    x2, y2 = vector
    x, y = x1 + x2, y1 + y2
    return [x, y]

def touch(tail, relative, direction):
    if relative == (0, 0):  # overlapping
        return tail
    if not relative[0] or not relative[1]: # on the same row or column
        if relative == to[direction]: 
            return move(tail, to[direction]) # if head is moving the same firection as relative position
        else : return tail
    # on diagonal direction
    else:
        if (relative[0] == to[direction][0] or relative[1] == to[direction][1]):
            return move(tail, relative)
        else: return tail

def execute_instruction(positions, direction, times, visited):
    while times >= 1:
        for i in range(len(positions)-1):
            relative = relative_position(positions[i], positions[i+1])
            positions[i] = move(positions[i], to[direction])
            positions[i+1] = touch(positions[i+1], relative, direction)
        if positions[-1] not in visited:
            visited.append(positions[i+1])
        print(positions)
        times -= 1
    return positions

# Part 1
visited_1 = []
pair = [[0, 0], [0, 0]]
for instruction in data:
    direction, times = instruction.strip().split(" ")
    pair[0], pair[1] = execute_instruction(pair, direction, int(times), visited_1)
print(len(visited_1))
