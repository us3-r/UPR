# this file is not needed inside of the program but sometimes it does not run without it

import json

with open("default.json","r") as file:
    default_data = json.loads(file.read())

for i in default_data.values():
    # print(i)
    if i == "":
        print("empty")