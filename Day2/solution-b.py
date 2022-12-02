# Part 2: calculate the total score with oppenents' shapes and outcomes

# read and parse
with open('input.txt') as file:
    rounds = file.readlines()

# X: LOSE, Y: DRAW, Z: WIN
# A: ROCK, B: PAPER, C: SCISSORS
round_score = {"X": 0, "Y": 3, "Z": 6}
shape_score = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1}
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
    score_of_round = 0
    opponent, outcome = one_round.strip().split(' ')
    total_score += shape_score[opponent][outcome] # the score for the shape we selected
    total_score += round_score[outcome] # the score for the outcome of the round

print(total_score)