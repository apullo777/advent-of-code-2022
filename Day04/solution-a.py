# Part 1: find how many pairs of intervals fully containing one another

with open('input.txt') as file:
    pairs = file.readlines()

def lower_bound(interval):
    return interval.split("-")[0]

def upper_bound(interval):
    return interval.split("-")[-1]

def is_different_sign(num1, num2):
    product = num1 * num2
    if product != abs(product):
        return True
    return False

def is_zero(x):
    if int(x) == 0:
        return True
    return False

# For two intervals A and B
# A fully contains B when 
# (a) A.lower <= B.lower and 
# (b) A.upper >= B.upper 
# so we test the difference of their lower and upper bounds
# if the product != abs(product), the two values have different sign, meaning that one fully contain another
# we also need to check whether they equal at one end, ex. (2, 5) and (3, 5) also count as full inclusion

def is_fully_contain(interval_1, interval_2):
    lower_diff = int(lower_bound(interval_1)) - int(lower_bound(interval_2))
    upper_diff = int(upper_bound(interval_1)) - int(upper_bound(interval_2))
    if is_different_sign(lower_diff, upper_diff): return True
    if (is_zero(upper_diff) or is_zero(lower_diff)): return True
    return False

fully_contain = 0
for pair in pairs:
    interval_1, interval_2 = pair.strip().split(",")
    if (is_fully_contain(interval_1, interval_2)):
        fully_contain += 1 

print(fully_contain)