data = [s.strip() for s in open("input.txt").readlines()]
width, height = len(data[0]), len(data)

def get_char(square):
    return data[square[1]][square[0]]

def is_adj(s1, s2):
    return ord(get_char(s1)) <= ord(get_char(s2)) + 1

def get_and_replace_square(square, new_square):
    y = min([y for y in range(height) if square in data[y]])
    x = data[y].index(square)
    data[y] = data[y][:x] + new_square + data[y][x+1:]
    return (x, y)

def get_nbrs(square):
    nbrs = []
    (x, y) = square
    if x > 0 and is_adj(square, (x-1, y)):
        nbrs.append((x-1, y))
    if x < width - 1 and is_adj(square, (x+1, y)):
        nbrs.append((x+1, y))
    if y > 0 and is_adj(square, (x, y-1)):
        nbrs.append((x, y-1))
    if y < height - 1 and is_adj(square, (x, y+1)):
        nbrs.append((x, y+1))
    return nbrs 

def bfs(path, visited):
    new_path = []
    for square in path:
        for nbr in get_nbrs(square):
            if nbr not in path and nbr not in visited and nbr not in new_path:
                new_path.append(nbr)
        visited.append(square)
    return new_path

# Part 1:
(start_x, start_y) = get_and_replace_square('S', 'a')
(end_x, end_y) = get_and_replace_square('E', 'z')
path_1 = [(end_x, end_y)] # Find the path back to the starting point backwards from the end point
visited_1 = []
steps_1 = 0

while ((start_x, start_y) not in path_1): 
    steps_1 += 1
    path_1 = bfs(path_1, visited_1)

print(steps_1)

# Part 2:
path_2 = [(end_x, end_y)]
visited_2 = [] 
steps_2 = 0 

while ('a' not in [get_char(square) for square in path_2]): 
    steps_2 += 1
    path_2 = bfs(path_2, visited_2)

print(steps_2)