with open('input.txt') as file:
    data = file.readlines()

def track_state(cycle, x_value, array):
    cycle += 1
    array.append(x_value)

def draw(cycle, array):
    x_val = array[cycle]
    sprite_pos = [x_val - 1, x_val, x_val + 1]
    # If the current pixel is within the sprite, return a "#, otherwise, return a "."
    if (cycle % 40) - 1 in sprite_pos: return "#"
    else: return "."

x, x_val, cycle = [], 1, 0
x.append(x_val)

for line in data:
    if line.strip() == "noop":
        track_state(cycle, x_val, array=x)
    else:
        instruction, value = line.strip().split(" ")
        track_state(cycle, x_val, array=x)
        track_state(cycle, x_val, array=x)
        x_val += int(value)

# Part 1
result = []
for i in range(20, 221, 40):
    result.append(x[i] * i)

print(sum(result))

# Part 2
i = 0
# Loop until the end of the list is reached
while i < len(x) - 1:
    row = ""
    # Loop through the next 40 values in the list of X register values
    for j in range(i+1, i+41):
        row += draw(j, x)  # Add the result of drawing the sprite on the screen to the current row
    print(row)
    i += 40