from typing import cast
from collections import defaultdict

rows = defaultdict(list)
columns = defaultdict(list)


with open("input.txt") as forest_grid:
    for row_index, forest_line in enumerate(forest_grid):
        forest_line = cast(str, forest_line)
        forest_line = forest_line.rstrip()

        for column_index, tree in enumerate(forest_line):
            columns[column_index].append(int(tree))
            rows[row_index].append(int(tree))


forest_width = len(rows[0])
forest_height = len(columns[0])
visible_trees = 0
for row_index, forest_line in rows.items():
    for column_index, tree in enumerate(forest_line[1:-1]):
        column_index += 1

        if (
            row_index in (0, forest_height - 1) or
            max(forest_line[:column_index]) < tree or # row left
            max(forest_line[column_index + 1:]) < tree or # row right
            max(columns[column_index][:row_index]) < tree or # column above
            max(columns[column_index][row_index + 1:]) < tree # column below
        ):
            visible_trees += 1
            continue

print(visible_trees + forest_height * 2)