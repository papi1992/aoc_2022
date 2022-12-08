from typing import Set


def _get_sections(section_start: str, section_end: str) -> Set[int]:
    return set(range(int(section_start), int(section_end) + 1))


pairs = 0
with open("input.txt") as sections:
    for pairs_sections in sections:
        pairs_sections = pairs_sections.rstrip()

        elf1, elf2 = pairs_sections.split(",")
        elf1_sections = _get_sections(*elf1.split("-"))
        elf2_sections = _get_sections(*elf2.split("-"))

        if not elf1_sections - elf2_sections:
            pairs += 1

        elif not elf2_sections - elf1_sections:
            pairs += 1
    

print(pairs)
