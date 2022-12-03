# Part 2: find shared char among three lines and calculate the sum of priorities

with open('input.txt') as file:
    GROUP_NUM = 3
    rucksacks = file.read().split("\n")
    groups = []
    for i in range(0, len(rucksacks), GROUP_NUM):
        groups.append(rucksacks[i:i+GROUP_NUM])

def string_to_set(string):
    char_set = set()
    for char in string:
        char_set.add(char)
    return char_set

def common_characters(strings):
    i = len(strings)
    common_set = common_characters((arrays[:i-1])) & string_to_set(arrays[i-1:]) 
    common_string = ""
    for ele in common_set:
        common_string += str(ele)
    return common_string

def common_characters(array):
    MAX_NUM = 58 # unicode A - z
    a1 = [True] * MAX_NUM # array recording common characters
    for i in range(len(array)):
        a2 = [False] * MAX_NUM # array recording what was seen in a string
        for j in range(len(array[i])): 
            if (a1[ord(array[i][j]) - ord("A")]):  # character seen before
                a2[ord(array[i][j]) - ord("A")] = True  # mark the character
        for k in range(MAX_NUM): # copy the second array to the first
            a1[k] = a2[k]
        
    for i in range(MAX_NUM): # return common characters
        if a1[i]:
            return chr(i + ord("A"))

def priorities(type):
    UPPER_CASE_NUM = 26
    LOWER_CASE_NUM = 26 + 5
    diff = ord(type) - ord("A")
    # a-z: 1-26, A-Z: 27-52
    if diff < UPPER_CASE_NUM: # upper case
        return diff + UPPER_CASE_NUM + 1
    else: return diff - LOWER_CASE_NUM # lower case

total = 0
for group in groups:
    shared_type = common_characters(group)
    total += priorities(shared_type)

print(total)