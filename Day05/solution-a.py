from string import ascii_uppercase
import copy

# Because we are reading the data from top to bottom. 
# we are using an array to represent a stack 
# with the first item of the array representing the top of the stack.
def prepare_stack(stacks):
    prepared_stacks = [[] for _ in range(9)]
    for row in stacks:
        for i in range(len(row)): # len(row) == 35
            if row[i] in ascii_uppercase: 
                prepared_stacks[i//4].append(row[i]) # each column consists of 4 items: ["[", "A", "]" " "]
    return prepared_stacks

def execute_step(step, stacks, mode):
    for step in steps.split('\n'):
        words = step.strip().split(' ')
        no, fr, to = int(words[1]), int(words[3]), int(words[5])

        if mode == '1': # CrateMover 9000
            for _ in range(no):
                stacks[to-1].insert(0, stacks[fr-1].pop(0))

        if mode == '2': # CrateMover 9001
            # We are first adding items to the bottom of the stack, rather than the top, 
            # in order to maintain the original order of the items
            for num in range(no-1, -1, -1): #  reversing the order in which we are moving the items
                stacks[to-1].insert(0, stacks[fr-1].pop(num))

    return ''.join(list(stack[0] for stack in stacks))            


with open('input.text') as file:
    stacks, steps = file.read().split('\n\n')

stacks = prepare_stack(stacks.split('\n'))

# Part 1
stacks_1 = copy.deepcopy(stacks)
print(execute_step(steps, stacks_1, '1'))

# Part 2
stacks_2 = copy.deepcopy(stacks)
print(execute_step(steps, stacks_2, '2'))