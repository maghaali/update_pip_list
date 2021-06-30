#!/usr/bin/env python3
import re
import os


# pip outdated information, temp file
os.system("pip list --outdated > pip_outdated_list.txt")
with open("pip_outdated_list.txt") as file:
    outdated_list = file.read().splitlines()

# retrieve name of packages
final_list = []
for item in outdated_list[2:]:
    final_list += re.findall(r"^[a-zA-Z-_0-9]*", item)

# update one by one
with open("pip_outdated_list.txt", "a") as file:
    file.write("\nList of updated packages:\n")
    for item in final_list:
        file.write(item)
        os.system(f"python -m pip install --upgrade {item}")

# remove temp file
# os.system("del pip_outdated_list.txt")
