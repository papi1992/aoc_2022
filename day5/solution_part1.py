import re


crate_pattern = "\[[a-zA-Z]\]"
moving_pattern = "move (\d+) from (\d+) to (\d+)"

with open("input.txt") as supply_info:
    first_line = supply_info.readline()
    crates_len = int(len(first_line[:-2]) / 3)
    crates_matrix = [[] for _ in range(crates_len)]

    supply_info.seek(0, 0)

    for supplies in supply_info:
        supplies = supplies.replace("\n", "")

        if re.search(crate_pattern, supplies):
            for i in range(crates_len):
                crate_start = 0 + i * 4
                crate_end = 3 + i * 4
                crate = supplies[crate_start: crate_end]

                if crate.startswith("["):
                    crates_matrix[i].insert(0, crate)

        elif supplies.startswith("move"):
            _move, _from, _to = re.search(moving_pattern, supplies).groups()
            _move, _from, _to = int(_move), int(_from) - 1, int(_to) - 1

            for _ in range(_move):
                crates_matrix[_to].append(crates_matrix[_from].pop())


final_word = ""
for crates in crates_matrix:
    if crates:
        final_word = final_word + crates[-1][1:2]

print(final_word)
