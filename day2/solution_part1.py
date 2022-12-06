shape_score_mapping = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
# A, X = Rock ; B, Y = Paper ; C, Z = Scissors
# Rock < Paper < Scissors < Rock
# Exceptional cases A(Rock)(1) > Z(Scissors)(3); C(Scissors)(3) < X(Rock)(1)

score = 0
exceptional_cases = ["A Z", "C X"]
with open("input.txt") as strategy_guide:
    for game_round in strategy_guide.readlines():
        game_round = game_round.strip()

        if game_round in exceptional_cases:
            if game_round == "A Z":
                score += 3

            if game_round == "C X":
                score += 7

        else:
            opponent_shape, my_shape = game_round.split(" ")
            opponent_shape_score, my_shape_score = shape_score_mapping[opponent_shape], shape_score_mapping[my_shape]

            if opponent_shape_score < my_shape_score:
                score += my_shape_score + 6
            
            if opponent_shape_score == my_shape_score:
                score += my_shape_score + 3

            if opponent_shape_score > my_shape_score:
                score += my_shape_score

print(score)
