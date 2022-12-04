# Part 1: find how many pairs of intervals fully containing one another

with open('input.txt') as file:
    pairs = file.readlines()

def lower_bound(interval):
    return interval.split("-")[0]

def upper_bound(interval):
    return interval.split("-")[-1]

def is_different_sign(num1, num2):
    if num1 and num2:
        product = num1 * num2
        if product != abs(product):
            return True
    return False

def is_zero(x):
    if int(x) == 0:
        return True
    return False

def check_diff(interval_1, interval_2, mode):
    if mode == "parallel":
        diff_1 = int(lower_bound(interval_1)) - int(upper_bound(interval_2))
        diff_2 = int(lower_bound(interval_1)) - int(upper_bound(interval_2))
    if mode == "opposite":
        diff_1 = int(lower_bound(interval_1)) - int(upper_bound(interval_2))
        diff_2 = int(upper_bound(interval_1)) - int(lower_bound(interval_2))
        
    if is_different_sign(diff_1, diff_2): return False
    if (is_zero(diff_1) or is_zero(diff_2)): return False
    return True

def not_fully_contain(interval_1, interval_2):
    return check_diff(interval_1, interval_2, "parallel")

def not_paritailly_overlap(interval_1, interval_2):  
    return check_diff(interval_1, interval_2, "opposite")

no_overlap = 0
for pair in pairs:
    interval_1, interval_2 = pair.strip().split(",")
    if not_fully_contain(interval_1, interval_2):
        if not_paritailly_overlap(interval_1, interval_2):
            no_overlap += 1

overlap = len(pairs) - no_overlap

print(overlap)