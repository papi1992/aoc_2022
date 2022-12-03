top_n_calorie_carrier = 3

calorie_sums = []
with open("input.txt") as calories_file:
    current_total_calorie = 0
    for calorie in calories_file.readlines():
        if "\n" == calorie:
            calorie_sums.append(current_total_calorie)
            current_total_calorie = 0
            continue

        current_total_calorie += int(calorie.rstrip())

print(sum(sorted(calorie_sums)[-top_n_calorie_carrier:]))
