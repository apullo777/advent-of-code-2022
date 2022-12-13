import math

with open('input.txt') as file:
    data = file.read().split("\n\n")

# Parse instructions for each monkey
monkeys = []
for monkey in data:
    lines =  monkey.split("\n")

    starting_items_line = lines[1].strip().split(": ")[1]
    starting_items = [int(x) for x in starting_items_line.split(",")]

    operation_line = lines[2].strip()
    operation = operation_line.split("=")[1].strip()

    test_line = lines[3].strip()
    modulo = test_line.split("by")[1].strip()

    true_branch_line = lines[4].strip()
    true_branch = int(true_branch_line.split(" ")[-1])

    false_branch_line = lines[5].strip()
    false_branch = int(false_branch_line.split(" ")[-1])

    monkey = {
        "items": starting_items,
        "do": operation,
        "mod": int(modulo),
        "true": int(true_branch),
        "false": int(false_branch),
        "count": 0
    }
    monkeys.append(monkey)

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}

def do_parser(do, item):
    operand_1, operator, operand_2 = do.strip().split(" ")
    if operand_2.isnumeric():
        return op[operator](int(item), int(operand_2))
    if operand_2 == 'old':
        return op[operator](int(item), int(item))

def throw_item(monkeys, item, index):
    monkeys[index]['items'].append(item)

def play_round(monkeys):
    for i in range(len(monkeys)):
        while(monkeys[i]['items']):
            monkeys[i]['count'] += 1
            monkeys[i]['items'][0] = do_parser(monkeys[i]['do'], monkeys[i]['items'][0]) // 3
            if monkeys[i]['items'][0] % monkeys[i]['mod']:
                throw_item(monkeys, monkeys[i]['items'].pop(0), monkeys[i]['false'])
            else: 
                throw_item(monkeys, monkeys[i]['items'].pop(0), monkeys[i]['true'])

# Part 1:
for _ in range(20):
    item = []
    play_round(monkeys)
    for monkey in monkeys:
        item.append(monkey['items'])

result_1 = []
for monkey in monkeys:
    result_1.append(monkey['count'])

print(math.prod(sorted(result_1)[-2:]))