#!/usr/bin/env python3
import re
import os


# pip outdated information, temp file
os.system("pip list --outdated > pip_outdated_list.txt")
with open("pip_outdated_list.txt") as file:
    outdated_list = file.read().splitlines()

# remove temp file
os.system("del pip_outdated_list.txt")

# retrieve name of packages
final_list = []
for item in outdated_list[2:]:
    final_list += re.findall(r"^[a-zA-Z-]*", item)

# update one by one
for item in final_list:
    os.system(f"python -m pip install --upgrade {item}")
