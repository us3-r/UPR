import json

with open("default.json","r") as file:
    default_data = json.loads(file.read())

for i in default_data.values():
    # print(i)
    if i == "":
        print("empty")