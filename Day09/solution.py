with open('input.txt') as file:
    data = file.readlines()

# This function takes the head and tail positions and returns
# the relative position of the head from the perspective of the tail
# ex. (-1, -1) means head is bottom left to tail
def relative_position(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    return (x_diff, y_diff)

# using a dictionary to map each direction to a (x, y) vector
to = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}

# moves a point in a given direction by a given vector
def move(point, vector):
    x1, y1 = point    
    x2, y2 = vector
    x, y = x1 + x2, y1 + y2
    return [x, y]

def is_diagonal(vector):
    x, y = vector
    return (x and y)

def is_perpendicular(vector_1, vector_2):
    x1, y1 = vector_1
    x2, y2 = vector_2
    if (x1 and y1) and (x2 and y2):
        return (y1 / x1) * (y2 / x2) == -1
    else: 
        return (x1 * x2) == 0 and ( y1 * y2) == 0

def is_parallel(vector_1, vector_2):
    x1, y1 = vector_1
    x2, y2 = vector_2
    if (x1 and y1) and (x2 and y2):
        return (y1 / x1) == (y2 / x2)
    else: 
        return (not x1 and not x2) or (not y1 and not y2)

def find_45_adjacent(vector):
    x, y = vector

    if is_diagonal(vector):
        return [(x, 0), (0, y)]

    if not is_diagonal(vector) and vector != (0, 0):
        if not x: return [(1, y), (-1, y)]
        if not y: return [(x, 1), (x, -1)]

def touch(tail, relative, direction):
    if relative == (0, 0):  # head and tail are overlapping
        return tail

    elif is_diagonal(relative):  # head and tail are in diagonal position
        if (direction == relative or 
            direction in find_45_adjacent(relative)):
            return move(tail, relative)

        if relative == (-direction[0], direction[1]):
            return move(tail, relative[1])

        if relative == (direction[0], -direction[1]):
            return move(tail, relative[0])

    # head is on the same row or column as tail
    else:
        if direction == relative:
            return move(tail, direction)
        if direction in find_45_adjacent(relative):
            return move(tail, relative)
        else: return tail


def execute_instruction(positions, direction, times, visited, mode):
    # Repeat the movement of the rope for the given number of times
    while times >= 1:
        # moving head and first knot
        prev_head, prev_tail = positions[0], positions[1]  # Store the previous head and tail positions

        relative = relative_position(positions[0], positions[1])
        positions[0] = move(positions[0], direction)  # Update the head position by moving it in the given direction
        positions[1] = touch(positions[1], relative, direction) # Update the first knot position using the touch function

        # Set the direction of movement to the relative position of the first knot
        direction = relative_position(positions[1], prev_tail) 
        # Iterate over the other knots (knots 2 to 9)
        for i in range(1, len(positions)-2):
            relative = relative_position(prev_tail, positions[i+1]) # Calculate the relative position of the current knot from the perspective of the previous knot
            prev_head, prev_tail = prev_tail, positions[i+1]  # Update the previous head and tail
            positions[i+1] = touch(positions[i+1], relative, direction)
            direction = relative_position(positions[i+1], prev_tail)

        if positions[-1] not in visited:
            visited.append(positions[-1])

        times -= 1
    return positions

# Part 1
visited_1 = []
pair = [[0, 0], [0, 0]]
for instruction in data:
    direction, times = instruction.strip().split(" ")
    pair[0], pair[1] = execute_instruction(pair, to[direction], int(times), visited_1, mode='1')
print(len(visited_1))

# Part 2
visited_2 = []
positions = [[0, 0] for _ in range(10)]
for instruction in data:
    direction, times = instruction.strip().split(" ")
    positions = execute_instruction(positions, to[direction], int(times), visited_2, mode='2')
print(len(visited_2))