

with open('input.txt') as file:
    data = file.readlines()

def is_visible(row, col, matrix):
    tree = matrix[row][col]
    row_len, col_len = len(matrix), len(matrix[0])
    east = list(matrix[row][col+1:])
    west = list(matrix[row][:col])

    south, north = [], []
    for i in range(row_len):
        if i < row: 
            north.append(matrix[i][col])
        if i > row:
            south.append(matrix[i][col])

    def is_tallest(tree, subset):
        for element in subset:
            if int(tree) <= int(element):
                return False
        return True

    if (is_tallest(tree, north) or
        is_tallest(tree, south) or
        is_tallest(tree, east) or
        is_tallest(tree, west)):
        return True

    return False


matrix = []
for line in data:
    matrix.append(line.strip())

count = len(matrix) * 2 + len(matrix[0]) * 2 - 4
for row in range(1, len(matrix)-1):
    for col in range(1, len(matrix[0])-1):
        if is_visible(row, col, matrix):
            count += 1
print(count)
