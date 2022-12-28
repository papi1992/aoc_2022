from typing import cast, List
from collections import defaultdict
from math import prod

rows = defaultdict(list)
columns = defaultdict(list)


with open("input.txt") as forest_grid:
    for row_index, forest_line in enumerate(forest_grid):
        forest_line = cast(str, forest_line)
        forest_line = forest_line.rstrip()

        for column_index, tree in enumerate(forest_line):
            columns[column_index].append(int(tree))
            rows[row_index].append(int(tree))


def _get_multiplier(trees: List[str], current_tree: int, reversed: bool = False) -> int:
    counter = 0

    if reversed:
        trees = trees[::-1]

    for neighborhood_tree in trees:
        if neighborhood_tree >= current_tree:
            counter += 1
            break
        
        counter += 1

    return counter


scenic_score = 0
for row_index, forest_line in rows.items():
    for column_index, tree in enumerate(forest_line):
        scenic_multipliers = []
        
        scenic_multipliers.append(_get_multiplier(forest_line[:column_index], tree, reversed=True))
        scenic_multipliers.append(_get_multiplier(forest_line[column_index + 1:], tree))
        scenic_multipliers.append(_get_multiplier(columns[column_index][:row_index], tree, reversed=True))
        scenic_multipliers.append(_get_multiplier(columns[column_index][row_index + 1:], tree))

        current_score = prod(scenic_multipliers)        
        if current_score > scenic_score:
            scenic_score = current_score
        

print(scenic_score)