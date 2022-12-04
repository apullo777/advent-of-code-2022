# Part 2: find how many pairs of overlapped intervals


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

def is_zero(num):
    if num == 0:
        return True
    return False

def not_fully_contain(interval_1, interval_2):
    lower_diff = int(lower_bound(interval_1)) - int(lower_bound(interval_2))
    upper_diff = int(upper_bound(interval_1)) - int(upper_bound(interval_2))
    if is_different_sign(lower_diff, upper_diff): return False
    if (is_zero(upper_diff) or is_zero(lower_diff)): return False
    return True

def not_paritailly_overlap(interval_1, interval_2):
    if lower_bound(interval_1) > lower_bound(interval_2):
        interval_1, interval_2 = interval_2, interval_1   # assume intervel_1 is smaller than interval_2
    if upper_bound(interval_1) >= lower_bound(interval_2):
        return False
    return True

no_overlap = 0

for pair in pairs:
    interval_1, interval_2 = pair.strip().split(",")
    if not_fully_contain(interval_1, interval_2):
        if not_paritailly_overlap(interval_1, interval_2):
            no_overlap +=1

overlap = len(pairs) - no_overlap

print(overlap)