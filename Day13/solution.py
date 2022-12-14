import ast

with open('input.txt') as file:
    pairs = file.read().split("\n\n")

def compare_pairs(left, right):
    # If left or right is an integer, convert it to a list with a single value
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    # handle empty lists
    if isinstance(left, list) and (isinstance(right, list)):
        if not len(left) or not len(right): # either is empty list
            if len(left) > len(right): return False
            else: return True

    while left and right:
        # If both elements are integers, compare them directly
        if isinstance(left[0], int) and isinstance(right[0], int):
            if left[0] < right[0]:
                return True
            elif left[0] > right[0]:
                return False
        # Otherwise, compare them as packets
        else:
            if not compare_pairs(left[0], right[0]):
                return False
        
        # Move to the next element in both packets
        left = left[1:]
        right = right[1:]

    # If left has more elements, it's in the right order
    if left: return False
    # If right has more elements, it's not in the right order
    elif right: return True
    # Otherwise, they are the same
    else: return True

result = []
for i in range(len(pairs)):
    left, right = pairs[i].split("\n")
    left, right = ast.literal_eval(left), ast.literal_eval(right)
    if compare_pairs(left, right): result.append(i+1)

print(sum(result))