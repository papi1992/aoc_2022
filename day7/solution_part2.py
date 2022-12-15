from collections import defaultdict
import re

cd_pattern = "cd (.+)"
file_size_pattern = "(\d+) .+"
folders = defaultdict(list)
folder_path = []

total_disk_space = 70_000_000
needed_disk_space = 30_000_000

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


space_to_delete = needed_disk_space - (total_disk_space - sum(folders["/"]))
differences = []
for folder_path, content in folders.items():
    content_sum = sum(content)
    differences.append(
        {"folder_path": folder_path, "difference": content_sum - space_to_delete, "content_sum": content_sum}
    )

for difference in sorted(differences, key=lambda difference: difference["difference"]):
    if difference["difference"] >= 0:
        print(difference)
        break
