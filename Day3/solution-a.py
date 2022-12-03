# divide each line into two halves, find shared char, and calculate the sum of priorites

with open('input.txt') as file:
    rucksacks = file.readlines()

def find_duplicate(s1, s2):
    d = {}
    for char in s1:  # count frequency
        if char in d:
            d[char] += 1
        else: 
            d[char] = 1

    for char in s2:
        if char in d:
            return char

def priorities(type):
    priority = ord(type) - ord("A")
    if priority <= 25:
        return priority + 27
    else: return priority - 31

total = 0
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    first, second = rucksack[:mid], rucksack[mid:]
    shared_type = find_duplicate(first, second)
    total += priorities(shared_type)

print(total)


    





 






