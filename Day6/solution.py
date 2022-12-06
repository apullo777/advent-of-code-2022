with open('input.txt') as file:
    data = file.read().strip()

def check(start_index, signal, marker_amount):
    if len(set(signal)) != len(signal):
        return 0
    return start_index + marker_amount

def iterate(signal, marker_amount):
    index = 0
    for i in range(len(signal)-3):
        index += check(i, signal[i:i+marker_amount], marker_amount)
        if index: break
    return index

print(iterate(data, 4)) # part 1
print(iterate(data, 14)) # part 2