# Part 2: find shared char among three lines and calculate the sum of priorities

with open('input.txt') as file:
    GROUP_NUM = 3
    rucksacks = file.read().split("\n")
    groups = []
    for i in range(0, len(rucksacks), GROUP_NUM):
        groups.append(rucksacks[i:i+GROUP_NUM])

def str_to_set(str):
    char_set = set()
    for char in str:
        char_set.add(char)
    return char_set

def set_to_str(set):
    s = ""
    for ele in set:
        s += str(ele)
    return s

def common_characters(strings):
    arr = []
    for s in strings:
        arr.append(str_to_set(s))
    mid = len(arr) // 2
    if len(arr) == 1: return arr[0]
    return common_characters(arr[:mid]) & common_characters(arr[mid:])

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
    shared_type = set_to_str(common_characters(group))
    total += priorities(shared_type)

print(total)