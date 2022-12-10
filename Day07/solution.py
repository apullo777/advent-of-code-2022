import re
import copy

def filesystem_parser(data):
    GO_DOWN = "cd ([A-Za-z0-9]+)"
    GO_UP = "cd \.\."
    FILE_SIZE = "([0-9]+) (?:[A-Za-z0-9]+)"
    
    size_dict = {}         # use a dict to store file sizes, with file paths as keys
    current_path = [""]     # current path represented as a list of folder names

    for line in data:
        if re.search(GO_DOWN, line):
            current_path.append(re.findall(GO_DOWN, line)[0])

        if re.search(GO_UP, line):
           current_path.pop()

        if re.search(FILE_SIZE, line):
            size = int(re.findall(FILE_SIZE, line)[0])
            path = ""
            for folder in current_path:   # add file size to each of its root folders
                path += "/" + folder
                if not path in size_dict:
                    size_dict[path] = 0
                size_dict[path] += size

    return size_dict


with open('input.txt') as file:
    data = file.readlines()
file_size_dict = filesystem_parser(data)
size_list = map(lambda path: file_size_dict[path], file_size_dict)


# Part 1: 
MAX_SIZE = 100000
size_list_1 = copy.deepcopy(size_list)
print(sum(filter(lambda size: size <= MAX_SIZE, size_list_1)))

# Part 2:
MIN_DELETE_SPACE = (30000000 + file_size_dict["/"]) - 70000000 
size_list_2 = copy.deepcopy(size_list)
print(min(list(filter(lambda size: MIN_DELETE_SPACE < size, size_list_2))))