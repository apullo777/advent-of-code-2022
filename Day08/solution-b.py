with open('input.txt') as file:
    data = file.readlines()

def evaluate(row, col, matrix):
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

    def visible_tree(row, col, line_of_trees, matrix):
        count = 0  # farthest one 
        while line_of_trees:
            tree = line_of_trees.pop()
            if matrix[row][col] > tree:
               count += 1
            else: 
               count+= 1 
               break
        return count

    up = visible_tree(row, col, north, matrix)
    down = visible_tree(row, col, south[::-1], matrix)
    right = visible_tree(row, col, east[::-1], matrix)
    left = visible_tree(row, col, west, matrix)

    return up * down * right * left


matrix = []
for line in data:
    matrix.append(line.strip())

# Part 2
scores = []
for row in range(1, len(matrix)):
    for col in range(1, len(matrix[0])):
        scores.append(evaluate(row, col, matrix))
print(max(scores))