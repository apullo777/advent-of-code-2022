with open('input.txt') as file:
    data = file.readlines()
    matrix = []
    for line in data:
        matrix.append(line.strip())

# Create a list of line_of_trees in each direction (up, down, right, left)
# relative to the specified position in the matrix
def create_lines_of_trees(row, col, matrix):
    tree = matrix[row][col]
    row_len, col_len = len(matrix), len(matrix[0])

    # Create a list of the trees to the right and left of the current tree
    right = list(matrix[row][col+1:])
    left = list(matrix[row][:col])
    
    # Create lists of the trees above and below the current tree
    up, down = [], []
    for i in range(row_len):
        if i < row: 
            up.append(matrix[i][col])
        if i > row:
            down.append(matrix[i][col])
    return [up, down, right, left]

# Check if the specified tree is visible (taller than all trees in each direction)
def is_visible(row, col, matrix):
    lines_of_trees = create_lines_of_trees(row, col, matrix)
    current_tree = matrix[row][col]

    # Check if the current tree is taller than all trees in the specified line of trees
    def is_tallest(current_tree, line_of_trees):
        for tree in line_of_trees:
            if int(current_tree) <= int(tree):
                return False
        return True

    # Check if the current tree is the tallest tree in each direction
    if (is_tallest(current_tree, lines_of_trees[0]) or  # up
        is_tallest(current_tree, lines_of_trees[1]) or  # down
        is_tallest(current_tree, lines_of_trees[2]) or  # right 
        is_tallest(current_tree, lines_of_trees[3])):   # left
        return True

    # If the current tree is not the tallest in any direction, return False
    return False

# Evaluate the scenic score of the specified tree x
# by counting the number of trees visible from perspective of x in each direction 
# and multiplying the counts together
def evaluate_score(row, col, matrix):
    lines_of_trees = create_lines_of_trees(row, col, matrix)

    # Count the number of trees visible from perspective of the specified tree
    def visible_trees(row, col, matrix, line_of_trees):
        count = 0 
        while line_of_trees:
            tree = line_of_trees.pop()
            if matrix[row][col] > tree:
               count += 1
            else: 
               count+= 1 
               break
        return count

    up = visible_trees(row, col, matrix, lines_of_trees[0])
    down = visible_trees(row, col, matrix, lines_of_trees[1][::-1])
    right = visible_trees(row, col, matrix, lines_of_trees[2][::-1])
    left = visible_trees(row, col, matrix, lines_of_trees[3])

    return up * down * right * left

# Part 1
count = len(matrix) * 2 + len(matrix[0]) * 2 - 4
for row in range(1, len(matrix)-1):
    for col in range(1, len(matrix[0])-1):
        if is_visible(row, col, matrix):
            count += 1
print(count)

# Part 2
scores = []
for row in range(1, len(matrix)):
    for col in range(1, len(matrix[0])):
        scores.append(evaluate_score(row, col, matrix))
print(max(scores))