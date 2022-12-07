from itertools import islice
from string import ascii_letters


priorities_sum = 0
with open("input.txt") as rucksacks: 
    while True:
        group = [set(elf.rstrip()) for elf in islice(rucksacks, 3)]
        if not group:
            break
        
        elf1, elf2, elf3 = group
        badge = next(iter(elf1.intersection(elf2).intersection(elf3)))
        priorities_sum += ascii_letters.index(badge) + 1


print(priorities_sum)
