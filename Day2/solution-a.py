# Part 1: calculate the total score with shapes of oppnents and players

# read and parse
with open('input.txt') as file:
    rounds = file.readlines()

# 1: ROCK, 2: PAPER, 3:SCISSORS
shape = {
"A": 1, "B": 2, "C": 3,
"X": 1, "Y": 2, "Z": 3
}

total_score = 0

def play_round(opponent, player):
    if shape[opponent] == shape[player]:
        return 3
    difference = shape[opponent] - shape[player]
    if (difference == -1 or difference == 2):
        return 6
    else: return 0

for one_round in rounds:
    opponent, player = one_round.strip().split(' ')
    total_score += shape[player] # the score for the shape we selected
    total_score += play_round(opponent, player) # the score for the outcome of the round

print(total_score)
