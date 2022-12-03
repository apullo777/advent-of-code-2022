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
    common_string =""
    for ele in common_set:
        common_string += str(ele)
    return common_string

def priorities(type):
    priority = ord(type) - ord("A")
    if priority <= 25:
        return priority + 27
    else: return priority - 31

total = 0
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    first, second = string_to_set(rucksack[:mid]), string_to_set(rucksack[mid:])
    shared_type = common_characters(first, second)
    total += priorities(shared_type)

print(total)



    





 






