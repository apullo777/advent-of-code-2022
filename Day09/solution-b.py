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

def touch(tail, relative, direction):
    if relative == (0, 0):  # overlapping
        return tail

    # If the previous knot is moving in the same direction as the head,
    # the current knot moves one position in that direction as well.
    if relative == direction:
        return move(tail, direction)

    # If the previous knot is moving in the opposite direction of the head,
    # the current knot does not move.
    elif relative == (-direction[0], -direction[1]):
        return tail

    # If the previous knot is moving in a direction perpendicular to the direction of the head,
    # the current knot moves one position in the direction of the previous knot.
    elif relative[0] == 0 or relative[1] == 0:
        return move(tail, relative)

    # If the previous knot is moving in a diagonal direction with respect to the direction of the head,
    # the current knot moves one position in the direction of the previous knot if the direction of the head is also diagonal.
    # Otherwise, the current knot does not move.
    else:
        if abs(relative[0]) == abs(direction[0]):
            return move(tail, relative)
        else:
            return tail

def execute_instruction(positions, direction, times, visited):
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
        for i in range(1, len(positions)-1):
            relative = relative_position(prev_tail, positions[i+1]) # Calculate the relative position of the current knot from the perspective of the previous knot
            prev_head, prev_tail = prev_tail, positions[i+1]  # Update the previous head and tail
            positions[i+1] = touch(positions[i+1], relative, direction)
            direction = relative_position(positions[i+1], prev_tail)

        if positions[-1] not in visited:
            visited.append(positions[-1])

        print(positions)
        times -= 1
    return positions

# Part 2
visited_2 = []
positions = [[0, 0] for _ in range(10)]
for instruction in data:
    direction, times = instruction.strip().split(" ")
    positions = execute_instruction(positions, to[direction], int(times), visited_2)
print(len(visited_2))