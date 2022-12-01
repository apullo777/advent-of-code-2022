with open ('input.txt') as file:
    calories = file.read().strip()

# 1a: find the amount of the largest
res = []
for calories_by_elf in calories.split("\n\n"):
    total = 0
    for calories_by_item in calories_by_elf.split("\n"):
        total += int(calories_by_item)
    res.append(total)
res = sorted(res) 
print(res[-1])

#1b: find the sum of the top three
print(sum(res[-3:]))