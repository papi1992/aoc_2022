from collections import defaultdict
import re

cd_pattern = "cd (.+)"
file_size_pattern = "(\d+) .+"
folders = defaultdict(list)
folder_path = []

with open("input.txt") as commands:
    for command in commands:
        command = command.rstrip()

        if command.startswith("$ cd"):
            folder = re.search(cd_pattern, command).groups()[0]

            if folder == "..":
                folder_path.pop()

            else:
                folder_path.append(folder)

        if command[0].isnumeric():
            file_size = re.search(file_size_pattern, command).groups()[0]

            for index, folder in enumerate(folder_path):
                current_path = "/".join(folder_path[:index + 1])
                folders[current_path].append(int(file_size))


for folder_path, content in folders.items():
    print(f"{folder_path} - {content} - {sum(content)}")

full_sum = 0
for list_of_files in folders.values():
    files_sum = sum(list_of_files)
    
    if sum(list_of_files) <= 100_000:
        full_sum += files_sum

print(full_sum)
