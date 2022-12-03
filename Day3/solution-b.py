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
    array = []
    for string in strings:
        array.append(string_to_set(string))
    common_set = array[0] & array[1]
    for i in range(len(array) - 2):
        common_set = common_set & array[i+2]
    common_string = ""
    for ele in common_set:
        common_string += str(ele)
    return common_string

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