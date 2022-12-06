shape_score_mapping = {"A": 1, "B": 2, "C": 3}
score_mapping = {"X": {"A": 3, "B": 1, "C": 2}, "Z": {"A": 8, "B": 9, "C": 7}}

# A = Rock ; B = Paper ; C = Scissors
# Rock < Paper < Scissors < Rock
# Exceptional cases A(Rock)(1) > Z(Scissors)(3); C(Scissors)(3) < X(Rock)(1)

score = 0
with open("input.txt") as strategy_guide:
    for game_round in strategy_guide.readlines():
        game_round = game_round.strip()

        opponent_shape, outcome_indicator = game_round.split(" ")

        if outcome_indicator != "Y":
            score += score_mapping[outcome_indicator][opponent_shape]
        else:
            score += shape_score_mapping[opponent_shape] + 3

print(score)
