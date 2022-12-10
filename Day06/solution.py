with open('input.txt') as file:
    data = file.read().strip()

def check(start_index, signal, marker_len):
    if len(set(signal)) != len(signal):
        return 0
    return start_index + marker_len

def iterate(signal, marker_len):
    index = 0
    for i in range(len(signal) - marker_len + 1):
        index += check(i, signal[i:i+marker_len], marker_len)
        if index: break
    return index

print(iterate(data, 4)) # part 1: packet
print(iterate(data, 14)) # part 2: message