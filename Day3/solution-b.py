# Part 2: find shared char among three lines and calculate the sum of priorities

with open('input.txt') as file:
    rucksacks = file.read().split("\n")
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])

def common_characters(array):
    a1 = [True] * 58 # array recording common characters, unicode A - z
    for i in range(len(array)):
        a2 = [False] * 58 # array recording what was seen in a string
        for j in range(len(array[i])): 
            if (a1[ord(array[i][j]) - ord("A")]):  # character seen before
                a2[ord(array[i][j]) - ord("A")] = True  # mark the character
        for k in range(58): # copy the second array to the first
            a1[k] = a2[k]
        
    for i in range(58): # return common characters
        if a1[i]:
            return chr(i + ord("A"))

def priorities(type):
    priority = ord(type) - ord("A")
    if priority <= 25:
        return priority + 27
    else: return priority - 31

total = 0
for group in groups:
    shared_type = common_characters(group)
    total += priorities(shared_type)

print(total)





    



