with open('input.txt') as file:
    data = file.read().strip()

def char_index(char):
    return ord(char) - ord("a")

def check(start_index, signal, marker_amount):
    frequencies = [0] * 26
    for char in signal:
        frequencies[char_index(char)] += 1
    
    nonzero_count = sum(1 for freq in frequencies if (freq != 0))

    if nonzero_count == marker_amount: 
        return start_index + marker_amount
    else: return 0

def iterate(signal, marker_amount):
    index = 0
    for i in range(len(signal)-3):
        index += check(i, signal[i:i+marker_amount], marker_amount)
        if index: break
    return index

print(iterate(data, 4)) # part 1
print(iterate(data, 14)) # part 2


