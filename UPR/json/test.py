import json
with open("AI.json","r") as file:
    AI_data = json.loads(file.read())

for i in AI_data:
    print(i)
    if i =="BLOCK TYPE":print("-----------------")

