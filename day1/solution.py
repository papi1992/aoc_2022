max_calorie = 0
with open("input.txt") as calories_file:

    current_max_calorie = 0
    for calorie in calories_file.readlines():
        if "\n" == calorie:
            if current_max_calorie > max_calorie:
                max_calorie = current_max_calorie
            
            current_max_calorie = 0
            continue

        current_max_calorie += int(calorie.rstrip())

print(max_calorie)
