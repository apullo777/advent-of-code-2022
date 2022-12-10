# divide each line into two halves, find shared char, and calculate the sum of priorites

with open('input.txt') as file:
    rucksacks = file.readlines()

def string_to_set(string):
    char_set = set()
    for char in string:
        char_set.add(char)
    return char_set

def common_characters(s1, s2):
    common_set = s1.intersection(s2)
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
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    first, second = string_to_set(rucksack[:mid]), string_to_set(rucksack[mid:])
    shared_type = common_characters(first, second)
    total += priorities(shared_type)

print(total)