# Part 1: find how many pairs of intervals overlapping

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

# There are three major cases of two intervals 
# 1. fully containing
# 2. partially overlaping
# 3. non-overlapping
# Since we already knew how to find case 1 in Part 1, our goal is to distinguish case 2 and 3
# In cases where full inclusion has been excluded, if a partial overlap occurs,
# regardless of whether one interval is on the left or right of the other, 
# the product of the differences between the upper and lower bounds of the two intervals
# should be different from its abosulte value (different sgin or zero)
# for example, considering both [(2, 4), (3, 5)] and [(3, 5), (2, 4)]
# the product of their differences are, respectively, (2-5)*(4-3) = -3 * 1 and (3-4)*(5-2) -1 * 3
# these differences having different sign means partial overlap
# we also need to consider cases like [(2, 4), (4, 6)] which also counts as overlapping (one difference is zero)
# excluding these then we have non-overlapping cases (case 3)

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