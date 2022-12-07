from string import ascii_letters


priorities_sum = 0
with open("input.txt") as rucksacks:
    for rucksack in rucksacks.readlines():
        rucksack = rucksack.rstrip()

        first_comparment = set(rucksack[:int(len(rucksack)/2)])
        second_comparment = set(rucksack[int(len(rucksack)/2):])

        error = first_comparment.intersection(second_comparment)
        priority = ascii_letters.index(next(iter(error))) + 1

        priorities_sum += priority


print(priorities_sum)
